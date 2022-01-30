from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    email: str
    cost_type: str
    created_on: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    
 

    class Config:
        orm_mode = True


