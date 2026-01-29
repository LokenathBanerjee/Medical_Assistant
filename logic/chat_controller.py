import streamlit as st
from llm.gemini_langchain import call_gemini
from logic.emergency import is_emergency, emergency_message
from logic.medical_guard import is_medical_query, medical_only_message

QUESTION_SETS = [
    """1️⃣ What is your main problem and since when?
Options:
- Fever
- Cough
- Cold
- Headache
- Body pain
Example: Fever for 2 days""",

    """2️⃣ Do you currently have fever?
Options:
- Yes (high)
- Yes (mild)
- No
- Not sure""",

    """3️⃣ Are you experiencing any of these? (you can mention multiple)
Options:
- Cough
- Cold
- Sore throat
- Body pain
- Headache
- None""",

    """4️⃣ How severe are your symptoms?
Options:
- Mild
- Moderate
- Severe""",

    """5️⃣ Have you taken any medicine or do you have allergies?
Options:
- No medicine taken
- Took paracetamol
- Took antibiotics
- Have drug allergy
- Not sure"""
]


def handle_chat(user_input: str) -> str:
    # 🚨 Emergency check
    if user_input and is_emergency(user_input):
        return emergency_message()

    # ✅ INIT STATE & ASK FIRST QUESTION
    if "step" not in st.session_state:
        st.session_state.step = 0
        st.session_state.answers = []
        return QUESTION_SETS[0]

    # ✅ STORE ANSWER
    st.session_state.answers.append(
        f"Q{st.session_state.step + 1}: {user_input}"
    )

    # ✅ MEDICAL-ONLY CHECK (ONLY AFTER Q1 ANSWER)
    if st.session_state.step == 0 and not is_medical_query(user_input):
        # Roll back storing invalid answer
        st.session_state.answers.pop()
        return medical_only_message()

    st.session_state.step += 1

    # 🛑 AFTER 5 QUESTIONS → DIAGNOSIS
    if st.session_state.step >= len(QUESTION_SETS):
        prompt = f"""
You are a medical assistant.

Patient responses:
{chr(10).join(st.session_state.answers)}

Based on this information:
1. Probable diagnosis (short, safe)
2. Medicines:(rupees in INR)
   - Cheap (generic)
   - Moderate
   - Expensive
3. Home care advice
4. Clear medical disclaimer
"""
        return call_gemini(prompt)

    # ✅ ASK NEXT QUESTION
    return QUESTION_SETS[st.session_state.step]
