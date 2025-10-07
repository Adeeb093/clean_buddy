import imaplib
import email

def fetch_emails(user, app_password, limit=5):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(user, app_password)
    mail.select("inbox")
    result, data = mail.search(None, "ALL")
    email_ids = data[0].split()
    latest_email_ids = email_ids[-limit:]
    emails = []
    for e_id in latest_email_ids:
        result, msg_data = mail.fetch(e_id, "(RFC822)")
        raw_email = msg_data[0][1]
        emails.append(raw_email)
    mail.logout()
    return emails
