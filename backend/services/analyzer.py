def analyze_comment(text: str):
    text = text.lower()

    if "hate" in text:
        return {
            "category": "Hate Speech",
            "severity": "High",
            "score": 90,
        }

    elif "idiot" in text or "stupid" in text:
        return {
            "category": "Harassment",
            "severity": "Medium",
            "score": 60,
        }

    elif "kill" in text:
        return {
            "category": "Violence",
            "severity": "Critical",
            "score": 100,
        }

    return {
        "category": "Safe",
        "severity": "Low",
        "score": 5,
    }