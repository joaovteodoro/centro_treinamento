# BACKEND — Centro Treinamento

API REST desenvolvida com FastAPI para gestão de atletas, categorias e centros de treinamento.


## CONFIGURANDO O AMBIENTE

> Todos os comandos devem ser executados dentro da pasta `backend/`

### Poetry

**1. Instalar o Poetry**

```powershell
pip install poetry
```
obs: como poetry foi instalado via pip, toda vez que for necessário executar poetry 'comando', será necessário passar na frente ' python -m ', conforme passo abaixo

**2. Instalar dependências e criar o ambiente virtual**

```powershell
python -m poetry install
```
obs: Instala todas as dependências informadas no arquivo poetry.lock (se não houver poetry.lock, utiliza as dependências informadas no pyproject.toml)

**3. Rodar sem ativar o ambiente virtual**

Execute o seguinte comando
```powershell
python -m poetry run uvicorn app.main:app --reload
```
Obs: isso só é feito após toda a configuração

**Comandos úteis**

| Ação | Comando |
|---|---|
| Adicionar pacote | `python -m poetry add 'pacote' ` |
| Remover pacote | `python -m poetry remove 'pacote' ` |
| Listar pacote instalados | ` python -m poetry show ` |
| Ativar o ambiente virtual | `python -m poetry env activate ` |

### PostgreSQL

**4. Instale o PostgreSQL**

Instale o PostgreSQL pelo link https://www.postgresql.org/download/ 

**5. Crie um banco de dados**

No programa pgAdmin4 (instalado junto com o PostgreSQL), crie um database com o nome de 'centro_treinamento'

**6. Conecte o banco de dados**

Dentro do .env configure o banco de dados:
```powershell
DB_URL=postgresql+asyncpg://postgres:senha@localhost:porta/centro_treinamento
```

### Alembic

**7. Crie e aplique as tabelas no banco**

```powershell
python -m poetry run alembic revision --autogenerate -m "init"
python -m poetry run alembic upgrade head
```
Obs: cria as tabelas no PosgreSQL

**Comandos úteis**

| Ação | Comando |
|---|---|
| Gerar nova migration | `python -m poetry run alembic revision --autogenerate -m "descricao"` |
| Aplicar migrations | `python -m poetry run alembic upgrade head` |
| Reverter última migration | `python -m poetry run alembic downgrade -1` |


## INICIALIZANDO O BACKEND

Para rodar o programa você deve:

```
1 Instalar o Poetry (passo 01)
2 Baixar as dependências (passo 02)
3 Instalar o PostgreSQL (passo 04)
4 Criar o banco de dados no PostgreSQL por meio do pgAdmin4 (passo 05)
5 Configurar o banco de dados (passo 06)
6 Inicializar o Alembic (passo 07)
7 Rodar o Uvicorn com poetry (passo 03)
```
