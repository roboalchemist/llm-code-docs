# Source: https://developer.nvidia.com/warp-python.md

1. [Home](https://developer.nvidia.com/)
2. [Developer Tools Catalog](/developer-tools-catalog)

NVIDIA Warp

# NVIDIA Warp

## Differentiable Spatial Computing for Python

NVIDIA Warp is an open-source developer framework for building and accelerating data generation and spatial computing in Python. Warp gives coders an easy way to write GPU-accelerated, kernel-based programs for simulation AI, robotics, and machine learning (ML). With Warp, Python developers can create GPU-accelerated, 3D simulation workflows that drive ML pipelines in PyTorch, JAX, PhysicsNeMo, and [NVIDIA Omniverse™](https://www.nvidia.com/en-us/omniverse/). Benefits include simulation performance equivalent to native CUDA® code, with the convenience and developer productivity of Python.

[Download Now  
](https://github.com/NVIDIA/warp)

## Key Features

### Kernel-Based Code

NVIDIA Warp performs a just-in-time (JIT) runtime compilation of Python functions to x86 and CUDA® kernel-level code. Kernel-based programming provides a low-level abstraction that maps closely to GPU hardware, and, in contrast to tensor-based programming, provides implicit kernel fusion (controlled by the user), fine-grained control over threads, native support for conditional logic, and sparse scatter and gather.

[Learn more](https://nvidia.github.io/warp/basics.html#kernels)

### Differentiable Programming

In addition to generating forward-mode kernel code, Warp can generate reverse-mode (adjoint) kernels that propagate the gradients of simulation results back into frameworks, such as PyTorch and JAX for network training, design optimization, and parameter estimation.

[Learn more](https://nvidia.github.io/warp/modules/differentiability.html#differentiability)

### Built for Spatial Computing

Warp includes built-in functionality to enable 3D simulation and geometry processing. In addition to a rich spatial math library, Warp provides higher-level data structures, such as meshes, hash grids, and sparse volumes (NanoVDB) for GPU-accelerated geometric queries.

[Learn more](https://nvidia.github.io/warp/modules/runtime.html#meshes)

* * *

## See NVIDIA Warp in Action

Many Python developers are using Warp today. In Omniverse, groups are using Warp for digital humans, physics simulation, and procedural animation. Warp includes several higher-level data structures that make implementing simulation and geometry processing algorithms easier.

### Meshes

Triangle meshes are ubiquitous in simulation and computer graphics. Warp provides a built-in type for managing mesh data that supports geometric queries, such as closest-point, ray-cast, and overlap checks.

### Sparse Volumes  

Sparse volumes are incredibly useful for representing grid data over large domains, such as signed distance fields (SDFs) for complex objects, or velocities for large-scale fluid flow. Warp includes support for sparse volumes defined using the NanoVDB standard.

### Hash Grids

Many particle-based simulation methods, such as the discrete element method (DEM) or smoothed particle hydrodynamics (SPH), involve iterating over spatial neighbors to compute force interactions. Hash grids are a well-established data structure to accelerate these nearest-neighbor queries and are particularly well-suited to the GPU.

 ![A quadrotor drone being simulated and controlled using NVIDIA Warp.](https://developer.download.nvidia.com/images/warp-drone.jpg)

### Robotics

In this example, Warp is used to simulate the dynamics of a quadrotor drone using the AirSim aerodynamics model. Through Warp’s differentiable simulation capabilities, users can write model-based predictive controllers (MPC) to optimize the drone’s trajectory with loss functions that take into account obstacles and target goals.

[Learn More](https://github.com/NVIDIA/warp?tab=readme-ov-file#warpexamplessim)

 ![img-aAn aerodynamic flow simulation around a vehicle using NVIDIA Warp. lt-text](https://developer.download.nvidia.com/images/warp-f1-car-aero.jpg)

### Simulation

Here, you can see Warp being used to create an incompressible flow solver for aerodynamics simulation around a vehicle. Warp provides built-in support for multidimensional arrays and sparse collision fields via NanoVDB to accurately represent the vehicle’s collision geometry.

[Learn More](https://github.com/NVIDIA/warp?tab=readme-ov-file#warpexamplescore)

 ![imgAn example of differentiable simulation for initial value alt-text](https://developer.download.nvidia.com/images/warp-training-optimization.jpg)

### Training and Optimization

We can also use Warp to solve initial value problems. Thanks to Warp’s differentiable kernels, we’re able to simulate the trajectory of the ball and obtain gradients with respect to the initial velocity. These gradients can then be used in PyTorch or JAX to optimize the trajectory and hit the target after a few seconds.

[Learn More](https://github.com/NVIDIA/warp?tab=readme-ov-file#warpexamplesoptim)

 ![A synthetic image generation pipeline written in NVIDIA Warp.](https://developer.download.nvidia.com/images/warp-sdg-cropped.jpg)

### Data Generation

Warp enables accelerated data generation and processing in Python. In this example, Warp kernels are used to generate procedural image data as part of an Omniverse [synthetic data generation](https://www.nvidia.com/en-us/use-cases/synthetic-data/) (SDG) pipeline.

[Learn More](http://docs.omniverse.nvidia.com/extensions/warp.html)

* * *

_Autodesk Research Leverages NVIDIA Warp to Accelerate Computational Fluid Dynamics on NVIDIA GPUs_
 

#### Accelerate CAE Tool Development

Warp is enabling computer-aided engineering (CAE) industry developers to accelerate physics-based CAE simulations and embrace real-time interactive design using AI-enabled digital twins. Warp gives coders an easy way to write kernel-based programs for CAE and machine learning. Warp supports PyTorch, JAX, PhysicsNeMo, and NVIDIA Omniverse.

[Learn More](https://developer.nvidia.com/topics/cae)

* * *

#### Newton, the Next-Generation Open-Source Physics Simulation Engine

Newton is an open-source, GPU-accelerated, and extensible physics engine, co-developed by Google DeepMind and Disney Research, and [managed by the Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-contribution-of-newton-by-disney-research-google-deepmind-and-nvidia-to-accelerate-open-robot-learning). Built on NVIDIA Warp and OpenUSD, Newton is optimized for robotics and compatible with learning frameworks such as MuJoCo Playground or NVIDIA Isaac Lab. [Newton Beta](https://github.com/newton-physics) is now available to use.

[Get Started on Newton](/newton-physics)

![](https://developer.download.nvidia.com/images/isaac/newton-ari.jpg)

* * *

## NVIDIA Warp On Demand Playlist

* * *

## Resources

- [Read technical blogs](https://developer.nvidia.com/blog/creating-differentiable-graphics-and-physics-simulation-in-python-with-nvidia-warp)
- [View Warp documentation](https://nvidia.github.io/warp)
- [See the GTC Talk on Warp](https://www.nvidia.com/en-us/on-demand/session/gtc24-s63345/)

- [Watch Omniverse Basics: NVIDIA Warp Overview](https://www.nvidia.com/en-us/on-demand/session/omniverse2020-om1453/)
- [Visit the developer forums](https://github.com/NVIDIA/warp/issues)
- [Explore NVIDIA Deep Learning Institute (DLI) training](https://www.nvidia.com/en-us/training/)

Visit Github to download the latest version of NVIDIA Warp software.

[Download Now](https://github.com/NVIDIA/warp)


