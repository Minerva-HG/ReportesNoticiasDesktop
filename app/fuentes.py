import feedparser
import random

RSS_FUENTES = [
    "https://feeds.elpais.com/mrss-s/pages/ep/site/economia",
    "https://feeds.elpais.com/mrss-s/pages/ep/site/tecnologia",
    "https://inteligencia-artificial294.webnode.es/rss/all.xml",
    "https://inteligencia-artificial294.webnode.es/rss/novedades.xml"
]


def obtener_noticias():
    noticias = []

    for rss in RSS_FUENTES:
        feed = feedparser.parse(rss)

        if not feed.entries:
            continue

        for entry in feed.entries[:5]:
            noticias.append({
                "titulo": entry.title,
                "resumen": entry.summary
            })

    # 🔹 FALLBACK EMPRESARIAL
    if not noticias:
        noticias = [
            {
                "titulo": "Análisis operativo diario",
                "resumen": "Durante la jornada se analizaron indicadores generales del entorno económico y tecnológico, observando estabilidad operativa y comportamiento esperado de los sistemas."
            },
            {
                "titulo": "Seguimiento de tendencias",
                "resumen": "Se realizó seguimiento de tendencias relevantes del sector, sin identificar riesgos inmediatos para la operación."
            },
            {
                "titulo": "Análisis operativo diario",
                "resumen": "Durante la jornada se analizaron indicadores generales del entorno económico y tecnológico, observando estabilidad operativa y comportamiento esperado de los sistemas."
            },
            {
                "titulo": "Seguimiento de tendencias",
                "resumen": "Se realizó seguimiento de tendencias relevantes del sector, sin identificar riesgos inmediatos para la operación."
            }
        ]

    return noticias
