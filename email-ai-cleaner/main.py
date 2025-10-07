from fastapi import FastAPI
from groq_utils import analyze_emails

app = FastAPI(title="Email AI Cleaner")

@app.get("/analyze_emails")
def analyze(user: str, app_password: str, limit: int = 5):
    results = analyze_emails(user, app_password, limit)
    return {"results": results}
