# Source: https://developer.nvidia.com/networking/hpc-x.md

# NVIDIA HPC-X

## Increase scalability and performance of messaging communications.

NVIDIA® HPC-X® is a comprehensive software package that includes Message Passing Interface (MPI), Symmetrical Hierarchical Memory (SHMEM) and Partitioned Global Address Space (PGAS) communications libraries, and various acceleration packages. This full-featured, tested, and packaged toolkit enables MPI and SHMEM/PGAS programming languages to achieve high performance, scalability, and efficiency and ensures that communication libraries are fully optimized by NVIDIA Quantum InfiniBand networking solutions.

### Performance at Any Scale

HPC-X takes advantage of NVIDIA Quantum InfiniBand hardware-based networking acceleration engines to maximize application performance. It dramatically reduces MPI operation time, freeing up valuable CPU resources, and decreases the amount of data traversing the network, allowing unprecedented scale to reach evolving performance demands.

 ![NVIDIA In-Network Computing](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/networking/hpc-x/nvidia-mellanox-in-network-2c50-d%402x.jpg)

## Software and Acceleration Packages

### HPC-X MPI

MPI is a standardized, language-independent specification for writing message-passing programs. NVIDIA HPC-X MPI is a high-performance, optimized implementation of Open MPI that takes advantage of NVIDIA’s additional acceleration capabilities, while providing seamless integration with industry-leading commercial and open-source application software packages.

[Learn More](https://docs.mellanox.com/category/hpcx)

### HPC-X OpenSHMEM

The HPC-X OpenSHMEM programming library is a one-side communications library that supports a unique set of parallel programming features, including point-to-point and collective routines, synchronizations, atomic operations, and a shared memory paradigm used between the processes of a parallel programming application.

[Learn More](https://docs.mellanox.com/category/hpcx)

### In-Network Computing

NVIDIA Scalable Hierarchical Aggregation and Reduction Protocol (SHARP™) improves the performance of MPI operations by offloading them from the CPU to the switch network and eliminating the need to send data multiple times, decreasing the amount of data traversing the network and dramatically reducing MPI operation time.

[Learn More](https://docs.mellanox.com/category/hpcx)

### Unified Communication X

Unified Communications X (UCX®) is an open-source communication framework for data-centric and high-performance applications. UCX provides a low-overhead, point-to-point communication path for near-native, hardware-level performance with cross-platform support.

[Learn More](https://docs.mellanox.com/category/hpcx)

### Unified Collective Communication

Unified Collective Communication (UCC) is an open-source communication framework for high-performance applications. UCC provides low-overhead collective communications leveraging InfiniBand In-Network Computing acceleration engines.

[Learn More](https://docs.mellanox.com/category/hpcx)

### NCCL/SHARP and UCX Support

NCCL-RDMA plug-ins enable remote direct-memory access (RDMA) and switch-based collectives (SHARP) with the NVIDIA Collective Communication Library (NCCL). The NCCL UCX plug-in replaces the default NCCL verbs-based inter-node communication routines with UCX-based communication routines for enhanced performance.

[Learn More](https://docs.mellanox.com/category/hpcx)

### ClusterKit

ClusterKit is a multifaceted node-assessment tool for high-performance clusters. ClusterKit employs well-known techniques and tests to ensure the health and performance of a cluster.

[Learn More](https://docs.mellanox.com/category/hpcx)

### Key Features

- Offloads collectives communications from MPI onto NVIDIA Quantum InfiniBand networking hardware
- Multiple transport support, including Reliable Connection (RC), Dynamic Connected (DC), and Unreliable Datagram (UD)
- Intra-node shared memory communication
- Receive-side tag matching
- Native support for MPI-3
- Multi-rail support with message striping
- NVIDIA GPUDirect® with CUDA® support
- NCCL-RDMA-SHARP plug-in support

### Benefits

- Increases CPU availability, application scalability, and system efficiency for improved application performance
- Ensures node-level and system-level health and performance
- Maximizes application performance with underlying hardware architecture
- Fully optimized for NVIDIA Quantum InfiniBand networking solutions
- Supports any interconnect based on InfiniBand or Ethernet standards

  

## Resources

- [
Datasheet
](#product-briefs)
- [
Reference Guide
](#reference-guide)
- [
Download
](#download)

- [NVIDIA HPC-X](https://nvdam.widen.net/s/8xqvk2vprd/infiniband-hpcx-datasheet-web)

- [NVIDIA HPC-X Product Documentation](https://docs.mellanox.com/category/hpcx)
- [NVIDIA Scalable Hierarchical Aggregation and Reduction Protocol (SHARP) Product Documentation](https://docs.mellanox.com/category/mlnxsharp)
- [NVIDIA Scalable Hierarchical Aggregation and Reduction Protocol (SHARP) API Guide](https://www.mellanox.com/files/related-docs/prod_acceleration_software/Mellanox_SHARP_SW_API_Guide.pdf)

https://downloaders.azurewebsites.net/downloaders/hpcx_downloader/downloader2.html?1

### See how you can build the most efficient, high-performance network.
  
[Request a Demo](https://mellanox.secure.force.com/VF_Lead_Demo_Form)

### Configure Your Cluster

[GET STARTED](https://www.mellanox.com/solutions/configuration-tools)

### Take Networking Courses

[LEARN MORE](https://academy.mellanox.com)

### Ready to Purchase?

[HOW TO BUY](https://store.mellanox.com/)


