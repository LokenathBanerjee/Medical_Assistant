# =========================
# EMERGENCY KEYWORDS
# =========================

CRITICAL_COMBINATIONS = [
    ("vomit", "blood"),
    ("vomiting", "blood"),
    ("cough", "blood"),
    ("spit", "blood"),
    ("severe", "bleeding"),
    ("heavy", "bleeding"),
    ("chest", "pain"),
    ("shortness", "breath"),
    ("difficulty", "breathing"),
    ("high", "fever"),
    ("unconscious", "person"),
    ("seizure", "attack"),
    ("head", "injury"),
    ("road", "accident"),
]

CRITICAL_SINGLE_WORDS = [
    "heart attack",
    "stroke",
    "paralysis",
    "unconscious",
    "seizure",
    "fits",
    "coma",
    "cardiac arrest",
    "brain hemorrhage",
    "internal bleeding",
    "poisoning",
    "overdose",
    "burns",
    "electric shock",
    "suicide",
    "collapsed"
]

CRITICAL_PHRASES = [
    "cannot breathe",
    "not breathing",
    "breathing stopped",
    "lost consciousness",
    "sudden chest pain",
    "severe head injury",
    "massive bleeding",
    "blood pressure very high",
    "blood sugar very low"
]

# =========================
# EMERGENCY DETECTOR
# =========================

def is_emergency(text: str) -> bool:
    text = text.lower()

    # Combination-based detection
    for a, b in CRITICAL_COMBINATIONS:
        if a in text and b in text:
            return True

    # Single-word / multi-word critical terms
    for word in CRITICAL_SINGLE_WORDS:
        if word in text:
            return True

    # Phrase-based detection
    for phrase in CRITICAL_PHRASES:
        if phrase in text:
            return True

    return False
def emergency_message():
    return (
        "🚨 **MEDICAL EMERGENCY DETECTED** 🚨\n\n"
        "Your symptoms indicate a potentially life-threatening condition.\n\n"
        "➡️ Seek **immediate medical attention**.\n"
        "➡️ Call emergency services(call 112) **now** or go to the nearest hospital.\n\n"
        "⚠️ Do NOT delay treatment."
    )
