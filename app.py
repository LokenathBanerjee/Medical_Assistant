import streamlit as st
from logic.chat_controller import handle_chat

st.set_page_config(page_title="AI Medical Assistant", layout="centered")
st.title("🩺 AI Medical Assistant")

if st.button("🔄 New Patient / Clear Chat"):
    st.session_state.clear()
    st.rerun()   # ✅ FIXED


# 👉 SHOW FIRST QUESTION
if "step" not in st.session_state:
    st.chat_message("assistant").write(handle_chat(""))

user_input = st.chat_input("Type your answer here...")

if user_input:
    st.chat_message("user").write(user_input)
    response = handle_chat(user_input)
    st.chat_message("assistant").write(response)
