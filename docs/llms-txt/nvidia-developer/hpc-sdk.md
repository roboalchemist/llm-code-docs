# Source: https://developer.nvidia.com/hpc-sdk.md

# NVIDIA HPC SDK

## A Comprehensive Suite of Compilers, Libraries and Tools for HPC

The NVIDIA HPC Software Development Kit (SDK) includes the proven compilers, libraries and software tools essential to maximizing developer productivity and the performance and portability of HPC applications.

![NVIDIA HPC SDK Development and Analysis](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/hpc-sdk-explainer-diagram-update-r1.png &quot;NVIDIA HPC SDK Development and Analysis&quot;)

The NVIDIA HPC SDK C, C++, and Fortran compilers support GPU acceleration of HPC modeling and simulation applications with standard C++ and Fortran, OpenACC® directives, and CUDA®. GPU-accelerated math libraries maximize performance on common HPC algorithms, and optimized communications libraries enable standards-based multi-GPU and scalable systems programming. Performance profiling and debugging tools simplify porting and optimization of HPC applications, and containerization tools enable easy deployment on-premises or in the cloud. With support for NVIDIA GPUs and Arm or x86-64 CPUs running Linux, the HPC SDK provides the tools you need to build NVIDIA GPU-accelerated HPC applications.

[Download Now](https://developer.nvidia.com/nvidia-hpc-sdk-downloads)[Get Container](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/nvhpc)

* * *

## Why Use the NVIDIA HPC SDK?

### Performance

Widely used HPC applications, including VASP, Gaussian, ANSYS Fluent, GROMACS, and NAMD, use CUDA, OpenACC, and GPU-accelerated math libraries to deliver breakthrough performance to their users. You can use these same software tools to GPU-accelerate your applications and achieve dramatic speedups and power efficiency using NVIDIA GPUs.

### Portability

Build and optimize applications for over 99 percent of today&#39;s Top500 systems, including those based on NVIDIA GPUs, x86-64, or Arm. You can use drop-in libraries, C++17 parallel algorithms and OpenACC directives to GPU accelerate your code and ensure your applications are fully portable to other compilers and systems.

### Productivity

Maximize science and engineering throughput and minimize coding time with a single integrated suite that allows you to quickly port, parallelize and optimize for GPU acceleration, including industry-standard communication libraries for multi-GPU and scalable computing, and profiling and debugging tools for analysis.

* * *

## Support for Your Favorite Programming Languages

### C++17 Parallel Algorithms

C++17 parallel algorithms enable portable parallel programming using the Standard Template Library (STL). The NVIDIA HPC SDK C++ compiler supports full C++17 on CPUs and offloading of parallel algorithms to NVIDIA GPUs, enabling GPU programming with no directives, pragmas, or annotations. Programs that use C++17 parallel algorithms are readily portable to most C++ implementations for Linux, Windows, and macOS.

### Fortran 2003 Compiler

The NVIDIA Fortran compiler supports Fortran 2003 and many features of Fortran 2008. With support for OpenACC and [CUDA Fortran](/cuda-fortran) on NVIDIA GPUs, and SIMD vectorization, OpenACC and OpenMP for multicore x86-64 and Arm, it has the features you need to port and optimize your Fortran applications on today’s heterogeneous GPU-accelerated HPC systems.

### OpenACC Directives

NVIDIA Fortran, C, and, C++ compilers support OpenACC directive-based parallel programming for NVIDIA GPUs and multicore CPUs. Over 200 HPC application ports have been initiated or enabled using OpenACC, including production applications like VASP, Gaussian, ANSYS Fluent, WRF, and MPAS. OpenACC is the proven performance-portable directives solution for GPUs and multicore CPUs.

* * *

## Key Features

 ![NVIDIA HPC SDK includes a suite of GPU-accelerated math libraries](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda-x-libraries.svg &quot; NVIDIA HPC SDK includes a suite of GPU-accelerated math libraries&quot;)

### GPU Math Libraries

The NVIDIA HPC SDK includes a suite of [GPU-accelerated math libraries](https://developer.nvidia.com/gpu-accelerated-libraries#linear-algebra) for compute-intensive applications. The cuBLAS and cuSOLVER libraries provide GPU-optimized and multi-GPU implementations of all BLAS routines and core routines from LAPACK, automatically using NVIDIA GPU Tensor Cores where possible. cuFFT includes GPU-accelerated 1D, 2D, and 3D FFT routines for real and complex data, and cuSPARSE provides basic linear algebra subroutines for sparse matrices. These libraries are callable from CUDA and OpenACC programs written in C, C++ and Fortran.

### Optimized for Tensor Cores

NVIDIA GPU Tensor Cores enable scientists and engineers to dramatically accelerate suitable algorithms using mixed precision or double precision. The NVIDIA HPC SDK math libraries are optimized for Tensor Cores and multi-GPU nodes to deliver the full performance potential of your system with minimal coding effort. Using the NVIDIA Fortran compiler, you can leverage Tensor Cores through automatic mapping of transformational array intrinsics to the cuTENSOR library.

Technical Blog: [Bringing Tensor Cores to Standard Fortran](https://developer.nvidia.com/blog/bringing-tensor-cores-to-standard-fortran/)

 ![NVIDIA A100 Tensor Core FP64](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/HPC_SDK/A100_TensorCore_FP64.jpg &quot; NVIDIA A100 Tensor Core FP64&quot;)

 ![NVIDIA HPC compilers and tools are optimized for your CPU](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/optimized-for-cpu.svg &quot;NVIDIA HPC compilers and tools are optimized for your CPU&quot;)

### Optimized for Your CPU

Heterogeneous HPC servers use GPUs for accelerated computing and multicore CPUs based on the x86-64 or Arm instruction set architectures. [NVIDIA HPC compilers](/hpc-compilers) and tools are supported on all of these CPUs, and all compiler optimizations are fully enabled on any CPU that supports them. With uniform features, command-line options, language implementations, programming models, and tool and library user interfaces across all supported systems, the NVIDIA HPC SDK simplifies the developer experience in diverse HPC environments.

### Multi-GPU Programming

The NVIDIA Collective Communications Library (NCCL) implements highly optimized multi-GPU and multi-node collective communication primitives using MPI-compatible all-gather, all-reduce, broadcast, reduce, and reduce-scatter routines to take advantage of all available GPUs within and across your HPC server nodes. NVSHMEM implements the OpenSHMEM standard for GPU memory and provides multi-GPU and multi-node communication primitives that can be initiated from a host CPU or GPU and called from within a CUDA kernel.

 ![NVIDIA Collective Communications Library (NCCL) implements multi-GPU programming](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/multi-gpu-programming.svg &quot;NVIDIA Collective Communications Library (NCCL) implements multi-GPU programming&quot;)

 ![NVIDIA HPC SDK includes a MPI library for scalable systems programming](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/scalable-system-programming.jpg &quot;NVIDIA HPC SDK includes a MPI library for scalable systems programming&quot;)

### Scalable Systems Programming

MPI is the standard for programming distributed-memory scalable systems. The NVIDIA HPC SDK includes a CUDA-aware MPI library based on Open MPI with support for GPUDirect™ so you can send and receive GPU buffers directly using remote direct memory access (RDMA), including buffers allocated in CUDA Unified Memory. CUDA-aware Open MPI is fully compatible with CUDA C/C++, CUDA Fortran and the NVIDIA OpenACC compilers.

### Nsight Performance Profiling

Nsight™ Systems provides system-wide visualization of application performance on HPC servers and enables you to optimize away bottlenecks and scale parallel applications across multicore CPUs and GPUs. Nsight Compute allows you to deep dive into GPU kernels in an interactive profiler for GPU-accelerated applications via a graphical or command-line user interface, and allows you to pinpoint performance bottlenecks using the NVTX API to directly instrument regions of your source code.

 ![Nsight systems provides visualization of app performance on HPC servers](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/nsight-performance-profiling.jpg &quot;Nsight systems provides visualization of app performance on HPC servers&quot;)

 ![NVIDIA HPC SDK can deploy software anywhere using the HPC Container Maker](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/nvidia-gpu-cloud-hpc-apps-kv-16x9.jpg &quot;NVIDIA HPC SDK can deploy software anywhere using the HPC Container Maker&quot;)

### Deploy Anywhere

[Containers](https://developer.nvidia.com/ai-hpc-containers) simplify software deployment by bundling applications and their dependencies into portable virtual environments. The NVIDIA HPC SDK includes instructions for developing, profiling, and deploying software using the HPC Container Maker to simplify the creation of container images. The NVIDIA Container Runtime enables seamless GPU support in virtually all container frameworks, including Docker and Singularity.

 Technical blog: [Building and Deploying HPC Applications using NVIDIA HPC SDK from the NVIDIA NGC Catalog](https://developer.nvidia.com/blog/building-and-deploying-hpc-applications-using-hpc-sdk-from-ngc-catalog/). 

* * *

## What Users are Saying

_“On Perlmutter, we need Fortran, C and C++ compilers that support all the programming models our users need and expect on NVIDIA GPUs and AMD EPYC CPUs — MPI, OpenMP, OpenACC, CUDA and optimized math libraries. The NVIDIA HPC SDK checks all of those boxes.”_

**– Nicholas Wright, NERSC Chief Architect**

  

* * *

## HPC Compilers Support Services

HPC Compiler Support Services provide access to NVIDIA technical experts, including:

- Paid technical support for the NVFORTRAN, NVC++ and NVC compilers (NVCC excluded).
- Help with installation and usage of NVFORTRAN, NVC++ and NVC compilers.
- Confirmation of bug reports, prioritization of bug fixes above those from non-paid users.
- Where possible, help with temporary workarounds for confirmed compiler bugs.
- Access to release archives including both HPC SDK and legacy PGI packages.
- For more details please refer to [End Customer Terms &amp; Conditions.](http://docs.nvidia.com/hpc-sdk/compilers/hcss-terms-and-conditions/index.html)

### Get Started

- Interested in purchasing the support offer? [Contact us](mailto:enterpriseservices@nvidia.com). 
- Already have an active support contract and already registered for support? Log in to the [NVIDIA support portal](https://nvid.nvidia.com/dashboard).
- Existing customer and want to renew your contract? [Contact us](mailto:renewalsales@nvidia.com?subject=Renewing%20HPC%20Compilers%20Support%20Services). 
- Questions? Learn more by sending email to [enterpriseservices@nvidia.com](mailto:enterpriseservices@nvidia.com?subject=HPC%20Compilers%20Support%20Services%20Question). 

* * *

## Featured Content

## Resources

- [HPC SDK Documentation](https://docs.nvidia.com/hpc-sdk/index.html)
- [Developer Forums](https://forums.developer.nvidia.com/)
- Training: 
  - [Portable Acceleration of HPC Applications using ISO C++ - Part 1: Fundamentals](https://www.nvidia.com/en-us/on-demand/session/gtcspring23-dlit51170/)
  - [Portable Acceleration of HPC Applications using ISO C++ - Part 2: Fundamentals](https://www.nvidia.com/en-us/on-demand/session/gtcspring23-dlit51170/)
  - [Scaling GPU-Accelerated Applications with the C++ Standard Library](https://courses.nvidia.com/courses/course-v1:DLI+S-AC-09+V1/)

- [GPU Hackathons and Bootcamps](https://www.openhackathons.org/s/)
- Industry Articles: 
  - [Why Standards-Based Parallel Programming Should be in Your HPC Toolbox](https://www.hpcwire.com/2022/09/05/why-standards-based-parallel-programming-should-be-in-your-hpc-toolbox/?=&amp;linkId=100000147318917)
  - [Leveraging Standards-Based Parallel Programming in HPC Applications](https://www.hpcwire.com/2022/10/03/leveraging-standards-based-parallel-programming-in-hpc-applications/)
  - [New C++ Sender Library Enables Portable Asynchrony](https://www.hpcwire.com/2022/12/05/new-c-sender-library-enables-portable-asynchrony/)

- Technical Blogs: 
  - [Developing Accelerated Code with Standard Language Parallelism](/blog/developing-accelerated-code-with-standard-language-parallelism/)
  - [Multi-GPU Programming with Standard Parallel C++: Part One](/blog/multi-gpu-programming-with-standard-parallel-c-part-1/)
  - [Multi-GPU Programming with Standard Parallel C++: Part Two](/blog/multi-gpu-programming-with-standard-parallel-c-part-2/)
  - [Using Fortran Standard Parallel Programming for GPU Acceleration](/blog/using-fortran-standard-parallel-programming-for-gpu-acceleration/)
  - [N Ways to SAXPY: Demonstrating the Breadth of GPU Programming Options](/blog/n-ways-to-saxpy-demonstrating-the-breadth-of-gpu-programming-options)
  - [Accelerating Standard C++ with GPUs Using stdpar](/blog/accelerating-standard-c-with-gpus-using-stdpar/)
  - [Accelerating Fortran DO CONCURRENT with GPUs and the NVIDIA HPC SDK](/blog/accelerating-fortran-do-concurrent-with-gpus-and-the-nvidia-hpc-sdk/)
  - [Bringing Tensor Cores to Standard Fortran](/blog/bringing-tensor-cores-to-standard-fortran/)
  - [Building and Deploying HPC Applications Using NVIDIA HPC SDK from the NVIDIA NGC Catalog](/blog/building-and-deploying-hpc-applications-using-hpc-sdk-from-ngc-catalog/)
  - [Accelerating Python on GPUs with nvc++ and Cython](/blog/accelerating-python-on-gpus-with-nvc-and-cython/)
  - [Multinode Multi-GPU: Using NVIDIA cuFFTMp FFTs at Scale](/blog/multinode-multi-gpu-using-nvidia-cufftmp-ffts-at-scale/)
  - [Extending Block-Cyclic Tensors for Multi-GPU with NVIDIA cuTensorMg](/blog/extending-block-cyclic-tensors-for-multi-gpu-with-nvidia-cutensormg/)
  - [Accelerating GPU Applications with NVIDIA Math Libraries](/blog/accelerating-gpu-applications-with-nvidia-math-libraries/)
  - [Accelerating NVIDIA HPC Software with SVE on AWS Graviton3](/blog/accelerating-nvidia-hpc-software-with-sve-on-aws-graviton3/?ncid=so-twit-562255#cid=hpc06_so-twit_en-us)

- Presentations: 
  - [Standard Fortran on GPUs and its Utility in Quantum Chemistry Codes](https://www.youtube.com/watch?v=DrvI2gw3tnI)

- Related libraries and software: 
  - [NVIDIA GPUDirect®](/gpudirect)
  - [Magnum IO](https://www.nvidia.com/en-us/data-center/magnum-io/)

## Get Started

[Download](/nvidia-hpc-sdk-downloads)


