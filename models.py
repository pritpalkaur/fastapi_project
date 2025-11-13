from pydantic import BaseModel

class Product(BaseModel):
    Name: str
    Price: float
