import streamlit as st
from openai import OpenAI

# OpenAI 연결
ai_client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)


# ---------------------------
# AI 분석 함수
# ---------------------------
def analyze_paper(text):

    response = ai_client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {
                "role": "system",
                "content": """
                너는 신소재공학 전문 연구 조교이다.
                사용자가 입력한 논문 내용을 분석한다.

                반드시 아래 순서로 답변한다.

                1. 논문 내용 요약
                2. 연구 목적
                3. 사용된 소재 및 기술
                4. 주요 결과
                5. 핵심 전공 영어 단어
                6. 어려운 문장 설명
                """
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content



# ---------------------------
# Streamlit 화면
# ---------------------------

st.title("🧪 Material AI Lab")
st.subheader("AI 신소재 논문 분석 도우미")

st.write(
    """
    신소재공학 논문(Abstract)을 입력하면
    AI가 연구 내용을 분석하고 전공 영어 학습을 도와줍니다.
    """
)


paper = st.text_area(
    "📄 논문 Abstract를 입력하세요",
    height=300,
    placeholder=
    """
    Example:
    Lithium-ion batteries have attracted significant attention...
    """
)


if st.button("🔍 논문 분석하기"):

    if paper.strip() == "":
        st.warning("논문 내용을 입력해주세요.")

    else:
        with st.spinner("AI가 논문을 분석 중입니다..."):

            result = analyze_paper(paper)

        st.success("분석 완료!")

        st.markdown(result)



# ---------------------------
# 추가 질문 기능
# ---------------------------

st.divider()

st.subheader("💬 논문 내용 질문하기")


question = st.chat_input(
    "예: 이 논문의 핵심 소재는 무엇인가요?"
)


if question:

    response = ai_client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {
                "role": "system",
                "content":
                "너는 신소재공학 논문을 설명하는 전문 연구원이다."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    st.chat_message("assistant").write(
        response.choices[0].message.content
    )
