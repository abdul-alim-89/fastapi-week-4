from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    """Intial function"""
    return {"message" : "Welcome to fastapi"}