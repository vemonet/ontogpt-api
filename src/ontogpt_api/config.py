from pydantic import BaseSettings


class Settings(BaseSettings):
    BIOPORTAL_APIKEY: str
    OPENAI_APIKEY: str

    # API_PASSWORD: str = 'password'


settings = Settings()
