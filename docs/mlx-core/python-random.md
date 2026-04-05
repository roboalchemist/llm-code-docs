:::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::: bd-article-container
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
  [.rst]{.btn__text-container}](../_sources/python/random.rst "Download source file"){.btn
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
# Random

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::::::: {#random .section}
[]{#id1}

# Random[\#](#random "Link to this heading"){.headerlink}

Random sampling functions in MLX use an implicit global PRNG state by
default. However, all function take an optional [`key`{.docutils
.literal .notranslate}]{.pre} keyword argument for when more
fine-grained control or explicit state management is needed.

For example, you can generate random numbers with:

:::: {.highlight-python .notranslate}
::: highlight
    for _ in range(3):
      print(mx.random.uniform())
:::
::::

which will print a sequence of unique pseudo random numbers.
Alternatively you can explicitly set the key:

:::: {.highlight-python .notranslate}
::: highlight
    key = mx.random.key(0)
    for _ in range(3):
      print(mx.random.uniform(key=key))
:::
::::

which will yield the same pseudo random number at each iteration.

Following [JAX's PRNG
design](https://jax.readthedocs.io/en/latest/jep/263-prng.html){.reference
.external} we use a splittable version of Threefry, which is a
counter-based PRNG.

::: pst-scrollable-table-container
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------
  [[`bernoulli`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.random.bernoulli.html#mlx.core.random.bernoulli "mlx.core.random.bernoulli"){.reference .internal}(\[p, shape, key, stream\])                                            Generate Bernoulli random values.
  [[`categorical`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.random.categorical.html#mlx.core.random.categorical "mlx.core.random.categorical"){.reference .internal}(logits\[, axis, shape, \...\])                                Sample from a categorical distribution.
  [[`gumbel`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.random.gumbel.html#mlx.core.random.gumbel "mlx.core.random.gumbel"){.reference .internal}(\[shape, dtype, key, stream\])                                                    Sample from the standard Gumbel distribution.
  [[`key`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.random.key.html#mlx.core.random.key "mlx.core.random.key"){.reference .internal}(seed)                                                                                         Get a PRNG key from a seed.
  [[`normal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.random.normal.html#mlx.core.random.normal "mlx.core.random.normal"){.reference .internal}(\[shape, dtype, loc, scale, key, stream\])                                        Generate normally distributed random numbers.
  [[`multivariate_normal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.random.multivariate_normal.html#mlx.core.random.multivariate_normal "mlx.core.random.multivariate_normal"){.reference .internal}(mean, cov\[, shape, \...\])   Generate jointly-normal random samples given a mean and covariance.
  [[`randint`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.random.randint.html#mlx.core.random.randint "mlx.core.random.randint"){.reference .internal}(low, high\[, shape, dtype, key, stream\])                                     Generate random integers from the given interval.
  [[`seed`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.random.seed.html#mlx.core.random.seed "mlx.core.random.seed"){.reference .internal}(seed)                                                                                     Seed the global PRNG.
  [[`split`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.random.split.html#mlx.core.random.split "mlx.core.random.split"){.reference .internal}(key\[, num, stream\])                                                                 Split a PRNG key into sub keys.
  [[`truncated_normal`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.random.truncated_normal.html#mlx.core.random.truncated_normal "mlx.core.random.truncated_normal"){.reference .internal}(lower, upper\[, shape, \...\])            Generate values from a truncated normal distribution.
  [[`uniform`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.random.uniform.html#mlx.core.random.uniform "mlx.core.random.uniform"){.reference .internal}(\[low, high, shape, dtype, key, stream\])                                     Generate uniformly distributed random numbers.
  [[`laplace`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.random.laplace.html#mlx.core.random.laplace "mlx.core.random.laplace"){.reference .internal}(\[shape, dtype, loc, scale, key, stream\])                                    Sample numbers from a Laplace distribution.
  [[`permutation`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.random.permutation.html#mlx.core.random.permutation "mlx.core.random.permutation"){.reference .internal}(x\[, axis, key, stream\])                                     Generate a random permutation or permute the entries of an array.
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------
:::
::::::::

::::: prev-next-area
[](_autosummary/mlx.core.zeros_like.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.zeros_like
:::

[](_autosummary/mlx.core.random.bernoulli.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.random.bernoulli
:::
:::::
::::::::::::::::::::::::
:::::::::::::::::::::::::

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
::::::::::::::::::::::::::::::::
