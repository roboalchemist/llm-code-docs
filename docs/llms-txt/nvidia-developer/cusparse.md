# Source: https://developer.nvidia.com/cusparse.md

# cuSPARSE

GPU library APIs for sparse computation.   
 cuSPARSE host APIs provide GPU accelerated basic linear algebra routines, and cuSPARSELt host APIs provide structured sparsity support that leverages sparse tensor cores for GEMM. Sparsity is widely applicable in machine learning, AI, computational fluid dynamics, seismic exploration and computational sciences.

## cuSPARSE Host API
[Download](https://developer.nvidia.com/hpc-sdk)[Documentation](https://docs.nvidia.com/cuda/cusparse/index.html)  

The cuSPARSE APIs provides GPU-accelerated basic linear algebra subroutines for sparse matrix computations for unstructured sparsity. cuSPARSE is widely used by engineers and scientists working on applications in machine learning, AI, computational fluid dynamics, seismic exploration, and computational sciences.

  

cuSPARSE is included in both the [NVIDIA HPC SDK](https://developer.nvidia.com/hpc-sdk) and the [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads).

## cuSPARSELt Host API
[Download](https://developer.nvidia.com/cusparselt-downloads)[Documentation](https://docs.nvidia.com/cuda/cusparselt/index.html)  

cuSPARSELt APIs offer 2:4 structured sparsity support via Sparse Tensor Core in Ampere and later architectures for GEneral Matrix Multiplications (GEMMs). cuSPARSELt APIs provide options for pruning and compression of sparse matrices, Activation functions, bias vectors, and output scaling for AI and deep learning use cases.

* * *

## cuSPARSE Performance

The cuSPARSE library is highly optimized for performance on NVIDIA GPUs, with SpMM performance 30-150X faster than CPU-only alternatives.

## cuSPARSE Key Features

- Support for dense, COO, CSR, CSC, and Blocked CSR sparse matrix formats
- Full suite of sparse routines covering sparse vector x dense vector operations, sparse matrix x dense vector operations, and sparse matrix x dense matrix operations.
- Routines for sparse matrix x sparse matrix addition and multiplication
- Generic high-performance APIs for sparse-dense vector multiplication (SpVV), sparse matrix-dense vector multiplication (SpMV), and sparse matrix-dense matrix multiplication (SpMM)
- ILU0 and IC0 preconditioners

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/cusparse9_2.png)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/cusparse9_2.png)

* * *

## Resources

**Documentation:**

- [cuSPARSE](https://docs.nvidia.com/cuda/cusparse/index.html) 
- [cuSPARSELt](https://docs.nvidia.com/cuda/cusparselt/index.html) 

**Samples:**

- [cuSPARSE](https://github.com/NVIDIA/CUDALibrarySamples/tree/master/cuSPARSE) 
- [cuSPARSELt](https://github.com/NVIDIA/CUDALibrarySamples/tree/master/cuSPARSELt) 

**[Forums](https://forums.developer.nvidia.com/tags/c/accelerated-computing/gpu-accelerated-libraries/12/cusparse)**

**[Feedback](mailto:Math-Libs-Feedback@nvidia.com)**


