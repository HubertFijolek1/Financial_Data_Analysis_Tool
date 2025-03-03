from fastapi import FastAPI, Depends
from external_api import fetch_external_data
from sqlalchemy.orm import Session
from config import SessionLocal
from finance.aggregation import aggregate_financials
from fastapi.responses import Response, StreamingResponse
from finance.pdf_report import generate_financial_pdf
from finance.chart import generate_financial_chart
import io

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/financials/report/pdf", tags=["Reports"])
async def financial_report_pdf(db: Session = Depends(get_db)):
    """
    Generate and return a PDF financial report.
    """
    records_query = db.query(FinancialRecord).all()
    records = [
        {
            "record_date": str(record.record_date),
            "revenue": record.revenue,
            "expense": record.expense,
            "profit": record.profit,
        }
        for record in records_query
    ]
    pdf_data = generate_financial_pdf(records)
    return Response(content=pdf_data, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=financial_report.pdf"})

@app.get("/financials/chart", tags=["Reports"])
async def financial_chart(db: Session = Depends(get_db)):
    """
    Generate a dynamic chart (PNG image) for financial revenue trends.
    """
    records_query = db.query(FinancialRecord).all()
    records = [
        {
            "record_date": str(record.record_date),
            "revenue": record.revenue,
        }
        for record in records_query
    ]
    chart_image = generate_financial_chart(records)
    return StreamingResponse(io.BytesIO(chart_image), media_type="image/png")

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

