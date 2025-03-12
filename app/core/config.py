
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY: str = os.getenv('GROQ_API_KEY')
    

settings = Settings()