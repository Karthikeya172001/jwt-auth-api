from fastapi import FastAPI
from app.auth.routes import router as auth_router

app = FastAPI(
    title="JWT Authentication API",
    version="1.0.0"
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"status": "running"}