# Source: https://developer.nvidia.com/nsight-graphics.md

1. [Home](/)
[Developer Tools ](https://developer.nvidia.com/tools-overview)[Nsight Graphics](https://developer.nvidia.com/nsight-graphics)

 ![Nsight Compute](https://developer.download.nvidia.com/images/nvidia-nsight-graphics-icon-gbp-shaded-128.png)

# NVIDIA Nsight Graphics  

NVIDIA Nsight™ Graphics is a standalone developer tool with ray-tracing support that enables you to debug, profile, and export frames built with Direct3D, Vulkan, OpenGL, OpenVR, and the Oculus SDK.

[Download for Windows  ](https://developer.nvidia.com/downloads/assets/tools/secure/nsight-graphics/2025_5_0/windows/NVIDIA_Nsight_Graphics_2025.5.0.25335.msi)     |       [Download for Linux (.run)  ](https://developer.nvidia.com/downloads/assets/tools/secure/nsight-graphics/2025_5_0/linux/NVIDIA_Nsight_Graphics_2025.5.0.25335.run)     |       [Download for Linux (.deb)  ](https://developer.nvidia.com/downloads/assets/tools/secure/nsight-graphics/2025_5_0/linux/NVIDIA_Nsight_Graphics_2025.5.0.25335.deb)

[Get started](https://developer.nvidia.com/nsight-graphics/get-started)

https://www.youtube-nocookie.com/embed/LKR5XIW1lgs?

 

Learn how Nsight Graphics can be used to accelerate development and help make high-performance games with beautiful graphics. 

### Optimize Performance  

Graphics optimization and hardware utilization shouldn’t be ambiguous. Nsight Graphics offers an unparalleled level of access into the performance markers of your graphics API—an invaluable aid in finding optimization opportunities that couldn’t be identified without looking under the GPU’s hood. 

### Debug Graphics  

Nsight Graphics enables smooth graphics development on NVIDIA platforms. Identify bugs and trace them back to their source on the target application, including real-time shader debugging. At its most granular, Nsight Graphics lets developers inspect every individual event involved in generating a frame—down to the pixel.

### Boost Ray Tracing  

The Ray Tracing Inspector in Nsight Graphics enables the next generation of real-time rendering technology. Analyze ray tracing efficiency, improve acceleration structures, optimize axis-aligned bounding boxes (AABBs), build flags, and overlaps. The entire frame can be thoroughly examined to ensure the best image fidelity and frame performance.

* * *

## Explore Key Features

### Track GPU Performance  

Analyze GPU throughput and utilization with minimal overhead for non-biased activity data. On the captured timeline, drill down into critical performance markers and inspect hardware unit throughputs, cache hit rates, memory throughput, and more. 

 ![GPU Trace shows a full timeline of application workload](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/track-gpu-performance-630x354.jpg)

_GPU Trace showing a full timeline of application workload._

 ![GPU Trace analysis identifies performance blockers automatically](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/analyze-gpu-traces-630x354.jpg)

_Trace analysis automatically identifying performance blockers._  

### Analyze GPU Traces  

Nsight Graphics supports automated performance analysis on captured GPU traces. Deep profiling of streaming multiprocessor (SM) performance is accomplished by automatically tracing the execution of shaders across a series of frames.

### Debug Ray-Tracing and Shaders  

Debug ray-tracing API calls and examine their state. The Ray Tracing Inspector exposes acceleration structures, helping you optimize how rays intersect with the geometry in your scene. You can also examine ray tracing efficiency to ensure ray-traversal speeds are high.

Debug shader code with the Vulkan Shader Debugger, which exposes shader source in your render pipeline in real-time so you can quickly make fixes directly to the  code.

 ![Ray Tracing Inspector analyzes ray tracing efficiency and reveals acceleration structures](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/debug-pipelines-630x354.jpg)

_The Ray Tracing Inspector analyzes ray tracing efficiency and reveals acceleration structures._  

 ![Ray Tracing Shader timing heatmap makes a stalling shader issue clear with a red hotspot](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/profile-shaders-630x354.jpg)

_Shader timing heatmap makes a stalling shader issue clear with a red hotspot._  

### Profile Ray-Tracing Shaders  

The Nsight Graphics Shader Profiler exposes shader data, including stalls and the reasons they occurred. The Real-Time Shader Profiler allows you to view the most expensive shaders at each moment in real-time. And the shader timing heatmap visualizes hotspots overlaid on the scene where shader times lagged per pixel.  
  
Profiling ray-tracing shaders can be an arduous task that requires extensive knowledge of the GPU. These features turn ray-tracing profiling into a streamlined and intuitive process.

### Export C++ Capture  

Create a self-contained C++ project that allows for frame analysis in a reduced CPU-load scenario. This lets you perform repeatable and isolated analysis without being bound to the original application and provides a protected environment for experimenting with optimization tweaks.

 ![A C++ project that allows for frame analysis of Hellblade: Senua&#39;s Sacrifice game in a reduced CPU-load scenario](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/export-c-capture-630x354.jpg)

_Images of Hellblade: Senua&#39;s Sacrifice courtesy of[ Ninja Theory Ltd](http://www.ninjatheory.com/); Hellblade is a Direct3D 12 / DXR game based on Unreal Engine 4._  

* * *

## View Other Tools Within the Nsight Suite  

Nsight Graphics is part of the NVIDIA Nsight Developer Tools suite; a collection of powerful tools, libraries, and SDKs that enable developers to build, debug, and profile software utilizing the latest accelerated computing hardware.

 ![img-alt-text](https://developer.download.nvidia.com/images/nvidia-nsight-aftermath-icon.png)

### Nsight Aftermath SDK  

Nsight Aftermath SDK is a library that integrates into a D3D12 or Vulkan game’s crash reporter to generate GPU “mini-dumps” when an exception or TDR occurs, exposing pipeline information to resolve an unexpected crash.

[Get Started](https://developer.nvidia.com/nsight-aftermath)

 ![img-alt-text](https://developer.download.nvidia.com/images/nvidia-nsight-systems-icon-gbp-shaded-256.png)

### Nsight Systems  

NVIDIA Nsight Systems is a system-wide performance analysis tool designed to visualize an application’s algorithms, help you identify the largest opportunities to optimize, and tune to scale efficiently across any quantity or size of CPUs and GPUs.

[Get Started](https://developer.nvidia.com/nsight-systems)

### Nsight Perf SDK  

NVIDIA Nsight Pef SDK is a graphics profiling toolbox that enables you to collect GPU performance metrics directly from your application. Leverage the built-in HUD renderer for real-time, high-level performance triage.

[Get Started](https://developer.nvidia.com/nsight-perf-sdk)

[Learn More About Nsight Tools](https://developer.nvidia.com/tools-overview)[Browse Tutorials](http://developer.nvidia.com/nsight-developer-tools)

* * *

## Check out partner testimonials and ecosystem  

&gt; Dassault Systèmes and its SOLIDWORKS brand have always supported bleeding-edge rendering technologies from NVIDIA. Nsight Graphics is one of our go-to graphics debugging tools. With valuable features like C++ Capture and Pixel History, Nsight Graphics has enabled us to solve complex rendering problems with ease.
&gt; 
&gt; —Siddharth Palaniappan, SOLIDWORKS Graphics R&amp;D Development Senior Manager, Dassault Systèmes
&gt; 
&gt; ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-dassault-systems.svg)

&gt; Vulkan is the cornerstone of Adobe’s multi-platform, multi-vendor rendering strategy for its Adobe Substance 3D products. Thanks to the ray-tracing extensions that NVIDIA pioneered and contributed to Khronos, Vulkan gives native access to ray-tracing hardware, offering exceptional ray-tracing performance on supported devices. In addition, Nsight Graphics and Nsight Systems are invaluable tools when it comes to understanding and improving the performance of Vulkan ray-tracing applications.
&gt; 
&gt; — Francois Beaune, Lead Software Engineer of Photorealistic Rendering, Adobe 3D and Immersive
&gt; 
&gt; ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-adobe.svg)

&gt; Nsight Graphics provides a huge productivity boost for our team, because it helps us to efficiently debug shader logic, parameters, or textures. Nsight Graphics additionally is invaluable to gain insights into memory layout of geometry and textures. The team is always eager to support our development efforts with best practices and new features.
&gt; 
&gt; — Jan Ohlenburg, Director of Software Development, Maxon
&gt; 
&gt; ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-maxon.svg)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-adobe.svg)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-autodesk.svg)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-dassault-systems.svg)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-epic-games.svg)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-maxon.svg)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-ubi-soft.svg)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-popcorn-fx.svg)

* * *

## Watch Nsight Graphics Tutorial Series

Fundamental concepts in graphics development, and key tips for ensuring peak performed, are explored with Nsight Graphics.

https://www.youtube-nocookie.com/embed/HSsPJ4qK6AU?
 

How to Improve Shader Performance by Resolving LDC Divergence

https://www.youtube-nocookie.com/embed/f0a9mN4HQCI?
 

Avoiding Stalls and Hitches in DirectX 12

https://www.youtube-nocookie.com/embed/ctow9BO79nA?
 

Building Acceleration Structures Using Async Compute

* * *

## Watch Nsight Graphics sessions and technical videos on demand  

* * *

## Stay up to date on the latest Nsight Graphics news  

* * *

## Find more resources  

 ![img-alt-text](https://developer.download.nvidia.com/icons/m48-misc-question-faq.svg)

#### Explore Nsight Tools Forums  

 ![img-alt-text](https://developer.download.nvidia.com/icons/m48-document-support-guide-2.svg)

#### Read Nsight Graphics Documentation  

 ![img-alt-text](https://developer.download.nvidia.com/icons/m48-live-talk-on-demand.svg)

#### Browse Nsight Tools Tutorials  

 ![img-alt-text](https://developer.download.nvidia.com/icons/m48-people-group.svg)

#### Join the NVIDIA Developer Program  

 

Ready to get started with NVIDIA Nsight Graphics?

[Download Now](https://developer.nvidia.com/nsight-graphics/get-started)

Quick Links

- [Download for Windows  
  
  
  
  
](https://developer.nvidia.com/downloads/assets/tools/secure/nsight-graphics/2025_5_0/windows/NVIDIA_Nsight_Graphics_2025.5.0.25335.msi)
- [Download for Linux (.run)  
](https://developer.nvidia.com/downloads/assets/tools/secure/nsight-graphics/2025_5_0/linux/NVIDIA_Nsight_Graphics_2025.5.0.25335.run)
- [Download for Linux (.deb)  
](https://developer.nvidia.com/downloads/assets/tools/secure/nsight-graphics/2025_5_0/linux/NVIDIA_Nsight_Graphics_2025.5.0.25335.deb)

* * *


