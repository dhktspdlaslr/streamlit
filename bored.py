import streamlit as st
import requests

# Title
st.title('🏀 Bored API 앱')

# Sidebar 입력
st.sidebar.header('입력')
selected_type = st.sidebar.selectbox(
    '활동 유형 선택',
    ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
)

# 올바른 API URL
base_url = "https://www.boredapi.com/api/activity"
suggested_activity_url = f"{base_url}?type={selected_type}"

# URL 확인
st.write(f"API 요청 URL: {suggested_activity_url}")

try:
    # API 요청
    response = requests.get(suggested_activity_url)
    response.raise_for_status()  # HTTP 에러 확인
    suggested_activity = response.json()  # JSON 변환

    # 정상적인 응답
    st.header('제안된 활동')
    st.info(suggested_activity['activity'])

    # 활동 상세 정보
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label='참가자 수', value=suggested_activity['participants'], delta='')
    with col2:
        st.metric(label='활동 유형', value=suggested_activity['type'].capitalize(), delta='')
    with col3:
        st.metric(label='가격', value=suggested_activity['price'], delta='')

except requests.exceptions.RequestException as e:
    # 요청/네트워크 오류 메시지
    st.error(f"API 요청에 실패했습니다. URL을 확인하거나 네트워크 상태를 점검하세요: {e}")
except (KeyError, ValueError) as e:
    # JSON 처리 오류 메시지
    st.error("API에서 올바르지 않은 데이터를 받았습니다. API 서버 상태를 확인하세요.")