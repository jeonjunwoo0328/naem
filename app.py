import streamlit as st
from openai import OpenAI

# OpenAI 설정
ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# -----------------------
# Session State
# -----------------------
if "history" not in st.session_state:
    st.session_state.history = []


# -----------------------
# AI 요청 함수
# -----------------------
def ask_ai(prompt):

    response = ai_client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {
                "role": "system",
                "content":
                """
                너는 친절한 영어 전문 튜터이다.
                사용자의 영어 실력을 향상시키기 위해
                독해, 문법, 작문을 자세히 설명한다.

                설명은:
                - 쉬운 한국어
                - 영어 예문
                - 틀린 이유
                - 개선 방법
                순서로 제공한다.
                """
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content



# -----------------------
# 페이지
# -----------------------

def reading_page():

    st.header("📖 영어 독해 훈련")

    level = st.selectbox(
        "난이도",
        ["초급", "중급", "고급"]
    )

    topic = st.text_input(
        "원하는 주제",
        "환경"
    )


    if st.button("독해 지문 만들기"):

        prompt = f"""
        {level} 수준의 영어 독해 지문을 만들어줘.

        주제: {topic}

        구성:
        1. 영어 지문
        2. 한국어 해석
        3. 중요 단어
        4. 독해 문제 3개
        """

        result = ask_ai(prompt)

        st.write(result)



def grammar_page():

    st.header("✏️ 영어 문법 코치")

    sentence = st.text_area(
        "검사할 영어 문장을 입력하세요"
    )


    if st.button("문법 검사"):

        prompt = f"""
        다음 영어 문장을 분석해줘.

        문장:
        {sentence}

        알려줄 내용:
        1. 문법 오류
        2. 올바른 문장
        3. 문법 설명
        4. 비슷한 예문
        """

        result = ask_ai(prompt)

        st.write(result)



def writing_page():

    st.header("📝 영어 작문 첨삭")

    writing = st.text_area(
        "작성한 영어 글을 입력하세요"
    )


    if st.button("첨삭 받기"):

        prompt = f"""
        다음 영어 글을 첨삭해줘.

        글:
        {writing}

        분석:
        1. 자연스러운 표현 수정
        2. 문법 오류
        3. 더 좋은 표현
        4. 점수 (100점 기준)
        """

        result = ask_ai(prompt)

        st.write(result)



def conversation_page():

    st.header("💬 영어 회화 연습")

    situation = st.text_input(
        "상황",
        "카페에서 주문하기"
    )


    if st.button("회화 시작"):

        prompt = f"""
        영어 회화 연습을 시작하자.

        상황:
        {situation}

        규칙:
        - 영어로 대화
        - 내가 틀리면 한국어로 설명
        - 자연스러운 표현 알려주기
        """

        result = ask_ai(prompt)

        st.write(result)



# -----------------------
# Navigation
# -----------------------

pg = st.navigation(
    [
        st.Page(
            reading_page,
            title="독해 공부",
            icon="📖"
        ),

        st.Page(
            grammar_page,
            title="문법 검사",
            icon="✏️"
        ),

        st.Page(
            writing_page,
            title="작문 첨삭",
            icon="📝"
        ),

        st.Page(
            conversation_page,
            title="영어 회화",
            icon="💬"
        )
    ],
    position="top"
)


st.title("🌎 AI 영어 공부 도우미")

pg.run()
