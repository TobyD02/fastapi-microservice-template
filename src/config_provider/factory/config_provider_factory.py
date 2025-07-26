from config.config import config
from src.config_provider.config_provider import ConfigProvider


def config_provider_factory():
    return ConfigProvider(
        base_path=config["base_path"]
    )