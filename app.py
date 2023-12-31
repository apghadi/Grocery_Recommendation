import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from predict_page import add_bg_from_local

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    add_bg_from_local('img2.jpg') 
    show_predict_page()
else:
    show_explore_page()