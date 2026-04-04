# Source: https://developer.nvidia.com/embedded/jetpack.md

1. [Home  
](/)

[Embedded Computing](/embedded/develop/software)

JetPack

# NVIDIA JetPack

NVIDIA JetPack™ is the official software stack for the NVIDIA Jetson™ platform, giving you a comprehensive suite of tools and libraries for building AI-powered edge applications. JetPack 7, the latest evolution in the series, is the most advanced software stack yet, purpose-built to enable cutting-edge robotics and generative AI at the edge. With full support for NVIDIA Jetson platforms, JetPack 7 provides ultra-low latency, deterministic performance, and scalable deployment for machines that interact with the physical world.

[JetPack Downloads and Notes](/embedded/jetpack/downloads &quot;vMaterials for Windows&quot;)[Jetson Linux Developer Guide](https://docs.nvidia.com/jetson/archives/r38.4/DeveloperGuide/ &quot;vMaterials for Linux &quot;)[Developer Forum](https://forums.developer.nvidia.com/c/robotics-edge-computing/jetson-embedded-systems/jetson-thor/740 &quot;vMaterials for Linux &quot;)

* * *

## JetPack 7 Overview

JetPack 7 gives you full support for the NVIDIA® Jetson [Thor](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)™ platform, preemptable real-time kernel, Multi-Instance GPU (MIG), and integrated [Holoscan Sensor Bridge](https://www.nvidia.com/en-us/technologies/holoscan-sensor-bridge/). Built on Linux Kernel 6.8 and Ubuntu 24.04 LTS, and designed with a modular, cloud-native architecture, it integrates the latest NVIDIA AI compute stack and seamlessly integrates with NVIDIA AI workflows. Whether you’re developing humanoid robots or building an application with the most demanding generative AI workload, JetPack 7 delivers the software foundation to bring them to life.

**JetPack 7 is architected with SBSA architecture**  
  
With JetPack 7, Jetson software aligns with the Server Base System Architecture (SBSA), positioning Jetson Thor alongside industry-standard ARM server design. SBSA standardizes critical hardware and firmware interfaces, delivering stronger OS support, simpler software portability, and smoother enterprise integration. Building on this foundation, Jetson Thor now supports a unified CUDA 13.0 installation across all Arm targets, streamlining development, reducing fragmentation, and ensuring consistency from server-class systems to Jetson Thor.

[![NVIDIA Jetson software stack](https://developer.download.nvidia.com/images/jetson/jetson-software-stack-diagram-r1-01(1).svg &quot;NVIDIA Jetson software stack&quot;)](https://developer.download.nvidia.com/images/jetson/jetson-software-stack-diagram-r1-01(1).svg)

Click Image to Enlarge

* * *

## Components of the JetPack SDK 

### AI Compute Stack

Note: Jetson Thor is based on the SBSA stack. Please use the SBSA installer when installing from the links below.

#### CUDA  

The NVIDIA® CUDA® Toolkit provides a powerful development environment for creating GPU-accelerated applications, including a compiler, math libraries, and debugging tools.

[Explore CUDA](/cuda-toolkit)

#### cuDNN  

The NVIDIA cuDNN (CUDA Deep Neural Network) library offers high-performance primitives for deep learning, with optimized implementations for convolution, pooling, normalization, and activation layers.

[Explore cuDNN](/cudnn)

#### TensorRT  

NVIDIA TensorRT™ is a high-performance inference runtime that optimizes and accelerates deep learning models, delivering low latency and high throughput across major frameworks.

[Explore TensorRT](/tensorrt)

### AI Frameworks

#### PyTorch  

PyTorch is a fast, flexible deep learning framework with NGC containers for easy deployment across AI tasks like NLP, computer vision, and recommendation systems.

[Explore PyTorch](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch)

#### vLLM  

vLLM is a fast and easy-to-use library for LLM inference and serving.

Coming Soon

#### SGLang

SGLang is a fast serving framework for large language models and vision language models.

Coming Soon  
  

#### Triton Inference Server

NVIDIA Triton Inference Server™ enables seamless AI deployment across cloud and edge environments, ensuring consistency and performance optimization.

[See Triton Inference Server](https://github.com/triton-inference-server)

### Jetson Linux Components and Libraries

#### Flashing

Jetson devices can be flashed with Jetson Linux through multiple methods, from command-line tools to automated scripts, with NVIDIA SDK Manager offering the most user-friendly option.

[Explore Flashing](https://docs.nvidia.com/jetson/archives/r38.4/DeveloperGuide/SD/FlashingSupportJetsonThor.html)

#### Security

Jetson Linux delivers a comprehensive suite of security features spanning edge to cloud, including secure boot, disk encryption, runtime integrity, fTPM, and secure OTA updates.

[Explore Security](https://docs.nvidia.com/jetson/archives/r38.4/DeveloperGuide/SD/Security.html)

#### OTA

OTA (Over-the-Air) updates on Jetson enable seamless, remote delivery of software and security upgrades, keeping devices up-to-date without manual intervention.

[Explore JetPack Flashing](https://docs.nvidia.com/jetson/archives/r38.4/DeveloperGuide/SD/SoftwarePackagesAndTheUpdateMechanism.html#over-the-air-update)

#### Graphics Libraries

Jetson supports various graphics APIs, including OpenGL, Vulkan, and EGL, enabling GPU-accelerated rendering and compute for advanced 3D graphics and UI rendering.

[Explore Graphics APIs](https://docs.nvidia.com/jetson/archives/r38.4/DeveloperGuide/SD/Graphics.html)

#### Multimedia APIs

Jetson Linux Multimedia APIs provide low-level access to camera and video processing hardware. This lets you create high-performance applications with fine-grained control over multimedia pipelines.

[Explore Multimedia APIs](https://docs.nvidia.com/jetson/archives/r38.4/DeveloperGuide/SD/Multimedia.html)

#### Computer Vision Libraries

JetPack includes optimized computer vision libraries like OpenCV and VisionWorks that accelerate image processing and vision tasks on Jetson platforms using GPUs and dedicated hardware.

[See Computer Vision Libraries](/computer-vision-sdk)

### Other JetPack Components

#### Jetson Platform Services

Jetson Platform Services is a modular software suite that accelerates AI development on Jetson and helps with rapid deployment of edge applications.

[See Jetson Platform Services](/embedded/jetpack/jetson-platform-services-get-started)

#### Cloud-Native Design

Cloud-native design on Jetson helps you create scalable AI applications at the edge with containerized development, Kubernetes, and microservices, bridging cloud and edge development.

[Explore Cloud-Native](https://developer.nvidia.com/embedded/jetson-cloud-native)[Explore NGC Containers](https://catalog.ngc.nvidia.com/containers?filters=&amp;orderBy=weightPopularDESC&amp;query=&amp;page=&amp;pageSize=)

#### Nsight Developer Tools

NVIDIA Nsight™ developer tools provide powerful profiling, debugging, and performance analysis for optimizing GPU-accelerated applications across AI, graphics, and compute workloads.

[Explore Nsight Developer Tool](/nsight-systems)

### Supported SDKs

#### NVIDIA DeepStream SDK  

This SDK gives you a powerful toolkit for building AI-powered vision applications, enabling real-time video analytics with accelerated inference and object tracking.

[Explore DeepStream SDK](/deepstream-sdk)

#### NVIDIA Isaac ROS

NVIDIA Isaac ROS is a collection of hardware-accelerated ROS 2 packages for NVIDIA Jetson. It’s ideal for high-performance perception, localization, and AI in robotics applications.

[Explore Isaac ROS](/isaac/ros)

#### NVIDIA Holoscan SDK

NVIDIA Holoscan SDK is a streaming AI framework for building real-time sensor-processing applications at the edge. It enables high-performance pipelines for healthcare, robotics, and industrial use cases.

[Explore Holoscan SDK](/holoscan-sdk)

### Community Support

#### Jetson AI Lab

Jetson AI Lab is an interactive platform for learning and experimenting with AI on NVIDIA Jetson, offering hands-on projects, tutorials, and tools tailored for edge AI development.

[Explore Jetson AI Lab](https://www.jetson-ai-lab.com/)

#### Developer Forums

NVIDIA Developer Forums are a community hub for developers to ask questions, share knowledge, and get support on NVIDIA technologies, platforms, and SDKs..

[Explorer Developer Forums](https://forums.developer.nvidia.com/c/robotics-edge-computing/jetson-embedded-systems/70)

* * *

## Ethical AI 

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   
  
For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety &amp; Security, and Privacy Subcards. Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Get started with JetPack today.

[Download JetPack](/embedded/jetpack/downloads)


