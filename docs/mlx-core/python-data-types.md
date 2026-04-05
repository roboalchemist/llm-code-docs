:::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::: bd-content
:::::::::::::::::::::: bd-article-container
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
  [.rst]{.btn__text-container}](../_sources/python/data_types.rst "Download source file"){.btn
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
# Data Types

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::::: {#data-types .section}
[]{#id1}

# Data Types[\#](#data-types "Link to this heading"){.headerlink}

The default floating point type is [`float32`{.docutils .literal
.notranslate}]{.pre} and the default integer type is [`int32`{.docutils
.literal .notranslate}]{.pre}. The table below shows supported values
for [[`Dtype`{.xref .py .py-obj .docutils .literal
.notranslate}]{.pre}](_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype"){.reference
.internal}.

::: pst-scrollable-table-container
+------------------------+-------+--------------------------------------------------+
| Type                   | Bytes | Description                                      |
+========================+=======+==================================================+
| [`bool_`{.docutils     | 1     | Boolean ([`True`{.docutils .literal              |
| .literal               |       | .notranslate}]{.pre}, [`False`{.docutils         |
| .notranslate}]{.pre}   |       | .literal .notranslate}]{.pre}) data type         |
+------------------------+-------+--------------------------------------------------+
| [`uint8`{.docutils     | 1     | 8-bit unsigned integer                           |
| .literal               |       |                                                  |
| .notranslate}]{.pre}   |       |                                                  |
+------------------------+-------+--------------------------------------------------+
| [`uint16`{.docutils    | 2     | 16-bit unsigned integer                          |
| .literal               |       |                                                  |
| .notranslate}]{.pre}   |       |                                                  |
+------------------------+-------+--------------------------------------------------+
| [`uint32`{.docutils    | 4     | 32-bit unsigned integer                          |
| .literal               |       |                                                  |
| .notranslate}]{.pre}   |       |                                                  |
+------------------------+-------+--------------------------------------------------+
| [`uint64`{.docutils    | 8     | 64-bit unsigned integer                          |
| .literal               |       |                                                  |
| .notranslate}]{.pre}   |       |                                                  |
+------------------------+-------+--------------------------------------------------+
| [`int8`{.docutils      | 1     | 8-bit signed integer                             |
| .literal               |       |                                                  |
| .notranslate}]{.pre}   |       |                                                  |
+------------------------+-------+--------------------------------------------------+
| [`int16`{.docutils     | 2     | 16-bit signed integer                            |
| .literal               |       |                                                  |
| .notranslate}]{.pre}   |       |                                                  |
+------------------------+-------+--------------------------------------------------+
| [`int32`{.docutils     | 4     | 32-bit signed integer                            |
| .literal               |       |                                                  |
| .notranslate}]{.pre}   |       |                                                  |
+------------------------+-------+--------------------------------------------------+
| [`int64`{.docutils     | 8     | 64-bit signed integer                            |
| .literal               |       |                                                  |
| .notranslate}]{.pre}   |       |                                                  |
+------------------------+-------+--------------------------------------------------+
| [`bfloat16`{.docutils  | 2     | 16-bit brain float (e8, m7)                      |
| .literal               |       |                                                  |
| .notranslate}]{.pre}   |       |                                                  |
+------------------------+-------+--------------------------------------------------+
| [`float16`{.docutils   | 2     | 16-bit IEEE float (e5, m10)                      |
| .literal               |       |                                                  |
| .notranslate}]{.pre}   |       |                                                  |
+------------------------+-------+--------------------------------------------------+
| [`float32`{.docutils   | 4     | 32-bit float                                     |
| .literal               |       |                                                  |
| .notranslate}]{.pre}   |       |                                                  |
+------------------------+-------+--------------------------------------------------+
| [`float64`{.docutils   | 8     | 64-bit double                                    |
| .literal               |       |                                                  |
| .notranslate}]{.pre}   |       |                                                  |
+------------------------+-------+--------------------------------------------------+
| [`complex64`{.docutils | 8     | 64-bit complex float                             |
| .literal               |       |                                                  |
| .notranslate}]{.pre}   |       |                                                  |
+------------------------+-------+--------------------------------------------------+

: [Supported Data
Types]{.caption-text}[\#](#id2 "Link to this table"){.headerlink} {#id2
.table}
:::

::: {.admonition .note}
Note

Arrays with type [`float64`{.docutils .literal .notranslate}]{.pre} only
work with CPU operations. Using [`float64`{.docutils .literal
.notranslate}]{.pre} arrays on the GPU will result in an exception.
:::

Data type are aranged in a hierarchy. See the [[`DtypeCategory`{.xref
.py .py-obj .docutils .literal
.notranslate}]{.pre}](_autosummary/mlx.core.DtypeCategory.html#mlx.core.DtypeCategory "mlx.core.DtypeCategory"){.reference
.internal} object documentation for more information. Use
[[`issubdtype()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](_autosummary/mlx.core.issubdtype.html#mlx.core.issubdtype "mlx.core.issubdtype"){.reference
.internal} to determine if one [`dtype`{.docutils .literal
.notranslate}]{.pre} (or category) is a subtype of another category.

::: pst-scrollable-table-container
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`Dtype`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype"){.reference .internal}                                             An object to hold the type of a [[`array`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference .internal}.
  [[`DtypeCategory`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.DtypeCategory.html#mlx.core.DtypeCategory "mlx.core.DtypeCategory"){.reference .internal}(\*values)   Type to hold categories of [[`dtypes`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype"){.reference .internal}.
  [[`issubdtype`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.issubdtype.html#mlx.core.issubdtype "mlx.core.issubdtype"){.reference .internal}(arg1, arg2)             Check if a [[`Dtype`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype"){.reference .internal} or [[`DtypeCategory`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.DtypeCategory.html#mlx.core.DtypeCategory "mlx.core.DtypeCategory"){.reference .internal} is a subtype of another.
  [[`finfo`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.finfo.html#mlx.core.finfo "mlx.core.finfo"){.reference .internal}(\*args, \*\*kwargs)                         Get information on floating-point types.
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
::::::

::::: prev-next-area
[](_autosummary/mlx.core.array.view.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.array.view
:::

[](_autosummary/mlx.core.Dtype.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.Dtype
:::
:::::
::::::::::::::::::::::
:::::::::::::::::::::::

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
::::::::::::::::::::::::::::::
