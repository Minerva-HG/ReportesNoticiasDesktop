from email_sender import enviar_correo

enviar_correo(
    asunto="Prueba SMTP",
    html_body="<h2>Correo de prueba exitoso</h2>",
    archivos_adjuntos=[]
)