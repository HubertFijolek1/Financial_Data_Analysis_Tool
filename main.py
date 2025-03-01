from fastapi import FastAPI

app = FastAPI(
    title="Financial Data Analysis Tool",
    description="An internal tool for processing and analyzing financial data.",
    version="0.1.0"
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Financial Data Analysis Tool API"}
