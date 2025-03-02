from sqlalchemy.orm import Session
from finance.models import FinancialRecord
from sqlalchemy import func

def aggregate_financials(db: Session):
    """
    Returns aggregated financial data: total revenue, total expense, average profit.
    """
    total_revenue = db.query(func.sum(FinancialRecord.revenue)).scalar() or 0.0
    total_expense = db.query(func.sum(FinancialRecord.expense)).scalar() or 0.0
    avg_profit = db.query(func.avg(FinancialRecord.profit)).scalar() or 0.0
    return {
        "total_revenue": total_revenue,
        "total_expense": total_expense,
        "average_profit": avg_profit,
    }
