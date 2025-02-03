from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Property, Inquiry
from app.schemas import PropertyCreate, PropertyResponse, InquiryCreate, InquiryResponse
from app.database import get_db

router = APIRouter()

# Route to create a new property
@router.post("/properties/", response_model=PropertyResponse)
def create_property(property: PropertyCreate, db: Session = Depends(get_db)):
    try:
        new_property = Property(
            title=property.title,
            description=property.description,
            price=property.price,
            available=property.available
        )
        db.add(new_property)
        db.commit()
        db.refresh(new_property)
        return new_property
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating property: {str(e)}")

# Route to get a property by its ID
@router.get("/properties/{property_id}", response_model=PropertyResponse)
def get_property(property_id: int, db: Session = Depends(get_db)):
    property = db.query(Property).filter(Property.id == property_id).first()
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    return property

# Route to create an inquiry
@router.post("/inquiries/", response_model=InquiryResponse)
def create_inquiry(inquiry: InquiryCreate, db: Session = Depends(get_db)):
    # Check for duplicate inquiry by the same user
    existing_inquiry = db.query(Inquiry).filter(Inquiry.property_id == inquiry.property_id, Inquiry.user_id == inquiry.user_id).first()
    if existing_inquiry:
        raise HTTPException(status_code=400, detail="Inquiry already exists for this property by this user")

    new_inquiry = Inquiry(
        property_id=inquiry.property_id,
        user_id=inquiry.user_id,
        message=inquiry.message
    )
    db.add(new_inquiry)
    db.commit()
    db.refresh(new_inquiry)
    return new_inquiry

# Route to get inquiries for a specific property
@router.get("/properties/{property_id}/inquiries", response_model=list[InquiryResponse])
def get_inquiries(property_id: int, db: Session = Depends(get_db)):
    inquiries = db.query(Inquiry).filter(Inquiry.property_id == property_id).all()
    return inquiries
