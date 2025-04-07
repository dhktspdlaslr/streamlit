import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

# Streamlit 앱 제목
st.title("Data Profiling with `ydata-profiling`")

# 데이터 로드 (예제 데이터: Penguins 데이터셋 사용)
DATA_URL = "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"
df = pd.read_csv(DATA_URL)

# 데이터프레임 표시
st.write("### Input DataFrame")
st.dataframe(df)

# 프로파일링 보고서 생성
profile = ProfileReport(df, explorative=True)

# 프로파일링 보고서를 Streamlit에 HTML로 표시
st.write("### Profiling Report")
st.components.v1.html(profile.to_html(), height=1000, scrolling=True)