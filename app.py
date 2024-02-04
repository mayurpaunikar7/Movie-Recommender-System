import pandas as pd
import pickle
import streamlit as st
import requests
import time


def fetch_poster(movie_id, max_retries=3, delay_between_retries=1):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=91f221dfa2d5d92cb743bd48400de8b1".format(movie_id)

    for attempt in range(max_retries):
        try:
            data = requests.get(url)
            data.raise_for_status()  # Raise an error for bad responses
            data = data.json()
            poster_path = data['poster_path']
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        except requests.RequestException as e:
            print(f"Error fetching data (Attempt {attempt + 1}/{max_retries}): {e}")
            time.sleep(delay_between_retries)

    # If all retries fail, raise the last encountered exception
    raise None


def movie_reccomendation(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


st.title('Movie Recommender System')
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

Selected_Movie_Name = st.selectbox(
    'Select Movie',
    movies['title'].values)


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = movie_reccomendation(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5, gap="medium")
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

