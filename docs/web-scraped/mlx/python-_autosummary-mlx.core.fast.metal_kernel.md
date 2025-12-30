# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fast.metal_kernel.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.fast.metal_kernel.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.fast.metal_kernel

## Contents

- [[`metal_kernel()`]](#mlx.core.fast.metal_kernel)

# mlx.core.fast.metal_kernel[\#](#mlx-core-fast-metal-kernel "Link to this heading")

[[metal_kernel]][(]*[[name]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[input_names]][[:]][ ][[[Sequence]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]]*, *[[output_names]][[:]][ ][[[Sequence]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]]*, *[[source]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[header]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'\']]*, *[[ensure_row_contiguous]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[atomic_outputs]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)] [[→] [[[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")]][\#](#mlx.core.fast.metal_kernel "Link to this definition")

:   A jit-compiled custom Metal kernel defined from a source string.

    Full documentation: [[Custom Metal Kernels]](../../dev/custom_metal_kernels.html#custom-metal-kernels).

    Parameters[:]

    :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Name for the kernel.

        - **input_names** (*List\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- The parameter names of the inputs in the function signature.

        - **output_names** (*List\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*\]*) -- The parameter names of the outputs in the function signature.

        - **source** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Source code. This is the body of a function in Metal, the function signature will be automatically generated.

        - **header** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- Header source code to include before the main function. Useful for helper functions or includes that should live outside of the main function body.

        - **ensure_row_contiguous** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Whether to ensure the inputs are row contiguous before the kernel runs. Default: [`True`].

        - **atomic_outputs** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Whether to use atomic outputs in the function signature e.g. [`device`]` `[`atomic<float>`]. Default: [`False`].

    Returns[:]

    :   Callable [`metal_kernel`].

    Example

    :::: 
    ::: highlight
        def exp_elementwise(a: mx.array):
            source = '''
                uint elem = thread_position_in_grid.x;
                T tmp = inp[elem];
                out[elem] = metal::exp(tmp);
            '''

            kernel = mx.fast.metal_kernel(
                name="myexp",
                input_names=["inp"],
                output_names=["out"],
                source=source
            )
            outputs = kernel(
                inputs=[a],
                template=[("T", mx.float32)],
                grid=(a.size, 1, 1),
                threadgroup=(256, 1, 1),
                output_shapes=[a.shape],
                output_dtypes=[a.dtype],
                verbose=True,
            )
            return outputs[0]

        a = mx.random.normal(shape=(4, 16)).astype(mx.float16)
        b = exp_elementwise(a)
        assert mx.allclose(b, mx.exp(a))
    :::
    ::::

[](mlx.core.fast.scaled_dot_product_attention.html "previous page")

previous

mlx.core.fast.scaled_dot_product_attention

[](mlx.core.fast.cuda_kernel.html "next page")

next

mlx.core.fast.cuda_kernel

Contents

- [[`metal_kernel()`]](#mlx.core.fast.metal_kernel)

By MLX Contributors

© Copyright 2023, Apple.\