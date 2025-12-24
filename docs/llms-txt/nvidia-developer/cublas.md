# Source: https://developer.nvidia.com/cublas.md

# cuBLAS

* * *

## Basic Linear Algebra on NVIDIA GPUs

[Download](/hpc-sdk)[Documentation](https://docs.nvidia.com/cuda/cublas/index.html)[Samples](http://github.com/nvidia/cudalibrarysamples)[Support](https://forums.developer.nvidia.com/tags/c/accelerated-computing/gpu-accelerated-libraries/12/cublas)[Feedback](mailto:Math-Libs-Feedback@nvidia.com?subject=cuBLAS%20Feedback&amp;body=Thank%20you%20for%20using%20our%20software%20and%20taking%20time%20to%20provide%20your%0D%0A%0D%0Afeedback.%0D%0A%0D%0A%0D%0A%0D%0AIf%20you%20have%20a%20question%20or%20issue,%20please%20post%20it%20on%20the%20NVIDIA%20%20%0D%0A%0D%0AGPU-ACCELERATED%20LIBRARIES%20Developer%20Forum%20at:%0D%0A%0D%0Ahttps://forums.developer.nvidia.com/c/accelerated-computing/gpu-accelerated-libraries/12%0D%0A%0D%0A%0D%0A%0D%0ATo%20submit%20a%20bug%20report,%20please%20follow%20the%20instructions%20at:%20%0D%0A%0D%0Ahttps://forums.developer.nvidia.com/t/how-to-report-a-bug/67911%0D%0A%0D%0A%0D%0A%0D%0AProvide%20as%20much%20information%20and%20reproducer%20code%20as%20possible.%0D%0A%0D%0A%0D%0A%0D%0AFor%20feedback%20or%20feature%20requests,%20please%20reply%20to%20this%20email%20and%20provide%20%0D%0A%0D%0Athe%20following:%0D%0A%0D%0A%0D%0A%0D%0A%20%201.%20Target%20Library%20(e.g.%20cuBLAS,%20cuFFT,%20etc.)%0D%0A%0D%0A%20%202.%20Target%20Hardware%20(e.g.%20V100,%20A100,%20etc.)%0D%0A%0D%0A%20%203.%20Target%20OS%20(e.g.%20RHEL%208.1,%20Ubuntu%2020.04,%20Windows%2010,%20etc.)%0D%0A%0D%0A%20%204.%20Use%20cases%20(the%20more%20detail%20the%20better)%0D%0A%0D%0A%20%20%20%20%20a.%20Data%20type(s)%0D%0A%0D%0A%20%20%20%20%20b.%20Data%20size(s)%0D%0A%0D%0A%20%20%20%20%20c.%20Format(s)%0D%0A%0D%0A%20%205.%20Limiting%20factors%20by%20not%20having%20the%20desired%20functionality.)

  

NVIDIA cuBLAS is a GPU-accelerated library for accelerating AI and HPC applications. It includes several API extensions for providing drop-in industry standard BLAS APIs and GEMM APIs with support for fusions that are highly optimized for NVIDIA GPUs. The cuBLAS library also contains extensions for batched operations, execution across multiple GPUs, and mixed- and low-precision execution with additional tuning for the best performance.   
  
 The cuBLAS library is included in both the [NVIDIA HPC SDK](https://developer.nvidia.com/hpc-sdk) and the [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads).

  
[Explore what’s new in the latest release.](https://developer.nvidia.com/cuda-toolkit/whatsnew)

* * *

## cuBLAS API Extensions

## cuBLAS Host API 

cuBLAS Host APIs for CUDA-accelerated **BLAS** for **Level 1** (vector-vector), **Level 2** (matrix-vector), and **Level 3** (matrix-matrix) operations. cuBLAS also includes custom GEMM extension APIs that are simple to use for drop-in hardware acceleration.   
  
_cuBLAS APIs are available in the cuBLAS library._

## cuBLASLt Host API 

cuBLASLt Host APIs are **multi-stage GEMM APIs** that are highly expressive, allowing applications to leverage the latest NVIDIA architecture features for the best performance with support for **fusions** and performance tuning options.   
  
_cuBLASLt APIs are available in the cuBLAS library._

## cuBLASXt Single-Process Multi-GPU Host API 

cuBLASXt Host API exposes a multi-GPU capable interface for efficiently dispatching Level 3 workloads across one or multiple GPUs in a **single node**.

_cuBLASXt APIs are available in the cuBLAS library._

  

## cuBLASMp Multi-Node Multi-GPU Host API (Preview)

cuBLASMp (Preview) is a high-performance, **multi-process** , GPU-accelerated library for **distributed** basic dense linear algebra. cuBLASMp is available for standalone download and as part of the [HPC SDK](https://developer.nvidia.com/hpc-sdk).

  
[Download cuBLASMp](http://developer.nvidia.com/cublasmp-downloads)

## cuBLASDx Device API (Preview)

cuBLASDx (Preview) is a **device side** API extension to cuBLAS for performing BLAS calculations inside your CUDA kernel. **Fusing** numerical operations decreases the latency and improves the performance of your application.

  
[Download cuBLASDx](https://developer.nvidia.com/cublasdx-downloads)

## cuBLAS Key Features

- Complete support for all 152 standard BLAS routines
- Support for half-precision and integer matrix multiplication
- GEMM and GEMM extensions with fusion optimized for Tensor Cores
- GEMM performance tuned for sizes used in various Deep Learning models
- Supports CUDA streams for concurrent operations

  

## cuBLAS Performance

The cuBLAS library is highly optimized for performance on NVIDIA GPUs, and leverages tensor cores for acceleration of low- and mixed-precision matrix multiplication.

  

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/CUDALibs/cublas-11-mixed.png)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/CUDALibs/cublas-11-mixed.png)

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/CUDALibs/cublas-11-fp64.png)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/CUDALibs/cublas-11-fp64.png)

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/CUDALibs/cublas-11-int.png)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/CUDALibs/cublas-11-int.png)

_cuBLAS Matrix Multiply performance on Datacenter GPUs for various precisions_

  
  

## cuBLASMp Key Features

- Multi-node multi-GPU basic linear algebra functionality
- 2D Block Cyclic data layout
- Fortran wrappers available through nvfortran

  

## cuBLASMp Performance

cuBLASMp harnesses tensor core acceleration, while efficiently communicating between GPUs and synchronizing their processes.

  
  

[![](https://developer.download.nvidia.com/images/WeakScaling_Cropped.png)](https://developer.download.nvidia.com/images/WeakScaling_Cropped.png)

Weak scaling of cuBLASMp distributed double precision GEMM. M,N,K = 55k per GPU

[![](https://developer.download.nvidia.com/images/NewStrongScaling_Cut.png)](https://developer.download.nvidia.com/images/NewStrongScaling_Cut.png)

Strong scaling of cuBLASMp distributed double precision GEMM. M,N,K = 55k

  

## cuBLASLt Performance

[![](https://developer.download.nvidia.com/images/llama-2-training.png)](https://developer.download.nvidia.com/images/llama-2-training.png)

Weak scaling of cuBLASMp distributed double precision GEMM. M,N,K = 55k per GPU


