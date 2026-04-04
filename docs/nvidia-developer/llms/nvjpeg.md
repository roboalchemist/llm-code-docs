# Source: https://developer.nvidia.com/nvjpeg.md

Learn from the best in the field with our exclusive computer vision speaker series. [Register now](https://www.nvidia.com/en-us/events/computer-vision-speaker-series/?nvid=nv-int-unbr-911558) for free! 

  

# nvJPEG Libraries 

## GPU-accelerated JPEG decoder, encoder and transcoder 

The nvJPEG library is a high-performance GPU-accelerated library for decoding, encoding and transcoding JPEG format images. The nvJPEG2000 library is for decoding JPEG 2000 format images. Applications that rely on nvJPEG or nvJPEG2000 for decoding deliver higher throughput and lower latency compared to CPU-only decoding.

  

## nvJPEG 

The nvJPEG library provides low-latency decoding, encoding, and transcoding for common JPEG formats used in computer vision applications such as image classification, object detection and image segmentation.

  

### nvJPEG Key Features 

- Hybrid decoding using both the CPU and the GPU 
- Hardware acceleration for baseline JPEG decode on A100 GPUs 
- Single image and batched image decoding 
- Single phase and multiphase decoding 
- Color space conversion to RGB, BGR, RGBI, BGRI, and YUV 
- Input to the library is in the host memory, and the output is in the GPU memory 
- User-provided memory manager for the device and pinned host memory allocations 

### Get Started with nvJPEG 

- For the most current version of nvJPEG, download the [CUDA Toolkit](/cuda-toolkit). 
- If you are using CUDA Toolkit 10.0 or 9.0, please download the [nvJPEG installer](/nvjpeg-release-download). 
- [nvJPEG Documentation](https://docs.nvidia.com/cuda/nvjpeg/index.html)
- [nvJPEG Examples](https://github.com/NVIDIA/CUDALibrarySamples) on GitHub 
- Technical Blog: [Leveraging the Hardware JPEG Decoder and NVIDIA nvJPEG Library on NVIDIA A100 GPUs](https://developer.nvidia.com/blog/leveraging-hardware-jpeg-decoder-and-nvjpeg-on-a100/)

  

* * *

## nvJPEG Performance 

### Decoding Speed with Multiple Threads 
 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/fhd.png)

Speed up achieved by hardware decode on A100 compared to CUDA decode on V100 and CPU only decode.

CPU: Intel Xeon Platinum 8168@2GHz 3.7GHz Turbo (Skylake) HT On

### Encoding Speed 
 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/baseline.png)

JPEG Baseline encoding throughput comparison between CPU, and V100 and A100 GPUs for common image sizes and formats.

CPU: Intel Xeon Platinum 8168@2GHz 3.7GHz Turbo (Skylake) HT On

  
 
* * *

## nvJPEG2000 

The nvJPEG2000 library is for application developers and researchers who are employing JPEG 2000 formatted images in their research in fields such as deep learning, medical imaging, digital pathology, remote sensing and digital cinema applications. nvJPEG2000 reads and decodes JPEG 2000 format image data from CPU memory. The decoded output is in GPU memory. The library relies on both CPU and GPU for decoding.

  

### nvJPEG2000 Key Features 

- Output formats: grayscale and color images with arbitrary width and height 
- Compression Technique: Lossy (wavelet CDF 9/7) and lossless (wavelet CDF 5/3) image compression and decompression 
- jp2 file format and jpeg2000 code stream are supported 

### Get Started with nvJPEG2000 

[Download](/nvjpeg2000-downloads)

- [nvJPEG2000 Documentation](https://docs.nvidia.com/cuda/nvjpeg2000/index.html)
- [nvJPEG2000 Examples](https://github.com/NVIDIA/CUDALibrarySamples) on GitHub 

  
 
* * *

## nvJPEG2000 Performance 
  

### 4x Faster Lossless Decoding 
 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/lossless_updated.png)

Lossless: 5-3 wavelet transform

CPU: Intel Xeon Gold 6240@2GHz 3.9GHz Turbo (Cascade Lake) HT On

### 7X Faster Lossy Decoding 
 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/lossy_updated.png)

Lossy: 9-7 wavelet transform

CPU: Intel Xeon Gold 6240@2GHz 3.9GHz Turbo (Cascade Lake) HT On

  

* * *

## Resources 
  

- Technical Blog: [Leveraging the Hardware JPEG Decoder and NVIDIA nvJPEG Library on NVIDIA A100 GPUs](https://developer.nvidia.com/blog/leveraging-hardware-jpeg-decoder-and-nvjpeg-on-a100/)
- Related libraries and software: 
  - [NVIDIA Data Loading Library (DALI)](/DALI)
  - [NVIDIA Performance Primitives (NPP)](/npp)
  - [NVIDIA GPU Cloud](https://ngc.nvidia.com/catalog/collections)

- For questions or feedback, please contact [nvjpeg@nvidia.com](mailto:nvjpeg@nvidia.com)
- To make a feature request or report an issue, register on [NVIDIA Developer Zone](/developer-program)

  

### Join the Developer Program 
  

[Join Now](/developer-program)


