# Source: https://developer.nvidia.com/networking/rivermax.md

1. [Home](/)

[Networking](/networking)

Rivermax

# NVIDIA Rivermax

NVIDIA® Rivermax® is an optimized networking SDK for media and data streaming applications.

[Get Started](#section-get-started &quot;Get Started&quot;)[Documentation](#section-learning-library &quot;Documentation&quot;)[NVIDIA DOCA Forum](https://forums.developer.nvidia.com/c/infrastructure/doca/370 &quot;DOCA Forums&quot;)

* * *

## See Rivermax in Action

#### Real-Time Streaming for the World’s Largest LED Display

The Las Vegas Sphere relies on NVIDIA Rivermax software to accelerate media streaming. Rivermax enables direct, low‑latency data transfers between the network and GPUs, and with NVIDIA BlueField® DPUs and ConnectX® NICs, it ensures jitter‑free, synchronized delivery of ultra‑high‑resolution, multi‑layer 16K video across the Sphere’s massive LED canvas.

[Learn More](https://blogs.nvidia.com/blog/sphere-las-vegas/)

![NVIDIA Rivermax provides real-time streaming for the Las Vegas Sphere, world’s largest LED display](https://developer.download.nvidia.com/images/networking/sphere-entertainment-1920x1080.jpg)

* * *

## How Rivermax Works

![Join NVIDIA Developer Community](https://developer.download.nvidia.com/images/networking/doca-animation-rivermax-how-it-works-4129550-1920x1080-r05.gif)

### Simplify SMPTE ST 2110 Deployment   

Accelerate the transition to SMPTE ST 2110 with NVIDIA GPUs, NVIDIA networking, and the Rivermax SDK.

[Learn More](https://www.youtube.com/watch?v=-AulvUL7npc)

### Start Building With Rivermax  

Quickly build and optimize data- and media-streaming applications with Rivermax.

[Learn More](https://docs.nvidia.com/doca/sdk/doca+rivermax/index.html)

### Boost Video Streaming With Rivermax  

Learn how to combine GPU-accelerated image and video processing with Rivermax to achieve ultra-high throughput and performance for video streaming applications.

[Learn More](https://www.nvidia.com/en-eu/products/holoscan/media/)

### Rivermax for Media and Entertainment  

Discover how Rivermax enables ultra-low-latency, high-throughput IP streaming over Ethernet to power next-gen broadcast and media production workflows.

[Learn More](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/networking/rivermax/NVIDIA-Rivermax-Datasheet.pdf)

* * *

## Key Features

GPU-accelerated media streaming is streamlined with direct SMPTE ST 2110 processing—delivering efficient, scalable, real-time performance.

### GPUDirect Support

With NVIDIA GPUDirect®, Rivermax utilizes the high-speed PCIe interface to pass data directly to and from the GPU without burdening the CPU.

- 

Cuts processing latency

- 

Supported on Linux and Windows

- 

ST2110 and any data streaming

### Kernel Bypass, CPU Efficient 

Rivermax minimizes CPU overhead and maximizes application performance.

- 

Kernel bypass technology for direct, hardware-based data transfer between user-space memory and the network interface

- 

Offloads packet processing from the CPU to dedicated hardware accelerators

- 

Hardware-level packet pacing for smooth, consistent streaming across all data flows

### Advanced and Flexible SDK

The unified, cross-platform SDK is designed for high-performance media streaming and easy integration.

- 

Seamless GPU-NIC orchestration with support for SMPTE ST 2110 and hardware-based interconnects

- 

Broad compatibility across Linux, Windows, x86, and Arm, with a simple API for frame- and line-based data

- 

Integrated timing and redundancy via easy PTP/NMOS integration and SMPTE ST 2022-7 stream reconstruction

* * *

## Get Started With Rivermax 

![Register and login to NVIDIA Rivermax getting started page](https://developer.download.nvidia.com/icons/m48-login-256px-blk.svg)

### Log In

**Register to access the Rivermax Getting Started page.**  
  
Explore SDK highlights, and download and install it on supported platforms.

[Go to the Rivermax Getting Started Page](/networking/rivermax-getting-started)

![EPIC Unreal Engine Plug-In](https://developer.download.nvidia.com/icons/m48-accelerate-computing-with-cuda-c-c++.svg)

### Build and Explore

**Access advanced code samples.**  
  
Deploy the Rivermax SDK and use example code to stream video, data, and audio.

[Explore Code Samples on the Rivermax GitHub](https://github.com/NVIDIA/Rivermax)

![EPIC Unreal Engine Plug-In](https://developer.download.nvidia.com/icons/m48-virtual-pc-cloud-computer.svg)

### Get the Epic Unreal Engine Plug-In

**Use SMPTE 2110 with an nDisplay virtual production setup.**  
  
Learn to integrate SMPTE 2110 with NVIDIA Rivermax for virtual production.

[Use SMPTE ST 2110 With nDisplay](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-smpte-2110-with-ndisplay?application_version=5.5)

* * *

## Starter Kits

### SMPTE ST 2110

SMPTE ST 2110 delivers modern, flexible, and high-performance IP-based media production.

- 

[Simplified Application-Level Interfaces for Sending and Receiving Generic or Media Streams (GitHub)](https://github.com/NVIDIA/rivermax-dev-kit/tree/main)

- 

[NVIDIA Holoscan for Media—Real-Time AI Platform for the Future of Live Media](/holoscan-for-media)

- 

[NVIDIA DeepStream—ST2110 GStreamer Pipeline (Documentation)](https://docs.nvidia.com/metropolis/deepstream/8.0/text/DS_plugin_gst-nvdsudpsink.html)

- 

[Ultra-High-Performance Video Streaming Meets the GPU With NVIDIA Rivermax (GTC Session)](https://www.nvidia.com/en-us/on-demand/session/gtcspring21-s31886/)

### Virtual Production

Epic Unreal Engine with Rivermax enhances flexibility and performance for virtual productions, so creative teams can deliver high-quality, synchronized content to multiple displays.

- 

[DOCA-FireFly Time Service (Documentation)](https://docs.nvidia.com/networking/display/dpf2504/doca+firefly+service)

- 

[Timing With DOCA Firefly (Whitepaper)](https://resources.nvidia.com/en-us-accelerated-networking-resource-library/gtc21-fall-networkin)

- 

[Epic Games and NVIDIA Are Setting New Standards in Virtual Production (Blog)](https://resources.nvidia.com/en-us-professional-broadcast/unreal-engine)

- 

[Epic Unreal Engine Plug-In](https://dev.epicgames.com/community/learning/tutorials/mPJO/unreal-engine-smpte-2110-ux)

### Professional Audiovisual

Pro AV is a rapidly evolving field powering the world&#39;s most advanced communication, entertainment, and collaborative spaces.

- 

[The MSG Sphere Is a Flagship Pro AV Project—by Definition and in Scale (Blog)](https://blogs.nvidia.com/blog/sphere-las-vegas/)

- 

[Accelerating Customers&#39; Media Streaming Solutions on Windows (GTC Session)](https://www.nvidia.com/en-us/on-demand/session/gtcspring22-s41927/)

- 

[IPMX Receiver Code (GitHub)](https://github.com/NVIDIA/rivermax-dev-kit/tree/main/source/apps/rmax_ipmx_receiver)

- 

[IPMX Sender Code (GitHub)](https://github.com/NVIDIA/rivermax-dev-kit/tree/main/source/apps/rmax_ipmx_sender)

* * *

## Learning Library

Tech Blog 

Rivermax and FastSockets: Ultra-Low-Latency Networking

**NVIDIA Rivermax**  
  
Ultra-low latency and zero packet loss are vital for the financial, gaming, and media and entertainment industries.

Video 

FlowCaster Rivermax Software ST2110 for Adobe, Avid, and Resolve

**NVIDIA Rivermax**  
  
Drastic&#39;s FlowCaster plug-in for Adobe Premiere, Avid Media Composer, DaVinci Resolve, and others leverages the NVIDIA Rivermax software to generate SMPTE 2110-compliant audio, video, and ancillary output.

Tutorial 

Ultra-High-Performance Video Streaming Meets the GPU With NVIDIA Rivermax

**NVIDIA Rivermax**  
  
Rivermax natively supports GPUDirect on Linux and Windows to provide maximum performance with low latency.

Tutorial 

Connecting NVIDIA NIM to Uncompressed Audio and Video Pipelines With Holoscan for Media

**NVIDIA Holoscan for Media**  
  
NVIDIA Holoscan for Media is a software-defined platform running on AI infrastructure for developing, deploying, and running live media applications.

Video 

AI-Enabled IP-Based Workflows With NVIDIA Rivermax and NVIDIA Jetson

**NVIDIA DOCA FireFly, RTX™ A600, Rivermax, BlueField DPU, ConnectX-6 Dx NIC, and Jetson™**  
  
NVIDIA and Dell technologies simplify SMPTE ST 2110 and enable AI-driven workflows from workstation to edge to power next-gen IP broadcast.

Guide 

Rivermax License Generation Guidelines

**NVIDIA Rivermax**  
  
This document provides guidelines for generating a license for NVIDIA Rivermax.

* * *

## Partner Ecosystem

Explore the NVIDIA partners who are rolling out full, Rivermax-based IP solutions rigorously tested in their labs.

[
 ![NVIDIA Rivermax Ecosystem Partner - 7thSense](https://developer.download.nvidia.com/images/logos/7thsense-logo.svg)
](https://7thsense.one/)

[
 ![NVIDIA Rivermax Ecosystem Partner - ATEME](https://developer.download.nvidia.com/images/logos/ateme-logo.svg)
](https://www.ateme.com/product-titan-software/)

[
 ![NVIDIA Rivermax Ecosystem Partner - Avid](https://developer.download.nvidia.com/images/logos/avid-logo.svg)
](https://www.avid.com/)

[
 ![NVIDIA Rivermax Ecosystem Partner - Amazon AWS](https://developer.download.nvidia.com/images/logos/aws-logo(1).svg)
](https://aws.amazon.com/elemental-live/)

[
 ![NVIDIA Rivermax Ecosystem Partner - Comprimato](https://developer.download.nvidia.com/images/logos/comprimato-logo.svg)
](https://comprimato.com/products/twenty-one-encoder/)

[
 ![NVIDIA Rivermax Ecosystem Partner - Disguise](https://developer.download.nvidia.com/images/logos/disguise-logo.svg)
](https://www.disguise.one/en/products/rx-range/rx/)

[
 ![NVIDIA Rivermax Ecosystem Partner - Drastic.tv](https://developer.download.nvidia.com/images/logos/dt-logo.svg)
](https://www.drastic.tv/)

[
 ![NVIDIA Rivermax Ecosystem Partner - Emergent](https://developer.download.nvidia.com/images/logos/emergent-logo.svg)
](https://emergentvisiontec.com/)

[
 ![NVIDIA Rivermax Ecosystem Partner - Evertz](https://developer.download.nvidia.com/images/logos/evertz-logo.svg)
](https://evertz.com/applications/live-production/)

[
 ![NVIDIA Rivermax Ecosystem Partner - Grass Valley](https://developer.download.nvidia.com/images/logos/grass-valley-logo.svg)
](https://www.grassvalley.com/ampp/)

[
 ![NVIDIA Rivermax Ecosystem Partner - Harmonic](https://developer.download.nvidia.com/images/logos/harmonic-logo.svg)
](https://www.harmonicinc.com/video-streaming/media-servers-storage/spectrum-x/)

[
 ![NVIDIA Rivermax Ecosystem Partner - IMMERSIVE Design Studios](https://developer.download.nvidia.com/images/logos/immersive-logo.svg)
](http://www.immersivedesignstudios.com)

[
 ![NVIDIA Rivermax Ecosystem Partner - IntoPIX](https://developer.download.nvidia.com/images/logos/intopix-logo.svg)
](https://www.intopix.com/blogs/post/gtc-2021-4k-demo-JPEG-XS-Rivermax-NIC-ConnectX5-2110)

[
 ![NVIDIA Rivermax Ecosystem Partner - Lawo](https://developer.download.nvidia.com/images/logos/lawo-logo.svg)
](https://lawo.com/)

[
 ![NVIDIA Rivermax Ecosystem Partner - Mediaproxy](https://developer.download.nvidia.com/images/logos/mediaproxy-logo.svg)
](https://www.mediaproxy.com/Solutions/Monitoring)

[
 ![NVIDIA Rivermax Ecosystem Partner - NEIO Systems](https://developer.download.nvidia.com/images/logos/neio-systems-logo.svg)
](http://neio.systems)

[
 ![NVIDIA Rivermax Ecosystem Partner - Panasonic](https://developer.download.nvidia.com/images/logos/panasonic-logo.svg)
](https://pro-av.panasonic.net/en/products/it_ip_platform/)

[
 ![NVIDIA Rivermax Ecosystem Partner - Pixera](https://developer.download.nvidia.com/images/logos/pixera-logo.svg)
](https://pixera.one/en/)

[
 ![NVIDIA Rivermax Ecosystem Partner - RT Software](https://developer.download.nvidia.com/images/logos/rt-software-logo.svg)
](https://rtsw.co.uk/)

[
 ![NVIDIA Rivermax Ecosystem Partner - Telestream](https://developer.download.nvidia.com/images/logos/telestream-logo.svg)
](http://www.telestream.net/iq/inspect-2110.htm)

[
 ![NVIDIA Rivermax Ecosystem Partner - Unreal Engine](https://developer.download.nvidia.com/images/logos/unreal-engine-logo.svg)
](https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-workflows-for-smpte-2110-in-unreal-engine)

 ![NVIDIA Rivermax Ecosystem Partner -ZREAL](https://developer.download.nvidia.com/images/logos/zreal-logo.svg)

* * *

## More Resources

![NVIDIA Rivermax FAQ](https://developer.download.nvidia.com/icons/m48-misc-question-faq.svg)

### Read the FAQ

![Join NVIDIA Developer Community](https://developer.download.nvidia.com/icons/m48-people-group.svg)

### Join the Community

![Sign up for NVIDIA Developer Newsletter](https://developer.download.nvidia.com/icons/m48-email-settings.svg)

### Sign Up for the Developer Newsletter

Get started with NVIDIA Rivermax today.

[Download Now](/networking/rivermax-getting-started &quot;Download Rivermax&quot;)


