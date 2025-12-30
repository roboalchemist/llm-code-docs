# Source: https://ml-explore.github.io/mlx/build/html/usage/quick_start.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../_sources/usage/quick_start.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# Quick Start Guide

## Contents

- [Basics](#basics)
- [Function and Graph Transformations](#function-and-graph-transformations)

# Quick Start Guide[\#](#quick-start-guide "Link to this heading")

## Basics[\#](#basics "Link to this heading")

Import [`mlx.core`] and make an [[`array`]](../python/_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"):

    >> import mlx.core as mx
    >> a = mx.array([1, 2, 3, 4])
    >> a.shape
    [4]
    >> a.dtype
    int32
    >> b = mx.array([1.0, 2.0, 3.0, 4.0])
    >> b.dtype
    float32

Operations in MLX are lazy. The outputs of MLX operations are not computed until they are needed. To force an array to be evaluated use [[`eval()`]](../python/_autosummary/mlx.core.eval.html#mlx.core.eval "mlx.core.eval"). Arrays will automatically be evaluated in a few cases. For example, inspecting a scalar with [[`array.item()`]](../python/_autosummary/mlx.core.array.item.html#mlx.core.array.item "mlx.core.array.item"), printing an array, or converting an array from [[`array`]](../python/_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array") to [[`numpy.ndarray`]](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.3)") all automatically evaluate the array.

    >> c = a + b    # c not yet evaluated
    >> mx.eval(c)  # evaluates c
    >> c = a + b
    >> print(c)     # Also evaluates c
    array([2, 4, 6, 8], dtype=float32)
    >> c = a + b
    >> import numpy as np
    >> np.array(c)   # Also evaluates c
    array([2., 4., 6., 8.], dtype=float32)

See the page on [[Lazy Evaluation]](lazy_evaluation.html#lazy-eval) for more details.

## Function and Graph Transformations[\#](#function-and-graph-transformations "Link to this heading")

MLX has standard function transformations like [[`grad()`]](../python/_autosummary/mlx.core.grad.html#mlx.core.grad "mlx.core.grad") and [[`vmap()`]](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap "mlx.core.vmap"). Transformations can be composed arbitrarily. For example [`grad(vmap(grad(fn)))`] (or any other composition) is allowed.

    >> x = mx.array(0.0)
    >> mx.sin(x)
    array(0, dtype=float32)
    >> mx.grad(mx.sin)(x)
    array(1, dtype=float32)
    >> mx.grad(mx.grad(mx.sin))(x)
    array(-0, dtype=float32)

Other gradient transformations include [[`vjp()`]](../python/_autosummary/mlx.core.vjp.html#mlx.core.vjp "mlx.core.vjp") for vector-Jacobian products and [[`jvp()`]](../python/_autosummary/mlx.core.jvp.html#mlx.core.jvp "mlx.core.jvp") for Jacobian-vector products.

Use [[`value_and_grad()`]](../python/_autosummary/mlx.core.value_and_grad.html#mlx.core.value_and_grad "mlx.core.value_and_grad") to efficiently compute both a function's output and gradient with respect to the function's input.

[](../install.html "previous page")

previous

Build and Install

[](lazy_evaluation.html "next page")

next

Lazy Evaluation

Contents

- [Basics](#basics)
- [Function and Graph Transformations](#function-and-graph-transformations)

By MLX Contributors

© Copyright 2023, Apple.\