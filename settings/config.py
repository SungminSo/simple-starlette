import os


class BaseConfig:
    MODE = os.getenv("MODE", "dev")

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB = 0


class DevConfig(BaseConfig):
    pass


class StageConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = os.getenv("REDIS_PORT")
    REDIS_DB = os.getenv("REDIS_DB")


config_map = dict(
    dev=DevConfig,
    stage=StageConfig,
    prod=ProdConfig,
)

try:
    config = config_map[os.getenv("MODE", "dev")]()
except KeyError:
    config = DevConfig()
