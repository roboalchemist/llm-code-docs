:::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::: bd-article-container
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
  [.rst]{.btn__text-container}](../_sources/usage/saving_and_loading.rst "Download source file"){.btn
  .btn-sm .btn-download-source-button .dropdown-item target="_blank"
  bs-placement="left" bs-toggle="tooltip"}
- [ ]{.btn__icon-container} [.pdf]{.btn__text-container}
:::

[ ]{.btn__icon-container}
::::
:::::
::::::
:::::::::
::::::::::

::::: {#jb-print-docs-body .onlyprint}
# Saving and Loading Arrays

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::::::::::::: {#saving-and-loading-arrays .section}
[]{#saving-and-loading}

# Saving and Loading Arrays[\#](#saving-and-loading-arrays "Link to this heading"){.headerlink}

MLX supports multiple array serialization formats.

::: pst-scrollable-table-container
+-----------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Format          | Extension                 | Function                                                                                                                                      | Notes                |
+=================+===========================+===============================================================================================================================================+======================+
| NumPy           | [`.npy`{.docutils         | [[`save()`{.xref .py .py-func .docutils .literal                                                                                              | Single arrays only   |
|                 | .literal                  | .notranslate}]{.pre}](../python/_autosummary/mlx.core.save.html#mlx.core.save "mlx.core.save"){.reference .internal}                          |                      |
|                 | .notranslate}]{.pre}      |                                                                                                                                               |                      |
+-----------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| NumPy archive   | [`.npz`{.docutils         | [[`savez()`{.xref .py .py-func .docutils .literal                                                                                             | Multiple arrays      |
|                 | .literal                  | .notranslate}]{.pre}](../python/_autosummary/mlx.core.savez.html#mlx.core.savez "mlx.core.savez"){.reference .internal} and                   |                      |
|                 | .notranslate}]{.pre}      | [[`savez_compressed()`{.xref .py .py-func .docutils .literal                                                                                  |                      |
|                 |                           | .notranslate}]{.pre}](../python/_autosummary/mlx.core.savez_compressed.html#mlx.core.savez_compressed "mlx.core.savez_compressed"){.reference |                      |
|                 |                           | .internal}                                                                                                                                    |                      |
+-----------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Safetensors     | [`.safetensors`{.docutils | [[`save_safetensors()`{.xref .py .py-func .docutils .literal                                                                                  | Multiple arrays      |
|                 | .literal                  | .notranslate}]{.pre}](../python/_autosummary/mlx.core.save_safetensors.html#mlx.core.save_safetensors "mlx.core.save_safetensors"){.reference |                      |
|                 | .notranslate}]{.pre}      | .internal}                                                                                                                                    |                      |
+-----------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| GGUF            | [`.gguf`{.docutils        | [[`save_gguf()`{.xref .py .py-func .docutils .literal                                                                                         | Multiple arrays      |
|                 | .literal                  | .notranslate}]{.pre}](../python/_autosummary/mlx.core.save_gguf.html#mlx.core.save_gguf "mlx.core.save_gguf"){.reference .internal}           |                      |
|                 | .notranslate}]{.pre}      |                                                                                                                                               |                      |
+-----------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

: [Serialization
Formats]{.caption-text}[\#](#id1 "Link to this table"){.headerlink}
{#id1 .table}
:::

The [[`load()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.load.html#mlx.core.load "mlx.core.load"){.reference
.internal} function will load any of the supported serialization
formats. It determines the format from the extensions. The output of
[[`load()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.load.html#mlx.core.load "mlx.core.load"){.reference
.internal} depends on the format.

Here's an example of saving a single array to a file:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> a = mx.array([1.0])
    >>> mx.save("array", a)
:::
::::

The array [`a`{.docutils .literal .notranslate}]{.pre} will be saved in
the file [`array.npy`{.docutils .literal .notranslate}]{.pre} (notice
the extension is automatically added). Including the extension is
optional; if it is missing it will be added. You can load the array
with:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> mx.load("array.npy")
    array([1], dtype=float32)
:::
::::

Here's an example of saving several arrays to a single file:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> a = mx.array([1.0])
    >>> b = mx.array([2.0])
    >>> mx.savez("arrays", a, b=b)
:::
::::

For compatibility with [[`numpy.savez()`{.xref .py .py-func .docutils
.literal
.notranslate}]{.pre}](https://numpy.org/doc/stable/reference/generated/numpy.savez.html#numpy.savez "(in NumPy v2.4)"){.reference
.external} the MLX [[`savez()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.savez.html#mlx.core.savez "mlx.core.savez"){.reference
.internal} takes arrays as arguments. If the keywords are missing, then
default names will be provided. This can be loaded with:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> mx.load("arrays.npz")
    {'b': array([2], dtype=float32), 'arr_0': array([1], dtype=float32)}
:::
::::

In this case [[`load()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.load.html#mlx.core.load "mlx.core.load"){.reference
.internal} returns a dictionary of names to arrays.

The functions [[`save_safetensors()`{.xref .py .py-func .docutils
.literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.save_safetensors.html#mlx.core.save_safetensors "mlx.core.save_safetensors"){.reference
.internal} and [[`save_gguf()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.save_gguf.html#mlx.core.save_gguf "mlx.core.save_gguf"){.reference
.internal} are similar to [[`savez()`{.xref .py .py-func .docutils
.literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.savez.html#mlx.core.savez "mlx.core.savez"){.reference
.internal}, but they take as input a [[`dict`{.xref .py .py-obj
.docutils .literal
.notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"){.reference
.external} of string names to arrays:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> a = mx.array([1.0])
    >>> b = mx.array([2.0])
    >>> mx.save_safetensors("arrays", {"a": a, "b": b})
:::
::::
::::::::::::::

::::: prev-next-area
[](indexing.html "previous page"){.left-prev}

::: prev-next-info
previous

Indexing Arrays
:::

[](function_transforms.html "next page"){.right-next}

::: prev-next-info
next

Function Transforms
:::
:::::
::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::

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
::::::::::::::::::::::::::::::::::::::
