import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

# Obtén la clave de cifrado y la URL cifrada desde las variables de entorno
ENCRYPTION_KEY = "oiLuaj4newXDLmHUOVM_iKkHCl6Gjh_dytC-5vgx5rA="
ENCRYPTED_DATABASE_URL = "gAAAAABnMXA3Oou0gr5R5zdzyaEcESTjUeBiec20-uLx2Xg5ucLQM7XnWUj0sm_8OeQNuPuP1Nuz3I6jZ0ajRIJoivH-HsJoDYB196C4-z92ggJq2qunDGRcx3XQNjqZMEl4BKPj-fy16JSFVdJXqrXqTHgEZ5u7tUReqRQcUhd1P2wDok1Zwdk1Lym7HvE9j0KBUUQJ9RfGJ2v6DGLqZVULV3GgI2HPY7GqJLxAzWPYPvW3-nsb5jMa7TewGFS5dfld98lc4hE2"

# Inicializa el objeto de cifrado
cipher_suite = Fernet(ENCRYPTION_KEY)

def get_database_url():
    # Desencripta la `DATABASE_URL`
    decrypted_url = cipher_suite.decrypt(ENCRYPTED_DATABASE_URL.encode()).decode()
    return decrypted_url

DATABASE_URL = get_database_url()
