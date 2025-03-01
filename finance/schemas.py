from pydantic import BaseModel, Field
from datetime import date, datetime

class FinancialRecordBase(BaseModel):
    record_date: date
    revenue: float = Field(..., gt=0)
    expense: float = Field(..., ge=0)

class FinancialRecordCreate(FinancialRecordBase):
    pass

class FinancialRecord(FinancialRecordBase):
    id: int
    profit: float
    class Config:
        orm_mode = True

class ExternalDataBase(BaseModel):
    source: str
    data_value: float
    timestamp: datetime

class ExternalDataCreate(ExternalDataBase):
    pass

class ExternalData(ExternalDataBase):
    id: int
    class Config:
        orm_mode = True
