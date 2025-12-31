# Source: https://developer.nvidia.com/cufft.md

1. [Home](/)
2. 
3.  / NVIDIA cuFFT

 ![](https://developer.download.nvidia.com/images/cuFFT-flat.svg)
# NVIDIA cuFFT

NVIDIA cuFFT, a library that provides GPU-accelerated Fast Fourier Transform (FFT) implementations, is used for building applications across disciplines, such as deep learning, computer vision, computational physics, molecular dynamics, quantum chemistry, and seismic and medical imaging.

# Available in the [CUDA Toolkit](/cuda-toolkit)

### cuFFT

Divide-and-conquer algorithms for computing discrete Fourier transformers. Multi-GPU support for FFT calculations on up to 16 GPUs in a single node.

[Learn More](#section-cufft)

# Available in the [HPC SDK](/hpc-sdk)

### cuFFT

Divide-and-conquer algorithms for computing discrete Fourier transformers. Multi-GPU support for FFT calculations on up to 16 GPUs in a single node.

[Learn More](#section-cufft)

### cuFFTMp

Multi-node support for FFTs in exascale problems.

[Learn More](#section-cufftmp)

# Available as Standalone

### cuFFTDx Device APIs

cuFFT Device Extensions for performing FFT calculations inside a CUDA kernel.

[Learn More and Download](#section-cufftdx)

* * *

## cuFFT

The FFT is a divide-and-conquer algorithm for efficiently computing discrete Fourier transforms of complex or real-valued datasets. It’s one of the most important and widely used numerical algorithms in computational physics and general signal processing. The cuFFT library provides a simple interface for computing FFTs on an NVIDIA GPU, which allows users to quickly leverage the GPU’s floating-point power and parallelism in a highly optimized and tested FFT library.  
  
When calculations are distributed across GPUs, cuFFT supports using up to 16 GPUs connected to a CPU to perform Fourier Transforms through its cuFFTXt APIs. Performance is a function of the bandwidth between the GPUs, the computational ability of the individual GPUs, and the type and number of FFTs to be performed.

[HPC SDK](https://developer.nvidia.com/nvidia-hpc-sdk-downloads)[CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)

Key Features

Single-GPU Performance

Multi-GPU Performance

- 1D, 2D, and 3D transforms of complex and real data types

- Familiar APIs similar to the advanced interface of the Fastest Fourier Transform in the West (FFTW)

- Flexible data layouts allowing arbitrary strides between individual elements and array dimensions

- Streamed asynchronous execution

- Half-, single-, and double-precision transforms

- Batch execution

- In-place and out-of-place transforms

- Support for up to 16-GPU systems

- Thread-safe and callable from multiple host threads

The cuFFT library is highly optimized for performance on NVIDIA GPUs. The chart below displays the performance boost achieved by moving to newer hardware—with zero code changes.

# 1D Single-Precision FFT
 ![A line chart displays performance boost achieved by moving to newer hardware with no code changes	](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuFFT/1-d-single-precision-fft-850x480.svg)

The chart below compares the performance of 16 NVIDIA Volta™ GV100 Tensor Core GPUs to the performance of eight NVIDIA Ampere architecture GA100 Tensor Core GPUs for 3D C2C FP32 FFTs.

  

* * *

## cuFFTDx Device Extensions

cuFFT Device Extensions (cuFFTDx) enable users to perform FFT calculations inside their CUDA kernel. Fusing numerical operations can decrease latency and improve the performance of their application.

[Download cuFFTDx](https://developer.nvidia.com/cufftdx-downloads)

Key Features

Performance

- FFT embeddable into a CUDA kernel

- High-performance, no-unnecessary data movement from and to global memory

- Customizable with options to adjust selection of FFT routine for different needs (size, precision, batches, etc.)

- Ability to fuse FFT kernels with other operations, saving global memory trips

- Compatible with future versions of the CUDA Toolkit

- Support for Windows

The chart below shows how cuFFTDx can provide over a 2X performance boost compared with cuFFT host calls when executing convolution with 1D FFTs.

* * *

## cuFFTMp Multi-Node Support

The multi-node FFT functionality, available through the cuFFTMp API, enables scientists and engineers to solve distributed 2D and 3D FFTs in exascale problems. The library handles all the communications between machines, allowing users to focus on other aspects of their problems.

[Download cuFFTMp](https://developer.nvidia.com/cufftmp-downloads?target_os=Linux)[Download HPC-SDK](https://developer.nvidia.com/nvidia-hpc-sdk-downloads)

Key Features

Performance

- 2D and 3D distributed-memory FFTs

- Slabs (1D) and pencils (2D) data decomposition, with arbitrary block sizes

- Message Passing Interface (MPI) compatible

- Low-latency implementation using NVSHMEM, optimized for single-node and multi-node FFTs

Below compares multi-node weak-scaling performance for distributed 3D FFT by precision, as the problem size and number of GPUs increase. The benchmark was achieved on the NVIDIA Selene supercomputer. Note that, for FP64 and size 1,6384 3, the data didn’t fit on the system.

 ![The chart compares multi-node weak scaling performance for distributed 3D FFT by precision](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuFFT/multi-node-support-850x480.svg)

* * *

## cuFFTDx + cuFFT LTO EA Preview

This early-access version of [cuFFT](https://developer.nvidia.com/cufft) and [cuFFTDx](https://developer.nvidia.com/cufftdx-downloads) previews an innovative way of expanding features of the device library, cuFFTDx, through the host library, cuFFT. It leverages device Link-Time Optimizations (LTO) features of the CUDA Toolkit to combine code segments and achieve optimal performance.

[Download Now](https://developer.nvidia.com/cufftea)

Key Features

Performance

- A new way of enhancing your cuFFTDx project via our cuFFT host library.

- Over 1000 additional sizes supported with improved performance and without workspace requirement, via code sharing across our libraries enabled by LTO.  

- Supporting both offline builds (using NVCC) and runtime builds (using NVRTC / nvJitLink).

- Additional link time optimization in cuFFTDx applications.

The chart below shows the performance improvements of the additional functionality of cuFFTDx enabled by cuFFT using LTO.

* * *

## Resources

**Documentation:**

- [cuFFT/cuFFTXt](https://docs.nvidia.com/cuda/cufft/index.html)

- [cuFFTMp](https://docs.nvidia.com/hpc-sdk/cufftmp/index.html)

- [cuFFTDx](https://docs.nvidia.com/cuda/cufftdx/index.html)

**Presentations:**

- [Just-In-Time Link-Time Optimization Adoption in cuSPARSE/cuFFT](https://www.nvidia.com/en-us/on-demand/session/gtcfall21-a31155/)

- [New FFT Library With Flexible C++ API](https://www.nvidia.com/en-us/on-demand/session/gtcsiliconvalley2019-s9257/)

**Samples:**

- [Math Library Github](https://github.com/NVIDIA/CUDALibrarySamples)

- [CUDA Toolkit Github](https://github.com/NVIDIA/cuda-samples)

**Blogs:**

- [Accelerating GPU Applications with NVIDIA Math Libraries](https://developer.nvidia.com/blog/accelerating-gpu-applications-with-nvidia-math-libraries/)

- [Using NVIDIA cuFFTMp FFTs at Scale](https://developer.nvidia.com/blog/multinode-multi-gpu-using-nvidia-cufftmp-ffts-at-scale/)

**Downloads:**

- [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)

- [cuFFTDX + cuFFT LTO EA](https://developer.nvidia.com/cufftea)

- [NVIDIA HPC SDK](https://developer.nvidia.com/nvidia-hpc-sdk-downloads)

- [cuFFTDx](https://developer.nvidia.com/mathdx)

* * *

 ![Decorative image representing Developer Forums](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuFFT/m48-communication-chat-256px-blk.png)
#### Visit the Forums

 ![Decorative image representing contact NVIDIA](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuFFT/m48-information-notification-256px-blk.png)
#### Contact Us

Quick Links

- [HPC SDK](https://developer.nvidia.com/hpc-sdk)
- [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit)[Download cuFFTDx](https://developer.nvidia.com/cufftdx-downloads)

* * *


