import os
from dotenv import load_dotenv

load_dotenv()

class setting:
    DATABASE_URL = os.getenv('DATABASE_URL')
    API_URL = os.getenv("API_URL","http://localhost:8000")


settings = setting()