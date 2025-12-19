from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Electricity Bill Web API is running"}
