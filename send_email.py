import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

def send_email(product_name, price):
    load_dotenv()

    URL_PRODUCT = os.getenv("URL_PRODUCT")
    EMAIL_SENDER = os.getenv("EMAIL_SENDER")
    EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

    body_email = f"""
    <h3>O preço baixou!
    <p>O produto <b>{product_name}</b> atigiu o valor de <b>{price:.2f}</b>.</p>
    <p>Link> <a href="{URL_PRODUCT}">Ver no mercado livre</a></p>
    """

    message = EmailMessage()
    message['Subject'] = f"Aleata de preço: {product_name[:20]}..."
    message['From'] = EMAIL_SENDER
    message['To'] = EMAIL_RECEIVER
    message.set_content(body_email, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_RECEIVER)
            smtp.send_message(message)
        print("Email de alerta enviando com sucesso")
    except Exception as e:
        print(f"falha ao enviar o email: {e}")

