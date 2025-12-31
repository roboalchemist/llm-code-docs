# Source: https://developer.nvidia.com/cuequivariance.md

1. [Topics](/topics)

NVIDIA cuEquivariance

# NVIDIA cuEquivariance

cuEquivariance is a CUDA-X™ library specifically designed to tackle the demanding computational requirements of geometry-aware neural networks, which are essential for tasks involving 3D data. cuEquivariance provides optimized NVIDIA CUDA® kernels and comprehensive APIs, including those for triangle attention and triangle multiplication, to accelerate such processes across various scientific domains, including drug and material discovery.

[Download Now](https://github.com/NVIDIA/cuEquivariance?tab=readme-ov-file)[Documentation](https://docs.nvidia.com/cuda/cuequivariance/)

* * *

## Key Features

### Flexible API

Alternative equivariance libraries are bound to a specific choice of SO(3) [irreps basis](https://docs.nvidia.com/cuda/cuequivariance/api/generated/cuequivariance.Irrep.html) and data layout. With cuEquivariance, you can specify your own irreps basis tensor product by creating a [segmented tensor product](https://docs.nvidia.com/cuda/cuequivariance/tutorials/stp.html), and generalize such operations beyond irreps to build equivariant neural networks.

### CUDA-Accelerated Performance

Achieve up to:

- 10x speedup for end-to-end MACE performance
- 200x speedup for symmetric contraction operation performance
- 100,000 natoms per GPU being simulated with MACE
- 3.5x speedups for triangle operations performance 

_For more information on the performance noted above, please view the Performance section below._

### Expansive MLIPs Support and Accelerations 

- 

Leading equivariant machine-learning interatomic potential models including MACE, Allegro, NequIP, and DiffDock

- 

Protein models with triangle kernels, including: Boltz, Neo-1, and OpenFold

 
* * *

## Get Started With NVIDIA cuEquivariance

### Quick Install With Conda

    conda install conda-forge::cuequivariance

### Quick Install With pip

    # Choose the frontend you want to use pip install cuequivariance-jax pip install cuequivariance-torch pip install cuequivariance # Installs only the core non-ML components # CUDA kernels pip install cuequivariance-ops-torch-cu11 pip install cuequivariance-ops-torch-cu12 pip install cuequivariance-ops-jax-cu12

* * *

## Performance

* * *

## More Resources

 ![NVIDIA Developer Newsletter](https://brand-assets.cne.ngc.nvidia.com/assets/marketing-icons/2.1.0/email-settings.svg)
### Sign up for Developer Newsletter  

 ![Get Training and Certification](https://developer.download.nvidia.com/images/isaac/m48-certification-ribbon-2-256px-blk.png)
### Get Training and Certification  

 ![NVIDIA Developer Program](https://brand-assets.cne.ngc.nvidia.com/assets/marketing-icons/2.1.0/developer-1.svg)
### Join the NVIDIA Developer Program  

## Ethical AI   

NVIDIA believes Trustworthy AI is a shared responsibility, and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   
  
  
For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety &amp; Security, and Privacy Subcards. Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

**Get started with cuEquivariance today.**

[Install Now  
](https://github.com/NVIDIA/cuEquivariance/tree/main/docs/tutorials)


