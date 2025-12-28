import numpy as np
from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        """
        Constructor de la clase. 
        Se ejecuta al crear el objeto: e = Embedder()
        """
        print("🔄 Cargando modelo de embeddings...")

        # Descarga y carga el modelo 'all-mpnet-base-v2' (uno de los mejores para inglés)
        # Este modelo convierte frases en vectores de 768 números.
        self.model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
        
        print("✅ Modelo cargado")

    def encode(self, text: str) -> np.ndarray:
        """
        Convierte un texto (letra de canción) en un vector numérico normalizado.
        """
        # 1. Genera el embedding inicial usando la red neuronal
        emb = self.model.encode(text, convert_to_numpy=True)
        
        # 2. Normalización L2 (Paso clave para buscadores)
        # Divide el vector por su norma (longitud). 
        # Esto hace que todos los vectores midan 1, facilitando comparar canciones 
        # por su 'ángulo' o similitud de coseno más adelante.
        emb = emb / np.linalg.norm(emb)
        
        # Imprime la forma del vector (ej. (768,)) para confirmar que es correcto
        print("🧠 Embedding generado:", emb.shape)
        
        return emb