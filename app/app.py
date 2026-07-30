import streamlit as st
from datetime import date

# -----------------------------
# 페이지 기본 설정
# -----------------------------
st.set_page_config(
    page_title="Smart Factory Dashboard",
    page_icon="🏭",
    layout="wide"
)

# -----------------------------
# 사이드바
# -----------------------------
st.sidebar.title("📋 Menu")

page = st.sidebar.radio(
    "페이지 선택",
    [
        "Home",
        "Dashboard",
        "About"
    ]
)

# -----------------------------
# 메인 화면
# -----------------------------
st.title("🏭 Smart Factory Quality Dashboard")

st.subheader("AI 기반 스마트 제조 품질 이상 탐지 시스템")

st.write(f"📅 오늘 날짜 : {date.today()}")

st.divider()

st.write(f"현재 선택한 메뉴 : **{page}**")