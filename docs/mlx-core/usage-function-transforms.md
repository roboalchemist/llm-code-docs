:::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::: bd-article-container
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
  [.rst]{.btn__text-container}](../_sources/usage/function_transforms.rst "Download source file"){.btn
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
# Function Transforms

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Automatic Differentiation](#automatic-differentiation){.reference
  .internal .nav-link}
- [Automatic Vectorization](#automatic-vectorization){.reference
  .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::: {#function-transforms .section}
[]{#id1}

# Function Transforms[\#](#function-transforms "Link to this heading"){.headerlink}

MLX uses composable function transformations for automatic
differentiation, vectorization, and compute graph optimizations. To see
the complete list of function transformations check-out the [[API
documentation]{.std
.std-ref}](../python/transforms.html#transforms){.reference .internal}.

The key idea behind composable function transformations is that every
transformation returns a function which can be further transformed.

Here is a simple example:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> dfdx = mx.grad(mx.sin)
    >>> dfdx(mx.array(mx.pi))
    array(-1, dtype=float32)
    >>> mx.cos(mx.array(mx.pi))
    array(-1, dtype=float32)
:::
::::

The output of [[`grad()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.grad.html#mlx.core.grad "mlx.core.grad"){.reference
.internal} on [[`sin()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.sin.html#mlx.core.sin "mlx.core.sin"){.reference
.internal} is simply another function. In this case it is the gradient
of the sine function which is exactly the cosine function. To get the
second derivative you can do:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> d2fdx2 = mx.grad(mx.grad(mx.sin))
    >>> d2fdx2(mx.array(mx.pi / 2))
    array(-1, dtype=float32)
    >>> mx.sin(mx.array(mx.pi / 2))
    array(1, dtype=float32)
:::
::::

Using [[`grad()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.grad.html#mlx.core.grad "mlx.core.grad"){.reference
.internal} on the output of [[`grad()`{.xref .py .py-func .docutils
.literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.grad.html#mlx.core.grad "mlx.core.grad"){.reference
.internal} is always ok. You keep getting higher order derivatives.

Any of the MLX function transformations can be composed in any order to
any depth. See the following sections for more information on
[[automatic differentiation]{.std .std-ref}](#auto-diff){.reference
.internal} and [[automatic vectorization]{.std
.std-ref}](#vmap){.reference .internal}. For more information on
[[`compile()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.compile.html#mlx.core.compile "mlx.core.compile"){.reference
.internal} see the [[compile documentation]{.std
.std-ref}](compile.html#compile){.reference .internal}.

:::::::::: {#automatic-differentiation .section}
## Automatic Differentiation[\#](#automatic-differentiation "Link to this heading"){.headerlink}

Automatic differentiation in MLX works on functions rather than on
implicit graphs.

::: {.admonition .note}
Note

If you are coming to MLX from PyTorch, you no longer need functions like
[`backward`{.docutils .literal .notranslate}]{.pre},
[`zero_grad`{.docutils .literal .notranslate}]{.pre}, and
[`detach`{.docutils .literal .notranslate}]{.pre}, or properties like
[`requires_grad`{.docutils .literal .notranslate}]{.pre}.
:::

The most basic example is taking the gradient of a scalar-valued
function as we saw above. You can use the [[`grad()`{.xref .py .py-func
.docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.grad.html#mlx.core.grad "mlx.core.grad"){.reference
.internal} and [[`value_and_grad()`{.xref .py .py-func .docutils
.literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.value_and_grad.html#mlx.core.value_and_grad "mlx.core.value_and_grad"){.reference
.internal} function to compute gradients of more complex functions. By
default these functions compute the gradient with respect to the first
argument:

:::: {.highlight-python .notranslate}
::: highlight
    def loss_fn(w, x, y):
       return mx.mean(mx.square(w * x - y))

    w = mx.array(1.0)
    x = mx.array([0.5, -0.5])
    y = mx.array([1.5, -1.5])

    # Computes the gradient of loss_fn with respect to w:
    grad_fn = mx.grad(loss_fn)
    dloss_dw = grad_fn(w, x, y)
    # Prints array(-1, dtype=float32)
    print(dloss_dw)

    # To get the gradient with respect to x we can do:
    grad_fn = mx.grad(loss_fn, argnums=1)
    dloss_dx = grad_fn(w, x, y)
    # Prints array([-1, 1], dtype=float32)
    print(dloss_dx)
:::
::::

One way to get the loss and gradient is to call [`loss_fn`{.docutils
.literal .notranslate}]{.pre} followed by [`grad_fn`{.docutils .literal
.notranslate}]{.pre}, but this can result in a lot of redundant work.
Instead, you should use [[`value_and_grad()`{.xref .py .py-func
.docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.value_and_grad.html#mlx.core.value_and_grad "mlx.core.value_and_grad"){.reference
.internal}. Continuing the above example:

:::: {.highlight-python .notranslate}
::: highlight
    # Computes the gradient of loss_fn with respect to w:
    loss_and_grad_fn = mx.value_and_grad(loss_fn)
    loss, dloss_dw = loss_and_grad_fn(w, x, y)

    # Prints array(1, dtype=float32)
    print(loss)

    # Prints array(-1, dtype=float32)
    print(dloss_dw)
:::
::::

You can also take the gradient with respect to arbitrarily nested Python
containers of arrays (specifically any of [[`list`{.xref .py .py-obj
.docutils .literal
.notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"){.reference
.external}, [[`tuple`{.xref .py .py-obj .docutils .literal
.notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)"){.reference
.external}, or [[`dict`{.xref .py .py-obj .docutils .literal
.notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"){.reference
.external}).

Suppose we wanted a weight and a bias parameter in the above example. A
nice way to do that is the following:

:::: {.highlight-python .notranslate}
::: highlight
    def loss_fn(params, x, y):
       w, b = params["weight"], params["bias"]
       h = w * x + b
       return mx.mean(mx.square(h - y))

    params = {"weight": mx.array(1.0), "bias": mx.array(0.0)}
    x = mx.array([0.5, -0.5])
    y = mx.array([1.5, -1.5])

    # Computes the gradient of loss_fn with respect to both the
    # weight and bias:
    grad_fn = mx.grad(loss_fn)
    grads = grad_fn(params, x, y)

    # Prints
    # {'weight': array(-1, dtype=float32), 'bias': array(0, dtype=float32)}
    print(grads)
:::
::::

Notice the tree structure of the parameters is preserved in the
gradients.

In some cases you may want to stop gradients from propagating through a
part of the function. You can use the [[`stop_gradient()`{.xref .py
.py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.stop_gradient.html#mlx.core.stop_gradient "mlx.core.stop_gradient"){.reference
.internal} for that.
::::::::::

:::::::::: {#automatic-vectorization .section}
## Automatic Vectorization[\#](#automatic-vectorization "Link to this heading"){.headerlink}

Use [[`vmap()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap "mlx.core.vmap"){.reference
.internal} to automate vectorizing complex functions. Here we'll go
through a basic and contrived example for the sake of clarity, but
[[`vmap()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap "mlx.core.vmap"){.reference
.internal} can be quite powerful for more complex functions which are
difficult to optimize by hand.

::: {.admonition .warning}
Warning

Some operations are not yet supported with [[`vmap()`{.xref .py .py-func
.docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap "mlx.core.vmap"){.reference
.internal}. If you encounter an error like: [`ValueError:`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`Primitive's`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`vmap`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`not`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`implemented.`{.docutils .literal .notranslate}]{.pre}
file an [issue](https://github.com/ml-explore/mlx/issues){.reference
.external} and include your function. We will prioritize including it.
:::

A naive way to add the elements from two sets of vectors is with a loop:

:::: {.highlight-python .notranslate}
::: highlight
    xs = mx.random.uniform(shape=(4096, 100))
    ys = mx.random.uniform(shape=(100, 4096))

    def naive_add(xs, ys):
        return [xs[i] + ys[:, i] for i in range(xs.shape[0])]
:::
::::

Instead you can use [[`vmap()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap "mlx.core.vmap"){.reference
.internal} to automatically vectorize the addition:

:::: {.highlight-python .notranslate}
::: highlight
    # Vectorize over the second dimension of x and the
    # first dimension of y
    vmap_add = mx.vmap(lambda x, y: x + y, in_axes=(0, 1))
:::
::::

The [`in_axes`{.docutils .literal .notranslate}]{.pre} parameter can be
used to specify which dimensions of the corresponding input to vectorize
over. Similarly, use [`out_axes`{.docutils .literal .notranslate}]{.pre}
to specify where the vectorized axes should be in the outputs.

Let's time these two different versions:

:::: {.highlight-python .notranslate}
::: highlight
    import timeit

    print(timeit.timeit(lambda: mx.eval(naive_add(xs, ys)), number=100))
    print(timeit.timeit(lambda: mx.eval(vmap_add(xs, ys)), number=100))
:::
::::

On an M1 Max the naive version takes in total [`5.639`{.docutils
.literal .notranslate}]{.pre} seconds whereas the vectorized version
takes only [`0.024`{.docutils .literal .notranslate}]{.pre} seconds,
more than 200 times faster.

Of course, this operation is quite contrived. A better approach is to
simply do [`xs`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`+`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`ys.T`{.docutils .literal .notranslate}]{.pre}, but for
more complex functions [[`vmap()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap "mlx.core.vmap"){.reference
.internal} can be quite handy.
::::::::::
:::::::::::::::::::::::

::::: prev-next-area
[](saving_and_loading.html "previous page"){.left-prev}

::: prev-next-info
previous

Saving and Loading Arrays
:::

[](compile.html "next page"){.right-next}

::: prev-next-info
next

Compilation
:::
:::::
::::::::::::::::::::::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [Automatic Differentiation](#automatic-differentiation){.reference
  .internal .nav-link}
- [Automatic Vectorization](#automatic-vectorization){.reference
  .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::

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
::::::::::::::::::::::::::::::::::::::::::::::::::::
