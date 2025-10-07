import os
from groq import Groq
from email_utils import fetch_emails, extract_email_text, select_email_text

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def analyze_email_context_groq(email_text, interest="project updates, billing, client messages"):
    return client.analyze(text=email_text, interest=interest)

def analyze_emails(user, app_password, limit=5):
    emails = fetch_emails(user, app_password, limit)
    results = []
    for raw_email in emails:
        subject, body = extract_email_text(raw_email)
        email_text = select_email_text(subject, body)
        analysis = analyze_email_context_groq(email_text)
        results.append({"subject": subject, "body": email_text, "analysis": analysis})
    return results
