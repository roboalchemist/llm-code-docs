# Source: https://ml-explore.github.io/mlx/build/html/python/linalg.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../_sources/python/linalg.rst "Download source file")
- [ ] [.pdf]

[ ]

# Linear Algebra

[]

# Linear Algebra[\#](#linear-algebra "Link to this heading")

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`inv`]](_autosummary/mlx.core.linalg.inv.html#mlx.core.linalg.inv "mlx.core.linalg.inv")(a, \*\[, stream\])                                                                 Compute the inverse of a square matrix.
  [[`tri_inv`]](_autosummary/mlx.core.linalg.tri_inv.html#mlx.core.linalg.tri_inv "mlx.core.linalg.tri_inv")(a\[, upper, stream\])                                              Compute the inverse of a triangular square matrix.
  [[`norm`]](_autosummary/mlx.core.linalg.norm.html#mlx.core.linalg.norm "mlx.core.linalg.norm")(a, /\[, ord, axis, keepdims, stream\])                                         Matrix or vector norm.
  [[`cholesky`]](_autosummary/mlx.core.linalg.cholesky.html#mlx.core.linalg.cholesky "mlx.core.linalg.cholesky")(a\[, upper, stream\])                                          Compute the Cholesky decomposition of a real symmetric positive semi-definite matrix.
  [[`cholesky_inv`]](_autosummary/mlx.core.linalg.cholesky_inv.html#mlx.core.linalg.cholesky_inv "mlx.core.linalg.cholesky_inv")(L\[, upper, stream\])                          Compute the inverse of a real symmetric positive semi-definite matrix using it\'s Cholesky decomposition.
  [[`cross`]](_autosummary/mlx.core.linalg.cross.html#mlx.core.linalg.cross "mlx.core.linalg.cross")(a, b\[, axis, stream\])                                                    Compute the cross product of two arrays along a specified axis.
  [[`qr`]](_autosummary/mlx.core.linalg.qr.html#mlx.core.linalg.qr "mlx.core.linalg.qr")(a, \*\[, stream\])                                                                     The QR factorization of the input matrix.
  [[`svd`]](_autosummary/mlx.core.linalg.svd.html#mlx.core.linalg.svd "mlx.core.linalg.svd")(a\[, compute_uv, stream\])                                                         The Singular Value Decomposition (SVD) of the input matrix.
  [[`eigvals`]](_autosummary/mlx.core.linalg.eigvals.html#mlx.core.linalg.eigvals "mlx.core.linalg.eigvals")(a, \*\[, stream\])                                                 Compute the eigenvalues of a square matrix.
  [[`eig`]](_autosummary/mlx.core.linalg.eig.html#mlx.core.linalg.eig "mlx.core.linalg.eig")(a, \*\[, stream\])                                                                 Compute the eigenvalues and eigenvectors of a square matrix.
  [[`eigvalsh`]](_autosummary/mlx.core.linalg.eigvalsh.html#mlx.core.linalg.eigvalsh "mlx.core.linalg.eigvalsh")(a\[, UPLO, stream\])                                           Compute the eigenvalues of a complex Hermitian or real symmetric matrix.
  [[`eigh`]](_autosummary/mlx.core.linalg.eigh.html#mlx.core.linalg.eigh "mlx.core.linalg.eigh")(a\[, UPLO, stream\])                                                           Compute the eigenvalues and eigenvectors of a complex Hermitian or real symmetric matrix.
  [[`lu`]](_autosummary/mlx.core.linalg.lu.html#mlx.core.linalg.lu "mlx.core.linalg.lu")(a, \*\[, stream\])                                                                     Compute the LU factorization of the given matrix [`A`].
  [[`lu_factor`]](_autosummary/mlx.core.linalg.lu_factor.html#mlx.core.linalg.lu_factor "mlx.core.linalg.lu_factor")(a, \*\[, stream\])                                         Computes a compact representation of the LU factorization.
  [[`pinv`]](_autosummary/mlx.core.linalg.pinv.html#mlx.core.linalg.pinv "mlx.core.linalg.pinv")(a, \*\[, stream\])                                                             Compute the (Moore-Penrose) pseudo-inverse of a matrix.
  [[`solve`]](_autosummary/mlx.core.linalg.solve.html#mlx.core.linalg.solve "mlx.core.linalg.solve")(a, b, \*\[, stream\])                                                      Compute the solution to a system of linear equations [`AX`]` `[`=`]` `[`B`].
  [[`solve_triangular`]](_autosummary/mlx.core.linalg.solve_triangular.html#mlx.core.linalg.solve_triangular "mlx.core.linalg.solve_triangular")(a, b, \*\[, upper, stream\])   Computes the solution of a triangular system of linear equations [`AX`]` `[`=`]` `[`B`].
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[](_autosummary/mlx.core.fft.ifftshift.html "previous page")

previous

mlx.core.fft.ifftshift

[](_autosummary/mlx.core.linalg.inv.html "next page")

next

mlx.core.linalg.inv

By MLX Contributors

© Copyright 2023, Apple.\