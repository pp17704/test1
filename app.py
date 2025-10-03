from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Arjuna from FastAPI battlefield!"}

@app.get("/health")
def health_check():
    return {"status": "UP"}

