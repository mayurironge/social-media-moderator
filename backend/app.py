from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Analysis
from fastapi import FastAPI
from database import engine
from models import Base
from schema import AnalyzeRequest
from services.analyzer import analyze_comment
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from models import Analysis
Base.metadata.create_all(bind=engine)


app = FastAPI(title="Social Media Moderator API")


@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/analyze")
def analyze(request: AnalyzeRequest, db: Session = Depends(get_db)):

    result = analyze_comment(request.text)

    record = Analysis(
        comment=request.text,
        category=result["category"],
        severity=result["severity"],
        score=result["score"]
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return result

@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    history = db.query(Analysis).all()
    return history