
from pydantic import BaseModel, Field, validator

class CalcRequest(BaseModel):
    a: float = Field(...)
    b: float = Field(...)
    op: str = Field(..., description="add|sub|mul|div")

    @validator("op")
    def valid_op(cls, v):
        if v not in {"add", "sub", "mul", "div"}:
            raise ValueError("op must be one of add|sub|mul|div")
        return v

class CalcResponse(BaseModel):
    result: float
