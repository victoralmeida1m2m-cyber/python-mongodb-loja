import pandas as pd
from sklearn.linear_model import LinearRegression
from database.conexao import db

colecao_vendas = db["vendas"]

def prever_faturamento_mensal():
    dados_brutos = list(colecao_vendas.find())
    
    if not dados_brutos:
        return {"erro": "Não existem vendas registadas."}

    df = pd.DataFrame(dados_brutos)
    
    # 1. Valida se as colunas reais (total e data_venda) existem no MongoDB
    if 'total' not in df.columns or 'data_venda' not in df.columns:
        return {"erro": "Faltam as colunas 'total' ou 'data_venda' nos registos do MongoDB."}
        
    # 2. Converte os dados do MongoDB para o formato matemático do Pandas
    df['valor'] = pd.to_numeric(df['total'], errors='coerce')
    df['data'] = pd.to_datetime(df['data_venda'], errors='coerce')
    
    # Remove qualquer linha que tenha falhado na conversão
    df = df.dropna(subset=['valor', 'data'])

    # 3. Agrupa o faturamento pelo mês e ano real
    df['ano_mes'] = df['data'].dt.to_period('M')
    faturamento_mensal = df.groupby('ano_mes')['valor'].sum().reset_index()

    # Cria uma sequência numérica para o eixo X do gráfico da IA (1, 2, 3...)
    faturamento_mensal['mes_sequencial'] = range(1, len(faturamento_mensal) + 1)

    # Verifica se existem pelo menos 2 meses distintos para traçar a reta
    if len(faturamento_mensal) < 2:
        return {"erro": "O modelo precisa de vendas em pelo menos 2 meses diferentes para prever a tendência."}

    # 4. Treina o Modelo de Machine Learning
    X = faturamento_mensal[['mes_sequencial']] 
    y = faturamento_mensal['valor']

    modelo = LinearRegression()
    modelo.fit(X, y)

    # 5. Prevê o faturamento do próximo mês
    proximo_mes_index = faturamento_mensal['mes_sequencial'].max() + 1
    previsao_bruta = modelo.predict([[proximo_mes_index]])
    
    # Monta o JSON final
    resultado = {
        "meses_analisados": int(len(faturamento_mensal)),
        "faturamento_medio_atual": round(y.mean(), 2),
        "previsao_proximo_mes": round(previsao_bruta[0], 2),
        "tendencia": "crescimento" if modelo.coef_[0] > 0 else "queda"
    }
    
    return resultado