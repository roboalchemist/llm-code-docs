# Source: https://ml-explore.github.io/mlx/build/html/python/transforms.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../_sources/python/transforms.rst "Download source file")
- [ ] [.pdf]

[ ]

# Transforms

[]

# Transforms[\#](#transforms "Link to this heading")

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`eval`]](_autosummary/mlx.core.eval.html#mlx.core.eval "mlx.core.eval")(\*args)                                                               Evaluate an [[`array`]](_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array") or tree of [[`array`]](_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array").
  [[`async_eval`]](_autosummary/mlx.core.async_eval.html#mlx.core.async_eval "mlx.core.async_eval")(\*args)                                       Asynchronously evaluate an [[`array`]](_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array") or tree of [[`array`]](_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array").
  [[`compile`]](_autosummary/mlx.core.compile.html#mlx.core.compile "mlx.core.compile")(fun\[, inputs, outputs, shapeless\])                      Returns a compiled function which produces the same output as [`fun`].
  [[`custom_function`]](_autosummary/mlx.core.custom_function.html#mlx.core.custom_function "mlx.core.custom_function")                           Set up a function for custom gradient and vmap definitions.
  [[`disable_compile`]](_autosummary/mlx.core.disable_compile.html#mlx.core.disable_compile "mlx.core.disable_compile")()                         Globally disable compilation.
  [[`enable_compile`]](_autosummary/mlx.core.enable_compile.html#mlx.core.enable_compile "mlx.core.enable_compile")()                             Globally enable compilation.
  [[`grad`]](_autosummary/mlx.core.grad.html#mlx.core.grad "mlx.core.grad")(fun\[, argnums, argnames\])                                           Returns a function which computes the gradient of [`fun`].
  [[`value_and_grad`]](_autosummary/mlx.core.value_and_grad.html#mlx.core.value_and_grad "mlx.core.value_and_grad")(fun\[, argnums, argnames\])   Returns a function which computes the value and gradient of [`fun`].
  [[`jvp`]](_autosummary/mlx.core.jvp.html#mlx.core.jvp "mlx.core.jvp")(fun, primals, tangents)                                                   Compute the Jacobian-vector product.
  [[`vjp`]](_autosummary/mlx.core.vjp.html#mlx.core.vjp "mlx.core.vjp")(fun, primals, cotangents)                                                 Compute the vector-Jacobian product.
  [[`vmap`]](_autosummary/mlx.core.vmap.html#mlx.core.vmap "mlx.core.vmap")(fun\[, in_axes, out_axes\])                                           Returns a vectorized version of [`fun`].
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[](_autosummary/mlx.core.random.permutation.html "previous page")

previous

mlx.core.random.permutation

[](_autosummary/mlx.core.eval.html "next page")

next

mlx.core.eval

By MLX Contributors

© Copyright 2023, Apple.\