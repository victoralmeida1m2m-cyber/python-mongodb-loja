# 🛒 Loja do Aluno — Backend & Machine Learning

API desenvolvida em **Python e Flask** para gerenciamento e análise de dados de um e-commerce acadêmico.

O projeto integra **MongoDB**, **Pandas** e **Machine Learning** para transformar dados de vendas em informações úteis para análise de negócio, incluindo **previsão de faturamento** e um **dashboard interativo de Business Intelligence**.

---

## 🚀 Tecnologias

| Área | Tecnologia |
|---|---|
| Backend | Python 3 + Flask |
| Banco de dados | MongoDB + PyMongo |
| Análise de dados | Pandas |
| Machine Learning | Scikit-Learn |
| Modelo utilizado | Regressão Linear |
| Dashboard | HTML5 + CSS3 + Chart.js |
| Ambiente | GitHub Codespaces |

---

## 📂 Estrutura do Projeto

```text
python-mongodb-loja/
│
├── database/
│   ├── app.py
│   ├── atualizar.py
│   ├── conexao.py
│   ├── consultar.py
│   ├── excluir.py
│   └── inserir.py
│
├── relatorio/
│   ├── previsao.py
│   └── vendas.py
│   └── machine_learning.py
├── templates/
│   └── dashboard.html
│   └── index.html
|
├── server.py
├── requirements.txt
└── README.md
```

### 📁 Organização

- **`database/`** — conexão e operações com o MongoDB.
- **`relatorio/`** — consultas, análise de vendas e modelos de Machine Learning.
- **`templates/`** — páginas HTML utilizadas pelo Flask.
- **`server.py`** — aplicação principal e definição das rotas.
- **`requirements.txt`** — dependências necessárias para executar o projeto.

---

## ⚙️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/python-mongodb-loja.git
cd python-mongodb-loja
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure o MongoDB

Configure as credenciais de conexão com o MongoDB de acordo com a estrutura utilizada no projeto.

> Recomenda-se utilizar variáveis de ambiente para informações sensíveis, como a URL de conexão do MongoDB.

### 4. Execute o servidor Flask

```bash
python server.py
```

### 5. Acesse a aplicação

Após iniciar o servidor, acesse:

```text
http://127.0.0.1:5000
```

---

## 📊 Dashboard

O projeto possui um dashboard desenvolvido com **HTML, CSS e Chart.js**, permitindo visualizar informações relacionadas às vendas e ao faturamento.

### Rota

```http
GET /dashboard
```

O dashboard apresenta informações como:

- Faturamento;
- Médias de vendas;
- Indicadores de desempenho;
- Projeções;
- Gráficos interativos.

---

## 🤖 Machine Learning

O projeto utiliza **Machine Learning** para realizar uma previsão de faturamento com base no histórico de vendas armazenado no MongoDB.

O modelo utilizado é a **Regressão Linear**, disponibilizada pelo Scikit-Learn.

### Fluxo da previsão

```text
MongoDB
   ↓
Dados de vendas
   ↓
Pandas
   ↓
Agrupamento por mês
   ↓
Regressão Linear
   ↓
Previsão de faturamento
   ↓
Dashboard / API
```

O modelo utiliza principalmente:

- `data_venda` — data em que a venda ocorreu;
- `total` — valor total da venda.

Os dados são agrupados mensalmente e utilizados para identificar uma tendência de faturamento.

---

## 🔗 API de Previsão

A aplicação disponibiliza uma rota específica para consultar a previsão:

```http
GET /api/ml/previsao-faturamento
```

A rota:

1. Consulta os dados de vendas no MongoDB;
2. Processa os dados utilizando Pandas;
3. Agrupa o faturamento por período;
4. Treina o modelo de Regressão Linear;
5. Calcula a previsão do próximo período;
6. Retorna os resultados em formato JSON.

### Exemplo de resposta

```json
{
  "previsao_faturamento": 12500.50
}
```

> O valor apresentado acima é apenas um exemplo de estrutura de resposta.

---

## 🧠 Conceito de Machine Learning

A Regressão Linear busca identificar uma relação entre os dados históricos e uma variável de interesse.

Neste projeto, o modelo utiliza o histórico de faturamento para encontrar uma **linha de tendência** e estimar o comportamento do próximo mês.

De forma simplificada:

```text
Histórico de vendas
        ↓
Faturamento mensal
        ↓
Tendência dos dados
        ↓
Regressão Linear
        ↓
Previsão
```

---

## 📈 Objetivo do Projeto

O projeto foi desenvolvido com o objetivo de integrar diferentes áreas do desenvolvimento e da análise de dados em uma única aplicação:

- Desenvolvimento Backend;
- Banco de dados NoSQL;
- Manipulação e análise de dados;
- Machine Learning;
- APIs;
- Business Intelligence;
- Visualização de dados.

A proposta é transformar dados armazenados no MongoDB em **informações e previsões que possam auxiliar na tomada de decisões**.

---

## 🛠️ Próximos Passos

Possíveis evoluções para o projeto:

- [ ] Melhorar o modelo de previsão;
- [ ] Adicionar novos indicadores ao dashboard;
- [ ] Implementar autenticação;
- [ ] Criar novos endpoints para análise de vendas;
- [ ] Comparar diferentes modelos de Machine Learning;
- [ ] Adicionar métricas de avaliação do modelo;
- [ ] Melhorar a interface do dashboard;
- [ ] Implementar deploy da aplicação.

---

## 👨‍💻 Autor

**João Victor Cardoso**

Estudante de **Bacharelado em Inteligência Artificial** e desenvolvedor em formação com foco em **Dados, Python, SQL, MongoDB e Machine Learning**.

[LinkedIn](https://linkedin.com/in/joaovictorcardoso)
