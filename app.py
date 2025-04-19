import streamlit as st
import pandas as pd
import pickle
import requests

movies_dict = pickle.load(open('movies_imdb.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    api_key = '1fe5ffb0'
    url = f"http://www.omdbapi.com/?i={movie_id}&apikey={api_key}"
    response = requests.get(url)

    data = response.json()
    
    try:
        poster_link = data['Poster']
    except:
        poster_link = "https://raw.githubusercontent.com/rahul5r/Movie-Recommendation-System/refs/heads/main/dataset/no_poster.png"
    
    return poster_link

    

def recomend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
    recomended_movies = []
    recomended_movie_posters = []
    
    for i in movie_list:
        imdb_id = movies.iloc[i[0]].id_imdb
        recomended_movies.append(movies.iloc[i[0]].title)
        recomended_movie_posters.append(fetch_poster(imdb_id))
    
    
    return recomended_movies, recomended_movie_posters
    



st.title('Movie Recomendation System')

selected_movie = st.selectbox(
    "Which move have you watched Recently?",
    movies['title'],
    index=None,
    placeholder="Enter a movie name...",
)

if st.button("Recomend"):
    recomended_movies, recomended_movie_posters = recomend(selected_movie)
    coll, col2, col3, col4, col5 = st.columns(5)
    with coll:
        st.text(recomended_movies[0])
        st.image(recomended_movie_posters[0])
    with col2:
        st.text(recomended_movies[1])
        st.image(recomended_movie_posters[1])
    with col3:
        st.text(recomended_movies[2])
        st.image(recomended_movie_posters[2])
    with col4:
        st.text(recomended_movies[3])
        st.image(recomended_movie_posters[3])
    with col5:
        st.text(recomended_movies[4])
        st.image(recomended_movie_posters[4])
    