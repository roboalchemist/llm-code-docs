# Source: https://fastapi.tiangolo.com/es/

Title: FastAPI

URL Source: https://fastapi.tiangolo.com/es/

Markdown Content:
🌐 Traducción por IA y humanos
Esta traducción fue hecha por IA guiada por humanos. 🤝

Podría tener errores al interpretar el significado original, o sonar poco natural, etc. 🤖

Puedes mejorar esta traducción [ayudándonos a guiar mejor al LLM de IA](https://fastapi.tiangolo.com/es/contributing/#translations).

[Versión en inglés](https://fastapi.tiangolo.com/)

[![Image 1: FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com/es)

_FastAPI framework, alto rendimiento, fácil de aprender, rápido de programar, listo para producción_

[![Image 2: Test](https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master)](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)[![Image 3: Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi)[![Image 4: Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi)[![Image 5: Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)](https://pypi.org/project/fastapi)

* * *

**Documentación**: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com/es)

**Código Fuente**: [https://github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)

* * *

FastAPI es un framework web moderno, rápido (de alto rendimiento), para construir APIs con Python basado en las anotaciones de tipos estándar de Python.

Las funcionalidades clave son:

*   **Rápido**: Muy alto rendimiento, a la par con **NodeJS** y **Go** (gracias a Starlette y Pydantic). [Uno de los frameworks Python más rápidos disponibles](https://fastapi.tiangolo.com/es/#performance).
*   **Rápido de programar**: Aumenta la velocidad para desarrollar funcionalidades en aproximadamente un 200% a 300%. *
*   **Menos bugs**: Reduce en aproximadamente un 40% los errores inducidos por humanos (desarrolladores). *
*   **Intuitivo**: Gran soporte para editores. Autocompletado en todas partes. Menos tiempo depurando.
*   **Fácil**: Diseñado para ser fácil de usar y aprender. Menos tiempo leyendo documentación.
*   **Corto**: Minimiza la duplicación de código. Múltiples funcionalidades desde cada declaración de parámetro. Menos bugs.
*   **Robusto**: Obtén código listo para producción. Con documentación interactiva automática.
*   **Basado en estándares**: Basado (y completamente compatible) con los estándares abiertos para APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (anteriormente conocido como Swagger) y [JSON Schema](https://json-schema.org/).

* estimación basada en pruebas con un equipo de desarrollo interno, construyendo aplicaciones de producción.

[![Image 6](https://fastapi.tiangolo.com/img/sponsors/fastapicloud.png)](https://fastapicloud.com/ "FastAPI Cloud. By the same team behind FastAPI. You code. We Cloud.")

### Sponsors Oro y Plata[¶](https://fastapi.tiangolo.com/es/#gold-and-silver-sponsors)

[![Image 7](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io/?ref=fastapi "BlockBee Cryptocurrency Payment Gateway")[![Image 8](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI files")[![Image 9](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge "Auth, user management and more for your B2B product")[![Image 10](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-gh "Zuplo: Deploy, Secure, Document, and Monetize your FastAPI")[![Image 11](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com/?utm_source=fastapi "liblab - Generate SDKs from FastAPI")[![Image 12](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy & scale any full-stack web app on Render. Focus on building apps, not infra.")[![Image 13](https://fastapi.tiangolo.com/img/sponsors/coderabbit.png)](https://www.coderabbit.ai/?utm_source=fastapi&utm_medium=badge&utm_campaign=fastapi "Cut Code Review Time & Bugs in Half with CodeRabbit")[![Image 14](https://fastapi.tiangolo.com/img/sponsors/subtotal.svg)](https://subtotal.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=open-source "The Gold Standard in Retail Account Linking")[![Image 15](https://fastapi.tiangolo.com/img/sponsors/railway.png)](https://docs.railway.com/guides/fastapi?utm_medium=integration&utm_source=docs&utm_campaign=fastapi "Deploy enterprise applications at startup speed")[![Image 16](https://fastapi.tiangolo.com/img/sponsors/serpapi.png)](https://serpapi.com/?utm_source=fastapi_website "SerpApi: Web Search API")[![Image 17](https://fastapi.tiangolo.com/img/sponsors/greptile.png)](https://www.greptile.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=fastapi_sponsor_page "Greptile: The AI Code Reviewer")[![Image 18](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/?utm_source=fastapi&utm_medium=sponsor&utm_content=display "Pay as you go for market data")[![Image 19](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com/editor?utm_source=fastapi+repo&utm_medium=github+sponsorship "SDKs for your API | Speakeasy")[![Image 20](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/ "Svix - Webhooks as a service")[![Image 21](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral "Stainless | Generate best-in-class SDKs")[![Image 22](https://fastapi.tiangolo.com/img/sponsors/permit.png)](https://www.permit.io/blog/implement-authorization-in-fastapi?utm_source=github&utm_medium=referral&utm_campaign=fastapi "Fine-Grained Authorization for FastAPI")[![Image 23](https://fastapi.tiangolo.com/img/sponsors/interviewpal.png)](https://www.interviewpal.com/?utm_source=fastapi&utm_medium=open-source&utm_campaign=dev-hiring "InterviewPal - AI Interview Coach for Engineers and Devs")[![Image 24](https://fastapi.tiangolo.com/img/sponsors/dribia.png)](https://dribia.com/en/ "Dribia - Data Science within your reach")

[Otros sponsors](https://fastapi.tiangolo.com/es/fastapi-people/#sponsors)

Opiniones[¶](https://fastapi.tiangolo.com/es/#opinions)
-------------------------------------------------------

"_[...] Estoy usando **FastAPI** un montón estos días. [...] De hecho, estoy planeando usarlo para todos los servicios de **ML de mi equipo en Microsoft**. Algunos de ellos se están integrando en el núcleo del producto **Windows** y algunos productos de **Office**._"

Kabir Khan - **Microsoft**[(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

"_Adoptamos el paquete **FastAPI** para crear un servidor **REST** que pueda ser consultado para obtener **predicciones**. [para Ludwig]_"

Piero Molino, Yaroslav Dudin, y Sai Sumanth Miryala - **Uber**[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

"_**Netflix** se complace en anunciar el lanzamiento de código abierto de nuestro framework de orquestación de **gestión de crisis**: **Dispatch**! [construido con **FastAPI**]_"

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

"_Estoy súper emocionado con **FastAPI**. ¡Es tan divertido!_"

* * *

"_Honestamente, lo que has construido parece súper sólido y pulido. En muchos aspectos, es lo que quería que **Hug** fuera; es realmente inspirador ver a alguien construir eso._"

Timothy Crosley - **[Hug](https://github.com/hugapi/hug) creador**[(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

"_Si estás buscando aprender un **framework moderno** para construir APIs REST, échale un vistazo a **FastAPI** [...] Es rápido, fácil de usar y fácil de aprender [...]_"

"_Nos hemos cambiado a **FastAPI** para nuestras **APIs** [...] Creo que te gustará [...]_"

* * *

"_Si alguien está buscando construir una API de Python para producción, altamente recomendaría **FastAPI**. Está **hermosamente diseñado**, es **simple de usar** y **altamente escalable**, se ha convertido en un **componente clave** en nuestra estrategia de desarrollo API primero y está impulsando muchas automatizaciones y servicios como nuestro Ingeniero Virtual TAC._"

Deon Pillsbury - **Cisco**[(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/)

* * *

Mini documental de FastAPI[¶](https://fastapi.tiangolo.com/es/#fastapi-mini-documentary)
----------------------------------------------------------------------------------------

Hay un [mini documental de FastAPI](https://www.youtube.com/watch?v=mpR8ngthqiE) lanzado a finales de 2025, puedes verlo online:

[![Image 25: FastAPI Mini Documentary](https://fastapi.tiangolo.com/img/fastapi-documentary.jpg)](https://www.youtube.com/watch?v=mpR8ngthqiE)

**Typer**, el FastAPI de las CLIs[¶](https://fastapi.tiangolo.com/es/#typer-the-fastapi-of-clis)
------------------------------------------------------------------------------------------------

[![Image 26](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com/)

Si estás construyendo una aplicación de CLI para ser usada en la terminal en lugar de una API web, revisa [**Typer**](https://typer.tiangolo.com/).

**Typer** es el hermano pequeño de FastAPI. Y está destinado a ser el **FastAPI de las CLIs**. ⌨️ 🚀

Requisitos[¶](https://fastapi.tiangolo.com/es/#requirements)
------------------------------------------------------------

FastAPI se apoya en hombros de gigantes:

*   [Starlette](https://www.starlette.dev/) para las partes web.
*   [Pydantic](https://docs.pydantic.dev/) para las partes de datos.

Instalación[¶](https://fastapi.tiangolo.com/es/#installation)
-------------------------------------------------------------

Crea y activa un [entorno virtual](https://fastapi.tiangolo.com/es/virtual-environments/) y luego instala FastAPI:

**Nota**: Asegúrate de poner `"fastapi[standard]"` entre comillas para asegurar que funcione en todas las terminales.

Ejemplo[¶](https://fastapi.tiangolo.com/es/#example)
----------------------------------------------------

### Créalo[¶](https://fastapi.tiangolo.com/es/#create-it)

Crea un archivo `main.py` con:

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

O usa `async def`...
Si tu código usa `async` / `await`, usa `async def`:

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

Si no lo sabes, revisa la sección _"¿Con prisa?"_ sobre [`async` y `await` en la documentación](https://fastapi.tiangolo.com/es/async/#in-a-hurry).

### Córrelo[¶](https://fastapi.tiangolo.com/es/#run-it)

Corre el servidor con:

Acerca del comando `fastapi dev main.py`...
El comando `fastapi dev` lee tu archivo `main.py`, detecta la app **FastAPI** en él y arranca un servidor usando [Uvicorn](https://www.uvicorn.dev/).

Por defecto, `fastapi dev` comenzará con auto-recarga habilitada para el desarrollo local.

Puedes leer más sobre esto en la [documentación del CLI de FastAPI](https://fastapi.tiangolo.com/es/fastapi-cli/).

### Revísalo[¶](https://fastapi.tiangolo.com/es/#check-it)

Abre tu navegador en [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery).

Verás el response JSON como:

```
{"item_id": 5, "q": "somequery"}
```

Ya creaste una API que:

*   Recibe requests HTTP en los _paths_`/` y `/items/{item_id}`.
*   Ambos _paths_ toman _operaciones_`GET` (también conocidas como métodos HTTP).
*   El _path_`/items/{item_id}` tiene un _parámetro de path_`item_id` que debe ser un `int`.
*   El _path_`/items/{item_id}` tiene un _parámetro de query_`q` opcional que es un `str`.

### Documentación interactiva de la API[¶](https://fastapi.tiangolo.com/es/#interactive-api-docs)

Ahora ve a [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Verás la documentación interactiva automática de la API (proporcionada por [Swagger UI](https://github.com/swagger-api/swagger-ui)):

![Image 27: Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Documentación alternativa de la API[¶](https://fastapi.tiangolo.com/es/#alternative-api-docs)

Y ahora, ve a [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

Verás la documentación alternativa automática (proporcionada por [ReDoc](https://github.com/Rebilly/ReDoc)):

![Image 28: ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

Actualización del ejemplo[¶](https://fastapi.tiangolo.com/es/#example-upgrade)
------------------------------------------------------------------------------

Ahora modifica el archivo `main.py` para recibir un body desde un request `PUT`.

Declara el body usando tipos estándar de Python, gracias a Pydantic.

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

El servidor `fastapi dev` debería recargarse automáticamente.

### Actualización de la documentación interactiva de la API[¶](https://fastapi.tiangolo.com/es/#interactive-api-docs-upgrade)

Ahora ve a [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

*   La documentación interactiva de la API se actualizará automáticamente, incluyendo el nuevo body:

![Image 29: Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

*   Haz clic en el botón "Try it out", te permite llenar los parámetros e interactuar directamente con la API:

![Image 30: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

*   Luego haz clic en el botón "Execute", la interfaz de usuario se comunicará con tu API, enviará los parámetros, obtendrá los resultados y los mostrará en la pantalla:

![Image 31: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Actualización de la documentación alternativa de la API[¶](https://fastapi.tiangolo.com/es/#alternative-api-docs-upgrade)

Y ahora, ve a [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

*   La documentación alternativa también reflejará el nuevo parámetro de query y body:

![Image 32: ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### Resumen[¶](https://fastapi.tiangolo.com/es/#recap)

En resumen, declaras **una vez** los tipos de parámetros, body, etc. como parámetros de función.

Lo haces con tipos estándar modernos de Python.

No tienes que aprender una nueva sintaxis, los métodos o clases de un paquete específico, etc.

Solo **Python** estándar.

Por ejemplo, para un `int`:

```
item_id: int
```

o para un modelo `Item` más complejo:

```
item: Item
```

...y con esa única declaración obtienes:

*   Soporte para editores, incluyendo:
    *   Autocompletado.
    *   Chequeo de tipos.

*   Validación de datos:
    *   Errores automáticos y claros cuando los datos son inválidos.
    *   Validación incluso para objetos JSON profundamente anidados.

*   Conversión de datos de entrada: de la red a los datos y tipos de Python. Leyendo desde:
    *   JSON.
    *   Parámetros de path.
    *   Parámetros de query.
    *   Cookies.
    *   Headers.
    *   Forms.
    *   Archivos.

*   Conversión de datos de salida: convirtiendo de datos y tipos de Python a datos de red (como JSON):
    *   Convertir tipos de Python (`str`, `int`, `float`, `bool`, `list`, etc).
    *   Objetos `datetime`.
    *   Objetos `UUID`.
    *   Modelos de base de datos.
    *   ...y muchos más.

*   Documentación interactiva automática de la API, incluyendo 2 interfaces de usuario alternativas:
    *   Swagger UI.
    *   ReDoc.

* * *

Volviendo al ejemplo de código anterior, **FastAPI**:

*   Validará que haya un `item_id` en el path para requests `GET` y `PUT`.
*   Validará que el `item_id` sea del tipo `int` para requests `GET` y `PUT`.
    *   Si no lo es, el cliente verá un error útil y claro.

*   Revisa si hay un parámetro de query opcional llamado `q` (como en `http://127.0.0.1:8000/items/foo?q=somequery`) para requests `GET`.
    *   Como el parámetro `q` está declarado con `= None`, es opcional.
    *   Sin el `None` sería requerido (como lo es el body en el caso con `PUT`).

*   Para requests `PUT` a `/items/{item_id}`, leerá el body como JSON:
    *   Revisa que tiene un atributo requerido `name` que debe ser un `str`.
    *   Revisa que tiene un atributo requerido `price` que debe ser un `float`.
    *   Revisa que tiene un atributo opcional `is_offer`, que debe ser un `bool`, si está presente.
    *   Todo esto también funcionaría para objetos JSON profundamente anidados.

*   Convertirá de y a JSON automáticamente.
*   Documentará todo con OpenAPI, que puede ser usado por:
    *   Sistemas de documentación interactiva.
    *   Sistemas de generación automática de código cliente, para muchos lenguajes.

*   Proporcionará 2 interfaces web de documentación interactiva directamente.

* * *

Solo tocamos los conceptos básicos, pero ya te haces una idea de cómo funciona todo.

Intenta cambiar la línea con:

```
return {"item_name": item.name, "item_id": item_id}
```

...desde:

```
... "item_name": item.name ...
```

...a:

```
... "item_price": item.price ...
```

...y observa cómo tu editor autocompleta los atributos y conoce sus tipos:

![Image 33: editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

Para un ejemplo más completo incluyendo más funcionalidades, ve al [Tutorial - Guía del Usuario](https://fastapi.tiangolo.com/es/tutorial/).

**Alerta de spoilers**: el tutorial - guía del usuario incluye:

*   Declaración de **parámetros** desde otros lugares diferentes como: **headers**, **cookies**, **campos de formulario** y **archivos**.
*   Cómo establecer **restricciones de validación** como `maximum_length` o `regex`.
*   Un sistema de **Inyección de Dependencias** muy poderoso y fácil de usar.
*   Seguridad y autenticación, incluyendo soporte para **OAuth2** con **tokens JWT** y autenticación **HTTP Basic**.
*   Técnicas más avanzadas (pero igualmente fáciles) para declarar **modelos JSON profundamente anidados** (gracias a Pydantic).
*   Integración con **GraphQL** usando [Strawberry](https://strawberry.rocks/) y otros paquetes.
*   Muchas funcionalidades extra (gracias a Starlette) como:
    *   **WebSockets**
    *   pruebas extremadamente fáciles basadas en HTTPX y `pytest`
    *   **CORS**
    *   **Sesiones de Cookies**
    *   ...y más.

### Despliega tu app (opcional)[¶](https://fastapi.tiangolo.com/es/#deploy-your-app-optional)

Opcionalmente puedes desplegar tu app de FastAPI en [FastAPI Cloud](https://fastapicloud.com/), ve y únete a la lista de espera si no lo has hecho. 🚀

Si ya tienes una cuenta de **FastAPI Cloud** (te invitamos desde la lista de espera 😉), puedes desplegar tu aplicación con un solo comando.

Antes de desplegar, asegúrate de haber iniciado sesión:

Luego despliega tu app:

¡Eso es todo! Ahora puedes acceder a tu app en esa URL. ✨

#### Acerca de FastAPI Cloud[¶](https://fastapi.tiangolo.com/es/#about-fastapi-cloud)

**[FastAPI Cloud](https://fastapicloud.com/)** está construido por el mismo autor y equipo detrás de **FastAPI**.

Optimiza el proceso de **construir**, **desplegar** y **acceder** a una API con un esfuerzo mínimo.

Trae la misma **experiencia de desarrollador** de construir apps con FastAPI a **desplegarlas** en la nube. 🎉

FastAPI Cloud es el sponsor principal y proveedor de financiamiento para los proyectos open source _FastAPI and friends_. ✨

#### Despliega en otros proveedores de cloud[¶](https://fastapi.tiangolo.com/es/#deploy-to-other-cloud-providers)

FastAPI es open source y está basado en estándares. Puedes desplegar apps de FastAPI en cualquier proveedor de cloud que elijas.

Sigue las guías de tu proveedor de cloud para desplegar apps de FastAPI con ellos. 🤓

Rendimiento[¶](https://fastapi.tiangolo.com/es/#performance)
------------------------------------------------------------

Benchmarks independientes de TechEmpower muestran aplicaciones **FastAPI** ejecutándose bajo Uvicorn como [uno de los frameworks Python más rápidos disponibles](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7), solo por debajo de Starlette y Uvicorn (usados internamente por FastAPI). (*)

Para entender más sobre esto, ve la sección [Benchmarks](https://fastapi.tiangolo.com/es/benchmarks/).

Dependencias[¶](https://fastapi.tiangolo.com/es/#dependencies)
--------------------------------------------------------------

FastAPI depende de Pydantic y Starlette.

### Dependencias `standard`[¶](https://fastapi.tiangolo.com/es/#standard-dependencies)

Cuando instalas FastAPI con `pip install "fastapi[standard]"` viene con el grupo `standard` de dependencias opcionales:

Usadas por Pydantic:

*   [`email-validator`](https://github.com/JoshData/python-email-validator) - para validación de correos electrónicos.

Usadas por Starlette:

*   [`httpx`](https://www.python-httpx.org/) - Requerido si deseas usar el `TestClient`.
*   [`jinja2`](https://jinja.palletsprojects.com/) - Requerido si deseas usar la configuración de plantilla por defecto.
*   [`python-multipart`](https://github.com/Kludex/python-multipart) - Requerido si deseas soportar form "parsing", con `request.form()`.

Usadas por FastAPI:

*   [`uvicorn`](https://www.uvicorn.dev/) - para el servidor que carga y sirve tu aplicación. Esto incluye `uvicorn[standard]`, que incluye algunas dependencias (por ejemplo, `uvloop`) necesarias para servir con alto rendimiento.
*   `fastapi-cli[standard]` - para proporcionar el comando `fastapi`.
    *   Esto incluye `fastapi-cloud-cli`, que te permite desplegar tu aplicación de FastAPI en [FastAPI Cloud](https://fastapicloud.com/).

### Sin Dependencias `standard`[¶](https://fastapi.tiangolo.com/es/#without-standard-dependencies)

Si no deseas incluir las dependencias opcionales `standard`, puedes instalar con `pip install fastapi` en lugar de `pip install "fastapi[standard]"`.

### Sin `fastapi-cloud-cli`[¶](https://fastapi.tiangolo.com/es/#without-fastapi-cloud-cli)

Si quieres instalar FastAPI con las dependencias standard pero sin `fastapi-cloud-cli`, puedes instalar con `pip install "fastapi[standard-no-fastapi-cloud-cli]"`.

### Dependencias Opcionales Adicionales[¶](https://fastapi.tiangolo.com/es/#additional-optional-dependencies)

Existen algunas dependencias adicionales que podrías querer instalar.

Dependencias opcionales adicionales de Pydantic:

*   [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) - para la gestión de configuraciones.
*   [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) - para tipos extra para ser usados con Pydantic.

Dependencias opcionales adicionales de FastAPI:

*   [`orjson`](https://github.com/ijl/orjson) - Requerido si deseas usar `ORJSONResponse`.
*   [`ujson`](https://github.com/esnme/ultrajson) - Requerido si deseas usar `UJSONResponse`.

Licencia[¶](https://fastapi.tiangolo.com/es/#license)
-----------------------------------------------------

Este proyecto tiene licencia bajo los términos de la licencia MIT.
