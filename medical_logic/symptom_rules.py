import re
from typing import Dict, List, Optional, Tuple


def _norm(text: str) -> str:
    return (text or "").strip().lower()


def _extract_duration_days(text: str) -> Optional[int]:
    t = _norm(text)

    # hours
    m = re.search(r"(\d+)\s*(hour|hours|hr|hrs)\b", t)
    if m:
        return 0

    # days
    m = re.search(r"(\d+)\s*(day|days)\b", t)
    if m:
        return int(m.group(1))

    # weeks
    m = re.search(r"(\d+)\s*(week|weeks)\b", t)
    if m:
        return int(m.group(1)) * 7

    # months (rough)
    m = re.search(r"(\d+)\s*(month|months)\b", t)
    if m:
        return int(m.group(1)) * 30

    if "since yesterday" in t or "from yesterday" in t:
        return 1
    if "since today" in t or "from today" in t:
        return 0

    return None


def _extract_severity(text: str) -> Optional[str]:
    t = _norm(text)
    if any(w in t for w in ["severe", "very bad", "worst", "unbearable", "extreme"]):
        return "severe"
    if any(w in t for w in ["moderate", "medium", "manageable"]):
        return "moderate"
    if any(w in t for w in ["mild", "light", "slight"]):
        return "mild"
    return None


def _extract_temperature(text: str) -> Optional[str]:
    """
    Voice-friendly support:
      - 101 f / 101°F / 101 fahrenheit / 101 degrees fahrenheit / 101 degree fahrenheit
      - 38.5 c / 38.5°c / 38.5 celsius / 38.5 degrees celsius
    """
    t = _norm(text)

    # Celsius patterns
    m = re.search(
        r"(\d+(?:\.\d+)?)\s*(?:°\s*)?(?:c\b|celsius\b|degree c\b|degrees c\b|degree celsius\b|degrees celsius\b)",
        t,
    )
    if m:
        return f"{m.group(1)} C"

    # Fahrenheit patterns
    m = re.search(
        r"(\d+(?:\.\d+)?)\s*(?:°\s*)?(?:f\b|fahrenheit\b|degree f\b|degrees f\b|degree fahrenheit\b|degrees fahrenheit\b)",
        t,
    )
    if m:
        return f"{m.group(1)} F"

    return None


SYMPTOM_KEYWORDS = {
    "fever": ["fever", "high temperature", "temperature", "chills"],
    "cough": ["cough", "coughing"],
    "sore_throat": ["sore throat", "throat pain", "throat hurts"],
    "runny_nose": ["runny nose", "sneezing", "blocked nose", "stuffy nose", "congestion"],
    "headache": ["headache", "migraine", "head pain"],
    "body_ache": ["body ache", "muscle pain", "body pain", "myalgia"],
    "vomiting": ["vomit", "vomiting", "throwing up"],
    "diarrhea": ["diarrhea", "loose motion", "loose motions"],
    "stomach_pain": ["stomach pain", "abdominal pain", "belly pain"],
    "chest_pain": ["chest pain", "pressure in chest", "tightness in chest"],
    "breathlessness": ["shortness of breath", "difficulty breathing", "breathless", "can't breathe", "wheezing"],
}


def _detect_symptoms(text: str) -> List[str]:
    t = _norm(text)
    found = []
    for k, kws in SYMPTOM_KEYWORDS.items():
        if any(w in t for w in kws):
            found.append(k)
    return sorted(set(found))


def update_slots_from_text(slots: Dict, user_text: str) -> None:
    """
    Updates slots dict in-place.
    Keys:
      symptoms: list[str]
      duration_days: int
      severity: str
      temperature: str ("101 F" / "38.5 C")
    """
    t = _norm(user_text)

    # Symptoms
    symptoms = _detect_symptoms(t)
    if symptoms:
        existing = slots.get("symptoms", [])
        if isinstance(existing, str):
            existing = [s.strip() for s in existing.split(",") if s.strip()]
        if not isinstance(existing, list):
            existing = []
        slots["symptoms"] = sorted(set(existing + symptoms))

    # Duration
    d = _extract_duration_days(t)
    if d is not None:
        slots["duration_days"] = d

    # Severity
    sev = _extract_severity(t)
    if sev:
        slots["severity"] = sev

    # Temperature
    temp = _extract_temperature(t)
    if temp:
        slots["temperature"] = temp


def enough_info_message(slots: Dict) -> Tuple[bool, List[str]]:
    """
    Returns (enough, missing_fields)
    Missing fields are standardized: symptoms, duration, severity, temperature
    """
    missing: List[str] = []

    symptoms = slots.get("symptoms")
    if not symptoms or (isinstance(symptoms, list) and len(symptoms) == 0):
        missing.append("symptoms")

    if slots.get("duration_days") is None:
        missing.append("duration")

    if not slots.get("severity"):
        missing.append("severity")

    if isinstance(symptoms, list) and "fever" in symptoms and not slots.get("temperature"):
        missing.append("temperature")

    return (len(missing) == 0), missing
