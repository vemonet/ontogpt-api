import logging

from pydantic import BaseSettings


# Configure settings
class Settings(BaseSettings):
    BIOPORTAL_APIKEY: str
    OPENAI_APIKEY: str
    # API_PASSWORD: str = 'password'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

# Configure logger
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s: [%(module)s:%(funcName)s] %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
