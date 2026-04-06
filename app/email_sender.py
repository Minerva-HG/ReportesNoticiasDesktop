import smtplib
import os
from email.message import EmailMessage
from email_config import (
    SMTP_SERVIDOR,
    SMTP_PUERTO,
    EMAIL_REMITENTE,
    EMAIL_PASSWORD,
    DESTINATARIOS
)

def enviar_correo(asunto, html_body, archivos_adjuntos):
    msg = EmailMessage()
    msg["From"] = EMAIL_REMITENTE
    msg["To"] = ", ".join(DESTINATARIOS)
    msg["Subject"] = asunto

    # ✅ HTML
    msg.set_content("Este correo requiere un cliente compatible con HTML.")
    msg.add_alternative(html_body, subtype="html")

    for archivo in archivos_adjuntos:
        if not os.path.exists(archivo):
            continue

        with open(archivo, "rb") as f:
            data = f.read()

        nombre = os.path.basename(archivo)
        msg.add_attachment(
            data,
            maintype="application",
            subtype="octet-stream",
            filename=nombre
        )

    with smtplib.SMTP(SMTP_SERVIDOR, SMTP_PUERTO) as server:
        server.starttls()
        server.login(EMAIL_REMITENTE, EMAIL_PASSWORD)
        server.send_message(msg)