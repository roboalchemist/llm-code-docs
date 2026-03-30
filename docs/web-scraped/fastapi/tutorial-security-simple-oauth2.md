# Source: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/

Title: Simple OAuth2 with Password and Bearer - FastAPI

URL Source: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/

Markdown Content:
Simple OAuth2 with Password and Bearer - FastAPI
===============
- [x] - [x] 

[Skip to content](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#simple-oauth2-with-password-and-bearer)

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

 Simple OAuth2 with Password and Bearer 

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
            *   - [x]  Simple OAuth2 with Password and Bearer  [Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/) Table of contents  
                *   [Get the `username` and `password`](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#get-the-username-and-password)
                    *   [`scope`](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#scope)

                *   [Code to get the `username` and `password`](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#code-to-get-the-username-and-password)
                    *   [`OAuth2PasswordRequestForm`](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#oauth2passwordrequestform)
                    *   [Use the form data](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#use-the-form-data)
                    *   [Check the password](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#check-the-password)
                        *   [Password hashing](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#password-hashing)
                            *   [Why use password hashing](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#why-use-password-hashing)

                        *   [About `**user_dict`](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#about-user-dict)

                *   [Return the token](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#return-the-token)
                *   [Update the dependencies](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#update-the-dependencies)
                *   [See it in action](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#see-it-in-action)
                    *   [Authenticate](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#authenticate)
                    *   [Get your own user data](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#get-your-own-user-data)
                    *   [Inactive user](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#inactive-user)

                *   [Recap](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#recap)

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
*   [Get the `username` and `password`](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#get-the-username-and-password)
    *   [`scope`](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#scope)

*   [Code to get the `username` and `password`](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#code-to-get-the-username-and-password)
    *   [`OAuth2PasswordRequestForm`](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#oauth2passwordrequestform)
    *   [Use the form data](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#use-the-form-data)
    *   [Check the password](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#check-the-password)
        *   [Password hashing](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#password-hashing)
            *   [Why use password hashing](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#why-use-password-hashing)

        *   [About `**user_dict`](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#about-user-dict)

*   [Return the token](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#return-the-token)
*   [Update the dependencies](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#update-the-dependencies)
*   [See it in action](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#see-it-in-action)
    *   [Authenticate](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#authenticate)
    *   [Get your own user data](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#get-your-own-user-data)
    *   [Inactive user](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#inactive-user)

*   [Recap](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#recap)

1.   [FastAPI](https://fastapi.tiangolo.com/)
2.   [Learn](https://fastapi.tiangolo.com/learn/)
3.   [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
4.   [Security](https://fastapi.tiangolo.com/tutorial/security/)

Simple OAuth2 with Password and Bearer[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#simple-oauth2-with-password-and-bearer "Permanent link")
================================================================================================================================================================

Now let's build from the previous chapter and add the missing parts to have a complete security flow.

Get the `username` and `password`[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#get-the-username-and-password "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------

We are going to use **FastAPI** security utilities to get the `username` and `password`.

OAuth2 specifies that when using the "password flow" (that we are using) the client/user must send a `username` and `password` fields as form data.

And the spec says that the fields have to be named like that. So `user-name` or `email` wouldn't work.

But don't worry, you can show it as you wish to your final users in the frontend.

And your database models can use any other names you want.

But for the login _path operation_, we need to use these names to be compatible with the spec (and be able to, for example, use the integrated API documentation system).

The spec also states that the `username` and `password` must be sent as form data (so, no JSON here).

### `scope`[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#scope "Permanent link")

The spec also says that the client can send another form field "`scope`".

The form field name is `scope` (in singular), but it is actually a long string with "scopes" separated by spaces.

Each "scope" is just a string (without spaces).

They are normally used to declare specific security permissions, for example:

*   `users:read` or `users:write` are common examples.
*   `instagram_basic` is used by Facebook / Instagram.
*   `https://www.googleapis.com/auth/drive` is used by Google.

Info

In OAuth2 a "scope" is just a string that declares a specific permission required.

It doesn't matter if it has other characters like `:` or if it is a URL.

Those details are implementation specific.

For OAuth2 they are just strings.

Code to get the `username` and `password`[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#code-to-get-the-username-and-password "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now let's use the utilities provided by **FastAPI** to handle this.

### `OAuth2PasswordRequestForm`[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#oauth2passwordrequestform "Permanent link")

First, import `OAuth2PasswordRequestForm`, and use it as a dependency with `Depends` in the _path operation_ for `/token`:

Python 3.10+ 

```
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
```

`OAuth2PasswordRequestForm` is a class dependency that declares a form body with:

*   The `username`.
*   The `password`.
*   An optional `scope` field as a big string, composed of strings separated by spaces.
*   An optional `grant_type`.

Tip

The OAuth2 spec actually _requires_ a field `grant_type` with a fixed value of `password`, but `OAuth2PasswordRequestForm` doesn't enforce it.

If you need to enforce it, use `OAuth2PasswordRequestFormStrict` instead of `OAuth2PasswordRequestForm`.

*   An optional `client_id` (we don't need it for our example).
*   An optional `client_secret` (we don't need it for our example).

Info

The `OAuth2PasswordRequestForm` is not a special class for **FastAPI** as is `OAuth2PasswordBearer`.

`OAuth2PasswordBearer` makes **FastAPI** know that it is a security scheme. So it is added that way to OpenAPI.

But `OAuth2PasswordRequestForm` is just a class dependency that you could have written yourself, or you could have declared `Form` parameters directly.

But as it's a common use case, it is provided by **FastAPI** directly, just to make it easier.

### Use the form data[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#use-the-form-data "Permanent link")

Tip

The instance of the dependency class `OAuth2PasswordRequestForm` won't have an attribute `scope` with the long string separated by spaces, instead, it will have a `scopes` attribute with the actual list of strings for each scope sent.

We are not using `scopes` in this example, but the functionality is there if you need it.

Now, get the user data from the (fake) database, using the `username` from the form field.

If there is no such user, we return an error saying "Incorrect username or password".

For the error, we use the exception `HTTPException`:

Python 3.10+ 

```
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
```

### Check the password[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#check-the-password "Permanent link")

At this point we have the user data from our database, but we haven't checked the password.

Let's put that data in the Pydantic `UserInDB` model first.

You should never save plaintext passwords, so, we'll use the (fake) password hashing system.

If the passwords don't match, we return the same error.

#### Password hashing[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#password-hashing "Permanent link")

"Hashing" means: converting some content (a password in this case) into a sequence of bytes (just a string) that looks like gibberish.

Whenever you pass exactly the same content (exactly the same password) you get exactly the same gibberish.

But you cannot convert from the gibberish back to the password.

##### Why use password hashing[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#why-use-password-hashing "Permanent link")

If your database is stolen, the thief won't have your users' plaintext passwords, only the hashes.

So, the thief won't be able to try to use those same passwords in another system (as many users use the same password everywhere, this would be dangerous).

Python 3.10+ 

```
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
```

#### About `**user_dict`[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#about-user-dict "Permanent link")

`UserInDB(**user_dict)` means:

_Pass the keys and values of the `user\_dict` directly as key-value arguments, equivalent to:_

```
UserInDB(
    username = user_dict["username"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
    disabled = user_dict["disabled"],
    hashed_password = user_dict["hashed_password"],
)
```

Info

For a more complete explanation of `**user_dict` check back in [the documentation for **Extra Models**](https://fastapi.tiangolo.com/tutorial/extra-models/#about-user-in-dict).

Return the token[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#return-the-token "Permanent link")
--------------------------------------------------------------------------------------------------------------------

The response of the `token` endpoint must be a JSON object.

It should have a `token_type`. In our case, as we are using "Bearer" tokens, the token type should be "`bearer`".

And it should have an `access_token`, with a string containing our access token.

For this simple example, we are going to just be completely insecure and return the same `username` as the token.

Tip

In the next chapter, you will see a real secure implementation, with password hashing and JWT tokens.

But for now, let's focus on the specific details we need.

Python 3.10+ 

```
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
```

Tip

By the spec, you should return a JSON with an `access_token` and a `token_type`, the same as in this example.

This is something that you have to do yourself in your code, and make sure you use those JSON keys.

It's almost the only thing that you have to remember to do correctly yourself, to be compliant with the specifications.

For the rest, **FastAPI** handles it for you.

Update the dependencies[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#update-the-dependencies "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------

Now we are going to update our dependencies.

We want to get the `current_user`_only_ if this user is active.

So, we create an additional dependency `get_current_active_user` that in turn uses `get_current_user` as a dependency.

Both of these dependencies will just return an HTTP error if the user doesn't exist, or if is inactive.

So, in our endpoint, we will only get a user if the user exists, was correctly authenticated, and is active:

Python 3.10+ 

```
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated 

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
```

Info

The additional header `WWW-Authenticate` with value `Bearer` we are returning here is also part of the spec.

Any HTTP (error) status code 401 "UNAUTHORIZED" is supposed to also return a `WWW-Authenticate` header.

In the case of bearer tokens (our case), the value of that header should be `Bearer`.

You can actually skip that extra header and it would still work.

But it's provided here to be compliant with the specifications.

Also, there might be tools that expect and use it (now or in the future) and that might be useful for you or your users, now or in the future.

That's the benefit of standards...

See it in action[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#see-it-in-action "Permanent link")
--------------------------------------------------------------------------------------------------------------------

Open the interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Authenticate[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#authenticate "Permanent link")

Click the "Authorize" button.

Use the credentials:

User: `johndoe`

Password: `secret`

![Image 14](https://fastapi.tiangolo.com/img/tutorial/security/image04.png)

After authenticating in the system, you will see it like:

![Image 15](https://fastapi.tiangolo.com/img/tutorial/security/image05.png)

### Get your own user data[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#get-your-own-user-data "Permanent link")

Now use the operation `GET` with the path `/users/me`.

You will get your user's data, like:

```
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "full_name": "John Doe",
  "disabled": false,
  "hashed_password": "fakehashedsecret"
}
```

![Image 16](https://fastapi.tiangolo.com/img/tutorial/security/image06.png)

If you click the lock icon and logout, and then try the same operation again, you will get an HTTP 401 error of:

```
{
  "detail": "Not authenticated"
}
```

### Inactive user[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#inactive-user "Permanent link")

Now try with an inactive user, authenticate with:

User: `alice`

Password: `secret2`

And try to use the operation `GET` with the path `/users/me`.

You will get an "Inactive user" error, like:

```
{
  "detail": "Inactive user"
}
```

Recap[¶](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#recap "Permanent link")
----------------------------------------------------------------------------------------------

You now have the tools to implement a complete security system based on `username` and `password` for your API.

Using these tools, you can make the security system compatible with any database and with any user or data model.

The only detail missing is that it is not actually "secure" yet.

In the next chapter you'll see how to use a secure password hashing library and JWT tokens.

 Back to top [Previous Get Current User](https://fastapi.tiangolo.com/tutorial/security/get-current-user/)[Next OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

 The FastAPI trademark is owned by [@tiangolo](https://tiangolo.com/) and is registered in the US and across other regions 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://github.com/fastapi/fastapi "github.com")[](https://discord.gg/VQjSZaeJmf "discord.gg")[](https://x.com/fastapi "x.com")[](https://www.linkedin.com/company/fastapi "www.linkedin.com")[](https://tiangolo.com/ "tiangolo.com")
