import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGODB_URI")

if not uri:
    raise RuntimeError("Defina MONGODB_URI no arquivo .env (veja o .env.example).")

# Se o Mongo não responder em 5 s, falha com erro claro em vez de travar.
cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)

db = cliente["loja_do_aluno"]

produtos = db["produtos"]