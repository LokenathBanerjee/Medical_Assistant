def is_medical_query(text: str) -> bool:
    keywords = [

        # General health
        "health", "medical", "doctor", "hospital", "clinic", "patient", "disease", "illness",

        # Symptoms
        "fever", "pain", "ache", "headache", "migraine", "body pain",
        "cough", "cold", "flu", "sore throat",
        "vomit", "vomiting", "nausea",
        "diarrhea", "constipation",
        "fatigue", "weakness", "dizziness",
        "shortness of breath", "breathing problem",
        "chest pain", "palpitations",
        "sweating", "chills",
        "loss of appetite", "weight loss",
        "rash", "itching", "swelling",
        "bleeding", "blood",
        "burn", "injury", "fracture", "wound",

        # Body parts
        "head", "eye", "ear", "nose", "throat",
        "heart", "lung", "lungs",
        "stomach", "abdomen", "liver", "kidney",
        "brain", "nerve",
        "skin", "bone", "joint", "muscle",
        "arm", "leg", "back",

        # Diseases / conditions
        "infection", "viral", "bacterial", "fungal",
        "diabetes", "hypertension", "bp", "blood pressure",
        "asthma", "covid", "coronavirus",
        "tuberculosis", "tb",
        "cancer", "tumor",
        "allergy",
        "anemia",
        "arthritis",
        "stroke", "paralysis",
        "heart attack",
        "kidney stone",
        "ulcer",

        # Mental health
        "stress", "anxiety", "depression", "panic",
        "mental health", "insomnia", "sleep disorder",

        # Medicines & treatment
        "medicine", "tablet", "pill", "drug",
        "treatment", "therapy",
        "antibiotic", "painkiller", "paracetamol",
        "insulin",
        "syrup", "injection", "vaccine",
        "dose", "dosage", "side effect",

        # Tests & diagnosis
        "test", "scan", "x-ray", "ct", "mri",
        "blood test", "urine test",
        "ecg", "ekg",
        "diagnosis", "report",

        # Emergency terms
        "emergency", "critical", "severe",
        "unconscious", "fainting",
        "accident", "trauma",

        # Pregnancy / women health
        "pregnant", "pregnancy",
        "period", "menstruation",
        "pcos", "gynecology",

    ]

    text = text.lower()
    return any(keyword in text for keyword in keywords)

def medical_only_message():
    return (
        "⚠️ I am designed to answer **medical-related questions only**.\n"
        "Please describe a symptom or health concern."
    )
