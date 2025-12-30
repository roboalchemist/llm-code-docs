# Source: https://ml-explore.github.io/mlx/build/html/dev/extensions.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../_sources/dev/extensions.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# Custom Extensions in MLX

## Contents

- [Introducing the Example](#introducing-the-example)
- [Operations and Primitives](#operations-and-primitives)
  - [Operations](#operations)
  - [Primitives](#primitives)
  - [Using the Primitive](#using-the-primitive)
- [Implementing the Primitive](#implementing-the-primitive)
  - [Implementing the CPU Back-end](#implementing-the-cpu-back-end)
  - [Implementing the GPU Back-end](#implementing-the-gpu-back-end)
  - [Primitive Transforms](#primitive-transforms)
- [Building and Binding](#building-and-binding)
  - [Binding to Python](#binding-to-python)
  - [Building with CMake](#building-with-cmake)
  - [Building with [`setuptools`]](#building-with-setuptools)
- [Usage](#usage)
  - [Results](#results)
- [Scripts](#scripts)

# Custom Extensions in MLX[\#](#custom-extensions-in-mlx "Link to this heading")

You can extend MLX with custom operations on the CPU or GPU. This guide explains how to do that with a simple example.

## Introducing the Example[\#](#introducing-the-example "Link to this heading")

Let's say you would like an operation that takes in two arrays, [`x`] and [`y`], scales them both by coefficients [`alpha`] and [`beta`] respectively, and then adds them together to get the result [`z`]` `[`=`]` `[`alpha`]` `[`*`]` `[`x`]` `[`+`]` `[`beta`]` `[`*`]` `[`y`]. You can do that in MLX directly:

    import mlx.core as mx

    def simple_axpby(x: mx.array, y: mx.array, alpha: float, beta: float) -> mx.array:
        return alpha * x + beta * y

This function performs that operation while leaving the implementation and function transformations to MLX.

However, you may want to customize the underlying implementation, perhaps to make it faster. In this tutorial we will go through adding custom extensions. It will cover:

- The structure of the MLX library.

- Implementing a CPU operation.

- Implementing a GPU operation using metal.

- Adding the [`vjp`] and [`jvp`] function transformation.

- Building a custom extension and binding it to python.

## Operations and Primitives[\#](#operations-and-primitives "Link to this heading")

Operations in MLX build the computation graph. Primitives provide the rules for evaluating and transforming the graph. Let's start by discussing operations in more detail.

### Operations[\#](#operations "Link to this heading")

Operations are the front-end functions that operate on arrays. They are defined in the C++ API ([[Operations]](../cpp/ops.html#cpp-ops)), and the Python API ([[Operations]](../python/ops.html#ops)) binds them.

We would like an operation [`axpby()`] that takes in two arrays, [`x`] and [`y`], and two scalars, [`alpha`] and [`beta`]. This is how to define it in C++:

    /**
    *  Scale and sum two vectors element-wise
    *  z = alpha * x + beta * y
    *
    *  Use NumPy-style broadcasting between x and y
    *  Inputs are upcasted to floats if needed
    **/
    array axpby(
        const array& x, // Input array x
        const array& y, // Input array y
        const float alpha, // Scaling factor for x
        const float beta, // Scaling factor for y
        StreamOrDevice s =  // Stream on which to schedule the operation
    );

The simplest way to implement this is with existing operations:

    array axpby(
        const array& x, // Input array x
        const array& y, // Input array y
        const float alpha, // Scaling factor for x
        const float beta, // Scaling factor for y
        StreamOrDevice s /* =  */ // Stream on which to schedule the operation
    ) 

The operations themselves do not contain the implementations that act on the data, nor do they contain the rules of transformations. Rather, they are an easy to use interface that use [`Primitive`] building blocks.

### Primitives[\#](#primitives "Link to this heading")

A [`Primitive`] is part of the computation graph of an [`array`]. It defines how to create output arrays given input arrays. Further, a [`Primitive`] has methods to run on the CPU or GPU and for function transformations such as [`vjp`] and [`jvp`]. Let's go back to our example to be more concrete:

    class Axpby : public Primitive ;

        /**
        * A primitive must know how to evaluate itself on the CPU/GPU
        * for the given inputs and populate the output array.
        *
        * To avoid unnecessary allocations, the evaluation function
        * is responsible for allocating space for the array.
        */
        void eval_cpu(
            const std::vector<array>& inputs,
            std::vector<array>& outputs) override;
        void eval_gpu(
            const std::vector<array>& inputs,
            std::vector<array>& outputs) override;

        /** The Jacobian-vector product. */
        std::vector<array> jvp(
            const std::vector<array>& primals,
            const std::vector<array>& tangents,
            const std::vector<int>& argnums) override;

        /** The vector-Jacobian product. */
        std::vector<array> vjp(
            const std::vector<array>& primals,
            const std::vector<array>& cotangents,
            const std::vector<int>& argnums,
            const std::vector<array>& outputs) override;

        /**
        * The primitive must know how to vectorize itself across
        * the given axes. The output is a pair containing the array
        * representing the vectorized computation and the axis which
        * corresponds to the output vectorized dimension.
        */
        std::pair<std::vector<array>, std::vector<int>> vmap(
            const std::vector<array>& inputs,
            const std::vector<int>& axes) override;

        /** The name of primitive. */
        const char* name() const override 

        /** Equivalence check **/
        bool is_equivalent(const Primitive& other) const override;

      private:
        float alpha_;
        float beta_;
    };

The [`Axpby`] class derives from the base [`Primitive`] class. The [`Axpby`] treats [`alpha`] and [`beta`] as parameters. It then provides implementations of how the output array is produced given the inputs through [`Axpby::eval_cpu()`] and [`Axpby::eval_gpu()`]. It also provides rules of transformations in [`Axpby::jvp()`], [`Axpby::vjp()`], and [`Axpby::vmap()`].

### Using the Primitive[\#](#using-the-primitive "Link to this heading")

Operations can use this [`Primitive`] to add a new [`array`] to the computation graph. An [`array`] can be constructed by providing its data type, shape, the [`Primitive`] that computes it, and the [`array`] inputs that are passed to the primitive.

Let's reimplement our operation now in terms of our [`Axpby`] primitive.

    array axpby(
        const array& x, // Input array x
        const array& y, // Input array y
        const float alpha, // Scaling factor for x
        const float beta, // Scaling factor for y
        StreamOrDevice s /* =  */ // Stream on which to schedule the operation
    ) , s);
        auto out_shape = broadcasted_inputs[0].shape();

        // Construct the array as the output of the Axpby primitive
        // with the broadcasted and upcasted arrays as inputs
        return array(
            /* const std::vector<int>& shape = */ out_shape,
            /* Dtype dtype = */ out_dtype,
            /* std::unique_ptr<Primitive> primitive = */
            std::make_shared<Axpby>(to_stream(s), alpha, beta),
            /* const std::vector<array>& inputs = */ broadcasted_inputs);
    }

This operation now handles the following:

1.  Upcast inputs and resolve the output data type.

2.  Broadcast the inputs and resolve the output shape.

3.  Construct the primitive [`Axpby`] using the given stream, [`alpha`], and [`beta`].

4.  Construct the output [`array`] using the primitive and the inputs.

## Implementing the Primitive[\#](#implementing-the-primitive "Link to this heading")

No computation happens when we call the operation alone. The operation only builds the computation graph. When we evaluate the output array, MLX schedules the execution of the computation graph, and calls [`Axpby::eval_cpu()`] or [`Axpby::eval_gpu()`] depending on the stream/device specified by the user.

Warning

When [`Primitive::eval_cpu()`] or [`Primitive::eval_gpu()`] are called, no memory has been allocated for the output array. It falls on the implementation of these functions to allocate memory as needed.

### Implementing the CPU Back-end[\#](#implementing-the-cpu-back-end "Link to this heading")

Let's start by implementing [`Axpby::eval_cpu()`].

The method will go over each element of the output array, find the corresponding input elements of [`x`] and [`y`] and perform the operation point-wise. This is captured in the templated function [`axpby_impl()`].

    template <typename T>
    void axpby_impl(
        const mx::array& x,
        const mx::array& y,
        mx::array& out,
        float alpha_,
        float beta_,
        mx::Stream stream) 
      });
    }

Our implementation should work for all incoming floating point arrays. Accordingly, we add dispatches for [`float32`], [`float16`], [`bfloat16`] and [`complex64`]. We throw an error if we encounter an unexpected type.

    void Axpby::eval_cpu(
        const std::vector<mx::array>& inputs,
        std::vector<mx::array>& outputs)  else if (out.dtype() == mx::float16)  else if (out.dtype() == mx::bfloat16)  else if (out.dtype() == mx::complex64)  else 
    }

Just this much is enough to run the operation [`axpby()`] on a CPU stream! If you do not plan on running the operation on the GPU or using transforms on computation graphs that contain [`Axpby`], you can stop implementing the primitive here.

### Implementing the GPU Back-end[\#](#implementing-the-gpu-back-end "Link to this heading")

Apple silicon devices address their GPUs using the [Metal](https://developer.apple.com/documentation/metal?language=objc) shading language, and GPU kernels in MLX are written using Metal.

Note

Here are some helpful resources if you are new to Metal:

- A walkthrough of the metal compute pipeline: [Metal Example](https://developer.apple.com/documentation/metal/performing_calculations_on_a_gpu?language=objc)

- Documentation for metal shading language: [Metal Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf)

- Using metal from C++: [Metal-cpp](https://developer.apple.com/metal/cpp/)

Let's keep the GPU kernel simple. We will launch exactly as many threads as there are elements in the output. Each thread will pick the element it needs from [`x`] and [`y`], do the point-wise operation, and update its assigned element in the output.

    template <typename T>
    [[kernel]] void axpby_general(
            device const T* x [[buffer(0)]],
            device const T* y [[buffer(1)]],
            device T* out [[buffer(2)]],
            constant const float& alpha [[buffer(3)]],
            constant const float& beta [[buffer(4)]],
            constant const int* shape [[buffer(5)]],
            constant const int64_t* x_strides [[buffer(6)]],
            constant const int64_t* y_strides [[buffer(7)]],
            constant const int& ndim [[buffer(8)]],
            uint index [[thread_position_in_grid]]) 

We then need to instantiate this template for all floating point types and give each instantiation a unique host name so we can identify it.

    instantiate_kernel("axpby_general_float32", axpby_general, float)
    instantiate_kernel("axpby_general_float16", axpby_general, float16_t)
    instantiate_kernel("axpby_general_bfloat16", axpby_general, bfloat16_t)
    instantiate_kernel("axpby_general_complex64", axpby_general, complex64_t)

The logic to determine the kernel, set the inputs, resolve the grid dimensions, and dispatch to the GPU are contained in [`Axpby::eval_gpu()`] as shown below.

    /** Evaluate primitive on GPU */
    void Axpby::eval_gpu(
      const std::vector<array>& inputs,
      std::vector<array>& outputs) 

We can now call the [`axpby()`] operation on both the CPU and the GPU!

A few things to note about MLX and Metal before moving on. MLX keeps track of the active [`command_buffer`] and the [`MTLCommandBuffer`] to which it is associated. We rely on [`d.get_command_encoder()`] to give us the active metal compute command encoder instead of building a new one and calling [`compute_encoder->end_encoding()`] at the end. MLX adds kernels (compute pipelines) to the active command buffer until some specified limit is hit or the command buffer needs to be flushed for synchronization.

### Primitive Transforms[\#](#primitive-transforms "Link to this heading")

Next, let's add implementations for transformations in a [`Primitive`]. These transformations can be built on top of other operations, including the one we just defined:

    /** The Jacobian-vector product. */
    std::vector<array> Axpby::jvp(
            const std::vector<array>& primals,
            const std::vector<array>& tangents,
            const std::vector<int>& argnums) , we only push along x in which case the
        // jvp is just the tangent scaled by alpha
        // Similarly, if argnums = , the jvp is just the tangent
        // scaled by beta
        if (argnums.size() > 1) ;
        }
        // If argnums = , we take contributions from both
        // which gives us jvp = tangent_x * alpha + tangent_y * beta
        else ;
        }
    }

    /** The vector-Jacobian product. */
    std::vector<array> Axpby::vjp(
            const std::vector<array>& primals,
            const std::vector<array>& cotangents,
            const std::vector<int>& argnums,
            const std::vector<int>& /* unused */) 
        return vjps;
    }

Note, a transformation does not need to be fully defined to start using the [`Primitive`].

    /** Vectorize primitive along given axis */
    std::pair<std::vector<array>, std::vector<int>> Axpby::vmap(
            const std::vector<array>& inputs,
            const std::vector<int>& axes) 

## Building and Binding[\#](#building-and-binding "Link to this heading")

Let's look at the overall directory structure first.

extensions

├── axpby

│ ├── axpby.cpp

│ ├── axpby.h

│ └── axpby.metal

├── mlx_sample_extensions

│ └── \_\_init\_\_.py

├── bindings.cpp

├── CMakeLists.txt

└── setup.py

- [`extensions/axpby/`] defines the C++ extension library

- [`extensions/mlx_sample_extensions`] sets out the structure for the associated Python package

- [`extensions/bindings.cpp`] provides Python bindings for our operation

- [`extensions/CMakeLists.txt`] holds CMake rules to build the library and Python bindings

- [`extensions/setup.py`] holds the [`setuptools`] rules to build and install the Python package

### Binding to Python[\#](#binding-to-python "Link to this heading")

We use [nanobind](https://nanobind.readthedocs.io/en/latest/) to build a Python API for the C++ library. Since bindings for components such as [[`mlx.core.array`]](../python/_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"), [[`mlx.core.stream`]](../python/_autosummary/mlx.core.stream.html#mlx.core.stream "mlx.core.stream"), etc. are already provided, adding our [`axpby()`] is simple.

    NB_MODULE(_ext, m) 

Most of the complexity in the above example comes from additional bells and whistles such as the literal names and doc-strings.

Warning

[`mlx.core`] must be imported before importing [`mlx_sample_extensions`] as defined by the nanobind module above to ensure that the casters for [`mlx.core`] components like [[`mlx.core.array`]](../python/_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array") are available.

[]

### Building with CMake[\#](#building-with-cmake "Link to this heading")

Building the C++ extension library only requires that you [`find_package(MLX`]` `[`CONFIG)`] and then link it to your library.

    # Add library
    add_library(mlx_ext)

    # Add sources
    target_sources(
        mlx_ext
        PUBLIC
        $/axpby/axpby.cpp
    )

    # Add include headers
    target_include_directories(
        mlx_ext PUBLIC $
    )

    # Link to mlx
    target_link_libraries(mlx_ext PUBLIC mlx)

We also need to build the attached Metal library. For convenience, we provide a [`mlx_build_metallib()`] function that builds a [`.metallib`] target given sources, headers, destinations, etc. (defined in [`cmake/extension.cmake`] and automatically imported with MLX package).

Here is what that looks like in practice:

    # Build metallib
    if(MLX_BUILD_METAL)

    mlx_build_metallib(
        TARGET mlx_ext_metallib
        TITLE mlx_ext
        SOURCES $/axpby/axpby.metal
        INCLUDE_DIRS $ $
        OUTPUT_DIRECTORY $
    )

    add_dependencies(
        mlx_ext
        mlx_ext_metallib
    )

    endif()

Finally, we build the [nanobind](https://nanobind.readthedocs.io/en/latest/) bindings

    nanobind_add_module(
      _ext
      NB_STATIC STABLE_ABI LTO NOMINSIZE
      NB_DOMAIN mlx
      $/bindings.cpp
    )
    target_link_libraries(_ext PRIVATE mlx_ext)

    if(BUILD_SHARED_LIBS)
      target_link_options(_ext PRIVATE -Wl,-rpath,@loader_path)
    endif()

### Building with [`setuptools`][\#](#building-with-setuptools "Link to this heading")

Once we have set out the CMake build rules as described above, we can use the build utilities defined in [`mlx.extension`]:

    from mlx import extension
    from setuptools import setup

    if __name__ == "__main__":
        setup(
            name="mlx_sample_extensions",
            version="0.0.0",
            description="Sample C++ and Metal extensions for MLX primitives.",
            ext_modules=[extension.CMakeExtension("mlx_sample_extensions._ext")],
            cmdclass=,
            packages=["mlx_sample_extensions"],
            package_data=,
            extras_require=,
            zip_safe=False,
            python_requires=">=3.8",
        )

Note

We treat [`extensions/mlx_sample_extensions`] as the package directory even though it only contains a [`__init__.py`] to ensure the following:

- [`mlx.core`] must be imported before importing [`_ext`]

- The C++ extension library and the metal library are co-located with the python bindings and copied together if the package is installed

To build the package, first install the build dependencies with [`pip`]` `[`install`]` `[`-r`]` `[`requirements.txt`]. You can then build inplace for development using [`python`]` `[`setup.py`]` `[`build_ext`]` `[`-j8`]` `[`--inplace`] (in [`extensions/`])

This results in the directory structure:

extensions

├── mlx_sample_extensions

│ ├── \_\_init\_\_.py

│ ├── libmlx_ext.dylib \# C++ extension library

│ ├── mlx_ext.metallib \# Metal library

│ └── \_ext.cpython-3x-darwin.so \# Python Binding

...

When you try to install using the command [`python`]` `[`-m`]` `[`pip`]` `[`install`]` `[`.`] (in [`extensions/`]), the package will be installed with the same structure as [`extensions/mlx_sample_extensions`] and the C++ and Metal library will be copied along with the Python binding since they are specified as [`package_data`].

## Usage[\#](#usage "Link to this heading")

After installing the extension as described above, you should be able to simply import the Python package and play with it as you would any other MLX operation.

Let's look at a simple script and its results:

    import mlx.core as mx
    from mlx_sample_extensions import axpby

    a = mx.ones((3, 4))
    b = mx.ones((3, 4))
    c = axpby(a, b, 4.0, 2.0, stream=mx.cpu)

    print(f"c shape: ")
    print(f"c dtype: ")
    print(f"c is correct: ")

Output:

    c shape: [3, 4]
    c dtype: float32
    c is correct: True

### Results[\#](#results "Link to this heading")

Let's run a quick benchmark and see how our new [`axpby`] operation compares with the naive [`simple_axpby()`] we first defined.

    import mlx.core as mx
    from mlx_sample_extensions import axpby
    import time

    def simple_axpby(x: mx.array, y: mx.array, alpha: float, beta: float) -> mx.array:
        return alpha * x + beta * y

    M = 4096
    N = 4096

    x = mx.random.normal((M, N))
    y = mx.random.normal((M, N))
    alpha = 4.0
    beta = 2.0

    mx.eval(x, y)

    def bench(f):
        # Warm up
        for i in range(5):
            z = f(x, y, alpha, beta)
            mx.eval(z)

        # Timed run
        s = time.time()
        for i in range(100):
            z = f(x, y, alpha, beta)
            mx.eval(z)
        e = time.time()
        return 1000 * (e - s) / 100

    simple_time = bench(simple_axpby)
    custom_time = bench(axpby)

    print(f"Simple axpby:  ms | Custom axpby:  ms")

The results are [`Simple`]` `[`axpby:`]` `[`1.559`]` `[`ms`]` `[`|`]` `[`Custom`]` `[`axpby:`]` `[`0.774`]` `[`ms`]. We see modest improvements right away!

This operation is now good to be used to build other operations, in [[`mlx.nn.Module`]](../python/nn/module.html#mlx.nn.Module "mlx.nn.Module") calls, and also as a part of graph transformations like [`grad()`].

## Scripts[\#](#scripts "Link to this heading")

Download the code

The full example code is available in [mlx](https://github.com/ml-explore/mlx/tree/main/examples/extensions/).

[](../cpp/ops.html "previous page")

previous

Operations

[](metal_debugger.html "next page")

next

Metal Debugger

Contents

- [Introducing the Example](#introducing-the-example)
- [Operations and Primitives](#operations-and-primitives)
  - [Operations](#operations)
  - [Primitives](#primitives)
  - [Using the Primitive](#using-the-primitive)
- [Implementing the Primitive](#implementing-the-primitive)
  - [Implementing the CPU Back-end](#implementing-the-cpu-back-end)
  - [Implementing the GPU Back-end](#implementing-the-gpu-back-end)
  - [Primitive Transforms](#primitive-transforms)
- [Building and Binding](#building-and-binding)
  - [Binding to Python](#binding-to-python)
  - [Building with CMake](#building-with-cmake)
  - [Building with [`setuptools`]](#building-with-setuptools)
- [Usage](#usage)
  - [Results](#results)
- [Scripts](#scripts)

By MLX Contributors

© Copyright 2023, Apple.\