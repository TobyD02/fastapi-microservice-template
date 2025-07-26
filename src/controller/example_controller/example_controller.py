from src.config_provider.config_provider import ConfigProvider
from src.model.example_model import ExampleModel


class ExampleController:
    def __init__(self, config_provider: ConfigProvider):
        self.config_provider = config_provider

    def get_example(self):
        return ExampleModel(ping="ping", base_path=self.config_provider.base_path)