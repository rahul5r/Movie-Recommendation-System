import streamlit as st
import pandas as pd
import pickle


movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recomend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
    simiar_movies = [movies.iloc[i[0]].title for i in movie_list]
    
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