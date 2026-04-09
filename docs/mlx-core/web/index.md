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
  [.rst]{.btn__text-container}](_sources/index.rst "Download source file"){.btn
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
# MLX

:::: {#print-main-content}
::: {#jb-print-toc}
:::
::::
:::::

::: {#searchbox}
:::

::::::::: {#mlx .section}
# MLX[\#](#mlx "Link to this heading"){.headerlink}

MLX is a NumPy-like array framework designed for efficient and flexible
machine learning on Apple silicon, brought to you by Apple machine
learning research.

The Python API closely follows NumPy with a few exceptions. MLX also has
a fully featured C++ API which closely follows the Python API.

The main differences between MLX and NumPy are:

> ::: {}
> - **Composable function transformations**: MLX has composable function
>   transformations for automatic differentiation, automatic
>   vectorization, and computation graph optimization.
>
> - **Lazy computation**: Computations in MLX are lazy. Arrays are only
>   materialized when needed.
>
> - **Multi-device**: Operations can run on any of the supported devices
>   (CPU, GPU, ...)
> :::

The design of MLX is inspired by frameworks like
[PyTorch](https://pytorch.org/){.reference .external},
[Jax](https://github.com/google/jax){.reference .external}, and
[ArrayFire](https://arrayfire.org/){.reference .external}. A notable
difference from these frameworks and MLX is the *unified memory model*.
Arrays in MLX live in shared memory. Operations on MLX arrays can be
performed on any of the supported device types without performing data
copies. Currently supported device types are the CPU and GPU.

::: {.toctree-wrapper .compound}
[Install]{.caption-text}

- [Build and Install](install.html){.reference .internal}
:::

::: {.toctree-wrapper .compound}
[Usage]{.caption-text}

- [Quick Start Guide](usage/quick_start.html){.reference .internal}
- [Lazy Evaluation](usage/lazy_evaluation.html){.reference .internal}
- [Unified Memory](usage/unified_memory.html){.reference .internal}
- [Indexing Arrays](usage/indexing.html){.reference .internal}
- [Saving and Loading Arrays](usage/saving_and_loading.html){.reference
  .internal}
- [Function Transforms](usage/function_transforms.html){.reference
  .internal}
- [Compilation](usage/compile.html){.reference .internal}
- [Conversion to NumPy and Other
  Frameworks](usage/numpy.html){.reference .internal}
- [Distributed Communication](usage/distributed.html){.reference
  .internal}
- [Using Streams](usage/using_streams.html){.reference .internal}
- [Exporting Functions](usage/export.html){.reference .internal}
:::

::: {.toctree-wrapper .compound}
[Examples]{.caption-text}

- [Linear Regression](examples/linear_regression.html){.reference
  .internal}
- [Multi-Layer Perceptron](examples/mlp.html){.reference .internal}
- [LLM inference](examples/llama-inference.html){.reference .internal}
- [Data Parallelism](examples/data_parallelism.html){.reference
  .internal}
- [Tensor Parallelism](examples/tensor_parallelism.html){.reference
  .internal}
:::

::: {.toctree-wrapper .compound}
[Python API Reference]{.caption-text}

- [Array](python/array.html){.reference .internal}
- [Data Types](python/data_types.html){.reference .internal}
- [Devices and Streams](python/devices_and_streams.html){.reference
  .internal}
- [Export Functions](python/export.html){.reference .internal}
- [Operations](python/ops.html){.reference .internal}
- [Random](python/random.html){.reference .internal}
- [Transforms](python/transforms.html){.reference .internal}
- [Fast](python/fast.html){.reference .internal}
- [FFT](python/fft.html){.reference .internal}
- [Linear Algebra](python/linalg.html){.reference .internal}
- [Metal](python/metal.html){.reference .internal}
- [CUDA](python/cuda.html){.reference .internal}
- [Memory Management](python/memory_management.html){.reference
  .internal}
- [Neural Networks](python/nn.html){.reference .internal}
- [Optimizers](python/optimizers.html){.reference .internal}
- [Distributed Communication](python/distributed.html){.reference
  .internal}
- [Tree Utils](python/tree_utils.html){.reference .internal}
:::

::: {.toctree-wrapper .compound}
[C++ API Reference]{.caption-text}

- [Operations](cpp/ops.html){.reference .internal}
:::

::: {.toctree-wrapper .compound}
[Further Reading]{.caption-text}

- [Custom Extensions in MLX](dev/extensions.html){.reference .internal}
- [Metal Debugger](dev/metal_debugger.html){.reference .internal}
- [Metal Logging](dev/metal_logging.html){.reference .internal}
- [Custom Metal Kernels](dev/custom_metal_kernels.html){.reference
  .internal}
- [Using MLX in C++](dev/mlx_in_cpp.html){.reference .internal}
:::
:::::::::

:::: prev-next-area
[](install.html "next page"){.right-next}

::: prev-next-info
next

Build and Install
:::
::::
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
