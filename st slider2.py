import streamlit as st
from datetime import time, datetime

st.header('범위 슬라이더')

values=st.slider(
    '값의 범위를 선택하세요',
    0.0,100.0,(25.0,75.0))
st.write('값:', values)