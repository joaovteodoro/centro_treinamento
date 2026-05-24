# CENTRO TREINAMENTO

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=flat&logo=css&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)

Centro de treinamento é um projeto de um bootcamp desenvolvido pela DIO com o objetivo de desenvolver habilidades relacionadas à construção de APIs e testes.
Este software faz a gestão de um centro de treinamento, mostrando a relação entre as categorias de luta, os atletas e os centros de treinamentos

## TECNOLOGIAS UTILIZADAS
BACKEND
- Poetry || para controle de ambiente e pacotes
- PostgreSQL || para banco de dados
- SQL Alchemy + Alembic || para controle de migrações
- FastAPI || para criação de APIs
- Pytest || para testes

FRONTEND
- HTML + CSS + JS || para construção do frontend

## ORGANIZAÇÃO DO CÓDIGO

```
workout/
├── backend/                  ← API REST (Python/FastAPI)
│   ├── src/
│   │   └── app/              ← código fonte da aplicação
│   │       ├── atleta/
│   │       ├── categorias/
│   │       ├── centro_treinamento/
│   │       ├── configs/
│   │       └── contrib/
│   ├── alembic/              ← migrations do banco de dados
│   ├── tests/                ← realiza os testes de funcionamento do código
│   ├── pyproject.toml
│   └── README.md
│
└── frontend/                 ← interface web
└── dashboard.html
```

## INICIANDO O PROGRAMA
- Configure e ative o backend (leia o README.md dentro da pasta backend\ )
- Dentro da pasta frontend\ clique no arquivo dashboard.html

## EXECUTANDO OS TESTES DA APLICAÇÃO
- Leia o README.md dentro da pasta backend\tests\

## SEGURANÇA
Antes de subir para produção, no main.py, é necessário alterar:
    allow_origins=["*"] para allow_origins=["https://meusite.com"]


## FUNCIONALIDADES
- Cadastro, listagem e exclusão de atletas
- Cadastro, listagem e exclusão de categorias
- Cadastro, listagem e exclusão de centros de treinamento
- Filtro de atletas por nome e CPF
- Dashboard web integrado à API

