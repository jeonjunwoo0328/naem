import streamlit as st
from openai import OpenAI

ai_client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def create_quiz(field, level):

    response = ai_client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {
                "role": "system",
                "content": """

                너는 교수이다.
                너는 신소재공학 진학에 도움이 되는 문제를 만든다

                이 형식으로 만든다

                (문제)
                문제 내용

                (정답)
                답

                (해설)
                해설
                """
                },
                ]
    )

    st.title("🧪 Material Quiz AI")
st.subheader("AI 신소재공학 퀴즈 생성기")

st.write(
    """
    신소재공학 전공 분야별 문제를 AI가 생성합니다.
    시험 공부와 전공 복습에 활용하세요.
    """
)


field = st.selectbox("분야 선택", [ "배터리 소재",  "배터리 소재",  "금속 재료", "고분자 소재", "세라믹 소재"])
    
level = st.selectbox("난이도 선택", ["기초", "심화", "전문가"])
if st.button("문제 만들기"):
 with st.spinner("문제를 만드는 중..."): 
  quiz = create_quiz(field,level)
 st.success("문제 생성 완료")
 st.markdown(quiz)


            
        

               

