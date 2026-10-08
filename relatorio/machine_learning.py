import pandas as pd
from sklearn.cluster import KMeans
from database.conexao import produtos

def classificar_produtos_ia():
    dados_brutos = list(produtos.find())
    
    if not dados_brutos:
        return {"erro": "Nenhum produto encontrado."}
        
    df = pd.DataFrame(dados_brutos)
    
    if 'preco' in df.columns:
        # 1. Limpeza rigorosa (ML não aceita valores nulos)
        df['preco'] = pd.to_numeric(df['preco'], errors='coerce')
        df = df.dropna(subset=['preco'])
        
        # 2. Preparação da Matriz (Scikit-Learn exige dados em formato 2D)
        X = df[['preco']]
        
        # 3. Treinamento do Modelo K-Means
        # Pedimos para a IA encontrar 3 grupos distintos (n_clusters=3)
        modelo_ia = KMeans(n_clusters=3, random_state=42, n_init=10)
        
        # 4. Previsão: A IA cria uma nova coluna dizendo a qual grupo (0, 1 ou 2) cada produto pertence
        df['grupo_ia'] = modelo_ia.fit_predict(X)
        
        # 5. Organiza o relatório contando quantos produtos ficaram em cada grupo gerado pela IA
        contagem_grupos = df['grupo_ia'].value_counts().to_dict()
        
        # Renomeia as chaves para facilitar a leitura no JSON
        relatorio_ia = {
            f"grupo_{chave}": valor for chave, valor in contagem_grupos.items()
        }
        
        return {"padroes_encontrados_ia": relatorio_ia}
    else:
        return {"erro": "A coluna 'preco' não foi encontrada para treinar o modelo."}