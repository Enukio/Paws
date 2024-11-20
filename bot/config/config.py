import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int = 0
    API_HASH: str = ""

    REF_LINK: str = ""
    AUTO_TASK: bool = True
    AUTO_CONNECT_WALLET: bool = False
    DELAY_EACH_ACCOUNT: list[int] = [20, 30]
    IGNORE_TASKS: list[str] = ["boost"]
    ADVANCED_ANTI_DETECTION: bool = True
    USE_PROXY_FROM_FILE: bool = False

if not os.path.exists(".env"):
    print("Warning: .env file not found. Default values may be used.")

settings = Settings()

if not settings.API_ID or not settings.API_HASH:
    print("Warning: API_ID or API_HASH is missing or empty. Please check your .env file.")
