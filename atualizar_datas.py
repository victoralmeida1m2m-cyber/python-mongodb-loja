from database.conexao import db
from datetime import datetime

colecao_vendas = db["vendas"]

# Puxa todos os documentos que existem atualmente na coleção
documentos = list(colecao_vendas.find())

# Meses base para simular o histórico passado (Agosto=8, Setembro=9, Outubro=10)
meses_historico = [8, 9, 10]

vendas_atualizadas = 0

for indice, doc in enumerate(documentos):
    # Distribui os documentos sequencialmente entre os 3 meses
    mes_escolhido = meses_historico[indice % 3]
    
    # Cria a data (ex: 2026-08-15, 2026-09-15, etc.)
    data_retroativa = datetime(2026, mes_escolhido, 15)
    
    # O comando $set do MongoDB adiciona o novo campo sem apagar os existentes (como 'total', 'produto')
    colecao_vendas.update_one(
        {"_id": doc["_id"]},
        {"$set": {"data_venda": data_retroativa}}
    )
    vendas_atualizadas += 1

print(f"Sucesso! {vendas_atualizadas} vendas foram atualizadas com datas retroativas.")