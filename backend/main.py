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
     "nombre": "Pikachu", 
     "tipo": "Electrico",
     "pista": "Es un roedor amarillo y la mascota más famosa de la franquicia.",
     "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
     "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"},

    {"id": 2, 
     "nombre": "Charizard", 
     "tipo": "Fuego / Volador",
     "pista": "Lleva una llama en la punta de la cola y escupe fuego capaz de fundir rocas.",
     "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
     "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"},

    {"id": 3, 
     "nombre": "Snorlax", 
     "tipo": "Normal",
     "pista": "Pasa la mayor parte del día durmiendo y come 400 kg de comida al día.",
     "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png",
     "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png"},

    {"id": 4, 
     "nombre": "Gengar", 
     "tipo": "Fantasma / Veneno",
     "pista": "Le gusta esconderse en las sombras de las personas y reducir la temperatura a su alrededor.",
     "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
     "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png"},

    {"id": 5, 
     "nombre": "Jigglypuff", 
     "tipo": "Normal / Hada",
     "pista": "Canta una melodía pegajosa que hace dormir a cualquiera que la escuchey suelen ser muy cariñosos.",
     "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
     "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png"},

    {"id": 6, 
     "nombre": "Bulbasaur", 
     "tipo": "Planta / Veneno",
     "pista": "Tiene una semilla en su espalda que crece con el tiempo.",
     "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png",
     "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png"},

    {"id": 7, 
     "nombre": "Squirtle",
     "tipo": "Agua",
     "pista": "Es un pequeño Pokémon con caparazón que puede disparar agua a alta presión.",
     "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png",
     "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png"},

    {"id": 8, 
     "nombre": "Eevee",
     "tipo": "Normal",
     "pista": "Es conocido por su capacidad de evolucionar en múltiples formas.",
     "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
     "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png"},

    {"id": 9, 
     "nombre": "Mewtwo",
     "tipo": "Psíquico",
     "pista": "Es un Pokémon legendario creado a partir del ADN de Mew.",
     "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
     "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png"},

    {"id": 10,
        "nombre": "Lucario",
        "tipo": "Lucha / Acero",
        "pista": "Es un Pokémon que puede sentir y manipular la energía a su alrededor.",
        "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png"},

    {"id": 11,
        "nombre": "Garchomp",
        "tipo": "Dragón / Tierra",
        "pista": "Es un Pokémon que se asemeja a un tiburón y es muy rápido en tierra.",
        "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/445.png",
        "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/445.png"},

    {"id": 12,
        "nombre": "Greninja",
        "tipo": "Agua / Siniestro",
        "pista": "Es un Pokémon ninja que puede camuflarse con su entorno.",
        "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/658.png",
        "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/658.png"},

    {"id": 13,
        "nombre": "Lapras",
        "tipo": "Agua / Hielo",
        "pista": "Es un Pokémon que puede transportar personas a través del agua y tiene un gran poder de canto.",
        "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/131.png",
        "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/131.png"},

    {"id": 14,
        "nombre": "Butterfree",
        "tipo": "Bicho / Volador",
        "pista": "Es un Pokémon que puede volar y tiene un gran poder de curación.",
        "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/12.png",
        "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/12.png"},

    {"id": 15,
        "nombre": "Alakazam",
        "tipo": "Psíquico",
        "pista": "Es un Pokémon con un gran poder mental y puede mover objetos con su mente.",
        "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
        "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png"},

    {"id": 16,
        "nombre": "Onix",
        "tipo": "Tierra / Roca",
        "pista": "Es un Pokémon que se asemeja a una serpiente de roca y puede excavar túneles subterráneos.",
        "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/95.png",
        "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/95.png"},

    {"id": 17,
        "nombre": "Hawlucha",
        "tipo": "Lucha / Volador",
        "pista": "Es un Pokémon que puede volar y tiene un gran poder de combate.",
        "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/701.png",
        "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/701.png"},

    {"id": 18,
        "nombre": "Noivern",
        "tipo": "Volador / Dragón",
        "pista": "Es un Pokémon que puede volar y tiene un gran poder de combate.",
        "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/715.png",
        "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/715.png"},

    {"id": 19,
        "nombre": "Dedenne",
        "tipo": "Eléctrico / Hada",
        "pista": "Es un Pokémon que puede generar electricidad y tiene un gran poder de curación.",
        "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/607.png",
        "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/607.png"},

    {"id": 20,
        "nombre": "Goodra",
        "tipo": "Dragón / Agua",
        "pista": "Es un Pokémon que puede controlar el agua y tiene un gran poder de combate.",
        "imagen_silueta": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/698.png",
        "imagen_revelada": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/698.png"}
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
        "pista": pokemon["pista"],
        "imagen_silueta": pokemon["imagen_silueta"]
    }

@app.post("/api/validar")
def validar_respuesta(intento: Intento):
    pokemon = next((p for p in POKEDEX_DB if p["id"] == intento.id_pokemon), None)
    if not pokemon:
        return {"error": "Pokemon no encontrado"}
    
    es_correcto = pokemon["nombre"].lower() == intento.respuesta.strip().lower()

    return {
        "correcto": es_correcto,
        "nombre_correcto": pokemon["nombre"],
        "tipo": pokemon["tipo"],
        "imagen_revelada": pokemon["imagen_revelada"]
    }