import streamlit as st
from datetime import time, datetime

st.header('st.slider')

st.subheader('날짜 및 슬라이더')

start_time=st.slider(
    "언제 시작하시겠습니까?",
    value=datetime(2020,1,1,9,30),
    format="MM/DD/YY - hh:mm")
st.write("시작 시간:", start_time)