import streamlit as st
from datetime import time, datetime

st.header('st.slider')

st.subheader('시간 범위 슬라이더')

appointment = st.slider(
     "약속을 예약하세요:",
     value=(time(11, 30), time(12, 45)))
st.write("예약된 시간:", appointment)