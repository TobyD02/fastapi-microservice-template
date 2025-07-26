from typing import Annotated

from fastapi import Depends

from src.config_provider.config_provider import ConfigProvider
from src.config_provider.factory.config_provider_factory import config_provider_factory
from src.controller.example_controller.example_controller import ExampleController


def example_controller_factory(config_provider: Annotated[ConfigProvider, Depends(config_provider_factory)]):
    return ExampleController(config_provider)