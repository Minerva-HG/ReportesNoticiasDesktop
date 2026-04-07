
# Información del reporte
EMPRESA = "Reporte Ejecutivo Diario"
AUTOR = "Sistema Automatizado de Análisis"

# Duración total
DURACION_TOTAL_HORAS = 1

# Frecuencia de documentos
INTERVALO_DOCUMENTOS_MIN = 10

# Cálculo automático (NO TOCAR)
DOCUMENTOS_TOTALES = int((DURACION_TOTAL_HORAS * 60) / INTERVALO_DOCUMENTOS_MIN)

# Correos
INTERVALO_ENVIO_HORAS = 0.5

# UI / progreso
BLOQUES = DOCUMENTOS_TOTALES