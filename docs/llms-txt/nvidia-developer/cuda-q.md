# Source: https://developer.nvidia.com/cuda-q.md

# NVIDIA CUDA-Q

NVIDIA CUDA-Q™ is the quantum processing unit (QPU)-agnostic platform for [accelerated quantum supercomputing](https://developer.nvidia.com/blog/an-introduction-to-quantum-accelerated-supercomputing/).

[Get Started](https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html)

* * *

## How CUDA-Q Works

CUDA-Q is an open-source quantum development platform that orchestrates the hardware and software needed to run useful, large-scale [quantum computing](https://www.nvidia.com/en-us/glossary/quantum-computing/) applications. The platform’s hybrid programming model allows computation on GPU, CPU, and QPU resources in tandem from within a single quantum program. CUDA-Q is “qubit-agnostic”—seamlessly integrating with all QPUs and qubit modalities and offering GPU-accelerated simulations when adequate quantum hardware isn’t available. 

CUDA-Q extends far beyond the NISQ-era, charting a course to large-scale, error-corrected quantum supercomputing with libraries, tools, infrastructure, and a hybrid programming model built for the future of quantum computing. Under the hood, CUDA-Q can be interchangeably powered by industry-leading simulators or actual quantum processors from a growing list of vendors. Both of these engines can leverage AI supercomputing, whether to GPU-accelerate simulations or control and enhance QPU operations.

 ![A diagram showing how CUDA-Q works](https://developer.download.nvidia.com/images/cuda-q/cuda-q-diagram.jpg)
* * *

## Key Features

![Decorative icon](https://developer.download.nvidia.com/icons/m48-binaries.svg)

### Simplify Development of Hybrid Quantum-Classical Applications  

The kernel-based programming model makes it easy to write a hybrid application once and run it on multiple QPU and simulation backends.

![Decorative icon](https://developer.download.nvidia.com/icons/m48-scalability-up-sample.svg)

### Run Quantum Simulations at Scale  

Powerful state vector, tensor networks, and noisy simulators can accelerate your applications with GPUs.

![Decorative icon](https://developer.download.nvidia.com/icons/m48-simulations.svg)

### Simulate Quantum Systems  

Accelerated simulation of the time evolution of dynamic systems, noise modeling, and quantum error correction (QEC) tools allow QPU builders to design fault-tolerant systems.

![Decorative icon](https://developer.download.nvidia.com/icons/m48-app-development-cycle.svg)

### Write Once, Run Everywhere  

CUDA-Q is QPU agnostic and integrates with 75% of publicly available QPUs. Write your code once and run on all qubit modalities.

![Decorative icon](https://developer.download.nvidia.com/icons/m48-scaling-cuda-c++.svg)

### Use Familiar Tools  

Use Python or C++ to describe your algorithm in a high-level language. The CUDA-Q compiler will lower and optimize the code based on the backend, using industry tools such as Multi-Level Intermediate Representation (MLIR), Low Level Virtual Machine (LLVM), and Quantum Intermediate Representation (QIR).

![Decorative icon](https://developer.download.nvidia.com/icons/m48-well-being-crs-collabration.svg)

### Be Part of the Community  

CUDA-Q is an open-source project and is part of the quantum community. It interops with AI and high-performance computing (HPC) libraries and visualization tools. 

* * *

## Built for Performance

NVIDIA CUDA-Q enables the straightforward execution of hybrid code on many different types of quantum processors, simulated or physical. Researchers can use the cuQuantum-accelerated simulation backends or QPUs from our partners or connect their own simulator or quantum processor.

### GPU Advantage

CUDA-Q quantum algorithm simulations can achieve a speedup of up to 180x over a leading CPU, as well as scaling of the number of qubits with low overhead in GPU time.

 ![A chart showing CUDA-Q GPU speedup performance over CPU](https://developer.download.nvidia.com/images/cuda-q/gpu-advantage.jpg)
### Multiple GPU Scaling  

Multiple GPUs can scale the performance of quantum algorithm simulations by more than 300x.

 ![Multiple GPUs can scale a quantum algorithm beyond today’s quantum devices](https://developer.download.nvidia.com/images/cuda-q/quantum-computing-cuda-q-multiple-gpu-scaling-chart.jpg)
* * *

## Starter Kits

### Optimization

Understand and solve the Max-Cut optimization problem with the Quantum Approximate Optimization Algorithm (QAOA).

- 

[Read the QAOA paper](https://arxiv.org/abs/1411.4028). 

- 

Learn about CUDA-Q [optimizers](https://nvidia.github.io/cuda-quantum/latest/examples/python/optimizers_gradients.html) and use the [observe](https://nvidia.github.io/cuda-quantum/latest/examples/python/executing_kernels.html#Observe)function.

- 

[Run the Max-Cut notebook](https://nvidia.github.io/cuda-quantum/latest/applications/python/qaoa.html).

### Quantum Error Correction

Learn how to do quantum error correction with CUDA-Q.

- 

[Read the blog about CUDA-Q QEC.](https://developer.nvidia.com/blog/accelerating-quantum-error-correction-research-with-nvidia-quantum/)

- 

[Explore CUDA-Q QEC documentation](https://nvidia.github.io/cudaqx/components/qec/introduction.html#).

- 

[Run the QEC examples](https://nvidia.github.io/cudaqx/examples_rst/qec/examples.html).

### Dynamic Simulation  

Learn about the dynamics capabilities in CUDA-Q.

- 

[Read the blog that introduces the dynamics capabilities.](https://developer.nvidia.com/blog/accelerating-googles-qpu-development-with-new-quantum-dynamics-capabilities/)

- 

[Read CUDA-Q dynamics documentation](https://nvidia.github.io/cuda-quantum/latest/using/backends/dynamics.html#).

- 

[Explore different qubit modalities’ examples of system time evolution. examples.](https://github.com/NVIDIA/cuda-quantum/tree/742a31dee48f7fa6a9d274528f6f2875c6312f7b/docs/sphinx/examples/python/dynamics)

* * *

## Use Cases

### Fault-Tolerant Qubits  

Infleqtion demonstrated error-corrected, logical qubits using neutral atoms.

- 

[Read the “NVIDIA CUDA-Q Runs Breakthrough Logical Qubit Application on Infleqtion QPU” blog](https://developer.nvidia.com/blog/nvidia-cuda-q-runs-breakthrough-logical-qubit-application-on-infleqtion-qpu/).

- 

[Read the paper](https://arxiv.org/pdf/2412.07670).

- 

[View the implementation](https://nvidia.github.io/cuda-quantum/latest/applications/python/logical_aim_sqale.html).

### AI for Algorithm Design

The University of Toronto developed the Generative Quantum Eigensolver—a new class of quantum algorithms that uses AI to improve performance.

- 

[Read the “Advancing Quantum Algorithm Design With GPTs” blog](https://developer.nvidia.com/blog/advancing-quantum-algorithm-design-with-gpt/).

- 

Read the paper.

### Solar Energy Prediction  

The Chung Yuan Christian University developed a quantum neural network model for solar irradiance forecasting, showing faster training and improved performance.

- 

[Read the “Accelerating Quantum Algorithms for Solar Energy Prediction With NVIDIA CUDA-Q and NVIDIA cuDNN” blog](https://developer.nvidia.com/blog/accelerating-quantum-algorithms-for-solar-energy-prediction-with-nvidia-cuda-q-and-nvidia-cudnn/).

- 

Read the paper.

### Divisive Clustering

The University of Edinburgh developed a method of finding data patterns and clustering big data so it can be used in quantum computers.

- 

[Read the “CUDA-Q Enabled Resource Reduction for Quantum Clustering Algorithms” blog](https://developer.nvidia.com/blog/cuda-q-enabled-resource-reduction-for-quantum-clustering-algorithms/).

- 

[View the implementation](https://nvidia.github.io/cuda-quantum/latest/applications/python/divisive_clustering_coresets.html).

- 

[Read the paper](https://arxiv.org/pdf/2402.01529).

### Molecular Generation

Yale University developed a hybrid transformer with a quantized self-attention mechanism applied to molecular generation.

- 

[View the implementation](https://nvidia.github.io/cuda-quantum/latest/applications/python/quantum_transformer.html).

- 

[Read the paper](https://arxiv.org/abs/2502.19214).

### Circuit Synthesis

The University of Innsbruck used diffusion models to synthesize arbitrary unitaries into CUDA-Q kernels.

- 

[View the implementation](https://nvidia.github.io/cuda-quantum/latest/applications/python/unitary_compilation_diffusion_models.html).

- 

[Read the paper](https://www.nature.com/articles/s42256-024-00831-9).

* * *

## CUDA-Q Learning Resources

### CUDA-Q Documentation  

Browse [documentation](https://nvidia.github.io/cuda-quantum/latest/index.html) for the latest version of CUDA-Q.

### CUDA-Q Application Hub  

Run Python notebooks of real-life [applications](https://nvidia.github.io/cuda-quantum/latest/using/tutorials.html) showing the power of CUDA-Q.

### CUDA-Q Repo  

Visit the CUDA-Q GitHub [repository](https://github.com/NVIDIA/cuda-quantum) to contribute code and create issues.

### CUDA-QX Libraries  

Explore domain-specific CUDA-Q [libraries](https://nvidia.github.io/cudaqx/index.html) for QEC and solvers.

### CUDA-Q Academic  

Explore [CUDA-Q Academic](https://github.com/NVIDIA/cuda-q-academic) materials, including self-paced Jupyter notebook modules for building and optimizing hybrid quantum-classical algorithms using CUDA-Q.

### Quick-Start to Accelerated Quantum Supercomputing  

Watch a [hands-on session](https://www.nvidia.com/en-us/on-demand/session/gtcdc25-dct51159/?playlistId=gtcdc25-quantum-computing-and-hpc) and explore [the code](https://github.com/NVIDIA/cuda-q-academic/tree/2025-GTC-DC/workshops/2025-GTC-DC) to learn how to use CUDA-Q to bring together quantum algorithms with machine learning and generative AI to elevate quantum computing.

* * *

## Latest CUDA-Q News

* * *

## CUDA-Q Ecosystem

CUDA-Q is accelerating work across the quantum computing ecosystem, including partner integrations that range from building and controlling better quantum hardware to developing the first useful quantum algorithms.

 ![Quantum Computing Partner - Agnostiq](https://developer.download.nvidia.com/images/logos/agnostic.png)

 ![Quantum Computing Partner - Alice &amp; Bob](https://developer.download.nvidia.com/images/cuda/alice-bob-logo.svg)

 ![Quantum Computing Partner - Anyon Technologies](https://developer.download.nvidia.com/images/logos/anyon-technologies.png)

 ![Quantum Computing Partner - Aqarios](https://developer.download.nvidia.com/images/logos/aqarios-logo.svg)

 ![Quantum Computing Partner - Atlantic Quantum](https://developer.download.nvidia.com/images/logos/atlantic-quantum.png)

 ![Quantum Computing Partner - Atom Computing](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/atom-computing-logo.svg)

 ![Quantum Computing Partner - Diraq](https://developer.download.nvidia.com/images/logos/diraq.png)

 ![Quantum Computing Partner - Equal1](https://developer.download.nvidia.com/images/logos/equal1.png)

 ![Quantum Computing Partner - Fermioniq](https://developer.download.nvidia.com/images/logos/ferminiq.png)

 ![Quantum Computing Partner - IonQ](https://developer.download.nvidia.com/images/logos/logo-infleqtion.svg)

 ![Quantum Computing Partner - IonQ](https://developer.download.nvidia.com/images/cuda/ionq-logo.svg)

 ![Quantum Computing Partner - IQM](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/iqm-logo@2x.png)

 ![Quantum Computing Partner - QuEra Computing](https://developer.download.nvidia.com/images/cuda/quera-logo.svg)

 ![Quantum Computing Partner - Orca Computing](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/orca-computing-logo.svg)

 ![Quantum Computing Partner - Oxford Quantum Circuits](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/oqc-logo.svg)

 ![Quantum Computing Partner - Pasqal](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/pasqal-logo@2x.png)

 ![Quantum Computing Partner - PlanQC](https://developer.download.nvidia.com/images/logos/planqc-logo.svg)

 ![Quantum Computing Partner - qBraid](https://developer.download.nvidia.com/images/cuda/qbraid-logo.svg)

 ![Quantum Computing Partner - Quantum Circuits Inc](https://developer.download.nvidia.com/images/logos/qci.svg)

 ![Quantum Computing Partner - QC Ware](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/qc-ware-logo@2x.png)

 ![Quantum Computing Partner - QPerfect](https://developer.download.nvidia.com/images/logos/qperfect-logo.svg)

 ![Quantum Computing Partner - Quandela](https://developer.download.nvidia.com/images/logos/quandela-logo.svg)

 ![Quantum Computing Partner - Quantnuum](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/quantinuum-logo@2x.png)

 ![Quantum Computing Partner - Orca Computing](https://developer.download.nvidia.com/images/logos/quantum-art%20-logo.svg)

 ![Quantum Computing Partner - Quantum Brilliance](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/quantum-brilliance-logo@2x.png)

 ![Quantum Computing Partner - Quantum Machines](https://developer.download.nvidia.com/images/cuda/quantum-machines-logo.svg)

 ![Quantum Computing Partner - Qudora](https://developer.download.nvidia.com/images/logos/qudora-logo.svg)

 ![Quantum Computing Partner - Qubly](https://developer.download.nvidia.com/images/logos/quobly-logo.svg)

 ![Quantum Computing Partner - Rigetti](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/rigetti-logo@2x.png)

 ![Quantum Computing Partner - SEEQC](https://developer.download.nvidia.com/images/cuda/seeqc-logo.svg)

 ![Quantum Computing Partner - Terra Quantum](https://developer.download.nvidia.com/images/cuda/terra-quantum-logo.svg)

* * *

## More Resources

 ![](https://developer.download.nvidia.com/images/omniverse/m48-people-group.svg)
### Explore the Community

 ![](https://developer.download.nvidia.com/images/isaac/m48-ai-startup-256px-blk.png)
### Accelerate Your Startup

 ![](https://developer.download.nvidia.com/icons/m48-email-settings.svg)
### Sign Up for our Developer Newsletter

* * *

## Get started with CUDA-Q today.  

[Get Started](https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html)


