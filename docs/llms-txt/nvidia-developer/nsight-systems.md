# Source: https://developer.nvidia.com/nsight-systems.md

1. [Home](/)
[Developer Tools ](https://developer.nvidia.com/tools-overview)[Nsight Systems](https://developer.nvidia.com/nsight-systems)

 ![Nsight Compute](https://developer.download.nvidia.com/images/nvidia-nsight-systems-icon-gbp-shaded-256.png)

# NVIDIA Nsight Systems  

NVIDIA Nsight™ Systems is a system-wide performance analysis tool designed to visualize an application’s algorithms, identify the largest opportunities to optimize, and tune to scale efficiently across any quantity or size of CPUs and GPUs, from large servers to our smallest systems-on-a-chip (SoCs).

[Get Started](https://developer.nvidia.com/nsight-systems/get-started)

Nsight Systems 2025.6.1 is available now.

 ![Nsight Systems can make high-performance games with beautiful graphics](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/nsight-systems-850x480.jpg)
 

Nsight Systems visualizes system workload metrics on a timeline and provides tools that help developers detect, understand, and solve performance issues. 

### Profile the System  

The full picture of app optimization requires drilling deeply into hardware interactions to ensure maximum parallelism is achieved. Nsight Systems visualizes unbiased, system-wide activity data on a unified timeline, allowing application developers to investigate correlations, dependencies, activity, bottlenecks, and resource allocation to ensure hardware components are working harmoniously. 

### Analyze Performance  

Nsight Systems offers low-overheard performance analysis that visualizes otherwise hidden layers of events and metrics used for pursuing optimizations, including CPU parallelization and core utilization, GPU streaming-multiprocessor (SM) optimization, system workload and CUDA® libraries trace, network communications, OS interactions, and more.

### Scale Across Platforms  

Nsight Systems is the universal tool for developing applications on NVIDIA platforms, whether on-premises or in the cloud. Scale across a wide range of NVIDIA platforms, from [NVIDIA DGX™](https://www.nvidia.com/en-us/data-center/dgx-platform/) to [NVIDIA RTX™ workstations](https://www.nvidia.com/en-us/design-visualization/workstations/), including [NVIDIA DRIVE®](https://developer.nvidia.com/drive) for automotive and [NVIDIA Jetson™](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/) for edge AI and robotics. Nsight Systems provide valuable insights for optimizing AI, high-performance computing (HPC), pro-visualization and gaming applications. 

* * *

## Explore Key Features   

### Visualize CPU-GPU Interactions  

Nsight Systems latches on to a target application to expose GPU and CPU activity, events, annotations, throughput, and performance metrics in a chronological timeline. With low overhead, this data can be visualized accurately and in parallel for ease of understanding. GPU workloads are further correlated with in-application CPU events, allowing for performance blockers to be easily identified and remedied. 

 ![Nsight Systems can make high-performance games with beautiful graphics](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/visualize-cpu-gpu-interactions-630x354.jpg)

_CPU activity (top) in parallel to GPU graphics and compute activity (bottom)._  

 ![Nsight Systems tracks GPU activity](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/track-gpu-activity-630x354.jpg)

_The GPU Metrics section of the Nsight Systems timeline._  

### Track GPU Activity  

To further explore the GPU, toggling on GPU Metrics Sampling will plot low-level input/output (IO) activity such as PCIe throughput, [NVIDIA NVLink®](https://www.nvidia.com/en-us/data-center/nvlink/), and dynamic random-access memory (DRAM) activity. GPU Metrics Sampling also exposes SM utilization, Tensor Core activity, instruction throughput, and warp occupancy. Every workload and their CPU origin can be readily tracked to support performance tuning. 

### Trace GPU Workloads  

For compute tasks, Nsight Systems supports investigating the CUDA API and tracing CUDA libraries, including cuBLAS, cuDNN, and NVIDIA TensorRT™. For graphics computing, Nsight Systems supports profiling Vulkan, OpenGL, DirectX 11, DirectX 12, DXR, and NVIDIA OptiX™ APIs.  

 ![Nsight Systems traces GPU workloads](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/trace-gpu-workloads-630x354.jpg)

_Alt text: DX12 API calls as they happen chronologically in the timeline alongside render thread._  

https://www.youtube-nocookie.com/embed/XPXfeh80zDE?
 

_Scale AI Applications to the Data Center and Cloud with NVIDIA Nsight Systems GTC Demo Video_  

### Accelerate Multi-Node Performance  

Nsight Systems supports multi-node profiling to resolve performance limiters on the scale of data centers and clusters. [Multi-node analysis](https://docs.nvidia.com/nsight-systems/UserGuide/index.html#multi-report-analysis) automatically diagnoses performance limiters across many nodes simultaneously. Additionally, network metrics alongside Python backtrace sampling paint a complete picture across GPUs, CPUs, DPUs, and internode communication.

### Optimize Python for AI and Deep Learning  

Nsight Systems helps you write Python applications that maximize GPU utilization. Backtraces and automatic call stack sampling allows you to fine-tune performance for deep learning applications.   
  
Furthermore, integration with Jupyter Lab allows you to profile Python and other supported languages directly in Jupyter, including detailed analysis with the full Nsight Systems GUI. 

[Get the NVIDIA Nsight Tools JupyterLab Extension](https://pypi.org/project/jupyterlab-nvidia-nsight/)

https://www.youtube-nocookie.com/embed/aQ1NYoRvp7o?
 

_Feature Spotlight on Python support in Nsight Developer Tools_   

 ![Nsight Systems detects frame stutter and bottlenecks](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/detect-frame-stutter-and-bottlenecks-630x354.jpg)

_Nsight Systems detected a low-health frame resulting in a large stutter, as well as the calls that caused it. _  

### Detect Frame Stutter and Bottlenecks  

Nsight Systems automatically detects slow frames (by highlighting frame times higher than a target) as well as local stutter frames (by highlighting frames with higher times than neighboring frames). It also automatically reports CPU times per frame and API calls that are likely candidates for causing stutters. This equips developers with plenty of information to locate and resolve the causes of frame drops and inconsistent frame timing.

[Read more about using Nsight Systems to fix stutters in games](https://developer.nvidia.com/blog/using-nsight-systems-for-fixing-stutters-in-games/)

[View Full Feature List](https://developer.nvidia.com/nsight-systems/get-started#feat-table)[Get Started](https://developer.nvidia.com/nsight-systems/get-started)

* * *

## View Other Tools Within the Nsight Suite  

Nsight Systems is part of the NVIDIA Nsight Developer Tools suite, a collection of powerful tools, libraries, and SDKs that enable developers to build, debug, and profile software utilizing the latest accelerated computing hardware.

 ![img-alt-text](https://developer.download.nvidia.com/images/nvidia-nsight-graphics-icon-gbp-shaded-128.png)

### Nsight Graphics  

NVIDIA Nsight Graphics is a standalone developer tool with ray-tracing support that enables you to debug, profile, and export frames built with Direct3D, Vulkan, OpenGL, OpenVR, and the Oculus SDK.

[Get Started](https://developer.nvidia.com/nsight-graphics)

 ![img-alt-text](https://developer.download.nvidia.com/images/nvidia-nsight-compute-icon-gbp-shaded-128.png)

### Nsight Compute  

Nsight Compute is an interactive kernel profiler for CUDA applications. It provides detailed performance metrics and API debugging via a user interface and command-line tool. It also provides a customizable, data-driven user interface and metric collection that can be extended with analysis scripts for post-processing results..

[Get Started](https://developer.nvidia.com/nsight-compute)

 ![img-alt-text](https://developer.download.nvidia.com/images/nvidia-nsight-aftermath-icon.png)

### Nsight Aftermath SDK  

Nsigh Aftermath SDK is a library that integrates into a D3D12 or Vulkan game’s crash reporter to generate GPU “mini-dumps” when an exception or TDR occurs, exposing pipeline information to resolve an unexpected crash.

[Get Started](https://developer.nvidia.com/nsight-aftermath)

[Browse Tutorials](http://developer.nvidia.com/nsight-developer-tools)[Learn More About Nsight Tools](https://developer.nvidia.com/tools-overview)

* * *

## Check out partner testimonials and ecosystem  

&gt; Vulkan is the cornerstone of Adobe’s multi-platform, multi-vendor rendering strategy for its Adobe Substance 3D products. Thanks to the ray-tracing extensions that NVIDIA pioneered and contributed to Khronos, Vulkan gives native access to ray-tracing hardware, offering exceptional ray-tracing performance on supported devices. In addition, Nsight Graphics and Nsight Systems are invaluable tools when it comes to understanding and improving the performance of Vulkan ray-tracing applications.
&gt; 
&gt; — Francois Beaune, Lead Software Engineer of Photorealistic Rendering, Adobe 3D and Immersive
&gt; 
&gt; ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-adobe.svg)

&gt; NVIDIA Nsight Systems has enabled the Microsoft Azure HPC+AI team to perform detailed analysis and optimize GPU-accelerated AI and software for our services and customers. The tool paints a clear picture of events on the CPUs, GPUs, NICs, and OS, which have allowed us to quickly identify the top time-consuming functions and cold spots to target.
&gt; 
&gt; — Kushal Datta, Principal Software Engineer, Microsoft Azure HPC+AI
&gt; 
&gt; ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-microsoft.svg)

&gt; We noticed that our new Quadro P6000 server was ‘starved’ during training, and we needed experts to support us. NVIDIA Nsight Systems helped us to achieve over 90% GPU utilization. A deep learning model that previously took 600 minutes to train now takes only 90.
&gt; 
&gt; — Felix Goldberg, Chief AI Scientist, Tracxpoint

**Deepset achieves a 3.9X speedup and 12.8X cost reduction for training natural language processing models by working with AWS and NVIDIA.**

[Learn More](https://aws.amazon.com/blogs/machine-learning/deepset-achieves-a-3-9x-speedup-and-12-8x-cost-reduction-for-training-nlp-models-by-working-with-aws-and-nvidia/)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-adobe.svg)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-autodesk.svg)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-dassault-systems.svg)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-epic-games.svg)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-microsoft.svg)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-popcorn-fx.svg)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/logo-ubi-soft.svg)

* * *

## Watch Nsight Developer Tools CUDA Tutorials  

CUDA Developer Tools is a series of tutorial videos designed to get you started with using Nsight tools for CUDA development. It explores key features for CUDA profiling, debugging, and optimizing. 

https://www.youtube.com/embed/xdFQZSV5IrU?https://www.youtube.com/embed/xdFQZSV5IrU?https://www.youtube-nocookie.com/embed/xdFQZSV5IrU?
 

#### CUDA Developer Tools | NVIDIA Nsight Tools Ecosystem  

https://www.youtube-nocookie.com/embed/dUDGO66IadU?
 

#### CUDA Developer Tools | Intro to NVIDIA Nsight Systems  

https://www.youtube-nocookie.com/embed/Iuy_RAvguBM?
 

#### CUDA Developer Tools | Intro to NVIDIA Nsight Compute  

[CUDA Developer Tools Tutorials Playlist](https://www.youtube.com/playlist?list=PL5B692fm6--ukF8S7ul5NmceZhXLRv_lR)

* * *

## Watch Nsight Systems Sessions and Technical Videos on Demand  

* * *

## Stay up to Date on the Latest NVIDIA Nsight Systems News  

* * *

## Find more resources  

 ![img-alt-text](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/forums-icon-48x48_1.svg)

#### Explore Nsight Systems Forums   

 ![img-alt-text](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/documentation-icon-48x48_1.svg)

#### Read Nsight Systems Documentation  

 ![img-alt-text](https://developer.download.nvidia.com/images/m48-live-talk-on-demand-256px-grn-1.png)

#### Browse Nsight Tools Tutorials  

[  
](https://developer.nvidia.com/tools-tutorials)

 ![img-alt-text](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/m48-people-group-256px-grn.png)

#### Join the NVIDIA Developer Program  

Ready to get started with NVIDIA Nsight Systems?

[Download Now](https://developer.nvidia.com/nsight-systems/get-started)

Quick Links

- [Download](https://developer.nvidia.com/nsight-systems/get-started)
- [Documentation](https://docs.nvidia.com/nsight-systems/index.html)

* * *


