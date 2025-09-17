from fastapi import FastAPI
from enum import Enum


app = FastAPI()


class Operator(Enum):
    SUM = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "div"

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/calculate/{a}/{operator}/{b}")
async def calculate(a: int, operator: Operator, b: int):
    match operator:
        case Operator.SUM:
            result = a + b
        case Operator.SUBTRACT:
            result = a - b
        case Operator.MULTIPLY:
            result = a * b
        case Operator.DIVIDE:
            if b == 0:
                return {"error": "Division by zero is not allowed."}
            result = a / b
    return {"result": result}
