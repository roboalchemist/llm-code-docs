:::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::: bd-content
:::::::::::::::::::: bd-article-container
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
  [.rst]{.btn__text-container}](../_sources/python/linalg.rst "Download source file"){.btn
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
# Linear Algebra

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

:::: {#linear-algebra .section}
[]{#linalg}

# Linear Algebra[\#](#linear-algebra "Link to this heading"){.headerlink}

::: pst-scrollable-table-container
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`inv`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.inv.html#mlx.core.linalg.inv "mlx.core.linalg.inv"){.reference .internal}(a, \*\[, stream\])                                                                 Compute the inverse of a square matrix.
  [[`tri_inv`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.tri_inv.html#mlx.core.linalg.tri_inv "mlx.core.linalg.tri_inv"){.reference .internal}(a\[, upper, stream\])                                              Compute the inverse of a triangular square matrix.
  [[`norm`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.norm.html#mlx.core.linalg.norm "mlx.core.linalg.norm"){.reference .internal}(a, /\[, ord, axis, keepdims, stream\])                                         Matrix or vector norm.
  [[`cholesky`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.cholesky.html#mlx.core.linalg.cholesky "mlx.core.linalg.cholesky"){.reference .internal}(a\[, upper, stream\])                                          Compute the Cholesky decomposition of a real symmetric positive semi-definite matrix.
  [[`cholesky_inv`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.cholesky_inv.html#mlx.core.linalg.cholesky_inv "mlx.core.linalg.cholesky_inv"){.reference .internal}(L\[, upper, stream\])                          Compute the inverse of a real symmetric positive semi-definite matrix using it\'s Cholesky decomposition.
  [[`cross`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.cross.html#mlx.core.linalg.cross "mlx.core.linalg.cross"){.reference .internal}(a, b\[, axis, stream\])                                                    Compute the cross product of two arrays along a specified axis.
  [[`qr`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.qr.html#mlx.core.linalg.qr "mlx.core.linalg.qr"){.reference .internal}(a, \*\[, stream\])                                                                     The QR factorization of the input matrix.
  [[`svd`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.svd.html#mlx.core.linalg.svd "mlx.core.linalg.svd"){.reference .internal}(a\[, compute_uv, stream\])                                                         The Singular Value Decomposition (SVD) of the input matrix.
  [[`eigvals`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.eigvals.html#mlx.core.linalg.eigvals "mlx.core.linalg.eigvals"){.reference .internal}(a, \*\[, stream\])                                                 Compute the eigenvalues of a square matrix.
  [[`eig`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.eig.html#mlx.core.linalg.eig "mlx.core.linalg.eig"){.reference .internal}(a, \*\[, stream\])                                                                 Compute the eigenvalues and eigenvectors of a square matrix.
  [[`eigvalsh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.eigvalsh.html#mlx.core.linalg.eigvalsh "mlx.core.linalg.eigvalsh"){.reference .internal}(a\[, UPLO, stream\])                                           Compute the eigenvalues of a complex Hermitian or real symmetric matrix.
  [[`eigh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.eigh.html#mlx.core.linalg.eigh "mlx.core.linalg.eigh"){.reference .internal}(a\[, UPLO, stream\])                                                           Compute the eigenvalues and eigenvectors of a complex Hermitian or real symmetric matrix.
  [[`lu`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.lu.html#mlx.core.linalg.lu "mlx.core.linalg.lu"){.reference .internal}(a, \*\[, stream\])                                                                     Compute the LU factorization of the given matrix [`A`{.docutils .literal .notranslate}]{.pre}.
  [[`lu_factor`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.lu_factor.html#mlx.core.linalg.lu_factor "mlx.core.linalg.lu_factor"){.reference .internal}(a, \*\[, stream\])                                         Computes a compact representation of the LU factorization.
  [[`pinv`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.pinv.html#mlx.core.linalg.pinv "mlx.core.linalg.pinv"){.reference .internal}(a, \*\[, stream\])                                                             Compute the (Moore-Penrose) pseudo-inverse of a matrix.
  [[`solve`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.solve.html#mlx.core.linalg.solve "mlx.core.linalg.solve"){.reference .internal}(a, b, \*\[, stream\])                                                      Compute the solution to a system of linear equations [`AX`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`B`{.docutils .literal .notranslate}]{.pre}.
  [[`solve_triangular`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.core.linalg.solve_triangular.html#mlx.core.linalg.solve_triangular "mlx.core.linalg.solve_triangular"){.reference .internal}(a, b, \*\[, upper, stream\])   Computes the solution of a triangular system of linear equations [`AX`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`B`{.docutils .literal .notranslate}]{.pre}.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
::::

::::: prev-next-area
[](_autosummary/mlx.core.fft.ifftshift.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.fft.ifftshift
:::

[](_autosummary/mlx.core.linalg.inv.html "next page"){.right-next}

::: prev-next-info
next

mlx.core.linalg.inv
:::
:::::
::::::::::::::::::::
:::::::::::::::::::::

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
::::::::::::::::::::::::::::
