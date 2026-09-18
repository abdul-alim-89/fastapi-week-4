from pydantic import BaseModel, Field, ConfigDict

class Category(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: int
    name: str

class ProductCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    in_stock: bool = True
    tags: list[str] = []
    category: Category
