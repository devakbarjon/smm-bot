import ast
import os
from typing import List

from dotenv import load_dotenv
from pydantic import BaseModel, SecretStr

load_dotenv()

class Settings(BaseModel):
    BOT_TOKEN: SecretStr
    DEVS: List[int]
    SECRET_KEY: SecretStr
    BACKEND_URL: str


settings = Settings(
    BOT_TOKEN=os.getenv("BOT_TOKEN"),
    DEVS=ast.literal_eval(os.getenv("DEV_ID", "[]")),
    SECRET_KEY=os.getenv("SECRET_KEY"),
    BACKEND_URL=os.getenv("BACKEND_URL")
)
