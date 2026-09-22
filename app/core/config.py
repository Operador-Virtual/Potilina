from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Potilina"
    env: str = "dev"
    webhook_secret: str | None = None


settings = Settings()
