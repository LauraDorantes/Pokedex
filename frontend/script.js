const API_URL = "https://pokedex-msrz.onrender.com";

let pokemonActualId = null;

document.addEventListener("DOMContentLoaded", () => {
    cargarNuevoReto();
});

async function cargarNuevoReto() {
    const imgEl = document.getElementById("pokemon-img");
    const resEl = document.getElementById("resultado");
    const inputEl = document.getElementById("respuesta-input");

    imgEl.className = "silueta";
    resEl.className = "resultado hidden";
    inputEl.value = "";
    inputEl.disabled = false;
    document.getElementById("btn-adivinar").disabled = false;
    document.getElementById("btn-siguiente").classList.add("hidden");
    document.getElementById("pista").textContent = "Consultando al servidor...";
    
    try {
        const response = await fetch(`${API_URL}/api/reto`);
        const data = await response.json();

        pokemonActualId = data.id;
        imgEl.src = data.imagen_silueta;
        document.getElementById("pista").textContent = `💡 Pista: "${data.pista}"`;
    } catch (error) {
        document.getElementById("pista").textContent = "❌ Error al conectar con el servidor Backend.";
        console.error("Error:", error);
    }
}

async function enviarRespuesta() {
  const inputEl = document.getElementById("respuesta-input");
  const respuestaText = inputEl.value;

  if (!respuestaText.trim()) return;

  try {
    const response = await fetch(`${API_URL}/api/validar`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        id_pokemon: pokemonActualId,
        respuesta: respuestaText
      })
    });

    const data = await response.json();

    const imgEl = document.getElementById("pokemon-img");
    const resEl = document.getElementById("resultado");

    // Revelar la imagen quitando la clase 'silueta'
    imgEl.className = "revelado";
    imgEl.src = data.imagen_revelada;

    // Bloquear inputs
    inputEl.disabled = true;
    document.getElementById("btn-adivinar").disabled = true;
    document.getElementById("btn-siguiente").classList.remove("hidden");

    // Mostrar mensaje según el resultado recibido del servidor
    resEl.classList.remove("hidden");
    if (data.correcto) {
      resEl.className = "resultado correcto";
      resEl.textContent = `¡Correcto! 🎉 Es ${data.nombre_correcto} (Tipo: ${data.tipo})`;
    } else {
      resEl.className = "resultado incorrecto";
      resEl.textContent = `¡Incorrecto! ❌ Era ${data.nombre_correcto} (Tipo: ${data.tipo})`;
    }

  } catch (error) {
    console.error("Error al validar respuesta:", error);
  }
}