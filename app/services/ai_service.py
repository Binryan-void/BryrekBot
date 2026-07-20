from groq import AsyncGroq
from app.config import settings

class AIService:
    client = AsyncGroq(api_key=settings.GROQ_API_KEY)

    @staticmethod
    async def generate_response(prompt: str, system_instruction: str = "Eres un asistente útil y amable.") -> str:
        # Petición asíncrona a la API de Groq
        response = await AIService.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1024,
        )
        return response.choices[0].message.content
