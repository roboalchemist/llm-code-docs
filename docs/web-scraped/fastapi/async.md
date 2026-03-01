# Source: https://fastapi.tiangolo.com/async/

Title: Concurrency and async / await - FastAPI

URL Source: https://fastapi.tiangolo.com/async/

Markdown Content:
Concurrency and async / await - FastAPI
===============
- [x] - [x] 

[Skip to content](https://fastapi.tiangolo.com/async/#concurrency-and-async-await)

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

 Concurrency and async / await 

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
    *   - [x]  Concurrency and async / await  [Concurrency and async / await](https://fastapi.tiangolo.com/async/) Table of contents  
        *   [In a hurry?](https://fastapi.tiangolo.com/async/#in-a-hurry)
        *   [Technical Details](https://fastapi.tiangolo.com/async/#technical-details)
        *   [Asynchronous Code](https://fastapi.tiangolo.com/async/#asynchronous-code)
            *   [Concurrency and Burgers](https://fastapi.tiangolo.com/async/#concurrency-and-burgers)
            *   [Concurrent Burgers](https://fastapi.tiangolo.com/async/#concurrent-burgers)
            *   [Parallel Burgers](https://fastapi.tiangolo.com/async/#parallel-burgers)
            *   [Burger Conclusion](https://fastapi.tiangolo.com/async/#burger-conclusion)
            *   [Is concurrency better than parallelism?](https://fastapi.tiangolo.com/async/#is-concurrency-better-than-parallelism)
            *   [Concurrency + Parallelism: Web + Machine Learning](https://fastapi.tiangolo.com/async/#concurrency-parallelism-web-machine-learning)

        *   [`async` and `await`](https://fastapi.tiangolo.com/async/#async-and-await)
            *   [More technical details](https://fastapi.tiangolo.com/async/#more-technical-details)
            *   [Write your own async code](https://fastapi.tiangolo.com/async/#write-your-own-async-code)
            *   [Other forms of asynchronous code](https://fastapi.tiangolo.com/async/#other-forms-of-asynchronous-code)

        *   [Coroutines](https://fastapi.tiangolo.com/async/#coroutines)
        *   [Conclusion](https://fastapi.tiangolo.com/async/#conclusion)
        *   [Very Technical Details](https://fastapi.tiangolo.com/async/#very-technical-details)
            *   [Path operation functions](https://fastapi.tiangolo.com/async/#path-operation-functions)
            *   [Dependencies](https://fastapi.tiangolo.com/async/#dependencies)
            *   [Sub-dependencies](https://fastapi.tiangolo.com/async/#sub-dependencies)
            *   [Other utility functions](https://fastapi.tiangolo.com/async/#other-utility-functions)

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
            *   [Dependencies with yield](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)

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
*   [In a hurry?](https://fastapi.tiangolo.com/async/#in-a-hurry)
*   [Technical Details](https://fastapi.tiangolo.com/async/#technical-details)
*   [Asynchronous Code](https://fastapi.tiangolo.com/async/#asynchronous-code)
    *   [Concurrency and Burgers](https://fastapi.tiangolo.com/async/#concurrency-and-burgers)
    *   [Concurrent Burgers](https://fastapi.tiangolo.com/async/#concurrent-burgers)
    *   [Parallel Burgers](https://fastapi.tiangolo.com/async/#parallel-burgers)
    *   [Burger Conclusion](https://fastapi.tiangolo.com/async/#burger-conclusion)
    *   [Is concurrency better than parallelism?](https://fastapi.tiangolo.com/async/#is-concurrency-better-than-parallelism)
    *   [Concurrency + Parallelism: Web + Machine Learning](https://fastapi.tiangolo.com/async/#concurrency-parallelism-web-machine-learning)

*   [`async` and `await`](https://fastapi.tiangolo.com/async/#async-and-await)
    *   [More technical details](https://fastapi.tiangolo.com/async/#more-technical-details)
    *   [Write your own async code](https://fastapi.tiangolo.com/async/#write-your-own-async-code)
    *   [Other forms of asynchronous code](https://fastapi.tiangolo.com/async/#other-forms-of-asynchronous-code)

*   [Coroutines](https://fastapi.tiangolo.com/async/#coroutines)
*   [Conclusion](https://fastapi.tiangolo.com/async/#conclusion)
*   [Very Technical Details](https://fastapi.tiangolo.com/async/#very-technical-details)
    *   [Path operation functions](https://fastapi.tiangolo.com/async/#path-operation-functions)
    *   [Dependencies](https://fastapi.tiangolo.com/async/#dependencies)
    *   [Sub-dependencies](https://fastapi.tiangolo.com/async/#sub-dependencies)
    *   [Other utility functions](https://fastapi.tiangolo.com/async/#other-utility-functions)

1.   [FastAPI](https://fastapi.tiangolo.com/)
2.   [Learn](https://fastapi.tiangolo.com/learn/)

Concurrency and async / await[¶](https://fastapi.tiangolo.com/async/#concurrency-and-async-await "Permanent link")
==================================================================================================================

Details about the `async def` syntax for _path operation functions_ and some background about asynchronous code, concurrency, and parallelism.

In a hurry?[¶](https://fastapi.tiangolo.com/async/#in-a-hurry "Permanent link")
-------------------------------------------------------------------------------

**TL;DR:**

If you are using third party libraries that tell you to call them with `await`, like:

```
results = await some_library()
```

Then, declare your _path operation functions_ with `async def` like:

```
@app.get('/')
async def read_results():
    results = await some_library()
    return results
```

Note

You can only use `await` inside of functions created with `async def`.

* * *

If you are using a third party library that communicates with something (a database, an API, the file system, etc.) and doesn't have support for using `await`, (this is currently the case for most database libraries), then declare your _path operation functions_ as normally, with just `def`, like:

```
@app.get('/')
def results():
    results = some_library()
    return results
```

* * *

If your application (somehow) doesn't have to communicate with anything else and wait for it to respond, use `async def`, even if you don't need to use `await` inside.

* * *

If you just don't know, use normal `def`.

* * *

**Note**: You can mix `def` and `async def` in your _path operation functions_ as much as you need and define each one using the best option for you. FastAPI will do the right thing with them.

Anyway, in any of the cases above, FastAPI will still work asynchronously and be extremely fast.

But by following the steps above, it will be able to do some performance optimizations.

Technical Details[¶](https://fastapi.tiangolo.com/async/#technical-details "Permanent link")
--------------------------------------------------------------------------------------------

Modern versions of Python have support for **"asynchronous code"** using something called **"coroutines"**, with **`async` and `await`** syntax.

Let's see that phrase by parts in the sections below:

*   **Asynchronous Code**
*   **`async` and `await`**
*   **Coroutines**

Asynchronous Code[¶](https://fastapi.tiangolo.com/async/#asynchronous-code "Permanent link")
--------------------------------------------------------------------------------------------

Asynchronous code just means that the language 💬 has a way to tell the computer / program 🤖 that at some point in the code, it 🤖 will have to wait for _something else_ to finish somewhere else. Let's say that _something else_ is called "slow-file" 📝.

So, during that time, the computer can go and do some other work, while "slow-file" 📝 finishes.

Then the computer / program 🤖 will come back every time it has a chance because it's waiting again, or whenever it 🤖 finished all the work it had at that point. And it 🤖 will see if any of the tasks it was waiting for have already finished, doing whatever it had to do.

Next, it 🤖 takes the first task to finish (let's say, our "slow-file" 📝) and continues whatever it had to do with it.

That "wait for something else" normally refers to I/O operations that are relatively "slow" (compared to the speed of the processor and the RAM memory), like waiting for:

*   the data from the client to be sent through the network
*   the data sent by your program to be received by the client through the network
*   the contents of a file in the disk to be read by the system and given to your program
*   the contents your program gave to the system to be written to disk
*   a remote API operation
*   a database operation to finish
*   a database query to return the results
*   etc.

As the execution time is consumed mostly by waiting for I/O operations, they call them "I/O bound" operations.

It's called "asynchronous" because the computer / program doesn't have to be "synchronized" with the slow task, waiting for the exact moment that the task finishes, while doing nothing, to be able to take the task result and continue the work.

Instead of that, by being an "asynchronous" system, once finished, the task can wait in line a little bit (some microseconds) for the computer / program to finish whatever it went to do, and then come back to take the results and continue working with them.

For "synchronous" (contrary to "asynchronous") they commonly also use the term "sequential", because the computer / program follows all the steps in sequence before switching to a different task, even if those steps involve waiting.

### Concurrency and Burgers[¶](https://fastapi.tiangolo.com/async/#concurrency-and-burgers "Permanent link")

This idea of **asynchronous** code described above is also sometimes called **"concurrency"**. It is different from **"parallelism"**.

**Concurrency** and **parallelism** both relate to "different things happening more or less at the same time".

But the details between _concurrency_ and _parallelism_ are quite different.

To see the difference, imagine the following story about burgers:

### Concurrent Burgers[¶](https://fastapi.tiangolo.com/async/#concurrent-burgers "Permanent link")

You go with your crush to get fast food, you stand in line while the cashier takes the orders from the people in front of you. 😍

![Image 14](https://fastapi.tiangolo.com/img/async/concurrent-burgers/concurrent-burgers-01.png)

Then it's your turn, you place your order of 2 very fancy burgers for your crush and you. 🍔🍔

![Image 15](https://fastapi.tiangolo.com/img/async/concurrent-burgers/concurrent-burgers-02.png)

The cashier says something to the cook in the kitchen so they know they have to prepare your burgers (even though they are currently preparing the ones for the previous clients).

![Image 16](https://fastapi.tiangolo.com/img/async/concurrent-burgers/concurrent-burgers-03.png)

You pay. 💸

The cashier gives you the number of your turn.

![Image 17](https://fastapi.tiangolo.com/img/async/concurrent-burgers/concurrent-burgers-04.png)

While you are waiting, you go with your crush and pick a table, you sit and talk with your crush for a long time (as your burgers are very fancy and take some time to prepare).

As you are sitting at the table with your crush, while you wait for the burgers, you can spend that time admiring how awesome, cute and smart your crush is ✨😍✨.

![Image 18](https://fastapi.tiangolo.com/img/async/concurrent-burgers/concurrent-burgers-05.png)

While waiting and talking to your crush, from time to time, you check the number displayed on the counter to see if it's your turn already.

Then at some point, it finally is your turn. You go to the counter, get your burgers and come back to the table.

![Image 19](https://fastapi.tiangolo.com/img/async/concurrent-burgers/concurrent-burgers-06.png)

You and your crush eat the burgers and have a nice time. ✨

![Image 20](https://fastapi.tiangolo.com/img/async/concurrent-burgers/concurrent-burgers-07.png)

Info

Beautiful illustrations by [Ketrina Thompson](https://www.instagram.com/ketrinadrawsalot). 🎨

* * *

Imagine you are the computer / program 🤖 in that story.

While you are at the line, you are just idle 😴, waiting for your turn, not doing anything very "productive". But the line is fast because the cashier is only taking the orders (not preparing them), so that's fine.

Then, when it's your turn, you do actual "productive" work, you process the menu, decide what you want, get your crush's choice, pay, check that you give the correct bill or card, check that you are charged correctly, check that the order has the correct items, etc.

But then, even though you still don't have your burgers, your work with the cashier is "on pause" ⏸, because you have to wait 🕙 for your burgers to be ready.

But as you go away from the counter and sit at the table with a number for your turn, you can switch 🔀 your attention to your crush, and "work" ⏯ 🤓 on that. Then you are again doing something very "productive" as is flirting with your crush 😍.

Then the cashier 💁 says "I'm finished with doing the burgers" by putting your number on the counter's display, but you don't jump like crazy immediately when the displayed number changes to your turn number. You know no one will steal your burgers because you have the number of your turn, and they have theirs.

So you wait for your crush to finish the story (finish the current work ⏯ / task being processed 🤓), smile gently and say that you are going for the burgers ⏸.

Then you go to the counter 🔀, to the initial task that is now finished ⏯, pick the burgers, say thanks and take them to the table. That finishes that step / task of interaction with the counter ⏹. That in turn, creates a new task, of "eating burgers" 🔀 ⏯, but the previous one of "getting burgers" is finished ⏹.

### Parallel Burgers[¶](https://fastapi.tiangolo.com/async/#parallel-burgers "Permanent link")

Now let's imagine these aren't "Concurrent Burgers", but "Parallel Burgers".

You go with your crush to get parallel fast food.

You stand in line while several (let's say 8) cashiers that at the same time are cooks take the orders from the people in front of you.

Everyone before you is waiting for their burgers to be ready before leaving the counter because each of the 8 cashiers goes and prepares the burger right away before getting the next order.

![Image 21](https://fastapi.tiangolo.com/img/async/parallel-burgers/parallel-burgers-01.png)

Then it's finally your turn, you place your order of 2 very fancy burgers for your crush and you.

You pay 💸.

![Image 22](https://fastapi.tiangolo.com/img/async/parallel-burgers/parallel-burgers-02.png)

The cashier goes to the kitchen.

You wait, standing in front of the counter 🕙, so that no one else takes your burgers before you do, as there are no numbers for turns.

![Image 23](https://fastapi.tiangolo.com/img/async/parallel-burgers/parallel-burgers-03.png)

As you and your crush are busy not letting anyone get in front of you and take your burgers whenever they arrive, you cannot pay attention to your crush. 😞

This is "synchronous" work, you are "synchronized" with the cashier/cook 👨‍🍳. You have to wait 🕙 and be there at the exact moment that the cashier/cook 👨‍🍳 finishes the burgers and gives them to you, or otherwise, someone else might take them.

![Image 24](https://fastapi.tiangolo.com/img/async/parallel-burgers/parallel-burgers-04.png)

Then your cashier/cook 👨‍🍳 finally comes back with your burgers, after a long time waiting 🕙 there in front of the counter.

![Image 25](https://fastapi.tiangolo.com/img/async/parallel-burgers/parallel-burgers-05.png)

You take your burgers and go to the table with your crush.

You just eat them, and you are done. ⏹

![Image 26](https://fastapi.tiangolo.com/img/async/parallel-burgers/parallel-burgers-06.png)

There was not much talk or flirting as most of the time was spent waiting 🕙 in front of the counter. 😞

Info

Beautiful illustrations by [Ketrina Thompson](https://www.instagram.com/ketrinadrawsalot). 🎨

* * *

In this scenario of the parallel burgers, you are a computer / program 🤖 with two processors (you and your crush), both waiting 🕙 and dedicating their attention ⏯ to be "waiting on the counter" 🕙 for a long time.

The fast food store has 8 processors (cashiers/cooks). While the concurrent burgers store might have had only 2 (one cashier and one cook).

But still, the final experience is not the best. 😞

* * *

This would be the parallel equivalent story for burgers. 🍔

For a more "real life" example of this, imagine a bank.

Up to recently, most of the banks had multiple cashiers 👨‍💼👨‍💼👨‍💼👨‍💼 and a big line 🕙🕙🕙🕙🕙🕙🕙🕙.

All of the cashiers doing all the work with one client after the other 👨‍💼⏯.

And you have to wait 🕙 in the line for a long time or you lose your turn.

You probably wouldn't want to take your crush 😍 with you to run errands at the bank 🏦.

### Burger Conclusion[¶](https://fastapi.tiangolo.com/async/#burger-conclusion "Permanent link")

In this scenario of "fast food burgers with your crush", as there is a lot of waiting 🕙, it makes a lot more sense to have a concurrent system ⏸🔀⏯.

This is the case for most of the web applications.

Many, many users, but your server is waiting 🕙 for their not-so-good connection to send their requests.

And then waiting 🕙 again for the responses to come back.

This "waiting" 🕙 is measured in microseconds, but still, summing it all, it's a lot of waiting in the end.

That's why it makes a lot of sense to use asynchronous ⏸🔀⏯ code for web APIs.

This kind of asynchronicity is what made NodeJS popular (even though NodeJS is not parallel) and that's the strength of Go as a programming language.

And that's the same level of performance you get with **FastAPI**.

And as you can have parallelism and asynchronicity at the same time, you get higher performance than most of the tested NodeJS frameworks and on par with Go, which is a compiled language closer to C [(all thanks to Starlette)](https://www.techempower.com/benchmarks/#section=data-r17&hw=ph&test=query&l=zijmkf-1).

### Is concurrency better than parallelism?[¶](https://fastapi.tiangolo.com/async/#is-concurrency-better-than-parallelism "Permanent link")

Nope! That's not the moral of the story.

Concurrency is different than parallelism. And it is better on **specific** scenarios that involve a lot of waiting. Because of that, it generally is a lot better than parallelism for web application development. But not for everything.

So, to balance that out, imagine the following short story:

> You have to clean a big, dirty house.

_Yep, that's the whole story_.

* * *

There's no waiting 🕙 anywhere, just a lot of work to be done, on multiple places of the house.

You could have turns as in the burgers example, first the living room, then the kitchen, but as you are not waiting 🕙 for anything, just cleaning and cleaning, the turns wouldn't affect anything.

It would take the same amount of time to finish with or without turns (concurrency) and you would have done the same amount of work.

But in this case, if you could bring the 8 ex-cashier/cooks/now-cleaners, and each one of them (plus you) could take a zone of the house to clean it, you could do all the work in **parallel**, with the extra help, and finish much sooner.

In this scenario, each one of the cleaners (including you) would be a processor, doing their part of the job.

And as most of the execution time is taken by actual work (instead of waiting), and the work in a computer is done by a CPU, they call these problems "CPU bound".

* * *

Common examples of CPU bound operations are things that require complex math processing.

For example:

*   **Audio** or **image processing**.
*   **Computer vision**: an image is composed of millions of pixels, each pixel has 3 values / colors, processing that normally requires computing something on those pixels, all at the same time.
*   **Machine Learning**: it normally requires lots of "matrix" and "vector" multiplications. Think of a huge spreadsheet with numbers and multiplying all of them together at the same time.
*   **Deep Learning**: this is a sub-field of Machine Learning, so, the same applies. It's just that there is not a single spreadsheet of numbers to multiply, but a huge set of them, and in many cases, you use a special processor to build and / or use those models.

### Concurrency + Parallelism: Web + Machine Learning[¶](https://fastapi.tiangolo.com/async/#concurrency-parallelism-web-machine-learning "Permanent link")

With **FastAPI** you can take advantage of concurrency that is very common for web development (the same main attraction of NodeJS).

But you can also exploit the benefits of parallelism and multiprocessing (having multiple processes running in parallel) for **CPU bound** workloads like those in Machine Learning systems.

That, plus the simple fact that Python is the main language for **Data Science**, Machine Learning and especially Deep Learning, make FastAPI a very good match for Data Science / Machine Learning web APIs and applications (among many others).

To see how to achieve this parallelism in production see the section about [Deployment](https://fastapi.tiangolo.com/deployment/).

`async` and `await`[¶](https://fastapi.tiangolo.com/async/#async-and-await "Permanent link")
--------------------------------------------------------------------------------------------

Modern versions of Python have a very intuitive way to define asynchronous code. This makes it look just like normal "sequential" code and do the "awaiting" for you at the right moments.

When there is an operation that will require waiting before giving the results and has support for these new Python features, you can code it like:

```
burgers = await get_burgers(2)
```

The key here is the `await`. It tells Python that it has to wait ⏸ for `get_burgers(2)` to finish doing its thing 🕙 before storing the results in `burgers`. With that, Python will know that it can go and do something else 🔀 ⏯ in the meanwhile (like receiving another request).

For `await` to work, it has to be inside a function that supports this asynchronicity. To do that, you just declare it with `async def`:

```
async def get_burgers(number: int):
    # Do some asynchronous stuff to create the burgers
    return burgers
```

...instead of `def`:

```
# This is not asynchronous
def get_sequential_burgers(number: int):
    # Do some sequential stuff to create the burgers
    return burgers
```

With `async def`, Python knows that, inside that function, it has to be aware of `await` expressions, and that it can "pause" ⏸ the execution of that function and go do something else 🔀 before coming back.

When you want to call an `async def` function, you have to "await" it. So, this won't work:

```
# This won't work, because get_burgers was defined with: async def
burgers = get_burgers(2)
```

* * *

So, if you are using a library that tells you that you can call it with `await`, you need to create the _path operation functions_ that uses it with `async def`, like in:

```
@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers
```

### More technical details[¶](https://fastapi.tiangolo.com/async/#more-technical-details "Permanent link")

You might have noticed that `await` can only be used inside of functions defined with `async def`.

But at the same time, functions defined with `async def` have to be "awaited". So, functions with `async def` can only be called inside of functions defined with `async def` too.

So, about the egg and the chicken, how do you call the first `async` function?

If you are working with **FastAPI** you don't have to worry about that, because that "first" function will be your _path operation function_, and FastAPI will know how to do the right thing.

But if you want to use `async` / `await` without FastAPI, you can do it as well.

### Write your own async code[¶](https://fastapi.tiangolo.com/async/#write-your-own-async-code "Permanent link")

Starlette (and **FastAPI**) are based on [AnyIO](https://anyio.readthedocs.io/en/stable/), which makes it compatible with both Python's standard library [asyncio](https://docs.python.org/3/library/asyncio-task.html) and [Trio](https://trio.readthedocs.io/en/stable/).

In particular, you can directly use [AnyIO](https://anyio.readthedocs.io/en/stable/) for your advanced concurrency use cases that require more advanced patterns in your own code.

And even if you were not using FastAPI, you could also write your own async applications with [AnyIO](https://anyio.readthedocs.io/en/stable/) to be highly compatible and get its benefits (e.g. _structured concurrency_).

I created another library on top of AnyIO, as a thin layer on top, to improve a bit the type annotations and get better **autocompletion**, **inline errors**, etc. It also has a friendly introduction and tutorial to help you **understand** and write **your own async code**: [Asyncer](https://asyncer.tiangolo.com/). It would be particularly useful if you need to **combine async code with regular** (blocking/synchronous) code.

### Other forms of asynchronous code[¶](https://fastapi.tiangolo.com/async/#other-forms-of-asynchronous-code "Permanent link")

This style of using `async` and `await` is relatively new in the language.

But it makes working with asynchronous code a lot easier.

This same syntax (or almost identical) was also included recently in modern versions of JavaScript (in Browser and NodeJS).

But before that, handling asynchronous code was quite more complex and difficult.

In previous versions of Python, you could have used threads or [Gevent](https://www.gevent.org/). But the code is way more complex to understand, debug, and think about.

In previous versions of NodeJS / Browser JavaScript, you would have used "callbacks". Which leads to "callback hell".

Coroutines[¶](https://fastapi.tiangolo.com/async/#coroutines "Permanent link")
------------------------------------------------------------------------------

**Coroutine** is just the very fancy term for the thing returned by an `async def` function. Python knows that it is something like a function, that it can start and that it will end at some point, but that it might be paused ⏸ internally too, whenever there is an `await` inside of it.

But all this functionality of using asynchronous code with `async` and `await` is many times summarized as using "coroutines". It is comparable to the main key feature of Go, the "Goroutines".

Conclusion[¶](https://fastapi.tiangolo.com/async/#conclusion "Permanent link")
------------------------------------------------------------------------------

Let's see the same phrase from above:

> Modern versions of Python have support for **"asynchronous code"** using something called **"coroutines"**, with **`async` and `await`** syntax.

That should make more sense now. ✨

All that is what powers FastAPI (through Starlette) and what makes it have such an impressive performance.

Very Technical Details[¶](https://fastapi.tiangolo.com/async/#very-technical-details "Permanent link")
------------------------------------------------------------------------------------------------------

Warning

You can probably skip this.

These are very technical details of how **FastAPI** works underneath.

If you have quite some technical knowledge (coroutines, threads, blocking, etc.) and are curious about how FastAPI handles `async def` vs normal `def`, go ahead.

### Path operation functions[¶](https://fastapi.tiangolo.com/async/#path-operation-functions "Permanent link")

When you declare a _path operation function_ with normal `def` instead of `async def`, it is run in an external threadpool that is then awaited, instead of being called directly (as it would block the server).

If you are coming from another async framework that does not work in the way described above and you are used to defining trivial compute-only _path operation functions_ with plain `def` for a tiny performance gain (about 100 nanoseconds), please note that in **FastAPI** the effect would be quite opposite. In these cases, it's better to use `async def` unless your _path operation functions_ use code that performs blocking I/O.

Still, in both situations, chances are that **FastAPI** will [still be faster](https://fastapi.tiangolo.com/#performance) than (or at least comparable to) your previous framework.

### Dependencies[¶](https://fastapi.tiangolo.com/async/#dependencies "Permanent link")

The same applies for [dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/). If a dependency is a standard `def` function instead of `async def`, it is run in the external threadpool.

### Sub-dependencies[¶](https://fastapi.tiangolo.com/async/#sub-dependencies "Permanent link")

You can have multiple dependencies and [sub-dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/) requiring each other (as parameters of the function definitions), some of them might be created with `async def` and some with normal `def`. It would still work, and the ones created with normal `def` would be called on an external thread (from the threadpool) instead of being "awaited".

### Other utility functions[¶](https://fastapi.tiangolo.com/async/#other-utility-functions "Permanent link")

Any other utility function that you call directly can be created with normal `def` or `async def` and FastAPI won't affect the way you call it.

This is in contrast to the functions that FastAPI calls for you: _path operation functions_ and dependencies.

If your utility function is a normal function with `def`, it will be called directly (as you write it in your code), not in a threadpool, if the function is created with `async def` then you should `await` for that function when you call it in your code.

* * *

Again, these are very technical details that would probably be useful if you came searching for them.

Otherwise, you should be good with the guidelines from the section above: [In a hurry?](https://fastapi.tiangolo.com/async/#in-a-hurry).

 Back to top [Previous Python Types Intro](https://fastapi.tiangolo.com/python-types/)[Next Environment Variables](https://fastapi.tiangolo.com/environment-variables/)

 The FastAPI trademark is owned by [@tiangolo](https://tiangolo.com/) and is registered in the US and across other regions 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://github.com/fastapi/fastapi "github.com")[](https://discord.gg/VQjSZaeJmf "discord.gg")[](https://x.com/fastapi "x.com")[](https://www.linkedin.com/company/fastapi "www.linkedin.com")[](https://tiangolo.com/ "tiangolo.com")
