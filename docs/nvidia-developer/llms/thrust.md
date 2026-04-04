# Source: https://developer.nvidia.com/thrust.md

# Thrust

 

Thrust is a powerful library of parallel algorithms and data structures. Thrust provides a flexible, high-level interface for GPU programming that greatly enhances developer productivity. Using Thrust, C++ developers can write just a few lines of code to perform GPU-accelerated sort, scan, transform, and reduction operations orders of magnitude faster than the latest multi-core CPUs. For example, the thrust::sort algorithm delivers 5x to 100x faster sorting performance than STL and TBB.

 ![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/Thrust_newlogo3.JPG)

&gt; Having access to GPU computing through the standard template interface greatly increases productivity for a wide range of tasks, from simple cashflow generation to complex computations with Libor market models, variable annuities or CVA adjustments. The Thrust C++ library has lowered the barrier of entry significantly by taking care of low-level functionality like memory access and allocation, allowing the financial engineer to focus on algorithm development in a GPU-enhanced environment.
&gt; 
&gt; Peter Decrem, Director of Rates Products, Quantifi

[Download Now](/cuda-downloads)

[Explore what’s new in the latest release...](/cuda-toolkit/whatsnew)

## Key Features

Thrust provides STL-like templated interfaces to several algorithms and data structures designed for high performance heterogeneous parallel computing:

![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/Thrustpageimage1a.png)

## Examples

The easiest way to learn Thrust is by looking at a few examples.

The example below generates random numbers on the host and transfers them to the device where they are sorted.

![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/Thrustpageimage4.png)

This second code sample computes the sum of 100 random numbers on the GPU.

![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/Thrustpageimage5.png)

## Performance

Review the latest [CUDA performance report](http://developer.download.nvidia.com/compute/cuda/compute-docs/cuda-performance-report.pdf) to learn how much you could accelerate your code.

![](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/images/libperf/rel60/Thrust.jpg)

## Availability

In addition to the Thrust open source project hosted on Github, a production-tested version of Thrust is included in the CUDA Toolkit

## Additional Resources

- [Thrust QuickStart Guide](http://docs.nvidia.com/cuda/thrust/index.html)
- [An Introduction to Thrust](http://code.google.com/p/thrust/downloads/detail?name=An%20Introduction%20To%20Thrust.pdf)
- [Using Thrust With Fortran](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/cuda/files/Using-Thrust-to-Sort-CUDA-FORTRAN-Arrays.pdf), [Watch the Webinar MP4](http://developer.download.nvidia.com/CUDA/training/ThrustonFortran.mp4)
- [Thrust 1.0 Overview Webinar](http://developer.download.nvidia.com/CUDA/training/webinarthrust1.mp4)
- [Other GPU-accelerated libraries](/gpu-accelerated-libraries)
- [Prototyping with Thrust: GTC 2010](http://www.gputechconf.com/page/gtc-on-demand.html#session2104)


