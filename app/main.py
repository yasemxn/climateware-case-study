from fastapi import FastAPI
from app import endpoints

app = FastAPI(
    title="Climateware AI Recommendation API",
    description="Provides carbon emission reduction suggestions via GPT-4o",
    version="1.0.0"
)

app.include_router(endpoints.router)
