# Source: https://developer.nvidia.com/cuda-qx.md

# NVIDIA CUDA-QX

Quantum researchers and developers across a wide range of domains, from quantum error correction to hybrid solvers, use GPU programming to accelerate their applications. This demands highly optimized, domain-specific libraries. NVIDIA CUDA-QX, built on top of CUDA-Q™, is a collection of libraries and tools for accelerating research and development toward useful accelerated quantum supercomputing.

[Get Started](http://www.github.com/NVIDIA/cudaqx)

 ![Quantum Computing Stacked Diagram](https://developer.download.nvidia.com/images/cuda/quantum-computing-diagram-sc24.jpg)
* * *

## CUDA-QX Libraries

CUDA-QX libraries are built on top of [CUDA-Q](https://developer.nvidia.com/cuda-q), NVIDIA’s open-source, hardware-agnostic platform for accelerated quantum supercomputing, and are also released open-source on GitHub. The CUDA-QX libraries provide optimized implementations of key quantum primitives—from quantum error correction to hybrid algorithms—enabling developers to easily leverage the CUDA-Q platform.

### CUDA-Q QEC

CUDA-Q QEC, which includes GPU-accelerated decoding primitives, Google’s stim stabilizer simulator, and extension points in CUDA-Q for custom decoders, is the foundational toolkit for any error correction researcher.

[Learn More About CUDA-Q QEC](https://nvidia.github.io/cudaqx/components/qec/introduction.html)

### CUDA-Q Solvers

Run prebuilt optimized kernels for VQE, ADAPT-VQE, QAOA, GQE, and more to get the most performance out of today’s hardware.

[Learn More About CUDA-Q Solvers](https://nvidia.github.io/cudaqx/components/solvers/introduction.html)

* * *

## Performance

### Single Syndrome Decoding Latency

 ![](https://developer.download.nvidia.com/images/cuda-qx/single-syndrome-decoding-latency.svg)

### Batched Decoding Throughput

 ![](https://developer.download.nvidia.com/images/cuda-qx/batched-decoding-throughput.svg)

Belief Propagation-Ordered Statistics Decoding (BP-OSD) is one of the most promising approaches for scalable quantum error correction. CUDA-Q QEC accelerates BP-OSD with state-of-the-art latency and throughput, offering a 29–35x speedup over industry standard decoders for a single shot, as well as an additional speedup of up to 42x for high-throughput use cases where many syndromes need to be decoded at once.

* * *

## Latest Product News

### Introducing NVIDIA CUDA-QX Libraries for Accelerated Quantum Supercomputing

Learn how the CUDA-QX libraries can accelerate the development of hybrid applications, ranging from quantum error correction to chemical simulation.

[Learn More About CUDA-QX Libraries](https://developer.nvidia.com/blog/introducing-nvidia-cuda-qx-libraries-for-accelerated-quantum-supercomputing/)

### NVIDIA and QuEra Decode Quantum Errors with AI

Learn how researchers will boost magic state fidelity and accelerate QEC research with NVIDIA AI Decoder, a transformer based AI decoder.

[Learn More About AI Decoder  
](https://developer.nvidia.com/blog/?p=97001&amp;preview=1&amp;_ppp=e793b2b0ef)

### Accelerating Quantum Error Correction Research With NVIDIA Quantum

Learn how CUDA-Q QEC features like an advanced BP+OSD decoder implementation, integration with Infleqtion’s qLDPC code library, and CUDA-Q’s accelerated noisy simulator help streamline quantum error correction research.

[Learn More About QEC   
](https://developer.nvidia.com/blog/accelerating-quantum-error-correction-research-with-nvidia-quantum/)

* * *

Get Started With CUDA-QX Today.

[Get Started](http://www.github.com/NVIDIA/cudaqx)


