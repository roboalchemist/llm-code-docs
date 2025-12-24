# Source: https://developer.nvidia.com/optical-flow-sdk.md

## Optical Flow
- [Benefits](#benefits)[Performance](#performance)[Use Cases](#use-cases)[Resources](#resources)

# NVIDIA Optical Flow SDK

The NVIDIA Optical Flow SDK taps in to the latest hardware capabilities of NVIDIA Turing™, Ampere, and Ada architecture GPUs dedicated to computing the relative motion of pixels between images. The hardware uses sophisticated algorithms to yield highly accurate flow vectors, ideal for handling frame-to-frame intensity variations and tracking true object motion.

[Get Started](https://developer.nvidia.com/opticalflow/download)
  

 ![Turing hardware generated optical flow map sample](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/opticalflow/OF_SDK_000.png) Turing hardware-generated optical flow map sample — [source footage](https://ultravideo.cs.tut.fi/#testsequences)

* * *

## Optical Flow Benefits

## Accurate Video Analytics

Accurately detect and track objects in successive video frames while significantly reducing the computational complexity requirements.

## Real-Time Performance

Interpolate or extrapolate video frames in real time, improving smoothness of video playback or reducing latency in VR experiences.

## GPU Acceleration

Get performance optimized for Turing, Ampere, and future generations of NVIDIA GPU architectures that includes high-speed computation of accurate flow vectors with little impact on the CPU or GPU.

* * *

## Performance
 ![A chart showing performance of frame interpolation time](https://developer.download.nvidia.com/images/frame-interpolation-time-1920x1080.jpg &quot;A chart showing performance of frame interpolation time&quot;)

Frame Interpolation Time

  
  
 ![A graph showing optical flow quality metrics](https://developer.download.nvidia.com/images/optical-flow-quality-metrics-1920x1080.jpg &quot;A graph showing optical flow quality metrics&quot;)

Optical Flow Quality metrics

* * *

## Optical Flow Engine-Assisted Frame Rate Up-Conversion Library
  

 ![Interpolated frames are generated in between the original frames to create a smoother image](https://developer.download.nvidia.com/images/optical-flow-fruc-1920x1080-1.jpg &quot;Interpolated frames are generated in between the original frames to create a smoother image&quot;)

NvOFFRUC interpolates new frames using optical flow vectors to double the effective frame rate of a video. The result is improved smoothness of video playback and perceived visual quality.

[Learn More About Frame Rate Up-Conversion](https://developer.nvidia.com/blog/harnessing-the-nvidia-ada-architecture-for-frame-rate-up-conversion-in-the-nvidia-optical-flow-sdk/)

  
  
  
  

## Object Tracking for Intelligent Video Analytics
  

Optical Flow SDK 2.0 introduced an object tracker library based on optical flow, along with source code and ready-to-use API. In our experiments, the optical flow-based object tracker has been shown to reduce the GPU utilization by up to 80%, compared to some of the most popular algorithms without compromising the accuracy of tracking. Optical Flow SDK 3.0 introduces a DirectX12 Interface, forward and backward flow and a global flow vector.

[Learn More About Optical Flow SDK](https://developer.nvidia.com/blog/an-introduction-to-the-nvidia-optical-flow-sdk/)

 ![A flowchart showing object tracking for Intelligent Video Analytics](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/opticalflow/OF2_005.png &quot;A flowchart showing object tracking for Intelligent Video Analytics&quot;)

  
  
  
  

## Video Frame Interpolation and Extrapolation
  

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/opticalflow/OF_SDK_001b.png)

Optical flow can also be used very effectively for interpolating or extrapolating video frames in real time. This can be useful in improving the smoothness of video playback, generating slow-motion videos, or reducing the apparent latency in VR experience. Optical Flow functionality in Turing and Ampere GPUs accelerates these use cases by offloading the intensive flow vector computation to a dedicated hardware engine on the GPU silicon, thereby freeing up GPU and CPU cycles for other tasks. This functionality in hardware is independent of CUDA cores.

[Learn More About Video Frame Interpolation and Extrapolation](https://docs.nvidia.com/video-technologies/optical-flow-sdk/nvfruc-programming-guide/index.html#frame-interpolation)

* * *

## Videos &amp; Webinars

## Additional Resources

 ![](https://developer.download.nvidia.com/images/newspaper-icon.svg)[Read DevBlog:An Introduction to the Optical Flow SDK](https://devblogs.nvidia.com/an-introduction-to-the-nvidia-optical-flow-sdk/)
  

 ![](https://developer.download.nvidia.com/images/newspaper-icon.svg)[Read DevBlog: AV1 Encoding and NvOFFRUC: Video Performance Boosts and Higher Fidelity on the NVIDIA Ada Architecture](https://developer.nvidia.com/blog/av1-encoding-and-fruc-video-performance-boosts-and-higher-fidelity-on-the-nvidia-ada-architecture/)
  

 ![](https://developer.download.nvidia.com/images/newspaper-icon.svg)[Read DevBlog: Harnessing the NVIDIA Ada Architecture for Frame-Rate Up-Conversion in the NVIDIA Optical Flow SDK](https://developer.nvidia.com/blog/harnessing-the-nvidia-ada-architecture-for-frame-rate-up-conversion-in-the-nvidia-optical-flow-sdk/)
  

 ![](https://developer.download.nvidia.com/images/file-icon.svg)[View Document: Optical Flow Documentation](https://docs.nvidia.com/video-technologies/optical-flow-sdk/index.html)
  

 ![](https://developer.download.nvidia.com/images/newspaper-icon.svg)[Github: NVIDIA Optical Flow in OpenCV](https://github.com/opencv/opencv_contrib)

Get started developing with the Optical Flow SDK.

[Download Now](https://developer.nvidia.com/opticalflow/download)  


