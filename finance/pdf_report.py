from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_financial_pdf(records: list):
    """
    Generate a PDF report for a list of financial records.
    Each record should be a dict with keys: record_date, revenue, expense, profit.
    """
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    p.setFont("Helvetica", 12)
    p.drawString(50, height - 50, "Financial Report")
    y = height - 80

    for record in records:
        line = f"Date: {record['record_date']}, Revenue: {record['revenue']}, Expense: {record['expense']}, Profit: {record['profit']}"
        p.drawString(50, y, line)
        y -= 20
        if y < 50:
            p.showPage()
            y = height - 50

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf