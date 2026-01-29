import streamlit as st
from llm.gemini_langchain import call_gemini
from logic.medical_guard import is_medical_query, medical_only_message
from logic.emergency import is_emergency, emergency_message


def handle_chat(user_input: str) -> str:
    """
    Human-like doctor conversation controller.
    LLM decides what to ask next.
    Python only handles safety + memory.
    """

    # ----------------- EMERGENCY FIRST -----------------
    if is_emergency(user_input):
        return emergency_message()

    # ----------------- INIT MEMORY -----------------
    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    # ----------------- MEDICAL ONLY (FIRST MESSAGE) -----------------
    if not st.session_state.conversation and not is_medical_query(user_input):
        return medical_only_message()

    # ----------------- STORE USER MESSAGE -----------------
    st.session_state.conversation.append(f"Patient: {user_input}")

    # ----------------- DOCTOR THINKING PROMPT -----------------
    doctor_prompt = f"""
You are an experienced, calm medical doctor talking to a patient.

Conversation so far:
{chr(10).join(st.session_state.conversation)}

Your task:
- Ask ONE natural follow-up question like a real doctor
- Do NOT repeat questions already answered
- Accept vague answers (yes, no, not sure, maybe)
- Do NOT force temperature numbers
- Decide what is most clinically useful to ask next
- If you already have enough information, reply ONLY with:
  DIAGNOSIS_READY

Style:
- Friendly
- Short
- Human
- Not robotic
"""

    doctor_reply = call_gemini(doctor_prompt).strip()

    # ----------------- IF READY FOR DIAGNOSIS -----------------
    if "DIAGNOSIS_READY" in doctor_reply.upper():
        diagnosis_prompt = f"""
You are a medical assistant.

Based on the following patient conversation:
{chr(10).join(st.session_state.conversation)}

Provide:
1. Probable diagnosis (brief, non-alarming)
2. Medicines:
   - Cheap (generic)
   - Moderate
   - Expensive
3. Clear medical disclaimer (not a diagnosis, consult doctor)

Keep it simple and safe.
"""
        return call_gemini(diagnosis_prompt)

    # ----------------- STORE DOCTOR QUESTION -----------------
    st.session_state.conversation.append(f"Doctor: {doctor_reply}")

    return doctor_reply
