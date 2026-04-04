# Source: https://developer.nvidia.com/video-codec-sdk.md

# NVIDIA Video Codec SDK

A comprehensive set of APIs including high-performance tools, samples and documentation for hardware-accelerated video encode and decode on Windows and Linux.

[Get Started  
](/video-codec-sdk/download)[Notify Me for Future Releases  
](https://developer.nvidia.com/video-codec-sdk/notify-me)

![img-alt-text](https://developer.download.nvidia.com/images/nvidia-video-codec-sdk.jpg)

Video apps and streaming enabled by NVENC and NVDEC on consumer laptops, desktops and datacenters ensure optimized performance across platforms.

## Hardware-Based Decoder and Encoder

NVIDIA GPUs contain one or more hardware-based decoders and encoders (separate from the CUDA cores) which provide fully accelerated hardware-based video decoding and encoding for several popular codecs. This provides two benefits:

- 

With decoding/encoding offloaded, the compute engine and the CPU are free for other operations.

- 

Any processing pipeline which requires video and GPU compute in sequence runs far more efficiently. This is because the output of the video decoder can be directly provided to the GPU compute, and the output of the GPU compute can be directly provided to the video encoder without any extra memory/PCIe transfers.

GPU hardware accelerator engines for video encoding (referred to as NVENC) and video decoding (referred to as NVDEC) support faster-than-real-time video processing, which makes them suitable for use in multiple applications, including video transcoding, video data compression/decompression for deep learning, game broadcasting, virtual desktops, cloud gaming, secure video playback, etc. Video Codec SDK exposes the APIs that let you harness the NVENC and NVDEC for all video encoding/decoding capabilities of these engines. NVIDIA’s newest GPU architecture, Blackwell, further enhances the performance and quality of NVENC and NVDEC. The ultra-high quality (UHQ) mode for HEVC introduced in SDK v12.2 extends to AV1 in SDK v13.0 (January 2025). In addition, the Blackwell architecture supports 422 H.264; 422 HEVC; 422i, 420i H.264; multi-view HEVC, and improved H.264 throughput per NVDEC.

### Hardware-Accelerated Video Encoding - NVENC  

NVIDIA GPUs contain an on-chip hardware-accelerated video encoder (NVENC), which provides video encoding for H.264, HEVC (H.265) and AV1 codecs.   
  
The software enhancements in SDK v13.0 enable extending ultra-high quality (UHQ) mode to AV1 encoding.. This makes AV1 encoding on Blackwell NVENC comparable to software AV1 encoding with ~3X throughput. The UHQ HEVC mode was introduced in the SDK v12.2 in the Ada generation.  
  
Blackwell introduces 422 progressive and interlaced encode and decode support in hardware, enabling professional use cases in media and entertainment, video editing and broadcast. Multiple NVENCs working together can achieve performance as high as 8K video at 60FPS+.   
  
Video Codec SDK 13.0 also introduces MV-HEVC for hardware-accelerated stereo encoding to address use cases in broadcast, auto and AR/VR headsets.   
  
Using rich APIs in Video Codec SDK, NVENC can be used in a wide range of use cases requiring latency as low as cloud gaming and quality as high as OTT streaming and studio broadcasting. NVIDIA’s Python video bindings, such as PyNvVideoCodec, enable deep learning applications to harness the power of NVENC for video data curation and archiving.

 ![](https://developer.download.nvidia.com/images/2160p30-HQ.png?vv)

[![](https://developer.download.nvidia.com/images/1080p30-LL.png?v)](https://developer.download.nvidia.com/images/1080p30-low-latency-encoding.jpg)

Note: These graphs showcase performance on NVIDIA data center A10, L4, and L40S.  
  
Bitrate savings are BD-BR based on PSNR, averaged across a large variety of content (several hundreds of video clips), using FFmpeg.  
  
Only data center GPUs are presented on the benchmark graphs for clarity, but an equivalent workstation GPU with the same architecture performs similarly​. To learn more about the hardware details, the process and software configuration used for generating the above data, please refer to [this detailed documentation](https://developer.download.nvidia.com/designworks/video-codec-sdk/Video-Benchmark-Ada-July-2023.pdf)​.

| **GPU** | **H.264 (AVCHD) YUV 4:2:0** | **H.264 (AVCHD) YUV 4:4:4** | **H.264 (AVCHD) LOSSLESS** | **H.265 (HEVC) YUV 4:2:0** | **H.265 (HEVC) YUV 4:4:4** | **H.265 (HEVC) LOSSLESS** | **AV1** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MAX Color | MAX Res. | MAX Color | MAX Res. | MAX Color | MAX Res. | MAX Color | MAX Res. | MAX Color | MAX Res. | MAX Color | MAX Res. | MAX Color | MAX Res. |
| Maxwell (1st Gen)\* | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| Maxwell (2nd Gen) | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | N/A | N/A | N/A | N/A | N/A | N/A |
| Maxwell (GM206) | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | N/A | N/A |
| Pascal | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 10-bit | 8192 x 8192\*\* | 10-bit | 8192 x 8192\*\* | 10-bit | 8192 x 8192\*\* | N/A | N/A |
| Volta | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 10-bit | 8192 x 8192 | 10-bit | 8192 x 8192 | 10-bit | 8192 x 8192 | N/A | N/A |
| Turing | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 10-bit | 8192 x 8192 | 10-bit | 8192 x 8192 | 10-bit | 8192 x 8192 | N/A | N/A |
| Ampere  
(A100) | No | No | No | No | No | No | No | No | No | No | No | No | No | No |
| Ampere  
(non A100) | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 10-bit | 8192 x 8192 | 10-bit | 8192 x 8192 | 10-bit | 8192 x 8192 | N/A | N/A |
| Ada | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 8-bit | 4096 x 4096 | 10-bit | 8192 x 8192 | 10-bit | 8192 x 8192 | 10-bit | 8192 x 8192 | 10-bit | 8192 x 8192 |

_\* Except GM108 and GP108 (not supported)_

_\*\* Except GP100 (is limited to 4K resolution)_

### Hardware-Accelerated Video Decoding - NVDEC  

NVIDIA GPUs contain an on-chip hardware-accelerated video decoder (NVDEC), which provides video decoding for several popular codecs.  
  
The APIs in Video Codec SDK enable the software developers to harness the power of NVDEC for many use cases, ranging from traditional use cases such as secure video playback to accelerating video data ingestion and decoding for DNN training and inference.  
  
NVDEC supports hardware-accelerated decoding of the following video codecs on Windows and Linux platforms: MPEG-2, VC-1, H.264 (AVCHD), H.265 (HEVC), VP8, VP9, and AV1 (see table below for codec support for each GPU generation).   
  
With Blackwell GPUs, NVDEC doubles the video decoding throughput for H.264 decoding and adds support for 422 decoding for H.264 and HEVC codecs.

[![](https://developer.download.nvidia.com/images/1080p30-Decode-Streams.png?v)](https://developer.download.nvidia.com/images/1080p30-decode-streams.jpg)

| **GPU** | **\*H.265 (HEVC) 4:4:4** | **H.265 (HEVC) 4:2:0** | **H.264 (AVCHD) 4:2:0** | **VP9** | **VP8** | **MPEG-2** | **VC-1** | **AV1** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAX Color | MAX Res. | MAX Color | MAX Res. | MAX Color | MAX Res. | MAX Color | MAX Res. | MAX Color | MAX Res. | MAX Color | MAX Res. | MAX Color | MAX Res. | MAX Color | MAX Res. |
| Kepler | N/A | N/A | N/A | N/A | 8-bit | 4096 x 4096 | N/A | N/A | N/A | N/A | 8-bit | 4080 x 4080 | 8-bit | 2048 x 1024 | N/A | N/A |
| Maxwell (1st Gen)\* | N/A | N/A | N/A | N/A | 8-bit | 4096 x 4096 | N/A | N/A | N/A | N/A | 8-bit | 4080 x 4080 | 8-bit | 2048 x 1024 | N/A | N/A |
| Maxwell (2nd Gen) | N/A | N/A | N/A | N/A | 8-bit | 4096 x 4096 | N/A | N/A | 8-bit | 4096 x 4096 | 8-bit | 4080 x 4080 | 8-bit | 2048 x 1024 | N/A | N/A |
| Maxwell (GM206) | N/A | N/A | 10-bit | 4096 x 2304 | 8-bit | 4096 x 4096 | 8-bit | 4096 x 2304 | 8-bit | 4096 x 4096 | 8-bit | 4080 x 4080 | 8-bit | 2048 x 1024 | N/A | N/A |
| Pascal | N/A | N/A | 12-bit | 8192 x 8192\*\* | 8-bit | 4096 x 4096 | 12-bit\*\*\*\* | 8192 x 8192\*\* | 8-bit | 4096 x 4096\*\*\* | 8-bit | 4080 x 4080 | 8-bit | 2048 x 1024 | N/A | N/A |
| Volta | N/A | N/A | 12-bit | 8192 x 8192 | 8-bit | 4096 x 4096 | 12-bit | 8192 x 8192 | 8-bit | 4096 x 4096 | 8-bit | 4080 x 4080 | 8-bit | 2048 x 1024 | N/A | N/A |
| Turing | 12-bit | 8192 x 8192 | 12-bit | 8192 x 8192 | 8-bit | 4096 x 4096 | 12-bit | 8192 x 8192 | 8-bit | 4096 x 4096 | 8-bit | 4080 x 4080 | 8-bit | 2048 x 1024 | N/A | N/A |
| Ampere   
(A100) | 12-bit | 8192 x 8192 | 12-bit | 8192 x 8192 | 8-bit | 4096 x 4096 | 12-bit | 8192 x 8192 | 8-bit | 4096 x 4096 | 8-bit | 4080 x 4080 | 8-bit | 2048 x 1024 | N/A | N/A |
| Ampere   
(non A100) | 12-bit | 8192 x 8192 | 12-bit | 8192 x 8192 | 8-bit | 4096 x 4096 | 12-bit | 8192 x 8192 | 8-bit | 4096 x 4096 | 8-bit | 4080 x 4080 | 8-bit | 2048 x 1024 | 10-bit | 8192 x 8192 |
| Ada | 12-bit | 8192 x 8192 | 12-bit | 8192 x 8192 | 8-bit | 4096 x 4096 | 12-bit | 8192 x 8192 | 8-bit | 4096 x 4096 | 8-bit | 4080 x 4080 | 8-bit | 2048 x 1024 | 10-bit | 8192 x 8192 |

_\* Except GM108 (not supported)_

_\*\* Max resolution support is limited to selected Pascal chips_

_\*\*\* VP8 decode support is limited to selected Pascal chips_

_\*\*\*\* VP9 10/12 bit decode support is limited to select Pascal chips_

* * *

## Video Codec APIs  

NVIDIA has provided hardware-accelerated video processing on GPUs for over a decade through the NVIDIA Video Codec SDK.   
  
Video Codec SDK is a comprehensive set of APIs, high-performance tools, sample applications, reusable code, and documentation for hardware-accelerated video encoding and decoding on Windows and Linux.   
  
The NVENCODE and NVDECODE APIs in the NVIDIA Video Codec SDK are C-style APIs, useful for high-performance encoding and decoding using NVENC and NVDEC, respectively. They expose most of the hardware functionality, along with other codec features that are commonly used. Video Codec SDK also provides a set of reusable code in the form of C++ classes built on top of the NVENCODE/NVDECODE APIs, which the applications can easily integrate. NVENCODE/NVDECODE APIs are comprehensive in nature, and expose a large number of codec capabilities, including advanced features.   
  
DirectX and Vulkan Video, on the other hand, provide low-level, hardware-agnostic APIs, and attempt to provide more precise control over resource/memory allocation, task scheduling, and work submission to video hardware engines.  
  
Whether you prefer DirectX or Vulkan, you can combine flexible GPU-accelerated video encoding and decoding with other GPU acceleration, like 3D and AI, using the language of your choice.  
  
The low-level Vulkan Video extensions are also attractive to developers of popular open-source streaming media frameworks such as [GStreamer](https://gstreamer.freedesktop.org/features/index.html) and [FFmpeg](https://lynne.ee/vulkan-video-decoding.html), both of which are being actively ported to Vulkan Video. The cross-platform availability of Vulkan will enable accelerated GPU processing for these frameworks across multiple platforms without needing to port to multiple proprietary video APIs. Please refer to the [Vulkan Video getting started page](https://developer.nvidia.com/vulkan/video/get-started) for more details.  
  
[PyNvVideoCodec](https://docs.nvidia.com/video-technologies/pynvvideocodec/index.html) is another set of APIs introduced in Q4 2023, which provides simple APIs for harnessing video encoding and decoding capabilities when working with videos in Python. PyNvVideoCodec is a library that provides python bindings over C++ APIs for hardware accelerated video encoding and decoding. Major advantages of PyNvVideoCodec are: simple installation process, easy APIs with advanced features, and direct interoperability with many deep learning frameworks such as PyTorch.  
  
Video Codec SDK, DirectX Video, Vulkan Video, and PyNvVideoCodec provide comprehensive support for GPU-accelerated video workflows. NVIDIA will continue to support these APIs, providing developers multiple options to choose from, and use the ones that best suit their needs.

| | Vulkan Video | DirectX Video | NVIDIA Video Codec SDK | PyNvVideoCodec |
| --- | --- | --- | --- | --- |
| **Platform** | Windows and Linux | Windows | Windows and Linux | Windows and Linux |
| **Benefits** | 
- Low-Level Control

- Native Vulkan Integration

- Easy for Vulkan developers

- Multi-Vendor

 | 
- Low-Level Control

- Native DirectX and Windows integration

- Easy for DirectX developers

- Multi-Vendor

 | 
- Low- and high-level control 

- Native Integration in custom pipelines

- Useful for users with less knowledge of Vulkan and DirectX

- Easy for C, C++ developers 

- NVIDIA Proprietary API

- Comprehensive feature set

 | 
- Python bindings over C++ Video Codec SDK wrapper classes

- Easy for Python developers

- NVIDIA Proprietary API

 |
| **Native API interface** | Vulkan Graphics | D3D11 (Decode only) and D3D12 | D3D9, D3D10, D3D11, D3D12 (Encode only) CUDA (Encode and decode) | CUDA (Encode and decode), PyTorch, TensorRT |

* * *

## Partners and Examples

 ![NVIDIA Partner logo - Beamr](https://developer.download.nvidia.com/images/Beamr_Logo_NVIDIA.png)

 ![NVIDIA Partner logo - BlackMagicDesign](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/gpudirect/logo-action-blackmagic.png)

 ![NVIDIA Partner logo - Comprimato](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/images-videocodec/comprimato-showcase-logo.png)

 ![NVIDIA Partner logo - DeltaCast](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/gpudirect/logo-action-deltacast.png)

 ![NVIDIA Partner logo - Fastvideo](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/images-videocodec/fastvideo-showcase-logo.png)

 ![NVIDIA Partner logo - Slussonic](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/images-videocodec/flussonic-showcase-logo.png)

 ![NVIDIA Partner logo - GCore](https://developer.download.nvidia.com/images/logo-gcore.png)

 ![NVIDIA Partner logo - Main Concept](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/mainconcept-logo.jpg)

 ![NVIDIA Partner logo - Medialooks](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/images-videocodec/medialooks-showcase-logo.png)

 ![NVIDIA Partner logo - Multicamera Systems](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/images-videocodec/multicam_logo.png)

 ![NVIDIA Partner logo - NORPIX](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/images-videocodec/norpix-showcase-logo.png)

 ![NVIDIA Example logo - GeForce Now](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/images-videocodec/gfn-showcase-logo.png)

 ![NVIDIA Partner logo - Open Broadcaster Software](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/images-videocodec/obs-showcase-logo.png)

 ![NVIDIA Partner logo - Premeier](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/images-videocodec/premiere_thumb.png)

 ![NVIDIA Partner logo - Splitmedia Labs](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/images-videocodec/logo-action-splitmedia.png)

 ![NVIDIA Partner logo - Streamline](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/images-videocodec/streamline-showcase-logo.png)

 ![NVIDIA Partner logo - Telestream](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/images-videocodec/telestream-showcase-logo.png)

 ![NVIDIA Partner logo - Visionular](https://developer.download.nvidia.com/images/logos/logo-visionular-logo-horizontal.png)

 ![NVIDIA Partner logo - Wowza](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/designworks/images-videocodec/Wowza-showcase-logo.png)

* * *

## Latest Video Codec SDK News

[See all Video Codec SDK blogs](https://developer.nvidia.com/blog/recent-posts/?products=Video+Codec+SDK)

* * *

## Resources

- 
[GPU Support Matrix](/video-encode-and-decode-gpu-support-matrix-new)

* * *

## Get started developing with Video Codec SDK.

[Get Started  
](/video-codec-sdk/download)

Quick Links

- [Get Started](/video-codec-sdk/download)
- [Support Matrix  
](/video-encode-decode-support-matrix)
- 

* * *


