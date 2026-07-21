import streamlit as st

# -------------------------------
# Session State
# -------------------------------
if "todo_list" not in st.session_state:
    st.session_state.todo_list = []

if "user_motto" not in st.session_state:
    st.session_state.user_motto = "오늘도 화이팅!"


# -------------------------------
# 할 일 추가 함수
# -------------------------------
def add_todo():
    task = st.session_state.todo_input
    if task:
        st.session_state.todo_list.append([task, False])
        st.toast("할 일이 추가되었습니다!")
        st.session_state.todo_input = ""


# -------------------------------
# 페이지 1 : 오늘의 다짐
# -------------------------------
def page1():
    st.title("🌱 갓생 살기 플래너")

    st.header("📣 1. 오늘의 다짐")

    motto = st.text_input(
        "나의 한 줄 좌우명을 적어주세요",
        value=st.session_state.user_motto,
    )

    if st.button("다짐 저장"):
        st.session_state.user_motto = motto
        st.success("좌우명이 등록되었습니다!")


# -------------------------------
# 페이지 2 : 오늘의 할 일
# -------------------------------
def page2():
    st.header("✅ 2. 오늘의 할 일")

    st.write(f"현재 다짐: **{st.session_state.user_motto}**")

    st.text_input(
        "추가할 할 일을 입력하세요",
        key="todo_input"
    )

    st.button("추가하기", on_click=add_todo)

    st.markdown("---")

    if not st.session_state.todo_list:
        st.info("등록된 할 일이 없습니다.")

    for i in range(len(st.session_state.todo_list)):
        col1, col2, col3 = st.columns([4, 1, 1])

        with col1:
            st.write(f"{i+1}. {st.session_state.todo_list[i][0]}")

        with col2:
            if st.button("완료", key=f"btn_{i}"):
                st.session_state.todo_list[i][1] = True
                st.rerun()

        with col3:
            if st.session_state.todo_list[i][1]:
                st.write("✅ 달성!")


# -------------------------------
# 페이지 3 : 갓생 지수
# -------------------------------
def page3():
    st.header("📈 3. 나의 갓생 지수")

    if not st.session_state.todo_list:
        st.write("아직 등록된 할 일이 없습니다.")
        return

    total = len(st.session_state.todo_list)
    count = sum(item[1] for item in st.session_state.todo_list)

    progress = count / total

    st.metric("오늘의 달성률", f"{progress*100:.1f}%")
    st.progress(progress)

    if st.button("기록 전체 초기화"):
        st.session_state.todo_list = []
        st.rerun()


# -------------------------------
# Navigation
# -------------------------------
pg = st.navigation([
    st.Page(page1, title="오늘의 다짐", icon="📣"),
    st.Page(page2, title="오늘의 할 일", icon="✅"),
    st.Page(page3, title="나의 갓생 지수", icon="📈"),
])

pg.run()
