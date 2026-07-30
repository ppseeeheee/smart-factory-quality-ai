import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="AI Smart Factory",
    page_icon="🏭",
    layout="wide"
)

# -----------------------------
# 사이드바
# -----------------------------
st.sidebar.title("🏭 AI Smart Factory")

menu = st.sidebar.radio(
    "메뉴",
    [
        "📊 Dashboard",
        "🧠 Prediction"
    ]
)

st.sidebar.divider()

st.sidebar.caption("Version 1.0")

# -----------------------------
# 메인 화면
# -----------------------------
st.title(menu)

st.write("여기에 페이지 내용이 들어갑니다.")