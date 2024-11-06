import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

# Obtén la clave de cifrado y la URL cifrada desde las variables de entorno
ENCRYPTION_KEY = "RzLqZGkwvrorYhEOB9UOz2DSj6Izc-T76PhYz6ccVbU="
ENCRYPTED_DATABASE_URL = "gAAAAABnKwm6yaAM3D9sA2BNwkL1NnsUZlr8n0g93fD7f8BMQBX5vq5aeqLPQJfM-GDPkLPva4AGCVUyqZsk4gzJ0rhbOpraEmjQEKEAOffWZPxVci78kaz2lAzfdrJKBOFhYBhP8TmskRWL_-n_tluKv3syozbYBf77t4yRu3lYB2b2Hk3Fr66j3u8UsnyP7gCXfhMnVhxVBJedLKYgFFU6H6s0NQsjpGeP1z6242OL5Z32UNyhD3nZuEJC_XpxKlJhi_ze-kqR"

# Inicializa el objeto de cifrado
cipher_suite = Fernet(ENCRYPTION_KEY)

def get_database_url():
    # Desencripta la `DATABASE_URL`
    decrypted_url = cipher_suite.decrypt(ENCRYPTED_DATABASE_URL.encode()).decode()
    return decrypted_url

DATABASE_URL = get_database_url()
