from fastapi import FastAPI

app = FastAPI(title="Smart Inventory Sync API")

@app.get("/")
def read_root():
    return {"message": "Welcome to Smart Inventory Sync API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}