# Source: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

Title: OAuth2 with Password (and hashing), Bearer with JWT tokens - FastAPI

URL Source: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

Markdown Content:
OAuth2 with Password (and hashing), Bearer with JWT tokens - FastAPI
===============
- [x] - [x] 

[Skip to content](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#oauth2-with-password-and-hashing-bearer-with-jwt-tokens)

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

 OAuth2 with Password (and hashing), Bearer with JWT tokens 

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
            *   [Dependencies with yield](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)

        *   - [x] [Security](https://fastapi.tiangolo.com/tutorial/security/)  Security  
            *   [Security - First Steps](https://fastapi.tiangolo.com/tutorial/security/first-steps/)
            *   [Get Current User](https://fastapi.tiangolo.com/tutorial/security/get-current-user/)
            *   [Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)
            *   - [x]  OAuth2 with Password (and hashing), Bearer with JWT tokens  [OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) Table of contents  
                *   [About JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#about-jwt)
                *   [Install `PyJWT`](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-pyjwt)
                *   [Password hashing](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#password-hashing)
                    *   [Why use password hashing](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#why-use-password-hashing)

                *   [Install `pwdlib`](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-pwdlib)
                *   [Hash and verify the passwords](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#hash-and-verify-the-passwords)
                *   [Handle JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#handle-jwt-tokens)
                *   [Update the dependencies](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#update-the-dependencies)
                *   [Update the `/token`_path operation_](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#update-the-token-path-operation)
                    *   [Technical details about the JWT "subject" `sub`](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#technical-details-about-the-jwt-subject-sub)

                *   [Check it](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#check-it)
                *   [Advanced usage with `scopes`](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#advanced-usage-with-scopes)
                *   [Recap](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#recap)

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
*   [About JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#about-jwt)
*   [Install `PyJWT`](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-pyjwt)
*   [Password hashing](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#password-hashing)
    *   [Why use password hashing](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#why-use-password-hashing)

*   [Install `pwdlib`](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-pwdlib)
*   [Hash and verify the passwords](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#hash-and-verify-the-passwords)
*   [Handle JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#handle-jwt-tokens)
*   [Update the dependencies](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#update-the-dependencies)
*   [Update the `/token`_path operation_](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#update-the-token-path-operation)
    *   [Technical details about the JWT "subject" `sub`](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#technical-details-about-the-jwt-subject-sub)

*   [Check it](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#check-it)
*   [Advanced usage with `scopes`](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#advanced-usage-with-scopes)
*   [Recap](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#recap)

1.   [FastAPI](https://fastapi.tiangolo.com/)
2.   [Learn](https://fastapi.tiangolo.com/learn/)
3.   [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
4.   [Security](https://fastapi.tiangolo.com/tutorial/security/)

OAuth2 with Password (and hashing), Bearer with JWT tokens[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#oauth2-with-password-and-hashing-bearer-with-jwt-tokens "Permanent link")
==================================================================================================================================================================================================

Now that we have all the security flow, let's make the application actually secure, using JWT tokens and secure password hashing.

This code is something you can actually use in your application, save the password hashes in your database, etc.

We are going to start from where we left in the previous chapter and increment it.

About JWT[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#about-jwt "Permanent link")
---------------------------------------------------------------------------------------------------

JWT means "JSON Web Tokens".

It's a standard to codify a JSON object in a long dense string without spaces. It looks like this:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

It is not encrypted, so, anyone could recover the information from the contents.

But it's signed. So, when you receive a token that you emitted, you can verify that you actually emitted it.

That way, you can create a token with an expiration of, let's say, 1 week. And then when the user comes back the next day with the token, you know that user is still logged in to your system.

After a week, the token will be expired and the user will not be authorized and will have to sign in again to get a new token. And if the user (or a third party) tried to modify the token to change the expiration, you would be able to discover it, because the signatures would not match.

If you want to play with JWT tokens and see how they work, check [https://jwt.io](https://jwt.io/).

Install `PyJWT`[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-pyjwt "Permanent link")
-------------------------------------------------------------------------------------------------------------

We need to install `PyJWT` to generate and verify the JWT tokens in Python.

Make sure you create a [virtual environment](https://fastapi.tiangolo.com/virtual-environments/), activate it, and then install `pyjwt`:

```
$ pip install pyjwt

---> 100%
```

Info

If you are planning to use digital signature algorithms like RSA or ECDSA, you should install the cryptography library dependency `pyjwt[crypto]`.

You can read more about it in the [PyJWT Installation docs](https://pyjwt.readthedocs.io/en/latest/installation.html).

Password hashing[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#password-hashing "Permanent link")
-----------------------------------------------------------------------------------------------------------------

"Hashing" means converting some content (a password in this case) into a sequence of bytes (just a string) that looks like gibberish.

Whenever you pass exactly the same content (exactly the same password) you get exactly the same gibberish.

But you cannot convert from the gibberish back to the password.

### Why use password hashing[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#why-use-password-hashing "Permanent link")

If your database is stolen, the thief won't have your users' plaintext passwords, only the hashes.

So, the thief won't be able to try to use that password in another system (as many users use the same password everywhere, this would be dangerous).

Install `pwdlib`[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-pwdlib "Permanent link")
---------------------------------------------------------------------------------------------------------------

pwdlib is a great Python package to handle password hashes.

It supports many secure hashing algorithms and utilities to work with them.

The recommended algorithm is "Argon2".

Make sure you create a [virtual environment](https://fastapi.tiangolo.com/virtual-environments/), activate it, and then install pwdlib with Argon2:

```
$ pip install "pwdlib[argon2]"

---> 100%
```

Tip

With `pwdlib`, you could even configure it to be able to read passwords created by **Django**, a **Flask** security plug-in or many others.

So, you would be able to, for example, share the same data from a Django application in a database with a FastAPI application. Or gradually migrate a Django application using the same database.

And your users would be able to login from your Django app or from your **FastAPI** app, at the same time.

Hash and verify the passwords[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#hash-and-verify-the-passwords "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------

Import the tools we need from `pwdlib`.

Create a PasswordHash instance with recommended settings - it will be used for hashing and verifying passwords.

Tip

pwdlib also supports the bcrypt hashing algorithm but does not include legacy algorithms - for working with outdated hashes, it is recommended to use the passlib library.

For example, you could use it to read and verify passwords generated by another system (like Django) but hash any new passwords with a different algorithm like Argon2 or Bcrypt.

And be compatible with all of them at the same time.

Create a utility function to hash a password coming from the user.

And another utility to verify if a received password matches the hash stored.

And another one to authenticate and return a user.

Python 3.10+ 

```
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

password_hash = PasswordHash.recommended()

DUMMY_HASH = password_hash.hash("dummypassword")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me/")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> User:
    return current_user

@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

password_hash = PasswordHash.recommended()

DUMMY_HASH = password_hash.hash("dummypassword")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me/")
async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User:
    return current_user

@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
```

When `authenticate_user` is called with a username that doesn't exist in the database, we still run `verify_password` against a dummy hash.

This ensures the endpoint takes roughly the same amount of time to respond whether the username is valid or not, preventing **timing attacks** that could be used to enumerate existing usernames.

Note

If you check the new (fake) database `fake_users_db`, you will see how the hashed password looks like now: `"$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc"`.

Handle JWT tokens[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#handle-jwt-tokens "Permanent link")
-------------------------------------------------------------------------------------------------------------------

Import the modules installed.

Create a random secret key that will be used to sign the JWT tokens.

To generate a secure random secret key use the command:

```
$ openssl rand -hex 32

09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
```

And copy the output to the variable `SECRET_KEY` (don't use the one in the example).

Create a variable `ALGORITHM` with the algorithm used to sign the JWT token and set it to `"HS256"`.

Create a variable for the expiration of the token.

Define a Pydantic Model that will be used in the token endpoint for the response.

Create a utility function to generate a new access token.

Python 3.10+ 

```
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

password_hash = PasswordHash.recommended()

DUMMY_HASH = password_hash.hash("dummypassword")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me/")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> User:
    return current_user

@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

password_hash = PasswordHash.recommended()

DUMMY_HASH = password_hash.hash("dummypassword")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me/")
async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User:
    return current_user

@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
```

Update the dependencies[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#update-the-dependencies "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------

Update `get_current_user` to receive the same token as before, but this time, using JWT tokens.

Decode the received token, verify it, and return the current user.

If the token is invalid, return an HTTP error right away.

Python 3.10+ 

```
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

password_hash = PasswordHash.recommended()

DUMMY_HASH = password_hash.hash("dummypassword")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me/")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> User:
    return current_user

@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

password_hash = PasswordHash.recommended()

DUMMY_HASH = password_hash.hash("dummypassword")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me/")
async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User:
    return current_user

@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
```

Update the `/token`_path operation_[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#update-the-token-path-operation "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

Create a `timedelta` with the expiration time of the token.

Create a real JWT access token and return it.

Python 3.10+ 

```
from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

password_hash = PasswordHash.recommended()

DUMMY_HASH = password_hash.hash("dummypassword")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me/")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> User:
    return current_user

@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

password_hash = PasswordHash.recommended()

DUMMY_HASH = password_hash.hash("dummypassword")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        verify_password(password, DUMMY_HASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me/")
async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User:
    return current_user

@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
```

### Technical details about the JWT "subject" `sub`[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#technical-details-about-the-jwt-subject-sub "Permanent link")

The JWT specification says that there's a key `sub`, with the subject of the token.

It's optional to use it, but that's where you would put the user's identification, so we are using it here.

JWT might be used for other things apart from identifying a user and allowing them to perform operations directly on your API.

For example, you could identify a "car" or a "blog post".

Then you could add permissions about that entity, like "drive" (for the car) or "edit" (for the blog).

And then, you could give that JWT token to a user (or bot), and they could use it to perform those actions (drive the car, or edit the blog post) without even needing to have an account, just with the JWT token your API generated for that.

Using these ideas, JWT can be used for way more sophisticated scenarios.

In those cases, several of those entities could have the same ID, let's say `foo` (a user `foo`, a car `foo`, and a blog post `foo`).

So, to avoid ID collisions, when creating the JWT token for the user, you could prefix the value of the `sub` key, e.g. with `username:`. So, in this example, the value of `sub` could have been: `username:johndoe`.

The important thing to keep in mind is that the `sub` key should have a unique identifier across the entire application, and it should be a string.

Check it[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#check-it "Permanent link")
-------------------------------------------------------------------------------------------------

Run the server and go to the docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

You'll see the user interface like:

![Image 14](https://fastapi.tiangolo.com/img/tutorial/security/image07.png)

Authorize the application the same way as before.

Using the credentials:

Username: `johndoe` Password: `secret`

Check

Notice that nowhere in the code is the plaintext password "`secret`", we only have the hashed version.

![Image 15](https://fastapi.tiangolo.com/img/tutorial/security/image08.png)

Call the endpoint `/users/me/`, you will get the response as:

```
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "full_name": "John Doe",
  "disabled": false
}
```

![Image 16](https://fastapi.tiangolo.com/img/tutorial/security/image09.png)

If you open the developer tools, you could see how the data sent only includes the token, the password is only sent in the first request to authenticate the user and get that access token, but not afterwards:

![Image 17](https://fastapi.tiangolo.com/img/tutorial/security/image10.png)

Note

Notice the header `Authorization`, with a value that starts with `Bearer`.

Advanced usage with `scopes`[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#advanced-usage-with-scopes "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------

OAuth2 has the notion of "scopes".

You can use them to add a specific set of permissions to a JWT token.

Then you can give this token to a user directly or a third party, to interact with your API with a set of restrictions.

You can learn how to use them and how they are integrated into **FastAPI** later in the **Advanced User Guide**.

Recap[¶](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#recap "Permanent link")
-------------------------------------------------------------------------------------------

With what you have seen up to now, you can set up a secure **FastAPI** application using standards like OAuth2 and JWT.

In almost any framework handling the security becomes a rather complex subject quite quickly.

Many packages that simplify it a lot have to make many compromises with the data model, database, and available features. And some of these packages that simplify things too much actually have security flaws underneath.

* * *

**FastAPI** doesn't make any compromise with any database, data model or tool.

It gives you all the flexibility to choose the ones that fit your project the best.

And you can use directly many well maintained and widely used packages like `pwdlib` and `PyJWT`, because **FastAPI** doesn't require any complex mechanisms to integrate external packages.

But it provides you the tools to simplify the process as much as possible without compromising flexibility, robustness, or security.

And you can use and implement secure, standard protocols, like OAuth2 in a relatively simple way.

You can learn more in the **Advanced User Guide** about how to use OAuth2 "scopes", for a more fine-grained permission system, following these same standards. OAuth2 with scopes is the mechanism used by many big authentication providers, like Facebook, Google, GitHub, Microsoft, X (Twitter), etc. to authorize third party applications to interact with their APIs on behalf of their users.

 Back to top [Previous Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)[Next Middleware](https://fastapi.tiangolo.com/tutorial/middleware/)

 The FastAPI trademark is owned by [@tiangolo](https://tiangolo.com/) and is registered in the US and across other regions 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://github.com/fastapi/fastapi "github.com")[](https://discord.gg/VQjSZaeJmf "discord.gg")[](https://x.com/fastapi "x.com")[](https://www.linkedin.com/company/fastapi "www.linkedin.com")[](https://tiangolo.com/ "tiangolo.com")
