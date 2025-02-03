from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Agent, Inquiry
from app.schemas import InquiryResponse

router = APIRouter()

# Endpoint to assign an inquiry to an agent
@router.post("/agents/{agent_id}/assign_inquiry/{inquiry_id}", response_model=InquiryResponse)
def assign_inquiry_to_agent(agent_id: int, inquiry_id: int, db: Session = Depends(get_db)):
    # Fetch the agent from the database
    db_agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")

    # Fetch the inquiry from the database
    db_inquiry = db.query(Inquiry).filter(Inquiry.id == inquiry_id).first()
    if db_inquiry is None:
        raise HTTPException(status_code=404, detail="Inquiry not found")

    # Assign the inquiry to the agent
    db_inquiry.agent_id = agent_id
    db.commit()
    db.refresh(db_inquiry)

    return db_inquiry
