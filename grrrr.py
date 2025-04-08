import streamlit as st
from groq import Groq
import re  # 정규식을 사용하기 위한 라이브러리

# Streamlit UI 시작
st.title('Groq API를 이용한 Chat bot')

# 사이드바에 API 키 입력 필드 추가
st.sidebar.header("설정")
api_key = st.sidebar.text_input("API 키를 입력해주세요:", type="password", key="api_key")

# API 키 확인
if not api_key:
    st.warning("API 키가 입력되지 않았습니다. 사이드바에 API 키를 입력해주세요.")
    st.stop()

# Groq 클라이언트 초기화
try:
    client = Groq(api_key=api_key)  # 입력받은 API 키 사용
except Exception as e:
    st.error(f"API 키가 유효하지 않습니다. 오류: {str(e)}")
    st.stop()

# API 응답 처리 함수
def get_response(question):
    """Groq API로부터 응답을 처리하는 함수"""
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": question}],
        model="qwen-qwq-32b",
    )
    full_response = chat_completion.choices[0].message.content

    # <think> 태그 제거
    clean_response = re.sub(r"<think>.*?</think>", "", full_response, flags=re.DOTALL).strip()

    return clean_response

# 사용자 입력 필드
question = st.text_input("질문을 입력해주세요:", key="question")

# 버튼 클릭 시 응답 생성
if st.button('회신'):
    if not api_key:
        st.error("API 키가 입력되지 않았습니다. 질문을 하기 위해서는 API 키를 입력해주세요!")
    elif not question:
        st.warning("질문을 입력해주세요.")
    else:
        with st.spinner('회신 중...'):
            try:
                response = get_response(question)

                # 사용자에게 수정된 응답 표시
                st.write(f"**응답:** {response}")  
            except Exception as e:
                st.error(f"오류 발생: {str(e)}")
