# Source: https://developer.nvidia.com/nccl.md

1. [Cloud and Data Center](/aerial)

[Networking](/networking)

NCCL

# NVIDIA Collective Communications Library (NCCL)

The NVIDIA Collective Communication Library (NCCL) implements multi-GPU and multi-node communication primitives optimized for NVIDIA GPUs and networking. 

[Download NCCL](https://developer.nvidia.com/nccl/nccl-download &quot;Download&quot;)[Documentation](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html# &quot;Documentation&quot;)[Release Notes  
  
  
](https://docs.nvidia.com/deeplearning/nccl/release-notes/index.html &quot;Release Notes&quot;)[GitHub](https://github.com/NVIDIA/nccl &quot;GitHub&quot;)[NCCL API Guide](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api.html &quot;NCCL API Guide&quot;)

* * *

## How NCCL Works 

NCCL provides routines such as all-gather, all-reduce, broadcast, reduce, reduce-scatter, and point-to-point send and receive. These routines are optimized to achieve high bandwidth and low latency over PCIe,NVIDIA NVLink™, and other high-speed interconnects within a node and over NVIDIA networking across nodes.  
  
With its single-kernel implementation of communication and computation, NCCL ensures low-latency synchronization, making it ideal for both distributed training and real-time inference scenarios. Developers can scale across nodes without tuning for specific hardware configurations, thanks to the NCCL dynamic topology detection and streamlined C-based API.  
  
NCCL can be built and installed through [Github](https://github.com/NVIDIA/nccl). NCCL is also available for download as part of the [NVIDIA HPC SDK](/hpc-sdk) and through binaries on the [NVIDIA developer zone](/nccl/nccl-download).

![This is how NVIDIA Collective Communication Library (NCCL) works](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/NCCL_1GPU_multiGPU.png)

### Performance

NCCL removes the need for developers to optimize their applications for specific machines. NCCL provides fast collectives over multiple GPUs both within and across nodes.

### Ease of Programming

NCCL uses a simple C API that can be easily accessed from a variety of programming languages. NCCL closely follows the popular collectives API defined by Message Passing Interface (MPI).

### Compatibility

NCCL is compatible with any multi-GPU parallelization model, including single-threaded, multi-threaded (using one thread per GPU), and multi-process (MPI combined with multi-threaded operation on GPUs).

* * *

## Key Features

- 

High-performance collective and point-to-point communication for faster multi-GPU and multi-node training

- 

Device APIs that enable communication directly from CUDA kernels, unlocking lower latency and better compute–communication overlap

- 

Automatic topology detection across PCIe, NVLink™, NVSwitch™, InfiniBand, RoCE, and other networks to maximize performance

- 

Advanced graph search algorithms that build the most efficient rings and trees for peak bandwidth and minimal latency

- 

Flexible plugin framework that extends NCCL to custom transports and next-generation interconnects

- 

Full support for multi-threaded, multi-process, and MPI-driven distributed applications

- 

Integrated profiling, reliability, and observability tools like NCCL RAS and NCCL Inspector to accelerate debugging and performance tuning

* * *

## NCCL Blogs

* * *

## More Resources

Check out the following videos presented by our NCCL team to learn more.

- 

[GTC Webinar](https://www.nvidia.com/en-us/on-demand/session/gtc25-s72583/)

- 

[Multi-GPU Programming in NCCL and NVSHMEM](https://www.youtube.com/live/2xMzQ1Z2Qe0)

- 

[GPU Communication Libraries Tutorial](https://www.youtube.com/watch?v=rlA5QreHekk&amp;list=PLBM5Lly_T4yRGBFgforeMTDpjasC_PV7r&amp;index=32)

Learn more about related libraries and software.

- 

[NVIDIA HPC SDK](/hpc-sdk)

- 

[cuDNN](/cudnn)

- 

[cuBLAS](/cublas)

- 

[NVIDIA DALI®](/dali)

- 

[NVIDIA NGC™](https://ngc.nvidia.com/)

- 

[NVIDIA Magnum IO™](https://www.nvidia.com/en-us/data-center/magnum-io/)

 ![Decorative image representing Developer Newsletter](https://developer.download.nvidia.com/icons/m48-email-settings.svg)
### Submit a Bug, RFE, or Question

 ![Decorative image representing Developer Community](https://developer.download.nvidia.com/icons/m48-developer-1.svg)
### Join the NVIDIA Developer Program

Get started with NCCL today.

[Download NCCL](/nccl/nccl-download &quot;Download NCCL&quot;)


