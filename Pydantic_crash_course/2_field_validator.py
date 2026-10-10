from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email address")
        return v

patient_info = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "weight": 72.5,
    "married": True,
    "allergies": ["Peanuts", "Shellfish"],
    "contact_details": {"email": "john.doe@example.com", "phone": "123-456-7890"}
    }

def insert_patient_data(patient: Patient):
    print("Age: ", patient.age)
    print("Name: ", patient.name)
    print("Allergies: ", patient.allergies)
    print("Contact Details: ", patient.contact_details)
    print("Patient data inserted successfully.")


patient1 = Patient(**patient_info)
insert_patient_data(patient1)

