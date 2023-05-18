from pydantic import BaseModel
import string


class Product(BaseModel):
    id:int
    name:string(100)
    descripition:str
    price:int
    category_id:int

    

