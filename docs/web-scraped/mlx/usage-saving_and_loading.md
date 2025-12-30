# Source: https://ml-explore.github.io/mlx/build/html/usage/saving_and_loading.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../_sources/usage/saving_and_loading.rst "Download source file")
- [ ] [.pdf]

[ ]

# Saving and Loading Arrays

[]

# Saving and Loading Arrays[\#](#saving-and-loading-arrays "Link to this heading")

MLX supports multiple array serialization formats.

+-----------------+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Format          | Extension                                               | Function                                                                                                                                                                                                                                                                                                                                                                                            | Notes                |
+=================+=========================================================+=====================================================================================================================================================================================================================================================================================================================================================================================================+======================+
| NumPy           | [`.npy`]         | [[`save()`]](../python/_autosummary/mlx.core.save.html#mlx.core.save "mlx.core.save")                                                                                                                                                                                                                               | Single arrays only   |
+-----------------+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| NumPy archive   | [`.npz`]         | [[`savez()`]](../python/_autosummary/mlx.core.savez.html#mlx.core.savez "mlx.core.savez") and [[`savez_compressed()`]](../python/_autosummary/mlx.core.savez_compressed.html#mlx.core.savez_compressed "mlx.core.savez_compressed") | Multiple arrays      |
+-----------------+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Safetensors     | [`.safetensors`] | [[`save_safetensors()`]](../python/_autosummary/mlx.core.save_safetensors.html#mlx.core.save_safetensors "mlx.core.save_safetensors")                                                                                                                                                                               | Multiple arrays      |
+-----------------+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| GGUF            | [`.gguf`]        | [[`save_gguf()`]](../python/_autosummary/mlx.core.save_gguf.html#mlx.core.save_gguf "mlx.core.save_gguf")                                                                                                                                                                                                           | Multiple arrays      |
+-----------------+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

: [Serialization Formats][\#](#id1 "Link to this table") 

The [[`load()`]](../python/_autosummary/mlx.core.load.html#mlx.core.load "mlx.core.load") function will load any of the supported serialization formats. It determines the format from the extensions. The output of [[`load()`]](../python/_autosummary/mlx.core.load.html#mlx.core.load "mlx.core.load") depends on the format.

Here's an example of saving a single array to a file:

    >>> a = mx.array([1.0])
    >>> mx.save("array", a)

The array [`a`] will be saved in the file [`array.npy`] (notice the extension is automatically added). Including the extension is optional; if it is missing it will be added. You can load the array with:

    >>> mx.load("array.npy")
    array([1], dtype=float32)

Here's an example of saving several arrays to a single file:

    >>> a = mx.array([1.0])
    >>> b = mx.array([2.0])
    >>> mx.savez("arrays", a, b=b)

For compatibility with [[`numpy.savez()`]](https://numpy.org/doc/stable/reference/generated/numpy.savez.html#numpy.savez "(in NumPy v2.3)") the MLX [[`savez()`]](../python/_autosummary/mlx.core.savez.html#mlx.core.savez "mlx.core.savez") takes arrays as arguments. If the keywords are missing, then default names will be provided. This can be loaded with:

    >>> mx.load("arrays.npz")
    

In this case [[`load()`]](../python/_autosummary/mlx.core.load.html#mlx.core.load "mlx.core.load") returns a dictionary of names to arrays.

The functions [[`save_safetensors()`]](../python/_autosummary/mlx.core.save_safetensors.html#mlx.core.save_safetensors "mlx.core.save_safetensors") and [[`save_gguf()`]](../python/_autosummary/mlx.core.save_gguf.html#mlx.core.save_gguf "mlx.core.save_gguf") are similar to [[`savez()`]](../python/_autosummary/mlx.core.savez.html#mlx.core.savez "mlx.core.savez"), but they take as input a [[`dict`]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") of string names to arrays:

    >>> a = mx.array([1.0])
    >>> b = mx.array([2.0])
    >>> mx.save_safetensors("arrays", )

[](indexing.html "previous page")

previous

Indexing Arrays

[](function_transforms.html "next page")

next

Function Transforms

By MLX Contributors

© Copyright 2023, Apple.\