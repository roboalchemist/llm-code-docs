# Source: https://developer.nvidia.com/npp.md

1. [Home](/)

Computer Vision

Computer Vision SDKs and Libraries

NPP

# NVIDIA Performance Primitives (NPP)

 ![Decorative image showing an example of Euclidean Distance Transform (EDT) function](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/NPP-example-Euclidean-distance-transport.png)
  
NPP example: Euclidean Distance Transform (EDT)

* * *

## Download NPP

NPP is a library of over 5,000 primitives for image and signal processing that lets you easily perform tasks such as color conversion, image compression, filtering, thresholding, and image manipulation. You can now access GPU-accelerated image, video, and signal-processing functions that perform up to 30X faster than CPU-only implementations.

[Download NPP](https://developer.nvidia.com/cuda-downloads)

## Download NPP+

NPP+ enables C++ support—a game-changer that surpasses the overall performance of NPP while requiring fewer operators. With the NPP+ library, you&#39;ll experience a seamless interface for image and signal processing, plus the added advantage of multi-GPU support. It’s an innovative standalone component that delivers enhanced capabilities and efficiency for all your processing needs.

[Download NPP+](https://developer.nvidia.com/nppplus-downloads)

* * *

## Use Cases

### Industrial Inspection

Enhance industrial inspection efficiency and accuracy by rapidly processing high-volume imaging data to detect defects, ensure quality control, and streamline maintenance operations.

### Medical Imaging

Help clinicians perform faster and more precise diagnostics with GPU-accelerated processing of complex imaging data for early detection and treatment planning.

### Robotics

Enable real-time, GPU-accelerated image and signal processing for enhanced autonomous decision-making, precision in object recognition, and rapid environmental analysis.

* * *

## NPP Benefits

### Scalable Performance

The NPP library optimizes the use of available computing resources so your application achieves maximum performance across data center, workstation, and embedded platforms. NPP can also handle highfidelity 10-bit or 12-bit HDR video (i.e. cooled sensor astrophotography).

### Simple Setup

Ready-to-use, domain-specific, high-performance primitives feature a rich set of functions supporting a large variety of image formats. Drop-in replacement for the Intel Integrated Performance Primitives (IPP) CPU library. NPP accepts raw uncompressed image or signal data and supports multiple RGB and YUV image and video formats.

### Flexible Design

Use as a stand-alone library to add GPU acceleration to your application in a matter of hours, or as a cooperative library for interoperating efficiently with your existing GPU code. It includes both low-level primitives and high-level capabilities.

### C++ Support

Enjoy faster execution times, simplify code, and enhance maintainability with NPP+. It helps you effortlessly integrate image and signal processing and tap into the power of multiple GPUs for scalability and higher performance levels.

* * *

## Comparative Performance
 ![A comparative performance chart of NVIDIA Performance Primitives (NPP) vs IPP](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/Comparative-performance-NPP-vs-IPP.png)
# Test Setup

- 

IPP 2018 running on an Intel Xeon Gold 6240@2GHz 3.9GHz Turbo (Cascade Lake) server with HT on; Ubuntu18.04 OS

- 

GPU—Tesla T4(TU104) 1\*16097 MiB 1\*40 SM

- 

Tesla V100-SXM2-32GB(GV100) 1\*32510 MiB 1\*80 SM

- 

A100-SXM4-40GB(GA100) 1\*40557 MiB 1\*108 SM

- 

CUDA Driver — 445.33 (r445\_00), CUDA Toolkit 11.0

- 

Speedup represents average bandwidth increase over all routines

* * *

## NPP Operations and Functions

NPP offers a broad range of over 5,000 operations and functions. Key categories include image color conversion, signal filtering, and image linear transforms. All categories of operations and functions:

- 

Image Arithmetic and Logical Operations

- 

Image Color Conversion Functions

- Image Data Exchange and Initialization Functions  

- 

Image Filtering Functions

- 

Image Geometry Transforms Functions

- 

Image Linear Transforms Functions

- 

Image Morphological Operations

- 

Image Statistics Functions

- 

Image Threshold and Compare Operations

- 

Image Memory Management Functions

- 

Signal Arithmetic and Logical Operations

- Signal Conversion Functions  

- 

Signal Filtering Functions

- 

Signal Initialization Functions

- 

Signal Statistical Functions

- 

Signal Memory Management Functions

[  
Additional NPP Operations](https://docs.nvidia.com/cuda/npp/)

If NPP isn’t the right library for your use case, check out other data processing libraries like [CV-CUDA](https://developer.nvidia.com/cv-cuda), [DALI](https://developer.nvidia.com/dali), [VPI](https://developer.nvidia.com/embedded/vpi), or [Optical Flow SDK](https://developer.nvidia.com/opticalflow-sdk).

* * *

## Videos and Webinar

* * *

## Additional Resources

- 
[GPU Accelerated Computing With C and C++ (2:01 Minutes)  
](https://developer.nvidia.com/how-to-cuda-c-cpp)
- 
[NVIDIA 2D Image and Signal Processing Performance Primitives (NPP) Documentation](https://docs.nvidia.com/cuda/npp/index.html)
- 
[Box Filter With NPP](https://github.com/NVIDIA/cuda-samples/tree/master/Samples/4_CUDA_Libraries/boxFilterNPP)
- 
[Histogram Equalization With NP](https://github.com/NVIDIA/cuda-samples/tree/master/Samples/4_CUDA_Libraries/histEqualizationNPP)

- 
[FreeImage and NPP Interoperability](https://github.com/NVIDIA/cuda-samples/tree/master/Samples/4_CUDA_Libraries/freeImageInteropNPP)
- 
[Watershed segmentation With NPP](https://github.com/NVIDIA/cuda-samples/tree/master/Samples/4_CUDA_Libraries/watershedSegmentationNPP)
- 
[Additional Code Samples](https://github.com/NVIDIA/CUDALibrarySamples/tree/master/NPP)

Get started with NVIDIA 2D Image and signal processing performance primitives (NPP).

[Download](https://developer.nvidia.com/cuda-downloads)

Quick Links

- [Download NPP  
](https://developer.nvidia.com/cuda-downloads)
- [Download NPP+](https://developer.nvidia.com/nppplus-downloads)
- 

* * *


