from typing import Annotated

from fastapi import FastAPI, Depends

from src.config_provider.factory.config_provider_factory import config_provider_factory
from src.controller.example_controller.example_controller import ExampleController
from src.controller.example_controller.factory.example_controller_factory import example_controller_factory


def define_routes(app: FastAPI):
    config_provider = config_provider_factory()

    @app.get(config_provider.base_path + "/")
    async def example(example_controller: Annotated[ExampleController, Depends(example_controller_factory)]):
        return example_controller.get_example()