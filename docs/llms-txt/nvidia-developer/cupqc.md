# Source: https://developer.nvidia.com/cupqc.md

1. [Home](/)

NVIDIA cuPQC

# NVIDIA cuPQC  

**NVIDIA cuPQC** is an SDK of optimized libraries for implementing GPU-accelerated Post-Quantum Cryptography (PQC) workflows—especially crucial in high-throughput data environments.

[Download Now](/cupqc-download/)

* * *

## Key Features

### Crypto Agility With NIST Algorithms

cuPQC achieves breakthrough performance on the NIST finalist algorithms ML-KEM and ML-DSA, with the flexibility to easily add future algorithms.

### High Performance

Accelerates NIST ML-KEM Keygen, Encapsulation and Decapsulation by 143x, 99x, and 84x, respectively over a state-of-the-art CPU.

### Comprehensive Cryptographic Primitives  

Offers a robust set of cryptographic primitives, enabling developers to implement advanced cryptographic schemes with flexibility and performance.

### Broad GPU Platform Support  

cuPQC offers a high-performance transition to PQC, optimized for diverse GPU platforms—from embedded platforms like NVIDIA Jetson™ to data center-scale platforms.

### Adopted by the Global Cryptography Ecosystem

Used by leading cryptographic developers, cloud service providers, and leading security startups. Available through the open-source library liboqs.

### Side-Channel Secure  

GPU-tailored code is secured against state-of-the-art microarchitectural and timing attacks.

* * *

## Primitives  

cuPQC offers a suite of sub-libraries (primitives) designed to accelerate cryptographic schemes.

### Cryptographic Hash

The Cryptographic Hash library accelerates cryptographic hash functions using GPU technology, providing implementations of widely used algorithms such as SHA-2, SHA-3, SHAKE, and Poseidon 2. Additionally, the library offers the capability to efficiently calculate Merkle Trees. With the Cryptographic Hash library, you can achieve significant performance improvements, making it ideal for applications that require fast and secure cryptographic protocols. Use cases include data integrity checks, digital signatures, proofs of membership, and hash-based signatures.

* * *

## Performance—Accelerating Leading PQC Algorithms  

ML-KEM is the finalist for key exchange standardized by NIST in August 2024. cuPQC achieves throughputs of up to 13.3 million keygen/s, 9.3 million encapsulations/s, and 8 million decapsulations/s for batched ML-KEM-768 on a single H100 SXM5 GPU, increases of 143x, 99x, and 84x, respectively over a state-of-the-art CPU.

![A chart showing up to 140X speedup on ML-KEM-768 primitives](https://developer.download.nvidia.com/images/cuPQC-algorithms-performance.svg)
_Performed on an NVIDIA H100. Measured in terms of throughput and operations per second, using a batch size of 1,000,000._

* * *

##   

 ![Post-Quantum Cryptography (PQC) Alliance logo](https://developer.download.nvidia.com/images/pqca.svg)

NVIDIA is a founding member of the PQC Alliance, a Linux Foundation consortium which aims to advance the adoption of PQC by producing high-assurance software implementations of standardized algorithms.

* * *

## Latest Product News

* * *

## Partners Adopting NVIDIA cuPQC

“cuPQC’s safe and high-performance algorithms make transitioning to post-quantum cryptography achievable for enterprises with high-throughput security applications”  
  
- Hart Montgomery, Linux Foundation

 ![NVIDIA cuPQC Partner - Evolution](https://developer.download.nvidia.com/images/cupqc/evolutionq-logo.svg)

 ![NVIDIA cuPQC Partner - Open Quantum Safe](https://developer.download.nvidia.com/images/cupqc/open-quantum-safe-logo.svg)

 ![NVIDIA cuPQC Partner - PQShield](https://developer.download.nvidia.com/images/cupqc/pq-shield-logo.svg)

 ![NVIDIA cuPQC Partner - QuSecure](https://developer.download.nvidia.com/images/cupqc/qusecure-logo.svg)

 ![NVIDIA cuPQC Partner - Sandbox AQ](https://developer.download.nvidia.com/images/cupqc/sandbox-aq-logo.svg)

* * *

## Resources

- 
[Documentation: Library](https://docs.nvidia.com/cuda/cupqc/index.html)
- 
[Make It So: Software Speeds Journey to Post-Quantum Cryptography](https://blogs.nvidia.com/blog/cupqc-quantum-cryptography/)

- 
[Feedback](mailto:cuPQC-Libs-Feedback@nvidia.com)
- 
[Quantum Computing Glossary Page](https://www.nvidia.com/en-us/glossary/quantum-computing/)


