# Source: https://developer.nvidia.com/vrworks.md

1. 

  1. 
[Home](/)
  2. [NVIDIA VRWorks Graphics](https://developer.nvidia.com/vrworks)

# NVIDIA VRWorks Graphics

VRWorks™ is a comprehensive suite of APIs, libraries, and engines that enable application and headset developers to create amazing virtual reality experiences. VRWorks enables a new level of presence by bringing physically realistic visuals, sound, touch interactions, and simulated environments to virtual reality.

[Get Started](#started)

## See VRWorks Results Across Industries

 ![](https://developer.download.nvidia.com/vrworks/images/vrworks-results-proviz-zerolight-1920x1080.jpg)

### ZeroLight

ZeroLight Virtual Showroom leverages VRS to enable foveated rendering on HMDs that support eye tracking

 

### ESI Group IC.IDO

ESI Group uses VR SLI to improve performance in their IC.IDO collaborative VR environment

 

### Autodesk VRED

Autodesk VRED integrates VRS, VR SLI and DLSS to deliver content adaptive shading and foveated rendering

* * *

## Benefits

VRWorks enhances advanced VR performance by increasing application rendering efficiency and image quality through the use of variable-rate shading and foveated rendering. It offers easy integration and unlimited configurability, thanks to versatile tools and extensive support for multiple graphics APIs, enabling developers to deliver superior VR experiences effortlessly. Additionally, optimized HMD support exposes headset manufacturers to the latest NVIDIA hardware technologies via a plug-and-play collection of APIs, resulting in more performant, immersive, and responsive virtual reality environments.

### Variable Rate Shading

Increase rendering performance and quality by applying a varying amount of processing power to different areas of the image. Variable Rate Shading (VRS) is an easy to implement rendering technique enabled by Turing GPUs. With VRS, single-pixel shading operations can be applied to a block of pixels, allowing applications to effectively vary the shading rate in different areas of the screen. VRS can be used to render more efficiently in VR by rendering to a buffer that closely approximates the lens corrected image that is output to the headset display. VRS can also be coupled with eye-tracking to maximize quality in the foveated region.

[Learn More](https://developer.nvidia.com/vrworks/graphics/variablerateshading)

 

### VRSS

Foveated rendering improves VR image quality by sampling select regions of the HMD screen at a higher shading rate. The latest version of VRSS (Variable Rate Supersampling) supports gaze tracking by integrating eye-tracking technology to dynamically change foveated regions based on where the user looks. VRSS is a zero-coding solution for application developers–all the work is done through NVIDIA drivers and the end user simply turns on VRSS in the NVIDIA Control Panel. HMD manufacturers can integrate their eye tracking run-time to take advantage of these features.

[Learn More](https://developer.nvidia.com/blog/delivering-dynamic-foveated-rendering-with-nvidia-vrss-2/)

 

### Multi-View Rendering

By rendering four projection centers, Multi-View Rendering (MVR) can power canted HMDs (non-coplanar displays) enabling extremely wide fields of view and novel display configurations. MVR is a feature in Turing GPUs that expands upon Single Pass Stereo, increasing the number of projection views for a single rendering pass from two to four. All four of the views available in a single pass are now position-independent and can shift along any axis in the projective space.

[Learn More](https://developer.nvidia.com/vrworks/graphics/multiview)

### VR SLI  

VR SLI provides increased performance for virtual reality apps where multiple GPUs can be assigned a specific eye to dramatically accelerate stereo rendering. With the GPU affinity API, VR SLI allows scaling for systems with more than 2 GPUs.

[Learn More](https://developer.nvidia.com/vrworks/graphics/vrsli)

 

### Lens Matched Shading  

Lens Matched Shading uses the new Simultaneous Multi-Projection architecture of NVIDIA Pascal-based GPUs to provide substantial performance improvements in pixel shading.

[Learn More](https://developer.nvidia.com/vrworks/graphics/lensmatchedshading)

 

### Direct Mode  

Enable better plug-and-play support and compatibility for VR headsets. With Direct Mode, the NVIDIA driver treats the HMD as a special display accessible only to VR applications instead of a normal Windows monitor where your desktop shows up. Direct Mode leverages Front Buffer Rendering to render directly to the front buffer to reduce latency, and Context Priority which supports fine-grained control over GPU scheduling. Context Priority enables advanced virtual reality features such as late latch and asynchronous time warp, which cut latency and quickly adjust images as HMD users move their heads, without the need to re-render a new frame.

[Learn More](https://developer.nvidia.com/vrworks-hmd-developer-program)

 

### DSC  

As HMD resolutions rapidly increase, the bandwidth requirements increase as well. Display Stream Compression (DSC) can provide the needed bandwidth reduction to support compression ratios up to 3:1. DSC was developed as an industry-wide standard for video interfaces; it features extremely low latency and visually lossless compression.

[Learn More](https://news.developer.nvidia.com/DSC-higher-fidelity-vr/)

* * *

## Get Started with NVIDIA VRWorks

### For Application Developers

VRWorks Graphics SDK provides a set of versatile tools to enable ease of integration for application developers to deliver the best VR performance and image quality, with the most configurability and lowest latency. VRWorks Graphics SDK continues to be widely adopted by leading ISV developers in both the enterprise, creative, and gaming markets.

[Download VRWorks Graphics SDK](https://developer.nvidia.com/downloads/vrworks/secure/3.6.2/public_3.6_06112024.zip)

### For HMD Manufacturers

VRWorks Graphics SDK provides custom tools for head-mounted display (HMD) manufacturers to optimize performance and latency to deliver the best image quality with high-resolution displays. The VRWorks SDK for headset developers is available through the VRWorks HMD Manufacturer Program.

[Register for VRWorks HMD Manufacturer Program](https://developer.nvidia.com/nvidia-vrworks-hmd-developer-program)

* * *

## Latest VRWorks News

* * *

## Resources

- 
[Consumer VR Solutions](https://www.nvidia.com/en-us/geforce/technologies/vr/)
- 
[Professional VR Solutions](http://www.nvidia.com/object/quadro-vr-ready.html)
- 
[VIVE Developer Site](https://developer.vive.com/)
- 
[SteamVR/OpenVR from Valve](https://store.steampowered.com/search/?category1=993)
- 
[[Oculus Developer Portal](https://developers.facebook.com/)  
](https://store.steampowered.com/search/?category1=993)

Ready to get started developing with VRWorks?

[Get Started](#started)

* * *


