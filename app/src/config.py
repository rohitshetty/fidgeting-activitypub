from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):

    base_domain: str
    public_key_pem_path: str
    private_key_pem_path: str
    public_key: str = ""

    test_user: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    settings = Settings()

    with open(settings.public_key_pem_path) as f:
        settings.public_key = f.read()
        settings.public_key = settings.public_key.replace("\n", "\\n")

    return settings
