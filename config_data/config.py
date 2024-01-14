from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    '''
    Функция загружает токен юота из окружения (файл .env)
    и возвращает экземпляр класса Config
    '''
    env = Env()
    env.read_env()
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))