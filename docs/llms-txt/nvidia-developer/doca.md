# Source: https://developer.nvidia.com/networking/doca.md

1. [Home](/)

[Networking](/networking)

NVIDIA DOCA

# NVIDIA DOCA Software Framework  

# Accelerate application development for NVIDIA BlueField and ConnectX networking devices.

NVIDIA DOCA™ unlocks the potential of the NVIDIA® BlueField® networking platform. By harnessing the power of BlueField DPUs and SuperNICs, DOCA enables the rapid creation of applications and services that offload, accelerate, and isolate data center workloads. It lets developers create software-defined, cloud-native, DPU- and SuperNIC-accelerated services with zero-trust protection, addressing the performance and security demands of modern data centers. DOCA-Host includes all needed host drivers and tools for your NVIDIA BlueField and ConnectX® devices.

[Download DOCA](http://developer.nvidia.com/doca-downloads &quot;Github Repo&quot;)[Get Started](https://developer.nvidia.com/networking/doca/getting-started &quot;Download Workflows&quot;)

![NVIDIA DOCA software framework diagram](https://developer.download.nvidia.com/images/doca/doca-3.0-stack-diagram.svg)

Together, DOCA and the BlueField networking platform enable the development of applications that deliver breakthrough networking, security, and storage performance. BlueField isolates the infrastructure service domain from the workload domain to offer significant improvements in application and server performance, security, and efficiency, giving developers all the tools they need to realize optimal, secure, accelerated data centers and AI clouds.  
  
DOCA software consists of an SDK and a runtime environment. The DOCA runtime, included by default with the BlueField networking platform, has tools for provisioning, deploying, and orchestrating containerized services on hundreds or thousands of DPUs and SuperNICs across the data center. The DOCA SDK provides industry-standard open APIs and software frameworks. The SDK supports a range of operating systems and distributions and includes drivers, libraries, tools, documentation, and example applications.   
  
DOCA-Host is the DOCA package for host installation and includes several installation profiles to best fit your data center workflows. DOCA-Host provides the needed interfaces for NVIDIA networking platforms, including both BlueField and ConnectX devices.

[Read the DOCA User Manual](https://docs.nvidia.com/doca/sdk/)
* * *

## Platform and Host Deployments

 ![NVIDIA DOCA software applications running on NVIDIA BlueField DPU](https://developer.download.nvidia.com/images/doca/doca-blue-field-networking-platform.jpg)
### DOCA on the BlueField Networking Platform

The NVIDIA BlueField networking platform, powered by the DOCA software framework, is an advanced computing platform for data center infrastructure, delivering accelerated software-defined networking, storage, security, and management services at massive scale.

[Learn About BlueField](https://www.nvidia.com/en-us/networking/products/data-processing-unit/)

 ![NVIDIA DOCA software applications running on a host server box](https://developer.download.nvidia.com/images/doca/doca-host.jpg)
### DOCA on the Host

NVIDIA BlueField and NVIDIA Connect-X are paired with DOCA to deliver Ethernet and InfiniBand connectivity solutions at speeds up to 800 gigabits per second (Gb/s). Built on an open foundation, the DOCA-host package includes essential drivers and tools to enhance networking performance and enable advanced functionality. DOCA software is available on every leading operating system as a standalone package (without a bundled OS) for Arm® and x86 architectures.

[Learn About DOCA-Host Installation and Profiles](https://docs.nvidia.com/doca/sdk/nvidia+doca+profiles/index.html)

* * *

## Unpack the Stack

# BlueField Software Bundle 

- 

The BlueField software bundle includes the bootloader, OS kernel, necessary network interface card (NIC) firmware, NVIDIA drivers, sample filesystem, and toolchain—all certified as part of the NVIDIA NGC™ catalog.

- 

The BlueField bundle includes Ubuntu 22.04 as a commercial-grade Linux distribution with continuous OS and security updates.

 ![A stack diagram of NVIDIA DOCA software apps running on Arm core of NVIDIA BlueField DPU](https://developer.download.nvidia.com/images/doca/blue-field-software-bundle.jpg)

 ![A stack diagram of NVIDIA DOCA business apps isolated from NVIDIA DOCA on infrastructure services domain](https://developer.download.nvidia.com/images/doca/sdk-key-components.jpg)

# SDK Key Components  

- 

DOCA RDMA (Remote direct-memory access) acceleration SDK: unified communications and collaboration (UCC) and Unified Communication X (UCX), RDMA verbs, GPUDirect®

- 

Network acceleration SDK: NVIDIA Accelerated Switching and Packet Processing (ASAP2)™ software-defined networking (SDN), emulated VirtIO, P4, 5T for 5G technology, Firefly time synchronization

- 

Security acceleration SDK: inline cryptography, App Shield runtime security

- 

Storage acceleration SDK: storage emulation and virtualization, crypto and compression

- 

Data path acceleration (DPA) SDK: accelerate workloads requiring high-performance access to NIC engines

- 

Management SDK: deployment, provisioning, service orchestration

- 

Industry-standard APIs: DPDK, SPDK, P4, Linux Netlink

- 

User space and kernel

 ![A decorative image showing an interapplication workflow on a monitor](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/devzone-networking-doca-sdk-icon-infrastrucure.svg)
### Forward and Backward Compatibility

DOCA provides multi-generational support to ensure that applications developed today will consistently run with added performance benefits on all future generations of BlueField.

 ![A decorative image of a cloud networking telemetry](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/devzone-networking-doca-sdk-icon-doca.svg)
### Offload, Accelerate, Isolate Infrastructure  

Network, storage, and security services are offloaded, accelerated, and isolated on BlueField while data is securely delivered to workloads at wire speed.

 ![A decorative image of a neural network](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/devzone-networking-doca-sdk-icon-sol.svg)
### Open Ecosystem

DOCA offers a software application framework to accelerate ecosystem development.

* * *

## DOCA Developer Resources  

# DOCA-Host and BlueField Bundle Runtime Downloads

Download DOCA-Host and the BlueField DPU and SuperNIC runtime image.

[Download DOCA](http://developer.nvidia.com/doca-downloads &quot;Github Repo&quot;)[Get Started](https://developer.nvidia.com/networking/doca/getting-started &quot;Download Workflows&quot;)

Quick Links

- [Download DOCA](http://developer.nvidia.com/doca-downloads)
- [Getting Started](https://developer.nvidia.com/networking/doca/getting-started)
- [DOCA Documentation](https://docs.nvidia.com/doca/sdk/)
- [BlueField Hardware Manual](https://docs.nvidia.com/networking/dpu-doca/index.html#dpu-hw)
- [BlueField Platform Software Manuals](https://docs.nvidia.com/networking/dpu-doca/index.html#dpu-os)

* * *


