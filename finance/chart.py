import matplotlib.pyplot as plt
import io
from fastapi.responses import Response

def generate_financial_chart(records: list):
    """
    Generate a line chart for financial revenue trends.
    Expects records as a list of dicts with 'record_date' and 'revenue'.
    """
    dates = [record["record_date"] for record in records]
    revenues = [record["revenue"] for record in records]

    plt.figure(figsize=(8, 4))
    plt.plot(dates, revenues, marker='o', linestyle='-', color='b')
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.title("Financial Revenue Trend")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return buf.read()
