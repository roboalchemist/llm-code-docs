# Source: https://developer.nvidia.com/curand.md

# cuRAND

 
## Random Number Generation on NVIDIA GPUs

[DOWNLOAD](/hpc-sdk)[DOCUMENTATION](http://docs.nvidia.com/cuda/curand/index.html)[SAMPLES](http://github.com/nvidia/cudalibrarysamples)[SUPPORT](https://forums.developer.nvidia.com/c/accelerated-computing/gpu-accelerated-libraries/12)[FEEDBACK](mailto:Math-Libs-Feedback@nvidia.com?subject=cuRand%20Feedback)

The NVIDIA CUDA Random Number Generation library (cuRAND) delivers high performance GPU-accelerated random number generation (RNG).  The cuRAND library delivers high quality random numbers 8x faster using hundreds of processor cores available in NVIDIA GPUs. The cuRAND library is included in both the [NVIDIA HPC SDK](/hpc-sdk) and the [CUDA Toolkit](/cuda-downloads).

[Explore what’s new in the latest release...](/cuda-toolkit/whatsnew)

Review the latest [CUDA performance report](http://developer.download.nvidia.com/compute/cuda/compute-docs/cuda-performance-report.pdf) to learn how much you could accelerate your code.

* * *

### cuRAND Performance 

cuRAND also provides two flexible interfaces, allowing you to generate random numbers in bulk from host code running on the CPU or from within your CUDA functions/kernels running on the GPU.  A variety of RNG algorithms and distribution options means you can select the best solution for your needs.

### cuRAND Key Features 

- **Flexible usage model**
  - Host API for generating random numbers in bulk on the GPU 
  - Inline implementation allows use inside GPU functions/kernels, or in your host code 

- **Four high-quality RNG algorithms**
  - MRG32k3a 
  - MTGP Merseinne Twister 
  - XORWOW pseudo-random generation 
  - Sobol’ quasi-random number generators, including support for scrambled and 64-bit RNG 

- **Multiple RNG distribution options**
  - Uniform distribution 
  - Normal distribution 
  - Log-normal distribution 
  - Single-precision or double-precision 
  - Poisson distribution 

[![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/curandcallout.JPG)](/nvidia-gpu-computing-documentation#cuRAND)

The random number generators and statistical distributions provided in the cuRAND library have been tested against well-known statistical test batteries, including TestUO1. Please see the cuRAND documentation for selected test results.

### cuRAND Availability 

The cuRAND library is freely available as part of the [NVIDIA HPC SDK](https://developer.nvidia.com/hpc-sdk). It is also included with the [CUDA Toolkit](http://www.nvidia.com/getcuda).   
 For more information on cuRAND and other CUDA math libraries:

- Source code examples demonstrating how to use the cuRAND library: 
  - [CUDA C Monte Carlo: Single Asian Option](http://docs.nvidia.com/cuda/cuda-samples/index.html#monte-carlo-single-asian-option)
  - [CUDA C Monte Carlo Estimation of Pi (batch QRNG)](http://docs.nvidia.com/cuda/cuda-samples/index.html#monte-carlo-estimation-of-pi--batch-qrng-)
  - [CUDA C Monte Carlo Estimation of Pi (batch PRNG)](http://docs.nvidia.com/cuda/cuda-samples/index.html#monte-carlo-estimation-of-pi--inline-prng-)
  - [CUDA C Monte Carlo Estimation of Pi (batch inline QRNG)](http://docs.nvidia.com/cuda/cuda-samples/index.html#monte-carlo-estimation-of-pi--batch-inline-qrng--)
  - [CUDA C Monte Carlo Estimation of Pi (inline PRNG)](http://docs.nvidia.com/cuda/cuda-samples/index.html#monte-carlo-estimation-of-pi--inline-prng-)

- [Additional GPU-accelerated libraries](/gpu-accelerated-libraries)

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/curand_perf_A100-PCIE-40GB_455.23.05_11.3.27_10.2.4.27_f64_light.svg)  
  
  
 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/curand_perf_A100-PCIE-40GB_455.23.05_11.3.27_10.2.4.27_f32_light.svg)


