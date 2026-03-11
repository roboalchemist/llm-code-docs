# Source: https://docs.litestar.dev/latest/usage/plugins/index.html

Title: Plugins — Litestar Framework

URL Source: https://docs.litestar.dev/latest/usage/plugins/index.html

Markdown Content:
Litestar supports a plugin system that allows you to extend the functionality of the framework.

Plugins are defined by protocols, and any type that satisfies a protocol can be included in the `plugins` argument of the [`app`](https://docs.litestar.dev/latest/reference/app.html#litestar.app.Litestar "litestar.app.Litestar").

InitPlugin[#](https://docs.litestar.dev/latest/usage/plugins/index.html#initplugin "Link to this heading")
----------------------------------------------------------------------------------------------------------

`InitPlugin` defines an interface that allows for customization of the application’s initialization process. Init plugins can define dependencies, add route handlers, configure middleware, and much more!

Implementations of these plugins must define a single method: [`on_app_init(self, app_config: AppConfig) -> AppConfig:`](https://docs.litestar.dev/latest/reference/plugins/index.html#litestar.plugins.InitPlugin.on_app_init "litestar.plugins.InitPlugin.on_app_init")

The method accepts and must return an [`AppConfig`](https://docs.litestar.dev/latest/reference/config.html#litestar.config.app.AppConfig "litestar.config.app.AppConfig") instance, which can be modified and is later used to instantiate the application.

This method is invoked after any `on_app_init` hooks have been called, and each plugin is invoked in the order that they are provided in the `plugins` argument of the [`app`](https://docs.litestar.dev/latest/reference/app.html#litestar.app.Litestar "litestar.app.Litestar"). Because of this, plugin authors should make it clear in their documentation if their plugin should be invoked before or after other plugins.

### Example[#](https://docs.litestar.dev/latest/usage/plugins/index.html#example "Link to this heading")

The following example shows a simple plugin that adds a route handler, and a dependency to the application.

Python 3.8+

`InitPlugin` implementation example[#](https://docs.litestar.dev/latest/usage/plugins/index.html#id4 "Link to this code")

from typing import Dict

from litestar import Litestar, get
from litestar.config.app import AppConfig
from litestar.di import Provide
from litestar.plugins import InitPlugin

@get("/", sync_to_thread=False)
def route_handler(name: str) -> Dict[str, str]:
    return {"hello": name}

def get_name() -> str:
    return "world"

class MyPlugin(InitPlugin):
    def on_app_init(self, app_config: AppConfig) -> AppConfig:
        app_config.dependencies["name"] = Provide(get_name, sync_to_thread=False)
        app_config.route_handlers.append(route_handler)
        return app_config

app = Litestar(plugins=[MyPlugin()])

Python 3.9+

`InitPlugin` implementation example[#](https://docs.litestar.dev/latest/usage/plugins/index.html#id5 "Link to this code")

from litestar import Litestar, get
from litestar.config.app import AppConfig
from litestar.di import Provide
from litestar.plugins import InitPlugin

@get("/", sync_to_thread=False)
def route_handler(name: str) -> dict[str, str]:
    return {"hello": name}

def get_name() -> str:
    return "world"

class MyPlugin(InitPlugin):
    def on_app_init(self, app_config: AppConfig) -> AppConfig:
        app_config.dependencies["name"] = Provide(get_name, sync_to_thread=False)
        app_config.route_handlers.append(route_handler)
        return app_config

app = Litestar(plugins=[MyPlugin()])

Run it

> curl http://127.0.0.1:8000/
{"hello":"world"}

The `MyPlugin` class is an implementation of the [`InitPlugin`](https://docs.litestar.dev/latest/reference/plugins/index.html#litestar.plugins.InitPlugin "litestar.plugins.InitPlugin"). It defines a single method, `on_app_init()`, which takes an [`AppConfig`](https://docs.litestar.dev/latest/reference/config.html#litestar.config.app.AppConfig "litestar.config.app.AppConfig") instance as an argument and returns same.

In the `on_app_init()` method, the dependency mapping is updated to include a new dependency named `"name"`, which is provided by the `get_name()` function, and `route_handlers` is updated to include the `route_handler()` function. The modified [`AppConfig`](https://docs.litestar.dev/latest/reference/config.html#litestar.config.app.AppConfig "litestar.config.app.AppConfig") instance is then returned.

SerializationPluginProtocol[#](https://docs.litestar.dev/latest/usage/plugins/index.html#serializationpluginprotocol "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

The SerializationPluginProtocol defines a contract for plugins that provide serialization functionality for data types that are otherwise unsupported by the framework.

Implementations of these plugins must define the following methods.

1.   [`supports_type(self, field_definition: FieldDefinition) -> bool:`](https://docs.litestar.dev/latest/reference/plugins/index.html#litestar.plugins.SerializationPluginProtocol "litestar.plugins.SerializationPluginProtocol")

The method takes a [`FieldDefinition`](https://docs.litestar.dev/latest/reference/typing.html#litestar.typing.FieldDefinition "litestar.typing.FieldDefinition") instance as an argument and returns a [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") indicating whether the plugin supports serialization for that type.

1.   [`create_dto_for_type(self, field_definition: FieldDefinition) -> type[AbstractDTO]:`](https://docs.litestar.dev/latest/reference/plugins/index.html#litestar.plugins.SerializationPluginProtocol.create_dto_for_type "litestar.plugins.SerializationPluginProtocol.create_dto_for_type")

This method accepts a [`FieldDefinition`](https://docs.litestar.dev/latest/reference/typing.html#litestar.typing.FieldDefinition "litestar.typing.FieldDefinition") instance as an argument and must return a [`AbstractDTO`](https://docs.litestar.dev/latest/reference/dto/base_dto.html#litestar.dto.base_dto.AbstractDTO "litestar.dto.base_dto.AbstractDTO") implementation that can be used to serialize and deserialize the type.

During application startup, if a data or return annotation is encountered that is not a supported type, is supported by the plugin, and doesn’t otherwise have a `dto` or `return_dto` defined, the plugin is used to create a DTO type for that annotation.

### Example[#](https://docs.litestar.dev/latest/usage/plugins/index.html#id2 "Link to this heading")

The following example shows the actual implementation of the `SerializationPluginProtocol` for [SQLAlchemy](https://www.sqlalchemy.org/) models that is is provided in `advanced_alchemy`.

`SerializationPluginProtocol` implementation example[#](https://docs.litestar.dev/latest/usage/plugins/index.html#id6 "Link to this code")

from  __future__  import annotations

from typing import TYPE_CHECKING

from litestar.utils import warn_deprecation

 __all__  = ("SQLAlchemySerializationPlugin",)

def  __getattr__ (attr_name: str) -> object:
    if attr_name in  __all__ :
        warn_deprecation(
            deprecated_name=f"litestar.contrib.sqlalchemy.plugins.serialization.{attr_name}",
            version="2.12",
            kind="import",
            removal_in="3.0",
            info=f"importing {attr_name} from 'litestar.contrib.sqlalchemy.plugins.serialization' is deprecated, please "
            "import it from 'litestar.plugins.sqlalchemy' instead",
        )
        from advanced_alchemy.extensions.litestar import SQLAlchemySerializationPlugin

        value = globals()[attr_name] = SQLAlchemySerializationPlugin
        return value

    raise AttributeError(f"module { __name__ !r} has no attribute {attr_name!r}")  # pragma: no cover

if TYPE_CHECKING:
    from advanced_alchemy.extensions.litestar import SQLAlchemySerializationPlugin

[`supports_type(self, field_definition: FieldDefinition) -> bool:`](https://advanced-alchemy.litestar.dev/latest/reference/extensions/litestar/index.html#advanced_alchemy.extensions.litestar.SQLAlchemySerializationPlugin.supports_type "(in advanced_alchemy)") returns a [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") indicating whether the plugin supports serialization for the given type. Specifically, we return `True` if the parsed type is either a collection of SQLAlchemy models or a single SQLAlchemy model.

[`create_dto_for_type(self, field_definition: FieldDefinition) -> type[AbstractDTO]:`](https://advanced-alchemy.litestar.dev/latest/reference/extensions/litestar/index.html#advanced_alchemy.extensions.litestar.SQLAlchemySerializationPlugin.create_dto_for_type "(in advanced_alchemy)") takes a [`FieldDefinition`](https://docs.litestar.dev/latest/reference/typing.html#litestar.typing.FieldDefinition "litestar.typing.FieldDefinition") instance as an argument and returns a [`SQLAlchemyDTO`](https://advanced-alchemy.litestar.dev/latest/reference/extensions/litestar/index.html#advanced_alchemy.extensions.litestar.SQLAlchemyDTO "(in advanced_alchemy)") subclass and includes some logic that may be interesting to potential serialization plugin authors.

The first thing the method does is check if the parsed type is a collection of SQLAlchemy models or a single SQLAlchemy model, retrieves the model type in either case and assigns it to the `annotation` variable.

The method then checks if `annotation` is already in the `_type_dto_map` dictionary. If it is, it returns the corresponding DTO type. This is done to ensure that multiple [`SQLAlchemyDTO`](https://advanced-alchemy.litestar.dev/latest/reference/extensions/litestar/index.html#advanced_alchemy.extensions.litestar.SQLAlchemyDTO "(in advanced_alchemy)") subtypes are not created for the same model.

If the annotation is not in the `_type_dto_map` dictionary, the method creates a new DTO type for the annotation, adds it to the `_type_dto_map` dictionary, and returns it.

DIPlugin[#](https://docs.litestar.dev/latest/usage/plugins/index.html#diplugin "Link to this heading")
------------------------------------------------------------------------------------------------------

[`DIPlugin`](https://docs.litestar.dev/latest/reference/plugins/index.html#litestar.plugins.DIPlugin "litestar.plugins.DIPlugin") can be used to extend Litestar’s dependency injection by providing information about injectable types.

Its main purpose it to facilitate the injection of callables with unknown signatures, for example Pydantic’s `BaseModel` classes; These are not supported natively since, while they are callables, their type information is not contained within their callable signature (their [`__init__()`](https://docs.litestar.dev/latest/reference/contrib/jinja.html#litestar.contrib.jinja.JinjaTemplateEngine.__init__ "litestar.contrib.jinja.JinjaTemplateEngine.__init__") method).

Python 3.8+

Dynamically generating signature information for a custom type[#](https://docs.litestar.dev/latest/usage/plugins/index.html#id7 "Link to this code")

from inspect import Parameter, Signature
from typing import Any, Dict, Tuple

from litestar import Litestar, get
from litestar.di import Provide
from litestar.plugins import DIPlugin

class MyBaseType:
    def  __init__ (self, param):
        self.param = param

class MyDIPlugin(DIPlugin):
    def has_typed_init(self, type_: Any) -> bool:
        return issubclass(type_, MyBaseType)

    def get_typed_init(self, type_: Any) -> Tuple[Signature, Dict[str, Any]]:
        signature = Signature([Parameter(name="param", kind=Parameter.POSITIONAL_OR_KEYWORD)])
        annotations = {"param": str}
        return signature, annotations

@get("/", dependencies={"injected": Provide(MyBaseType, sync_to_thread=False)})
async def handler(injected: MyBaseType) -> str:
    return injected.param

app = Litestar(route_handlers=[handler], plugins=[MyDIPlugin()])

Python 3.9+

Dynamically generating signature information for a custom type[#](https://docs.litestar.dev/latest/usage/plugins/index.html#id8 "Link to this code")

from inspect import Parameter, Signature
from typing import Any

from litestar import Litestar, get
from litestar.di import Provide
from litestar.plugins import DIPlugin

class MyBaseType:
    def  __init__ (self, param):
        self.param = param

class MyDIPlugin(DIPlugin):
    def has_typed_init(self, type_: Any) -> bool:
        return issubclass(type_, MyBaseType)

    def get_typed_init(self, type_: Any) -> tuple[Signature, dict[str, Any]]:
        signature = Signature([Parameter(name="param", kind=Parameter.POSITIONAL_OR_KEYWORD)])
        annotations = {"param": str}
        return signature, annotations

@get("/", dependencies={"injected": Provide(MyBaseType, sync_to_thread=False)})
async def handler(injected: MyBaseType) -> str:
    return injected.param

app = Litestar(route_handlers=[handler], plugins=[MyDIPlugin()])

Run it

> curl http://127.0.0.1:8000/?param=hello
hello

*   [Flash Messages](https://docs.litestar.dev/latest/usage/plugins/flash_messages.html)
*   [Problem Details](https://docs.litestar.dev/latest/usage/plugins/problem_details.html)

ReceiveRoutePlugin[#](https://docs.litestar.dev/latest/usage/plugins/index.html#receiverouteplugin "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

[`ReceiveRoutePlugin`](https://docs.litestar.dev/latest/reference/plugins/index.html#litestar.plugins.ReceiveRoutePlugin "litestar.plugins.ReceiveRoutePlugin") allows you to receive routes as they are registered on the application. This can be useful for plugins that need to perform actions based on the routes being added, such as generating documentation, validating route configurations, or tracking route statistics.

Implementations of this plugin must define a single method: [`receive_route(self, route: BaseRoute) -> None:`](https://docs.litestar.dev/latest/reference/plugins/index.html#litestar.plugins.ReceiveRoutePlugin.receive_route "litestar.plugins.ReceiveRoutePlugin.receive_route")

The method receives a [`BaseRoute`](https://docs.litestar.dev/latest/reference/routes.html#litestar.routes.BaseRoute "litestar.routes.BaseRoute") instance as routes are registered on the application. This happens during the application initialization process, after routes are created but before the application starts.

### Example[#](https://docs.litestar.dev/latest/usage/plugins/index.html#id3 "Link to this heading")

The following example shows a simple plugin that logs information about each route as it’s registered:

from litestar.plugins import ReceiveRoutePlugin
from litestar.routes import BaseRoute

class RouteLoggerPlugin(ReceiveRoutePlugin):
    def receive_route(self, route: BaseRoute) -> None:
        print(f"Route registered: {route.path} [{', '.join(route.methods)}]")
