# Source: https://docs.litestar.dev/latest/usage/dependency-injection.html

Title: Dependency Injection — Litestar Framework

URL Source: https://docs.litestar.dev/latest/usage/dependency-injection.html

Markdown Content:
Litestar has a simple but powerful dependency injection system that allows for declaring dependencies on all layers of the application:

from litestar import Controller, Router, Litestar, get
from litestar.di import Provide

async def bool_fn() -> bool: ...

async def dict_fn() -> dict: ...

async def list_fn() -> list: ...

async def int_fn() -> int: ...

class MyController(Controller):
    path = "/controller"
    # on the controller
    dependencies = {"controller_dependency": Provide(list_fn)}

    # on the route handler
    @get(path="/handler", dependencies={"local_dependency": Provide(int_fn)})
    def my_route_handler(
        self,
        app_dependency: bool,
        router_dependency: dict,
        controller_dependency: list,
        local_dependency: int,
    ) -> None: ...

# on the router
my_router = Router(
    path="/router",
    dependencies={"router_dependency": Provide(dict_fn)},
    route_handlers=[MyController],
)

# on the app
app = Litestar(
    route_handlers=[my_router], dependencies={"app_dependency": Provide(bool_fn)}
)

The above example illustrates how dependencies are declared on the different layers of the application.

Note

Litestar needs the injected types at runtime which might clash with linter rules’ recommendation to use `TYPE_CHECKING`.

Dependencies can be either callables - sync or async functions, methods, or class instances that implement the [`object.__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "(in Python v3.14)") method, or classes. These are in turn wrapped inside an instance of the [`Provide`](https://docs.litestar.dev/latest/reference/di.html#litestar.di.Provide "litestar.di.Provide") class.

Synchronous and asynchronous callables

Both synchronous and asynchronous callables are supported. One important aspect of this is that using a synchronous function which perform blocking operations, such as I/O or computationally intensive tasks, can potentially block the main thread running the event loop, and in turn block the whole application.

To mitigate this, the `sync_to_thread` parameter can be set to `True`, which will result in the function being run in a thread pool.

If a synchronous function is non-blocking, setting `sync_to_thread` to `False` will tell Litestar that the user is sure about its behavior and the function can be treated as non-blocking.

If a synchronous function is passed, without setting an explicit `sync_to_thread` value, a warning will be raised.

Pre-requisites and scope[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#pre-requisites-and-scope "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

The pre-requisites for dependency injection are these:

1.   dependencies must be callables.

2.   dependencies can receive kwargs and a `self` arg but not positional args.

3.   the kwarg name and the dependency key must be identical.

4.   the dependency must be declared using the `Provide` class.

5.   the dependency must be in the _scope_ of the handler function.

What is _scope_ in this context? Dependencies are **isolated** to the context in which they are declared. Thus, in the above example, the `local_dependency` can only be accessed within the specific route handler on which it was declared; The `controller_dependency` is available only for route handlers on that specific controller; And the 
```
router
dependency
```
 is available only to the route handlers registered on that particular router. Only the `app_dependency` is available to all route handlers.

Dependencies with yield (cleanup step)[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#dependencies-with-yield-cleanup-step "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to simple callables, dependencies can also be (async) generator functions, which allows to execute an additional cleanup step, such as closing a connection, after the handler function has returned.

Technical details

The cleanup stage is executed **after** the handler function returns, but **before** the response is sent (in case of HTTP requests)

### A basic example[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#a-basic-example "Link to this heading")

Python 3.8+

`dependencies.py`[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id1 "Link to this code")

from typing import Dict, Generator

from litestar import Litestar, get
from litestar.di import Provide

CONNECTION = {"open": False}

def generator_function() -> Generator[Dict[str, bool], None, None]:
 """Set connection to open and close it after the handler returns."""
    CONNECTION["open"] = True
    yield CONNECTION
    CONNECTION["open"] = False

@get("/", dependencies={"conn": Provide(generator_function)})
def index(conn: Dict[str, bool]) -> Dict[str, bool]:
 """Return the current connection state."""
    return conn

app = Litestar(route_handlers=[index])

Python 3.9+

`dependencies.py`[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id2 "Link to this code")

from collections.abc import Generator

from litestar import Litestar, get
from litestar.di import Provide

CONNECTION = {"open": False}

def generator_function() -> Generator[dict[str, bool], None, None]:
 """Set connection to open and close it after the handler returns."""
    CONNECTION["open"] = True
    yield CONNECTION
    CONNECTION["open"] = False

@get("/", dependencies={"conn": Provide(generator_function)})
def index(conn: dict[str, bool]) -> dict[str, bool]:
 """Return the current connection state."""
    return conn

app = Litestar(route_handlers=[index])

If you run the code you’ll see that `CONNECTION` has been reset after the handler function returned:

from litestar.testing import TestClient
from dependencies import app, CONNECTION

with TestClient(app=app) as client:
    print(client.get("/").json())  # {"open": True}
    print(CONNECTION)  # {"open": False}

### Handling exceptions[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#handling-exceptions "Link to this heading")

If an exception occurs within the handler function, it will be raised **within** the generator, at the point where it first `yield` ed. This makes it possible to adapt behaviour of the dependency based on exceptions, for example rolling back a database session on error and committing otherwise.

Python 3.8+

`dependencies.py`[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id3 "Link to this code")

from typing import Dict, Generator

from litestar import Litestar, get
from litestar.di import Provide

STATE = {"result": None, "connection": "closed"}

def generator_function() -> Generator[str, None, None]:
 """Set the connection state to open and close it after the handler returns.

 If an error occurs, set `result` to `"error"`, else set it to `"OK"`.
 """
    try:
        STATE["connection"] = "open"
        yield "hello"
        STATE["result"] = "OK"
    except ValueError:
        STATE["result"] = "error"
    finally:
        STATE["connection"] = "closed"

@get("/{name:str}", dependencies={"message": Provide(generator_function)})
def index(name: str, message: str) -> Dict[str, str]:
 """If `name` is "John", return a message, otherwise raise an error."""
    if name == "John":
        return {name: message}
    raise ValueError()

app = Litestar(route_handlers=[index])

Python 3.9+

`dependencies.py`[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id4 "Link to this code")

from collections.abc import Generator

from litestar import Litestar, get
from litestar.di import Provide

STATE = {"result": None, "connection": "closed"}

def generator_function() -> Generator[str, None, None]:
 """Set the connection state to open and close it after the handler returns.

 If an error occurs, set `result` to `"error"`, else set it to `"OK"`.
 """
    try:
        STATE["connection"] = "open"
        yield "hello"
        STATE["result"] = "OK"
    except ValueError:
        STATE["result"] = "error"
    finally:
        STATE["connection"] = "closed"

@get("/{name:str}", dependencies={"message": Provide(generator_function)})
def index(name: str, message: str) -> dict[str, str]:
 """If `name` is "John", return a message, otherwise raise an error."""
    if name == "John":
        return {name: message}
    raise ValueError()

app = Litestar(route_handlers=[index])

from litestar.testing import TestClient
from dependencies import STATE, app

with TestClient(app=app) as client:
    response = client.get("/John")
    print(response.json())  # {"John": "hello"}
    print(STATE)  # {"result": "OK", "connection": "closed"}

    response = client.get("/Peter")
    print(response.status_code)  # 500
    print(STATE)  # {"result": "error", "connection": "closed"}

Best Practice

You should always wrap `yield` in a `try`/`finally` block, regardless of whether you want to handle exceptions, to ensure that the cleanup code is run even when exceptions occurred:

def generator_dependency():
    try:
        yield
    finally:
        ...  # cleanup code

Attention

Do not re-raise exceptions within the dependency. Exceptions caught within these dependencies will still be handled by the regular mechanisms without an explicit re-raise

Important

Exceptions raised during the cleanup step of a dependency will be re-raised in an [`ExceptionGroup`](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "(in Python v3.14)") (for Python versions < 3.11, the [exceptiongroup](https://github.com/agronholm/exceptiongroup) will be used). This happens after all dependencies have been cleaned up, so exceptions raised during cleanup of one dependencies do not affect the cleanup of other dependencies.

Dependency keyword arguments[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#dependency-keyword-arguments "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

As stated above dependencies can receive kwargs but no args. The reason for this is that dependencies are parsed using the same mechanism that parses route handler functions, and they too - like route handler functions, can have data injected into them.

In fact, you can inject the same data that you can [inject into route handlers](https://docs.litestar.dev/latest/usage/routing/handlers.html#reserved-keyword-arguments).

from litestar import Controller, patch
from litestar.di import Provide
from pydantic import BaseModel, UUID4

class User(BaseModel):
    id: UUID4
    name: str

async def retrieve_db_user(user_id: UUID4) -> User: ...

class UserController(Controller):
    path = "/user"
    dependencies = {"user": Provide(retrieve_db_user)}

    @patch(path="/{user_id:uuid}")
    async def get_user(self, user: User) -> User: ...

In the above example we have a `User` model that we are persisting into a db. The model is fetched using the helper method `retrieve_db_user` which receives a `user_id` kwarg and retrieves the corresponding `User` instance. The `UserController` class maps the `retrieve_db_user` provider to the key `user` in its `dependencies` dictionary. This in turn makes it available as a kwarg in the `get_user` method.

Dependency overrides[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#dependency-overrides "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

Because dependencies are declared at each level of the app using a string keyed dictionary, overriding dependencies is very simple:

from litestar import Controller, get
from litestar.di import Provide

def bool_fn() -> bool: ...

def dict_fn() -> dict: ...

class MyController(Controller):
    path = "/controller"
    # on the controller
    dependencies = {"some_dependency": Provide(dict_fn)}

    # on the route handler
    @get(path="/handler", dependencies={"some_dependency": Provide(bool_fn)})
    def my_route_handler(
        self,
        some_dependency: bool,
    ) -> None: ...

The lower scoped route handler function declares a dependency with the same key as the one declared on the higher scoped controller. The lower scoped dependency therefore overrides the higher scoped one.

The `Provide` class[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#the-provide-class "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

The [`Provide`](https://docs.litestar.dev/latest/reference/di.html#litestar.di.Provide "litestar.di.Provide") class is a wrapper used for dependency injection. To inject a callable you must wrap it in `Provide`:

from random import randint
from litestar import get
from litestar.di import Provide

def my_dependency() -> int:
    return randint(1, 10)

@get(
    "/some-path",
    dependencies={
        "my_dep": Provide(
            my_dependency,
        )
    },
)
def my_handler(my_dep: int) -> None: ...

Attention

If [`Provide.use_cache`](https://docs.litestar.dev/latest/reference/di.html#litestar.di.Provide "litestar.di.Provide") is `True`, the return value of the function will be memoized the first time it is called and then will be used. There is no sophisticated comparison of kwargs, LRU implementation, etc., so you should be careful when you choose to use this option. Note that dependencies will only be called once per request, even with `Provide.use_cache` set to `False`.

Dependencies within dependencies[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#dependencies-within-dependencies "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

You can inject dependencies into other dependencies - exactly like you would into regular functions.

from litestar import Litestar, get
from litestar.di import Provide
from random import randint

def first_dependency() -> int:
    return randint(1, 10)

def second_dependency(injected_integer: int) -> bool:
    return injected_integer % 2 == 0

@get("/true-or-false")
def true_or_false_handler(injected_bool: bool) -> str:
    return "its true!" if injected_bool else "nope, its false..."

app = Litestar(
    route_handlers=[true_or_false_handler],
    dependencies={
        "injected_integer": Provide(first_dependency),
        "injected_bool": Provide(second_dependency),
    },
)

Note

The rules for [dependency overrides](https://docs.litestar.dev/latest/usage/dependency-injection.html#dependency-overrides) apply here as well.

The `Dependency` function[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#the-dependency-function "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

### Dependency validation[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#dependency-validation "Link to this heading")

By default, injected dependency values are validated by Litestar, for example, this application will raise an internal server error:

Python 3.8+

Dependency validation error[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id5 "Link to this code")

from typing import Any, Dict

from litestar import Litestar, get
from litestar.di import Provide

async def provide_str() -> str:
 """Returns a string."""
    return "whoops"

@get("/", dependencies={"injected": Provide(provide_str)}, sync_to_thread=False)
def hello_world(injected: int) -> Dict[str, Any]:
 """Handler expects an `int`, but we've provided a `str`."""
    return {"hello": injected}

app = Litestar(route_handlers=[hello_world])

Python 3.9+

Dependency validation error[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id6 "Link to this code")

from typing import Any

from litestar import Litestar, get
from litestar.di import Provide

async def provide_str() -> str:
 """Returns a string."""
    return "whoops"

@get("/", dependencies={"injected": Provide(provide_str)}, sync_to_thread=False)
def hello_world(injected: int) -> dict[str, Any]:
 """Handler expects an `int`, but we've provided a `str`."""
    return {"hello": injected}

app = Litestar(route_handlers=[hello_world])

Dependency validation can be toggled using the [`Dependency`](https://docs.litestar.dev/latest/reference/params.html#litestar.params.Dependency "litestar.params.Dependency") function.

Python 3.8+

Dependency validation error[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id7 "Link to this code")

from typing import Any, Dict

from typing_extensions import Annotated

from litestar import Litestar, get
from litestar.di import Provide
from litestar.params import Dependency

async def provide_str() -> str:
 """Returns a string."""
    return "whoops"

@get("/", dependencies={"injected": Provide(provide_str)}, sync_to_thread=False)
def hello_world(injected: Annotated[int, Dependency(skip_validation=True)]) -> Dict[str, Any]:
 """Handler expects an `int`, but we've provided a `str`."""
    return {"hello": injected}

app = Litestar(route_handlers=[hello_world])

Python 3.9+

Dependency validation error[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id8 "Link to this code")

from typing import Any

from typing import Annotated

from litestar import Litestar, get
from litestar.di import Provide
from litestar.params import Dependency

async def provide_str() -> str:
 """Returns a string."""
    return "whoops"

@get("/", dependencies={"injected": Provide(provide_str)}, sync_to_thread=False)
def hello_world(injected: Annotated[int, Dependency(skip_validation=True)]) -> dict[str, Any]:
 """Handler expects an `int`, but we've provided a `str`."""
    return {"hello": injected}

app = Litestar(route_handlers=[hello_world])

This may be useful for reasons of efficiency, or if pydantic cannot validate a certain type, but use with caution!

### Dependency function as a marker[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#dependency-function-as-a-marker "Link to this heading")

The [`Dependency`](https://docs.litestar.dev/latest/reference/params.html#litestar.params.Dependency "litestar.params.Dependency") function can also be used as a marker that gives us a bit more detail about your application.

#### Exclude dependencies with default values from OpenAPI docs[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#exclude-dependencies-with-default-values-from-openapi-docs "Link to this heading")

Depending on your application design, it is possible to have a dependency declared in a handler or [`Provide`](https://docs.litestar.dev/latest/reference/di.html#litestar.di.Provide "litestar.di.Provide") function that has a default value. If the dependency isn’t provided for the route, the default should be used by the function.

Python 3.8+

Dependency with default value[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id9 "Link to this code")

from typing import Any, Dict

from litestar import Litestar, get

@get("/", sync_to_thread=False)
def hello_world(optional_dependency: int = 3) -> Dict[str, Any]:
 """Notice we haven't provided the dependency to the route.

 This is OK, because of the default value, but the parameter shows in the docs.
 """
    return {"hello": optional_dependency}

app = Litestar(route_handlers=[hello_world])

Python 3.9+

Dependency with default value[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id10 "Link to this code")

from typing import Any

from litestar import Litestar, get

@get("/", sync_to_thread=False)
def hello_world(optional_dependency: int = 3) -> dict[str, Any]:
 """Notice we haven't provided the dependency to the route.

 This is OK, because of the default value, but the parameter shows in the docs.
 """
    return {"hello": optional_dependency}

app = Litestar(route_handlers=[hello_world])

This doesn’t fail, but due to the way the application determines parameter types, it is inferred to be a query parameter.

By declaring the parameter to be a dependency, Litestar knows to exclude it from the docs:

Python 3.8+

Dependency with default value[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id11 "Link to this code")

from typing import Any, Dict

from typing_extensions import Annotated

from litestar import Litestar, get
from litestar.params import Dependency

@get("/", sync_to_thread=False)
def hello_world(optional_dependency: Annotated[int, Dependency(default=3)]) -> Dict[str, Any]:
 """Notice we haven't provided the dependency to the route.

 This is OK, because of the default value, and now the parameter is excluded from the docs.
 """
    return {"hello": optional_dependency}

app = Litestar(route_handlers=[hello_world])

Python 3.9+

Dependency with default value[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id12 "Link to this code")

from typing import Any

from typing import Annotated

from litestar import Litestar, get
from litestar.params import Dependency

@get("/", sync_to_thread=False)
def hello_world(optional_dependency: Annotated[int, Dependency(default=3)]) -> dict[str, Any]:
 """Notice we haven't provided the dependency to the route.

 This is OK, because of the default value, and now the parameter is excluded from the docs.
 """
    return {"hello": optional_dependency}

app = Litestar(route_handlers=[hello_world])

#### Early detection if a dependency isn’t provided[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#early-detection-if-a-dependency-isn-t-provided "Link to this heading")

The other side of the same coin is when a dependency isn’t provided, and no default is specified. Without the dependency marker, the parameter is assumed to be a query parameter and the route will most likely fail when accessed.

If the parameter is marked as a dependency, this allows us to fail early instead:

Python 3.8+

Dependency not provided error[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id13 "Link to this code")

from typing import Any

from typing_extensions import Annotated

from litestar import Litestar, get
from litestar.params import Dependency

@get("/")
def hello_world(non_optional_dependency: Annotated[int, Dependency()]) -> dict[str, Any]:
 """Notice we haven't provided the dependency to the route.

 This is not great, however by explicitly marking dependencies, Litestar won't let the app start.
 """
    return {"hello": non_optional_dependency}

app = Litestar(route_handlers=[hello_world])

# ImproperlyConfiguredException: 500: Explicit dependency 'non_optional_dependency' for 'hello_world' has no default
# value, or provided dependency.

Python 3.9+

Dependency not provided error[#](https://docs.litestar.dev/latest/usage/dependency-injection.html#id14 "Link to this code")

from typing import Any

from typing import Annotated

from litestar import Litestar, get
from litestar.params import Dependency

@get("/")
def hello_world(non_optional_dependency: Annotated[int, Dependency()]) -> dict[str, Any]:
 """Notice we haven't provided the dependency to the route.

 This is not great, however by explicitly marking dependencies, Litestar won't let the app start.
 """
    return {"hello": non_optional_dependency}

app = Litestar(route_handlers=[hello_world])

# ImproperlyConfiguredException: 500: Explicit dependency 'non_optional_dependency' for 'hello_world' has no default
# value, or provided dependency.
