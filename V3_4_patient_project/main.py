from fastapi import FastAPI, Path, HTTPException, Query
import json


def load_data():
    with open("patient.json", "r") as file:
        data = json.load(file)
    return data 
 
app = FastAPI()

@app.get("/") #route for the endpoint
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "A fully functional and efficient patient management system."}

@app.get("/view")
def view_patients():
    data = load_data()
    return data


#Path parameter to view a specific patient by ID
@app.get("/view/{patient_id}") 
def view_patient(patient_id: str = Path(..., description="ID of the patient", example="P001")): # '...' indicates that the parameter is required
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="sort on basis of height, weight or age", example="name"), order: str = Query("asc", description="Order of sorting: asc or desc", example="asc")):
    
    valid_fields = ["height", "weight", "age"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field select from {valid_fields}")

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order value. Use 'asc' or 'desc'.")

    data = load_data()
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=(order == "desc"))

    return sorted_data


# To run the FastAPI application, use the command:
# uvicorn V3_patient_project/main:app --reload