from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(default='')

    class Config:
        env_file = '.env'


settings = Settings()