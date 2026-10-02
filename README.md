# 🛒 Loja do Aluno — Python + MongoDB + Flask

Projeto desenvolvido para praticar **Python, MongoDB, PyMongo e Flask**, integrando uma aplicação web a um banco de dados NoSQL.

A aplicação começou com foco no gerenciamento de produtos e operações no MongoDB. Durante o desenvolvimento, foi adicionada uma interface web com Flask para aplicar na prática conceitos de **Back-end, integração com banco de dados e Front-end**.

## 🚀 Tecnologias utilizadas

* **Python**
* **Flask**
* **MongoDB Atlas**
* **PyMongo**
* **HTML5**
* **CSS3**
* **python-dotenv**
* **Git e GitHub**

## 📌 Funcionalidades

### Banco de dados

A aplicação possui integração com o MongoDB para:

* Inserção de produtos
* Consulta de produtos
* Atualização de produtos
* Exclusão de produtos
* Filtros por categoria
* Filtros por avaliação
* Busca por nome do produto
* Filtro por cor
* Controle de estoque

### Relatórios de vendas

O projeto também possui uma estrutura para trabalhar com vendas, permitindo:

* Registrar produtos vendidos
* Informar quantidade
* Registrar preço unitário da venda
* Calcular o valor total
* Consultar informações de vendas

A coleção `vendas` é separada da coleção `produtos`, permitindo diferenciar o **estoque disponível** das **vendas realizadas**.

### Interface Web

Foi desenvolvida uma interface utilizando **Flask** como uma evolução do projeto após os estudos de Front-end.

A interface possui integração direta com o banco de dados e apresenta dinamicamente os produtos cadastrados.

Um dos elementos implementados é um **carrossel com os produtos mais bem avaliados**, utilizando os dados armazenados no MongoDB.

## 🏗️ Estrutura do projeto

```text
python-mongodb-loja/
│
├── database/
│   ├── app.py
│   ├── conexao.py
│   ├── consultar.py
│   ├── inserir.py
│   ├── atualizar.py
│   └── excluir.py
│
├── relatorio/
│   └── vendas.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── ...
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

> A estrutura pode evoluir conforme novas funcionalidades forem adicionadas ao projeto.

## 🔗 Integração Python + MongoDB

A conexão com o MongoDB é realizada utilizando **PyMongo**.

As credenciais da conexão ficam armazenadas em variáveis de ambiente através do arquivo `.env`.

Exemplo:

```env
MONGO_URI=sua_string_de_conexao
```

O arquivo `.env` não deve ser enviado para o GitHub.

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/joaovictorcardoso/python-mongodb-loja.git
```

Entre na pasta:

```bash
cd python-mongodb-loja
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure o arquivo `.env` com a sua conexão do MongoDB Atlas.

## ▶️ Executando o projeto

Para executar a aplicação:

```bash
python -m database.app
```

Depois, acesse no navegador:

```text
http://127.0.0.1:5000
```

## 🗄️ Banco de dados

Banco utilizado:

```text
loja_do_aluno
```

Principais coleções:

```text
produtos
vendas
```

Exemplo de produto:

```json
{
    "produto": "placa de video",
    "categoria": "informatica",
    "avaliacoes": 4.8,
    "Cor": "preto",
    "estoque": 8
}
```

## 🎯 Objetivos do projeto

Este projeto está sendo desenvolvido como parte da minha evolução na área de tecnologia, com foco principalmente em:

* Python
* Banco de dados
* MongoDB
* Desenvolvimento Back-end
* Desenvolvimento Web
* APIs e integração entre sistemas
* Organização de projetos
* Git e GitHub
* Análise e manipulação de dados

A interface web foi adicionada posteriormente como forma de colocar em prática os conhecimentos adquiridos em Front-end e integrar essa camada ao Back-end e ao banco de dados.

## 📚 Próximos passos

Algumas funcionalidades que podem ser incorporadas futuramente:

* Sistema de autenticação
* CRUD completo pela interface web
* Dashboard de vendas
* Gráficos utilizando dados do MongoDB
* Paginação de produtos
* Sistema de busca mais avançado
* API REST com Flask
* Integração com Machine Learning
* Deploy da aplicação

## 👨‍💻 Autor

**João Victor Cardoso**

Estudante de **Bacharelado em Inteligência Artificial — 3º período**

Focado no desenvolvimento de habilidades em:

**Python • Dados • Machine Learning • SQL • MongoDB • Back-end**

---

⭐ Projeto desenvolvido para aprendizado prático e evolução profissional na área de tecnologia.
