# Source: https://docs.litestar.dev/

Title: Litestar library documentation — Litestar Framework

URL Source: https://docs.litestar.dev/

Markdown Content:
Litestar is a powerful, flexible, highly performant, and opinionated ASGI framework.

The Litestar framework supports [Plugins](https://docs.litestar.dev/latest/usage/plugins/index.html), ships with [dependency injection](https://docs.litestar.dev/latest/usage/dependency-injection.html), [security primitives](https://docs.litestar.dev/latest/usage/security/index.html), [OpenAPI schema generation](https://docs.litestar.dev/latest/usage/openapi/index.html), [MessagePack](https://msgpack.org/), [middlewares](https://docs.litestar.dev/latest/usage/middleware/index.html), a great [CLI](https://docs.litestar.dev/latest/usage/cli.html) experience, and much more.

Installation[#](https://docs.litestar.dev/#installation "Link to this heading")
-------------------------------------------------------------------------------

pip install litestar

Tip

`litestar[standard]` includes commonly used extras like `uvicorn` and `jinja2` (for templating).

[Pydantic](https://docs.pydantic.dev/latest/)
`pip install 'litestar[pydantic]'`

[Attrs](https://www.attrs.org/)
`pip install 'litestar[attrs]'`

[Brotli Compression Middleware](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#brotli):
`pip install 'litestar[brotli]'`

[Cookie Based Sessions](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#client-side-sessions)
`pip install 'litestar[cryptography]'`

[JWT](https://docs.litestar.dev/latest/usage/security/jwt.html)
`pip install 'litestar[jwt]'`

[RedisStore](https://docs.litestar.dev/latest/usage/stores.html)
`pip install 'litestar[redis]'`

[Picologging](https://docs.litestar.dev/latest/usage/logging.html#using-picologging)
`pip install 'litestar[picologging]'`

[StructLog](https://docs.litestar.dev/latest/usage/logging.html#using-structlog)
`pip install 'litestar[structlog]'`

[Prometheus Instrumentation](https://docs.litestar.dev/latest/usage/metrics/prometheus.html)
`pip install 'litestar[prometheus]'`

[Open Telemetry Instrumentation](https://docs.litestar.dev/latest/usage/metrics/open-telemetry.html)
`pip install 'litestar[opentelemetry]'`

[SQLAlchemy](https://docs.litestar.dev/latest/usage/databases/sqlalchemy/index.html)
`pip install 'litestar[sqlalchemy]'`

[CLI](https://docs.litestar.dev/latest/usage/cli.html)
Deprecated since version 2.1.1: The `litestar` base installation now includes the CLI dependencies and this group is no longer required to use the CLI. If you need the optional CLI dependencies, install the `standard` group instead. **Will be removed in 3.0**

`pip install 'litestar[cli]'`

[Jinja Templating](https://docs.litestar.dev/latest/usage/templating.html)
`pip install 'litestar[jinja]'`

[Mako Templating](https://docs.litestar.dev/latest/usage/templating.html)
`pip install 'litestar[mako]'`

Standard Installation (includes Uvicorn and Jinja2 templating):
`pip install 'litestar[standard]'`

All Extras:
`pip install 'litestar[full]'`

Note

The full extras is not recommended because it will add a lot of unnecessary extras.

Minimal Example[#](https://docs.litestar.dev/#minimal-example "Link to this heading")
-------------------------------------------------------------------------------------

At a minimum, make sure you have installed `litestar[standard]`, which includes uvicorn.

First, create a file named `app.py` with the following contents:

from litestar import Litestar, get

@get("/")
async def index() -> str:
    return "Hello, world!"

@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}

app = Litestar([index, get_book])

Then, run the following command:

litestar run
# Or you can run Uvicorn directly:
uvicorn app:app --reload

You can now visit `http://localhost:8000/` and `http://localhost:8000/books/1` in your browser and you should see the responses of your two endpoints:

"Hello, world!"

and

{"book_id": 1}

Tip

You can also check out the automatically generated OpenAPI-based documentation at:

*   `http://localhost:8000/schema` (for [ReDoc](https://redocly.com/redoc)),

*   `http://localhost:8000/schema/swagger` (for [Swagger UI](https://swagger.io/)),

*   `http://localhost:8000/schema/elements` (for [Stoplight Elements](https://stoplight.io/open-source/elements/))

*   `http://localhost:8000/schema/rapidoc` (for [RapiDoc](https://rapidocweb.com/))

You can check out a more in-depth tutorial in the [Developing a basic TODO application](https://docs.litestar.dev/latest/tutorials/todo-app/index.html) section!

Expanded Example[#](https://docs.litestar.dev/#expanded-example "Link to this heading")
---------------------------------------------------------------------------------------

**Define your data model** using pydantic or any library based on it (for example ormar, beanie, SQLModel):

from pydantic import BaseModel, UUID4

class User(BaseModel):
    first_name: str
    last_name: str
    id: UUID4

You can also use dataclasses (standard library and Pydantic), [`typing.TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "(in Python v3.14)"), or [`msgspec.Struct`](https://jcristharif.com/msgspec/api.html#msgspec.Struct "(in msgspec)").

from uuid import UUID

from dataclasses import dataclass
from litestar.dto import DTOConfig, DataclassDTO

@dataclass
class User:
    first_name: str
    last_name: str
    id: UUID

class PartialUserDTO(DataclassDTO[User]):
    config = DTOConfig(exclude={"id"}, partial=True)

**Define a Controller for your data model:**

Python 3.8+

from typing import List

from litestar import Controller, get, post, put, patch, delete
from litestar.dto import DTOData
from pydantic import UUID4

from my_app.models import User, PartialUserDTO

class UserController(Controller):
    path = "/users"

    @post()
    async def create_user(self, data: User) -> User: ...

    @get()
    async def list_users(self) -> List[User]: ...

    @patch(path="/{user_id:uuid}", dto=PartialUserDTO)
    async def partial_update_user(
        self, user_id: UUID4, data: DTOData[User]
    ) -> User: ...

    @put(path="/{user_id:uuid}")
    async def update_user(self, user_id: UUID4, data: User) -> User: ...

    @get(path="/{user_id:uuid}")
    async def get_user(self, user_id: UUID4) -> User: ...

    @delete(path="/{user_id:uuid}")
    async def delete_user(self, user_id: UUID4) -> None: ...

Python 3.9+

from litestar import Controller, get, post, put, patch, delete
from litestar.dto import DTOData
from pydantic import UUID4

from my_app.models import User, PartialUserDTO

class UserController(Controller):
    path = "/users"

    @post()
    async def create_user(self, data: User) -> User: ...

    @get()
    async def list_users(self) -> list[User]: ...

    @patch(path="/{user_id:uuid}", dto=PartialUserDTO)
    async def partial_update_user(
        self, user_id: UUID4, data: DTOData[User]
    ) -> User: ...

    @put(path="/{user_id:uuid}")
    async def update_user(self, user_id: UUID4, data: User) -> User: ...

    @get(path="/{user_id:uuid}")
    async def get_user(self, user_id: UUID4) -> User: ...

    @delete(path="/{user_id:uuid}")
    async def delete_user(self, user_id: UUID4) -> None: ...

When instantiating your app, import your _controller_ into your application’s entry-point and pass it to Litestar:

from litestar import Litestar

from my_app.controllers.user import UserController

app = Litestar(route_handlers=[UserController])

To **run your application**, use an ASGI server such as [uvicorn](https://www.uvicorn.org/) :

uvicorn my_app.main:app --reload

Philosophy[#](https://docs.litestar.dev/#philosophy "Link to this heading")
---------------------------------------------------------------------------

*   Litestar is a community-driven project. This means not a single author, but rather a core team of maintainers is leading the project, supported by a community of contributors. Litestar currently has 5 maintainers and is being very actively developed.

*   Litestar draws inspiration from [NestJS](https://nestjs.com/) - a contemporary TypeScript framework - which places opinions and patterns at its core.

*   While still allowing for **function-based endpoints**, Litestar seeks to build on Python’s powerful and versatile OOP, by placing **class-based controllers** at its core.

*   Litestar is **not** a microframework. Unlike frameworks such as FastAPI, Starlette, or Flask, Litestar includes a lot of functionalities out of the box needed for a typical modern web application, such as ORM integration, client- and server-side sessions, caching, OpenTelemetry integration, and many more. It’s not aiming to be “the next Django” (for example, it will never feature its own ORM), but its scope is not micro either.

Feature comparison with similar frameworks[#](https://docs.litestar.dev/#feature-comparison-with-similar-frameworks "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

|  | Litestar | FastAPI | Starlette | Sanic | Quart |
| --- | --- | --- | --- | --- | --- |
| OpenAPI |  |  |  |  |  |
| Automatic API documentation | Swagger, ReDoc, Stoplight Elements | Swagger, ReDoc |  |  |  |
| Data validation |  |  |  |  |  |
| Dependency Injection |  |  |  |  |  |
| Class based routing |  | (Through extension) |  |  |  |
| ORM integration | SQLAlchemy, Tortoise, Piccolo |  |  |  | (Through extension) |
| Templating | Jinja, Mako | Jinja | Jinja | Jinja | Jinja |
| MessagePack |  |  |  |  |  |
| CORS |  |  |  |  | (Through extension) |
| CSRF |  |  |  |  |  |
| Rate-limiting |  |  |  | (Through extension) |  |
| JWT |  |  |  |  |  |
| Sessions |  | Client-side | Client-side |  | Client-side |
| Authentication | JWT / Session based |  |  |  |  |
| Caching |  |  |  |  |  |

Example Applications[#](https://docs.litestar.dev/#example-applications "Link to this heading")
-----------------------------------------------------------------------------------------------

*   [litestar-fullstack](https://github.com/litestar-org/litestar-fullstack) : A fully-capable, production-ready fullstack Litestar web application configured with best practices. It includes SQLAlchemy 2.0, VueJS, [Vite](https://vitejs.dev/), [SAQ job queue](https://saq-py.readthedocs.io/en/latest/), `Jinja` templates and more. [Read more](https://litestar-org.github.io/litestar-fullstack/latest/). Like all Litestar projects, this application is open to contributions, big and small.

*   [litestar-fullstack-inertia](https://github.com/litestar-org/litestar-fullstack-inertia) : Similar to [Litestar Fullstack](https://litestar-org.github.io/litestar-fullstack/latest/) but uses [Inertia.js](https://inertiajs.com/).

*   [litestar-hello-world](https://github.com/litestar-org/litestar-hello-world): A bare-minimum application setup. Great for testing and POC work.
