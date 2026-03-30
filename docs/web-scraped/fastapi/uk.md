# Source: https://fastapi.tiangolo.com/uk/

Title: FastAPI

URL Source: https://fastapi.tiangolo.com/uk/

Markdown Content:
🌐 Переклад ШІ та людьми
Цей переклад виконано ШІ під керівництвом людей. 🤝

Можливі помилки через неправильне розуміння початкового змісту або неприродні формулювання тощо. 🤖

Ви можете покращити цей переклад, [допомігши нам краще спрямовувати AI LLM](https://fastapi.tiangolo.com/uk/contributing/#translations).

[Англійська версія](https://fastapi.tiangolo.com/)

[![Image 1: FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com/uk)

_Фреймворк FastAPI - це висока продуктивність, легко вивчати, швидко писати код, готовий до продакшину_

[![Image 2: Test](https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master)](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)[![Image 3: Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi)[![Image 4: Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi)[![Image 5: Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)](https://pypi.org/project/fastapi)

* * *

**Документація**: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com/uk)

**Вихідний код**: [https://github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)

* * *

FastAPI - це сучасний, швидкий (високопродуктивний) вебфреймворк для створення API за допомогою Python, що базується на стандартних підказках типів Python.

Ключові особливості:

*   **Швидкий**: дуже висока продуктивність, на рівні з **NodeJS** та **Go** (завдяки Starlette та Pydantic). [Один із найшвидших Python-фреймворків](https://fastapi.tiangolo.com/uk/#performance).
*   **Швидке написання коду**: пришвидшує розробку функціоналу приблизно на 200%–300%. *
*   **Менше помилок**: зменшує приблизно на 40% кількість помилок, спричинених людиною (розробником). *
*   **Інтуїтивний**: чудова підтримка редакторами коду. Автодоповнення всюди. Менше часу на налагодження.
*   **Простий**: спроєктований так, щоб бути простим у використанні та вивченні. Менше часу на читання документації.
*   **Короткий**: мінімізує дублювання коду. Кілька можливостей з кожного оголошення параметра. Менше помилок.
*   **Надійний**: ви отримуєте код, готовий до продакшину. З автоматичною інтерактивною документацією.
*   **Заснований на стандартах**: базується на (і повністю сумісний з) відкритими стандартами для API: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (раніше відомий як Swagger) та [JSON Schema](https://json-schema.org/).

* оцінка на основі тестів, проведених внутрішньою командою розробників, що створює продакшн-застосунки.

[![Image 6](https://fastapi.tiangolo.com/img/sponsors/fastapicloud.png)](https://fastapicloud.com/ "FastAPI Cloud. By the same team behind FastAPI. You code. We Cloud.")

### Золоті та срібні спонсори[¶](https://fastapi.tiangolo.com/uk/#gold-and-silver-sponsors)

[![Image 7](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io/?ref=fastapi "BlockBee Cryptocurrency Payment Gateway")[![Image 8](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI files")[![Image 9](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge "Auth, user management and more for your B2B product")[![Image 10](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-gh "Zuplo: Deploy, Secure, Document, and Monetize your FastAPI")[![Image 11](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com/?utm_source=fastapi "liblab - Generate SDKs from FastAPI")[![Image 12](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy & scale any full-stack web app on Render. Focus on building apps, not infra.")[![Image 13](https://fastapi.tiangolo.com/img/sponsors/coderabbit.png)](https://www.coderabbit.ai/?utm_source=fastapi&utm_medium=badge&utm_campaign=fastapi "Cut Code Review Time & Bugs in Half with CodeRabbit")[![Image 14](https://fastapi.tiangolo.com/img/sponsors/subtotal.svg)](https://subtotal.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=open-source "The Gold Standard in Retail Account Linking")[![Image 15](https://fastapi.tiangolo.com/img/sponsors/railway.png)](https://docs.railway.com/guides/fastapi?utm_medium=integration&utm_source=docs&utm_campaign=fastapi "Deploy enterprise applications at startup speed")[![Image 16](https://fastapi.tiangolo.com/img/sponsors/serpapi.png)](https://serpapi.com/?utm_source=fastapi_website "SerpApi: Web Search API")[![Image 17](https://fastapi.tiangolo.com/img/sponsors/greptile.png)](https://www.greptile.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=fastapi_sponsor_page "Greptile: The AI Code Reviewer")[![Image 18](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/?utm_source=fastapi&utm_medium=sponsor&utm_content=display "Pay as you go for market data")[![Image 19](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com/editor?utm_source=fastapi+repo&utm_medium=github+sponsorship "SDKs for your API | Speakeasy")[![Image 20](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/ "Svix - Webhooks as a service")[![Image 21](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral "Stainless | Generate best-in-class SDKs")[![Image 22](https://fastapi.tiangolo.com/img/sponsors/permit.png)](https://www.permit.io/blog/implement-authorization-in-fastapi?utm_source=github&utm_medium=referral&utm_campaign=fastapi "Fine-Grained Authorization for FastAPI")[![Image 23](https://fastapi.tiangolo.com/img/sponsors/interviewpal.png)](https://www.interviewpal.com/?utm_source=fastapi&utm_medium=open-source&utm_campaign=dev-hiring "InterviewPal - AI Interview Coach for Engineers and Devs")[![Image 24](https://fastapi.tiangolo.com/img/sponsors/dribia.png)](https://dribia.com/en/ "Dribia - Data Science within your reach")

[Інші спонсори](https://fastapi.tiangolo.com/uk/fastapi-people/#sponsors)

Враження[¶](https://fastapi.tiangolo.com/uk/#opinions)
------------------------------------------------------

"_[...] I'm using **FastAPI** a ton these days. [...] I'm actually planning to use it for all of my team's **ML services at Microsoft**. Some of them are getting integrated into the core **Windows** product and some **Office** products._"

Kabir Khan - **Microsoft**[(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

"_We adopted the **FastAPI** library to spawn a **REST** server that can be queried to obtain **predictions**. [for Ludwig]_"

Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber**[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

"_**Netflix** is pleased to announce the open-source release of our **crisis management** orchestration framework: **Dispatch**! [built with **FastAPI**]_"

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

"_I’m over the moon excited about **FastAPI**. It’s so fun!_"

* * *

"_Honestly, what you've built looks super solid and polished. In many ways, it's what I wanted **Hug** to be - it's really inspiring to see someone build that._"

Timothy Crosley - **[Hug](https://github.com/hugapi/hug) creator**[(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

"_If you're looking to learn one **modern framework** for building REST APIs, check out **FastAPI** [...] It's fast, easy to use and easy to learn [...]_"

"_We've switched over to **FastAPI** for our **APIs** [...] I think you'll like it [...]_"

* * *

"_If anyone is looking to build a production Python API, I would highly recommend **FastAPI**. It is **beautifully designed**, **simple to use** and **highly scalable**, it has become a **key component** in our API first development strategy and is driving many automations and services such as our Virtual TAC Engineer._"

Deon Pillsbury - **Cisco**[(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/)

* * *

Міні-документальний фільм про FastAPI[¶](https://fastapi.tiangolo.com/uk/#fastapi-mini-documentary)
---------------------------------------------------------------------------------------------------

Наприкінці 2025 року вийшов [міні-документальний фільм про FastAPI](https://www.youtube.com/watch?v=mpR8ngthqiE), ви можете переглянути його онлайн:

[![Image 25: FastAPI Mini Documentary](https://fastapi.tiangolo.com/img/fastapi-documentary.jpg)](https://www.youtube.com/watch?v=mpR8ngthqiE)

**Typer**, FastAPI для CLI[¶](https://fastapi.tiangolo.com/uk/#typer-the-fastapi-of-clis)
-----------------------------------------------------------------------------------------

[![Image 26](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com/)

Якщо ви створюєте застосунок CLI для використання в терміналі замість веб-API, зверніть увагу на [**Typer**](https://typer.tiangolo.com/).

**Typer** - молодший брат FastAPI. І його задумано як **FastAPI для CLI**. ⌨️ 🚀

Вимоги[¶](https://fastapi.tiangolo.com/uk/#requirements)
--------------------------------------------------------

FastAPI стоїть на плечах гігантів:

*   [Starlette](https://www.starlette.dev/) для вебчастини.
*   [Pydantic](https://docs.pydantic.dev/) для частини даних.

Встановлення[¶](https://fastapi.tiangolo.com/uk/#installation)
--------------------------------------------------------------

Створіть і активуйте [віртуальне середовище](https://fastapi.tiangolo.com/uk/virtual-environments/), а потім встановіть FastAPI:

**Примітка**: переконайтеся, що ви взяли `"fastapi[standard]"` у лапки, щоб це працювало в усіх терміналах.

Приклад[¶](https://fastapi.tiangolo.com/uk/#example)
----------------------------------------------------

### Створіть[¶](https://fastapi.tiangolo.com/uk/#create-it)

Створіть файл `main.py` з:

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

Або використайте `async def`...
Якщо ваш код використовує `async` / `await`, скористайтеся `async def`:

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

**Примітка**:

Якщо ви не знаєте, перегляньте розділ _"In a hurry?"_ про [`async` та `await` у документації](https://fastapi.tiangolo.com/uk/async/#in-a-hurry).

### Запустіть[¶](https://fastapi.tiangolo.com/uk/#run-it)

Запустіть сервер за допомогою:

Про команду `fastapi dev main.py`...
Команда `fastapi dev` читає ваш файл `main.py`, знаходить у ньому застосунок **FastAPI** і запускає сервер за допомогою [Uvicorn](https://www.uvicorn.dev/).

За замовчуванням `fastapi dev` запускається з авто-перезавантаженням для локальної розробки.

Докладніше читайте в [документації FastAPI CLI](https://fastapi.tiangolo.com/uk/fastapi-cli/).

### Перевірте[¶](https://fastapi.tiangolo.com/uk/#check-it)

Відкрийте браузер і перейдіть на [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery).

Ви побачите JSON-відповідь:

```
{"item_id": 5, "q": "somequery"}
```

Ви вже створили API, який:

*   Отримує HTTP-запити за _шляхами_`/` та `/items/{item_id}`.
*   Обидва _шляхи_ приймають `GET`_операції_ (також відомі як HTTP _методи_).
*   _Шлях_`/items/{item_id}` містить _параметр шляху_`item_id`, який має бути типу `int`.
*   _Шлях_`/items/{item_id}` містить необовʼязковий `str`_параметр запиту_`q`.

### Інтерактивна документація API[¶](https://fastapi.tiangolo.com/uk/#interactive-api-docs)

Тепер перейдіть на [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Ви побачите автоматичну інтерактивну документацію API (надану [Swagger UI](https://github.com/swagger-api/swagger-ui)):

![Image 27: Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Альтернативна документація API[¶](https://fastapi.tiangolo.com/uk/#alternative-api-docs)

А тепер перейдіть на [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

Ви побачите альтернативну автоматичну документацію (надану [ReDoc](https://github.com/Rebilly/ReDoc)):

![Image 28: ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

Приклад оновлення[¶](https://fastapi.tiangolo.com/uk/#example-upgrade)
----------------------------------------------------------------------

Тепер змініть файл `main.py`, щоб отримувати тіло `PUT`-запиту.

Оголосіть тіло, використовуючи стандартні типи Python, завдяки Pydantic.

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

Сервер `fastapi dev` має автоматично перезавантажитися.

### Оновлення інтерактивної документації API[¶](https://fastapi.tiangolo.com/uk/#interactive-api-docs-upgrade)

Тепер перейдіть на [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

*   Інтерактивна документація API буде автоматично оновлена, включно з новим тілом:

![Image 29: Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

*   Натисніть кнопку "Try it out", вона дозволяє заповнити параметри та безпосередньо взаємодіяти з API:

![Image 30: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

*   Потім натисніть кнопку "Execute", інтерфейс користувача зв'яжеться з вашим API, надішле параметри, отримає результати та покаже їх на екрані:

![Image 31: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Оновлення альтернативної документації API[¶](https://fastapi.tiangolo.com/uk/#alternative-api-docs-upgrade)

А тепер перейдіть на [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

*   Альтернативна документація також відобразить новий параметр запиту та тіло:

![Image 32: ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### Підсумки[¶](https://fastapi.tiangolo.com/uk/#recap)

Отже, ви оголошуєте **один раз** типи параметрів, тіла тощо як параметри функції.

Ви робите це за допомогою стандартних сучасних типів Python.

Вам не потрібно вивчати новий синтаксис, методи чи класи конкретної бібліотеки тощо.

Лише стандартний **Python**.

Наприклад, для `int`:

```
item_id: int
```

або для складнішої моделі `Item`:

```
item: Item
```

...і з цим єдиним оголошенням ви отримуєте:

*   Підтримку редактора, включно з:
    *   Автодоповненням.
    *   Перевіркою типів.

*   Валідацію даних:
    *   Автоматичні та зрозумілі помилки, коли дані некоректні.
    *   Валідацію навіть для глибоко вкладених JSON-обʼєктів.

*   Перетворення вхідних даних: з мережі до даних і типів Python. Читання з:
    *   JSON.
    *   Параметрів шляху.
    *   Параметрів запиту.
    *   Cookies.
    *   Headers.
    *   Forms.
    *   Files.

*   Перетворення вихідних даних: перетворення з даних і типів Python у мережеві дані (як JSON):
    *   Перетворення типів Python (`str`, `int`, `float`, `bool`, `list`, тощо).
    *   Обʼєктів `datetime`.
    *   Обʼєктів `UUID`.
    *   Моделей бази даних.
    *   ...та багато іншого.

*   Автоматичну інтерактивну документацію API, включно з 2 альтернативними інтерфейсами користувача:
    *   Swagger UI.
    *   ReDoc.

* * *

Повертаючись до попереднього прикладу коду, **FastAPI**:

*   Перевірить, що `item_id` є у шляху для `GET` та `PUT`-запитів.
*   Перевірить, що `item_id` має тип `int` для `GET` та `PUT`-запитів.
    *   Якщо це не так, клієнт побачить корисну, зрозумілу помилку.

*   Перевірить, чи є необов'язковий параметр запиту з назвою `q` (як у `http://127.0.0.1:8000/items/foo?q=somequery`) для `GET`-запитів.
    *   Оскільки параметр `q` оголошено як `= None`, він необов'язковий.
    *   Без `None` він був би обов'язковим (як і тіло у випадку з `PUT`).

*   Для `PUT`-запитів до `/items/{item_id}` прочитає тіло як JSON:
    *   Перевірить, що є обовʼязковий атрибут `name`, який має бути типу `str`.
    *   Перевірить, що є обовʼязковий атрибут `price`, який має бути типу `float`.
    *   Перевірить, що є необовʼязковий атрибут `is_offer`, який має бути типу `bool`, якщо він присутній.
    *   Усе це також працюватиме для глибоко вкладених JSON-обʼєктів.

*   Автоматично перетворюватиме з та в JSON.
*   Документуватиме все за допомогою OpenAPI, який може бути використано в:
    *   Інтерактивних системах документації.
    *   Системах автоматичної генерації клієнтського коду для багатьох мов.

*   Надаватиме безпосередньо 2 вебінтерфейси інтерактивної документації.

* * *

Ми лише трішки доторкнулися до поверхні, але ви вже маєте уявлення про те, як усе працює.

Спробуйте змінити рядок:

```
return {"item_name": item.name, "item_id": item_id}
```

...із:

```
... "item_name": item.name ...
```

...на:

```
... "item_price": item.price ...
```

...і побачите, як ваш редактор автоматично доповнюватиме атрибути та знатиме їхні типи:

![Image 33: editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

Для більш повного прикладу, що включає більше можливостей, перегляньте [Навчальний посібник - Посібник користувача](https://fastapi.tiangolo.com/uk/tutorial/).

**Попередження про спойлер**: навчальний посібник - посібник користувача містить:

*   Оголошення **параметрів** з інших різних місць, як-от: **headers**, **cookies**, **form fields** та **files**.
*   Як встановлювати **обмеження валідації** як `maximum_length` або `regex`.
*   Дуже потужну і просту у використанні систему **Впровадження залежностей**.
*   Безпеку та автентифікацію, включно з підтримкою **OAuth2** з **JWT tokens** та **HTTP Basic** auth.
*   Досконаліші (але однаково прості) техніки для оголошення **глибоко вкладених моделей JSON** (завдяки Pydantic).
*   Інтеграцію **GraphQL** з [Strawberry](https://strawberry.rocks/) та іншими бібліотеками.
*   Багато додаткових можливостей (завдяки Starlette) як-от:
    *   **WebSockets**
    *   надзвичайно прості тести на основі HTTPX та `pytest`
    *   **CORS**
    *   **Cookie Sessions**
    *   ...та більше.

### Розгортання застосунку (необовʼязково)[¶](https://fastapi.tiangolo.com/uk/#deploy-your-app-optional)

За бажання ви можете розгорнути ваш застосунок FastAPI у [FastAPI Cloud](https://fastapicloud.com/), перейдіть і приєднайтеся до списку очікування, якщо ви ще цього не зробили. 🚀

Якщо у вас вже є обліковий запис **FastAPI Cloud** (ми запросили вас зі списку очікування 😉), ви можете розгорнути ваш застосунок однією командою.

Перед розгортанням переконайтеся, що ви ввійшли в систему:

Потім розгорніть ваш застосунок:

Ось і все! Тепер ви можете отримати доступ до вашого застосунку за цією URL-адресою. ✨

#### Про FastAPI Cloud[¶](https://fastapi.tiangolo.com/uk/#about-fastapi-cloud)

**[FastAPI Cloud](https://fastapicloud.com/)** створено тим самим автором і командою, що стоять за **FastAPI**.

Він спрощує процес **створення**, **розгортання** та **доступу** до API з мінімальними зусиллями.

Він забезпечує той самий **developer experience** створення застосунків на FastAPI під час їх **розгортання** у хмарі. 🎉

FastAPI Cloud - основний спонсор і джерело фінансування open source проєктів _FastAPI and friends_. ✨

#### Розгортання в інших хмарних провайдерів[¶](https://fastapi.tiangolo.com/uk/#deploy-to-other-cloud-providers)

FastAPI - open source проект і базується на стандартах. Ви можете розгортати застосунки FastAPI в будь-якому хмарному провайдері, який ви оберете.

Дотримуйтеся інструкцій вашого хмарного провайдера, щоб розгорнути застосунки FastAPI у нього. 🤓

Продуктивність[¶](https://fastapi.tiangolo.com/uk/#performance)
---------------------------------------------------------------

Незалежні тести TechEmpower показують застосунки **FastAPI**, які працюють під керуванням Uvicorn, як [одні з найшвидших доступних Python-фреймворків](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7), поступаючись лише Starlette та Uvicorn (які внутрішньо використовуються в FastAPI). (*)

Щоб дізнатися більше, перегляньте розділ [Benchmarks](https://fastapi.tiangolo.com/uk/benchmarks/).

Залежності[¶](https://fastapi.tiangolo.com/uk/#dependencies)
------------------------------------------------------------

FastAPI залежить від Pydantic і Starlette.

### Залежності `standard`[¶](https://fastapi.tiangolo.com/uk/#standard-dependencies)

Коли ви встановлюєте FastAPI за допомогою `pip install "fastapi[standard]"`, ви отримуєте групу необовʼязкових залежностей `standard`:

Використовується Pydantic:

*   [`email-validator`](https://github.com/JoshData/python-email-validator) - для валідації електронної пошти.

Використовується Starlette:

*   [`httpx`](https://www.python-httpx.org/) - потрібно, якщо ви хочете використовувати `TestClient`.
*   [`jinja2`](https://jinja.palletsprojects.com/) - потрібно, якщо ви хочете використовувати конфігурацію шаблонів за замовчуванням.
*   [`python-multipart`](https://github.com/Kludex/python-multipart) - потрібно, якщо ви хочете підтримувати форми з «парсингом» через `request.form()`.

Використовується FastAPI:

*   [`uvicorn`](https://www.uvicorn.dev/) - для сервера, який завантажує та обслуговує ваш застосунок. Це включає `uvicorn[standard]`, до якого входять деякі залежності (наприклад, `uvloop`), потрібні для високопродуктивної роботи сервера.
*   `fastapi-cli[standard]` - щоб надати команду `fastapi`.
    *   Це включає `fastapi-cloud-cli`, який дозволяє розгортати ваш застосунок FastAPI у [FastAPI Cloud](https://fastapicloud.com/).

### Без залежностей `standard`[¶](https://fastapi.tiangolo.com/uk/#without-standard-dependencies)

Якщо ви не хочете включати необовʼязкові залежності `standard`, ви можете встановити через `pip install fastapi` замість `pip install "fastapi[standard]"`.

### Без `fastapi-cloud-cli`[¶](https://fastapi.tiangolo.com/uk/#without-fastapi-cloud-cli)

Якщо ви хочете встановити FastAPI зі стандартними залежностями, але без `fastapi-cloud-cli`, ви можете встановити через `pip install "fastapi[standard-no-fastapi-cloud-cli]"`.

### Додаткові необовʼязкові залежності[¶](https://fastapi.tiangolo.com/uk/#additional-optional-dependencies)

Є ще деякі додаткові залежності, які ви можете захотіти встановити.

Додаткові необовʼязкові залежності Pydantic:

*   [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) - для керування налаштуваннями.
*   [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) - для додаткових типів, що можуть бути використані з Pydantic.

Додаткові необовʼязкові залежності FastAPI:

*   [`orjson`](https://github.com/ijl/orjson) - потрібно, якщо ви хочете використовувати `ORJSONResponse`.
*   [`ujson`](https://github.com/esnme/ultrajson) - потрібно, якщо ви хочете використовувати `UJSONResponse`.

Ліцензія[¶](https://fastapi.tiangolo.com/uk/#license)
-----------------------------------------------------

Цей проєкт ліцензовано згідно з умовами ліцензії MIT.
