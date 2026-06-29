import smtplib

EMAIL = "your_email@gmail.com"

PASSWORD = "your_app_password"


def send_email(receiver, subject, body):

    message = f"Subject:{subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:

        server.starttls()

        server.login(EMAIL, PASSWORD)

        server.sendmail(
            EMAIL,
            receiver,
            message
        )

    return "Email Sent Successfully"