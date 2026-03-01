# Source: https://fastapi.tiangolo.com/zh/

Title: FastAPI

URL Source: https://fastapi.tiangolo.com/zh/

Markdown Content:
🌐 由 AI 与人类协作翻译
本翻译由人类引导的 AI 生成。🤝

可能存在误解原意或不够自然等问题。🤖

你可以通过[帮助我们更好地引导 AI LLM](https://fastapi.tiangolo.com/zh/contributing/#translations)来改进此翻译。

[英文版本](https://fastapi.tiangolo.com/)

[![Image 1: FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com/zh)

_FastAPI 框架，高性能，易于学习，高效编码，生产可用_

[![Image 2: Test](https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master)](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster)[![Image 3: Coverage](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi)[![Image 4: Package version](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi)[![Image 5: Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058)](https://pypi.org/project/fastapi)

* * *

**文档**： [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com/zh)

**源码**： [https://github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)

* * *

FastAPI 是一个用于构建 API 的现代、快速（高性能）的 Web 框架，使用 Python 并基于标准的 Python 类型提示。

关键特性：

*   **快速**：极高性能，可与 **NodeJS** 和 **Go** 并肩（归功于 Starlette 和 Pydantic）。[最快的 Python 框架之一](https://fastapi.tiangolo.com/zh/#performance)。
*   **高效编码**：功能开发速度提升约 200% ～ 300%。*
*   **更少 bug**：人为（开发者）错误减少约 40%。*
*   **直观**：极佳的编辑器支持。处处皆可 自动补全。更少的调试时间。
*   **易用**：为易用和易学而设计。更少的文档阅读时间。
*   **简短**：最小化代码重复。一次参数声明即可获得多种功能。更少的 bug。
*   **健壮**：生产可用级代码。并带有自动生成的交互式文档。
*   **标准化**：基于（并完全兼容）API 的开放标准：[OpenAPI](https://github.com/OAI/OpenAPI-Specification)（以前称为 Swagger）和 [JSON Schema](https://json-schema.org/)。

* 基于某内部开发团队在构建生产应用时的测试估算。

[![Image 6](https://fastapi.tiangolo.com/img/sponsors/fastapicloud.png)](https://fastapicloud.com/ "FastAPI Cloud. By the same team behind FastAPI. You code. We Cloud.")

### 金牌和银牌赞助商[¶](https://fastapi.tiangolo.com/zh/#gold-and-silver-sponsors "Permanent link")

[![Image 7](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io/?ref=fastapi "BlockBee Cryptocurrency Payment Gateway")[![Image 8](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI files")[![Image 9](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge "Auth, user management and more for your B2B product")[![Image 10](https://fastapi.tiangolo.com/img/sponsors/zuplo.png)](https://zuplo.link/fastapi-gh "Zuplo: Deploy, Secure, Document, and Monetize your FastAPI")[![Image 11](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com/?utm_source=fastapi "liblab - Generate SDKs from FastAPI")[![Image 12](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy & scale any full-stack web app on Render. Focus on building apps, not infra.")[![Image 13](https://fastapi.tiangolo.com/img/sponsors/coderabbit.png)](https://www.coderabbit.ai/?utm_source=fastapi&utm_medium=badge&utm_campaign=fastapi "Cut Code Review Time & Bugs in Half with CodeRabbit")[![Image 14](https://fastapi.tiangolo.com/img/sponsors/subtotal.svg)](https://subtotal.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=open-source "The Gold Standard in Retail Account Linking")[![Image 15](https://fastapi.tiangolo.com/img/sponsors/railway.png)](https://docs.railway.com/guides/fastapi?utm_medium=integration&utm_source=docs&utm_campaign=fastapi "Deploy enterprise applications at startup speed")[![Image 16](https://fastapi.tiangolo.com/img/sponsors/serpapi.png)](https://serpapi.com/?utm_source=fastapi_website "SerpApi: Web Search API")[![Image 17](https://fastapi.tiangolo.com/img/sponsors/greptile.png)](https://www.greptile.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=fastapi_sponsor_page "Greptile: The AI Code Reviewer")[![Image 18](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/?utm_source=fastapi&utm_medium=sponsor&utm_content=display "Pay as you go for market data")[![Image 19](https://fastapi.tiangolo.com/img/sponsors/speakeasy.png)](https://speakeasy.com/editor?utm_source=fastapi+repo&utm_medium=github+sponsorship "SDKs for your API | Speakeasy")[![Image 20](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/ "Svix - Webhooks as a service")[![Image 21](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral "Stainless | Generate best-in-class SDKs")[![Image 22](https://fastapi.tiangolo.com/img/sponsors/permit.png)](https://www.permit.io/blog/implement-authorization-in-fastapi?utm_source=github&utm_medium=referral&utm_campaign=fastapi "Fine-Grained Authorization for FastAPI")[![Image 23](https://fastapi.tiangolo.com/img/sponsors/interviewpal.png)](https://www.interviewpal.com/?utm_source=fastapi&utm_medium=open-source&utm_campaign=dev-hiring "InterviewPal - AI Interview Coach for Engineers and Devs")[![Image 24](https://fastapi.tiangolo.com/img/sponsors/dribia.png)](https://dribia.com/en/ "Dribia - Data Science within your reach")

[其他赞助商](https://fastapi.tiangolo.com/zh/fastapi-people/#sponsors)

评价[¶](https://fastapi.tiangolo.com/zh/#opinions "Permanent link")
-----------------------------------------------------------------

「_[...] 最近我大量使用 **FastAPI**。[...] 我实际上计划把它用于我团队在 **微软** 的所有 **机器学习服务**。其中一些正在集成进核心 **Windows** 产品以及一些 **Office** 产品。_」

Kabir Khan - **Microsoft**[(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

「_我们采用 **FastAPI** 来构建可查询以获取**预测结果**的 **REST** 服务器。[用于 Ludwig]_」

Piero Molino，Yaroslav Dudin，Sai Sumanth Miryala - **Uber**[(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

「_**Netflix** 很高兴宣布开源我们的**危机管理**编排框架：**Dispatch**！[使用 **FastAPI** 构建]_」

Kevin Glisson，Marc Vilanova，Forest Monsen - **Netflix**[(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

「_我对 **FastAPI** 兴奋到飞起。它太有趣了！_」

* * *

「_老实说，你构建的东西非常稳健而且打磨得很好。从很多方面看，这就是我想让 **Hug** 成为的样子 —— 看到有人把它做出来真的很鼓舞人心。_」

* * *

「_如果你想学一个用于构建 REST API 的**现代框架**，看看 **FastAPI** [...] 它快速、易用且易学 [...]_」

「_我们已经把我们的 **API** 切换到 **FastAPI** [...] 我想你会喜欢它 [...]_」

* * *

「_如果有人正在构建生产级的 Python API，我强烈推荐 **FastAPI**。它**设计优雅**、**使用简单**且**高度可扩展**，已经成为我们 API 优先开发战略中的**关键组件**，并驱动了许多自动化和服务，比如我们的 Virtual TAC Engineer。_」

Deon Pillsbury - **Cisco**[(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/)

* * *

FastAPI 迷你纪录片[¶](https://fastapi.tiangolo.com/zh/#fastapi-mini-documentary "Permanent link")
--------------------------------------------------------------------------------------------

在 2025 年末发布了一部[FastAPI 迷你纪录片](https://www.youtube.com/watch?v=mpR8ngthqiE)，你可以在线观看：

[![Image 25: FastAPI Mini Documentary](https://fastapi.tiangolo.com/img/fastapi-documentary.jpg)](https://www.youtube.com/watch?v=mpR8ngthqiE)

**Typer**，命令行中的 FastAPI[¶](https://fastapi.tiangolo.com/zh/#typer-the-fastapi-of-clis "Permanent link")
-------------------------------------------------------------------------------------------------------

[![Image 26](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com/)

如果你要开发一个用于终端的 命令行 应用而不是 Web API，看看 [**Typer**](https://typer.tiangolo.com/)。

**Typer** 是 FastAPI 的小同胞。它的目标是成为**命令行中的 FastAPI**。⌨️ 🚀

依赖[¶](https://fastapi.tiangolo.com/zh/#requirements "Permanent link")
---------------------------------------------------------------------

FastAPI 站在巨人的肩膀之上：

*   [Starlette](https://www.starlette.dev/) 负责 Web 部分。
*   [Pydantic](https://docs.pydantic.dev/) 负责数据部分。

安装[¶](https://fastapi.tiangolo.com/zh/#installation "Permanent link")
---------------------------------------------------------------------

创建并激活一个[虚拟环境](https://fastapi.tiangolo.com/zh/virtual-environments/)，然后安装 FastAPI：

```
$ pip install "fastapi[standard]"

---> 100%
```

**Note**: 请确保把 `"fastapi[standard]"` 用引号包起来，以保证在所有终端中都能正常工作。

示例[¶](https://fastapi.tiangolo.com/zh/#example "Permanent link")
----------------------------------------------------------------

### 创建[¶](https://fastapi.tiangolo.com/zh/#create-it "Permanent link")

创建文件 `main.py`，内容如下：

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

或者使用 `async def`...
如果你的代码里会用到 `async` / `await`，请使用 `async def`：

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

**Note**:

如果你不确定，请查看文档中 _"In a hurry?"_ 章节的[`async` 和 `await`](https://fastapi.tiangolo.com/zh/async/#in-a-hurry)部分。

### 运行[¶](https://fastapi.tiangolo.com/zh/#run-it "Permanent link")

用下面的命令运行服务器：

```
$ fastapi dev main.py

 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

关于命令 `fastapi dev main.py`...
`fastapi dev` 命令会读取你的 `main.py` 文件，检测其中的 **FastAPI** 应用，并使用 [Uvicorn](https://www.uvicorn.dev/) 启动服务器。

默认情况下，`fastapi dev` 会在本地开发时启用自动重载。

你可以在 [FastAPI CLI 文档](https://fastapi.tiangolo.com/zh/fastapi-cli/)中了解更多。

### 检查[¶](https://fastapi.tiangolo.com/zh/#check-it "Permanent link")

用浏览器打开 [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery)。

你会看到如下 JSON 响应：

```
{"item_id": 5, "q": "somequery"}
```

你已经创建了一个 API，它可以：

*   在路径 `/` 和 `/items/{item_id}` 接收 HTTP 请求。
*   以上两个路径都接受 `GET`_操作_（也称为 HTTP _方法_）。
*   路径 `/items/{item_id}` 有一个应为 `int` 的 _路径参数_`item_id`。
*   路径 `/items/{item_id}` 有一个可选的 `str` 类型 _查询参数_`q`。

### 交互式 API 文档[¶](https://fastapi.tiangolo.com/zh/#interactive-api-docs "Permanent link")

现在访问 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)。

你会看到自动生成的交互式 API 文档（由 [Swagger UI](https://github.com/swagger-api/swagger-ui) 提供）：

![Image 27: Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### 可选的 API 文档[¶](https://fastapi.tiangolo.com/zh/#alternative-api-docs "Permanent link")

然后访问 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)。

你会看到另一个自动生成的文档（由 [ReDoc](https://github.com/Rebilly/ReDoc) 提供）：

![Image 28: ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

示例升级[¶](https://fastapi.tiangolo.com/zh/#example-upgrade "Permanent link")
--------------------------------------------------------------------------

现在修改 `main.py` 文件来接收来自 `PUT` 请求的请求体。

借助 Pydantic，使用标准的 Python 类型来声明请求体。

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

`fastapi dev` 服务器会自动重载。

### 交互式 API 文档升级[¶](https://fastapi.tiangolo.com/zh/#interactive-api-docs-upgrade "Permanent link")

现在访问 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)。

*   交互式 API 文档会自动更新，并包含新的请求体：

![Image 29: Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

*   点击「Try it out」按钮，它允许你填写参数并直接与 API 交互：

![Image 30: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

*   然后点击「Execute」按钮，界面会与你的 API 通信、发送参数、获取结果并在屏幕上展示：

![Image 31: Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### 可选文档升级[¶](https://fastapi.tiangolo.com/zh/#alternative-api-docs-upgrade "Permanent link")

再访问 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)。

*   可选文档同样会体现新的查询参数和请求体：

![Image 32: ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### 总结[¶](https://fastapi.tiangolo.com/zh/#recap "Permanent link")

总之，你只需要把参数、请求体等的类型作为函数参数**声明一次**。

这些都使用标准的现代 Python 类型即可。

你不需要学习新的语法、某个特定库的方法或类等。

只需要标准的 **Python**。

例如，一个 `int`：

```
item_id: int
```

或者更复杂的 `Item` 模型：

```
item: Item
```

……通过一次声明，你将获得：

*   编辑器支持，包括：
    *   自动补全。
    *   类型检查。

*   数据校验：
    *   当数据无效时自动生成清晰的错误信息。
    *   即便是多层嵌套的 JSON 对象也会进行校验。

*   转换 输入数据：从网络读取到 Python 数据和类型。读取来源：
    *   JSON。
    *   路径参数。
    *   查询参数。
    *   Cookies。
    *   Headers。
    *   Forms。
    *   Files。

*   转换 输出数据：从 Python 数据和类型转换为网络数据（JSON）：
    *   转换 Python 类型（`str`、`int`、`float`、`bool`、`list` 等）。
    *   `datetime` 对象。
    *   `UUID` 对象。
    *   数据库模型。
    *   ……以及更多。

*   自动生成的交互式 API 文档，包括两种可选的用户界面：
    *   Swagger UI。
    *   ReDoc。

* * *

回到之前的代码示例，**FastAPI** 将会：

*   校验 `GET` 和 `PUT` 请求的路径中是否包含 `item_id`。
*   校验 `GET` 和 `PUT` 请求中的 `item_id` 是否为 `int` 类型。
    *   如果不是，客户端会看到清晰有用的错误信息。

*   对于 `GET` 请求，检查是否存在名为 `q` 的可选查询参数（如 `http://127.0.0.1:8000/items/foo?q=somequery`）。
    *   因为参数 `q` 被声明为 `= None`，所以它是可选的。
    *   如果没有 `None`，它就是必需的（就像 `PUT` 情况下的请求体）。

*   对于发送到 `/items/{item_id}` 的 `PUT` 请求，把请求体作为 JSON 读取：
    *   检查是否存在必需属性 `name`，且为 `str`。
    *   检查是否存在必需属性 `price`，且为 `float`。
    *   检查是否存在可选属性 `is_offer`，如果存在则应为 `bool`。
    *   对于多层嵌套的 JSON 对象，同样适用。

*   自动完成 JSON 的读取与输出转换。
*   使用 OpenAPI 记录所有内容，可用于：
    *   交互式文档系统。
    *   多语言的客户端代码自动生成系统。

*   直接提供 2 种交互式文档 Web 界面。

* * *

我们只是浅尝辄止，但你已经大致了解其工作方式了。

尝试把这一行：

```
return {"item_name": item.name, "item_id": item_id}
```

……从：

```
... "item_name": item.name ...
```

……改为：

```
... "item_price": item.price ...
```

……看看你的编辑器如何自动补全属性并知道它们的类型：

![Image 33: editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

更多包含更多特性的完整示例，请参阅 [教程 - 用户指南](https://fastapi.tiangolo.com/zh/tutorial/)。

**剧透警告**：教程 - 用户指南包括：

*   来自不同位置的**参数**声明：**headers**、**cookies**、**form 字段**和**文件**。
*   如何设置**校验约束**，如 `maximum_length` 或 `regex`。
*   功能强大且易用的 **依赖注入** 系统。
*   安全与认证，包括对 **OAuth2**、**JWT tokens** 和 **HTTP Basic** 认证的支持。
*   更高级（但同样简单）的 **多层嵌套 JSON 模型** 声明技巧（得益于 Pydantic）。
*   通过 [Strawberry](https://strawberry.rocks/) 等库进行 **GraphQL** 集成。
*   许多额外特性（归功于 Starlette），例如：
    *   **WebSockets**
    *   基于 HTTPX 和 `pytest` 的极其简单的测试
    *   **CORS**
    *   **Cookie Sessions**
    *   ……以及更多。

### 部署你的应用（可选）[¶](https://fastapi.tiangolo.com/zh/#deploy-your-app-optional "Permanent link")

你可以选择把 FastAPI 应用部署到 [FastAPI Cloud](https://fastapicloud.com/)，如果还没有的话去加入候补名单吧。🚀

如果你已经有 **FastAPI Cloud** 账号（我们从候补名单邀请了你 😉），你可以用一个命令部署你的应用。

部署前，先确认已登录：

```
$ fastapi login

You are logged in to FastAPI Cloud 🚀
```

然后部署你的应用：

```
$ fastapi deploy

Deploying to FastAPI Cloud...

✅ Deployment successful!

🐔 Ready the chicken! Your app is ready at https://myapp.fastapicloud.dev
```

就这样！现在你可以通过该 URL 访问你的应用了。✨

#### 关于 FastAPI Cloud[¶](https://fastapi.tiangolo.com/zh/#about-fastapi-cloud "Permanent link")

**[FastAPI Cloud](https://fastapicloud.com/)** 由 **FastAPI** 的同一位作者和团队打造。

它让你以最小的工作量就能**构建**、**部署**并**访问**一个 API。

它把用 FastAPI 构建应用时的**开发者体验**带到了部署到云上的过程。🎉

FastAPI Cloud 是「FastAPI and friends」开源项目的主要赞助方和资金提供者。✨

#### 部署到其他云厂商[¶](https://fastapi.tiangolo.com/zh/#deploy-to-other-cloud-providers "Permanent link")

FastAPI 是开源且基于标准的。你可以部署 FastAPI 应用到你选择的任意云厂商。

按照你的云厂商的指南部署 FastAPI 应用即可。🤓

性能[¶](https://fastapi.tiangolo.com/zh/#performance "Permanent link")
--------------------------------------------------------------------

独立机构 TechEmpower 的基准测试显示，运行在 Uvicorn 下的 **FastAPI** 应用是[最快的 Python 框架之一](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7)，仅次于 Starlette 和 Uvicorn 本身（FastAPI 内部使用它们）。(*)

想了解更多，请参阅[基准测试](https://fastapi.tiangolo.com/zh/benchmarks/)章节。

依赖项[¶](https://fastapi.tiangolo.com/zh/#dependencies "Permanent link")
----------------------------------------------------------------------

FastAPI 依赖 Pydantic 和 Starlette。

### `standard` 依赖[¶](https://fastapi.tiangolo.com/zh/#standard-dependencies "Permanent link")

当你通过 `pip install "fastapi[standard]"` 安装 FastAPI 时，会包含 `standard` 组的一些可选依赖：

Pydantic 使用：

*   [`email-validator`](https://github.com/JoshData/python-email-validator) - 用于 email 校验。

Starlette 使用：

*   [`httpx`](https://www.python-httpx.org/) - 使用 `TestClient` 时需要。
*   [`jinja2`](https://jinja.palletsprojects.com/) - 使用默认模板配置时需要。
*   [`python-multipart`](https://github.com/Kludex/python-multipart) - 使用 `request.form()` 支持表单「解析」时需要。

FastAPI 使用：

*   [`uvicorn`](https://www.uvicorn.dev/) - 加载并提供你的应用的服务器。包含 `uvicorn[standard]`，其中包含高性能服务所需的一些依赖（例如 `uvloop`）。
*   `fastapi-cli[standard]` - 提供 `fastapi` 命令。
    *   其中包含 `fastapi-cloud-cli`，它允许你将 FastAPI 应用部署到 [FastAPI Cloud](https://fastapicloud.com/)。

### 不包含 `standard` 依赖[¶](https://fastapi.tiangolo.com/zh/#without-standard-dependencies "Permanent link")

如果你不想包含这些 `standard` 可选依赖，可以使用 `pip install fastapi`，而不是 `pip install "fastapi[standard]"`。

### 不包含 `fastapi-cloud-cli`[¶](https://fastapi.tiangolo.com/zh/#without-fastapi-cloud-cli "Permanent link")

如果你想安装带有 standard 依赖但不包含 `fastapi-cloud-cli` 的 FastAPI，可以使用 `pip install "fastapi[standard-no-fastapi-cloud-cli]"`。

### 其他可选依赖[¶](https://fastapi.tiangolo.com/zh/#additional-optional-dependencies "Permanent link")

还有一些你可能想安装的可选依赖。

额外的 Pydantic 可选依赖：

*   [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) - 用于配置管理。
*   [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) - 用于在 Pydantic 中使用的额外类型。

额外的 FastAPI 可选依赖：

*   [`orjson`](https://github.com/ijl/orjson) - 使用 `ORJSONResponse` 时需要。
*   [`ujson`](https://github.com/esnme/ultrajson) - 使用 `UJSONResponse` 时需要。

许可协议[¶](https://fastapi.tiangolo.com/zh/#license "Permanent link")
------------------------------------------------------------------

该项目遵循 MIT 许可协议。
