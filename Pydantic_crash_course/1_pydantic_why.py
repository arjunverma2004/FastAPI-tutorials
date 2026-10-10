from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50)]
    age: Annotated[int, Field(..., gt=0, description="Age must be greater than 0")]
    weight: Annotated[float, Field(..., gt=0, strict=True, description="Weight must be greater than 0")]

    #This Annotated helps to add metadata to the fields. This strict=True that pydantic will not allow any type coercion (convert '72.5' to 72.5) for the weight field. It must be a float and cannot be an integer or string.

    email: Optional[EmailStr] = None
    linkedin_profile: Optional[AnyUrl] = None

    Allergier: Optional[List[str]] = Field(default_factory=list, description="List of allergies") 
    #We used List[str] instead of list to also validate the list contains strings. None at last is the default value for Allergier if not provided.

    married: Optional[bool] = None
    contact_info: Dict[str, str] = Field(default_factory=dict, description="Contact information as a dictionary")

patient_info = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "Allergier": ["Peanuts", "Shellfish"],
    "contact_info": {"email": "john.doe@example.com", "phone": "123-456-7890"}
    }

def insert_patient_data(patient: Patient):
    print("Age: ", patient.age)
    print("Name: ", patient.name)
    print("Allergies: ", patient.Allergier)
    print("Contact Info: ", patient.contact_info)
    print("Patient data inserted successfully.")


patient1 = Patient(**patient_info)
insert_patient_data(patient1)

