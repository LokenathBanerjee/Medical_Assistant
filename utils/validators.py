# utils/validators.py

def is_medical_query(text: str) -> bool:
    t = (text or "").lower().strip()

    # Common symptom keywords (+ your typo "feaver")
    medical_keywords = [
        "fever", "feaver", "temperature", "chills",
        "cough", "cold", "sneeze", "runny nose", "congestion",
        "sore throat", "throat pain",
        "headache", "migraine",
        "body pain", "body ache", "muscle pain",
        "vomit", "vomiting", "nausea",
        "diarrhea", "loose motion", "loose motions",
        "stomach pain", "abdominal pain",
        "chest pain", "breathless", "shortness of breath",
        "rash", "itching",
        "infection", "allergy", "bp", "blood pressure", "sugar", "diabetes", "asthma"
    ]

    return any(k in t for k in medical_keywords)
