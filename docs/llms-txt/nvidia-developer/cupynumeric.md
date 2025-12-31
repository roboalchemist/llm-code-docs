# Source: https://developer.nvidia.com/cupynumeric.md

1. [Home](https://developer.nvidia.com/)

NVIDIA cuPyNumeric

# NVIDIA cuPyNumeric  

**NumPy and SciPy on Multi-Node Multi-GPU Systems**  
  
cuPyNumeric is a multi-node, multi-GPU array computing library that implements the NumPy API on top of Legate, bringing accelerated computing to the Python scientific community.  
  
**Python** is a powerful and user-friendly programming language widely adopted by researchers and scientists for data science, machine learning (ML), and productive numerical computing. **NumPy**  is the de facto standard for math and matrix libraries, providing a simple and easy-to-use programming model with interfaces that correspond closely to the mathematical needs of scientific applications.  
  
As data sizes and computational complexities grow, CPU-based Python and NumPy programs need help meeting the speed and scale demanded by cutting-edge research.  
  
Distributed accelerated computing offers the infrastructure to efficiently solve and test hypotheses in data-driven problems. Whether analyzing data from high-energy electron beams, solving complex computational fluid dynamics problems, or building ML models, researchers are increasingly seeking ways to scale their programs.  
  
With cuPyNumeric, you can take your existing NumPy workflows and seamlessly scale them from a single CPU to a single GPU, and up to thousands of GPUs across a multi-node, multi-GPU cluster, without changing your code. This powerful scaling enables you to focus on your research and discovery, not on complex code modifications for different hardware environments.  
  
Download the latest beta release of cuPyNumeric today.

The cuPyNumeric project is independent of the CuPy project. CuPy is a trademark of Preferred Networks, Inc, and the name ‘cuPyNumeric’ is used with their permission.

[Download Now  
](https://github.com/nv-legate/cunumeric &quot;Download Now on GitHub&quot;)

* * *

## Legate  

Legate is an abstraction layer that runs on top of the CUDA® runtime system, together providing scalable implementations of popular domain-specific APIs. NVIDIA cuPyNumeric layers on top of Legate, like many other libraries.  
  
Legate democratizes computing by making it possible for all programmers to leverage the power of large clusters of CPUs and GPUs by running the same code that runs on a desktop or a laptop at scale. Using this technology, scientists and researchers can develop and test programs on moderately sized datasets on local machines and then immediately scale up to larger datasets deployed on many nodes in the cloud or on a supercomputer without any code modifications.

[Getting Started With Legate](https://developer.nvidia.com/legate)
* * *

## Key Benefits  

The NVIDIA cuPyNumeric library on Legate:

- 

Supports native Python language and NumPy interface without constraints

- 

Transparently accelerates and scales existing NumPy workflows

- 

Provides a seamless drop-in replacement for NumPy

- 

Provides automatic parallelism and acceleration for multiple nodes across CPUs and GPUs

- 

Scales from one CPU up to thousands of GPUs optimally 

- 

Requires little to no code changes, allowing faster completion of scientific tasks 

- 

Is freely available. Get started with the [installation guide](https://docs.nvidia.com/cupynumeric/latest/installation.html) and [tutorial](https://github.com/NVIDIA/accelerated-computing-hub/blob/main/Accelerated_Python_User_Guide/notebooks_v1/Chapter_11_Distributed_Computing_cuPyNumeric.ipynb).

* * *

## cuPyNumeric Performance

![Weak Scaling of Richard-Lucy Devonvolution on NVIDIA DGX SuperPOD](https://developer.download.nvidia.com/images/nvidia-cunumeric-vs-cupy-2c50-d.svg)
_Weak Scaling of Richard-Lucy Deconvolution on DGX SuperPOD_

#### Processing 10TB Microscopy Image Data as a Single NumPy Array  

This multi-view lattice light-sheet microscopy example produces tens of terabytes (TB) of raw image data per day. Up until now, all processing has happened offline, after all the data has been collected. By moving all the preprocessing and reconstruction operations to GPUs and using cuPyNumeric on Legate, the data can be visualized in real time as it’s processed.

Get started with cuPyNumeric today.

[Download Now  
](https://github.com/nv-legate/cunumeric#installation &quot;Download Now on GitHub&quot;)


