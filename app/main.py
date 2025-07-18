from fastapi import FastAPI
from app.api.v1.users import router as users_router
# from app.core.config import settings

app = FastAPI()

# app.include_router(users.router)
app.include_router(users_router, prefix="/api/v1")

@app.get("/")
async def root():
    return "App running"