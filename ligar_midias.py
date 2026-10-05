"""Liga imagens, vídeos e modelos 3D aos produtos do MongoDB automaticamente.

Regra: o arquivo tem o nome do produto, em minúsculas, sem acento e com hífen
no lugar dos espaços. Exemplos:
    "mouse gamer"          -> mouse-gamer.jpg / mouse-gamer.mp4 / mouse-gamer.glb
    "headset gamer LENOVO" -> headset-gamer-lenovo.jpg
    "placa de video"       -> placa-de-video.jpg

Pastas:
    static/imagens  (.jpg .jpeg .png .webp)
    static/videos   (.mp4 .webm)
    static/modelos  (.glb)

Rode na raiz do projeto:  python ligar_midias.py
"""
import os
import re
import unicodedata

from database.conexao import produtos

PASTAS = {
    "imagem": ("static/imagens", (".jpg", ".jpeg", ".png", ".webp")),
    "video": ("static/videos", (".mp4", ".webm")),
    "modelo3d": ("static/modelos", (".glb",)),
}


def slug(texto):
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", texto.lower()).strip("-")


def achar(pasta, extensoes, nome):
    for ext in extensoes:
        if os.path.exists(os.path.join(pasta, nome + ext)):
            return nome + ext
    return None


for p in produtos.find():
    nome = p.get("produto", "")
    s = slug(nome)

    campos = {}
    for campo, (pasta, extensoes) in PASTAS.items():
        arquivo = achar(pasta, extensoes, s)
        if arquivo:
            campos[campo] = arquivo

    if campos:
        produtos.update_one({"_id": p["_id"]}, {"$set": campos})

    ligado = ", ".join(campos) if campos else "nada encontrado"
    print(f"{nome:<28} nome do arquivo: {s:<28} ligado: {ligado}")