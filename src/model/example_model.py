from pydantic import BaseModel

class ExampleModel(BaseModel):
    ping: str
    base_path: str