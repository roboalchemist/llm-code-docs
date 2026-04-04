# Source: https://developer.nvidia.com/cudss.md

1. [Home](/)
2. NVIDIA cuDSS

# NVIDIA cuDSS

NVIDIA cuDSS (Preview) is an optimized, first-generation GPU-accelerated Direct Sparse Solver library for solving linear systems with very sparse matrices. Direct Sparse Solvers are an important part of numerical computing for real-time applications like autonomous driving and process simulation, where increasing complexity and high throughput demands a robust direct solver.

[Download](http://developer.nvidia.com/cudss-downloads)[Documentation](https://docs.nvidia.com/cuda/cudss/index.html)[Feedback](mailto:cuDSS-EXTERNAL-Group@nvidia.com)

## Key Features

### GPU-accelerated Solver

Capitalizing on the CPU’s sequential computing and the GPU’s parallel computing, cuDSS leverages both the CPU and GPU to solve sparse matrices with only a few non-zero elements per row. The result is significantly higher performance than CPU-only solvers .

### Core Functionality Support

cuDSS solves sparse linear systems on single-GPU, multi-GPU, and multi-node platforms, including support for refactorization in cases with multiple systems, and different reorderings and types of matrices. cuDSS is also built to be stable, regardless of matrix size.  

### Optimized for NVIDIA GPUs 

cuDSS supports all NVIDIA GPUs, Pascal and newer, allowing you to integrate direct sparse solvers across a variety of NVIDIA-powered platforms. cuDSS also benefits from the [Grace Hopper Superchip](https://www.nvidia.com/en-us/data-center/grace-hopper-superchip/) architecture.

* * *

## cuDSS Performance

cuDSS is able to achieve significant performance gains compared to CPU-based Direct Sparse Solvers.

[![](https://developer.download.nvidia.com/images/cuDSS_Redo_1260.png)](https://developer.download.nvidia.com/images/cuDSS_Redo_1260.png)
* * *

## Resources

- [cuDSS Documentation](https://docs.nvidia.com/cuda/cudss/index.html)
- [cuDSS Samples](https://github.com/NVIDIA/CUDALibrarySamples)
- [cuDSS Feedback](mailto:cuDSS-EXTERNAL-Group@nvidia.com)

* * *

Ready to get started with cuDSS?

[Download](http://developer.nvidia.com/cudss-downloads)


