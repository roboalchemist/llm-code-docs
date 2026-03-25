# Source: https://docs.pyinvoke.org/en/stable/api/__init__.html

Title: __init__ — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/api/__init__.html

Markdown Content:
invoke.run(_command:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _**kwargs:Any_)→Optional[[invoke.runners.Result](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result")][¶](https://docs.pyinvoke.org/en/stable/api/__init__.html#invoke.run "Permalink to this definition")
Run `command` in a subprocess and return a [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") object.

See [`Runner.run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run") for API details.

Note

This function is a convenience wrapper around Invoke’s [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") and [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") APIs.

Specifically, it creates an anonymous [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") instance and calls its [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "invoke.context.Context.run") method, which in turn defaults to using a [`Local`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local "invoke.runners.Local") runner subclass for command execution.

New in version 1.0.

invoke.sudo(_command:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _**kwargs:Any_)→Optional[[invoke.runners.Result](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result")][¶](https://docs.pyinvoke.org/en/stable/api/__init__.html#invoke.sudo "Permalink to this definition")
Run `command` in a `sudo` subprocess and return a [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") object.

See [`Context.sudo`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.sudo "invoke.context.Context.sudo") for API details, such as the `password` kwarg.

Note

This function is a convenience wrapper around Invoke’s [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") and [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") APIs.

Specifically, it creates an anonymous [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") instance and calls its [`sudo`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.sudo "invoke.context.Context.sudo") method, which in turn defaults to using a [`Local`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local "invoke.runners.Local") runner subclass for command execution (plus sudo-related bits & pieces).

New in version 1.4.
