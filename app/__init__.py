from fastapi import FastAPI
from .routes import router

# Initialize FastAPI application
app = FastAPI(title="Property API", description="API for managing properties and inquiries")

# Include the router
app.include_router(router)

