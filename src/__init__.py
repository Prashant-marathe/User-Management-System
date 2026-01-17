from fastapi import FastAPI
from src.users.router import user_router
from contextlib import asynccontextmanager
from src.db.database import init_db

@asynccontextmanager
async def lifespan(app:FastAPI):
    print('Server Started Successfully')
    await init_db()
    yield
    print("Server stopped")

version = "v1"

app = FastAPI(
    title="User Management System",
    description="RESTAPI for User Management",
    version=version, 
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

app.include_router(user_router, prefix=f"/api/{version}/users", tags=['Users'])
