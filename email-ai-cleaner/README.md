# Email AI Cleaner

Fetch emails from Gmail, analyze them using Groq API.

## Deployment on Render

1. Create a Web Service, connect GitHub repo.
2. Set Environment Variables: GROQ_API_KEY, Gmail credentials.
3. Build: `pip install -r requirements.txt`
4. Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
