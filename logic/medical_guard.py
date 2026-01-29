def is_medical_query(text: str) -> bool:
    keywords = [
        "fever","pain","cough","vomit","blood","infection",
        "sick","ill","medicine","treatment","headache","nausea"
    ]
    text = text.lower()
    return any(k in text for k in keywords)

def medical_only_message():
    return (
        "⚠️ I am designed to answer **medical-related questions only**.\n"
        "Please describe a symptom or health concern."
    )
