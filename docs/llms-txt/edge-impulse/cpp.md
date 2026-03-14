# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/inference/linux/cpp.md

# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/inference/cpp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# C++ SDK

The C++ inferencing SDK is a portable library for digital signal processing and machine learning inferencing, and it contains native implementations for both processing and learning blocks in Edge Impulse. It is written in C++11 with all dependencies bundled, and can be built on both desktop systems and on microcontrollers. The SDK is located on GitHub: [edgeimpulse/inferencing-sdk-cpp](https://github.com/edgeimpulse/inferencing-sdk-cpp).

## Using the SDK

The easiest way of developing against the SDK is to use the **Deployment** page in the Edge Impulse studio. Deploying your impulse bundles all blocks, configuration and the SDK into a single package. To run the deployed package on your machine or embedded device, see the [Deployments](/hardware/deployments) tutorials.

## Hardware-optimized code

The SDK contains an implementation of all algorithms in software, but you can optionally output hardware-optimized code. For example, on Cortex-M microcontrollers we leverage CMSIS-DSP to optimize certain vector operations. These optimizations are selected at compile time in `config.hpp`, and mostly live in `numpy.hpp`. If you want to add optimizations for a new target this would be a good place to start. We welcome contributions!


Built with [Mintlify](https://mintlify.com).