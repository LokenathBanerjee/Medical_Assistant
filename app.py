import streamlit as st
from logic.chat_controller import handle_chat

st.set_page_config(page_title="AI Medical Assistant", layout="centered")
st.title("🩺 AI Medical Assistant")

# Initialize memory
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Reset button
if st.button("🔄 New Patient / Clear Chat"):
    st.session_state.clear()
    st.experimental_rerun()

# Chat input
user_input = st.chat_input("Describe your symptoms...")

if user_input:
    handle_chat(user_input)

# 🔥 DISPLAY FULL CONVERSATION MEMORY
for msg in st.session_state.conversation:
    if msg.startswith("Patient:"):
        st.chat_message("user").write(msg.replace("Patient:", "").strip())
    elif msg.startswith("Doctor:"):
        st.chat_message("assistant").write(msg.replace("Doctor:", "").strip())
