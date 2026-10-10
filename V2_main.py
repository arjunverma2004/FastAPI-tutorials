from fastapi import FastAPI

app = FastAPI()

@app.get("/") #route for the endpoint
def hello():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {"message": "This is a FastAPI application."}

# To run the FastAPI application, use the command:
# uvicorn V2_main:app --reload