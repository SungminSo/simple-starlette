import os


class BaseConfig:
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB = 0


class DevConfig(BaseConfig):
    pass


class StageConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    REDIS_HOST = os.getenv("redis_host")
    REDIS_PORT = os.getenv("redis_port")
    REDIS_DB = os.getenv("redis_db")


config_map = dict(
    dev=DevConfig,
    stage=StageConfig,
    prod=ProdConfig,
)

try:
    config = config_map[os.getenv("MODE", "dev")]()
except KeyError:
    config = DevConfig()
