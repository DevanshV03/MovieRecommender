import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=3721858efb595d92952ef9f638ef84e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movie_posters = []
    recommended_movie_names = []

    for i in distances[1:6]:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies_list.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.title(':blue[Movie] Recommender System :popcorn:')
st.divider()
st.write('Select A movie and click the recommend button to get similar movies to binge on!')
similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = movies_list['title'].values
option = st.selectbox(
    "What did you watch?",
    movies,
    placeholder="Select a movie...",
)

st.write("Displaying similar Movies to: ", option)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
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