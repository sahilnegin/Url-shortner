
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from url_shortener import shorten_url, get_original_url

app = FastAPI()


class URLRequest(BaseModel):
    url: str


@app.post("/shorten")
def create_short_url(request: URLRequest):
    code = shorten_url(request.url)
    return {"short_code": code}


@app.get("/expand/{short_code}")
def expand_short_url(short_code: str):
    original_url = get_original_url(short_code)
    if original_url is None:
        raise HTTPException(status_code=404, detail="Short code not found")
    return {"original_url": original_url}

# from fastapi import FastAPI, Request
# from pydantic import BaseModel

# from slowapi import Limiter, _rate_limit_exceeded_handler
# from slowapi.util import get_remote_address
# from slowapi.errors import RateLimitExceeded

# app = FastAPI()

# # Set up rate limiter
# limiter = Limiter(key_func=get_remote_address)
# app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# # Input model
# class TaxInput(BaseModel):
#     income: float
#     rate: float

# # Tax calculation function
# def calculate_tax(income: float, rate: float) -> float:
#     if income < 0 or rate < 0:
#         raise ValueError("Income and rate must be non-negative")
#     return income * (rate / 100)

# # Endpoint with rate limiting
# @app.post("/incometax")
# @limiter.limit("5/minute")
# def income_tax(request: Request, data: TaxInput):  # 👈 required
#     tax = calculate_tax(data.income, data.rate)
#     return {"tax": tax}
