from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGODB_URI")

cliente = MongoClient(uri)

db = cliente["loja_do_aluno"]

produtos = db["produtos"]