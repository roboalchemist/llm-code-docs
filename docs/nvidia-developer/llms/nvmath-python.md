# Source: https://developer.nvidia.com/nvmath-python.md

1. [Home](/)

[High Performance Computing](/hpc)

[CUDA-X GPU Accelerated Libraries](/gpu-accelerated-libraries)

nvmath-python

Quick Links

- [Install (pip)](https://docs.nvidia.com/cuda/nvmath-python/latest/installation.html#install-from-pypi)[Install (conda) ](https://docs.nvidia.com/cuda/nvmath-python/latest/installation.html#install-from-conda)[Build from source](https://docs.nvidia.com/cuda/nvmath-python/latest/installation.html#build-from-source)[GitHub](https://github.com/NVIDIA/nvmath-python/)[Documentation](https://docs.nvidia.com/cuda/nvmath-python/index.html)
- 

* * *

![img-alt-text](https://developer.download.nvidia.com/images/cudss-nvmath-python-green-r4@4x_CUT-1.png)

# nvmath-python

**nvmath-python** (Beta) is an [open source library](https://github.com/nvidia/nvmath-python) that bridges the gap between Python scientific community and [NVIDIA CUDA-X™ math Libraries](https://developer.nvidia.com/gpu-accelerated-libraries) by reimagining Python’s performance-oriented APIs. It interoperates with and complements existing array libraries such as NumPy, CuPy, and PyTorch by pushing performance limits to new levels through such capabilities as stateful APIs, just-in-time kernel fusion, custom callbacks, and scaling to many GPUs.   
  
Python practitioners, library developers, and GPU kernel writers are finding **nvmath-python** a powerful tool for getting their scientific, data science, and AI workflows scale with minimum effort.

[Install with pip](https://docs.nvidia.com/cuda/nvmath-python/latest/installation.html#install-from-pypi &quot;Install with pip&quot;)[Install with conda](https://docs.nvidia.com/cuda/nvmath-python/latest/installation.html#install-from-conda &quot;Install with conda&quot;)

**Other Links:**

[Build From Source](https://docs.nvidia.com/cuda/nvmath-python/latest/installation.html#build-from-source &quot;Build from source&quot;)[GitHub](https://github.com/NVIDIA/nvmath-python/ &quot;GitHub&quot;)

* * *

## Key Features  

### Intuitive Pythonic APIs

- 

**nvmath-python** reimagines math library APIs to cover **sophisticated use cases** , which are impossible with _NumPy-like_ APIs without performance compromises. 

- 

**Host APIs** provide both out-of-the-box simplicity and versatility of customization options through optional arguments for accessing all “knobs” of the underlying NVIDIA math libraries. Host APIs are divided into generic and specialized APIs. Generic APIs are intended for a consistent user experience across memory/execution spaces. They may not work with some data types, which are hardware specific and they do not necessarily leverage specific device capabilities. They are great for writing portable code. In contrast, specialized APIs have narrower applications, they may only work on a specific hardware only. They are great for fully leveraging hardware capabilities at the expense of portability.

- 

**Device APIs** allow embedding nvmath-python library calls in custom kernels, written using Python compilers such as numba-cuda. You no longer need to write GEMM or FFT kernels from scratch.

- 

**Host APIs with callbacks** allow embedding custom Python code into nvmath-python calls. Internal JIT machinery compiles the custom code and fuses with nvmath-python operation to achieve peak performance.

- 

**Stateful** (class-form) APIs allow splitting the entire math operation into specification, planning, autotuning, and execution phases. Having an expensive specification, planning, and autotuning done once, allows their cost amortization through multiple subsequent executions.

- 

**Integration with the** [Python logging facility](https://docs.python.org/3/library/logging.html) brings visibility into specification, planning, autotuning, and execution machinery details at runtime.

### Interoperability With Python Ecosystem  

- 

**nvmath-python** works in conjunction with popular Python packages. This includes GPU-based packages like CuPy, PyTorch, and RAPIDS and CPU-based packages like NumPy, SciPy, and scikit-learn. You can keep using familiar data structures and workflows while benefiting from accelerated math operations through **nvmath-python**.

- 

**nvmath-python** is not a replacement for array libraries such as NumPy, CuPy, and PyTorch. It does not implement array APIs for array creation, indexing, and slicing. **nvmath-python** is intended to be used alongside these array libraries. All these dependencies are optional, and you’re free to choose which array library (or multiple libraries) to work with alongside **nvmath-python**.

- 

**nvmath-python** supports CPU and GPU execution and memory spaces. It eases the transition between CPU and GPU implementations as well as allows implementing hybrid CPU-GPU workflows.

- 

In combination with Python compilers, such as [numba-cuda](https://github.com/NVIDIA/numba-cuda), you can implement GPU custom kernels with embedded **nvmath-python** library calls.

### Scalable Performance   

- 

**nvmath-python** pushes performance limits to an edge by delivering performance comparable to the underlying CUDA-X native libraries, such as [cuBLAS family](/cublas), [cuFFT family,](/cufft) [cuDSS](/cudss), and [cuRAND](/curand). With stateful APIs you can amortize the costs of _specification_, _planning_, and _autotuning_ phases through _multiple executions_.

- 

For CPU execution **nvmath-python** leverages the [NVPL library](/nvpl) for the best performance on [NVIDIA Grace™ CPU](https://www.nvidia.com/en-us/data-center/grace-cpu/) platforms. It also supports acceleration of x86 hosts by leveraging the MKL library.

- 

In combination with Python compilers, such as **[numba-cuda,](https://github.com/NVIDIA/numba-cuda)** you can now write highly performant kernels involving GEMM, FFT, and/or RNG operations. Here are just a few examples of impossible made possible with **nvmath-python** :

- 

[DGEMM emulation using int8 tensor cores](https://github.com/NVIDIA/nvmath-python/blob/main/examples/device/cublasdx_fp64_emulation.py)

- 

[Convolution kernel](https://github.com/NVIDIA/nvmath-python/blob/main/examples/device/cufftdx_convolution_performance.py)

- 

[Monte Carlo kernel](https://github.com/NVIDIA/nvmath-python/blob/main/examples/device/curand_philox_uniform4.py)

- 

**nvmath-python** allows scaling beyond a single GPU and even beyond a single node without major coding effort. Multi-GPU multi-node (MGMN) APIs allow easy transition from a single GPU implementation to MGMN and seamlessly scale to thousands of GPUs. The library also offers helper utilities for reshaping data (re-partitioning) as needed without major coding.

* * *

## Supported Operations

### Dense Linear Algebra - Generalized Matrix Multiplication  

The library offers a GEneralized Matrix Multiplication (GEMM) that performs   
𝐃 = 𝐹(ɑ ⋅ 𝐀 ⋅ 𝐁 + β ⋅ 𝐂), where 𝐀, 𝐁, 𝐂 are matrices of compatible dimensions and layouts, ɑ and β are scalars, and 𝐹(𝐗) is a pre-defined function (epilog) which is applied elementwise to matrix 𝐗.

#### Documentation

- 

[Specialized Host APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/host-apis/linalg/index.html)

- 

Generic Host APIs (coming soon)

- 

[Device APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/device-apis/cublas.html)

- 

Distributed APIs (coming soon)

#### Tutorials and examples

- 

[Blog &quot;Fusing Epilog Operations with Matrix Multiplication Using nvmath-python&quot;](https://developer.nvidia.com/blog/fusing-epilog-operations-with-matrix-multiplication-using-nvmath-python/)

- 

[Tutorial &quot;Introduction to GEMM with nvmath-python&quot;](https://github.com/NVIDIA/nvmath-python/blob/main/notebooks/matmul/01_introduction.ipynb)

- 

[Tutorial &quot;Epilogs&quot;](https://github.com/NVIDIA/nvmath-python/blob/main/notebooks/matmul/02_epilogs.ipynb)

- 

[Tutorial &quot;Implementing a neural network using nvmath-python&quot;](https://github.com/NVIDIA/nvmath-python/blob/main/notebooks/matmul/03_backpropagation.ipynb)

- 

[Tutorial &quot;FP8 computations with nvmath-python&quot;](https://github.com/NVIDIA/nvmath-python/blob/main/notebooks/matmul/04_fp8.ipynb)

- 

[Host API examples](https://github.com/NVIDIA/nvmath-python/tree/main/examples/linalg/advanced/matmul)

- 

[Device API examples](https://github.com/NVIDIA/nvmath-python/tree/main/examples/device)

- 

[Host APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/host-apis/linalg/index.html) provide a _specialized API_ located in nvmath.linalg.advanced submodule backed by cuBLASLt library. This API supports GPU execution space only. The key distinguishing feature of the library is an ability to fuse matrix operations and epilog in a **single fused kernel**. The library also offers facilities to perform additional **autotuning** allowing the best fused kernel selection for a specific hardware and a specific problem size. Both **stateful** and **stateless** APIs are provided. Generic APIs will be implemented in a future release.

- 

[Device APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/device-apis/cublas.html) are located in the nvmath.device submodule backed by [cuBLASDx library](https://docs.nvidia.com/cuda/cublasdx/). They can be used from within [numba-cuda](https://github.com/NVIDIA/numba-cuda) kernels.

- 

**Distributed APIs** will be implemented in a future release.

![nvmath-python linear algebra performance](https://developer.download.nvidia.com/images/linear_alg_perf_CUT.jpg)
_Advanced 
matmul performance is shown on H100 PCIe for matrices A[m×n], B[n×k], 
bias[m], where m=65536, n=16384, k=8192. The data type of the operands 
and result is bfloat16, float32 type is used for compute._

### Fast Fourier Transforms  

The library offers forward and inverse FFTs for complex-to-complex (C2C), complex-to-real (C2R), and real-to-complex (R2C) discrete Fourier transformations.

#### Documentation

- 

[Host APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/host-apis/fft/index.html)

- 

[Device APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/device-apis/cufft.html)

- 

[Distributed APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/distributed-apis/fft/index.html)

#### Tutorials and examples

- 

[Host API examples](https://github.com/NVIDIA/nvmath-python/tree/main/examples/fft)

- 

[Device API examples](https://github.com/NVIDIA/nvmath-python/tree/main/examples/device)

- 

[Distributed FFT API examples](https://github.com/NVIDIA/nvmath-python/tree/main/examples/distributed/fft)

- 

[Distributed Reshape API examples](https://github.com/NVIDIA/nvmath-python/tree/main/examples/distributed/reshape)

![nvmath-python FFT performance](https://developer.download.nvidia.com/images/fast_four_trans_perf_CUT.jpg)
_Fast fourier transform performance is shown on H100 PCIe for FFTs of size 512 computed in 1048576 (220) batches using complex64 data type._

- 

[Host APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/host-apis/fft/index.html) are located in the nvmath.fft submodule backed by [cuFFT](/cufft#section-cufft) library. The APIs support both CPU and GPU execution spaces. NVIDIA Grace™ CPU platforms are powered by the NVPL library whereas for x86 hosts MKL is offered as a CPU backend. The key distinguishing feature of the library is an ability to fuse an FFT operation and a custom callback written as a Python function into a **single fused kernel**. The library also offers facilities to perform additional **autotuning** allowing the best fused kernel selection for a specific hardware and a specific problem size. Both **stateful** and **stateless** APIs are provided.

- 

[Device APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/device-apis/cufft.html) are located in the nvmath.device submodule backed by [cuFFTDx library](/cufft#section-cufftdx). They can be used from within [numba-cuda](https://github.com/NVIDIA/numba-cuda) kernels.

- 

[Distributed APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/distributed-apis/fft/index.html) are located in the nvmath.distributed.fft submodule powered by [cuFFTMp library](/cufft#section-cufftmp), allowing users to solve distributed 2D and 3D FFT exascale problems.

### Random Number Generation

The library offers device APIs for performing random number generation from within a GPU kernel written in [numba-cuda](https://github.com/NVIDIA/numba-cuda). It provides a collection of pseudo- and quasi-random number bit generators as well as sampling from popular probability distributions.

#### Documentation

- 

[Device APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/device-apis/curand.html)

#### Tutorials and examples

- 

[Device API examples](https://github.com/NVIDIA/nvmath-python/tree/main/examples/device)

![nvmath-python FFT performance](https://developer.download.nvidia.com/images/gbm_paths.png)
_Stock pricing using Geometric Brownian Motion kernel written in numba-cuda using nvmath-python device RNG_

- 

[Device APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/device-apis/curand.html) are located in the nvmath.device submodule backed by [cuRAND library](/curand). They can be used from within numba-cuda kernels for high-performance Monte Carlo simulations on GPU. Please note, the library does not offer corresponding host APIs and rather encourages using random number generation facilities provided by respective array libraries, such as NumPy and CuPy.

**Bit RNGs:**

- 

MRG32k3a

- 

MTGP Merseinne Twister

- 

XORWOW

- 

Sobol quasi-random number generators

**Distribution RNGs:**

- 

Uniform distribution

- 

Normal distribution

- 

Log-normal distribution

- 

Poisson distribution

### Sparse Linear Algebra - Direct Solver  

The library offers specialized APIs to support sparse linear algebra computations. The library currently offers the specialized direct solver API for solving systems of linear equations   
𝐀 ⋅ 𝐗 = 𝐁, where 𝐀 is a known left-hand side (LHS) sparse matrix, 𝐁 is a known right-hand side (RHS) vector or a matrix of a compatible shape, and 𝐗 is an unknown solution provided by the solver.

#### Documentation

- 

[Specialized Host APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/host-apis/sparse/index.html)

- 

Generic Host APIs (in future)

- 

Device APIs (in future)

- 

Distributed APIs (coming soon)

#### Tutorials and examples

- 

[Host DSS API examples](https://github.com/NVIDIA/nvmath-python/tree/main/examples/sparse/advanced/direct_solver)

![nvmath-python FFT performance](https://developer.download.nvidia.com/images/DatacenterKV-2-1536x864.png)
_Stock pricing using Geometric Brownian Motion kernel written in numba-cuda using nvmath-python device RNG_

- 

**[Host APIs](https://docs.nvidia.com/cuda/nvmath-python/latest/host-apis/sparse/index.html)** provide a specialized API located in nvmath.sparse.advanced submodule backed by [cuDSS library](/cudss). This API supports GPU execution and hybrid GPU-CPU execution space only. The key distinguishing feature of the library is an ability to solve a series of linear systems in batches. The library supports explicit batching, when linear systems are provided as sequences of LHS and/or RHS, and implicit batching, when the sequence is inferred from a higher dimensional tensor. Both **stateful** and **stateless** APIs are provided. Generic APIs will be implemented in a future release.

- 

**Device APIs** will be available in a future release.

- 

**Distributed APIs** will be implemented in a future release.

* * *

## Resources

- 
[nvmath-python Documentation](https://docs.nvidia.com/cuda/nvmath-python/index.html)
- 
[nvmath-python Github](https://github.com/nvidia/nvmath-python)
- 

[nvmath-python Tutorials (Jupyter notebooks)](https://github.com/NVIDIA/nvmath-python/tree/main/notebooks/)

- 

[nvmath-python Examples](https://github.com/NVIDIA/nvmath-python/tree/main/examples)

- 
[CUDA-X GPU-Accelerated Libraries](https://developer.nvidia.com/gpu-accelerated-libraries)
- 
[nvmath-python Demo at GTC](https://www.nvidia.com/en-us/on-demand/session/gtc24-s62162/?start=1394)
- 

[Blog &quot;Fusing Epilog Operations with Matrix Multiplication Using nvmath-python&quot;](https://developer.nvidia.com/blog/fusing-epilog-operations-with-matrix-multiplication-using-nvmath-python/)

- 

[Tutorial &quot;Accelerating and Scaling Python for HPC&quot;](https://github.com/samaid/pyhpc-tutorial)

**Get started with nvmath-python**

[Install Now](https://docs.nvidia.com/cuda/nvmath-python/latest/quickstart.html &quot;Install Now&quot;)


