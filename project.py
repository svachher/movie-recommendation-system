import streamlit as st
import pickle
import pandas as pd
import requests



# HTML and CSS for title alignment
title_html = """
<style>
.centered-title {
    text-align: center;
}
</style>
<h1 class="centered-title">CineMate: Tailored Movie Recommendations for Every Viewer!</h1>
"""

# Display the HTML
st.markdown(title_html, unsafe_allow_html=True)

# Add your Streamlit content here
st.write("Welcome to CineMate! Discover movies you'll love.")


movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movie_dict)
#st.title('CineMate: Personalized Movie Recommendations')
similarity= pickle.load(open('similarity.pkl','rb'))





def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
##    recommended_movies_posters = []

    for i in movies_list:
      #  movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
     ##   recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies

selected_movie_name= st.selectbox(
    'how would you', movies['title'].values)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)




