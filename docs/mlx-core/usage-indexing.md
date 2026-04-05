:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
  [.rst]{.btn__text-container}](../_sources/usage/indexing.rst "Download source file"){.btn
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
# Indexing Arrays

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Differences from NumPy](#differences-from-numpy){.reference .internal
  .nav-link}
- [In Place Updates](#in-place-updates){.reference .internal .nav-link}
- [Boolean Mask Assignment](#boolean-mask-assignment){.reference
  .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::: {#indexing-arrays .section}
[]{#indexing}

# Indexing Arrays[\#](#indexing-arrays "Link to this heading"){.headerlink}

For the most part, indexing an MLX [[`array`{.xref .py .py-obj .docutils
.literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
.internal} works the same as indexing a NumPy [[`numpy.ndarray`{.xref
.py .py-obj .docutils .literal
.notranslate}]{.pre}](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)"){.reference
.external}. See the [NumPy
documentation](https://numpy.org/doc/stable/user/basics.indexing.html){.reference
.external} for more details on how that works.

For example, you can use regular integers and slices ([[`slice`{.xref
.py .py-obj .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.slice.html#mlx.core.slice "mlx.core.slice"){.reference
.internal}) to index arrays:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> arr = mx.arange(10)
    >>> arr[3]
    array(3, dtype=int32)
    >>> arr[-2]  # negative indexing works
    array(8, dtype=int32)
    >>> arr[2:8:2] # start, stop, stride
    array([2, 4, 6], dtype=int32)
:::
::::

For multi-dimensional arrays, the [`...`{.docutils .literal
.notranslate}]{.pre} or [[`Ellipsis`{.xref .py .py-obj .docutils
.literal
.notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#Ellipsis "(in Python v3.14)"){.reference
.external} syntax works as in NumPy:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> arr = mx.arange(8).reshape(2, 2, 2)
    >>> arr[:, :, 0]
    array(3, dtype=int32)
    array([[0, 2],
           [4, 6]], dtype=int32
    >>> arr[..., 0]
    array([[0, 2],
           [4, 6]], dtype=int32
:::
::::

You can index with [`None`{.docutils .literal .notranslate}]{.pre} to
create a new axis:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> arr = mx.arange(8)
    >>> arr.shape
    [8]
    >>> arr[None].shape
    [1, 8]
:::
::::

You can also use an [[`array`{.xref .py .py-obj .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
.internal} to index another [[`array`{.xref .py .py-obj .docutils
.literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
.internal}:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> arr = mx.arange(10)
    >>> idx = mx.array([5, 7])
    >>> arr[idx]
    array([5, 7], dtype=int32)
:::
::::

Mixing and matching integers, [[`slice`{.xref .py .py-obj .docutils
.literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.slice.html#mlx.core.slice "mlx.core.slice"){.reference
.internal}, [`...`{.docutils .literal .notranslate}]{.pre}, and
[[`array`{.xref .py .py-obj .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
.internal} indices works just as in NumPy.

Other functions which may be useful for indexing arrays are
[[`take()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.take.html#mlx.core.take "mlx.core.take"){.reference
.internal} and [[`take_along_axis()`{.xref .py .py-func .docutils
.literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.take_along_axis.html#mlx.core.take_along_axis "mlx.core.take_along_axis"){.reference
.internal}.

:::: {#differences-from-numpy .section}
## Differences from NumPy[\#](#differences-from-numpy "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

MLX indexing is different from NumPy indexing in two important ways:

- Indexing does not perform bounds checking. Indexing out of bounds is
  undefined behavior.

- Boolean mask based indexing is supported for assignment only (see
  [[Boolean Mask Assignment]{.std
  .std-ref}](#boolean-mask-assignment){.reference .internal}).
:::

The reason for the lack of bounds checking is that exceptions cannot
propagate from the GPU. Performing bounds checking for array indices
before launching the kernel would be extremely inefficient.

Indexing with boolean masks is something that MLX may support in the
future. In general, MLX has limited support for operations for which
output *shapes* are dependent on input *data*. Other examples of these
types of operations which MLX does not yet support include
[[`numpy.nonzero()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "(in NumPy v2.4)"){.reference
.external} and the single input version of [[`numpy.where()`{.xref .py
.py-func .docutils .literal
.notranslate}]{.pre}](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "(in NumPy v2.4)"){.reference
.external}.
::::

::::::::::::: {#in-place-updates .section}
## In Place Updates[\#](#in-place-updates "Link to this heading"){.headerlink}

In place updates to indexed arrays are possible in MLX. For example:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> a = mx.array([1, 2, 3])
    >>> a[2] = 0
    >>> a
    array([1, 2, 0], dtype=int32)
:::
::::

Just as in NumPy, in place updates will be reflected in all references
to the same array:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> a = mx.array([1, 2, 3])
    >>> b = a
    >>> b[2] = 0
    >>> b
    array([1, 2, 0], dtype=int32)
    >>> a
    array([1, 2, 0], dtype=int32)
:::
::::

Note that unlike NumPy, slicing an array creates a copy, not a view. So
mutating it does not mutate the original array:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> a = mx.array([1, 2, 3])
    >>> b = a[:]
    >>> b[2] = 0
    >>> b
    array([1, 2, 0], dtype=int32)
    >>> a
    array([1, 2, 3], dtype=int32)
:::
::::

Also unlike NumPy, updates to the same location are nondeterministic:

:::: {.highlight-shell .notranslate}
::: highlight
    >>> a = mx.array([1, 2, 3])
    >>> a[[0, 0]] = mx.array([4, 5])
:::
::::

The first element of [`a`{.docutils .literal .notranslate}]{.pre} could
be [`4`{.docutils .literal .notranslate}]{.pre} or [`5`{.docutils
.literal .notranslate}]{.pre}.

Transformations of functions which use in-place updates are allowed and
work as expected. For example:

:::: {.highlight-python .notranslate}
::: highlight
    def fun(x, idx):
        x[idx] = 2.0
        return x.sum()

    dfdx = mx.grad(fun)(mx.array([1.0, 2.0, 3.0]), mx.array([1]))
    print(dfdx)  # Prints: array([1, 0, 1], dtype=float32)
:::
::::

In the above [`dfdx`{.docutils .literal .notranslate}]{.pre} will have
the correct gradient, namely zeros at [`idx`{.docutils .literal
.notranslate}]{.pre} and ones elsewhere.
:::::::::::::

::::::::: {#boolean-mask-assignment .section}
[]{#id1}

## Boolean Mask Assignment[\#](#boolean-mask-assignment "Link to this heading"){.headerlink}

MLX supports boolean indices using NumPy syntax. A mask must already be
a [`bool_`{.xref .py .py-class .docutils .literal .notranslate}]{.pre}
MLX [[`array`{.xref .py .py-class .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
.internal} or a NumPy [`ndarray`{.docutils .literal .notranslate}]{.pre}
with [`dtype=bool`{.docutils .literal .notranslate}]{.pre}. Other index
types are routed through the standard scatter code.

:::: {.highlight-shell .notranslate}
::: highlight
    >>> a = mx.array([1.0, 2.0, 3.0])
    >>> mask = mx.array([True, False, True])
    >>> updates = mx.array([5.0, 6.0])
    >>> a[mask] = updates
    >>> a
    array([5.0, 2.0, 6.0], dtype=float32)
:::
::::

Scalar assignments broadcast to every [`True`{.docutils .literal
.notranslate}]{.pre} entry in [`mask`{.docutils .literal
.notranslate}]{.pre}. For non-scalar assignments, [`updates`{.docutils
.literal .notranslate}]{.pre} must provide at least as many elements as
there are [`True`{.docutils .literal .notranslate}]{.pre} entries in
[`mask`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-shell .notranslate}
::: highlight
    >>> a = mx.zeros((2, 3))
    >>> mask = mx.array([[True, False, True],
                         [False, False, True]])
    >>> a[mask] = 1.0
    >>> a
    array([[1.0, 0.0, 1.0],
           [0.0, 0.0, 1.0]], dtype=float32)
:::
::::

Boolean masks follow NumPy semantics:

- The mask shape must match the shape of the axes it indexes exactly.
  The only exception is a scalar boolean mask, which broadcasts to the
  full array.

- Any axes not covered by the mask are taken in full.

:::: {.highlight-shell .notranslate}
::: highlight
    >>> a = mx.arange(1000).reshape(10, 10, 10)
    >>> a[mx.random.normal((10, 10)) > 0.0] = 0  # valid: mask covers axes 0 and 1
:::
::::

The mask of shape [`(10,`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`10)`{.docutils
.literal .notranslate}]{.pre} applies to the first two axes, so
[`a[mask]`{.docutils .literal .notranslate}]{.pre} selects the 1-D
slices [`a[i,`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`j,`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`:]`{.docutils
.literal .notranslate}]{.pre} where [`mask[i,`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`j]`{.docutils
.literal .notranslate}]{.pre} is [`True`{.docutils .literal
.notranslate}]{.pre}. Shapes such as [`(1,`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`10,`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`10)`{.docutils .literal .notranslate}]{.pre} or
[`(10,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`10,`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`1)`{.docutils .literal .notranslate}]{.pre} do
not match the indexed axes and therefore raise errors.
:::::::::
:::::::::::::::::::::::::::::::

::::: prev-next-area
[](unified_memory.html "previous page"){.left-prev}

::: prev-next-info
previous

Unified Memory
:::

[](saving_and_loading.html "next page"){.right-next}

::: prev-next-info
next

Saving and Loading Arrays
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [Differences from NumPy](#differences-from-numpy){.reference .internal
  .nav-link}
- [In Place Updates](#in-place-updates){.reference .internal .nav-link}
- [Boolean Mask Assignment](#boolean-mask-assignment){.reference
  .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::

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
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
