from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient (BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Emergency contact is required for patients over 60")

patient_info = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@hdfc.com",
    "weight": 72.5,
    "married": True,
    "allergies": ["Peanuts", "Shellfish"],
    "contact_details": {"email": "john.doe@hdfc.com", "phone": "123-456-7890"}
    }

def insert_patient_data(patient: Patient):
    print("Age: ", patient.age)
    print("Name: ", patient.name)
    print("Allergies: ", patient.allergies)
    print("Contact Details: ", patient.contact_details)
    print("Patient data inserted successfully.")

insert_patient_data(Patient(**patient_info))