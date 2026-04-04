# Source: https://developer.nvidia.com/magnum-io.md

# NVIDIA MAGNUM IO SDK

## The IO Subsystem for the Modern, GPU-Accelerated Data Center

The NVIDIA MAGNUM IO™ software development kit (SDK) enables developers to remove input/output (IO) bottlenecks in AI, high performance computing (HPC), data science, and visualization applications, reducing the end-to-end time of their workflows. Magnum IO covers all aspects of data movement between CPUs, GPUsns, DPUs, and storage subsystems in virtualized, containerized, and bare-metal environments.

[Get Magnum IO Container](https://ngc.nvidia.com/catalog/containers/nvidia:magnum-io:magnum-io)

## Latest Magnum IO News

Magnum IO for Cloud-Native Supercomputing Architecture

Magnum IO, the IO subsystem for data centers, introduces the new enhancements necessary to accelerate IO and the communications supporting multi-tenant data centers, known as Magnum IO for Cloud-Native Supercomputing.

[Read More](/blog/accelerating-cloud-native-supercomputing-with-magnum-io/)

[![Magnum IO Cloud Native Architecture](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/magnum-io/magnum-io-cloud-native-architecture-cut-graphics-2c50-d%402x_1.jpg)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/magnum-io/magnum-io-cloud-native-architecture-cut-graphics-2c50-d%402x_1.jpg)

[![Volumetric Video Leveraging Magnum IO and Verizon 5G](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/magnum-io/magnum-demo-screen-grab-2c50-d@2x.jpg)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/magnum-io/magnum-demo-screen-grab-2c50-d@2x.jpg)

Volumetric Video Leveraging Magnum IO and Verizon 5G

Magnum IO GPUDirect over an InfiniBand network enables Verizon’s breakthrough distributed volumetric video architecture. By placing their technology into edge computing centers, located at sports centers around the United States and in Verizon facilities, they’re able to bring 3D experiences to media and serve up new options for putting you in the game.

[Watch Video](https://www.youtube.com/watch?v=YF1dsFjMkdw)

## Magnum IO Ecosystem

[![Magnum IO Web Diagram](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/Magnum_IO/nvidia-magnum-io-web-diagram.svg)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/Magnum_IO/nvidia-magnum-io-web-diagram.svg)
_The Magnum IO stack contains the libraries developers need to create and optimize applications IO across the whole stack: Networking across NVIDIA® NVLink®, Ethernet, and InfiniBand. Local and remote direct storage APIs. In-Networking Compute to accelerate multi-node operations. And IO management of networking hardware._

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/Magnum_IO/nvidia-abstractions-icon.svg)
### Flexible Abstractions

Magnum IO enables AI, data analytics, visualization, and HPC developers to innovate and accelerate applications built using common high-level abstractions and APIs.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/Magnum_IO/nvidia-scalability-icon.svg)
### Architected for Scale

Magnum IO technologies allow for scaling up computation to multiple GPUs via NVLink and PCIe and across multiple nodes on InfiniBand and Ethernet at data center scale.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/Magnum_IO/nvidia-management-icon.svg)
### Advanced IO Management

Advanced telemetry and monitoring built with NVIDIA NetQ™ and NVIDIA UFM® help users to configure, troubleshoot, and fine-tune the interconnect infrastructure for peak performance.

## Magnum IO Components

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/Magnum_IO/nvidia-network-icon.svg)
### Network IO

- [GPUDirect® RDMA](/gpudirect)
- [MOFED](https://www.mellanox.com/products/infiniband-drivers/linux/mlnx_ofed)
- [NCCL](/nccl)
- [NVIDIA ASAP2—Accelerated Switch and Packet Processing®](https://www.nvidia.com/en-us/networking/products/ethernet/)
- [NVIDIA HPC-X®](/networking/hpc-x)
- [NVSHMEM](/nvshmem)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/Magnum_IO/nvidia-storage-icon.svg)
### Storage IO

- [GPUDirect Storage](https://developer.nvidia.com/gpudirect-storage)
- SNAP

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/Magnum_IO/nvidia-inference-icon.svg)
### In-Network Computing

- Hardware tag matching
- [NVIDIA Scalable Hierarchical Aggregation and Reduction Protocol (SHARP)™](https://docs.mellanox.com/display/SHARPv200/Introduction)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/Magnum_IO/nvidia-management-icon.svg)
### IO Management

- [NVIDIA NetQ](nvidia.com/en-us/networking/ethernet-switching/netq/), [WJH](https://www.mellanox.com/products/what-just-happened)
- [NVIDIA UFM](https://www.nvidia.com/en-us/networking/infiniband/ufm/)

## Accelerating IO Across Applications

### Deep Learning

Magnum IO networking provides both point-to-point functions like send and receive, and collectives like AllReduce for deep learning training at scale. The collective APIs hide low-level optimizations like topology detection, peer-to-peer copy, and multi-threading to simplify deep learning training. Send/receive can enable users to accelerate giant deep learning models too big to fit in one GPU’s memory. GPUDirect Storage can also help alleviate IO bottlenecks from local or remote storage by bypassing bounce buffers on the CPU host.

### High-Performance Computing

To unlock next-generation discoveries, scientists rely on simulation to better understand complex molecules for drug discovery, physics for new sources of energy, and atmospheric data to better predict extreme weather patterns. Magnum IO exposes hardware-level acceleration engines and smart offloads, such as RDMA, GPUDirect, and NVIDIA SHARP, while bolstering the 400Gb/s high bandwidth and ultra-low latency of NVIDIA Quantum 2 InfiniBand networking.

With multi-tenancy, user applications may be unaware of indiscriminate interference from neighboring application traffic. Magnum IO, on the latest NVIDIA Quantum-2 InfiniBand platform, features new and improved capabilities for mitigating the negative impact on a user’s performance. This delivers optimal results, as well as the most efficient high performance computing (HPC) and machine learning deployments at any scale.

### Data Analytics

Data science and machine learning are the world&#39;s largest compute segments. Modest improvements in the accuracy of predictive machine learning models can translate into billions of dollars. To enhance accuracy, the RAPIDS™ Accelerator for Apache Spark library has a built-in shuffle based on NVIDIA UCX® that can leverage GPU-to-GPU communication and RDMA capabilities. Combined with NVIDIA networking, Magnum IO, GPU-accelerated Spark 3.0, and RAPIDS, the NVIDIA data center platform can speed up these huge workloads at unprecedented levels of performance and efficiency.

## Resources

- [Magnum IO Developer Environment Documentation](https://github.com/NVIDIA/MagnumIO/blob/main/dev-env/README.md)
- [GPUDirect Storage: A Direct Path Between Storage and GPU Memory](https://developer.nvidia.com/blog/gpudirect-storage/)
- [Accelerating IO in the Modern Data Center: Network IO](https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io/)
- [Accelerating NVSHMEM 2.0 Team-Based Collectives Using NCCL](https://developer.nvidia.com/blog/accelerating-nvshmem-2-0-team-based-collectives-using-nccl/)
- [Optimizing Data Movement in GPU Applications with the NVIDIA Magnum IO Developer Environment](https://developer.nvidia.com/blog/optimizing-data-movement-in-gpu-apps-with-magnum-io-developer-environment/)
- [Access MOFED](https://www.mellanox.com/products/infiniband-drivers/linux/mlnx_ofed)

Get Started Using the Magnum IO Developer Environment

The Magnum IO Developer Environment is available as a container with the latest versions of all libraries, development tools, and profiling tools needed to begin development and optimization. The optimized applications can then be run in virtualized, containerized, or bare-metal environments.

  
[Download on Github](https://github.com/NVIDIA/MagnumIO) [Download on NGC](https://ngc.nvidia.com/catalog/containers/nvidia:magnum-io:magnum-io)  


