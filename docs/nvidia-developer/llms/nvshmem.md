# Source: https://developer.nvidia.com/nvshmem.md

# NVSHMEM
  

**NVSHMEM™** is a parallel programming interface based on OpenSHMEM that provides efficient and scalable communication for NVIDIA GPU clusters. NVSHMEM creates a global address space for data that spans the memory of multiple GPUs and can be accessed with fine-grained GPU-initiated operations, CPU-initiated operations, and operations on CUDA® streams.

  

[Download NVSHMEM](/nvshmem-downloads) [Documentation](https://docs.nvidia.com/nvshmem/api/index.html) [Release Notes](https://docs.nvidia.com/nvshmem/release-notes-install-guide/release-notes/index.html) [GitHub](https://github.com/NVIDIA/nvshmem/releases) [NVSHMEM API Guide](https://docs.nvidia.com/nvshmem/api/api.html)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/nvshmem/mpi-nvshmem-explainer-diagram.svg)Existing communication models, such as Message-Passing Interface (MPI), orchestrate data transfers using the CPU. In contrast, NVSHMEM uses asynchronous, GPU-initiated data transfers, eliminating synchronization overheads between the CPU and the GPU.

* * *

#### Efficient, Strong Scaling

NVSHMEM enables long-running kernels that include both communication and computation, reducing overheads that can limit an application’s performance when strong scaling.

#### Low Overhead

One-sided communication primitives reduce overhead by allowing the initiating process or GPU thread to specify all information required to complete a data transfer. This low-overhead model enables many GPU threads to communicate efficiently.

#### Naturally Asynchronous

Asynchronous communications make it easier for programmers to interleave computation and communication, thereby increasing overall application performance.

  

* * *

## What&#39;s New in NVSHMEM 3.4

- Added support for data direct NIC configurations in the IB transports. - Added a new environment variable, `NVSHMEM_DISABLE_DATA_DIRECT`, to force disable data direct NIC even when present.
- Added support for CPU-Assisted IBGDA without the use of GDRCopy or the x86 regkey setting. Systems not supporting the other methods will automatically fall back to this new method. It enables the use of IBGDA on a broad range of systems without the need for administrator intervention.
- Added a new environment variable `NVSHMEM_HCA_PREFIX` to enable IB transports on systems which name their HCA devices in a non-standard way (for example, `ipb*` instead of `mlx5*`).
- Deprecated support for the combined `libnvshmem.a` host and device static library.

  

* * *

## Key Features
  

- Combines the memory of multiple GPUs into a partitioned global address space that’s accessed through NVSHMEM APIs
- Includes a low-overhead, in-kernel communication API for use by GPU threads
- Includes stream-based and CPU-initiated communication APIs
- Supports x86 and Arm processors
- Is interoperable with MPI and other OpenSHMEM implementations

  

* * *

## NVSHMEM Advantages
  

### Increase Performance

Convolution is a compute-intensive kernel that’s used in a wide variety of applications, including image processing, machine learning, and scientific computing. Spatial parallelization decomposes the domain into sub-partitions that are distributed over multiple GPUs with nearest-neighbor communications, often referred to as halo exchanges.

In the Livermore Big Artificial Neural Network (LBANN) deep learning framework, spatial-parallel convolution is implemented using several communication methods, including MPI and NVSHMEM. The MPI-based halo exchange uses the standard send and receive primitives, whereas the NVSHMEM-based implementation uses one-sided put, yielding significant performance improvements on Lawrence Livermore National Laboratory’s [Sierra supercomputer](https://computing.llnl.gov/computers/sierra).

  

##### Efficient Strong-Scaling on Sierra Supercomputer

  
  

  

##### Efficient Strong-Scaling on NVIDIA DGX SuperPOD

### Accelerate Time to Solution

Reducing the time to solution for high-performance, scientific computing workloads generally requires a strong-scalable application. QUDA is a library for lattice quantum chromodynamics (QCD) on GPUs, and it’s used by the popular MIMD Lattice Computation (MILC) and Chroma codes.

NVSHMEM-enabled QUDA avoids CPU-GPU synchronization for communication, thereby reducing critical-path latencies and significantly improving strong-scaling efficiency.

[Watch the GTC 2020 Talk](/gtc/2020/video/s21673)

  
  

### Simplify Development

The conjugate gradient (CG) method is a popular numerical approach to solving systems of linear equations, and CGSolve is an implementation of this method in the Kokkos programming model. The CGSolve kernel showcases the use of NVSHMEM as a building block for higher-level programming models like Kokkos.

NVSHMEM enables efficient multi-node and multi-GPU execution using Kokkos global array data structures without requiring explicit code for communication between GPUs. As a result, NVSHMEM-enabled Kokkos significantly simplifies development compared to using MPI and CUDA.

  

##### Productive Programming of Kokkos CGSolve

* * *

## Resources
  

- Users of NVSHMEM: 
  - [QUDA: Avoiding the Jam (Lattice 2022 Talk)](https://indico.hiskp.uni-bonn.de/event/40/contributions/693/attachments/318/539/Lattice2022_Wagner_NVSHMEM.pdf)
  - [cuFFTMp: Multinode Multi-GPU: Using NVIDIA cuFFTMp FFTs at Scale (Blog)](https://developer.nvidia.com/blog/multinode-multi-gpu-using-nvidia-cufftmp-ffts-at-scale/)
  - GROMACS 
    - [Massively Improved Multi-node NVIDIA GPU Scalability with GROMACS (Blog)](https://developer.nvidia.com/blog/massively-improved-multi-node-nvidia-gpu-scalability-with-gromacs)
    - [Cutting-Edge CUDA Technologies for Molecular Dynamics and Beyond (GTC 2023 Talk)](https://www.nvidia.com/en-us/on-demand/session/gtcspring23-s51110/)

  - [Kokkos: Performance Insights into Device-initiated RMA Using Kokkos Remote Spaces (Paper)](https://ieeexplore.ieee.org/document/10321871)
  - Others 
    - [Scalable Simulation of Quantum Circuit with Noise on GPU-based HPC Systems (GTC Talk)](https://www.nvidia.com/gtc/session-catalog/?tab.scheduledorondemand=1583520458947001NJiE&amp;search=nvshmem#/session/1638571299696001GJl3)

- NVSHMEM Blogs: 
  - [Enhancing Application Portability and Compatibility across New Platforms Using NVIDIA Magnum IO NVSHMEM 3.0](https://developer.nvidia.com/blog/enhancing-application-portability-and-compatibility-across-new-platforms-using-nvidia-magnum-io-nvshmem-3-0/)
  - [IBGDA: Improving Network Performance of HPC Systems Using NVIDIA Magnum IO NVSHMEM and GPUDirect Async](https://developer.nvidia.com/blog/improving-network-performance-of-hpc-systems-using-nvidia-magnum-io-nvshmem-and-gpudirect-async/)
  - [Scaling Scientific Computing with NVSHMEM](https://developer.nvidia.com/blog/scaling-scientific-computing-with-nvshmem/)
  - [Accelerating NVSHMEM 2.0 Team-Based Collectives Using NCCL](https://developer.nvidia.com/blog/accelerating-nvshmem-2-0-team-based-collectives-using-nccl/)

- [Introductory Webinar](https://www.nvidia.com/en-us/on-demand/session/gtcspring23-s51705/)
- [NVSHMEM Documentation](https://docs.nvidia.com/hpc-sdk/nvshmem/index.html)
- [NVSHMEM Best Practices Guide](https://docs.nvidia.com/nvshmem/release-notes-install-guide/best-practice-guide/index.html)
- [NVSHMEM API Documentation](https://docs.nvidia.com/nvshmem/api/api.html)
- [OpenSHMEM Specification](http://openshmem.org/site/)
- [NVSHMEM Developer Forum](https://forums.developer.nvidia.com/tag/nvshmem)
- For questions or to provide feedback, please contact [nvshmem@nvidia.com](mailto:nvshmem@nvidia.com)
- Related libraries and software:
  - [NVIDIA HPC SDK™](/hpc-sdk)
  - [NVIDIA GPUDirect®](/gpudirect)
  - [Magnum IO](https://www.nvidia.com/en-us/data-center/magnum-io/)
  - [CUDA-X™ Libraries](/gpu-accelerated-libraries)

  

Ready to start developing with NVSHMEM?

  

[Get Started](/nvshmem-downloads)


