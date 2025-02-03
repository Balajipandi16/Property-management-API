

---

# **Property Estate API**  

### **Overview**  
This project is a FastAPI-based system for managing real estate properties, agents, and customer inquiries. It includes features for:  
- Adding and retrieving properties  
- Managing agent assignments  
- Handling customer inquiries  
- Preventing duplicate inquiries for agents  
- Tracking property availability  

---

## **Project Structure**  

```
milestoneProject/
│── app/
│   │── api/
│   │   │── properties.py   # API routes for property management
│   │   │── inquiries.py    # API routes for handling inquiries
│   │   │── agents.py       # API routes for managing agents
│   │── models.py           # SQLAlchemy models
│   │── schemas.py          # Pydantic schemas for request validation
│   │── db.py               # Database connection and session management
│   │── database.py         # SQLAlchemy database configuration
│   │── __init__.py
│── main.py                 # FastAPI entry point
│── requirements.txt        # Project dependencies
│── README.md               # Documentation
│── .env                    # Environment variables
│── migrations/             # Alembic database migrations
```

---

## **Installation & Setup**  

### **Prerequisites**  
- Python 3.8+
- PostgreSQL  
- FastAPI  
- SQLAlchemy  
- Uvicorn  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/real-estate-api.git
cd real-estate-api
```

### **2️⃣ Create & Activate Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**  
Create a `.env` file and add the following:  
```
DATABASE_URL=postgresql://username:password@localhost:5432/real_estate_db
```

### **5️⃣ Run Database Migrations**  
```bash
alembic upgrade head
```

### **6️⃣ Start the FastAPI Server**  
```bash
uvicorn main:app --reload
```

---

## **API Endpoints**  

### **1️⃣ Property Management**  

| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/properties/{property_id}` | Fetch property details by ID |
| **POST** | `/properties/` | Create a new property |
| **POST** | `/properties/{property_id}/update_availability` | Mark property as unavailable |

#### **Example Request (Create Property)**
```json
{
  "title": "Luxury Apartment",
  "description": "A spacious 3BHK apartment.",
  "price": 200000,
  "available": true
}
```

### **2️⃣ Agent Management**  

| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/agents/` | Fetch all agents |
| **POST** | `/agents/` | Add a new agent |
| **POST** | `/agents/{agent_id}/assign_inquiry/{inquiry_id}` | Assign an inquiry to an agent |

### **3️⃣ Inquiry Management**  

| Method | Endpoint | Description |
|--------|---------|-------------|
| **POST** | `/inquiries/` | Submit an inquiry |
| **GET** | `/inquiries/{inquiry_id}` | Get details of an inquiry |
| **GET** | `/agents/{agent_id}/inquiries` | Get inquiries assigned to an agent |

#### **Example Request (Submit Inquiry)**
```json
{
  "property_id": 1,
  "user_id": 2,
  "message": "I am interested in this property."
}
```

---

## **Running Tests**  
Run the test suite using:  
```bash
pytest
```

---

## **Contributing**  
1. Fork the repository  
2. Create a new branch (`feature-branch`)  
3. Commit changes and push to your fork  
4. Submit a pull request  

---


