:::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::: bd-article-container
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
  [.rst]{.btn__text-container}](../_sources/usage/numpy.rst "Download source file"){.btn
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

# Conversion to NumPy and Other Frameworks

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}

## Contents

:::

- [PyTorch](#pytorch){.reference .internal .nav-link}
- [JAX](#jax){.reference .internal .nav-link}
- [TensorFlow](#tensorflow){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::: {#conversion-to-numpy-and-other-frameworks .section}
[]{#numpy}

# Conversion to NumPy and Other Frameworks[\#](#conversion-to-numpy-and-other-frameworks "Link to this heading"){.headerlink}

MLX array supports conversion between other frameworks with either:

- The [Python Buffer
  Protocol](https://docs.python.org/3/c-api/buffer.html){.reference
  .external}.

- [DLPack](https://dmlc.github.io/dlpack/latest/){.reference .external}.

Let's convert an array to NumPy and back.

:::: {.highlight-python .notranslate}
::: highlight
    import mlx.core as mx
    import numpy as np

    a = mx.arange(3)
    b = np.array(a) # copy of a
    c = mx.array(b) # copy of b
:::
::::

::: {.admonition .note}
Note

Since NumPy does not support [`bfloat16`{.docutils .literal
.notranslate}]{.pre} arrays, you will need to convert to
[`float16`{.docutils .literal .notranslate}]{.pre} or
[`float32`{.docutils .literal .notranslate}]{.pre} first:
[`np.array(a.astype(mx.float32))`{.docutils .literal
.notranslate}]{.pre}. Otherwise, you will receive an error like:
[`Item`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`size`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`2`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`for`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`PEP`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`3118`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`buffer`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`format`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`string`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`does`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`not`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`match`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`the`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`dtype`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`V`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`item`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`size`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`0.`{.docutils
.literal .notranslate}]{.pre}
:::

By default, NumPy copies data to a new array. This can be prevented by
creating an array view:

:::: {.highlight-python .notranslate}
::: highlight
    a = mx.arange(3)
    a_view = np.array(a, copy=False)
    print(a_view.flags.owndata) # False
    a_view[0] = 1
    print(a[0].item()) # 1
:::
::::

::: {.admonition .note}
Note

NumPy arrays with type [`float64`{.docutils .literal
.notranslate}]{.pre} will be default converted to MLX arrays with type
[`float32`{.docutils .literal .notranslate}]{.pre}.
:::

A NumPy array view is a normal NumPy array, except that it does not own
its memory. This means writing to the view is reflected in the original
array.

While this is quite powerful to prevent copying arrays, it should be
noted that external changes to the memory of arrays cannot be reflected
in gradients.

Let's demonstrate this in an example:

:::: {.highlight-python .notranslate}
::: highlight
    def f(x):
        x_view = np.array(x, copy=False)
        x_view[:] *= x_view # modify memory without telling mx
        return x.sum()

    x = mx.array([3.0])
    y, df = mx.value_and_grad(f)(x)
    print("f(x) = x² =", y.item()) # 9.0
    print("f'(x) = 2x !=", df.item()) # 1.0
:::
::::

The function [`f`{.docutils .literal .notranslate}]{.pre} indirectly
modifies the array [`x`{.docutils .literal .notranslate}]{.pre} through
a memory view. However, this modification is not reflected in the
gradient, as seen in the last line outputting [`1.0`{.docutils .literal
.notranslate}]{.pre}, representing the gradient of the sum operation
alone. The squaring of [`x`{.docutils .literal .notranslate}]{.pre}
occurs externally to MLX, meaning that no gradient is incorporated. It's
important to note that a similar issue arises during array conversion
and copying. For instance, a function defined as
[`mx.array(np.array(x)**2).sum()`{.docutils .literal
.notranslate}]{.pre} would also result in an incorrect gradient, even
though no in-place operations on MLX memory are executed.

:::::: {#pytorch .section}

## PyTorch[\#](#pytorch "Link to this heading"){.headerlink}

::: {.admonition .warning}
Warning

PyTorch Support for [[`memoryview`{.xref .py .py-obj .docutils .literal
.notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#memoryview "(in Python v3.14)"){.reference
.external} is experimental and can break for multi-dimensional arrays.
Casting to NumPy first is advised for now.
:::

PyTorch supports the buffer protocol, but it requires an explicit
[[`memoryview`{.xref .py .py-obj .docutils .literal
.notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#memoryview "(in Python v3.14)"){.reference
.external}.

:::: {.highlight-python .notranslate}
::: highlight
    import mlx.core as mx
    import torch

    a = mx.arange(3)
    b = torch.tensor(memoryview(a))
    c = mx.array(b.numpy())
:::
::::

Conversion from PyTorch tensors back to arrays must be done via
intermediate NumPy arrays with [`numpy()`{.docutils .literal
.notranslate}]{.pre}.
::::::

::::: {#jax .section}

## JAX[\#](#jax "Link to this heading"){.headerlink}

JAX fully supports the buffer protocol.

:::: {.highlight-python .notranslate}
::: highlight
    import mlx.core as mx
    import jax.numpy as jnp

    a = mx.arange(3)
    b = jnp.array(a)
    c = mx.array(b)
:::
::::
:::::

::::: {#tensorflow .section}

## TensorFlow[\#](#tensorflow "Link to this heading"){.headerlink}

TensorFlow supports the buffer protocol, but it requires an explicit
[[`memoryview`{.xref .py .py-obj .docutils .literal
.notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#memoryview "(in Python v3.14)"){.reference
.external}.

:::: {.highlight-python .notranslate}
::: highlight
    import mlx.core as mx
    import tensorflow as tf

    a = mx.arange(3)
    b = tf.constant(memoryview(a))
    c = mx.array(b)
:::
::::
:::::
:::::::::::::::::::::

::::: prev-next-area
[](compile.html "previous page"){.left-prev}

::: prev-next-info
previous

Compilation
:::

[](distributed.html "next page"){.right-next}

::: prev-next-info
next

Distributed Communication
:::
:::::
::::::::::::::::::::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [PyTorch](#pytorch){.reference .internal .nav-link}
- [JAX](#jax){.reference .internal .nav-link}
- [TensorFlow](#tensorflow){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::

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
::::::::::::::::::::::::::::::::::::::::::::::::::
