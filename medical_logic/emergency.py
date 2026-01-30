CRITICAL_COMBINATIONS = [
    ("vomit", "blood"),
    ("vomiting", "blood"),
    ("cough", "blood"),
    ("severe", "bleeding"),
    ("chest", "pain"),
    ("shortness", "breath"),
]

def is_emergency(text: str) -> bool:
    t = text.lower()
    return any(a in t and b in t for a, b in CRITICAL_COMBINATIONS)

def emergency_message() -> str:
    return (
        "🚨 **Possible medical emergency** detected.\n\n"
        "Please **seek immediate medical attention**:\n"
        "- Call emergency services, OR\n"
        "- Go to the nearest hospital now.\n\n"
        "If you can, share your **age** and exact symptoms with a doctor."
    )
