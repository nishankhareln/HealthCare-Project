EMERGENCY_KEYWORDS = [
    "chest pain", "heart attack", "stroke", "bleeding", 
    "unconscious", "breathing difficulty", "suicide", "poison"
]

def check_medical_emergency(message: str) -> bool:
    message = message.lower()
    return any(keyword in message for keyword in EMERGENCY_KEYWORDS)