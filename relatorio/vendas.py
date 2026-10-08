import pandas as pd
from database.conexao import produtos 

def obter_estatisticas_produtos():
    # Extrai os dados da base de dados
    dados_brutos = list(produtos.find())
    
    # Prevenção: se a coleção estiver vazia
    if not dados_brutos:
        return {"erro": "Nenhum produto encontrado."}
        
    df = pd.DataFrame(dados_brutos)
    df = df.drop(columns=['_id'], errors='ignore')
    
    # Verifica se a coluna 'preco' existe e converte para número
    if 'preco' in df.columns:
        df['preco'] = pd.to_numeric(df['preco'], errors='coerce')
        
        # Calcula as estatísticas e formata com 2 casas decimais
        estatisticas = {
            "produto_mais_caro": round(df['preco'].max(), 2),
            "produto_mais_barato": round(df['preco'].min(), 2),
            "media_de_precos": round(df['preco'].mean(), 2)
        }
        return estatisticas
    else:
        return {"erro": "A coluna 'preco' não foi encontrada."}
        
def obter_relatorio_segmentado():
    dados_brutos = list(produtos.find())
    
    if not dados_brutos:
        return {"erro": "Nenhum produto encontrado."}
        
    df = pd.DataFrame(dados_brutos)
    df = df.drop(columns=['_id'], errors='ignore')
    
    # Converte o preço para número, caso exista
    if 'preco' in df.columns:
        df['preco'] = pd.to_numeric(df['preco'], errors='coerce')
        
        # --- 1. Aplicação de Filtro ---
        # Filtra apenas os produtos que custam mais de 500
        df_premium = df[df['preco'] > 500]
        quantidade_premium = int(df_premium.shape[0]) # shape[0] conta o número de linhas
        
        relatorio = {
            "total_produtos_premium": quantidade_premium
        }
        
        # --- 2. Aplicação de Groupby ---
        # Verifica se a coluna 'categoria' existe para agrupar os dados
        if 'categoria' in df.columns:
            # Calcula a média de preço por categoria e converte para dicionário
            media_por_categoria = df.groupby('categoria')['preco'].mean().round(2).to_dict()
            relatorio["media_por_categoria"] = media_por_categoria
            
        return relatorio
    else:
        return {"erro": "A coluna 'preco' não foi encontrada."}