from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str
    DATABASE_URL: str
    REDIS_HOST: str
    REDIS_PORT: int
    BASE_URL: str
    RATE_LIMIT: int
    BASE69: str
    

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()