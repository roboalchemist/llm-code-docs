# Source: https://developer.nvidia.com/rtx-kit.md

# NVIDIA RTX Kit 

NVIDIA RTX™ Kit is a suite of neural rendering technologies to ray trace games with AI, render scenes with immense geometry, and create game characters with photo-realistic visuals.

[Get Started  
](#section-getting-started &quot;Github Repo&quot;)[Notify Me for Future Releases  
](/rtx-kit/notify-me &quot;Github Repo&quot;)[Download Zorah Sample  
](https://dlss.download.nvidia.com/demos/zorah/ZorahSample_UE5_Source_1.1.0.7z &quot;Github Repo&quot;)

* * *
 
https://www.youtube-nocookie.com/embed/5PHBXY0FI5o?&amp;autoplay=1&amp;loop=1&amp;playlist=5PHBXY0FI5o
 

Zorah technology demo, built in Unreal Engine 5

### Watch Trailer  

See Zorah in action in our visual trailer shown during the NVIDIA keynote at CES 2025.

[Watch Video (1:37)](https://youtu.be/H681NInCwFo)

### What are Cooperative Vectors?

See how cooperative vectors unlocks the full potential of neural rendering.

[Read Blog  
](https://devblogs.microsoft.com/directx/enabling-neural-rendering-in-directx-cooperative-vector-support-coming-soon/)

### Path Tracing in Unreal Engine 5

Learn what you can do with real-time path tracing in UE5.

[Watch Video (36:25)](https://www.youtube.com/watch?v=zD9kS1nOuyU&amp;pp=ygUfcGF0aCB0cmFjaW5nIGluIHVucmVhbCBlbmdpbmUgNQ%3D%3D)

### Get Started with RTX Kit  

In this tutorial, we will focus on how to get started with the new SDKs available today through NVIDIA RTX Kit.

[Read Blog  
](https://developer.nvidia.com/blog/get-started-with-neural-rendering-using-nvidia-rtx-kit/)

* * *

## Key Benefits

 ![A lamp and a piece of satin cloth placed on stone stairs](https://developer.download.nvidia.com/images/rtx/kit/deploy-ai-shaders-1920-1080.jpg)

### Train and Deploy AI From Shaders  

Unlock new compression techniques that reduce texture memory consumption up to 8X and compress shader code for up to 5X faster material processing. Allows developers to render film-quality assets in real time.

 ![Sunlight shining on ancient building walls](https://developer.download.nvidia.com/images/rtx/kit/path-trace-1920-1080.jpg)

### Path Trace at Game-Ready Performance   

Build your bounding volume hierarchy (BVH) faster and simulate physically accurate reflections, shadows and global illumination for detailed worlds.

 ![A digital human rendering by NVIDIA RTX Kit](https://developer.download.nvidia.com/images/rtx/kit/digital-human-render-1920-1080.jpg)

### Accelerate Digital Human Rendering  

Hardware-accelerated strand-based hair provides a simplified workflow with photo-realistic results and ray-traced subsurface scattering renders skin better.

* * *

## Get Started with RTX Kit Technologies

AI-Powered Shaders

Geometry and Lighting

Character Rendering

### RTX Neural Shaders 

Train and deploy neural networks within shaders to unlock new compression and approximation techniques for next-generation asset generation.

[Download (GitHub)](https://github.com/NVIDIA-RTX/Rtxns)

### RTX Neural Texture Compression 

Use AI to compress textures with up to 8x disk memory improvement at similar visual fidelity to traditional block compression.

[Download (GitHub)](https://github.com/NVIDIA-RTX/Rtxntc)

### RTX Texture Filtering 

Randomly samples textures after shading and filters difficult volumes, reducing artifacts and improving image quality.

[Download (GitHub)](https://github.com/NVIDIA-RTX/Rtxtf)

### RTX Neural Materials 

Use AI to compress shader code of complex multi-layered materials for up to 8X faster material processing to bring real-time performance to film-quality assets.

[Notify Me](/rtx-kit/notify-me/)

### RTX Texture Streaming  

Tool that divides textures into smaller tiles and efficiently manages and loads them based on need.

[Download (GitHub)](https://github.com/NVIDIA-RTX/RTXTS)

### RTX Mega Geometry 

Accelerate BVH building for cluster-based geometry systems, enabling up to 100x more ray-traced triangles and better performance in heavily ray-traced scenes.

[Download (GitHub)](https://github.com/NVIDIA-RTX/RTXMG)

[Access NVIDIA RTX Branch of Unreal Engine 5 ](https://developer.nvidia.com/game-engines/unreal-engine/rtx-branch)

### RTX Dynamic Illumination 

Library of importance sampling algorithms that sample the most important lights in a scene and renders them physically accurate.

1. 
ReSTIR Direct Illumination: One-bounce lighting from many lights without complex data
2. 
ReSTIR Global Illumination: Resamples multi-bounce indirect lighting paths  

3. 
ReSTIR Path Tracing: Samples the most impactful light paths for increased image quality

[Download (GitHub)](https://github.com/NVIDIA-RTX/RTXDI)

[Access RTX Branch of Unreal  
Engine 5](https://developer.nvidia.com/game-engines/unreal-engine/rtx-branch)

### RTX Global Illumination 

Scalable solution to compute multi-bounce indirect lighting.

1. 
Neural Radiance Cache (NRC): Use AI to predict the amount of light that&#39;s emitted from or passing through a specific area
2. 
Spatial Hash Radiance Cache( SHaRC): Fast and scalable algorithm to compute light in a given area  

3. 
Dynamic Diffuse Global Illumination (DDGI): Probe-based solution that delivers multi-bounce indirect lighting without lightmaps or baking.  

[Download (GitHub)](https://github.com/NVIDIA-RTX/Rtxgi)

[Access RTX Branch of Unreal  
Engine 5](https://developer.nvidia.com/game-engines/unreal-engine/rtx-branch)

### NVIDIA RTX™ Path Tracing   

NVIDIA RTX™ Path Tracing (RTXPT) merges years of best practices within real-time ray tracing and neural graphics development for building a real-time path tracer.

[Download (GitHub)](https://github.com/NVIDIA-RTX/RTXPT)

### NVIDIA Real-Time Denoisers   

Library of denoisers designed to work with low ray-per-pixel signals.

1. 
ReBLUR: Denoise diffuse and specular signals  

2. 
SIGMA: Denoise shadows
3. 
ReLAX: Denoise RTX Dynamic Illumination signals.  

[Download (GitHub)](https://github.com/NVIDIA-RTX/NRD)

### NVIDIA Opacity Micro-Map 

Efficiently map intricate geometries onto triangles and encode their opacity for better ray tracing performance.

[Download (GitHub)](https://github.com/NVIDIA-RTX/Omm)

### RTX Memory Utility 

Compaction and suballocation of acceleration structures to reduce memory consumption.

[Download (GitHub)](https://github.com/NVIDIA-RTX/Rtxmu)

### RTX Character Rendering 

Set of tools to create path-traced stand-based hair and skin.

1. 
Subsurface Scattering (SSS): Render skin with accurate lighting and translucency
2. 
Linear Swept Spheres (LSS): Blackwell accelerated sphere and curve primitive for strand-based path-traced hair.  

3. 
Enhanced analytical Bi-Directional Scattering Distribution Function (BSDF): Provides shading for strand-based hair.  

4. 
Disjoint Orthogonal Triangles Strips (DOTS): Provides high-quality strand-based hair for all GPUs.

[Download (GitHub)](https://github.com/NVIDIA-RTX/Rtxcr)

**RTX Branch of Unreal Engine 5 (Coming Soon)**

* * *

## Download the New Microsoft Agility SDK Preview Today

Cooperative vectors are a brand-new programming feature available now in Shader Model 6.9. It introduces RTX Tensor core acceleration for AI computations directly within game shaders. This enables significant performance improvements and efficiency gains in neural shading technologies.

[Download Now](https://devblogs.microsoft.com/directx/directx12agility/ &quot;Github Repo&quot;)[Learn More](https://devblogs.microsoft.com/directx/agility-sdk-1-717-preview-and-1-616-retail &quot;Github Repo&quot;)

* * *

## Additional RTX Rendering Technologies

### Generative AI Face Rendering

RTX Neural Faces is a new generative AI algorithm that allows developers to cross the uncanny valley in real time. This AI model is trained on a character dataset built from the original photographs of the model. Using a synthetic generation pipeline, the base character dataset is expanded to variants with different lighting conditions, emotions and occlusion. This model then takes a rasterized face and 3D pose and generates an enhanced face in real time.

[Get Notified when RTX Neural Faces is Available](/rtx-kit/notify-me)

https://www.youtube-nocookie.com/embed/KnozAHKTz9o?

![Images of a building rendered better with NVIDIA DLSS 4 and Reflex technologies](https://developer.download.nvidia.com/images/rtx/kit/dlss-reflex.jpg)

### Better With DLSS and Reflex

DLSS is a revolutionary suite of neural rendering technologies that uses AI to boost FPS, reduce latency, and improve image quality. ‌The latest breakthrough, DLSS 4, brings new Multi Frame Generation and enhanced Ray Reconstruction and Super Resolution, powered by [NVIDIA GeForce RTX™ 50 Series GPUs](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/) and fifth-generation Tensor Cores.   
  
Reflex technologies optimize the graphics pipeline for ultimate responsiveness, providing faster target acquisition, quicker reaction times, and improved aim precision in competitive games. Reflex 2 introduces Frame Warp, which further reduces latency based on the game’s latest mouse input.

[Learn More about NVIDIA DLSS](https://developer.nvidia.com/rtx/dlss)

[Learn More about NVIDIA Reflex](https://developer.nvidia.com/performance-rendering-tools/reflex)

### Improving Ray Traced Shader Performance

Shader Execution Reordering (SER) is a performance optimization that unlocks the potential for better execution and memory coherence in ray tracing shaders. SER allows applications to easily reorder threads on the GPU, reducing the divergence effects that occur in particularly challenging ray tracing workloads like path tracing. New SER innovations in GeForce RTX 50 Series GPUs further improve efficiency and precision of shader reordering operations compared to GeForce RTX 40 Series GPUs.

[Learn How to Get Started](/blog/improve-shader-performance-and-in-game-frame-rates-with-shader-execution-reordering/)

![NVIDIA RTX Neural Faces generates an enhanced face in real time](https://developer.download.nvidia.com/images/rtx/kit/ser-1920-1080.jpg)

* * *

## RTX Kit Library

* * *

## On-Demand Sessions

* * *

## More Resources

 ![A decorative image representing Developer Community](https://developer.download.nvidia.com/icons/m48-people-group.svg)

### Developer Forums  

 ![A decorative image representing Inception for Startups](https://developer.download.nvidia.com/images/m48-misc-question-faq-256px-blk.png)

### RTX Kit FAQ

 ![img-alt-text](https://developer.download.nvidia.com/icons/m48-email-settings.svg)

### Sign up for Developer Newsletter

* * *

Get Started with NVIDIA RTX Kit Today

[Download](#section-getting-started)


