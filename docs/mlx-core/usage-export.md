::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
:::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-bars}
:::
::::

:::::: header-article-items__end
::::: header-article-item
:::: article-header-buttons
[[
]{.btn__icon-container}](https://github.com/ml-explore/mlx "Source repository"){.btn
.btn-sm .btn-source-repository-button target="_blank"
bs-placement="bottom" bs-toggle="tooltip"}

::: {.dropdown .dropdown-download-buttons}

- [[ ]{.btn__icon-container}
  [.rst]{.btn__text-container}](../_sources/usage/export.rst "Download source file"){.btn
  .btn-sm .btn-download-source-button .dropdown-item target="_blank"
  bs-placement="left" bs-toggle="tooltip"}
- [ ]{.btn__icon-container} [.pdf]{.btn__text-container}
:::

[ ]{.btn__icon-container}

[]{.fa-solid .fa-list}
::::
:::::
::::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}
# Exporting Functions

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Basics of Exporting](#basics-of-exporting){.reference .internal
  .nav-link}
- [Exporting Modules](#exporting-modules){.reference .internal
  .nav-link}
- [Exporting with a Callback](#exporting-with-a-callback){.reference
  .internal .nav-link}
- [Shapeless Exports](#shapeless-exports){.reference .internal
  .nav-link}
- [Exporting Multiple Traces](#exporting-multiple-traces){.reference
  .internal .nav-link}
- [Transformations with Imported
  Functions](#transformations-with-imported-functions){.reference
  .internal .nav-link}
- [Importing Functions in C++](#importing-functions-in-c){.reference
  .internal .nav-link}
- [More Examples](#more-examples){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::::::::: {#exporting-functions .section}
[]{#export-usage}

# Exporting Functions[\#](#exporting-functions "Link to this heading"){.headerlink}

MLX has an API to export and import functions to and from a file. This
lets you run computations written in one MLX front-end (e.g. Python) in
another MLX front-end (e.g. C++).

This guide walks through the basics of the MLX export API with some
examples. To see the full list of functions check-out the [[API
documentation]{.std .std-ref}](../python/export.html#export){.reference
.internal}.

::::::::::: {#basics-of-exporting .section}
## Basics of Exporting[\#](#basics-of-exporting "Link to this heading"){.headerlink}

Let's start with a simple example:

:::: {.highlight-python .notranslate}
::: highlight
    def fun(x, y):
      return x + y

    x = mx.array(1.0)
    y = mx.array(1.0)
    mx.export_function("add.mlxfn", fun, x, y)
:::
::::

To export a function, provide sample input arrays that the function can
be called with. The data doesn't matter, but the shapes and types of the
arrays do. In the above example we exported [`fun`{.docutils .literal
.notranslate}]{.pre} with two [`float32`{.docutils .literal
.notranslate}]{.pre} scalar arrays. We can then import the function and
run it:

:::: {.highlight-python .notranslate}
::: highlight
    add_fun = mx.import_function("add.mlxfn")

    out, = add_fun(mx.array(1.0), mx.array(2.0))
    # Prints: array(3, dtype=float32)
    print(out)

    out, = add_fun(mx.array(1.0), mx.array(3.0))
    # Prints: array(4, dtype=float32)
    print(out)

    # Raises an exception
    add_fun(mx.array(1), mx.array(3.0))

    # Raises an exception
    add_fun(mx.array([1.0, 2.0]), mx.array(3.0))
:::
::::

Notice the third and fourth calls to [`add_fun`{.docutils .literal
.notranslate}]{.pre} raise exceptions because the shapes and types of
the inputs are different than the shapes and types of the example inputs
we exported the function with.

Also notice that even though the original [`fun`{.docutils .literal
.notranslate}]{.pre} returns a single output array, the imported
function always returns a tuple of one or more arrays.

The inputs to [[`export_function()`{.xref .py .py-func .docutils
.literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.export_function.html#mlx.core.export_function "mlx.core.export_function"){.reference
.internal} and to an imported function can be specified as variable
positional arguments or as a tuple of arrays:

:::: {.highlight-python .notranslate}
::: highlight
    def fun(x, y):
      return x + y

    x = mx.array(1.0)
    y = mx.array(1.0)

    # Both arguments to fun are positional
    mx.export_function("add.mlxfn", fun, x, y)

    # Same as above
    mx.export_function("add.mlxfn", fun, (x, y))

    imported_fun = mx.import_function("add.mlxfn")

    # Ok
    out, = imported_fun(x, y)

    # Also ok
    out, = imported_fun((x, y))
:::
::::

You can pass example inputs to functions as positional or keyword
arguments. If you use keyword arguments to export the function, then you
have to use the same keyword arguments when calling the imported
function.

:::: {.highlight-python .notranslate}
::: highlight
    def fun(x, y):
      return x + y

    # One argument to fun is positional, the other is a kwarg
    mx.export_function("add.mlxfn", fun, x, y=y)

    imported_fun = mx.import_function("add.mlxfn")

    # Ok
    out, = imported_fun(x, y=y)

    # Also ok
    out, = imported_fun((x,), {"y": y})

    # Raises since the keyword argument is missing
    out, = imported_fun(x, y)

    # Raises since the keyword argument has the wrong key
    out, = imported_fun(x, z=y)
:::
::::
:::::::::::

:::::::: {#exporting-modules .section}
## Exporting Modules[\#](#exporting-modules "Link to this heading"){.headerlink}

An [[`mlx.nn.Module`{.xref .py .py-obj .docutils .literal
.notranslate}]{.pre}](../python/nn/module.html#mlx.nn.Module "mlx.nn.Module"){.reference
.internal} can be exported with or without the parameters included in
the exported function. Here's an example:

:::: {.highlight-python .notranslate}
::: highlight
    model = nn.Linear(4, 4)
    mx.eval(model.parameters())

    def call(x):
       return model(x)

    mx.export_function("model.mlxfn", call, mx.zeros(4))
:::
::::

In the above example, the [[`mlx.nn.Linear`{.xref .py .py-obj .docutils
.literal
.notranslate}]{.pre}](../python/nn/_autosummary/mlx.nn.Linear.html#mlx.nn.Linear "mlx.nn.Linear"){.reference
.internal} module is exported. Its parameters are also saved to the
[`model.mlxfn`{.docutils .literal .notranslate}]{.pre} file.

::: {.admonition .note}
Note

For enclosed arrays inside an exported function, be extra careful to
ensure they are evaluated. The computation graph that gets exported will
include the computation that produces enclosed inputs.

If the above example was missing [`mx.eval(model.parameters()`{.docutils
.literal .notranslate}]{.pre}, the exported function would include the
random initialization of the [[`mlx.nn.Module`{.xref .py .py-obj
.docutils .literal
.notranslate}]{.pre}](../python/nn/module.html#mlx.nn.Module "mlx.nn.Module"){.reference
.internal} parameters.
:::

If you only want to export the [`Module.__call__`{.docutils .literal
.notranslate}]{.pre} function without the parameters, pass them as
inputs to the [`call`{.docutils .literal .notranslate}]{.pre} wrapper:

:::: {.highlight-python .notranslate}
::: highlight
    model = nn.Linear(4, 4)
    mx.eval(model.parameters())

    def call(x, **params):
      # Set the model's parameters to the input parameters
      model.update(tree_unflatten(list(params.items())))
      return model(x)

    params = tree_flatten(model.parameters(), destination={})
    mx.export_function("model.mlxfn", call, (mx.zeros(4),), params)
:::
::::
::::::::

::::: {#exporting-with-a-callback .section}
## Exporting with a Callback[\#](#exporting-with-a-callback "Link to this heading"){.headerlink}

To inspect the exported graph, you can pass a callback instead of a file
path to [[`export_function()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.export_function.html#mlx.core.export_function "mlx.core.export_function"){.reference
.internal}.

:::: {.highlight-python .notranslate}
::: highlight
    def fun(x):
      return x.astype(mx.int32)

    def callback(args):
      print(args)

    mx.export_function(callback, fun, mx.array([1.0, 2.0]))
:::
::::

The argument to the callback ([`args`{.docutils .literal
.notranslate}]{.pre}) is a dictionary which includes a [`type`{.docutils
.literal .notranslate}]{.pre} field. The possible types are:

- [`"inputs"`{.docutils .literal .notranslate}]{.pre}: The ordered
  positional inputs to the exported function

- [`"keyword_inputs"`{.docutils .literal .notranslate}]{.pre}: The
  keyword specified inputs to the exported function

- [`"outputs"`{.docutils .literal .notranslate}]{.pre}: The ordered
  outputs of the exported function

- [`"constants"`{.docutils .literal .notranslate}]{.pre}: Any graph
  constants

- [`"primitives"`{.docutils .literal .notranslate}]{.pre}: Inner graph
  nodes representating the operations

Each type has additional fields in the [`args`{.docutils .literal
.notranslate}]{.pre} dictionary.
:::::

::::: {#shapeless-exports .section}
## Shapeless Exports[\#](#shapeless-exports "Link to this heading"){.headerlink}

Just like [[`compile()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.compile.html#mlx.core.compile "mlx.core.compile"){.reference
.internal}, functions can also be exported for dynamically shaped
inputs. Pass [`shapeless=True`{.docutils .literal .notranslate}]{.pre}
to [[`export_function()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.export_function.html#mlx.core.export_function "mlx.core.export_function"){.reference
.internal} or [[`exporter()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.exporter.html#mlx.core.exporter "mlx.core.exporter"){.reference
.internal} to export a function which can be used for inputs with
variable shapes:

:::: {.highlight-python .notranslate}
::: highlight
    mx.export_function("fun.mlxfn", mx.abs, mx.array([0.0]), shapeless=True)
    imported_abs = mx.import_function("fun.mlxfn")

    # Ok
    out, = imported_abs(mx.array([-1.0]))

    # Also ok
    out, = imported_abs(mx.array([-1.0, -2.0]))
:::
::::

With [`shapeless=False`{.docutils .literal .notranslate}]{.pre} (which
is the default), the second call to [`imported_abs`{.docutils .literal
.notranslate}]{.pre} would raise an exception with a shape mismatch.

Shapeless exporting works the same as shapeless compilation and should
be used carefully. See the [[documentation on shapeless
compilation]{.std .std-ref}](compile.html#shapeless-compile){.reference
.internal} for more information.
:::::

::::: {#exporting-multiple-traces .section}
## Exporting Multiple Traces[\#](#exporting-multiple-traces "Link to this heading"){.headerlink}

In some cases, functions build different computation graphs for
different input arguments. A simple way to manage this is to export to a
new file with each set of inputs. This is a fine option in many cases.
But it can be suboptimal if the exported functions have a large amount
of duplicate constant data (for example the parameters of a
[[`mlx.nn.Module`{.xref .py .py-obj .docutils .literal
.notranslate}]{.pre}](../python/nn/module.html#mlx.nn.Module "mlx.nn.Module"){.reference
.internal}).

The export API in MLX lets you export multiple traces of the same
function to a single file by creating an exporting context manager with
[[`exporter()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.exporter.html#mlx.core.exporter "mlx.core.exporter"){.reference
.internal}:

:::: {.highlight-python .notranslate}
::: highlight
    def fun(x, y=None):
        constant = mx.array(3.0)
        if y is not None:
          x += y
        return x + constant

    with mx.exporter("fun.mlxfn", fun) as exporter:
        exporter(mx.array(1.0))
        exporter(mx.array(1.0), y=mx.array(0.0))

    imported_function = mx.import_function("fun.mlxfn")

    # Call the function with y=None
    out, = imported_function(mx.array(1.0))
    print(out)

    # Call the function with y specified
    out, = imported_function(mx.array(1.0), y=mx.array(1.0))
    print(out)
:::
::::

In the above example the function constant data, (i.e.
[`constant`{.docutils .literal .notranslate}]{.pre}), is only saved
once.
:::::

::::: {#transformations-with-imported-functions .section}
## Transformations with Imported Functions[\#](#transformations-with-imported-functions "Link to this heading"){.headerlink}

Function transformations like [[`grad()`{.xref .py .py-func .docutils
.literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.grad.html#mlx.core.grad "mlx.core.grad"){.reference
.internal}, [[`vmap()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap "mlx.core.vmap"){.reference
.internal}, and [[`compile()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.compile.html#mlx.core.compile "mlx.core.compile"){.reference
.internal} work on imported functions just like regular Python
functions:

:::: {.highlight-python .notranslate}
::: highlight
    def fun(x):
        return mx.sin(x)

    x = mx.array(0.0)
    mx.export_function("sine.mlxfn", fun, x)

    imported_fun = mx.import_function("sine.mlxfn")

    # Take the derivative of the imported function
    dfdx = mx.grad(lambda x: imported_fun(x)[0])
    # Prints: array(1, dtype=float32)
    print(dfdx(x))

    # Compile the imported function
    mx.compile(imported_fun)
    # Prints: array(0, dtype=float32)
    print(compiled_fun(x)[0])
:::
::::
:::::

::::::: {#importing-functions-in-c .section}
## Importing Functions in C++[\#](#importing-functions-in-c "Link to this heading"){.headerlink}

Importing and running functions in C++ is basically the same as
importing and running them in Python. First, follow the
[[instructions]{.std
.std-ref}](../dev/mlx_in_cpp.html#mlx-in-cpp){.reference .internal} to
setup a simple C++ project that uses MLX as a library.

Next, export a simple function from Python:

:::: {.highlight-python .notranslate}
::: highlight
    def fun(x, y):
        return mx.exp(x + y)

    x = mx.array(1.0)
    y = mx.array(1.0)
    mx.export_function("fun.mlxfn", fun, x, y)
:::
::::

Import and run the function in C++ with only a few lines of code:

:::: {.highlight-c++ .notranslate}
::: highlight
    auto fun = mx::import_function("fun.mlxfn");

    auto inputs = {mx::array(1.0), mx::array(1.0)};
    auto outputs = fun(inputs);

    // Prints: array(2, dtype=float32)
    std::cout << outputs[0] << std::endl;
:::
::::

Imported functions can be transformed in C++ just like in Python. Use
[`std::vector<mx::array>`{.docutils .literal .notranslate}]{.pre} for
positional arguments and [`std::map<std::string,`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`mx::array>`{.docutils .literal .notranslate}]{.pre} for
keyword arguments when calling imported functions in C++.
:::::::

::: {#more-examples .section}
## More Examples[\#](#more-examples "Link to this heading"){.headerlink}

Here are a few more complete examples exporting more complex functions
from Python and importing and running them in C++:

- [Inference and training a multi-layer
  perceptron](https://github.com/ml-explore/mlx/tree/main/examples/export){.reference
  .external}
:::
::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](using_streams.html "previous page"){.left-prev}

::: prev-next-info
previous

Using Streams
:::

[](../examples/linear_regression.html "next page"){.right-next}

::: prev-next-info
next

Linear Regression
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [Basics of Exporting](#basics-of-exporting){.reference .internal
  .nav-link}
- [Exporting Modules](#exporting-modules){.reference .internal
  .nav-link}
- [Exporting with a Callback](#exporting-with-a-callback){.reference
  .internal .nav-link}
- [Shapeless Exports](#shapeless-exports){.reference .internal
  .nav-link}
- [Exporting Multiple Traces](#exporting-multiple-traces){.reference
  .internal .nav-link}
- [Transformations with Imported
  Functions](#transformations-with-imported-functions){.reference
  .internal .nav-link}
- [Importing Functions in C++](#importing-functions-in-c){.reference
  .internal .nav-link}
- [More Examples](#more-examples){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::: {.bd-footer-content__inner .container}
::: footer-item
By MLX Contributors
:::

::: footer-item
© Copyright 2023, Apple.\
:::

::: footer-item
:::

::: footer-item
:::
:::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
