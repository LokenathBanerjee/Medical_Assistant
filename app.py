import streamlit as st

from agent.router import handle_user_message
from rag.retriever import get_retriever

# ✅ Voice (your functions)
from voice.speech_to_text import listen_once
# from voice.text_to_speech import speak  # optional

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="AI Medical Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================
# CSS (Premium UI)
# =========================
st.markdown(
    """
<style>
/* ----- App background ----- */
.stApp{
    background: radial-gradient(circle at top, #0b1220 0%, #070b12 55%, #05070c 100%);
}

/* ----- Remove default top padding so header looks complete ----- */
.block-container{
    padding-top: 0rem !important;
    padding-bottom: 2rem;
}

/* ----- Sidebar glass ----- */
section[data-testid="stSidebar"] > div{
    background: rgba(7, 11, 18, 0.92);
    backdrop-filter: blur(12px);
    border-right: 1px solid rgba(255,255,255,0.06);
}

/* ----- Header banner ----- */
.header{
    background: linear-gradient(90deg, rgba(0,198,255,0.25), rgba(0,114,255,0.22));
    border: 1px solid rgba(0,255,255,0.14);
    box-shadow: 0 12px 40px rgba(0,0,0,0.35);
    padding: 26px 40px;
    margin: 0 -2rem 18px -2rem; /* stretch full width */
    border-bottom-left-radius: 22px;
    border-bottom-right-radius: 22px;
}
.header h1{
    color: #ffffff;
    margin: 0;
    font-size: 3rem;
    letter-spacing: 0.3px;
}
.header p{
    color: #c7e7ff;
    margin: 8px 0 0 0;
    font-size: 1.05rem;
}

/* ----- Inputs (chat + text) ----- */
.stTextInput > div > div > input,
.stChatInput textarea{
    background: rgba(255,255,255,0.06) !important;
    color: #e5e7eb !important;
    border: 1px solid rgba(0,255,255,0.16) !important;
    border-radius: 14px !important;
}

/* ----- Buttons ----- */
.stButton > button{
    background: linear-gradient(135deg, #00c6ff, #0072ff) !important;
    color: white !important;
    border-radius: 14px !important;
    padding: 0.68rem 1rem !important;
    border: none !important;
    font-weight: 700 !important;
}

/* ----- Cards ----- */
.card{
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(0,255,255,0.12);
    border-radius: 18px;
    padding: 16px 16px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.35);
    margin-bottom: 12px;
}

/* ----- Helper text ----- */
.small{
    color: #b2ebf2;
    font-size: 0.92rem;
    margin: 0;
}
.hint{
    color: #e0f7fa;
    font-size: 0.98rem;
    margin: 0;
}

/* ----- Badges ----- */
.badge{
    display: inline-block;
    padding: 6px 10px;
    border-radius: 999px;
    background: rgba(0,255,255,0.12);
    border: 1px solid rgba(0,255,255,0.22);
    color: #80deea;
    font-size: 0.8rem;
    margin-right: 8px;
}

/* ----- Key-Value rows (slots panel) ----- */
.kv{
    display:flex;
    justify-content:space-between;
    gap:12px;
    padding: 8px 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}
.kv:last-child{ border-bottom:none; }
.k{ color:#80deea; font-size:0.9rem; }
.v{ color:#e0f7fa; font-size:0.95rem; font-weight:600; text-align:right; }

/* ----- Make chat area look cleaner ----- */
[data-testid="stChatMessage"]{
    border-radius: 16px;
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================
# Init memory (KEEP same keys to avoid errors)
# =========================
if "history" not in st.session_state:
    st.session_state.history = []
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "slots" not in st.session_state:
    st.session_state.slots = {}

# ✅ Mode (default Text)
if "input_mode" not in st.session_state:
    st.session_state.input_mode = "Text"

# =========================
# Load retriever (RAG)
# =========================
retriever = get_retriever(data_dir="data")

# =========================
# Header (Full width)
# =========================
st.markdown(
    """
<div class="header">
    <h1>🩺 AI Medical Assistant</h1>
    <p>Clinical-style symptom guidance & safety checks</p>
</div>
""",
    unsafe_allow_html=True,
)

# =========================
# Sidebar
# =========================
with st.sidebar:
    st.markdown("## 🧭 Menu")
    st.markdown('<p class="small">Use the chat for symptom analysis</p>', unsafe_allow_html=True)

    st.divider()

    if st.button("🆕 New Patient / Clear Chat", use_container_width=True):
        st.session_state.pop("history", None)
        st.session_state.pop("conversation", None)
        st.session_state.pop("slots", None)
        st.session_state.input_mode = "Text"
        st.rerun()

    st.markdown(
        """
<div class="card">
  <p class="small"><b>Tip:</b> Add duration, severity, allergies, and current medicines.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    slots = st.session_state.get("slots", {})
    if isinstance(slots, dict) and slots:
        st.markdown('<div class="card"><h4 style="margin:0 0 10px 0;">🧾 Extracted Info</h4>', unsafe_allow_html=True)
        for key, val in slots.items():
            st.markdown(
                f"""
<div class="kv">
  <div class="k">{str(key)}</div>
  <div class="v">{str(val)}</div>
</div>
""",
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
<div class="card">
  <p class="small"><b>Note:</b> This tool is informational and not a substitute for a doctor.</p>
</div>
""",
        unsafe_allow_html=True,
    )

# =========================
# Main Layout
# =========================
left, right = st.columns([2, 1], gap="large")

with left:
    # ✅ Badges + Mode selector (same area, minimal UI change)
    st.markdown(
        """
<div style="margin-bottom:10px;">
  <span class="badge">Symptom Chat</span>
  <span class="badge">RAG Enabled</span>
  <span class="badge">Memory</span>
  <p class="small" style="margin-top:10px;">Describe your symptoms clearly to get better guidance.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    # Mode selector (small, does not change design)
    mode_col1, mode_col2, mode_col3 = st.columns([1.2, 1.2, 3])
    with mode_col1:
        if st.button("📝 Text", use_container_width=True):
            st.session_state.input_mode = "Text"
    with mode_col2:
        if st.button("🎙️ Voice", use_container_width=True):
            st.session_state.input_mode = "Voice"
    with mode_col3:
        st.markdown(f"<p class='small'>Current mode: <b>{st.session_state.input_mode}</b></p>", unsafe_allow_html=True)

    st.markdown(
        """
<div class="card">
  <p class="hint"><b>Example:</b> “Fever since 2 days, sore throat, mild cough, no breathing issues.”</p>
</div>
""",
        unsafe_allow_html=True,
    )

    # Render existing chat
    for msg in st.session_state.conversation:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # ✅ VOICE MODE UI (minimal)
    if st.session_state.input_mode == "Voice":
        v1, v2 = st.columns([1, 3])
        with v1:
            speak_btn = st.button("🎙️ Speak Now", use_container_width=True)
        with v2:
            st.markdown("<p class='small'>Click Speak Now and say your symptoms clearly.</p>", unsafe_allow_html=True)

        if speak_btn:
            try:
                with st.spinner("Listening..."):
                    transcript = listen_once(timeout=6, phrase_time_limit=10)

                # store transcript like user message
                st.session_state.conversation.append({"role": "user", "content": f"🎙️ {transcript}"})
                with st.chat_message("user"):
                    st.markdown(f"🎙️ {transcript}")

                # IMPORTANT: same pipeline as text
                with st.chat_message("assistant"):
                    with st.spinner("Analyzing symptoms..."):
                        reply = handle_user_message(user_input=transcript, retriever=retriever)
                    st.markdown(reply)

                st.session_state.conversation.append({"role": "assistant", "content": reply})

            except Exception as e:
                st.error(f"Voice error: {e}")

    # ✅ TEXT MODE: keep your original chat input
    else:
        user_input = st.chat_input("Describe your symptoms...")

        if user_input:
            st.session_state.conversation.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            with st.chat_message("assistant"):
                with st.spinner("Analyzing symptoms..."):
                    try:
                        reply = handle_user_message(user_input=user_input, retriever=retriever)
                    except Exception as e:
                        reply = f"⚠️ Error: {e}"
                st.markdown(reply)

            st.session_state.conversation.append({"role": "assistant", "content": reply})

with right:
    st.markdown(
        """
<div class="card">
  <h3 style="margin:0;">🧾 Consultation Panel</h3>
  <p class="small">Quick view (you can later auto-fill this from your router output)</p>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="card">
  <h4 style="margin:0 0 8px 0;">🧠 Summary</h4>
  <p class="small">Parse your assistant output or return structured JSON to fill this automatically.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="card">
  <h4 style="margin:0 0 8px 0;">🚨 Red Flags</h4>
  <p class="small">If severe chest pain, breathing difficulty, fainting, confusion, or very high fever → seek urgent care.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="card">
  <h4 style="margin:0 0 8px 0;">💊 Medicines / Alternatives</h4>
  <p class="small">Medicine suggestions will appear in the assistant chat at the final step.</p>
</div>
""",
        unsafe_allow_html=True,
    )
