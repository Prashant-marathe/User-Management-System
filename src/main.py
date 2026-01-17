from fastapi import FastAPI
from src.users.router import user_router

version = "v1"

app = FastAPI(
    title="User Management System",
    description="RESTAPI for User Management",
    version=version, 
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(user_router, prefix=f"/api/{version}/users", tags=['Users'])
