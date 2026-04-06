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
        for entry in feed.entries[:5]:
            noticias.append({
                "titulo": entry.title,
                "resumen": entry.summary
            })

    return random.sample(noticias, min(8, len(noticias)))
