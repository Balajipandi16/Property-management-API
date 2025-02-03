from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Inquiry  # Direct import from models
from app.schemas import InquiryCreate, InquiryResponse

router = APIRouter()

@router.post("/inquiries/", response_model=InquiryResponse)
def create_inquiry(inquiry: InquiryCreate, db: Session = Depends(get_db)):
    existing_inquiry = db.query(Inquiry).filter(
        Inquiry.property_id == inquiry.property_id,
        Inquiry.user_id == inquiry.user_id
    ).first()

    if existing_inquiry:
        raise HTTPException(status_code=400, detail="Inquiry already submitted for this property by the user.")

    db_inquiry = Inquiry(**inquiry.dict())
    db.add(db_inquiry)
    db.commit()
    db.refresh(db_inquiry)
    return db_inquiry
