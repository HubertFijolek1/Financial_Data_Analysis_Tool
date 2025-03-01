from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FinancialRecord(Base):
    __tablename__ = "financial_records"

    id = Column(Integer, primary_key=True, index=True)
    record_date = Column(Date, nullable=False)
    revenue = Column(Float, nullable=False)
    expense = Column(Float, nullable=False)
    profit = Column(Float, nullable=False)

class ExternalData(Base):
    __tablename__ = "external_data"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, nullable=False)
    data_value = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)