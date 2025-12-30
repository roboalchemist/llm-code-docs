# Source: https://ml-explore.github.io/mlx/build/html/python/fast.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../_sources/python/fast.rst "Download source file")
- [ ] [.pdf]

[ ]

# Fast

[]

# Fast[\#](#fast "Link to this heading")

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`rms_norm`]](_autosummary/mlx.core.fast.rms_norm.html#mlx.core.fast.rms_norm "mlx.core.fast.rms_norm")(x, weight, eps, \*\[, stream\])                                                                       Root Mean Square normalization (RMS norm).
  [[`layer_norm`]](_autosummary/mlx.core.fast.layer_norm.html#mlx.core.fast.layer_norm "mlx.core.fast.layer_norm")(x, weight, bias, eps, \*\[, stream\])                                                         Layer normalization.
  [[`rope`]](_autosummary/mlx.core.fast.rope.html#mlx.core.fast.rope "mlx.core.fast.rope")(a, dims, \*, traditional, base, scale, \...)                                                                          Apply rotary positional encoding to the input.
  [[`scaled_dot_product_attention`]](_autosummary/mlx.core.fast.scaled_dot_product_attention.html#mlx.core.fast.scaled_dot_product_attention "mlx.core.fast.scaled_dot_product_attention")(q, k, v, \*, scale)   A fast implementation of multi-head attention: [`O`]` `[`=`]` `[`softmax(Q`]` `[`@`]` `[`K.T,`]` `[`dim=-1)`]` `[`@`]` `[`V`].
  [[`metal_kernel`]](_autosummary/mlx.core.fast.metal_kernel.html#mlx.core.fast.metal_kernel "mlx.core.fast.metal_kernel")(name, input_names, \...\[, \...\])                                                    A jit-compiled custom Metal kernel defined from a source string.
  [[`cuda_kernel`]](_autosummary/mlx.core.fast.cuda_kernel.html#mlx.core.fast.cuda_kernel "mlx.core.fast.cuda_kernel")(name, input_names, output_names, \...)                                                    A jit-compiled custom CUDA kernel defined from a source string.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[](_autosummary/mlx.core.vmap.html "previous page")

previous

mlx.core.vmap

[](_autosummary/mlx.core.fast.rms_norm.html "next page")

next

mlx.core.fast.rms_norm

By MLX Contributors

© Copyright 2023, Apple.\