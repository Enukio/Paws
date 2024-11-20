import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from colorama import Fore, Style

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
    print(f"{Fore.YELLOW}Warning: .env file not found. Default values may be used.{Style.RESET_ALL}")

settings = Settings()
