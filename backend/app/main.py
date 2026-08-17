from fastapi import FastAPI

app = FastAPI(
    title="Home Library API",
    description="API for managing a home library",
    version="0.1.0",
)

@app.get("/")
def root():
    return {"message": "Home Library API is running"}
