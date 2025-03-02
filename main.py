from fastapi import FastAPI, Depends
from external_api import fetch_external_data
from sqlalchemy.orm import Session
from config import SessionLocal
from finance.aggregation import aggregate_financials

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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



@app.get("/financials/report", tags=["Reports"])
async def financial_report(db: Session = Depends(get_db)):
    """
    Return aggregated financial data.
    """
    report = aggregate_financials(db)
    return report

