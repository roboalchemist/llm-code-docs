::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::: bd-article-container
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
  [.rst]{.btn__text-container}](../_sources/usage/lazy_evaluation.rst "Download source file"){.btn
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
# Lazy Evaluation

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Why Lazy Evaluation](#why-lazy-evaluation){.reference .internal
  .nav-link}
  - [Transforming Compute
    Graphs](#transforming-compute-graphs){.reference .internal
    .nav-link}
  - [Only Compute What You Use](#only-compute-what-you-use){.reference
    .internal .nav-link}
- [When to Evaluate](#when-to-evaluate){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::: {#lazy-evaluation .section}
[]{#lazy-eval}

# Lazy Evaluation[\#](#lazy-evaluation "Link to this heading"){.headerlink}

::::::::: {#why-lazy-evaluation .section}
## Why Lazy Evaluation[\#](#why-lazy-evaluation "Link to this heading"){.headerlink}

When you perform operations in MLX, no computation actually happens.
Instead a compute graph is recorded. The actual computation only happens
if an [[`eval()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.eval.html#mlx.core.eval "mlx.core.eval"){.reference
.internal} is performed.

MLX uses lazy evaluation because it has some nice features, some of
which we describe below.

::: {#transforming-compute-graphs .section}
### Transforming Compute Graphs[\#](#transforming-compute-graphs "Link to this heading"){.headerlink}

Lazy evaluation lets us record a compute graph without actually doing
any computations. This is useful for function transformations like
[[`grad()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.grad.html#mlx.core.grad "mlx.core.grad"){.reference
.internal} and [[`vmap()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap "mlx.core.vmap"){.reference
.internal} and graph optimizations.

Currently, MLX does not compile and rerun compute graphs. They are all
generated dynamically. However, lazy evaluation makes it much easier to
integrate compilation for future performance enhancements.
:::

::::::: {#only-compute-what-you-use .section}
### Only Compute What You Use[\#](#only-compute-what-you-use "Link to this heading"){.headerlink}

In MLX you do not need to worry as much about computing outputs that are
never used. For example:

:::: {.highlight-python .notranslate}
::: highlight
    def fun(x):
        a = fun1(x)
        b = expensive_fun(a)
        return a, b

    y, _ = fun(x)
:::
::::

Here, we never actually compute the output of [`expensive_fun`{.docutils
.literal .notranslate}]{.pre}. Use this pattern with care though, as the
graph of [`expensive_fun`{.docutils .literal .notranslate}]{.pre} is
still built, and that has some cost associated to it.

Similarly, lazy evaluation can be beneficial for saving memory while
keeping code simple. Say you have a very large model [`Model`{.docutils
.literal .notranslate}]{.pre} derived from [[`mlx.nn.Module`{.xref .py
.py-obj .docutils .literal
.notranslate}]{.pre}](../python/nn/module.html#mlx.nn.Module "mlx.nn.Module"){.reference
.internal}. You can instantiate this model with [`model`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`Model()`{.docutils .literal
.notranslate}]{.pre}. Typically, this will initialize all of the weights
as [`float32`{.docutils .literal .notranslate}]{.pre}, but the
initialization does not actually compute anything until you perform an
[[`eval()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.eval.html#mlx.core.eval "mlx.core.eval"){.reference
.internal}. If you update the model with [`float16`{.docutils .literal
.notranslate}]{.pre} weights, your maximum consumed memory will be half
that required if eager computation was used instead.

This pattern is simple to do in MLX thanks to lazy computation:

:::: {.highlight-python .notranslate}
::: highlight
    model = Model() # no memory used yet
    model.load_weights("weights_fp16.safetensors")
:::
::::
:::::::
:::::::::

:::::::::: {#when-to-evaluate .section}
## When to Evaluate[\#](#when-to-evaluate "Link to this heading"){.headerlink}

A common question is when to use [[`eval()`{.xref .py .py-func .docutils
.literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.eval.html#mlx.core.eval "mlx.core.eval"){.reference
.internal}. The trade-off is between letting graphs get too large and
not batching enough useful work.

For example:

:::: {.highlight-python .notranslate}
::: highlight
    for _ in range(100):
         a = a + b
         mx.eval(a)
         b = b * 2
         mx.eval(b)
:::
::::

This is a bad idea because there is some fixed overhead with each graph
evaluation. On the other hand, there is some slight overhead which grows
with the compute graph size, so extremely large graphs (while
computationally correct) can be costly.

Luckily, a wide range of compute graph sizes work pretty well with MLX:
anything from a few tens of operations to many thousands of operations
per evaluation should be okay.

Most numerical computations have an iterative outer loop (e.g. the
iteration in stochastic gradient descent). A natural and usually
efficient place to use [[`eval()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.eval.html#mlx.core.eval "mlx.core.eval"){.reference
.internal} is at each iteration of this outer loop.

Here is a concrete example:

:::: {.highlight-python .notranslate}
::: highlight
    for batch in dataset:

        # Nothing has been evaluated yet
        loss, grad = value_and_grad_fn(model, batch)

        # Still nothing has been evaluated
        optimizer.update(model, grad)

        # Evaluate the loss and the new parameters which will
        # run the full gradient computation and optimizer update
        mx.eval(loss, model.parameters())
:::
::::

An important behavior to be aware of is when the graph will be
implicitly evaluated. Anytime you [`print`{.docutils .literal
.notranslate}]{.pre} an array, convert it to an [[`numpy.ndarray`{.xref
.py .py-obj .docutils .literal
.notranslate}]{.pre}](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)"){.reference
.external}, or otherwise access its memory via [[`memoryview`{.xref .py
.py-obj .docutils .literal
.notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#memoryview "(in Python v3.14)"){.reference
.external}, the graph will be evaluated. Saving arrays via
[[`save()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.save.html#mlx.core.save "mlx.core.save"){.reference
.internal} (or any other MLX saving functions) will also evaluate the
array.

Calling [[`array.item()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.array.item.html#mlx.core.array.item "mlx.core.array.item"){.reference
.internal} on a scalar array will also evaluate it. In the example
above, printing the loss ([`print(loss)`{.docutils .literal
.notranslate}]{.pre}) or adding the loss scalar to a list
([`losses.append(loss.item())`{.docutils .literal .notranslate}]{.pre})
would cause a graph evaluation. If these lines are before
[`mx.eval(loss,`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`model.parameters())`{.docutils .literal
.notranslate}]{.pre} then this will be a partial evaluation, computing
only the forward pass.

Also, calling [[`eval()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.eval.html#mlx.core.eval "mlx.core.eval"){.reference
.internal} on an array or set of arrays multiple times is perfectly
fine. This is effectively a no-op.

::: {.admonition .warning}
Warning

Using scalar arrays for control-flow will cause an evaluation.
:::

Here is an example:

:::: {.highlight-python .notranslate}
::: highlight
    def fun(x):
        h, y = first_layer(x)
        if y > 0:  # An evaluation is done here!
            z  = second_layer_a(h)
        else:
            z  = second_layer_b(h)
        return z
:::
::::

Using arrays for control flow should be done with care. The above
example works and can even be used with gradient transformations.
However, this can be very inefficient if evaluations are done too
frequently.
::::::::::
::::::::::::::::::

::::: prev-next-area
[](quick_start.html "previous page"){.left-prev}

::: prev-next-info
previous

Quick Start Guide
:::

[](unified_memory.html "next page"){.right-next}

::: prev-next-info
next

Unified Memory
:::
:::::
:::::::::::::::::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [Why Lazy Evaluation](#why-lazy-evaluation){.reference .internal
  .nav-link}
  - [Transforming Compute
    Graphs](#transforming-compute-graphs){.reference .internal
    .nav-link}
  - [Only Compute What You Use](#only-compute-what-you-use){.reference
    .internal .nav-link}
- [When to Evaluate](#when-to-evaluate){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::

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
:::::::::::::::::::::::::::::::::::::::::::::::
