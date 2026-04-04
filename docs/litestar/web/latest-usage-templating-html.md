# Source: https://docs.litestar.dev/latest/usage/templating.html

Title: Templating — Litestar Framework

URL Source: https://docs.litestar.dev/latest/usage/templating.html

Markdown Content:
Litestar has built-in support for [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/) , [Mako](https://www.makotemplates.org/) and [Minijinja](https://github.com/mitsuhiko/minijinja/tree/main/minijinja-py) template engines, as well as abstractions to make use of any template engine you wish.

Template engines[#](https://docs.litestar.dev/latest/usage/templating.html#template-engines "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

To stay lightweight, a Litestar installation does not include the _Jinja_, _Mako_ or _Minijinja_ libraries themselves. Before you can start using them, you have to install it via the respective extra:

Jinja

pip install 'litestar[jinja]'

Mako

pip install 'litestar[mako]'

MiniJinja

pip install 'litestar[minijinja]'

Tip

_Jinja_ is included in the `standard` extra. If you installed Litestar using `litestar[standard]`, you do not need to explicitly add the `jinja` extra.

### Registering a template engine[#](https://docs.litestar.dev/latest/usage/templating.html#registering-a-template-engine "Link to this heading")

To register one of the built-in template engines you simply need to pass it to the Litestar constructor:

Jinja

from pathlib import Path

from litestar import Litestar
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig

app = Litestar(
    route_handlers=[],
    template_config=TemplateConfig(
        directory=Path("templates"),
        engine=JinjaTemplateEngine,
    ),
)

Mako

from pathlib import Path

from litestar import Litestar
from litestar.contrib.mako import MakoTemplateEngine
from litestar.template.config import TemplateConfig

app = Litestar(
    route_handlers=[],
    template_config=TemplateConfig(
        directory=Path("templates"),
        engine=MakoTemplateEngine,
    ),
)

MiniJinja

from pathlib import Path

from litestar import Litestar
from litestar.contrib.minijinja import MiniJinjaTemplateEngine
from litestar.template.config import TemplateConfig

app = Litestar(
    route_handlers=[],
    template_config=TemplateConfig(
        directory=Path("templates"),
        engine=MiniJinjaTemplateEngine,
    ),
)

Note

The `directory` parameter passed to [`TemplateConfig`](https://docs.litestar.dev/latest/reference/template.html#litestar.template.TemplateConfig "litestar.template.TemplateConfig") can be either a directory or list of directories to use for loading templates.

### Registering a Custom Template Engine[#](https://docs.litestar.dev/latest/usage/templating.html#registering-a-custom-template-engine "Link to this heading")

The above example will create a jinja Environment instance, but you can also pass in your own instance.

from litestar import Litestar
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template import TemplateConfig
from jinja2 import Environment, DictLoader

my_custom_env = Environment(loader=DictLoader({"index.html": "Hello {{name}}!"}))
app = Litestar(
    template_config=TemplateConfig(
        instance=JinjaTemplateEngine.from_environment(my_custom_env)
    )
)

Note

The `instance` parameter passed to [`TemplateConfig`](https://docs.litestar.dev/latest/reference/template.html#litestar.template.TemplateConfig "litestar.template.TemplateConfig") can not be used in conjunction with the `directory` parameter, if you choose to use instance you’re fully responsible on the engine creation.

### Defining a custom template engine[#](https://docs.litestar.dev/latest/usage/templating.html#defining-a-custom-template-engine "Link to this heading")

If you wish to use another templating engine, you can easily do so by implementing [`TemplateEngineProtocol`](https://docs.litestar.dev/latest/reference/template.html#litestar.template.TemplateEngineProtocol "litestar.template.TemplateEngineProtocol"). This class accepts a generic argument which should be the template class, and it specifies two methods:

Python 3.8+

from typing import Protocol, Union, List
from pydantic import DirectoryPath

# the template class of the respective library
from some_lib import SomeTemplate

class TemplateEngineProtocol(Protocol[SomeTemplate]):
    def  __init__ (self, directory: Union[DirectoryPath, List[DirectoryPath]]) -> None:
 """Builds a template engine."""
        ...

    def get_template(self, template_name: str) -> SomeTemplate:
 """Loads the template with template_name and returns it."""
        ...

Python 3.9+

from typing import Protocol, Union
from pydantic import DirectoryPath

# the template class of the respective library
from some_lib import SomeTemplate

class TemplateEngineProtocol(Protocol[SomeTemplate]):
    def  __init__ (self, directory: Union[DirectoryPath, list[DirectoryPath]]) -> None:
 """Builds a template engine."""
        ...

    def get_template(self, template_name: str) -> SomeTemplate:
 """Loads the template with template_name and returns it."""
        ...

Python 3.10+

from typing import Protocol
from pydantic import DirectoryPath

# the template class of the respective library
from some_lib import SomeTemplate

class TemplateEngineProtocol(Protocol[SomeTemplate]):
    def  __init__ (self, directory: DirectoryPath | list[DirectoryPath]) -> None:
 """Builds a template engine."""
        ...

    def get_template(self, template_name: str) -> SomeTemplate:
 """Loads the template with template_name and returns it."""
        ...

Once you have your custom engine you can register it as you would the built-in engines.

### Accessing the template engine instance[#](https://docs.litestar.dev/latest/usage/templating.html#accessing-the-template-engine-instance "Link to this heading")

If you need to access the template engine instance, you can do so via the [`TemplateConfig.engine`](https://docs.litestar.dev/latest/reference/template.html#litestar.template.TemplateConfig "litestar.template.TemplateConfig") attribute:

Jinja

from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig

template_config = TemplateConfig(engine=JinjaTemplateEngine, directory="templates")

Mako

from litestar.contrib.mako import MakoTemplateEngine
from litestar.template.config import TemplateConfig

template_config = TemplateConfig(engine=MakoTemplateEngine, directory="templates")

MiniJinja

from litestar.contrib.minijinja import MiniJinjaTemplateEngine
from litestar.template.config import TemplateConfig

template_config = TemplateConfig(engine=MiniJinjaTemplateEngine, directory="templates")

Template responses[#](https://docs.litestar.dev/latest/usage/templating.html#template-responses "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

Once you have a template engine registered you can return [`templates responses`](https://docs.litestar.dev/latest/reference/response/index.html#litestar.response.Template "litestar.response.Template") from your route handlers:

Jinja

from pathlib import Path

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response import Template
from litestar.template.config import TemplateConfig

@get(path="/{template_type: str}", sync_to_thread=False)
def index(name: str, template_type: str) -> Template:
    if template_type == "file":
        return Template(template_name="hello.html.jinja2", context={"name": name})
    elif template_type == "string":
        return Template(template_str="Hello <strong>Jinja</strong> using strings", context={"name": name})

app = Litestar(
    route_handlers=[index],
    template_config=TemplateConfig(
        directory=Path( __file__ ).parent / "templates",
        engine=JinjaTemplateEngine,
    ),
)

Mako

from  __future__  import annotations

from pathlib import Path

from litestar import Litestar, get
from litestar.contrib.mako import MakoTemplateEngine
from litestar.response import Template
from litestar.template.config import TemplateConfig

@get(path="/{template_type: str}", sync_to_thread=False)
def index(name: str, template_type: str) -> Template:
    if template_type == "file":
        return Template(template_name="hello.html.mako", context={"name": name})
    elif template_type == "string":
        return Template(template_str="Hello <strong>Mako</strong> using strings", context={"name": name})

app = Litestar(
    route_handlers=[index],
    template_config=TemplateConfig(
        directory=Path( __file__ ).parent / "templates",
        engine=MakoTemplateEngine,
    ),
)

MiniJinja

from  __future__  import annotations

from pathlib import Path

from litestar import Litestar, get
from litestar.contrib.minijinja import MiniJinjaTemplateEngine
from litestar.response import Template
from litestar.template.config import TemplateConfig

@get(path="/{template_type: str}", sync_to_thread=False)
def index(name: str, template_type: str) -> Template:
    if template_type == "file":
        return Template(template_name="hello.html.minijinja", context={"name": name})
    elif template_type == "string":
        return Template(template_str="Hello <strong>Minijinja</strong> using strings", context={"name": name})

app = Litestar(
    route_handlers=[index],
    template_config=TemplateConfig(
        directory=Path( __file__ ).parent / "templates",
        engine=MiniJinjaTemplateEngine,
    ),
)

*   `name` is the name of the template file within on of the specified directories. If no file with that name is found, a [`TemplateNotFoundException`](https://docs.litestar.dev/latest/reference/exceptions.html#litestar.exceptions.TemplateNotFoundException "litestar.exceptions.TemplateNotFoundException") exception will be raised.

*   `context` is a dictionary containing arbitrary data that will be passed to the template engine’s `render` method. For Jinja and Mako, this data will be available in the [template context](https://docs.litestar.dev/latest/usage/templating.html#template-context)

Template Files vs. Strings[#](https://docs.litestar.dev/latest/usage/templating.html#template-files-vs-strings "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

When you define a template response, you can either pass a template file name or a string containing the template. The latter is useful if you want to define the template inline for small templates or [HTMX](https://docs.litestar.dev/latest/usage/htmx.html) responses for example.

File name

Template via file[#](https://docs.litestar.dev/latest/usage/templating.html#id6 "Link to this code")

@get()
async def example() -> Template:
    return Template(template_name="test.html", context={"hello": "world"})

String

Template via string[#](https://docs.litestar.dev/latest/usage/templating.html#id7 "Link to this code")

@get()
async def example() -> Template:
    template_string = "{{ hello }}"
    return Template(template_str=template_string, context={"hello": "world"})

Template context[#](https://docs.litestar.dev/latest/usage/templating.html#id1 "Link to this heading")
------------------------------------------------------------------------------------------------------

Both [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/) and [Mako](https://www.makotemplates.org/) support passing a context object to the template as well as defining callables that will be available inside the template.

### Accessing the request instance[#](https://docs.litestar.dev/latest/usage/templating.html#accessing-the-request-instance "Link to this heading")

The current [`Request`](https://docs.litestar.dev/latest/reference/connection.html#litestar.connection.Request "litestar.connection.request.Request") is available within the template context under `request`, which also provides access to the [app instance](https://docs.litestar.dev/latest/usage/applications.html).

Accessing `app.state.key` for example would look like this: <strong>check_context_key: </strong>{{ check_context_key() }}

Jinja

<html>
    <body>
        <div>
            <span>My state value: {{request.app.state.some_key}}</span>
        </div>
    </body>
</html>

Mako

html
<html>
    <body>
        <div>
            <span>My state value: ${request.app.state.some_key}</span>
        </div>
    </body>
</html>

MiniJinja

<html>
    <body>
        <div>
            <span>My state value: {{request.app.state.some_key}}</span>
        </div>
    </body>
</html>

### Adding CSRF inputs[#](https://docs.litestar.dev/latest/usage/templating.html#adding-csrf-inputs "Link to this heading")

If you want to add a hidden `<input>` tag containing a [CSRF token](https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks#cross-site_request_forgery_csrf), you first need to configure [CSRF protection](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#csrf). With that in place, you can now insert the CSRF input field inside an HTML form:

Jinja

<html>
    <body>
        <div>
            <form action="https://myserverurl.com/some-endpoint" method="post">
                {{ csrf_input | safe }}
                <label for="fname">First name:</label><br>
                <input type="text" id="fname" name="fname">
                <label for="lname">Last name:</label><br>
                <input type="text" id="lname" name="lname">
            </form>
        </div>
    </body>
</html>

Mako

<html>
    <body>
        <div>
            <form action="https://myserverurl.com/some-endpoint" method="post">
                ${csrf_input | n}
                <label for="fname">First name:</label><br>
                <input type="text" id="fname" name="fname">
                <label for="lname">Last name:</label><br>
                <input type="text" id="lname" name="lname">
            </form>
        </div>
    </body>
</html>

MiniJinja

<html>
    <body>
        <div>
            <form action="https://myserverurl.com/some-endpoint" method="post">
                {{ csrf_input | safe}}
                <label for="fname">First name:</label><br>
                <input type="text" id="fname" name="fname">
                <label for="lname">Last name:</label><br>
                <input type="text" id="lname" name="lname">
            </form>
        </div>
    </body>
</html>

The input holds a CSRF token as its value and is hidden so users cannot see or interact with it. The token is sent back to the server when the form is submitted, and is checked by the CSRF middleware.

Note

The csrf_input must be marked as safe in order to ensure that it does not get escaped.

### Passing template context[#](https://docs.litestar.dev/latest/usage/templating.html#passing-template-context "Link to this heading")

Passing context to the template is very simple - its one of the kwargs expected by the [`Template`](https://docs.litestar.dev/latest/reference/response/index.html#litestar.response.Template "litestar.response.Template") container, so simply pass a string keyed dictionary of values:

from litestar import get
from litestar.response import Template

@get(path="/info")
def info() -> Template:
    return Template(template_name="info.html", context={"numbers": "1234567890"})

Template callables[#](https://docs.litestar.dev/latest/usage/templating.html#template-callables "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

Both [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/) and [Mako](https://www.makotemplates.org/) allow users to define custom callables that are ran inside the template. Litestar builds on this and offers some functions out of the box.

### Built-in callables[#](https://docs.litestar.dev/latest/usage/templating.html#built-in-callables "Link to this heading")

`url_for`
To access urls for route handlers, you can use the `url_for` function. Its signature and behaviour match those of [`route_reverse`](https://docs.litestar.dev/latest/reference/app.html#litestar.app.Litestar.route_reverse "litestar.app.Litestar.route_reverse"). More details about route handler indexing can be found [here](https://docs.litestar.dev/latest/usage/routing/handlers.html#route-handler-indexing).

`csrf_token`
This function returns the request’s unique [CSRF token](https://docs.litestar.dev/latest/usage/middleware/builtin-middleware.html#csrf) You can use this if you wish to insert the `csrf_token` into non-HTML based templates, or insert it into HTML templates not using a hidden input field but by some other means, for example inside a special `<meta>` tag.

`url_for_static_asset`
URLs for static files can be created using the `url_for_static_asset` function. It’s signature and behaviour are identical to [`app.url_for_static_asset`](https://docs.litestar.dev/latest/reference/app.html#litestar.app.Litestar.url_for_static_asset "litestar.app.Litestar.url_for_static_asset").

### Registering template callables[#](https://docs.litestar.dev/latest/usage/templating.html#registering-template-callables "Link to this heading")

The [`TemplateEngineProtocol`](https://docs.litestar.dev/latest/reference/template.html#litestar.template.TemplateEngineProtocol "litestar.template.base.TemplateEngineProtocol") specifies the method `register_template_callable` that allows defining a custom callable on a template engine. This method is implemented for the two built in engines, and it can be used to register callables that will be injected into the template. The callable should expect one argument - the context dictionary. It can be any callable - a function, method, or class that defines the call method. For example:

Jinja

Python 3.8+

`template_functions.py`[#](https://docs.litestar.dev/latest/usage/templating.html#id8 "Link to this code")

from pathlib import Path
from typing import Any, Dict

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response import Template
from litestar.template.config import TemplateConfig

def my_template_function(ctx: Dict[str, Any]) -> str:
    return ctx.get("my_context_key", "nope")

def register_template_callables(engine: JinjaTemplateEngine) -> None:
    engine.register_template_callable(
        key="check_context_key",
        template_callable=my_template_function,
    )

template_config = TemplateConfig(
    directory=Path( __file__ ).parent / "templates",
    engine=JinjaTemplateEngine,
    engine_callback=register_template_callables,
)

@get("/", sync_to_thread=False)
def index() -> Template:
    return Template(template_name="index.html.jinja2")

app = Litestar(
    route_handlers=[index],
    template_config=template_config,
)

Python 3.9+

`template_functions.py`[#](https://docs.litestar.dev/latest/usage/templating.html#id9 "Link to this code")

from pathlib import Path
from typing import Any

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response import Template
from litestar.template.config import TemplateConfig

def my_template_function(ctx: dict[str, Any]) -> str:
    return ctx.get("my_context_key", "nope")

def register_template_callables(engine: JinjaTemplateEngine) -> None:
    engine.register_template_callable(
        key="check_context_key",
        template_callable=my_template_function,
    )

template_config = TemplateConfig(
    directory=Path( __file__ ).parent / "templates",
    engine=JinjaTemplateEngine,
    engine_callback=register_template_callables,
)

@get("/", sync_to_thread=False)
def index() -> Template:
    return Template(template_name="index.html.jinja2")

app = Litestar(
    route_handlers=[index],
    template_config=template_config,
)

`templates/index.html.jinja2`[#](https://docs.litestar.dev/latest/usage/templating.html#id10 "Link to this code")

<strong>check_context_key: </strong>{{ check_context_key() }}

Mako

Python 3.8+

`template_functions.py`[#](https://docs.litestar.dev/latest/usage/templating.html#id11 "Link to this code")

from pathlib import Path
from typing import Any, Dict

from litestar import Litestar, get
from litestar.contrib.mako import MakoTemplateEngine
from litestar.response import Template
from litestar.template.config import TemplateConfig

def my_template_function(ctx: Dict[str, Any]) -> str:
    return ctx.get("my_context_key", "nope")

def register_template_callables(engine: MakoTemplateEngine) -> None:
    engine.register_template_callable(
        key="check_context_key",
        template_callable=my_template_function,
    )

template_config = TemplateConfig(
    directory=Path( __file__ ).parent / "templates",
    engine=MakoTemplateEngine,
    engine_callback=register_template_callables,
)

@get("/", sync_to_thread=False)
def index() -> Template:
    return Template(template_name="index.html.mako")

app = Litestar(
    route_handlers=[index],
    template_config=template_config,
)

Python 3.9+

`template_functions.py`[#](https://docs.litestar.dev/latest/usage/templating.html#id12 "Link to this code")

from pathlib import Path
from typing import Any

from litestar import Litestar, get
from litestar.contrib.mako import MakoTemplateEngine
from litestar.response import Template
from litestar.template.config import TemplateConfig

def my_template_function(ctx: dict[str, Any]) -> str:
    return ctx.get("my_context_key", "nope")

def register_template_callables(engine: MakoTemplateEngine) -> None:
    engine.register_template_callable(
        key="check_context_key",
        template_callable=my_template_function,
    )

template_config = TemplateConfig(
    directory=Path( __file__ ).parent / "templates",
    engine=MakoTemplateEngine,
    engine_callback=register_template_callables,
)

@get("/", sync_to_thread=False)
def index() -> Template:
    return Template(template_name="index.html.mako")

app = Litestar(
    route_handlers=[index],
    template_config=template_config,
)

`templates/index.html.mako`[#](https://docs.litestar.dev/latest/usage/templating.html#id13 "Link to this code")

<strong>check_context_key: </strong>${ check_context_key() }

Minijinja

`template_functions.py`[#](https://docs.litestar.dev/latest/usage/templating.html#id14 "Link to this code")

from pathlib import Path

from litestar import Litestar, get
from litestar.contrib.minijinja import MiniJinjaTemplateEngine, StateProtocol
from litestar.response import Template
from litestar.template.config import TemplateConfig

def my_template_function(ctx: StateProtocol) -> str:
    return ctx.lookup("my_context_key") or "nope"

def register_template_callables(engine: MiniJinjaTemplateEngine) -> None:
    engine.register_template_callable(key="check_context_key", template_callable=my_template_function)

template_config = TemplateConfig(
    directory=Path( __file__ ).parent / "templates",
    engine=MiniJinjaTemplateEngine,
    engine_callback=register_template_callables,
)

@get("/", sync_to_thread=False)
def index() -> Template:
    return Template(template_name="index.html.minijinja")

app = Litestar(route_handlers=[index], template_config=template_config)

`templates/index.html.minijinja`[#](https://docs.litestar.dev/latest/usage/templating.html#id15 "Link to this code")

<strong>check_context_key: </strong>{{ check_context_key() }}

Run the example with `uvicorn template_functions:app` , visit [http://127.0.0.1:8000](http://127.0.0.1:8000/), and you’ll see

![Image 1: Template engine callable example](https://docs.litestar.dev/latest/_images/template_engine_callable.png)
