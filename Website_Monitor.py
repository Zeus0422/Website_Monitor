import smtplib
import requests

EMAIL_ADDRESS = "carloseckert05coding@gmail.com"
EMAIL_PASSWORD = ""


r = requests.get("", timeout=0.1)
a = 0

while 0 == 0 and a == 0:
    if r.status_code != 200 or not r.ok:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = "Alert-from-Python-Script"
            body = "a"
            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(EMAIL_ADDRESS, "carloseckert05coding@gmail.com", msg)
            print("a")

        a = 1
        Print: "Email sent"
