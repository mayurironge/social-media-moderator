from sqlalchemy import Column, Integer, String
from database import Base


class Analysis(Base):
    __tablename__ = "analysis_history"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String, nullable=False)
    category = Column(String)
    severity = Column(String)
    score = Column(Integer)