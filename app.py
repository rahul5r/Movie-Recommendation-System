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
        poster_link = None

    

def recomend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
    simiar_movies = []
    movie_posters = []
    
    for i in movie_list:
        simiar_movies.append(movies.iloc[i[0]].title)
        simiar_movies.append(movies.iloc[i[0]].id_imdb)
    
    
    return simiar_movies
    



st.title('Movie Recomendation System')

selected_movie = st.selectbox(
    "Which move have you watched Recently?",
    movies['title'],
    index=None,
    placeholder="Enter a movie name...",
)

if st.button("Recomend"):
    recomended_movies = recomend(selected_movie)
    st.write(recomended_movies)