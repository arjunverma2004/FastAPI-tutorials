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
    def validate_email(cls, value):

        valid_domains = ["hdfc.com", "icici.com"]
        domain = value.split("@")[-1]
        
        if domain not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return value

    @field_validator("name", mode="after")
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator("age", mode="after")
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 120 :
            return value
        raise ValueError("Age must be a positive integer")
        

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


patient1 = Patient(**patient_info)
insert_patient_data(patient1)

