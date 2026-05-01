import os
from dotenv import load_dotenv

load_dotenv()

class Config:
      GROQ_API_KEY = os.getenv("GROQ_API_KEY")
      GROQ_MODEL = os.getenv("GROQ_MODEL")
      GROQ_TEMPERATURE = float(os.getenv("GROQ_TEMPERATURE"))
