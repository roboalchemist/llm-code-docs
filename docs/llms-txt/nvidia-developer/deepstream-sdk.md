# Source: https://developer.nvidia.com/deepstream-sdk.md

1. [Home](/)

[Deep Learning](https://developer.nvidia.com/deep-learning)

[Deep Learning Software](https://developer.nvidia.com/deep-learning-software)

DeepStream SDK

Quick Links

- [Get Started](/deepstream-sdk)
- [Download DeepStream](https://catalog.ngc.nvidia.com/orgs/nvidia/collections/deepstream_sdk)

* * *

# NVIDIA DeepStream SDK

NVIDIA DeepStream’s multi-platform support gives you a faster, easier way to develop and deploy real-time video streaming pipelines for generative AI agents and applications. You can even deploy them on premises, at the edge, and in the cloud with just the click of a button.

[Get Started](https://developer.nvidia.com/deepstream-getting-started &quot;Get Started&quot;)[Download DeepStream](https://catalog.ngc.nvidia.com/orgs/nvidia/collections/deepstream_sdk &quot;Download DeepStream&quot;)

* * *

## What is NVIDIA DeepStream?

The NVIDIA DeepStream SDK is a comprehensive real-time streaming analytics toolkit based on GStreamer for AI-based multi-sensor processing, video, audio, and image understanding. It’s ideal for developers, software partners, startups, and OEMs building vision AI agents and applications and services for a wide range of industries like smart cities, retail, manufacturing, and more.  
  
You can now create and deploy stream-processing pipelines that incorporate generative AI and other complex processing tasks like multi-camera tracking in minutes. To further accelerate development, DeepStream is also part of the [NVIDIA Metropolis Blueprint for Video Search and Summarization (VSS)](https://build.nvidia.com/nvidia/video-search-and-summarization/nim). This sample architecture for building visual AI agents can extract valuable insights from massive volumes of industrial video sensor data in real time.  
  
DeepStream is an integral part of [NVIDIA Metropolis](https://www.nvidia.com/en-us/autonomous-machines/intelligent-video-analytics-platform/), the platform for building end-to-end vision AI agents and applications that transform pixel and sensor data into actionable insights.

![What is DeepStream and how does the software stack look like](https://developer.download.nvidia.com/images/deepstream/metropolis-deepstream-vision-ai-edge.jpg)
_DeepStream is an integral part of NVIDIA Metropolis, the platform for building end-to-end services and solutions that transform pixel and sensor data to actionable insights._

* * *

## Benefits  

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/deepstream/m48-configuration-sdk-256px-blk.png)
### Rapidly Deploy AI From the Cloud to the Edge

The DeepStream SDK provides a complete video stream processing, ingestion, multi-camera, tracking pipeline that’s 100% NVIDIA GPU-accelerated. It’s ideal for a wide range of use cases across industries such as manufacturing, logistics, retail, and more.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/deepstream/m48-microservices-2-256x-blk.png)
### Reduce Development Time to Minutes 

DeepStream Inference Builder simplifies the development process with declarative application definitions and easy addition of API endpoints for your application.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/deepstream/m48-speed-256px-blk.png)
### Real-Time Insights

Extract rich metadata in real time from sensor data such as images, video, and lidar.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/deepstream/m48-edge-computing-256px-blk.png)
### Achieve the Lowest Total Cost of Ownership With NVIDIA GPUs

Increase stream density, maximize performance, and minimize TCO by deploying AI models with DeepStream on NVIDIA hardware.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/deepstream/m48-complexity-1-256px-blk.png)
### Multiple Programming Options

Create powerful vision AI applications using C/C++ and Python.

* * *

## Unique Capabilities  

# Accelerate Vision AI Development With 40+ GPU-Accelerated Plug-Ins

DeepStream kickstarts the development of seamless real-time streaming pipelines for AI-based video, audio, and image analytics. It ships with 40+ hardware-accelerated plug-ins and 30+ sample applications and extensions to optimize pre/post processing, inference, multi-camera tracking, message brokers, and more.   
  
**Inference Builder** turns AI model ideas into production-ready services with ease. Developers can now go from YAML config to deployment in minutes—automating data flow, preprocessing, model execution, and API integration.  
  
**DeepStream Service Maker** simplifies the development process by abstracting the complexities of GStreamer to easily build C++ object-oriented applications. Use Service Maker to build complete DeepStream pipelines with a few lines of code  
  
**DeepStream Libraries**  powered by NVIDIA® CV-CUDA™, NvImageCodec, and PyNvVideoCodec offer low-level GPU-accelerated operations to optimize pre- and post- stages of vision AI pipelines.

[Learn More](https://github.com/NVIDIA-AI-IOT/inference_builder)

[![A diagram showing how DeepStream inference builder works to accelerate vision AI.](https://developer.download.nvidia.com/images/deepstream/deepstream-diagram-ari.jpg)](https://developer.download.nvidia.com/images/deepstream/deepstream-diagram-ari.jpg)

_Click to Enlarge_

#### Enable Multi-Camera Tracking Across   
a Range of Cameras

Multiview 3D tracking (MV3DT), an extension of DeepStream NvTracker, enables distributed, real-time 3D tracking across networks of cameras. It works seamlessly with both 2D and 3D detectors, supporting a wide range of use cases. DeepStream automatically assigns unique IDs for new objects, preserving identity through occlusions and handovers.   
  
For precise multi-camera tracking, DeepStream includes a new calibration tool that aligns multiple cameras to the deployment floor plan simultaneously. This reduces manual effort and ensures consistent, accurate results.

[Learn More](https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_MV3DT.html)

# Build End-to-End AI Solutions  

Speed up overall development efforts and unlock greater real-time performance by building end-to-end vision AI applications with NVIDIA Metropolis. Start with production-quality vision AI models, adapt and optimize them with the NVIDIA TAO Toolkit, and deploy using DeepStream. Use the Metropolis VSS Blueprint to build visual AI agents that can process thousands of live videos simultaneously to drive insights and automation.   
  
Get incredible flexibility—from rapid prototyping to full production-level solutions—and choose your inference path. With native integration to NVIDIA [Triton™ Inference Server](/nvidia-triton-inference-server), you can deploy models in native frameworks such as PyTorch and TensorFlow for inference. For high-throughput inference, use NVIDIA TensorRT to achieve the best possible performance.

[Learn More](https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_TAO_integration.html)

[![DeepStream helps developers build seamless streaming pipeline for AI based video analytics](https://developer.download.nvidia.com/images/deepstream/end-to-end-vision-ai-development-ari.jpg)](https://developer.download.nvidia.com/images/deepstream/end-to-end-vision-ai-development-ari.jpg)
_Click to Expand_

[![DeepStream helps developers build seamless streaming pipeline for AI based video analytics](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/deepstream/embedded-deepstream-sdk3.jpg)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/deepstream/embedded-deepstream-sdk3.jpg)
_Click to Expand_

#### Enjoy Seamless Development From Edge to Cloud

DeepStream’s off-the-shelf containers let you build once and deploy anywhere—on clouds, workstations with NVIDIA GPUs, or NVIDIA Jetson™ devices. With the DeepStream Container Builder and NGC containers, you can easily create scalable, high-performance AI applications managed with Kubernetes and Helm.  
  
DeepStream REST-APIs also let you manage multiple parameters at run-time, simplifying the creation of SaaS solutions. With a standard REST-API interface, you can build web portals for control and configuration or integrate into your existing applications.

[Learn More](https://docs.nvidia.com/metropolis/deepstream/dev-guide/)

# Get Production-Ready

DeepStream is available as a part of NVIDIA AI Enterprise, an end-to-end, secure, cloud-native AI software platform optimized to accelerate enterprises to the leading edge of AI.  
NVIDIA AI Enterprise delivers validation and integration for NVIDIA AI open-source software, access to AI solution workflows to speed time to production, certifications to deploy AI everywhere, and enterprise-grade support, security, and API stability to mitigate the potential risks of open-source software.

[Learn More](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/)

![A collage of images showing DeepStream as a part of NVIDIA AI Enterprise to help deploy AI anywhere](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/nvidia-ai-enterprise-630x354_1.jpg)

* * *

## Explore Multiple Programming Options

### Inference Builder

Streamline the entire workflow with a simple YAML configuration—automating data flow, preprocessing, model execution, and API integration.

[Learn More About Inference Builder](https://github.com/NVIDIA-AI-IOT/inference_builder)

### Python

Construct DeepStream pipelines using Gst Python, the GStreamer framework&#39;s Python bindings. The source code for the binding and Python sample applications are available on GitHub.

[Learn More About Python](https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_service_maker_python.html)

### C/C++

Create applications in C/C++, interact directly with GStreamer and DeepStream plug-ins, and use reference applications and templates.

[Learn More About C/C++](https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_C_Sample_Apps.html)

* * *

## Improve Accuracy and Real-Time Performance  

DeepStream offers exceptional throughput for a wide variety of object detection, image processing, and instance segmentation AI models. The following table shows the end-to-end application performance from data ingestion, decoding, and image processing to inference. It takes multiple 1080p/30fps streams as input. Note that running on the DLAs for Jetson devices frees up the GPU for other tasks. For performance best practices, [watch this video tutorial](https://www.youtube.com/watch?v=Or8vfydL69s&amp;feature=youtu.be).

| Foundation Model | Tracker | Precision | Jetson Thor | L40S | A6000 | B200 | RTX PRO WS | RTX PRO SE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-RADIO-Base | No Tracker | FP16 | 1242 | 2880 | 2568 | 8352 | 3025 | 3864 |
| NV-DinoV2-Large | No Tracker | FP16 | 412 | 797 | 616 | 3552 | 895 | 1330 |
| RT-DETR + C-RADIO-Base | No Tracker | FP16 | 194 | 609 | 546 | 1888 | 630 | 920 |
| RT-DETR + C-RADIO-Base | NvDCF | FP16 | 161 | 618 | 534 | 1824 | 627 | 848 |
| RT-DETR + C-RADIO-Base | MV3DT | FP16 | 183 | 343 | 497 | 1128 | 598 | 624 |
| TrafficCamNet Transformer Lite | NvDCF | FP16 | 157 | 685 | 584 | 1200 | 785 | 928 |
| Peoplenet (2.6.3) | MV3DT | FP16 | 617 | 486 | 552 | 4320 | 860 | 852 |
| Grounding-DINO | No Tracker | FP16 | 24 | 98 | 101 | 208 | 132 | 158 |
| SegFormer + C-RADIO-Base | No Tracker | FP16 | 135 | 870 | 884 | 1508 | 157 | 1060 |
| Mask2Former + SWIN | No Tracker | FP16 | 26 | 94 | 63 | 173 | 68 | 102 |

  
The DeepStream SDK lets you apply AI to streaming video and simultaneously optimize video decode/encode, image scaling, and conversion and edge-to-cloud connectivity for complete end-to-end performance optimization.  
  
To learn more about the performance using DeepStream, check the [documentation](https://www.google.com/url?q=https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Performance.html&amp;sa=D&amp;source=docs&amp;ust=1715369000151037&amp;usg=AOvVaw0yBjmmdaH_95_HgwtP21jm).

* * *

## Read Customer Stories  

 ![Industry.AI Customer Story](https://developer.download.nvidia.com/images/deepstream/bengaluru-airport-ai-ari.jpg)

### Optimizing Operations at Bengaluru Airport  

Industry.AI used the NVIDIA Metropolis stack, including DeepStream, to increase the safety and efficiency of the airport. Using vision AI, it was able to track abandoned baggage, flag long passenger queues, and alert security teams of potential issues.

[Read the Blog](https://blogs.nvidia.com/blog/bengaluru-airport-vision-ai/)

 ![KoiReader Customer Story](https://developer.download.nvidia.com/images/deepstream/koireader-distribution-center-operation-ari.jpg)

### Enhancing Distribution Center Operation 

KoiReader developed an AI-powered machine vision solution using NVIDIA developer tools that included the DeepStream SDK to help PepsiCo achieve precision and efficiency in dynamic distribution environments.

[Learn More About KoiReader](https://blogs.nvidia.com/blog/pepsi-koivision/)

 ![YMA Customer Story Please take the image from the video](https://developer.download.nvidia.com/images/deepstream/ai-smart-spaces-ari.jpg)

### Scaling AI-Powered Smart Spaces

FYMA used NVIDIA DeepStream and NVIDIA Triton™ to improve AI-powered space analytics with frame rates exceeding previous benchmarks by 10x and accuracy by 3x.

[Learn More](https://www.youtube.com/watch?v=GPsQAKq02lc)

* * *

## General FAQ

DeepStream is a closed-source SDK. Note that sources for all reference applications and several plugins are available. DeepStream Inference Builder will be open -source and available on [GitHub](https://github.com/NVIDIA-AI-IOT/inference_builder).

The DeepStream SDK can be used to build end-to-end AI-powered applications to analyze video and sensor data. Some popular use cases are retail analytics, parking management, managing logistics, optical inspection, robotics, and sports analytics.

See the [Platforms and OS compatibility table](https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Quickstart.html#platform-and-os-compatibility).

Yes, that’s now possible with the integration of the Triton Inference server. Also with DeepStream 6.1.1, applications can communicate with independent/remote instances of Triton Inference Server using gPRC.

DeepStream supports several popular models out of the box. For instance, DeepStream supports all NVIDIA TAO models and ships with an example to run YOLO models.

Yes, DeepStream 8.0 or later supports NVIDIA Blackwell architecture.

Yes, audio is supported with DeepStream SDK. To get started, download the software and review the reference audio and Automatic Speech Recognition (ASR) applications. Learn more by reading the [ASR DeepStream Plugin](https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_plugin_gst-nvdsasr.html)

Build high-performance vision AI apps and services using the DeepStream SDK.

[Get Started](/deepstream-getting-started &quot;Get Started with DeepStream SDK&quot;)


