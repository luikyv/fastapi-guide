---
layout: page
title: Guia para começar com FastAPI
permalink: /guide/
---


Nesse guia apresentaremos o framework FastAPI e como ele pode ser utilizado para construir APIs do tipo REST em Python de maneira eficiente.

Antes de começarmos, um pouco de contexto. Hoje em dia, a comunicação entre sistemas de computação se dá em grande parte por meio de APIs. Nesse cenário, um sistema A envia requisições HTTP (HTTP sendo um protocolo de comunicação na internet) a um sistema B e recebe como resposta os recursos solicitados ou a confirmação de que uma ação foi realizada no sistema B.

Dito isso, FastAPI entra como um framework escrito em Python para facilitar o desenvolvimento de APIs. Existem diversos outros frameworks para isso em Python e ainda muitos outros se considerarmos outras linguagens de programação como Java e C#. Então porque escolher FastAPI nesse mar de opções? Vejamos alguns motivos.

Por ser baseado em Python o desenvolvimento com FastAPI é extremamente fácil, mas, dependendo da sua aplicação, pode ser mais interessante usar Spring que é baseado em Java por exemplo. Talvez Java possua algumas vantagens que possam ser mais interessantes para sua aplicação.

Além da facilidade que Python traz ao desenvolvimento, essa linguagem é bastante útil em ambientes onde a manipulação de dados é constante. Podemos comprovar isso ao pensar que a bibliotecas mais famosas para manipulação de dados vêm do Python. Temos como exemplos Numpy e Pandas. Assim, FastAPI se torna uma boa opção se sua aplicação vai ter como foco dados.

Além disso, como o próprio nome diz, o FastAPI é fast. O "rápido" em seu nome se dá principalmente pelo fato de podermos utilizar programação asíncrona de maneira simples nesse framework. Isso traz mais flexibilade e eficiência a sua API, pois você tem certo controle de como diferentes processos são chamados. Mais para frente vamos ver em detalhes como tudo isso funciona.

Falando agora de popularidade, FastAPI vem desbancando diversos outros frameworks e, apesar de ter aparecido recentemente no mercado, muitos desenvolvedores e empresas estão optando por ele.

Indo ao que interessa a todos, vemos que a [média salarial](https://www.linkedin.com/posts/tiangolo_fastapi-activity-7010582598099849217-CzZt?utm_source=share&utm_medium=member_desktop) de desenvolvedores de FastAPI é bem alta e maior do que a de desenvolvedores de frameworks como .NET e Node.js o que é um feito impressionante.

Depois dessa breve introdução, vamos ver em detalhes alguns conceitos sobre desenvolvimento de APIs, ferramentas do Python e entender como de fato usar FastAPI.

# Fundamentos

## HTTP
HTTP é um protocolo que permite que clientes iniciem comunicações com servidores pela internet a fim de realizar transações. Dentre essas transações podemos citar recuperar uma página html ou executar uma operação no servidor para alterar o estado de um banco de dados.

Usando o protocolo HTTP, podemos interagir com APIs. Para isso, durante o desenvolvimento com FastAPI, precisamos definir os endpoints e os respectivos métodos que serão invocados para realizar as chamadas. Para aqueles não familiarizados, um endpoint é um ponto de acesso a recursos da API. Essencialmente, é uma URL por onde um cliente externo se comunica com a API usando o protocolo HTTP.

Dentre os métodos disponíveis no protocolo HTTP, os que mais iremos usar são aqueles que representam as operações CRUD (Create, Read, Update, Delete). Esses são:
* GET: Para fazer a leitura de recursos
* POST: Para criar recursos
* PUT: Para atualizar recursos
* DELETE: Para deletar recursos.

## Rest APIs

Antes de entendermos o que é uma API REST, precisamos ter em mente o que é uma API. A sigla API significa Application Programming Interface, então uma interface de programação de aplicação. Uma API nada mais é do que um contrato a ser seguido para poder intergir como uma aplicação que possui recursos que interessam ao desenvolvedor. Esse recursos mantidos pela aplicação podem ser dados, uma lógida de computação, entre outros. Por exemplo, o Google tem uma [API](https://materiais.ipnet.cloud/google-maps-api-entrada-b?utm_source=google-search&utm_medium=cpc&utm_campaign=[Cadastro]_Google_Maps_Platform_Especificas_de_Conversao_-_Fundo_Brasil&utm_id=17377035032&utm_term=135647100845&utm_content=api%20google%20maps&gclid=Cj0KCQiA5NSdBhDfARIsALzs2ECb9W2XJsivUJCRjqqfl0krafI_ttroFSgQRXOhFZEBlMjGHJSl0ycaApbtEALw_wcB) que permite desenvolvedores integrar mapas personalizados do Google Maps em suas aplicações. Assim uma API pode ser vista como um intermediador entre sua aplicação e a aplicação de um terceiro que possui recursos que você precisa.

Já uma API REST, você também vai ouvir API RESTful, é uma API que segue a arquitetura REST, onde REST quer dizer "Representational State Transfer" ou Transferência de Estado Representacional. REST é um conjunto de restrições para a arquitetura da sua API. Se sua API respeita essas restrições, você tem uma API REST.

O nome REST se dá pelo fato que, quando um cliente requisita um recurso à API através do protocolo HTTP, a API responde com uma representação do estado atual do recurso. Essa reprentação pode vir em diversos formatos como JSON e HTML. Entretanto, JSON é o mais utilizado por ser uma formato eficiente com estrutura simples e várias linguagens de programação permitem interação com ele.

Dentre algumas restrições incluídas no REST temos
* Arquitetura cliente/servidor onde a comunicação se dá com HTTP (HTTP sendo um protocolo de comunicação onde conseguimos interagir com um servidor de endereço conhecido, endereço esse que é uma url, utilizando métodos como GET, POST, ...)
* Comunicação sem estado. Isso quer dizer basicamente que o servidor em si não armazena o estado das chamadas que ele recebe, então uma chamada ao servidor não interfere em outras.

Existem algumas outras restrições, mas, só pelo fato de utilizar o framework FastAPI, muitas já são respeitadas. Além disso, apesar dessas restrições, APIs REST são simples de desenvolver e utilizar e, por isso, estão se tornando a primeira opção dos desenvolvedores.

## Pyenv
Quando trabalhando com projetos em Python, é fundamental a utilização de ambientes virtuais. Para demonstrar isso, imagine que você tem dois projetos em Python em seu computador e ambos dependem da biblioteca, digamos, Tortoise. O problema é que o primeiro projeto precisa que a versão de Tortoise seja 1.0, já o segundo precisa da versão 1.1. Ambientes virtuais resolver esse problema, pois, para cada projeto, você cria um ambiente virtual e esses ambientes são independetes um do outro. Assim, você pode usar diferentes versão da mesma biblioteca ou mesmo diferentes versões do Python, sem que hajam conflitos entre eles.

Aqui usaremos Pyenv para criar e gerenciar ambientes virtuais, mas você pode usar qualquer outra ferramenta que lide com ambientes virtuais.

Para começar vamos criar o diretório do nosso projeto.

```bash
mkdir my-project && cd my-project
```

Vamos usar a versão 3.9.11 de Python. Caso você não a tenha em seu computador, pode instalar com:

```bash
mkdir fastapi-guide
cd fastapi-guide
```

Agora, vamos criar o ambiente virtual que daremos o nome de `my_env_3911`. Como boa prática, coloque a versão que você está usando no nome do ambiente para que seja mais fácil de lembrar. Após isso, basta ativá-lo.

```bash
pyenv virtualenv 3.9.11 my_env_3911
pyenv activate my_env_3911
```

Para garantir que `my_env_3911` será ativado cada vez que você entrar em `fastapi-guide`, execute o seguinte comando. Ele criar um arquivo chamado .python-version dentro de `fastapi-guide`. Esse arquivo tem o nome do ambiente virtual que você está usando que é, no nosso caso, `my_env_3911`.

```bash
pyenv local my_env_3911
```

## Poetry
Poetry é uma ferramenta de gestão de dependências e empacotamento para projetos em Python.

Depois que você declara as dependências que o software que você está desenvolvendo precisa, Poetry as instala e atualiza por você. Além disso, Poetry garante que instalar seu projeto em outros ambientes não causar supresas indesejáveis. Isso significa que seu projeto pode ser compartilhado de maneira consistente e outras pessoas podem utilizá-lo sem grandes dificuldades.

Para instalar Poetry, podemos usar este script: https://install.python-poetry.org/

Vamos inicializar o Poetry no diretório do nosso projeto.

```bash
poetry init
```

Para declarar as dependências que precisamos, basta utilizar o comando `poetry add`. Como exemplo:

```bash
poetry add pandas
```

Já se quisermos remover a dependência:

```bash
poetry remove pandas
```

Se quiser saber mais sobre Pyenv e Poetry, confira esse artigo no Medium: [Manage Dependencies in Python with Poetry](https://medium.com/@luikymagno/manage-dependencies-in-python-with-poetry-18562c944e96)

## Programação Assíncrona

Uma das grandes vantagens que o FastAPI traz é a possibilidade de utilizar programação asíncrona. Nesse modelo de programação, nos fazemos uma chamada a uma tarefa e vamos para outra enquanto a primeira aguarda ser finalizada. Assim, conseguimos introduzir paralelismo em nosso software e temos controle de quando essas chamadas asíncronas são feitas.

O modelo de programação asíncrona é bastante eficaz quando precisamos executar tarefas bloqueantes. Essas tarefas levam um tempo relativamente alto para terminar e exemplos são requisições HTTP, consultas a bancos de dados e operações I/O. Quando um processo asíncrono atinge um operação bloqueante, ele a começa e a deixa esperando concluir. Enquanto isso, o processo começa a executar outra tarefa e, uma vez terminada a operação bloqueante, ele retorna ao local onde estava para terminar a execução.

Em Python, temos duas palavras chave que nos permitem implementar operações asíncronas. A primeira é `async` e você a usa para definir funções que serão executadas asíncronamente. A outra é `await` e é usada para chamar funções asíncronas. Sendo mais específico, funções definidas com `async` são chamadas de corotinas e o retorno dessas são futures. Quando você chama uma função asíncrona com `await`, ela te retorna um future que é um objeto que vai ser resolvido depois como o real resultado da função assim que ele termina de executar.

Vejamos um exempo de como isso funciona na prática. Aqui, vamos usar a biblioteca Asyncio para chamar asíncronamente uma função de sleep
```python
import asyncio

async def fake_blocking_operation(id: int) -> None:
    print(f"Start faking blocking operation {id}")
    await asyncio.sleep(1)
    print(f"Fake blocking operation {id} has completed")
```

Se quisermos executar duas chamadas dessa função paralelamente, podemos usar a função `asyncio.gather` que recebe como argumento uma sequência de corotinas.
```python
async def main_in_parallel() -> None:
    await asyncio.gather(
        fake_blocking_operation(1),
        fake_blocking_operation(2)
    )

if __name__=="__main__":
    t_0 = timeit.default_timer()
    asyncio.run(main_in_parallel())
    t_1 = timeit.default_timer()
    print(f"Elapsed time: {round(t_1 - t_0, 2)}s")
```

O resultado da execução acima é o seguinte
```
Start faking blocking operation 1
Start faking blocking operation 2
Fake blocking operation 1 has completed
Fake blocking operation 2 has completed
Elapsed time: 1.0s
```

Perceba que ao invés de esperar 2 segundos para as duas chamadas da operação bloqueante terminarem, só tivemos que esperar 1 segundo. Isso exemplifica como a programação asíncrona é útil quando aplicada do jeito correto. Em FastAPI, nos podemos criar funções e endpoints chamando operações asíncronas o que torna no código bastante eficaz.

Se quiser saber mais como funciona a programação asíncrona em Python, confira meu artigo no Medium que mostra como usar Asyncio e seus conceitos base: [Asynchrounous Programming with Python Asyncio](https://medium.com/@luikymagno/asynchrounous-programming-with-python-asyncio-db87f2936fb0).

# FastAPI

Com os fundamentos estabelecidos, agora podemos entender como FastAPI os aplica e como melhor usar esse framework.

## Primeiros passos

Para começar, vamos construir uma API que seja a mais simples possível.

Crie um arquivo chamado `main.py` e insira as seguintes linhas de código.
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello-world")
async def greet():
    return {"message": "Hello, World!"}
```

Aqui temos nosso primeiro endpoint `/hello-world`. Esse endpoint responde ao método GET com o seguinte Json: `{"message": "Hello, World!"}`.

Para ver isso em ação, vamos levantar a aplicação. Para isso, basta executar o seguinte comando `uvicorn main:app --reload`. Esse comando instancia sua aplicação a cada vez que há uma mudança no código e a deixa acessível no servidor web [Uvicorn](https://www.uvicorn.org/) disponível localmente. Agora, digite no seu navegador `http://127.0.0.1:8000/hello-world` e você verá o seguinte Json. Vale lembrar, seu navegador executa automaticamente o método GET quando você digita uma URL na barra de pesquisa.

```json
{"message": "Hello, World!"}
```

Note que você não apenas digitou `/hello-world`, mas sim este com `http://127.0.0.1:8000` prefixado. `http://127.0.0.1:8000` ou também `http://localhost:8000` se refere ao host da sua aplicação e a porta onde ela está disponível, como você iniciou o servidor localmente, o seu host é, intuitivamente, o `localhost`.

Além disso, perceba que o objeto que representa sua aplicação e pelo qual você define seus endpoints é uma instância de `FastAPI` que referenciamos com a variável `app`. Com esse objeto, definimos endpoints informando seu path, `hello-world` em nosso exemplo, e decorando funções que performam as regras de negócio usando o marcador `@`. Essas funções serão executadas quando chamadas pelo método e path corretos.

Ademais, FastAPI gera automaticamente uma especificação da sua API no padrão OpenAPI e tem integração com o Swagger que é um serviço que renderiza uma interface amigável a partir dessa especificação. Nessa interface, você tem acesso a informações como docstrings e schemas aceitos como payload nos seus endpoints, além de poder interagir com a API diretamente por essa interface. Para acessá-la, vá em `http://localhost:8000/docs` ou, se preferir, existe uma outra versão da interface em `http://localhost:8000/redoc`.

## Parâmetros

Existem dois tipos de parâmetros que você pode definir em seus endpoints e ambos são responsáveis por modificar o comportamente do endpoint sendo chamado. O primeiro são os parâmetros de query e funcionam exatamente como parâmetros de uma função qualquer.
```python
@app.get("/books")
async def read_book(genre: str):
    return {"book_genre": genre}
```

Para chamar esse endpoint, poderiamos realizar um GET em `/books?genre=action`. Neste caso, estariamos recuperando um ou vários livros do gênero ação.
Parâmetros de query veem ao final do path e são precedidos de `?`. Se houvessem mais parâmetros, eles precisariam estar separados por `&` na URL. Eles são úteis para filtar recursos e trazer mais informação à execução da regra de negócio.

Além disso, podemos customizar ainda mais esse parâmetro com validações e valores padrão. Para isso, podemos usar o objeto `Query` como valor padrão do parâmetro como no seguinte exemplo:
```python
@app.get("/books")
async def read_book(genre: str = Query(default="romance", max_length=50)):
    return {"book_genre": genre}
```

Ao fazer isso, o parâmetro `genre` deve ter no máximo 50 caracteres e será "romance" caso nenhum valor for atribuído a ele. Se alguma validação falhar, o cliente receberá o erro 422 que significa Unprocessable Entity.

Já o segundo é do tipo path e é passado e extraído pela sua API no path do endpoint.
```python
@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {"book_id": book_id}
```
No exemplo acima o endpoint `/books` recebe obrigatoriamente um parâmetro do tipo inteiro que representa o id de um livro. Então para chamá-lo, você poderia executar um GET em `/books/1` e recuperar o livro de id 1.

Quando precisamos acessar um recurso disponibilizado pela API e precisamos o **especificar**, digamos, com um id, parâmetros de path trazem um melhor entendimento do que a requisição sendo executada faz. No exemplo anterior, nós queremos dos livros aquele de id 1. Assim `/books/1` se torna mais legível do que se fosse implementado com um parâmetro de query `/books?id=1`. Ambos atingem o mesmo objetivo, mas nesse caso, usar o parâmetro de path traz mais legibilidade a sua aplicação, por isso é interessante saber como usá-lo para que seja aplicado devidamente.

## Request Body (Payload)

Em diversas situações, será necessário receber dados vindos do cliente para executar a lógica implementada no endpoint. Para que o cliente possa enviar esses dados e API os receber, precisamos definir um **request body** que, em FastAPI, nada mais é do que um objeto que será instanciado a partir de uma classe que definimos usando [Pydantic](https://docs.pydantic.dev/). Por sua vez, Pydantic é uma biblioteca em Python para modelação e interpretação de dados que introduz mecanismos de validação e tratamento de erros.

Vamos definir nossa primeira payload. Ao criar os campos da classe, podemos seguir o padrão `nome: tipo = valor_padrão`. Em um arquivo chamados schemas.py, insira:
```python
from typing import Optional
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
```

Feito isso, podemos incluir a payload Book em um endpoint de criação de livros. Como estamos tratando a criação, vamos definir o endpoint com o método POST.
```python
import schemas
from fastapi import FastAPI

app = FastAPI()

@app.post("/book")
async def create_book(book: schemas.Book) -> schemas.Book:
    return book
```

Ao fazer isso, o endpoint `/book` do tipo POST vai receber um Json que deve estar formatado com as variáveis de Book e vai criar um objeto dessa classe o qual vai passar como parâmetro ao endpoint onde nós podemos realizar as operações que desejamos. Caso o Json recebido não esteja no formato adequado, o cliente receberá o erro 422.

Para ver isso funcionando, você pode realizar uma chamda no terminal, já que o browser não será útil, pois precisamos realizar um POST e não um GET. Com o servidor rodando localmente, execute o comando:
```bash
curl -X POST http://localhost:8080/book
   -H 'Content-Type: application/json'
   -d '{"title":"Harry Potter","description":"The Sorcerer's Stone","price": 50.0}'
``` 
Ou, se preferir, ao acessar o swagger fornecido pelo FastAPI, você pode realizar a mesma requisição.

Perceba também que dessa vez definimos o tipo do retorno do POST endpoint `/book` como o tipo Book. Ao fazer isso, haverá uma validação de que o que retornamos de fato é um objeto do tipo Book. Além disso, esse informação do tipo de retorno também é apresentada na especificação OpenAPI o que melhora o entendimento de como usar a API.

# FastAPI com Banco de dados

Ao desenvolver APIs, um dos cenários mais frequentes é a utilização de banco de dados relacionais. Com bancos de dados, temos acesso a informações armazenadas de maneira persistente e essas informações podem ser usadas para implementar a lógica de negócio de nossos endpoints. Em certos casos, a API que construimos terá o único objetivo de servir como interface ao banco de dados para que outras APIs possam acessá-lo com facilidade.

Umas da maneiras mais simples de interagir com bancos de dados é através de ORMs. ORM significa Object Relational Mapping, então ela vai nos fornecer objetos que mapeiam tabelas de banco de dados. Ela permite que possamos fazer consultas na linguagem de programação que utilizamos, em nosso caso Python, sem necessidade de escrever SQL. A ORM que vamos utilizar nesse curso será [Tortoise](https://tortoise.github.io/), visto que ela permite o uso de asíncronismo, uma das principais vantagens de FastAPI. Já o banco de dados escolhido é o [PostgreSQL](https://www.postgresql.org/), um dos mais utilizados no mercado.

### Tortoise

Vejamos em linhas gerais como usar Tortoise em nossos projetos. Primeiro certifique-se que a instância de PostgreSQL está ativa com o comando.
```bash
systemctl status postgresql
```

Para usar Tortoise, precisamos primeiro criar um banco de dados que vai conter as tabelas que criarmos. Vamos criar um banco chamado `bookstore` e, para isso, execute os seguintes comandos no terminal. A senha default é `postgres`.
```bash
psql --username=postgres --host=localhost
CREATE DATABASE bookstore;
```

Uma vez o banco criado e ativo, podemos nos concentrar em como usar a ORM. Nesse exemplo, vamos definir uma classe chamada `Book` que mapeará uma tabela chamada `books` usando Tortoise. Essa tabela terá uma chave primária que será o campo `id` criado automaticamente, um campo `name` do tipo Char, um campo `description` também do tipo Char, um campo `price` que será um float e por fim um campo `created_at` que será do tipo data e será criado automaticamente sem que precisemos definí-lo.

Em um arquivo chamado models.py, digite:
```python
from tortoise import fields
from tortoise.models import Model

import schemas

class Book(Model):
    """
    This represents a book in the database.
    """

    class Meta:
        table="books"

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    description = fields.CharField(max_length=100)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    created_at = fields.DatetimeField(auto_now_add=True)

    def to_book() -> schemas.Book:
        """Create a book of type schemas.Book from models.Book"""
        return Book(**self.dict())
```

Agora, modifique o arquivo `main.py` para que esteja assim:
```python
from typing import List
import logging
from fastapi import FastAPI, status

import schemas
import models

app = FastAPI()

@app.post("/book", status_code=status.HTTP_201_CREATED)
async def create_book(book: schemas.Book) -> None:
    """Create a new book in the table 'books'"""
    book_db: models.Book = await models.Book.create(**book.dict(exclude_unset=True))
    logging.info(f"Book {book_df.title} was created with id: {book.id}")

@app.get("/books", status_code=status.HTTP_200_OK)
async def get_all_books(book: schemas.Book) -> List[Book]:
    """Return all books contained in the table 'books'"""
    return [book_db.to_book() for book_db in (await models.Book.all())]

if __name__=="__main__":
    register_tortoise(
        app,
        db_url="postgres://postgres:postgres@127.0.0.1:5432/bookstore",
        modules={"models": ["models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
```
Aqui, temos dois endpoints, o POST `/book` cria um livro na tabela `books` a partir da payload que ele recebe e o GET `/books` recupera todos os livros no banco de dados. Veja que a interface fornecida por Tortoise é capaz de executar consultas ao banco de forma asíncrona o que ajuda a otimizar a performance da API.

Ao iniciar o servidor, o comando `register_tortoise` será executado. Ele iniciará a API e criará uma conexão com a base de dados PostgreSQL usando a url de conexão "postgres://postgres:postgres@127.0.0.1:5432/bookstore" que identifica a instância do bando de dados. Essa url segue o formato 
"DB_TYPE://USERNAME:PASSWORD@HOST:PORT/DB_NAME". Ao definir `generate_schemas` como `True` as tabelas definas em models.py serão criadas no bando de dados `bookstore` sem que precisemos executar o SQL para isso diretamente. Tortoise sabe que deve criar tabelas a partir de models.py, pois o dissemos no parâmetro `modules` de `register_tortoise`.

Tortoise também nos possibilita diversas outras capacidades de manipulação de dados como filtrar e definir relações mais complexas entre as tabelas. Nós implementaremos uma aplicação mais completa na seção onde implementaremos um projeto com FastAPI. 

# Segurança no FastAPI

Não importa o framework que você decida usar, a segurança da API é um assunto extremamente importante e precisa ser cuidado com muita atenção. Existem muitos jeitos de garantir que seus endpoints sejam requisitados somente por aqueles que estão autenticados e possuem os acessos corretos. Atualmente, a utilização de tokens e do framework OAuth2 tem dominado o mercado em relação a essa segurança. Porém, aqui, veremos um jeito mais simples a fim de introduzir o assunto e facilitar o entendimento. Para isso, vamos usar a autenticação do tipo `Basic` nesse guia em vez de outras mais complexas como utilizando tokens JWT.

A autenticação do tipo `Basic` requer apenas que o cliente da API passe um cabeçalho (header) na requisição informando o nome de usuário e sua senha. No lado da API, verificamos que o usuário de fato existe e que a senha fornecida é correta. Caso esses testes sejam positivos, damos continuidade à lógica do endpoint e retornamos a devida resposta. Entretanto, se houver falha, o endpoint retornará o erro 401 que significa que o cliente não está autorizado.

Vejamos como implementar isso com um exemplo:
```python
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> HTTPBasicCredentials:
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"john"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )

    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"password"
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials

@app.get("/user")
def get_user(credentials: HTTPBasicCredentials = Depends(get_current_username)):
    return {"username": credentials.username}
```

Aqui, definimos a variável `security` como uma instância de `HTTPBasic` e criamos uma função que depende dessa variável. Por sua vez, essa função é atribuíada ao parâmetro `credentials` do endpoint GET `user`. Ao fazer isso, quando o endpoint for requisitado, FastAPI vai tentar chamar essa função com os valores fornecidos pelo cliente no header. Isso acontece, pois estamos usando a classe `Depends` que declara uma dependência que deve ser satisfeita. Ao chamar essa função, fazemos a verificação usuário por seu nome que deve ser `john` e sua senha `password`. Se os valores estiverem corretos, retornamos o nome do usuário. Caso contrário retornamos o erro 401. 

Para este exemplo, será melhor usar a interface fornecida pelo FastAPI no Swagger. Para acessar o endpoint `/user`, é preciso passar as credenciais corretas do usuário que são username=john e password=password. Ao fazer isso, podemos chamar o endpoint.

Se você quiser se aprofundar mais em segurança, confira esse artigo no Medium [The Role Cryptography Plays in Security](https://medium.com/@luikymagno/the-role-cryptography-plays-in-security-32d522413e1e).

# Mini Projeto
Nessa seção, vamos colocar tudo o que vimos em prática em um projeto que vai simular alguns aspectos do contexto de uma livraria. Além disso, após terminar a implementação, vamos dar os primeiros passos nos testes da aplicação para garantir que ela funcione como esperado, assim como vamos criar uma imagem docker para ela a fim de que ela possa ser implantada em qualquer máquina onde Docker esteja instalado.

## Modelagem dos Dados

Para o contexto simulado em nosso projeto, teremos 3 entidades que serão:
* user com atributos username e password
* book com atributos title, author, description, price

Cada uma dessas entidades será mapeada por uma tabela. Além disso, cada entidade deve ser mapeada também com uma classe que extende o `BaseModel` de Pydantic para que possa melhor interagir nos endpoints.


Em um arquivo schemas.py, insira:
```python
from typing import Optional
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    price: float

class User(BaseModel):
    username: str
    password: str
```

Para modelar essas entidades no banco de dados, precisamos entender a relação entre elas para que possamos as implementar corretamente usando Tortoise. Vamos pensar um pouco, um usuário pode comprar vários livros, mas uma unidade de um livro só pode ser comprada por um usuário. Assim, vemos que a relação entre as entidade é um usuário para muitos livros. Para implementar essa relação, uma referência ao usuário, logo sua chave primária, deve exister em livro, sendo esse o conceito de chave estrangeira.

Em um arquivo models.py, insira:
```python
from tortoise import fields
from tortoise.models import Model

import schemas as schemas

class User(Model):
    """
    This represents a book in the database.
    """

    class Meta:
        table="users"

    username = fields.CharField(max_length=100, pk=True, unique=True)
    password = fields.CharField(max_length=100)
    books: fields.ReverseRelation["Book"]

    def to_user(self) -> schemas.User:
        """Create a book of type schemas.Book from models.Book"""
        return schemas.User(**dict(self))

class Book(Model):
    """
    This represents a book in the database.
    """

    class Meta:
        table="books"

    id = fields.IntField(pk=True, unique=True)
    title = fields.CharField(max_length=100)
    description = fields.CharField(max_length=100)
    author = fields.CharField(max_length=100)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    sold = fields.BooleanField(default=False)
    user: fields.ForeignKeyNullableRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="books", null=True
    )

    def to_book(self) -> schemas.Book:
        """Create a book of type schemas.Book from models.Book"""
        print(dict(self))
        return schemas.Book(**dict(self))
```

## Endpoints

Feito a modelagem dos dados, podemos começar a implementar a lógica dos endpoints.

Em nosso projeto, teremos endpoints.
* POST `/user`. Cria um usuário a partir de schemas.User.
* POST `/book`. Cria um usuário a partir de schemas.Book.
* GET `/book`. Recupera um livro a partir de seu título.
* POST `/book/sell`. Protegido por HTTP Basic, realiza a venda de um livro pelo seu título ao usuário autenticado.
* GET `/books`. Protegido por HTTP Basic, recupera todos os livros do usuário autenticado.

Em um arquivo main.py, insira:
```python
import logging
import secrets
from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from tortoise.contrib.fastapi import register_tortoise

import schemas as schemas
import models as models
from config import Config

app = FastAPI()

security = HTTPBasic()


async def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> models.User:
    user_db = await models.User.filter(username=credentials.username).first()
    if user_db is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    password_bytes = credentials.password.encode("utf8")
    is_correct_password = secrets.compare_digest(
        password_bytes, user_db.password.encode("utf8")
    )

    if not (is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user_db

@app.post("/user", status_code=status.HTTP_201_CREATED)
async def get_user(user: schemas.User):
    """Create a new user in the table 'users'"""
    logging.info("test")
    user_db = await models.User.create(**user.dict())
    logging.info(f"User {user_db.username} was created")

@app.post("/book", status_code=status.HTTP_201_CREATED)
async def create_book(book: schemas.Book) -> None:
    """Create a new book in the table 'books'"""
    book_db = await models.Book.create(**book.dict(exclude_unset=True))
    logging.info(f"Book {book_db.title} was created with id: {book_db.id}")

@app.get("/book", status_code=status.HTTP_200_OK)
async def get_book(title: str) -> schemas.Book:
    """Get a book by its title"""
    book_db = await models.Book.filter(title=title).first()
    if book_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with title {title} was not found"
        )

    logging.info(f"Book {book_db.title} was retrieved")
    return book_db.to_book()

@app.post("/book/sell", status_code=status.HTTP_201_CREATED)
async def sell_book(title: str, credentials: HTTPBasicCredentials = Depends(get_current_user)) -> None:
    """Sell a book to the authenticated user"""
    book_db = await models.Book.filter(title=title, sold=False).first()
    if book_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with title {title} was not found"
        )

    logging.info(f"Book {book_db.title} was retrieved")
    book_db.update_from_dict({"sold": True, "user_id": credentials.username})
    await book_db.save()

@app.get("/books", status_code=status.HTTP_200_OK)
async def get_books(user_db: models.User = Depends(get_current_user)) -> List[schemas.Book]:
    """Fetch all books of the authenticated user"""
    logging.info(f"User {user_db.username} was retrieved")
    return [book_db.to_book() async for book_db in user_db.books]

register_tortoise(
    app,
    db_url=Config.DB_URL,
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
```

Para melhor organizar o código, crie uma classe de configuração. Em um arquivo config.py insira:
```python
class Config:
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "localhost"
    DB_NAME: str = "library"
    DB_URL: str = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
```

Perceba que os endpoints criados aqui foram implementados usando funções asíncronas, já que operações asíncronas (consultas ao banco de dados) são realizadas.

Com os endpoint implementados, ao ativar o servidor, podemos utilizar a interface do Swagger para realizar operações de cadastro de usuários e livros, assim como vendas e consulta do histórico de compras de um usuário.


## Testes

Uma das partes mais importantes de todo projeto de software é o teste das funcionalidades implementas para tentar mitigar possíveis erros de lógica do sistema. Em Python, a biblioteca Pytest é bastante útil para esta finalidade. Nesse exemplo, vamos testar o endpoint `/books` da nossa API.

Como vamos testar uma aplicação que interage com um banco de dados, uma das opções para não acessar o real banco de dados é usar um banco de dados em memória que será populado e destruído a cada vez que os testes forem executados. Assim, conseguimos simular com mais precisão o cenário real.

O banco de dados em memória escolhido é o [SQLite](https://www.sqlite.org/index.html) e para habilitá-lo, basta trocar a URL de conexão do PostgreSQL para `"sqlite://:memory:"` no `main.py`.

FastAPI também busca facilitar o desenvolvimento em relação aos testes e por isso fornece um cliente de teste que permite interagir com nossa API. Esse cliente é uma instância da classe TestClient. Além disso, para criar o cliente de teste, podemos usar fixtures em Python. De maneira resumida, testes anotados com fixtures terão certas instruções executadas antes e outras depois a cada vez que forem chamados. Essas instruções são definidas na própria fixture e são separadas pelo comando `yield`.

Em um arquivo tests.py, insira:
```python
from typing import Generator, AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from config import Config

from tortoise.contrib.test import finalizer, initializer
from tortoise import Tortoise

import schemas
import models

Config.DB_URL = "sqlite://:memory:"
from main import app

user = schemas.User(username="testuser", password="password")
book = schemas.Book(title="Test Book", author="Test Author", description="Test book description", price=50.0)    

@pytest.fixture
def client() -> Generator:
    with TestClient(app) as c:
        yield c

class TestBooks:
    url = "/books"

    @pytest.mark.asyncio
    async def test_user_without_books(self, client: TestClient) -> None:

        # Populate the db
        await models.User(**user.dict()).save()

        response = client.get(
            self.url,
            auth=(user.username, user.password),
        )
        assert response.status_code == 200
        assert response.json() == []
    
    @pytest.mark.asyncio
    async def test_user_with_book(self, client: TestClient) -> None:

        # Populate the db
        await models.User(**user.dict()).save()
        await models.Book(**book.dict(), user_id=user.username).save()

        response = client.get(
            self.url,
            auth=(user.username, user.password),
        )
        assert response.status_code == 200
        assert response.json() == [book.dict()]
```

Para executar os testes, basta rodar o comand `pytest tests.py`.

## Docker
Docker é um software que permite definir containers onde nossos projetos serão executados de maneira que qualquer outra máquina que possua Docker instalado poderá ativar o container sem a necessidade de se preocupar com demais dependências. Com Docker, podemos agilizar a implantação de nossos projetos em ambientes como produção, assim como compartilhá-los de maneira simples permitindo a facilitação do processo de desenvolvimento.

Primeiro, vamos definir o arquivo Docker que permitirá estabelecer a imagem da qual containers poderão ser criados. Na raíz do projeto, insira o arquivo `Dockerfile`
```dockerfile
# Start from the official Python base image
FROM python:3.9
# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /code
# Copy poetry files to the working directory
COPY poetry.lock pyproject.toml /code
# Copy our files to inside the working directory
COPY . /code/api

# Install dependencies with poetry
RUN poetry install

# Start the server 
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]
```

Agora, basta construir a imagem e instanciar um container a partir dela.
```bash
docker build -t fastapi_project .
docker run -d --name api -p 80:80 --network="host" fastapi_project
```