import email
from email import policy

def extract_email_text(raw_email):
    msg = email.message_from_bytes(raw_email, policy=policy.default)
    subject = msg["subject"]
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body += part.get_payload(decode=True).decode()
    else:
        body = msg.get_payload(decode=True).decode()
    return subject, body
