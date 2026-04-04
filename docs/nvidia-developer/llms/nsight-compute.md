# Source: https://developer.nvidia.com/nsight-compute.md

  ![Nsight Compute](https://developer.download.nvidia.com/images/nvidia-nsight-compute-icon-gbp-shaded-128.png &quot;Nsight Compute&quot;) 
# NVIDIA Nsight Compute

NVIDIA Nsight™ Compute is an interactive profiler for CUDA® and NVIDIA OptiX™ that provides detailed performance metrics and API debugging via a user interface and command-line tool. Users can run guided analysis and compare results with a customizable and data-driven user interface, as well as post-process and analyze results in their own workflows.

[Get started](/tools-overview/nsight-compute/get-started)

NVIDIA Nsight Compute is also available as part of the [CUDA Toolkit](/cuda-toolkit).

  

https://www.youtube-nocookie.com/embed/04dJ-aePYpE
  

Watch an overview video about how guided analysis in Nsight Compute assists CUDA kernel optimizations.   
 Highlighting GPU throughput, warp state statistics, and source code correlation.

  

#### Profile CUDA and OptiX

For developing with CUDA or OptiX, application-level performance tuning is just the beginning of GPU optimization. When a deeper dive into compute processes is needed, it&#39;s crucial to have both visibility to hardware activity and the level of understanding required to optimize it. With NVIDIA Nsight Compute, you don’t have to be a hardware architecture expert to do this; Nsight Compute is a CUDA and OptiX profiler that detects performance issues, displays them intuitively, and delivers built-in guidance from NVIDIA engineers on how to resolve them.

#### Leverage NVIDIA’s Insight

Nsight Compute is designed to assist the hefty task of kernel profiling with a powerful set of tools bundled with NVIDIA’s own insights. By visualizing hardware performance metrics, it translates traditionally cryptic values into actionable information. The level of detail that Nsight Compute uncovers is ordered hierarchically, such that memory utilization can be correlated down to individual lines of source code. Built into every step of the process, guided analysis from NVIDIA’s own rule set identifies common performance limiters and offers valuable optimization advice.

#### Customize and Collaborate

For expert users, Nsight Compute can be extended with custom metric collection and analysis workflows. For cross-platform development, baseline comparisons reveal performance variations between different GPU architectures. For collaboration, dependencies and source information can be imported into the report and shared with colleagues and teams. Profiling can be conducted through the Nsight Compute GUI, or through the CLI; on the local device, or remotely. Python developers can leverage the NVRules API for automating analysis. Nsight Compute’s options for different development areas, experience levels, and project sizes are expansive.

* * *

## Explore Key Features

### Find Optimizations With Guided Analysis

Nsight Compute’s report pages provide insight into all aspects of a profile. The details page offers metrics that address overall GPU utilization, how performance is connected to various hardware concepts, and concludes with recommended optimization actions. Insights into performance problems and solutions from NVIDIA’s best practices are provided along the way via guided analysis. Baseline comparisons enable efficient feedback directly in the tool to understand the effects of any changes to the workload.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/nsight/nsight-compute-optimizations-guided-analysis-630x354.jpg)
_The details page raises flags on low GPU throughput and automatically detects performance limiters that are the potential source._

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/nsight/nsight-compute-inspect-memory-workload-630x354.jpg)
_Memory chart visualizing data transfer, where pipelines are colored with a heatmap based on their utilization._

### Inspect Memory Workload 

Memory workload analysis builds a visualization of memory transfer sizes and throughput on the profiled architecture, as well as a guide for improving performance. Heatmaps allow users to intuitively understand potential bottlenecks and under-utilizations in the memory pipeline. Detailed tables for each hardware unit enable insight into the path from originating instruction to executed memory access.

  
[Learn more about memory workload analysis](https://www.youtube.com/watch?v=DnwZ6ZTLw50&amp;t=138s)

### Correlate Source Code With Detailed Instruction Metrics

Nsight Compute supports correlating efficiency metrics down to the individual lines of code that contribute to them. This includes connecting assembly (SASS) with PTX and higher-level code, such as CUDA C/C++, Fortran, OpenACC or python. A heat-map visualization highlights areas with high metric values to quickly locate problematic areas. Warp stall sampling identifies latency and inefficiency issues while instruction execution metrics indicate expensive code locations. Such detail empowers the scrutinous eye to tune performance at a precise degree.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/nsight/nsight-compute-correlate-source-code-630x354.jpg)
_Metrics corresponding to individual lines of code being profiled in the source page._

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/nsight/nsight-compute-utilize-cuda-graphs-interactive-profiling-630x354.jpg)
_A CUDA graph visualizing how nodes are configured and connected._

### Utilize CUDA Graphs and Interactive Profiling

Interactive profiling creates a live session where application state can be viewed dynamically and full control of the target is preserved. This allows you to step API calls, inspect resources, or experiment with different kernel configurations to readily make performance comparisons. Explore and export CUDA graphs to understand how they are connected and profile individual nodes or the entire graph with detailed hardware metrics.

### Uplift OptiX Development

Nsight Compute is part of the NVIDIA Nsight Developer Tools suite, a collection of powerful tools, libraries, and SDKs that enable developers to build, debug, and profile software utilizing the latest accelerated computing hardware.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/nsight/nsight-compute-uplift-optix-api-development-630x354.jpg)
_Acceleration structure viewer where with a hierarchical view on the left, a graphical view in the middle, and control options on the right._

## View Other Tools Within the Nsight Suite

Nsight Compute is part of the NVIDIA Nsight Developer Tools suite; a collection of powerful tools, libraries, and SDKs that enable developers to build, debug, and profile software utilizing the latest accelerated computing hardware.

 ![](https://developer.download.nvidia.com/images/nvidia-nsight-graphics-icon-gbp-shaded-128.png)

### Nsight Graphics

NVIDIA Nsight™ Graphics is a standalone developer tool with ray-tracing support that enables you to debug, profile, and export frames built with Direct3D, Vulkan, OpenGL, OpenVR, and the Oculus SDK.

[Get Started](/nsight-graphics)

 ![](https://developer.download.nvidia.com/images/nsight-deep-learning-designer-96x96.png)

### Nsight Deep Learning Designer

NVIDIA Nsight DL Designer is an integrated development environment that helps developers efficiently design and develop deep neural networks for in-app inference.

[Get Started](/nsight-dl-designer)

 ![](https://developer.download.nvidia.com/images/nvidia-nsight-systems-icon-gbp-shaded-256.png)

### Nsight Systems

NVIDIA Nsight Systems is a system-wide performance analysis tool designed to visualize an application’s algorithms, help identify the largest opportunities to optimize, and tune to scale efficiently across any quantity or size of CPUs and GPUs.

[Get Started](/nsight-systems)

  

[Learn more about Nsight Tools](/tools-overview)  [Browse Tutorials](/tools-tutorials)

## Watch Nsight Developer Tools CUDA Tutorials

CUDA Developer Tools is a series of tutorial videos designed to get you started with using Nsight tools for CUDA development. It explores key features for CUDA profiling, debugging, and optimizing.

https://www.youtube-nocookie.com/embed/xdFQZSV5IrU?si=2J4RJszw7vyB9Jq4

### CUDA Developer Tools | NVIDIA Nsight Tools Ecosystem

https://www.youtube-nocookie.com/embed/dUDGO66IadU?si=1B88gFifsJk2CTAG

### CUDA Developer Tools | Intro to NVIDIA Nsight Systems

https://www.youtube-nocookie.com/embed/Iuy_RAvguBM?si=9bTGg4ZvXeBdhjSv
### CUDA Developer Tools | Intro to NVIDIA Nsight Compute

[CUDA Developer Tools Tutorials Playlist](https://www.youtube.com/playlist?list=PL5B692fm6--ukF8S7ul5NmceZhXLRv_lR)

* * *

## Watch Nsight Compute Sessions and Technical Videos on Demand

## Stay up to Date on the Latest NVIDIA Nsight Compute News
  

## Find More Resources

[![Developer Forums](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/forums-icon-48x48_1.svg)](https://forums.developer.nvidia.com/c/development-tools/nsight-compute/114)
### [Explore Nsight Forums](https://forums.developer.nvidia.com/c/development-tools/nsight-compute/114)

[![RTXDI Technical Blog](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/documentation-icon-48x48_1.svg)](https://docs.nvidia.com/nsight-compute/index.html)
### [Read Nsight Compute Documentation](https://docs.nvidia.com/nsight-compute/index.html)

[![ RTXDI Sessions on NVIDIA On-Demand](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/m48-digital-deep-learning-institute-talks-training-256px-grn.png)](http://developer.nvidia.com/tools-tutorials)
### [Browse Nsight Tools Tutorials](/tools-tutorials)

[![ NVIDIA Developer Program](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/m48-people-group-256px-grn.png)](https://developer.nvidia.com/developer-program)
### [Join the NVIDIA Developer Program](https://developer.nvidia.com/developer-program)

Ready to get started with NVIDIA Nsight Compute?

[Download Now](/tools-overview/nsight-compute/get-started)  


