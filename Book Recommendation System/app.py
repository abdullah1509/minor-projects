import pickle
import streamlit as st
import requests

st.set_page_config(page_title='Book Recommendation')
st.sidebar.title('ABDULLAH')
st.sidebar.image('pic.png')
st.sidebar.write('[RESUME](https://drive.google.com/file/d/1tMY5tE94UXsAq22qSUHwPaMAxbnNr1WV/view?usp=sharing)')
st.sidebar.write('[LINKEDIN](https://www.linkedin.com/in/abdullah-3008a7b6/)')
st.sidebar.write('[GITHUB](https://github.com/abdullah1509)')
st.sidebar.write('[HACKERRANK](https://www.hackerrank.com/mdabdullah1509)')


def recommend(movie):
    index = books[books['Title'] == books].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_book_names = []

    for i in distances[1:6]:
        # fetch the movie poster

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

