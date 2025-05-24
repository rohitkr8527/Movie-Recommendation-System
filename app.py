import streamlit as st
import pickle
import pandas as pd
import requests

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB API Key
API_KEY = '2e882a18b38e42ef8eb79b2dbaad95dd'

# Fetch poster from TMDB
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url).json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Recommendation logic
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# Page settings
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/942/942748.png", width=100)
st.sidebar.title("Movie Recommender 🎥")
st.sidebar.markdown("Select a movie from the dropdown and get similar movie recommendations with posters.")

# Header
st.markdown("""
    <style>
        .main-title {
            font-size: 3em;
            text-align: center;
            padding: 10px;
            background: linear-gradient(to right, #ff512f, #dd2476);
            color: white;
            border-radius: 12px;
            margin-bottom: 30px;
        }
        .movie-card {
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
    </style>
    <div class="main-title">🎬 Movie Recommender</div>
""", unsafe_allow_html=True)

# Dropdown
selected_movie = st.selectbox("📽️ Choose a movie you like:", movies['title'].values)

# Recommendation trigger
if st.button("🔍 Recommend"):
    with st.spinner("Finding awesome picks for you..."):
        names, posters = recommend(selected_movie)

    st.markdown("## ✨ Top Recommendations")
    st.markdown("<br>", unsafe_allow_html=True)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(f"""
                <div class="movie-card">
                    <img src="{posters[i]}" width="100%" style="border-radius:10px;">
                    <p><strong>{names[i]}</strong></p>
                </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center; color: gray; font-size: 14px;'>
        Built with ❤️ by Rohit 
    </div>
""", unsafe_allow_html=True)
