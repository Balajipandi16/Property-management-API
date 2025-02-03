from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base



class Property(Base):
    __tablename__ = "properties"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    price = Column(Integer)
    available = Column(Boolean)

    # Relationship with Inquiry
    inquiries = relationship("Inquiry", back_populates="property")

class Agent(Base):
    __tablename__ = 'agents'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True)
    
    # Relationship to track inquiries handled by this agent
    inquiries = relationship("Inquiry", back_populates="agent")

class Inquiry(Base):
    __tablename__ = 'inquiries'

    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey('properties.id'))
    user_id = Column(Integer)
    message = Column(String)
    agent_id = Column(Integer, ForeignKey('agents.id'))  # Link inquiry to agent

    agent = relationship("Agent", back_populates="inquiries")
    property = relationship("Property", back_populates="inquiries")





