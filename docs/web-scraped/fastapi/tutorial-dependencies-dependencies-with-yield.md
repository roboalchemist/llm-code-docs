# Source: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/

Title: Dependencies with yield - FastAPI

URL Source: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/

Markdown Content:
Dependencies with yield - FastAPI
===============
- [x] - [x] 

[Skip to content](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield)

[Join the **FastAPI Cloud** waiting list 🚀](https://fastapicloud.com/)

[Follow **@fastapi** on **X (Twitter)** to stay updated](https://x.com/fastapi)

[Follow **FastAPI** on **LinkedIn** to stay updated](https://www.linkedin.com/company/fastapi)

[Subscribe to the **FastAPI and friends** newsletter 🎉](https://fastapi.tiangolo.com/newsletter/)

[sponsor![Image 1](https://fastapi.tiangolo.com/img/sponsors/blockbee-banner.png)](https://blockbee.io/?ref=fastapi "BlockBee Cryptocurrency Payment Gateway")

[sponsor![Image 2](https://fastapi.tiangolo.com/img/sponsors/scalar-banner.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=top-banner "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI files")

[sponsor![Image 3](https://fastapi.tiangolo.com/img/sponsors/propelauth-banner.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=topbanner "Auth, user management and more for your B2B product")

[sponsor![Image 4](https://fastapi.tiangolo.com/img/sponsors/zuplo-banner.png)](https://zuplo.link/fastapi-web "Zuplo: Scale, Protect, Document, and Monetize your FastAPI")

[sponsor![Image 5](https://fastapi.tiangolo.com/img/sponsors/liblab-banner.png)](https://liblab.com/?utm_source=fastapi "liblab - Generate SDKs from FastAPI")

[sponsor![Image 6](https://fastapi.tiangolo.com/img/sponsors/render-banner.svg)](https://docs.render.com/deploy-fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy & scale any full-stack web app on Render. Focus on building apps, not infra.")

[sponsor![Image 7](https://fastapi.tiangolo.com/img/sponsors/coderabbit-banner.png)](https://www.coderabbit.ai/?utm_source=fastapi&utm_medium=banner&utm_campaign=fastapi "Cut Code Review Time & Bugs in Half with CodeRabbit")

[sponsor![Image 8](https://fastapi.tiangolo.com/img/sponsors/subtotal-banner.svg)](https://subtotal.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=open-source "Making Retail Purchases Actionable for Brands and Developers")

[sponsor![Image 9](https://fastapi.tiangolo.com/img/sponsors/railway-banner.png)](https://docs.railway.com/guides/fastapi?utm_medium=integration&utm_source=docs&utm_campaign=fastapi "Deploy enterprise applications at startup speed")

[sponsor![Image 10](https://fastapi.tiangolo.com/img/sponsors/serpapi-banner.png)](https://serpapi.com/?utm_source=fastapi_website "SerpApi: Web Search API")

[sponsor![Image 11](https://fastapi.tiangolo.com/img/sponsors/greptile-banner.png)](https://www.greptile.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=fastapi_sponsor_page "Greptile: The AI Code Reviewer")

[![Image 12: logo](https://fastapi.tiangolo.com/img/icon-white.svg)](https://fastapi.tiangolo.com/ "FastAPI")

 FastAPI 

 Dependencies with yield 

*   [en - English](https://fastapi.tiangolo.com/)
*   [de - Deutsch](https://fastapi.tiangolo.com/de/)
*   [es - español](https://fastapi.tiangolo.com/es/)
*   [fr - français](https://fastapi.tiangolo.com/fr/)
*   [ja - 日本語](https://fastapi.tiangolo.com/ja/)
*   [ko - 한국어](https://fastapi.tiangolo.com/ko/)
*   [pt - português](https://fastapi.tiangolo.com/pt/)
*   [ru - русский язык](https://fastapi.tiangolo.com/ru/)
*   [tr - Türkçe](https://fastapi.tiangolo.com/tr/)
*   [uk - українська мова](https://fastapi.tiangolo.com/uk/)
*   [zh - 简体中文](https://fastapi.tiangolo.com/zh/)
*   [zh-hant - 繁體中文](https://fastapi.tiangolo.com/zh-hant/)

[](javascript:void(0) "Share")

 Initializing search 

[fastapi/fastapi](https://github.com/fastapi/fastapi "Go to repository")

*   [FastAPI](https://fastapi.tiangolo.com/)
*   [Features](https://fastapi.tiangolo.com/features/)
*   [Learn](https://fastapi.tiangolo.com/learn/)
*   [Reference](https://fastapi.tiangolo.com/reference/)
*   [FastAPI People](https://fastapi.tiangolo.com/fastapi-people/)
*   [Resources](https://fastapi.tiangolo.com/resources/)
*   [About](https://fastapi.tiangolo.com/about/)
*   [Release Notes](https://fastapi.tiangolo.com/release-notes/)

[![Image 13: logo](https://fastapi.tiangolo.com/img/icon-white.svg)](https://fastapi.tiangolo.com/ "FastAPI") FastAPI  

[fastapi/fastapi](https://github.com/fastapi/fastapi "Go to repository")

*   [FastAPI](https://fastapi.tiangolo.com/)
*   [Features](https://fastapi.tiangolo.com/features/)
*   - [x] [Learn](https://fastapi.tiangolo.com/learn/)  Learn  
    *   [Python Types Intro](https://fastapi.tiangolo.com/python-types/)
    *   [Concurrency and async / await](https://fastapi.tiangolo.com/async/)
    *   [Environment Variables](https://fastapi.tiangolo.com/environment-variables/)
    *   [Virtual Environments](https://fastapi.tiangolo.com/virtual-environments/)
    *   - [x] [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)  Tutorial - User Guide  
        *   [First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
        *   [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
        *   [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
        *   [Request Body](https://fastapi.tiangolo.com/tutorial/body/)
        *   [Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)
        *   [Path Parameters and Numeric Validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/)
        *   [Query Parameter Models](https://fastapi.tiangolo.com/tutorial/query-param-models/)
        *   [Body - Multiple Parameters](https://fastapi.tiangolo.com/tutorial/body-multiple-params/)
        *   [Body - Fields](https://fastapi.tiangolo.com/tutorial/body-fields/)
        *   [Body - Nested Models](https://fastapi.tiangolo.com/tutorial/body-nested-models/)
        *   [Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
        *   [Extra Data Types](https://fastapi.tiangolo.com/tutorial/extra-data-types/)
        *   [Cookie Parameters](https://fastapi.tiangolo.com/tutorial/cookie-params/)
        *   [Header Parameters](https://fastapi.tiangolo.com/tutorial/header-params/)
        *   [Cookie Parameter Models](https://fastapi.tiangolo.com/tutorial/cookie-param-models/)
        *   [Header Parameter Models](https://fastapi.tiangolo.com/tutorial/header-param-models/)
        *   [Response Model - Return Type](https://fastapi.tiangolo.com/tutorial/response-model/)
        *   [Extra Models](https://fastapi.tiangolo.com/tutorial/extra-models/)
        *   [Response Status Code](https://fastapi.tiangolo.com/tutorial/response-status-code/)
        *   [Form Data](https://fastapi.tiangolo.com/tutorial/request-forms/)
        *   [Form Models](https://fastapi.tiangolo.com/tutorial/request-form-models/)
        *   [Request Files](https://fastapi.tiangolo.com/tutorial/request-files/)
        *   [Request Forms and Files](https://fastapi.tiangolo.com/tutorial/request-forms-and-files/)
        *   [Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
        *   [Path Operation Configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/)
        *   [JSON Compatible Encoder](https://fastapi.tiangolo.com/tutorial/encoder/)
        *   [Body - Updates](https://fastapi.tiangolo.com/tutorial/body-updates/)
        *   - [x] [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)  Dependencies  
            *   [Classes as Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/)
            *   [Sub-dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/)
            *   [Dependencies in path operation decorators](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/)
            *   [Global Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/)
            *   - [x]  Dependencies with yield  [Dependencies with yield](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/) Table of contents  
                *   [A database dependency with `yield`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#a-database-dependency-with-yield)
                *   [A dependency with `yield` and `try`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#a-dependency-with-yield-and-try)
                *   [Sub-dependencies with `yield`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#sub-dependencies-with-yield)
                *   [Dependencies with `yield` and `HTTPException`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield-and-httpexception)
                *   [Dependencies with `yield` and `except`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield-and-except)
                    *   [Always `raise` in Dependencies with `yield` and `except`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#always-raise-in-dependencies-with-yield-and-except)

                *   [Execution of dependencies with `yield`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#execution-of-dependencies-with-yield)
                *   [Early exit and `scope`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#early-exit-and-scope)
                    *   [`scope` for sub-dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#scope-for-sub-dependencies)

                *   [Dependencies with `yield`, `HTTPException`, `except` and Background Tasks](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield-httpexception-except-and-background-tasks)
                *   [Context Managers](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#context-managers)
                    *   [What are "Context Managers"](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#what-are-context-managers)
                    *   [Using context managers in dependencies with `yield`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#using-context-managers-in-dependencies-with-yield)

        *   - [x] [Security](https://fastapi.tiangolo.com/tutorial/security/)  Security  
            *   [Security - First Steps](https://fastapi.tiangolo.com/tutorial/security/first-steps/)
            *   [Get Current User](https://fastapi.tiangolo.com/tutorial/security/get-current-user/)
            *   [Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)
            *   [OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

        *   [Middleware](https://fastapi.tiangolo.com/tutorial/middleware/)
        *   [CORS (Cross-Origin Resource Sharing)](https://fastapi.tiangolo.com/tutorial/cors/)
        *   [SQL (Relational) Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
        *   [Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
        *   [Stream JSON Lines](https://fastapi.tiangolo.com/tutorial/stream-json-lines/)
        *   [Server-Sent Events (SSE)](https://fastapi.tiangolo.com/tutorial/server-sent-events/)
        *   [Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
        *   [Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/)
        *   [Static Files](https://fastapi.tiangolo.com/tutorial/static-files/)
        *   [Testing](https://fastapi.tiangolo.com/tutorial/testing/)
        *   [Debugging](https://fastapi.tiangolo.com/tutorial/debugging/)

    *   - [x] [Advanced User Guide](https://fastapi.tiangolo.com/advanced/)  Advanced User Guide  
        *   [Stream Data](https://fastapi.tiangolo.com/advanced/stream-data/)
        *   [Path Operation Advanced Configuration](https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/)
        *   [Additional Status Codes](https://fastapi.tiangolo.com/advanced/additional-status-codes/)
        *   [Return a Response Directly](https://fastapi.tiangolo.com/advanced/response-directly/)
        *   [Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/)
        *   [Additional Responses in OpenAPI](https://fastapi.tiangolo.com/advanced/additional-responses/)
        *   [Response Cookies](https://fastapi.tiangolo.com/advanced/response-cookies/)
        *   [Response Headers](https://fastapi.tiangolo.com/advanced/response-headers/)
        *   [Response - Change Status Code](https://fastapi.tiangolo.com/advanced/response-change-status-code/)
        *   [Advanced Dependencies](https://fastapi.tiangolo.com/advanced/advanced-dependencies/)
        *   - [x] [Advanced Security](https://fastapi.tiangolo.com/advanced/security/)  Advanced Security  
            *   [OAuth2 scopes](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/)
            *   [HTTP Basic Auth](https://fastapi.tiangolo.com/advanced/security/http-basic-auth/)

        *   [Using the Request Directly](https://fastapi.tiangolo.com/advanced/using-request-directly/)
        *   [Using Dataclasses](https://fastapi.tiangolo.com/advanced/dataclasses/)
        *   [Advanced Middleware](https://fastapi.tiangolo.com/advanced/middleware/)
        *   [Sub Applications - Mounts](https://fastapi.tiangolo.com/advanced/sub-applications/)
        *   [Behind a Proxy](https://fastapi.tiangolo.com/advanced/behind-a-proxy/)
        *   [Templates](https://fastapi.tiangolo.com/advanced/templates/)
        *   [WebSockets](https://fastapi.tiangolo.com/advanced/websockets/)
        *   [Lifespan Events](https://fastapi.tiangolo.com/advanced/events/)
        *   [Testing WebSockets](https://fastapi.tiangolo.com/advanced/testing-websockets/)
        *   [Testing Events: lifespan and startup - shutdown](https://fastapi.tiangolo.com/advanced/testing-events/)
        *   [Testing Dependencies with Overrides](https://fastapi.tiangolo.com/advanced/testing-dependencies/)
        *   [Async Tests](https://fastapi.tiangolo.com/advanced/async-tests/)
        *   [Settings and Environment Variables](https://fastapi.tiangolo.com/advanced/settings/)
        *   [OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/)
        *   [OpenAPI Webhooks](https://fastapi.tiangolo.com/advanced/openapi-webhooks/)
        *   [Including WSGI - Flask, Django, others](https://fastapi.tiangolo.com/advanced/wsgi/)
        *   [Generating SDKs](https://fastapi.tiangolo.com/advanced/generate-clients/)
        *   [Advanced Python Types](https://fastapi.tiangolo.com/advanced/advanced-python-types/)
        *   [JSON with Bytes as Base64](https://fastapi.tiangolo.com/advanced/json-base64-bytes/)
        *   [Strict Content-Type Checking](https://fastapi.tiangolo.com/advanced/strict-content-type/)

    *   [FastAPI CLI](https://fastapi.tiangolo.com/fastapi-cli/)
    *   - [x] [Deployment](https://fastapi.tiangolo.com/deployment/)  Deployment  
        *   [About FastAPI versions](https://fastapi.tiangolo.com/deployment/versions/)
        *   [FastAPI Cloud](https://fastapi.tiangolo.com/deployment/fastapicloud/)
        *   [About HTTPS](https://fastapi.tiangolo.com/deployment/https/)
        *   [Run a Server Manually](https://fastapi.tiangolo.com/deployment/manually/)
        *   [Deployments Concepts](https://fastapi.tiangolo.com/deployment/concepts/)
        *   [Deploy FastAPI on Cloud Providers](https://fastapi.tiangolo.com/deployment/cloud/)
        *   [Server Workers - Uvicorn with Workers](https://fastapi.tiangolo.com/deployment/server-workers/)
        *   [FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/)

    *   - [x] [How To - Recipes](https://fastapi.tiangolo.com/how-to/)  How To - Recipes  
        *   [General - How To - Recipes](https://fastapi.tiangolo.com/how-to/general/)
        *   [Migrate from Pydantic v1 to Pydantic v2](https://fastapi.tiangolo.com/how-to/migrate-from-pydantic-v1-to-pydantic-v2/)
        *   [GraphQL](https://fastapi.tiangolo.com/how-to/graphql/)
        *   [Custom Request and APIRoute class](https://fastapi.tiangolo.com/how-to/custom-request-and-route/)
        *   [Conditional OpenAPI](https://fastapi.tiangolo.com/how-to/conditional-openapi/)
        *   [Extending OpenAPI](https://fastapi.tiangolo.com/how-to/extending-openapi/)
        *   [Separate OpenAPI Schemas for Input and Output or Not](https://fastapi.tiangolo.com/how-to/separate-openapi-schemas/)
        *   [Custom Docs UI Static Assets (Self-Hosting)](https://fastapi.tiangolo.com/how-to/custom-docs-ui-assets/)
        *   [Configure Swagger UI](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/)
        *   [Testing a Database](https://fastapi.tiangolo.com/how-to/testing-database/)
        *   [Use Old 403 Authentication Error Status Codes](https://fastapi.tiangolo.com/how-to/authentication-error-status-code/)

*   - [x] [Reference](https://fastapi.tiangolo.com/reference/)  Reference  
    *   [`FastAPI` class](https://fastapi.tiangolo.com/reference/fastapi/)
    *   [Request Parameters](https://fastapi.tiangolo.com/reference/parameters/)
    *   [Status Codes](https://fastapi.tiangolo.com/reference/status/)
    *   [`UploadFile` class](https://fastapi.tiangolo.com/reference/uploadfile/)
    *   [Exceptions - `HTTPException` and `WebSocketException`](https://fastapi.tiangolo.com/reference/exceptions/)
    *   [Dependencies - `Depends()` and `Security()`](https://fastapi.tiangolo.com/reference/dependencies/)
    *   [`APIRouter` class](https://fastapi.tiangolo.com/reference/apirouter/)
    *   [Background Tasks - `BackgroundTasks`](https://fastapi.tiangolo.com/reference/background/)
    *   [`Request` class](https://fastapi.tiangolo.com/reference/request/)
    *   [WebSockets](https://fastapi.tiangolo.com/reference/websockets/)
    *   [`HTTPConnection` class](https://fastapi.tiangolo.com/reference/httpconnection/)
    *   [`Response` class](https://fastapi.tiangolo.com/reference/response/)
    *   [Custom Response Classes - File, HTML, Redirect, Streaming, etc.](https://fastapi.tiangolo.com/reference/responses/)
    *   [Middleware](https://fastapi.tiangolo.com/reference/middleware/)
    *   - [x] [OpenAPI](https://fastapi.tiangolo.com/reference/openapi/)  OpenAPI  
        *   [OpenAPI `docs`](https://fastapi.tiangolo.com/reference/openapi/docs/)
        *   [OpenAPI `models`](https://fastapi.tiangolo.com/reference/openapi/models/)

    *   [Security Tools](https://fastapi.tiangolo.com/reference/security/)
    *   [Encoders - `jsonable_encoder`](https://fastapi.tiangolo.com/reference/encoders/)
    *   [Static Files - `StaticFiles`](https://fastapi.tiangolo.com/reference/staticfiles/)
    *   [Templating - `Jinja2Templates`](https://fastapi.tiangolo.com/reference/templating/)
    *   [Test Client - `TestClient`](https://fastapi.tiangolo.com/reference/testclient/)

*   [FastAPI People](https://fastapi.tiangolo.com/fastapi-people/)
*   - [x] [Resources](https://fastapi.tiangolo.com/resources/)  Resources  
    *   [Help FastAPI - Get Help](https://fastapi.tiangolo.com/help-fastapi/)
    *   [Development - Contributing](https://fastapi.tiangolo.com/contributing/)
    *   [Full Stack FastAPI Template](https://fastapi.tiangolo.com/project-generation/)
    *   [External Links](https://fastapi.tiangolo.com/external-links/)
    *   [FastAPI and friends newsletter](https://fastapi.tiangolo.com/newsletter/)
    *   [Repository Management Tasks](https://fastapi.tiangolo.com/management-tasks/)

*   - [x] [About](https://fastapi.tiangolo.com/about/)  About  
    *   [Alternatives, Inspiration and Comparisons](https://fastapi.tiangolo.com/alternatives/)
    *   [History, Design and Future](https://fastapi.tiangolo.com/history-design-future/)
    *   [Benchmarks](https://fastapi.tiangolo.com/benchmarks/)
    *   [Repository Management](https://fastapi.tiangolo.com/management/)

*   [Release Notes](https://fastapi.tiangolo.com/release-notes/)

 Table of contents  
*   [A database dependency with `yield`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#a-database-dependency-with-yield)
*   [A dependency with `yield` and `try`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#a-dependency-with-yield-and-try)
*   [Sub-dependencies with `yield`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#sub-dependencies-with-yield)
*   [Dependencies with `yield` and `HTTPException`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield-and-httpexception)
*   [Dependencies with `yield` and `except`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield-and-except)
    *   [Always `raise` in Dependencies with `yield` and `except`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#always-raise-in-dependencies-with-yield-and-except)

*   [Execution of dependencies with `yield`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#execution-of-dependencies-with-yield)
*   [Early exit and `scope`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#early-exit-and-scope)
    *   [`scope` for sub-dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#scope-for-sub-dependencies)

*   [Dependencies with `yield`, `HTTPException`, `except` and Background Tasks](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield-httpexception-except-and-background-tasks)
*   [Context Managers](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#context-managers)
    *   [What are "Context Managers"](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#what-are-context-managers)
    *   [Using context managers in dependencies with `yield`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#using-context-managers-in-dependencies-with-yield)

1.   [FastAPI](https://fastapi.tiangolo.com/)
2.   [Learn](https://fastapi.tiangolo.com/learn/)
3.   [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
4.   [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)

Dependencies with yield[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield "Permanent link")
================================================================================================================================================

FastAPI supports dependencies that do some extra steps after finishing.

To do this, use `yield` instead of `return`, and write the extra steps (code) after.

Tip

Make sure to use `yield` one single time per dependency.

Technical Details

Any function that is valid to use with:

*   [`@contextlib.contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager) or
*   [`@contextlib.asynccontextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager)

would be valid to use as a **FastAPI** dependency.

In fact, FastAPI uses those two decorators internally.

A database dependency with `yield`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#a-database-dependency-with-yield "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

For example, you could use this to create a database session and close it after finishing.

Only the code prior to and including the `yield` statement is executed before creating a response:

Python 3.10+ 

```
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

The yielded value is what is injected into _path operations_ and other dependencies:

Python 3.10+ 

```
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

The code following the `yield` statement is executed after the response:

Python 3.10+ 

```
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

Tip

You can use `async` or regular functions.

**FastAPI** will do the right thing with each, the same as with normal dependencies.

A dependency with `yield` and `try`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#a-dependency-with-yield-and-try "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you use a `try` block in a dependency with `yield`, you'll receive any exception that was thrown when using the dependency.

For example, if some code at some point in the middle, in another dependency or in a _path operation_, made a database transaction "rollback" or created any other exception, you would receive the exception in your dependency.

So, you can look for that specific exception inside the dependency with `except SomeException`.

In the same way, you can use `finally` to make sure the exit steps are executed, no matter if there was an exception or not.

Python 3.10+ 

```
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

Sub-dependencies with `yield`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#sub-dependencies-with-yield "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------

You can have sub-dependencies and "trees" of sub-dependencies of any size and shape, and any or all of them can use `yield`.

**FastAPI** will make sure that the "exit code" in each dependency with `yield` is run in the correct order.

For example, `dependency_c` can have a dependency on `dependency_b`, and `dependency_b` on `dependency_a`:

Python 3.10+ 

```
from typing import Annotated

from fastapi import Depends

async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()

async def dependency_b(dep_a: Annotated[DepA, Depends(dependency_a)]):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)

async def dependency_c(dep_b: Annotated[DepB, Depends(dependency_b)]):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends

async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()

async def dependency_b(dep_a=Depends(dependency_a)):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)

async def dependency_c(dep_b=Depends(dependency_b)):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)
```

And all of them can use `yield`.

In this case `dependency_c`, to execute its exit code, needs the value from `dependency_b` (here named `dep_b`) to still be available.

And, in turn, `dependency_b` needs the value from `dependency_a` (here named `dep_a`) to be available for its exit code.

Python 3.10+ 

```
from typing import Annotated

from fastapi import Depends

async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()

async def dependency_b(dep_a: Annotated[DepA, Depends(dependency_a)]):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)

async def dependency_c(dep_b: Annotated[DepB, Depends(dependency_b)]):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends

async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()

async def dependency_b(dep_a=Depends(dependency_a)):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)

async def dependency_c(dep_b=Depends(dependency_b)):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)
```

The same way, you could have some dependencies with `yield` and some other dependencies with `return`, and have some of those depend on some of the others.

And you could have a single dependency that requires several other dependencies with `yield`, etc.

You can have any combinations of dependencies that you want.

**FastAPI** will make sure everything is run in the correct order.

Technical Details

This works thanks to Python's [Context Managers](https://docs.python.org/3/library/contextlib.html).

**FastAPI** uses them internally to achieve this.

Dependencies with `yield` and `HTTPException`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield-and-httpexception "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You saw that you can use dependencies with `yield` and have `try` blocks that try to execute some code and then run some exit code after `finally`.

You can also use `except` to catch the exception that was raised and do something with it.

For example, you can raise a different exception, like `HTTPException`.

Tip

This is a somewhat advanced technique, and in most of the cases you won't really need it, as you can raise exceptions (including `HTTPException`) from inside of the rest of your application code, for example, in the _path operation function_.

But it's there for you if you need it. 🤓

Python 3.10+ 

```
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

data = {
    "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
    "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
}

class OwnerError(Exception):
    pass

def get_username():
    try:
        yield "Rick"
    except OwnerError as e:
        raise HTTPException(status_code=400, detail=f"Owner error: {e}")

@app.get("/items/{item_id}")
def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
    item = data[item_id]
    if item["owner"] != username:
        raise OwnerError(username)
    return item
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

data = {
    "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
    "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
}

class OwnerError(Exception):
    pass

def get_username():
    try:
        yield "Rick"
    except OwnerError as e:
        raise HTTPException(status_code=400, detail=f"Owner error: {e}")

@app.get("/items/{item_id}")
def get_item(item_id: str, username: str = Depends(get_username)):
    if item_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
    item = data[item_id]
    if item["owner"] != username:
        raise OwnerError(username)
    return item
```

If you want to catch exceptions and create a custom response based on that, create a [Custom Exception Handler](https://fastapi.tiangolo.com/tutorial/handling-errors/#install-custom-exception-handlers).

Dependencies with `yield` and `except`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield-and-except "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you catch an exception using `except` in a dependency with `yield` and you don't raise it again (or raise a new exception), FastAPI won't be able to notice there was an exception, the same way that would happen with regular Python:

Python 3.10+ 

```
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

class InternalError(Exception):
    pass

def get_username():
    try:
        yield "Rick"
    except InternalError:
        print("Oops, we didn't raise again, Britney 😱")

@app.get("/items/{item_id}")
def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id == "portal-gun":
        raise InternalError(
            f"The portal gun is too dangerous to be owned by {username}"
        )
    if item_id != "plumbus":
        raise HTTPException(
            status_code=404, detail="Item not found, there's only a plumbus here"
        )
    return item_id
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

class InternalError(Exception):
    pass

def get_username():
    try:
        yield "Rick"
    except InternalError:
        print("Oops, we didn't raise again, Britney 😱")

@app.get("/items/{item_id}")
def get_item(item_id: str, username: str = Depends(get_username)):
    if item_id == "portal-gun":
        raise InternalError(
            f"The portal gun is too dangerous to be owned by {username}"
        )
    if item_id != "plumbus":
        raise HTTPException(
            status_code=404, detail="Item not found, there's only a plumbus here"
        )
    return item_id
```

In this case, the client will see an _HTTP 500 Internal Server Error_ response as it should, given that we are not raising an `HTTPException` or similar, but the server will **not have any logs** or any other indication of what was the error. 😱

### Always `raise` in Dependencies with `yield` and `except`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#always-raise-in-dependencies-with-yield-and-except "Permanent link")

If you catch an exception in a dependency with `yield`, unless you are raising another `HTTPException` or similar, **you should re-raise the original exception**.

You can re-raise the same exception using `raise`:

Python 3.10+ 

```
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

class InternalError(Exception):
    pass

def get_username():
    try:
        yield "Rick"
    except InternalError:
        print("We don't swallow the internal error here, we raise again 😎")
        raise

@app.get("/items/{item_id}")
def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id == "portal-gun":
        raise InternalError(
            f"The portal gun is too dangerous to be owned by {username}"
        )
    if item_id != "plumbus":
        raise HTTPException(
            status_code=404, detail="Item not found, there's only a plumbus here"
        )
    return item_id
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

class InternalError(Exception):
    pass

def get_username():
    try:
        yield "Rick"
    except InternalError:
        print("We don't swallow the internal error here, we raise again 😎")
        raise

@app.get("/items/{item_id}")
def get_item(item_id: str, username: str = Depends(get_username)):
    if item_id == "portal-gun":
        raise InternalError(
            f"The portal gun is too dangerous to be owned by {username}"
        )
    if item_id != "plumbus":
        raise HTTPException(
            status_code=404, detail="Item not found, there's only a plumbus here"
        )
    return item_id
```

Now the client will get the same _HTTP 500 Internal Server Error_ response, but the server will have our custom `InternalError` in the logs. 😎

Execution of dependencies with `yield`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#execution-of-dependencies-with-yield "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The sequence of execution is more or less like this diagram. Time flows from top to bottom. And each column is one of the parts interacting or executing code.

```
sequenceDiagram

participant client as Client
participant handler as Exception handler
participant dep as Dep with yield
participant operation as Path Operation
participant tasks as Background tasks

    Note over client,operation: Can raise exceptions, including HTTPException
    client ->> dep: Start request
    Note over dep: Run code up to yield
    opt raise Exception
        dep -->> handler: Raise Exception
        handler -->> client: HTTP error response
    end
    dep ->> operation: Run dependency, e.g. DB session
    opt raise
        operation -->> dep: Raise Exception (e.g. HTTPException)
        opt handle
            dep -->> dep: Can catch exception, raise a new HTTPException, raise other exception
        end
        handler -->> client: HTTP error response
    end

    operation ->> client: Return response to client
    Note over client,operation: Response is already sent, can't change it anymore
    opt Tasks
        operation -->> tasks: Send background tasks
    end
    opt Raise other exception
        tasks -->> tasks: Handle exceptions in the background task code
    end
```

Info

Only **one response** will be sent to the client. It might be one of the error responses or it will be the response from the _path operation_.

After one of those responses is sent, no other response can be sent.

Tip

If you raise any exception in the code from the _path operation function_, it will be passed to the dependencies with yield, including `HTTPException`. In most cases you will want to re-raise that same exception or a new one from the dependency with `yield` to make sure it's properly handled.

Early exit and `scope`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#early-exit-and-scope "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------

Normally the exit code of dependencies with `yield` is executed **after the response** is sent to the client.

But if you know that you won't need to use the dependency after returning from the _path operation function_, you can use `Depends(scope="function")` to tell FastAPI that it should close the dependency after the _path operation function_ returns, but **before** the **response is sent**.

Python 3.10+ 

```
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()

def get_username():
    try:
        yield "Rick"
    finally:
        print("Cleanup up before response is sent")

@app.get("/users/me")
def get_user_me(username: Annotated[str, Depends(get_username, scope="function")]):
    return username
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI

app = FastAPI()

def get_username():
    try:
        yield "Rick"
    finally:
        print("Cleanup up before response is sent")

@app.get("/users/me")
def get_user_me(username: str = Depends(get_username, scope="function")):
    return username
```

`Depends()` receives a `scope` parameter that can be:

*   `"function"`: start the dependency before the _path operation function_ that handles the request, end the dependency after the _path operation function_ ends, but **before** the response is sent back to the client. So, the dependency function will be executed **around** the _path operation **function**_.
*   `"request"`: start the dependency before the _path operation function_ that handles the request (similar to when using `"function"`), but end **after** the response is sent back to the client. So, the dependency function will be executed **around** the **request** and response cycle.

If not specified and the dependency has `yield`, it will have a `scope` of `"request"` by default.

### `scope` for sub-dependencies[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#scope-for-sub-dependencies "Permanent link")

When you declare a dependency with a `scope="request"` (the default), any sub-dependency needs to also have a `scope` of `"request"`.

But a dependency with `scope` of `"function"` can have dependencies with `scope` of `"function"` and `scope` of `"request"`.

This is because any dependency needs to be able to run its exit code before the sub-dependencies, as it might need to still use them during its exit code.

```
sequenceDiagram

participant client as Client
participant dep_req as Dep scope="request"
participant dep_func as Dep scope="function"
participant operation as Path Operation

    client ->> dep_req: Start request
    Note over dep_req: Run code up to yield
    dep_req ->> dep_func: Pass dependency
    Note over dep_func: Run code up to yield
    dep_func ->> operation: Run path operation with dependency
    operation ->> dep_func: Return from path operation
    Note over dep_func: Run code after yield
    Note over dep_func: ✅ Dependency closed
    dep_func ->> client: Send response to client
    Note over client: Response sent
    Note over dep_req: Run code after yield
    Note over dep_req: ✅ Dependency closed
```

Dependencies with `yield`, `HTTPException`, `except` and Background Tasks[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield-httpexception-except-and-background-tasks "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Dependencies with `yield` have evolved over time to cover different use cases and fix some issues.

If you want to see what has changed in different versions of FastAPI, you can read more about it in the advanced guide, in [Advanced Dependencies - Dependencies with `yield`, `HTTPException`, `except` and Background Tasks](https://fastapi.tiangolo.com/advanced/advanced-dependencies/#dependencies-with-yield-httpexception-except-and-background-tasks).

Context Managers[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#context-managers "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------

### What are "Context Managers"[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#what-are-context-managers "Permanent link")

"Context Managers" are any of those Python objects that you can use in a `with` statement.

For example, [you can use `with` to read a file](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files):

```
with open("./somefile.txt") as f:
    contents = f.read()
    print(contents)
```

Underneath, the `open("./somefile.txt")` creates an object that is called a "Context Manager".

When the `with` block finishes, it makes sure to close the file, even if there were exceptions.

When you create a dependency with `yield`, **FastAPI** will internally create a context manager for it, and combine it with some other related tools.

### Using context managers in dependencies with `yield`[¶](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#using-context-managers-in-dependencies-with-yield "Permanent link")

Warning

This is, more or less, an "advanced" idea.

If you are just starting with **FastAPI** you might want to skip it for now.

In Python, you can create Context Managers by [creating a class with two methods: `__enter__()` and `__exit__()`](https://docs.python.org/3/reference/datamodel.html#context-managers).

You can also use them inside of **FastAPI** dependencies with `yield` by using `with` or `async with` statements inside of the dependency function:

Python 3.10+ 

```
class MySuperContextManager:
    def __init__(self):
        self.db = DBSession()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()

async def get_db():
    with MySuperContextManager() as db:
        yield db
```

Tip

Another way to create a context manager is with:

*   [`@contextlib.contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager) or
*   [`@contextlib.asynccontextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager)

using them to decorate a function with a single `yield`.

That's what **FastAPI** uses internally for dependencies with `yield`.

But you don't have to use the decorators for FastAPI dependencies (and you shouldn't).

FastAPI will do it for you internally.

 Back to top [Previous Global Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/)[Next Security](https://fastapi.tiangolo.com/tutorial/security/)

 The FastAPI trademark is owned by [@tiangolo](https://tiangolo.com/) and is registered in the US and across other regions 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://github.com/fastapi/fastapi "github.com")[](https://discord.gg/VQjSZaeJmf "discord.gg")[](https://x.com/fastapi "x.com")[](https://www.linkedin.com/company/fastapi "www.linkedin.com")[](https://tiangolo.com/ "tiangolo.com")
