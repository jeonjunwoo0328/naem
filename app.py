import streamlit as st
from openai import OpenAI

# OpenAI 연결
ai_client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)


# ---------------------------
# AI 퀴즈 생성 함수
# ---------------------------
def create_quiz(field, level):

    response = ai_client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {
                "role": "system",
                "content": """
                너는 신소재공학 교수이다.
                학생의 전공 공부를 돕기 위한 퀴즈를 만든다.

                반드시 다음 형식으로 작성한다.

                [문제]
                문제 내용

                A.
                B.
                C.
                D.

                [정답]
                정답 번호

                [해설]
                자세한 설명
                """
            },
            {
                "role": "user",
                "content": f"""
                분야: {field}
                난이도: {level}

                신소재공학 관련 객관식 문제 1개를 만들어줘.
                """
            }
        ]
    )

    return response.choices[0].message.content



# ---------------------------
# Streamlit 화면
# ---------------------------

st.title("🧪 Material Quiz AI")
st.subheader("AI 신소재공학 퀴즈 생성기")

st.write(
    """
    신소재공학 전공 분야별 문제를 AI가 생성합니다.
    시험 공부와 전공 복습에 활용하세요.
    """
)


# 분야 선택

field = st.selectbox(
    "🔬 분야 선택",
    [
        "배터리 소재",
        "반도체 소재",
        "나노 소재",
        "금속 재료",
        "고분자 소재",
        "세라믹 소재"
    ]
)


# 난이도 선택

level = st.selectbox(
    "🎯 난이도",
    [
        "기초",
        "대학교 전공",
        "심화"
    ]
)



if st.button("🚀 문제 만들기"):

    with st.spinner("AI 교수가 문제를 만드는 중..."):

        quiz = create_quiz(field, level)

    st.success("문제 생성 완료!")

    st.markdown(quiz)



# ---------------------------
# 학습 기록
# ---------------------------

st.divider()

st.subheader("📚 오늘의 학습 기록")

if "quiz_count" not in st.session_state:
    st.session_state.quiz_count = 0


if st.button("학습 횟수 증가"):
    st.session_state.quiz_count += 1


st.metric(
    "푼 문제 수",
    f"{st.session_state.quiz_count}개"
)
