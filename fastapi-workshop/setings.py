from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host:str = '127.0.0.1'
    server_port:int = 8000
    engine:str = "mysql+mysqlconnector://root:root@localhost:3306/web_site"

#Чтение переменных из dotenv файлов
settings = Settings(
    _env_file = '.env',
    _env_file_encoding = 'utf-8'
)

