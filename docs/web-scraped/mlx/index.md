# Source: https://ml-explore.github.io/mlx/build/html/index.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](_sources/index.rst "Download source file")
- [ ] [.pdf]

[ ]

# MLX

# MLX[\#](#mlx "Link to this heading")

MLX is a NumPy-like array framework designed for efficient and flexible machine learning on Apple silicon, brought to you by Apple machine learning research.

The Python API closely follows NumPy with a few exceptions. MLX also has a fully featured C++ API which closely follows the Python API.

The main differences between MLX and NumPy are:

> ::: 
> - **Composable function transformations**: MLX has composable function transformations for automatic differentiation, automatic vectorization, and computation graph optimization.
>
> - **Lazy computation**: Computations in MLX are lazy. Arrays are only materialized when needed.
>
> - **Multi-device**: Operations can run on any of the supported devices (CPU, GPU, ...)
> :::

The design of MLX is inspired by frameworks like [PyTorch](https://pytorch.org/), [Jax](https://github.com/google/jax), and [ArrayFire](https://arrayfire.org/). A notable difference from these frameworks and MLX is the *unified memory model*. Arrays in MLX live in shared memory. Operations on MLX arrays can be performed on any of the supported device types without performing data copies. Currently supported device types are the CPU and GPU.

[Install]

- [Build and Install](install.html)

[Usage]

- [Quick Start Guide](usage/quick_start.html)
- [Lazy Evaluation](usage/lazy_evaluation.html)
- [Unified Memory](usage/unified_memory.html)
- [Indexing Arrays](usage/indexing.html)
- [Saving and Loading Arrays](usage/saving_and_loading.html)
- [Function Transforms](usage/function_transforms.html)
- [Compilation](usage/compile.html)
- [Conversion to NumPy and Other Frameworks](usage/numpy.html)
- [Distributed Communication](usage/distributed.html)
- [Using Streams](usage/using_streams.html)
- [Exporting Functions](usage/export.html)

[Examples]

- [Linear Regression](examples/linear_regression.html)
- [Multi-Layer Perceptron](examples/mlp.html)
- [LLM inference](examples/llama-inference.html)

[Python API Reference]

- [Array](python/array.html)
- [Data Types](python/data_types.html)
- [Devices and Streams](python/devices_and_streams.html)
- [Export Functions](python/export.html)
- [Operations](python/ops.html)
- [Random](python/random.html)
- [Transforms](python/transforms.html)
- [Fast](python/fast.html)
- [FFT](python/fft.html)
- [Linear Algebra](python/linalg.html)
- [Metal](python/metal.html)
- [CUDA](python/cuda.html)
- [Memory Management](python/memory_management.html)
- [Neural Networks](python/nn.html)
- [Optimizers](python/optimizers.html)
- [Distributed Communication](python/distributed.html)
- [Tree Utils](python/tree_utils.html)

[C++ API Reference]

- [Operations](cpp/ops.html)

[Further Reading]

- [Custom Extensions in MLX](dev/extensions.html)
- [Metal Debugger](dev/metal_debugger.html)
- [Metal Logging](dev/metal_logging.html)
- [Custom Metal Kernels](dev/custom_metal_kernels.html)
- [Using MLX in C++](dev/mlx_in_cpp.html)

[](install.html "next page")

next

Build and Install

By MLX Contributors

© Copyright 2023, Apple.\