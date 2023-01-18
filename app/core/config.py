
from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator, AnyUrl


class Settings(BaseSettings):
    PROJECT_NAME: str
    ENVIRONMENT: str = "dev"
    TESTING: bool = 0
    DATABASE_NAME: str
    DATABASE_TEST_NAME: str
    DATABASE_URL: AnyUrl = None
    DATABASE_TEST_URL: AnyUrl = None
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
