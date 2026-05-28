from fastapi import FastAPI
from pydantic import BaseModel
from core.form_analyzer import ANALYZERS

class AnalyzeRequest(BaseModel):
    exercise: str
    angles: dict
    
app = FastAPI()

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    analyzer = ANALYZERS[request.exercise]
    feedback = analyzer.analyse(request.angles)
    return {"feedback": feedback}

@app.get("/health")
def health_check():
    return {"status": "ok"}



