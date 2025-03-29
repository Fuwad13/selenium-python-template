from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    CHROMEDRIVER_PATH_LINUX: Path = Path(__file__).parent / "webdrivers" / "linux" / "chrome" / "chromedriver"
    CHROMEDRIVER_PATH_WINDOWS: Path = Path(__file__).parent / "webdrivers" / "windows" / "chrome" / "chromedriver.exe"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

Config = Settings()