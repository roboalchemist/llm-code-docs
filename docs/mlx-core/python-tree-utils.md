::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::: bd-content
::::::::::::::::::::: bd-article-container
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
  [.rst]{.btn__text-container}](../_sources/python/tree_utils.rst "Download source file"){.btn
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
# Tree Utils

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

::::: {#tree-utils .section}
[]{#utils}

# Tree Utils[\#](#tree-utils "Link to this heading"){.headerlink}

In MLX we consider a python tree to be an arbitrarily nested collection
of dictionaries, lists and tuples without cycles. Functions in this
module that return python trees will be using the default python
[`dict`{.docutils .literal .notranslate}]{.pre}, [`list`{.docutils
.literal .notranslate}]{.pre} and [`tuple`{.docutils .literal
.notranslate}]{.pre} but they can usually process objects that inherit
from any of these.

::: {.admonition .note}
Note

Dictionaries should have keys that are valid python identifiers.
:::

::: pst-scrollable-table-container
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`tree_flatten`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.utils.tree_flatten.html#mlx.utils.tree_flatten "mlx.utils.tree_flatten"){.reference .internal}(tree\[, prefix, is_leaf, \...\])                      Flattens a Python tree to a list of key, value tuples.
  [[`tree_unflatten`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.utils.tree_unflatten.html#mlx.utils.tree_unflatten "mlx.utils.tree_unflatten"){.reference .internal}(tree)                                         Recreate a Python tree from its flat representation.
  [[`tree_map`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.utils.tree_map.html#mlx.utils.tree_map "mlx.utils.tree_map"){.reference .internal}(fn, tree, \*rest\[, is_leaf\])                                        Applies [`fn`{.docutils .literal .notranslate}]{.pre} to the leaves of the Python tree [`tree`{.docutils .literal .notranslate}]{.pre} and returns a new collection with the results.
  [[`tree_map_with_path`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.utils.tree_map_with_path.html#mlx.utils.tree_map_with_path "mlx.utils.tree_map_with_path"){.reference .internal}(fn, tree, \*rest\[, \...\])   Applies [`fn`{.docutils .literal .notranslate}]{.pre} to the path and leaves of the Python tree [`tree`{.docutils .literal .notranslate}]{.pre} and returns a new collection with the results.
  [[`tree_reduce`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.utils.tree_reduce.html#mlx.utils.tree_reduce "mlx.utils.tree_reduce"){.reference .internal}(fn, tree\[, initializer, is_leaf\])                       Applies a reduction to the leaves of a Python tree.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::::

::::: prev-next-area
[](_autosummary/mlx.core.distributed.recv_like.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.distributed.recv_like
:::

[](_autosummary/mlx.utils.tree_flatten.html "next page"){.right-next}

::: prev-next-info
next

mlx.utils.tree_flatten
:::
:::::
:::::::::::::::::::::
::::::::::::::::::::::

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
:::::::::::::::::::::::::::::
