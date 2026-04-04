# Source: https://developer.nvidia.com/cusolver.md

# cuSOLVER

## Direct Linear Solvers on NVIDIA GPUs

[Download](/hpc-sdk)[Documentation](https://docs.nvidia.com/cuda-libraries/index.html)[Samples](http://github.com/nvidia/cudalibrarysamples)[Support](https://forums.developer.nvidia.com/c/accelerated-computing/gpu-accelerated-libraries/12)[Feedback](mailto:Math-Libs-Feedback@nvidia.com?subject=cuSOLVER%20Feedback)

The NVIDIA cuSOLVER library provides a collection of dense and sparse direct linear solvers and Eigen solvers which deliver significant acceleration for Computer Vision, CFD, Computational Chemistry, and Linear Optimization applications. The cuSOLVER library is included in both the [NVIDIA HPC SDK](/hpc-sdk) and the [CUDA Toolkit](/cuda-downloads).

## cuSOLVERMp Multi-Node Multi-GPU Host API

The NVIDIA cuSOLVERMp library is a high-performance, distributed-memory, GPU-accelerated library that provides tools for solving dense linear systems and eigenvalue problems. The library is available as a standalone download and is also included in the [NVIDIA HPC SDK](https://developer.nvidia.com/hpc-sdk).

  
[Download](http://developer.nvidia.com/cusolvermp-downloads)

## cuSOLVER Performance 

cuSOLVER 11 leverages DMMA Tensor Cores automtically. DGX A100 is over 2x faster than DGX-2 despite having half the number of GPUs thanks to A100 and third generation NVLINK and NVSWITCH.

## cuSOLVER Key Features 

- cusolverDN: Key LAPACK dense solvers 3-6x faster than MKL. 
  - Dense Cholesky, LU, SVD, QR
  - Applications include: optimization, Computer Vision, CFD

- cusolverSP 
  - Sparse direct solvers 
  - Symmetric &amp; generalized symmetric eigensolvers
  - Applications include: Newton&#39;s method, Chemical Kinetics

- cusolverRF 
  - Sparse refactorization solver
  - Applications include: Chemistry, ODEs, Circuit simulation

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/CUDALibs/cusolver-11_0.png)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/CUDALibs/cusolver-11_0.png)

Available now: cuSOLVERMp

  

The NVIDIA cuSOLVERMp library is a high-performance, distributed-memory, GPU-accelerated library that provides tools for solving dense linear systems and eigenvalue problems. The library is available as a standalone download and is also included in the NVIDIA HPC SDK.

  
[Download](https://developer.nvidia.com/cusolvermp-home)  


