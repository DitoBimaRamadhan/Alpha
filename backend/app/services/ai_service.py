from groq import Groq
from app.core.config import get_settings

settings = get_settings()
client = Groq(api_key=settings.GROQ_API_KEY)

class AIService:
    @staticmethod
    async def generate_text(prompt: str) -> str:
        # Menggunakan model Llama 3 atau model tersedia lainnya dari Groq
        # Berdasarkan gambar, kita gunakan model text-to-text yang kompeten
        try:
            completion = client.chat.completions.create(
                model="llama3-8b-8192", # Model standar Groq yang cepat dan murah
                messages=[
                    {"role": "system", "content": "You are ALPHA AI, a premium content generator."},
                    {"role": "user", "content": prompt}
                ],
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error connecting to Groq: {str(e)}"

    @staticmethod
    async def generate_image(prompt: str) -> str:
        # Groq saat ini fokus pada LLM, bukan Image Generation secara langsung
        # ponytail: placeholder tetap untuk gambar.
        return "https://via.placeholder.com/512?text=Groq+Focuses+on+LLM"
