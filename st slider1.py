import streamlit as st
from datetime import time, datetime

st.header('st.slider')

st.subheader('Slider')

age=st.slider('당신의 나이는?', 0, 130, 25)
st.write("나는 ", age, '살입니다.')