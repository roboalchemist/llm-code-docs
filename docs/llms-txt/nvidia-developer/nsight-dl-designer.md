# Source: https://developer.nvidia.com/nsight-dl-designer.md

1. 
Home
2. [Developer Tools](https://developer.nvidia.com/isaac)
3. Nsight Deep Learning Designer

 ![Nsight Deep Learning (DL) Designer logo](https://developer.download.nvidia.com/images/nsight/nvidia-nsight-dl-designer-icon.png)

# 

# NVIDIA Nsight Deep Learning Designer

Nsight Deep Learning (DL) Designer is an integrated development environment that helps developers efficiently design and optimize deep neural networks for high-performance inference. It&#39;s built atop the industry standard ONNX model format and popular inference solutions like TensorRT™ and ONNX Runtime.

[Get Started  
](/nsight-dl-designer/getting-started &quot;Download Now&quot;)

## 
## Key Benefits

Nsight DL Designer visualizes a TensorRT model for inspecting and editing.

#### 
### GUI for ONNX Model Design and Optimizations

Nsight DL Designer is a GUI-based tool that makes editing and creating an ONNX model visible and intuitive. Its integration with other tools (including user-defined ones) allows quick and easy whole model transformations.

#### 
### Built-in Profiler for Performance Evaluations

Nsight DL Designer ships with both a ONNX Runtime profiler and a TensorRT profiler. Developers can quickly evaluate a model’s inference performance profile while they make changes to the model.

#### 
### Integration With TensorRT

Nsight DL Designer ships with NVIDIA’s TensorRT (10.7) inference engine, and can be used as its GUI frontend (no separate installation of TensorRT is required). Developers can easily load an ONNX model and convert it into a TensorRT engine with all the ease of a GUI.

* * *

## Explore Key Features  

### Efficient Model Design Without Coding

Nsight DL Designer is a full-fledged editor for ONNX models. Its GUI allows developers to open an existing ONNX model, visualize its computation graph, and make changes to the model graph simply by dragging and dropping ONNX operators. DL Designer is currently aligned with ONNX version 1.15 (opset 20) and supports the latest features like Local Functions and FP8. Advanced users can create a model from scratch entirely in DL Designer (no coding in Python needed!).  
  
DL Designer is integrated with popular ONNX tools like GraphSurgeon and Polygraphy to enable easy global modifications to a model, like graph sanitization, FP16 conversion, and initializers type conversions.  
  
DL Designer also supports user-defined tools that allow developers to make quick whole model transformations using tools that they are familiar with. 

[Click to Enlarge  
  
](https://developer.download.nvidia.com/images/nsight/GlobalModifications.png)

_Global model modification options available in Nsight DL Designer_

[Click to Enlarge  
  
](https://developer.download.nvidia.com/images/nsight/inference-perf.png)

_Nsight DL Designer displays key GPU metrics for a model’s inference performance._

### Inference Performance Profiling With GPU Metrics

For performance-critical applications, frequent and accurate profiling of a model’s inference performance is necessary for developers to gain insights into the model’s bottlenecks and to tweak the model’s architecture or parameters to meet required performance targets.   
  
Nsight DL Designer ships with both a ONNX Runtime (1.17) profiler and a TensorRT (10.7) profiler so developers can design and profile their models all in a single environment. DL Designer’s ONNX Runtime profiler currently supports both CUDA and DirectML execution providers in addition to the CPU execution provider. With these built-in profilers, in addition to timing, developers can also get detailed profiling data that are based on GPU metrics like SM utilization, Tensor Core utilization, SM occupancy, and more. This allows developers to further optimize their models for a specific GPU family.  
  
One distinctive feature of DL Designer’s profilers is the ability to visually correlate the profiling data gathered at low-level kernels to the original ONNX operators in a model.

### Easy Model Export For Deployment

Nsight DL Designer provides flexible options to support model deployment. A network model edited or created using DL Designer can be easily exported as an ONNX file for platform-independent deployment or as a TensorRT engine for high-performance inferencing with TensorRT.   
  
When exporting a model as a TensorRT engine, the same tactics used for profiling will be used by default. This ensures that developers will see the same inference performance from the model in deployment as they see in profiling.

_Click to EnlargeTactics and optimization parameters selected for exporting models as TensorRT Engines._

* * *

## View Other Tools Within the Nsight Suite

Nsight DL Designer is part of the NVIDIA Nsight Developer Tools suite—a collection of powerful tools, libraries, and SDKs that enable developers to build, debug, and profile software utilizing the latest accelerated computing hardware.

 ![Nsight Systems logo](https://developer.download.nvidia.com/images/nsight/nvidia-nsight-systems-icon.png)

### 
### Nsight Systems

NVIDIA Nsight Systems is a system-wide performance analysis tool designed to visualize an application’s algorithms, help you identify the largest opportunities to optimize, and tune to scale efficiently across any quantity or size of CPUs and GPUs.

[Get Started](/nsight-systems)

 ![Nsight Compute logo](https://developer.download.nvidia.com/images/nsight/nvidia-nsight-compute-icon.png)

### 
### Nsight Compute

Nsight Compute is an interactive kernel profiler for CUDA applications. It provides detailed performance metrics and API debugging via a user interface and command-line tool. It also provides a customizable, data-driven user interface and metric collection that can be extended with analysis scripts for post-processing results.

[Get Started](/nsight-compute)

 ![Nsight Graphics logo](https://developer.download.nvidia.com/images/nvidia-nsight-graphics-icon-gbp-shaded-128.png)

### 
### Nsight Graphics

NVIDIA Nsight Graphics is a standalone developer tool with ray-tracing support that enables you to debug, profile, and export frames built with Direct3D, Vulkan, OpenGL, OpenVR, and the Oculus SDK.

[Get Started](/nsight-graphics)

[Browse Tutorials](/nsight-developer-tools &quot;Download Container&quot;)[Learn More About Nsight Tools  
](/tools-overview &quot;Download Now&quot;)

## Stay up to Date on the Latest NVIDIA Nsight Tools News

## Resources

 ![A query icon representing Nsight DL Designer Forums](https://developer.download.nvidia.com/images/nsight/m48-misc-question-faq.svg)

### Nsight DL Designer Forums  

 ![An envelope icon representing Nsight DL Designer feedback](https://developer.download.nvidia.com/images/nsight/m48-email-settings.svg)

### Nsight DL Designer Feedback  

 ![A LLM on a computer screen icon representing Nsight Tools Tutorials](https://developer.download.nvidia.com/images/nsight/m48-digital-deep-learning-institute-talks-training.svg)

### Browse Nsight Tools Tutorials  

Quick Links

- [Get Started](/nsight-dl-designer/getting-started)
- 
- 

* * *

Get started with Nsight DL Designer.

[Get Started](/nsight-dl-designer/getting-started &quot;Github Repo&quot;)


