import pickle
import streamlit as st
import requests

st.set_page_config(page_title='Book Recommendation')


def recommend(book):
    index = books[books['Title'] == book].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_book_names = []

    for i in distances[1:6]:
        recommended_book_names.append(books.iloc[i[0]].Title)
    return recommended_book_names


st.header('Book Recommendation System')
books = pickle.load(open('book_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

book_list = books['Title'].values
selected_book = st.selectbox(
    "Type or select a book from the dropdown", book_list )

if st.button('Show Recommendation'):
    recommended_book_names = recommend(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_book_names[0])

    with col2:
        st.text(recommended_book_names[1])


    with col3:
        st.text(recommended_book_names[2])


    with col4:
        st.text(recommended_book_names[3])


    with col5:
        st.text(recommended_book_names[4])

