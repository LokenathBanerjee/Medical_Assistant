CRITICAL_COMBINATIONS = [
    ("vomit","blood"),
    ("vomiting","blood"),
    ("cough","blood"),
    ("severe","bleeding")
]

def is_emergency(text: str) -> bool:
    text = text.lower()
    return any(a in text and b in text for a,b in CRITICAL_COMBINATIONS)

def emergency_message():
    return (
        "🚨 MEDICAL EMERGENCY DETECTED 🚨\n\n"
        "Seek immediate medical attention.\n"
        "Call emergency services or go to the nearest hospital."
    )
