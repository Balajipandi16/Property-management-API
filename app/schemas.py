from pydantic import BaseModel

# Schema for creating a new Property
class PropertyCreate(BaseModel):
    title: str
    description: str
    price: int
    available: bool

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models


# Schema for creating a new Inquiry
class InquiryCreate(BaseModel):
    property_id: int
    user_id: int
    message: str

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models


# Schema for a Property response (can be used in GET requests)
class PropertyResponse(BaseModel):
    id: int
    title: str
    description: str
    price: int
    available: bool

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models


# Schema for Inquiry response (can be used in GET requests)
class InquiryResponse(BaseModel):
    id: int
    property_id: int
    user_id: int
    message: str

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models


# Optional: Schema for list responses
class PropertyListResponse(BaseModel):
    id: int
    title: str
    price: int
    available: bool

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models


class InquiryListResponse(BaseModel):
    id: int
    property_id: int
    user_id: int

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models


from typing import List, Optional

# Schema for creating an Agent
class AgentCreate(BaseModel):
    name: str
    email: str
    phone: str

    class Config:
        orm_mode = True

# Schema for updating Agent details
class AgentUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]

    class Config:
        orm_mode = True

# Schema for Agent Response (used for GET requests)
class AgentResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    inquiries: List[str]  # List of inquiry messages handled by the agent

    class Config:
        orm_mode = True
