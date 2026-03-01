# Source: https://fastapi.tiangolo.com/pt/

Title: FastAPI

URL Source: https://fastapi.tiangolo.com/pt/

Markdown Content:
🌐 Tradução por IA e humanos
Esta tradução foi feita por IA orientada por humanos. 🤝

Ela pode conter erros de interpretação do significado original ou soar pouco natural, etc. 🤖

Você pode melhorar esta tradução [ajudando-nos a orientar melhor o LLM de IA](https://fastapi.tiangolo.com/pt/contributing/#translations).

[Versão em inglês](https://fastapi.tiangolo.com/)

[![Image 1: FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com/pt)

_Framework FastAPI, alta performance, fácil de aprender, fácil de codar, pronto para produção_

[![Image 2: Test](https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master)](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)[![Image 3: Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi)[![Image 4: Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi)[![Image 5: Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)](https://pypi.org/project/fastapi)

* * *

**Documentação**: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com/pt)

**Código fonte**: [https://github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)

* * *

FastAPI é um moderno e rápido (alta performance) framework web para construção de APIs com Python, baseado nos type hints padrões do Python.

Os recursos chave são:

*   **Rápido**: alta performance, equivalente a **NodeJS** e **Go** (graças ao Starlette e Pydantic). [Um dos frameworks mais rápidos disponíveis](https://fastapi.tiangolo.com/pt/#performance).
*   **Rápido para codar**: Aumenta a velocidade para desenvolver recursos entre 200% a 300%. *
*   **Poucos bugs**: Reduz cerca de 40% de erros induzidos por humanos (desenvolvedores). *
*   **Intuitivo**: Grande suporte a editores. Completação em todos os lugares. Menos tempo debugando.
*   **Fácil**: Projetado para ser fácil de aprender e usar. Menos tempo lendo docs.
*   **Enxuto**: Minimize duplicação de código. Múltiplas funcionalidades para cada declaração de parâmetro. Menos bugs.
*   **Robusto**: Tenha código pronto para produção. E com documentação interativa automática.
*   **Baseado em padrões**: Baseado em (e totalmente compatível com) os padrões abertos para APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (anteriormente conhecido como Swagger) e [JSON Schema](https://json-schema.org/).

* estimativas baseadas em testes realizados com equipe interna de desenvolvimento, construindo aplicações em produção.

[![Image 6](https://fastapi.tiangolo.com/img/sponsors/fastapicloud.png)](https://fastapicloud.com/ "FastAPI Cloud. By the same team behind FastAPI. You code. We Cloud.")

### Patrocinadores Ouro e Prata[¶](https://fastapi.tiangolo.com/pt/#gold-and-silver-sponsors)

[![Image 7](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io/?ref=fastapi "BlockBee Cryptocurrency Payment Gateway")[![Image 8](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI files")[![Image 9](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge "Auth, user management and more for your B2B product")[![Image 10](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-gh "Zuplo: Deploy, Secure, Document, and Monetize your FastAPI")[![Image 11](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com/?utm_source=fastapi "liblab - Generate SDKs from FastAPI")[![Image 12](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy & scale any full-stack web app on Render. Focus on building apps, not infra.")[![Image 13](https://fastapi.tiangolo.com/img/sponsors/coderabbit.png)](https://www.coderabbit.ai/?utm_source=fastapi&utm_medium=badge&utm_campaign=fastapi "Cut Code Review Time & Bugs in Half with CodeRabbit")[![Image 14](https://fastapi.tiangolo.com/img/sponsors/subtotal.svg)](https://subtotal.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=open-source "The Gold Standard in Retail Account Linking")[![Image 15](https://fastapi.tiangolo.com/img/sponsors/railway.png)](https://docs.railway.com/guides/fastapi?utm_medium=integration&utm_source=docs&utm_campaign=fastapi "Deploy enterprise applications at startup speed")[![Image 16](https://fastapi.tiangolo.com/img/sponsors/serpapi.png)](https://serpapi.com/?utm_source=fastapi_website "SerpApi: Web Search API")[![Image 17](https://fastapi.tiangolo.com/img/sponsors/greptile.png)](https://www.greptile.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=fastapi_sponsor_page "Greptile: The AI Code Reviewer")[![Image 18](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/?utm_source=fastapi&utm_medium=sponsor&utm_content=display "Pay as you go for market data")[![Image 19](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com/editor?utm_source=fastapi+repo&utm_medium=github+sponsorship "SDKs for your API | Speakeasy")[![Image 20](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/ "Svix - Webhooks as a service")[![Image 21](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral "Stainless | Generate best-in-class SDKs")[![Image 22](https://fastapi.tiangolo.com/img/sponsors/permit.png)](https://www.permit.io/blog/implement-authorization-in-fastapi?utm_source=github&utm_medium=referral&utm_campaign=fastapi "Fine-Grained Authorization for FastAPI")[![Image 23](https://fastapi.tiangolo.com/img/sponsors/interviewpal.png)](https://www.interviewpal.com/?utm_source=fastapi&utm_medium=open-source&utm_campaign=dev-hiring "InterviewPal - AI Interview Coach for Engineers and Devs")[![Image 24](https://fastapi.tiangolo.com/img/sponsors/dribia.png)](https://dribia.com/en/ "Dribia - Data Science within your reach")

[Outros patrocinadores](https://fastapi.tiangolo.com/pt/fastapi-people/#sponsors)

Opiniões[¶](https://fastapi.tiangolo.com/pt/#opinions)
------------------------------------------------------

"_[...] Estou usando **FastAPI** muito esses dias. [...] Estou na verdade planejando utilizar ele em todos os times de **serviços ML na Microsoft**. Alguns deles estão sendo integrados no \_core_ do produto **Windows** e alguns produtos **Office**._"

Kabir Khan - **Microsoft**[(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

"_Nós adotamos a biblioteca **FastAPI** para iniciar um servidor **REST** que pode ser consultado para obter **previsões**. [para o Ludwig]_"

Piero Molino, Yaroslav Dudin, e Sai Sumanth Miryala - **Uber**[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

"_A **Netflix** tem o prazer de anunciar o lançamento open-source do nosso framework de orquestração de **gerenciamento de crises**: **Dispatch**! [criado com **FastAPI**]_"

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

"_Estou muito entusiasmado com o **FastAPI**. É tão divertido!_"

* * *

"_Honestamente, o que você construiu parece super sólido e refinado. De muitas formas, é o que eu queria que o **Hug** fosse - é realmente inspirador ver alguém construir isso._"

Timothy Crosley - **criador do[Hug](https://github.com/hugapi/hug)**[(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

"_Se você está procurando aprender um **framework moderno** para construir APIs REST, dê uma olhada no **FastAPI** [...] É rápido, fácil de usar e fácil de aprender [...]_"

"_Nós trocamos nossas **APIs** por **FastAPI** [...] Acredito que você gostará dele [...]_"

* * *

"_Se alguém estiver procurando construir uma API Python para produção, eu recomendaria fortemente o **FastAPI**. Ele é **lindamente projetado**, **simples de usar** e **altamente escalável**, e se tornou um **componente chave** para a nossa estratégia de desenvolvimento API first, impulsionando diversas automações e serviços, como o nosso Virtual TAC Engineer._"

Deon Pillsbury - **Cisco**[(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/)

* * *

Mini documentário do FastAPI[¶](https://fastapi.tiangolo.com/pt/#fastapi-mini-documentary)
------------------------------------------------------------------------------------------

Há um [mini documentário do FastAPI](https://www.youtube.com/watch?v=mpR8ngthqiE) lançado no fim de 2025, você pode assisti-lo online:

[![Image 25: FastAPI Mini Documentary](https://fastapi.tiangolo.com/img/fastapi-documentary.jpg)](https://www.youtube.com/watch?v=mpR8ngthqiE)

**Typer**, o FastAPI das interfaces de linhas de comando[¶](https://fastapi.tiangolo.com/pt/#typer-the-fastapi-of-clis)
-----------------------------------------------------------------------------------------------------------------------

[![Image 26](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com/)

Se você estiver construindo uma aplicação CLI para ser utilizada no terminal ao invés de uma API web, dê uma olhada no [**Typer**](https://typer.tiangolo.com/).

**Typer** é o irmão menor do FastAPI. E seu propósito é ser o **FastAPI das CLIs**. ⌨️ 🚀

Requisitos[¶](https://fastapi.tiangolo.com/pt/#requirements)
------------------------------------------------------------

FastAPI está nos ombros de gigantes:

*   [Starlette](https://www.starlette.dev/) para as partes web.
*   [Pydantic](https://docs.pydantic.dev/) para a parte de dados.

Instalação[¶](https://fastapi.tiangolo.com/pt/#installation)
------------------------------------------------------------

Crie e ative um [ambiente virtual](https://fastapi.tiangolo.com/pt/virtual-environments/) e então instale o FastAPI:

**Nota**: Certifique-se de que você colocou `"fastapi[standard]"` com aspas, para garantir que funcione em todos os terminais.

Exemplo[¶](https://fastapi.tiangolo.com/pt/#example)
----------------------------------------------------

### Crie[¶](https://fastapi.tiangolo.com/pt/#create-it)

Crie um arquivo `main.py` com:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

Ou use `async def`...
Se seu código utiliza `async` / `await`, use `async def`:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

**Nota**:

Se você não sabe, verifique a seção _"Com pressa?"_ sobre [`async` e `await` nas docs](https://fastapi.tiangolo.com/pt/async/#in-a-hurry).

### Rode[¶](https://fastapi.tiangolo.com/pt/#run-it)

Rode o servidor com:

Sobre o comando `fastapi dev main.py`...
O comando `fastapi dev` lê o seu arquivo `main.py`, identifica o aplicativo **FastAPI** nele, e inicia um servidor usando o [Uvicorn](https://www.uvicorn.dev/).

Por padrão, o `fastapi dev` iniciará com _auto-reload_ habilitado para desenvolvimento local.

Você pode ler mais sobre isso na [documentação do FastAPI CLI](https://fastapi.tiangolo.com/pt/fastapi-cli/).

### Verifique[¶](https://fastapi.tiangolo.com/pt/#check-it)

Abra seu navegador em [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery).

Você verá a resposta JSON como:

```
{"item_id": 5, "q": "somequery"}
```

Você acabou de criar uma API que:

*   Recebe requisições HTTP nos _paths_`/` e `/items/{item_id}`.
*   Ambos _paths_ fazem _operações_`GET` (também conhecido como _métodos_ HTTP).
*   O _path_`/items/{item_id}` tem um _parâmetro de path_`item_id` que deve ser um `int`.
*   O _path_`/items/{item_id}` tem um _parâmetro query_`q``str` opcional.

### Documentação Interativa da API[¶](https://fastapi.tiangolo.com/pt/#interactive-api-docs)

Agora vá para [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Você verá a documentação automática interativa da API (fornecida por [Swagger UI](https://github.com/swagger-api/swagger-ui)):

![Image 27: Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Documentação Alternativa da API[¶](https://fastapi.tiangolo.com/pt/#alternative-api-docs)

E agora, vá para [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

Você verá a documentação automática alternativa (fornecida por [ReDoc](https://github.com/Rebilly/ReDoc)):

![Image 28: ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

Evoluindo o Exemplo[¶](https://fastapi.tiangolo.com/pt/#example-upgrade)
------------------------------------------------------------------------

Agora modifique o arquivo `main.py` para receber um corpo de uma requisição `PUT`.

Declare o corpo utilizando tipos padrão Python, graças ao Pydantic.

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

O servidor `fastapi dev` deverá recarregar automaticamente.

### Evoluindo a Documentação Interativa da API[¶](https://fastapi.tiangolo.com/pt/#interactive-api-docs-upgrade)

Agora vá para [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

*   A documentação interativa da API será automaticamente atualizada, incluindo o novo corpo:

![Image 29: Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

*   Clique no botão "Try it out", ele permitirá que você preencha os parâmetros e interaja diretamente com a API:

![Image 30: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

*   Então clique no botão "Execute", a interface do usuário irá se comunicar com a API, enviar os parâmetros, pegar os resultados e mostrá-los na tela:

![Image 31: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Evoluindo a Documentação Alternativa da API[¶](https://fastapi.tiangolo.com/pt/#alternative-api-docs-upgrade)

E agora, vá para [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

*   A documentação alternativa também irá refletir o novo parâmetro query e o corpo:

![Image 32: ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### Recapitulando[¶](https://fastapi.tiangolo.com/pt/#recap)

Resumindo, você declara **uma vez** os tipos dos parâmetros, corpo etc. como parâmetros de função.

Você faz isso com os tipos padrão do Python moderno.

Você não terá que aprender uma nova sintaxe, métodos ou classes de uma biblioteca específica etc.

Apenas **Python** padrão.

Por exemplo, para um `int`:

```
item_id: int
```

ou para um modelo mais complexo, `Item`:

```
item: Item
```

...e com essa única declaração você tem:

*   Suporte ao Editor, incluindo:
    *   Completação.
    *   Verificação de tipos.

*   Validação de dados:
    *   Erros automáticos e claros quando o dado é inválido.
    *   Validação até para objetos JSON profundamente aninhados.

*   Conversão de dados de entrada: vindo da rede para dados e tipos Python. Consegue ler:
    *   JSON.
    *   Parâmetros de path.
    *   Parâmetros query.
    *   Cookies.
    *   Cabeçalhos.
    *   Formulários.
    *   Arquivos.

*   Conversão de dados de saída: convertendo de tipos e dados Python para dados de rede (como JSON):
    *   Converte tipos Python (`str`, `int`, `float`, `bool`, `list` etc).
    *   Objetos `datetime`.
    *   Objetos `UUID`.
    *   Modelos de Banco de Dados.
    *   ...e muito mais.

*   Documentação interativa automática da API, incluindo 2 alternativas de interface de usuário:
    *   Swagger UI.
    *   ReDoc.

* * *

Voltando ao código do exemplo anterior, **FastAPI** irá:

*   Validar que existe um `item_id` no path para requisições `GET` e `PUT`.
*   Validar que `item_id` é do tipo `int` para requisições `GET` e `PUT`.
    *   Se não for, o cliente verá um erro útil e claro.

*   Verificar se existe um parâmetro query opcional nomeado como `q` (como em `http://127.0.0.1:8000/items/foo?q=somequery`) para requisições `GET`.
    *   Como o parâmetro `q` é declarado com `= None`, ele é opcional.
    *   Sem o `None` ele seria obrigatório (como o corpo no caso de `PUT`).

*   Para requisições `PUT` para `/items/{item_id}`, lerá o corpo como JSON:
    *   Verifica que tem um atributo obrigatório `name` que deve ser `str`.
    *   Verifica que tem um atributo obrigatório `price` que tem que ser um `float`.
    *   Verifica que tem um atributo opcional `is_offer`, que deve ser um `bool`, se presente.
    *   Tudo isso também funcionaria para objetos JSON profundamente aninhados.

*   Converter de e para JSON automaticamente.
*   Documentar tudo com OpenAPI, que poderá ser usado por:
    *   Sistemas de documentação interativos.
    *   Sistemas de clientes de geração de código automáticos, para muitas linguagens.

*   Fornecer diretamente 2 interfaces web de documentação interativa.

* * *

Nós apenas arranhamos a superfície, mas você já tem ideia de como tudo funciona.

Experimente mudar a seguinte linha:

```
return {"item_name": item.name, "item_id": item_id}
```

...de:

```
... "item_name": item.name ...
```

...para:

```
... "item_price": item.price ...
```

...e veja como seu editor irá auto-completar os atributos e saberá os tipos:

![Image 33: editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

Para um exemplo mais completo incluindo mais recursos, veja [Tutorial - Guia do Usuário](https://fastapi.tiangolo.com/pt/tutorial/).

**Alerta de Spoiler**: o tutorial - guia do usuário inclui:

*   Declaração de **parâmetros** de diferentes lugares como: **cabeçalhos**, **cookies**, **campos de formulários** e **arquivos**.
*   Como configurar **limitações de validação** como `maximum_length` ou `regex`.
*   Um poderoso e fácil de usar sistema de **Injeção de Dependência**.
*   Segurança e autenticação, incluindo suporte para **OAuth2** com autenticação com **JWT tokens** e **HTTP Basic**.
*   Técnicas mais avançadas (mas igualmente fáceis) para declaração de **modelos JSON profundamente aninhados** (graças ao Pydantic).
*   Integrações **GraphQL** com o [Strawberry](https://strawberry.rocks/) e outras bibliotecas.
*   Muitos recursos extras (graças ao Starlette) como:
    *   **WebSockets**
    *   testes extremamente fáceis baseados em HTTPX e `pytest`
    *   **CORS**
    *   **Cookie Sessions**
    *   ...e mais.

### Implemente sua aplicação (opcional)[¶](https://fastapi.tiangolo.com/pt/#deploy-your-app-optional)

Você pode opcionalmente implantar sua aplicação FastAPI na [FastAPI Cloud](https://fastapicloud.com/), vá e entre na lista de espera se ainda não o fez. 🚀

Se você já tem uma conta na **FastAPI Cloud** (nós convidamos você da lista de espera 😉), pode implantar sua aplicação com um único comando.

Antes de implantar, certifique-se de que está autenticado:

Depois, implemente sua aplicação:

É isso! Agora você pode acessar sua aplicação nesse URL. ✨

#### Sobre a FastAPI Cloud[¶](https://fastapi.tiangolo.com/pt/#about-fastapi-cloud)

**[FastAPI Cloud](https://fastapicloud.com/)** é construída pelo mesmo autor e equipe por trás do **FastAPI**.

Ela simplifica o processo de **construir**, **implantar** e **acessar** uma API com esforço mínimo.

Traz a mesma **experiência do desenvolvedor** de construir aplicações com FastAPI para **implantá-las** na nuvem. 🎉

A FastAPI Cloud é a principal patrocinadora e financiadora dos projetos open source do ecossistema _FastAPI and friends_. ✨

#### Implante em outros provedores de nuvem[¶](https://fastapi.tiangolo.com/pt/#deploy-to-other-cloud-providers)

FastAPI é open source e baseado em padrões. Você pode implantar aplicações FastAPI em qualquer provedor de nuvem que escolher.

Siga os tutoriais do seu provedor de nuvem para implantar aplicações FastAPI com eles. 🤓

Performance[¶](https://fastapi.tiangolo.com/pt/#performance)
------------------------------------------------------------

Testes de performance da Independent TechEmpower mostram aplicações **FastAPI** rodando sob Uvicorn como [um dos frameworks Python mais rápidos disponíveis](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7), somente atrás de Starlette e Uvicorn (utilizados internamente pelo FastAPI). (*)

Para entender mais sobre isso, veja a seção [Comparações](https://fastapi.tiangolo.com/pt/benchmarks/).

Dependências[¶](https://fastapi.tiangolo.com/pt/#dependencies)
--------------------------------------------------------------

O FastAPI depende do Pydantic e do Starlette.

### Dependências `standard`[¶](https://fastapi.tiangolo.com/pt/#standard-dependencies)

Quando você instala o FastAPI com `pip install "fastapi[standard]"`, ele vem com o grupo `standard` de dependências opcionais:

Utilizado pelo Pydantic:

*   [`email-validator`](https://github.com/JoshData/python-email-validator) - para validação de email.

Utilizado pelo Starlette:

*   [`httpx`](https://www.python-httpx.org/) - Obrigatório caso você queira utilizar o `TestClient`.
*   [`jinja2`](https://jinja.palletsprojects.com/) - Obrigatório se você quer utilizar a configuração padrão de templates.
*   [`python-multipart`](https://github.com/Kludex/python-multipart) - Obrigatório se você deseja suporte a "parsing" de formulário, com `request.form()`.

Utilizado pelo FastAPI:

*   [`uvicorn`](https://www.uvicorn.dev/) - para o servidor que carrega e serve a sua aplicação. Isto inclui `uvicorn[standard]`, que inclui algumas dependências (e.g. `uvloop`) necessárias para servir em alta performance.
*   `fastapi-cli[standard]` - que disponibiliza o comando `fastapi`.
    *   Isso inclui `fastapi-cloud-cli`, que permite implantar sua aplicação FastAPI na [FastAPI Cloud](https://fastapicloud.com/).

### Sem as dependências `standard`[¶](https://fastapi.tiangolo.com/pt/#without-standard-dependencies)

Se você não deseja incluir as dependências opcionais `standard`, você pode instalar utilizando `pip install fastapi` ao invés de `pip install "fastapi[standard]"`.

### Sem o `fastapi-cloud-cli`[¶](https://fastapi.tiangolo.com/pt/#without-fastapi-cloud-cli)

Se você quiser instalar o FastAPI com as dependências padrão, mas sem o `fastapi-cloud-cli`, você pode instalar com `pip install "fastapi[standard-no-fastapi-cloud-cli]"`.

### Dependências opcionais adicionais[¶](https://fastapi.tiangolo.com/pt/#additional-optional-dependencies)

Existem algumas dependências adicionais que você pode querer instalar.

Dependências opcionais adicionais do Pydantic:

*   [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) - para gerenciamento de configurações.
*   [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) - para tipos extras a serem utilizados com o Pydantic.

Dependências opcionais adicionais do FastAPI:

*   [`orjson`](https://github.com/ijl/orjson) - Obrigatório se você deseja utilizar o `ORJSONResponse`.
*   [`ujson`](https://github.com/esnme/ultrajson) - Obrigatório se você deseja utilizar o `UJSONResponse`.

Licença[¶](https://fastapi.tiangolo.com/pt/#license)
----------------------------------------------------

Esse projeto é licenciado sob os termos da licença MIT.
