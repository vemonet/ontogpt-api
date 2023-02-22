from pydantic import BaseSettings


class Settings(BaseSettings):
    BIOPORTAL_APIKEY: str
    OPENAI_APIKEY: str

    # API_PASSWORD: str = 'password'
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
