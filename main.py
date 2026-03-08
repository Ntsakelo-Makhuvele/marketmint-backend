from fastapi import FastAPI

app = FastAPI(title="Market Mint API", description="API for Market Mint application", version="1.0.0")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Market Mint API!"}


