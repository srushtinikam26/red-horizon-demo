from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Red Horizon Backend Running"}