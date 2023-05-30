from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikilogic
from mylib.logic import phrase as wikiphrases

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Pagina a buscar en Wikipedia"""
    result = search_wiki(value)
    return {"Result": result}


@app.get("/wiki/{value}")
async def wiki(value: str):
    """Consultar Wikipedia"""
    result = wikilogic(value)
    return {"Result": result}

@app.get("/phrase/{value}")
async def phrase(value: str):
    """Consultar Wikipedia y extraer frases"""
    result = wikiphrases(value)
    return {"Result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
