from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI(title = "Pokedex API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

POKEDEX_DB = [
    {"id": 1, 
     "name": "Pikachu", 
     "type": "Electrico",
     "clue": "Es un roedor amarillo y la mascota más famosa de la franquicia.",
     "img_siluette": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
     "img_full": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"},

    {"id": 2, 
     "name": "Charizard", 
     "type": "Fuego / Volador",
     "clue": "Lleva una llama en la punta de la cola y escupe fuego capaz de fundir rocas.",
     "img_siluette": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"},

    {"id": 3, 
     "name": "Snorlax", 
     "type": "Normal",
     "clue": "Pasa la mayor parte del día durmiendo y come 400 kg de comida al día.",
     "img_siluette": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png",
     "img_full": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png"},

    {"id": 4, 
     "name": "Gengar", 
     "type": "Fantasma / Veneno",
     "clue": "Le gusta esconderse en las sombras de las personas y reducir la temperatura a su alrededor.",
     "img_siluette": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png"},

    {"id": 5, 
     "name": "Jigglypuff", 
     "type": "Normal / Hada",
     "clue": "Canta una melodía pegajosa que hace dormir a cualquiera que la escuchey suelen ser muy cariñosos.",
     "img_siluette": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
     "img_full": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png"}
]

class Intento(BaseModel):
    id_pokemon: int
    respuesta: str

@app.get("/")
def home():
    return {"message": "Bienvenido a la Pokedex API"}

@app.get("/api/reto")
def obtener_reto():
    pokemon = random.choice(POKEDEX_DB)
    return {
        "id": pokemon["id"],
        "clue": pokemon["clue"],
        "img_siluette": pokemon["img_siluette"]
    }

@app.post("/api/validar")
def validar_respuesta(intento: Intento):
    pokemon = next((p for p in POKEDEX_DB if p["id"] == intento.id_pokemon), None)
    if not pokemon:
        return {"error": "Pokemon no encontrado"}
    
    es_correcto = pokemon["name"].lower() == intento.respuesta.strip().lower()

    return {
        "correcto": es_correcto,
        "nombre_correcto": pokemon["name"].capitalize(),
        "tipo": pokemon["type"],
        "imagen_revelada": pokemon["img_full"]
    }