import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(user_message: str):
    system_prompt = """
    You are a helpful and empathetic healthcare assistant.
    Your goal is to identify symptoms and suggest the type of specialist the patient needs.

    RULES:
    1. If the symptoms sound life-threatening, start with 🚨 EMERGENCY: and advise emergency services.
    2. Keep responses under 3 sentences.
    3. End your response by suggesting a specialist.
    4. Do not prescribe medication.
    """

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            model="llama-3.3-70b-versatile"
        )

        response = chat_completion.choices[0].message.content
        return response

    except Exception as e:
        print(f"Error in AI response: {e}")
        return "AI service error, please try again."
