# Source: https://developer.nvidia.com/nsight-perf-sdk.md

# NVIDIA Nsight Perf SDK

The NVIDIA® Nsight™ Perf SDK is a graphics profiling toolbox for DirectX, Vulkan, and OpenGL enabling you to collect GPU performance metrics directly from your application.

  
  
[Get Started](/nsight-perf-sdk/get-started)

[![NVIDIA Nsight® Perf SDK](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/Nsight_Perf_ProductPage_Hero_Updated.jpg)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/Nsight_Perf_ProductPage_Hero_Updated.jpg)
_Just a few lines of code are needed to set up GPU performance metrics collection with the Nsight Perf SDK._

[![Realtime Perf Triage](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/box-thumbnail.png) ](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/box-full-size-screenshot.png)(click image to expand)

## Realtime Perf Triage

Enable high-level performance triage via realtime collection and on-screen visualization of GPU performance metrics. The new GPU Periodic Sampler collects device-level metrics at high sampling rates with low overhead.

[![Profile In-Application](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/Profile_InAPP_Thumbnail.jpg)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/PixNSightPerfSDK.png)(click image to expand)
_Microsoft’s PIX on Windows showing
                        NVIDIA GPU performance metrics_

## Profile In-Application

Integrate GPU performance metric collection into your application or graphics developer tool of choice. Activate profiling from your own custom programmatic triggers. Choose the list of GPU metrics to collect, customize your output, and keep control over your workflow.

 ![CI/CD](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/CICD_Final.jpg)

## Upgrade Your CI/CD

Generate detailed profiler reports on every developer and artist change. Add dedicated perf regression criteria by inspecting GPU metric values.

* * *
  

## Realtime Performance HUD

[![Realtime Performance HUD](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/paragraph-thumbnail%5B16%5D.png)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/paragraph-full-size-screenshot.png)(click image to expand)

Add continuous performance metrics collection to your code, and leverage the built-in HUD renderer to effortlessly enable real-time, high-level performance triage.   
  
 Explore panels with metrics on SM, L2 cache, ROP, VRAM and various other subunits to gain an early understanding of the performance characteristics and potential bottlenecks of the scene as you move through it.   
  
 The HUD- and Periodic Sampler-utility classes also serve as an example for creating your own powerful, low-overhead, real-time workflows on top of the low-level Nsight Perf SDK API.

  

  
https://www.youtube-nocookie.com/embed/0gpoWXpOadA

* * *

## Timeline Viewer

Examine a snapshot of your application’s performance with the Nsight Perf SDK one-shot sampling mode.   
  
 This allows you to examine hardware activity with minimal overhead. Nsight Perf SDK’s high-frequency sampling collects key GPU metrics in sharp detail. You can visualize unit throughputs, warp occupancy, draw calls, and more on the new Timeline Viewer.

 ![]()[![Timeline Viewer](https://developer.download.nvidia.com/images/TimelineView_353.png)](https://developer.download.nvidia.com/images/TimelineView.png)(click image to expand)

  
https://www.youtube-nocookie.com/embed/HHjTvFbfZy0?si=BUjykJlZe7T8_dQU

* * *

## HTML Profiler Report Generator

[![Be One with the GPU](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/HTML_Profiler_Image_630.jpg)](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/NsightPerfSDK_HTML_report_v2.png)(click image to expand)

Generate detailed profiler reports with minimal effort. Simply insert a few calls at Graphics API Device Initialization, Present/SwapBuffers, a Keypress handler, or an automated trigger.   
  
 Insert annotations (PushRange/PopRange) around GPU workloads to collect additional reports per region of execution. The report generator automatically collects 100s of GPU metrics of interest; there is no need to study these complex topics on first usage.   
   
 The reports provide a top-down representation of GPU performance, with fast navigation to the top performance limiters. Quickly determine the workload type, pipeline activity and utilization, shader latency reasons, and 3D data flow.

## View Other Tools Within the Nsight Suite

Nsight Perf SDK is part of the NVIDIA Nsight Developer Tools suite—a collection of powerful tools, libraries, and SDKs that enable developers to build, debug, and profile software utilizing the latest accelerated computing hardware.

  

  
 ![](https://developer.download.nvidia.com/images/nvidia-nsight-graphics-icon-gbp-shaded-128.png)

### Nsight Graphics

NVIDIA Nsight Graphics is a standalone developer tool with ray-tracing support that enables you to debug, profile, and export frames built with Direct3D, Vulkan, OpenGL, OpenVR, and the Oculus SDK.

[Get Started](/nsight-graphics)

  
 ![Nsight Aftermath SDK](https://developer.download.nvidia.com/images/nvidia-nsight-aftermath-icon.png)

### Nsight Aftermath SDK

Nsigh Aftermath SDK is a library that integrates into a D3D12 or Vulkan game’s crash reporter to generate GPU “mini-dumps” when an exception or TDR occurs, exposing pipeline information to resolve an unexpected crash.p\&gt;

  
[Get Started](https://developer.nvidia.com/nsight-aftermath)

  
 ![](https://developer.download.nvidia.com/images/nvidia-nsight-systems-icon-gbp-shaded-256.png)

### Nsight Systems

NVIDIA Nsight Systems is a system-wide performance analysis tool designed to visualize an application’s algorithms, help you identify the largest opportunities to optimize, and tune to scale efficiently across any quantity or size of CPUs and GPUs.

  
[Get Started](/nsight-systems)

  

[Learn More About Nsight Tools](https://developer.nvidia.com/tools-overview)   [Browse Tutorials](http://developer.nvidia.com/tools-tutorials)

## Partners and Industry Standards

[![DirectX](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/DirectX-NSP.jpg)](https://docs.microsoft.com/en-us/windows/win32/direct3d12/direct3d-12-graphics)

[![Microsoft](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/Microsoft-NSP.jpg)](https://aka.ms/pixonwindows)

[![Khronos](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/Khronos_Group_NSP.jpg)](https://www.khronos.org/)

[![Vulkan](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/Vulkan_NSP.jpg)](https://www.khronos.org/vulkan/)

[![OpenGL](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/gamedev/OpenGL_NSP.jpg)](https://www.khronos.org/opengl/)

* * *
  

## NVIDIA Nsight Tools News
  

  
**[View all Nsight news](https://developer.nvidia.com/blog/tag/nsight/)**

## Find More Resources

[![Developer Forums](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/forums-icon-48x48_1.svg)](https://forums.developer.nvidia.com/)
### [Explore Nsight Perf SDK Forums](https://forums.developer.nvidia.com/)

[![ RTXDI Sessions on NVIDIA On-Demand](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/m48-digital-deep-learning-institute-talks-training-256px-grn.png)](http://developer.nvidia.com/tools-tutorials)
### [Browse Nsight Tools Tutorials](http://developer.nvidia.com/tools-tutorials)

[![ NVIDIA Developer Program](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/m48-people-group-256px-grn.png)](https://developer.nvidia.com/developer-program)
### [Join the NVIDIA Developer Program](https://developer.nvidia.com/developer-program)

Ready to download NVIDIA Nsight® Perf SDK?

[Get Started](nsight-perf-sdk/get-started)  


