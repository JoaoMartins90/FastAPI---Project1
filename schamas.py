from pydantic import BaseModel, Field, field_validator
from typing import List
import re 

class ConverterInput(BaseModel):
    price: float  = Field(gt=0)
    to_currencies: List[str]

    @field_validator('to_currencies')
    def validade_to_currency(cls, value):
        for currency in value:
            if not re.match('^[A-Z]{3}$', currency):
                raise ValueError(f'Invalid currency {currency}')
        return value
    

class ConverterOutput(BaseModel):
    message: str
    data: List[dict]










""" 

{
    "price": 12321,
    "to_currencies": ['USD', 'GBP']
}
"""