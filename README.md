🛒 Loja do Aluno - Backend & Machine Learning

Este projeto é uma API em Python baseada em Flask para um e-commerce acadêmico. O grande diferencial desta aplicação é a integração com um módulo de Inteligência Artificial (Machine Learning) para análise de dados e previsão de faturamento, além de um dashboard interativo para visualização de métricas de negócios (Business Intelligence).

🚀 Tecnologias Utilizadas

Backend: Python 3, Flask

Banco de Dados: MongoDB (PyMongo)

Ciência de Dados & ML: Pandas, Scikit-Learn (Regressão Linear)

Front-end (Dashboard): HTML5, CSS3, Chart.js

Ambiente de Desenvolvimento: GitHub Codespaces

📂 Estrutura do Projeto

O repositório está organizado de forma modular, separando banco de dados, regras de negócio e interfaces visuais:

📦 python-mongodb-loja
 ┣ 📂 database/           # Scripts de conexão e manipulação do MongoDB
 ┣ 📂 relatorio/          # Módulos de Inteligência Artificial e Pandas
 ┃ ┣ 📜 previsao.py       # Modelo de Regressão Linear para faturamento
 ┃ ┗ 📜 vendas.py         # Consultas estruturadas de vendas
 ┣ 📂 templates/          # Arquivos HTML renderizados pelo Flask
 ┃ ┗ 📜 dashboard.html    # Painel visual com gráficos (Chart.js)
 ┣ 📜 server.py           # Arquivo principal que roda o servidor Flask e define as rotas
 ┣ 📜 atualizar_datas.py  # Script de migração de dados (workaround de datas)
 ┗ 📜 requirements.txt    # Dependências do projeto


⚙️ Como Executar o Projeto

Como o projeto foi construído utilizando o GitHub Codespaces, o ambiente já possui grande parte das configurações prontas.

Abra o projeto no seu Codespaces ou clone o repositório localmente.

Instale as dependências (caso esteja em um novo ambiente local):

pip install -r requirements.txt


Inicie o servidor Flask:

python server.py


O servidor estará rodando na porta 5000.

🔗 Rotas Principais

A aplicação disponibiliza os seguintes endpoints de destaque:

GET /dashboard

Renderiza o painel visual de Business Intelligence. Exibe as médias de faturamento e projeta o crescimento em um gráfico interativo.

GET /api/ml/previsao-faturamento

Rota da API que consome os dados reais do MongoDB, processa via Pandas e utiliza o Scikit-Learn para prever o faturamento do próximo mês. Retorna um objeto JSON estruturado.

🧠 Lógica de Machine Learning

O módulo de IA utiliza Regressão Linear (LinearRegression do sklearn). Ele analisa a coluna data_venda e total dos documentos no MongoDB, agrupa o faturamento por mês, e traça uma linha de tendência matemática para calcular se a loja está em crescimento ou queda, estimando o valor exato do mês seguinte.