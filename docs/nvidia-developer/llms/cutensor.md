# Source: https://developer.nvidia.com/cutensor.md

# cuTENSOR

## Tensor Linear Algebra on NVIDIA GPUs 

NVIDIA cuTENSOR is a GPU-accelerated tensor linear algebra library for tensor contraction, reduction, and elementwise operations. With cuTENSOR, applications can harness the specialized tensor cores on NVIDIA GPUs to perform high-performance tensor computations and accelerate deep learning training and inference, computer vision, quantum chemistry, and computational physics workloads.

  
  
[Download](https://developer.nvidia.com/cutensor-downloads)  

## Resources:

- [Documentation](https://docs.nvidia.com/cuda/cutensor/index.html)
- [Samples](http://github.com/nvidia/cudalibrarysamples)

- [Feedback](mailto:Math-Libs-Feedback@nvidia.com)
- [Support](https://forums.developer.nvidia.com/c/accelerated-computing/gpu-accelerated-libraries/12)

  

## cuTENSORMp Available Now

cuTENSORMp offers new capabilities for contracting large tensors across multiple GPUs and multiple nodes. cuTENSORMp scales nearly linearly on NVIDIA Grace Blackwell NVL72 systems, enabling tensor math researchers to scale their contractions and have more options for tradeoffs for performance and scale in both quantum chemistry and quantum computing simulations.

  

 ![A chart showing strong scaling for 2x 32 GB contractions with cuTENSORMp across NVL72](https://developer.download.nvidia.com/images/cuda-charts-cutensor-webpage-charts-sc25-4538751-v7-chart2.png &quot;A chart showing strong scaling for 2x 32 GB contractions with cuTENSORMp across NVL72&quot;)

Users can get excellent performance for both tensors that exceed the memory of single GPUs, and speeding up fixed size tensor contractions, which have been optimized for Grace Blackwell NVL72.

  
[Read the cuTENSORMp Documentation](https://docs.nvidia.com/cuda/cutensor/latest/user_guide_cutensorMp.html)  

* * *

## cuTENSOR Performance 

The cuTENSOR library is highly optimized for performance on NVIDIA GPUs with support for DMMA, TF32, and now 3xTF32.

  

 ![A graph showing performance enhancements for various precisions with space and dense contractions](https://developer.download.nvidia.com/images/cutensor-performance-ari.png &quot; A graph showing performance enhancements for various precisions with space and dense contractions&quot;)

The latest version of cuTENSOR offers big speedups for workloads like Block-Sparse tensor contractions, driving significant performance improvements within the same hardware generation.

  
[Read the cuTENSOR Documentation](https://docs.nvidia.com/cuda/cutensor/latest/index.html)

### cuTENSOR Key Features 

- Just-in-time compiled kernels for tensor contraction
- Plan-based multi-stage APIs for all operations
- Support for arbitrarily dimensional tensor descriptors
- Support for 3xTF32 compute type
- Support for block-sparse tensor contractions
- Support for multi-process tensor contractions

- Support for int64 extents
- Tensor contraction, reduction, and elementwise operations
- Mixed precision support
- Expressive API allowing elementwise operation fusion

### Ready to get started with cuTENSOR?
[Download](https://developer.nvidia.com/cutensor-downloads)

