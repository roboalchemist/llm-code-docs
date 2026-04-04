# Source: https://developer.nvidia.com/compute-sanitizer.md

# NVIDIA Compute Sanitizer

## Compute Sanitizer Tools &amp; API
  

**Compute Sanitizer** is a functional correctness checking suite. This suite contains multiple tools that can perform different type of checks. Tool features are described below.

  

The **Compute Sanitizer API** enables the creation of sanitizing and tracing tools that target CUDA applications. Examples of such tools are memory and race condition checkers. The Compute Sanitizer API is composed of three APIs: the callback API, the patching API and the memory API. It is delivered as a dynamic library on supported platforms.

  

### [Memcheck](https://docs.nvidia.com/cuda/sanitizer-docs/ComputeSanitizer/index.html#memcheck-tool)

The _memcheck_ tool is a run time error detection tool for CUDA applications. The tool can precisely detect and report out of bounds and misaligned memory accesses to global, local and shared memory in CUDA applications. It can also detect and report hardware reported error information. In addition, the memcheck tool can detect and report memory leaks in the user application.

### [Racecheck](https://docs.nvidia.com/cuda/sanitizer-docs/ComputeSanitizer/index.html#racecheck-tool)

The _racecheck_ tool is a run time shared memory data access hazard detector. The primary use of this tool is to help identify memory access race conditions in CUDA applications that use shared memory.

In CUDA applications, storage declared with the _\_\_shared\_\__ qualifier is placed on chip _shared memory_. All threads in a thread block can access this per block shared memory. Shared memory goes out of scope when the thread block completes execution. As shared memory is on chip, it is frequently used for inter-thread communication and as a temporary buffer to hold data being processed. As this data is being accessed by multiple threads in parallel, incorrect program assumptions may result in data races. Racecheck is a tool built to identify these hazards and help users write programs free of shared memory races.

Currently, this tool only supports detecting accesses to on-chip shared memory.

### [Initcheck](https://docs.nvidia.com/cuda/sanitizer-docs/ComputeSanitizer/index.html#initcheck-tool)

The _initcheck_ tool is a run time uninitialized device global memory access detector. This tool can identify when device global memory is accessed without it being initialized via device side writes, or via CUDA memcpy and memset API calls.

Currently, this tool only supports detecting accesses to device global memory.

### [Synccheck](https://docs.nvidia.com/cuda/sanitizer-docs/ComputeSanitizer/index.html#synccheck-tool)

The _synccheck_ tool is a runtime tool that can identify whether a CUDA application is correctly using synchronization primitives, specifically \_\_syncthreads() and _\_\_syncwarp()_ intrinsics and their Cooperative Groups API counterparts.

  

### Developer Benefits 

**Compute Sanitizer** : Provides the ability to ensure the code correctness of your GPU accelerated kernels  
**Compute Sanitizer API** : Provides the ability to incorporate GPU code correctness into your own tools

  

**Both the Compute Sanitizer suite and API are available in the CUDA Toolkit. You may obtain the latest version of Compute Sanitizer by downloading the CUDA Toolkit**

[  Download the CUDA Toolkit Now ](https://developer.nvidia.com/cuda-downloads)
##### [Sanitizer Tools documentation](https://docs.nvidia.com/cuda/sanitizer-docs/ComputeSanitizer/index.html)  |   [Sanitizer API documentation](https://docs.nvidia.com/cuda/sanitizer-docs/SanitizerApiGuide/index.html)  |   [Revision History](https://docs.nvidia.com/cuda/sanitizer-docs/ReleaseNotes/index.html)

**NVIDIA® Compute Sanitizer** is freely offered through the [NVIDIA Registered Developer Program](/sign-up-gameworks-registered-developer-program) and as part of the [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit)  
  


