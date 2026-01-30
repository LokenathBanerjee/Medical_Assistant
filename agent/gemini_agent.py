import os
from typing import Any, List, Optional

from dotenv import load_dotenv
from groq import Groq

load_dotenv(override=True)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ✅ pick model from .env, with a safe default that is currently supported
DEFAULT_MODEL = "llama-3.1-8b-instant"
MODEL = os.getenv("GROQ_MODEL", DEFAULT_MODEL)

SYSTEM_PROMPT = """
You are an AI Medical Assistant.

Rules:
- Only answer medical-related questions.
- Ask follow-up questions about symptoms (duration, severity, location, triggers, allergies, existing conditions).
- Provide step-by-step guidance.
- Mention emergency red flags when relevant.
- Suggest medicines carefully, including cheaper and expensive alternatives, with safety cautions.
- Encourage consulting a doctor for serious symptoms.
""".strip()


def run_prompt(prompt: str, history: Optional[List[str]] = None, *args: Any, **kwargs: Any) -> str:
    """
    Router may call: run_prompt(prompt, history) or pass extra args (slots, etc).
    This signature keeps your project compatible.
    """
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        if history:
            for h in history:
                if isinstance(h, str) and h.strip():
                    messages.append({"role": "user", "content": h.strip()})

        messages.append({"role": "user", "content": prompt})

        resp = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.4,
        )
        return resp.choices[0].message.content

    except Exception as e:
        return f"⚠️ Groq Error: {e}"

