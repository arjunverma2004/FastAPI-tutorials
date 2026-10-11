from pydantic import BaseModel


#Exporting Pydantic models to dictionaries or JSON is a common requirement in many applications, especially when working with APIs or databases. Pydantic provides several methods to achieve this, including model_dump(), model_dump_json(), and model_dump_dict().
class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump() 
temp_json = patient1.model_dump_json()

print(temp)
print(type(temp))