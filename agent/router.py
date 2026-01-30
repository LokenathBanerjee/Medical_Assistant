import streamlit as st

from agent.gemini_agent import run_prompt
from agent.memory import add_to_history, history_to_text

from utils.validators import is_medical_query
from medical_logic.emergency import is_emergency, emergency_message
from medical_logic.symptom_rules import update_slots_from_text, enough_info_message

from agent.prompt import PROMPT_DIAGNOSIS_FINAL
from medical_logic.medicines import recommend_medicines, format_medicine_block


def _next_question_from_missing(missing: list) -> str:
    # Priority order (what you want in sequence)
    priority = ["symptoms", "duration", "temperature", "severity"]

    missing_set = set(missing)
    for field in priority:
        if field in missing_set:
            if field == "symptoms":
                return "What symptoms do you have? (fever/cough/sore throat/body ache/headache/vomiting/diarrhea)"
            if field == "duration":
                return "Since when do you have this problem? (e.g., 2 days / since yesterday)"
            if field == "temperature":
                return "What is your temperature right now? (e.g., 101°F or 38.3°C)"
            if field == "severity":
                return "How severe is it? (mild / moderate / severe)"
    return "Do you have any other symptoms?"


def handle_user_message(user_input: str, retriever=None) -> str:
    # emergency first
    if is_emergency(user_input):
        return emergency_message()

    # medical-only guard (first message only)
    if len(st.session_state.history) == 0 and not is_medical_query(user_input):
        return "⚠️ I answer **medical-related questions only**. Please describe a symptom or health concern."

    # ensure anti-repeat key exists
    if "last_missing" not in st.session_state:
        st.session_state.last_missing = None

    # memory
    add_to_history(st.session_state.history, "user", user_input)

    # slots extraction
    update_slots_from_text(st.session_state.slots, user_input)

    # RAG context (optional)
    context = ""
    if retriever is not None:
        try:
            docs = retriever.get_relevant_documents(user_input)
            context = "\n\n".join([d.page_content[:1200] for d in docs[:3]])
        except Exception:
            context = ""

    # check enough info
    enough, missing = enough_info_message(st.session_state.slots)

    # FINAL: diagnosis + medicines
    if enough:
        final_text = run_prompt(
            PROMPT_DIAGNOSIS_FINAL,
            {
                "history": history_to_text(st.session_state.history),
                "context": context,
                "input": user_input,
                "slots": st.session_state.slots,
            },
        )

        meds = recommend_medicines(
            st.session_state.slots,
            history_text=history_to_text(st.session_state.history),
        )
        final_text = final_text + "\n\n" + format_medicine_block(meds)

        add_to_history(st.session_state.history, "assistant", final_text)

        # reset anti-repeat tracker for next cycle
        st.session_state.last_missing = None
        return final_text

    # FOLLOW-UP: prevent repeating the same question
    # pick next missing, but if it’s same as last asked, choose a different one
    next_missing = missing[0] if missing else None
    if next_missing and st.session_state.last_missing == next_missing:
        if len(missing) > 1:
            next_missing = missing[1]  # ask the next missing field instead

    st.session_state.last_missing = next_missing
    question = _next_question_from_missing([next_missing] if next_missing else missing)

    add_to_history(st.session_state.history, "assistant", question)
    return question








