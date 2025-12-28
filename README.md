# Lyrics-Based Song Recommender

Sistema de recomendación de canciones basado en la **similitud semántica de las letras** usando **embeddings** (Sentence Transformers).

La aplicación permite:
- Recomendar canciones similares a otra canción
- Recomendar canciones a partir de una descripción emocional o situación personal
- No almacena letras completas (solo embeddings, por lo que es eficiente en espacio)
- Arquitectura MVC

---

## Funcionalidades

### ●) Modo 1 – Recomendación por canción
El usuario introduce una canción (vía URL de Genius) y la app recomienda canciones con letras similares.

### ●) Modo 2 – Recomendación por texto / estado emocional
El usuario describe lo que siente (ej: ruptura, tristeza, motivación) y la app recomienda canciones cuyas letras expresan lo mismo.

---

## Arquitectura del proyecto
```
lyrics-song-recommender/
├── app_streamlit.py # Interfaz web (Streamlit)
├── run_api.py # API FastAPI (opcional)
├── requirements.txt
│
├── data/
│ ├── metadata.csv # Metadatos de canciones (sin letras)
│ ├── embeddings.npy # Matriz de embeddings (Nx768)
│
├── models/
│ ├── embedder.py # Generación de embeddings
│ ├── similarity.py # Similaridad coseno
│
├── services/
│ ├── genius_client.py # Obtención de letras (temporal)
│ ├── recommender.py # Lógica principal de recomendación
│ ├── dataset_builder.py # Construcción del dataset inicial
│
├── controllers/
│ ├── cli_controller.py # Interfaz por consola
│ ├── api_controller.py # Endpoints FastAPI
```
## Tecnologías usadas

- Python 3.10+
- Sentence Transformers
- NumPy / Pandas
- Streamlit
- FastAPI
- Genius API
- Spotify API (solo para generar dataset inicial)


## Instalación

Clona el repositorio:

```
git clone https://github.com/mbatla00/lyrics-song-recommender.git
cd lyrics-music-recommender
```

Instala dependencias:
```
pip install -r requirements.txt
```

## APIs necesarias

### Genius API (obligatoria)
Usada para obtener letras solo en tiempo de ejecución.
1. https://genius.com/api-clients
2. Crea una app
3. Copia el Access Token
4. Pégalo en los archivos donde se indica

### Spotify API (opcional, solo para crear dataset)
Usada para obtener listas de canciones automáticamente.
1. https://developer.spotify.com/dashboard
2. Crea una app
3. Copia:
- Client ID
- Client Secret

## Crear el dataset inicial
```
python services/dataset_builder.py
```
Esto genera:
- data/metadata.csv
- data/embeddings.npy
Las letras NO se guardan.

## Ejecutar la app (Streamlit)
```
streamlit run app_streamlit.py
```
Se abrirá en:
```
http://localhost:8501
```

## Ejemplos de uso

- “Dame canciones similares a drivers license”
- “Me ha dejado mi pareja y quiero canciones tristes”
- “Quiero música chill para estudiar”
