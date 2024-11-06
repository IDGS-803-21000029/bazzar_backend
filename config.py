import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

# Obtén la clave de cifrado y la URL cifrada desde las variables de entorno
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
ENCRYPTED_DATABASE_URL = os.getenv("ENCRYPTED_DATABASE_URL")
\
print("Clave de cifrado:", ENCRYPTION_KEY)
print("URL cifrada:", ENCRYPTED_DATABASE_URL)

# Inicializa el objeto de cifrado
cipher_suite = Fernet(ENCRYPTION_KEY)

def get_database_url():
    # Desencripta la `DATABASE_URL`
    decrypted_url = cipher_suite.decrypt(ENCRYPTED_DATABASE_URL.encode()).decode()
    return decrypted_url

DATABASE_URL = get_database_url()
