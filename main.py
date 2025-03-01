from fastapi import FastAPI
from external_api import fetch_external_data

app = FastAPI()

@app.get("/external-data")

async def get_external_data(url: str):

    """Fetch data from an external API asynchronously."""

    data = await fetch_external_data(url)

    return {"data": data}

    title="Financial Data Analysis Tool",
    description="An internal tool for processing and analyzing financial data.",
    version="0.1.0"


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Financial Data Analysis Tool API"}
