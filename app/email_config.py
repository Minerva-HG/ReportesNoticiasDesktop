import os

SMTP_SERVIDOR = "smtp.gmail.com"
SMTP_PUERTO = 587

EMAIL_REMITENTE = os.environ.get("EMAIL_REMITENTE", "minializgodinez@gmail.com")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD", "")

DESTINATARIOS = [
    "minializ@hotmail.com",
    "mihernandezg@megacable.com.mx"
]