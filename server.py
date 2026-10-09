from flask import Flask, jsonify, render_template, request
from flask import Flask, jsonify, render_template
from database.conexao import produtos
from database.registrar_venda import efetuar_pedido, efetuar_venda
from relatorio.vendas import obter_estatisticas_produtos, obter_relatorio_segmentado
from relatorio.machine_learning import classificar_produtos_ia
from relatorio.previsao import prever_faturamento_mensal 
from flask import Flask, jsonify
from relatorio.vendas import obter_estatisticas_produtos

app = Flask(__name__)


# Palavra-chave no nome do produto -> ícone desenhado no carrossel.
# A ordem importa: "mousepad" precisa vir antes de "mouse".
ICONES = [
    ("placa de video", "gpu"),
    ("placa de desenvolvimento", "chip"),
    ("mousepad", "pad"),
    ("mouse", "mouse"),
    ("teclado", "kb"),
    ("cadeira", "chair"),
    ("headset", "head"),
    ("monitor", "mon"),
    ("microfone", "mic"),
    ("memoria", "ram"),
    ("computador", "pc"),
    ("kit", "chip"),
]


def url_midia(valor, pasta):
    """Aceita só o nome do arquivo (ex.: mouse.glb) ou uma URL completa."""
    if not valor:
        return None
    valor = str(valor)
    if valor.startswith(("http://", "https://", "/")):
        return valor
    return f"/static/{pasta}/{valor}"


def icone_para(nome):
    nome = nome.lower()
    for chave, icone in ICONES:
        if chave in nome:
            return icone
    return "chip"
@app.route('/dashboard')
def exibir_dashboard():
    return render_template('dashboard.html') 
      
@app.route('/api/ml/previsao-faturamento', methods=['GET'])
def previsao_vendas():
    dados_previsao = prever_faturamento_mensal()
    return jsonify(dados_previsao)    

@app.route('/api/ml/clusters', methods=['GET']) 
def relatorio_ml():
    dados_ia = classificar_produtos_ia()
    return jsonify(dados_ia)    
    
@app.route('/api/relatorios/segmentados', methods=['GET'])
def relatorio_segmentado():
    dados_relatorio = obter_relatorio_segmentado()
    return jsonify(dados_relatorio)

@app.route('/api/relatorios/produtos', methods=['GET'])
def relatorio_produtos():
    dados_relatorio = obter_estatisticas_produtos()
    return jsonify(dados_relatorio)
    
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/produtos")
def api_produtos():
    # Só produtos em estoque, os mais bem avaliados primeiro (máx. 16 cartões).
    docs = produtos.find({"estoque": {"$gt": 0}}).sort("avaliacao", -1).limit(16)

    lista = []
    for d in docs:
        nome = str(d.get("produto", "Produto"))
        # Monta o JSON campo a campo: assim _id (ObjectId), datas e campos
        # extras do banco nunca quebram a resposta.
        lista.append({
            "chave": nome,  # nome original do banco, usado na compra
            "nome": nome[:1].upper() + nome[1:],
            "preco": float(d.get("preco", 0)),
            "estoque": int(d.get("estoque", 0)),
            "categoria": str(d.get("categoria", "geral")),
            "avaliacao": float(d.get("avaliacao", 0)),
            "icone": icone_para(nome),
            "modelo3d": url_midia(d.get("modelo3d"), "modelos"),
            "video": url_midia(d.get("video"), "videos"),
            "imagem": url_midia(d.get("imagem"), "imagens"),
        })
    return jsonify(lista)


@app.route("/api/comprar", methods=["POST"])
def api_comprar():
    dados = request.get_json(silent=True) or {}
    resultado = efetuar_venda(dados.get("produto", ""), dados.get("quantidade", 1))
    return jsonify(resultado), (200 if resultado["ok"] else 400)


@app.route("/api/checkout", methods=["POST"])
def api_checkout():
    dados = request.get_json(silent=True) or {}
    resultado = efetuar_pedido(
        dados.get("cliente") or {},
        dados.get("pagamento", ""),
        dados.get("itens") or [],
    )
    return jsonify(resultado), (200 if resultado["ok"] else 400)


if __name__ == "__main__":
    # host 0.0.0.0 é necessário para funcionar no Codespaces
    app.run(host="0.0.0.0", port=5000, debug=True)

#fim