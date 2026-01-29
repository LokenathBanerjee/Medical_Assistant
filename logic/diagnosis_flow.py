def get_next_question(slots: dict) -> str:
    """
    Doctor-like adaptive questioning based on missing medical info
    """

    if "chief_complaint" not in slots:
        return "What problem is bothering you the most?"

    if "onset" not in slots:
        return "When did this problem start?"

    if slots.get("fever") and "fever_temp" not in slots:
        return "Have you checked your temperature? What was the highest reading?"

    if "severity" not in slots:
        return (
            "How severe is the discomfort?\n"
            "• Mild\n"
            "• Moderate\n"
            "• Severe"
        )

    if "associated_symptoms" not in slots:
        return (
            "Are you experiencing any other symptoms like cough, vomiting, "
            "breathing difficulty, rash, or bleeding?"
        )

    return "ENOUGH_INFO"
