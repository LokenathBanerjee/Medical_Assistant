def is_valid_followup_answer(text: str) -> bool:
    valid_words = [
        "yes","no","mild","moderate","severe",
        "days","day","weeks","week","hours","hour",
        "since","last","pain","fever","headache","vomiting"
    ]
    text = text.lower()
    return any(w in text for w in valid_words)
