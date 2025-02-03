from fastapi import FastAPI
from app.api import properties, inquiries, agents  # Import the agents router

app = FastAPI()

# Include routers for properties, inquiries, and agents
app.include_router(properties.router)
app.include_router(inquiries.router)
app.include_router(agents.router)  # Include the agents router
