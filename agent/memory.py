def history_to_text(history: list[str]) -> str:
    return "\n".join(history[-20:])  # keep last 20 lines

def add_to_history(history: list[str], role: str, text: str) -> None:
    if role.lower() == "user":
        history.append(f"Patient: {text}")
    else:
        history.append(f"Doctor: {text}")

