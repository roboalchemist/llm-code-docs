# Source: https://developer.nvidia.com/cupti.md

# NVIDIA CUDA Profiling Tools Interface (CUPTI) - CUDA Toolkit

The **NVIDIA CUDA Profiling Tools Interface (CUPTI)** is a library that enables the creation of profiling and tracing tools that target CUDA applications. CUPTI provides a set of APIs targeted at ISVs creating profilers and other performance optimization tools:

- the Activity API,
- the Callback API,
- the Host Profiling API,
- the Range Profiling API,
- the PC Sampling API,
- the SASS Metric API,
- the PM Sampling API,
- the Checkpoint API,
- the Profiling API,
- the Python API (available [separately](https://pypi.org/project/cupti-python/))

Using these CUPTI APIs, independent software developers can create profiling tools that provide low and deterministic profiling overhead on the target system, while giving insight into the CPU and GPU behavior of CUDA applications. Normally packaged with the CUDA Toolkit, NVIDIA occasionally uses this page to provide CUPTI improvements and bug fixes between toolkit releases.

  
  

**There is currently no CUPTI update to the CUDA Toolkit 13.1 Update 1. You may obtain the latest version of CUPTI by Downloading the CUDA Toolkit 13.1.1**

[Download the CUDA Toolkit 13.1 Update 1 Now](https://developer.nvidia.com/cuda-13-1-1-download-archive)[Download the CUDA Toolkit 13.1 Now](https://developer.nvidia.com/cuda-13-1-0-download-archive)  
[Download the CUPTI Python API 13.0.0 Now](https://pypi.org/project/cupti-python/13.0.0/)
##### [Revision History](/cupti-history)

#### Key Features

- Trace CUDA API by registering callbacks for API calls of interest

  - Full support for entry and exit points in the CUDA C Runtime (CUDART) and CUDA Driver

- GPU workload trace for the activities happening on the GPU, which includes kernel executions, memory operations (e.g., Host-to-Device memory copies) and memset operations.
- CUDA Unified Memory trace for transfers from host to device, device to host, device to device and page faults on CPU and GPU etc.
- Normalized timestamps for CPU and GPU trace
- Profile hardware and software event counters, including:

  - Utilization metrics for various hardware units
  - Instruction count and throughput
  - Memory load/store events and throughput
  - Cache hits/misses
  - Branches and divergent branches
  - Many more

- Enables automated bottleneck identification based on metrics such as instruction throughput, memory throughput, and more
- Range profiling to enable metric collection over concurrent kernel launches within a range
- Metrics attribution at the high-level source code and the executed assembly instructions.
- Device-wide sampling of the program counter (PC). The PC Sampling gives the number of samples for each source and assembly line with various stall reasons.

 See the CUPTI User Guide for a complete listing of hardware and software event counters available for performance analysis tools. 
#### Updates in CUDA Toolkit 13.1 Update 1 

##### Resolved Issues

  - Fixed incorrect correlation IDs for `cudaGraphLaunch` API calls and their associated kernel launches in profiling sessions after the first session.
  - Fixed issue where CUPTI graph creation callbacks were not triggered for CUDA device graphs under green context.
  - Fixed linker error when linking the static CUPTI library from CUDA 13.0 and 13.1 GA releases.
  - Fixed issue where CUPTI limited activity buffer records to 2GB regardless of the configured activity buffer size.

#### Updates in CUDA Toolkit 13.1 

##### New Features

  - Added support for Compute Engine context switch events. For more details, refer to the section [Compute Engine Context Switch](https://docs.nvidia.com/cupti/main/main.html#activity-ce-context-switch).
  - Added tracing for host execution nodes in CUDA Graphs i.e. nodes of type `CU_GRAPH_NODE_TYPE_HOST`. Enable with the activity kind `CUPTI_ACTIVITY_KIND_GRAPH_HOST_NODE`; records are reported as `CUpti_ActivityGraphHostNode`. 
  - Added tracing for host launches done by CUDA through `cudaLaunchHostFunc()` API. This is important in understanding the device bubbles in the stream timeline. Enable with the activity kind `CUPTI_ACTIVITY_KIND_HOST_LAUNCH`; records are reported as `CUpti_ActivityHostLaunch`. 
  - Users can query the collection scope for any metric. The `CUpti_MetricCollectionScope` enum lists the possible scopes: context or device. A parameter, `metricCollectionScope`, is added to `CUpti_Profiler_Host_GetMetricProperties_Params` to return the collection scope for a metric. 
  - By default, the counter availability image stores only context-level metrics in the binary blob. A new parameter, `bAllowDeviceLevelCounters` , has been added to the counter availability API struct `CUpti_Profiler_GetCounterAvailability_Params` to include device-level metrics in the image. 
  - Added a new parameter `sku` in `CUpti_Profiler_DeviceSupported_Params` for checking profiling support for a GPU SKU. 
  - Added a new parameter `priority` in the kernel record to provide the launch priority of the kernel. The `CUpti_ActivityKernel10` activity record is deprecated and replaced by the new `CUpti_ActivityKernel11` activity record. 

##### Resolved Issues

  - Fixed an issue that could cause invalid (zero) kernel timestamps when using the function `cuptiActivityRegisterTimestampCallback` to register a timestamp callback. This issue was introduced in the CUDA 12.6 Update 2 release. 

#### Requirements

##### Supported platforms

  - Linux x86\_64[1]
  - Windows x86\_64[1]
  - Linux aarch64 SBSA[1]
  - DRIVE OS QNX aarch64[2]
  - DRIVE OS Linux aarch64[2]

 [1] available in the [CUDA Desktop Toolkit](https://developer.nvidia.com/cuda-downloads) only   
 [2] available in the [Embedded](https://developer.nvidia.com/embedded/develop/tools) or [Drive](https://developer.nvidia.com/drive/drive-sdk) toolkits only   

##### Supported NVIDIA GPU architectures

  - Activity and Callback APIs

    - All architectures supported by CUDA Toolkit

  - Profiling and PC Sampling APIs

    - Blackwell: B100, GB10x, GB11x
    - Hopper: GH100
    - Ada: AD10x
    - Ampere: A100 with Multi-Instance GPU, GA10x
    - Turing

##### CUDA Toolkit

  - CUPTI can be found in the [CUDA Toolkit 13.1 Update 1](https://developer.nvidia.com/cuda-downloads) production release

##### Drivers

 Please use the following drivers 
    - 591.59 (Windows) available at the [NVIDIA Driver Download page](https://www.nvidia.com/Download/index.aspx).
    - 590.48.01 (Linux) provided with [CUDA Toolkit 13.1 Update 1](https://developer.nvidia.com/cuda-downloads) production release.

#### Documentation

- [Online Product Documentation](https://docs.nvidia.com/cupti/index.html)

#### Support

To provide feedback, request additional features, or report issues, please use the [Developer Forums](https://forums.developer.nvidia.com/c/developer-tools/cuda-profiler-tools-interface-cupti/109).

#### Installation Overview

When installing [CUDA Toolkit 13.1 Update 1](https://developer.nvidia.com/cuda-downloads) and specifying options, be sure to select CUDA \&gt; Development \&gt; Tools \&gt; CUPTI.


