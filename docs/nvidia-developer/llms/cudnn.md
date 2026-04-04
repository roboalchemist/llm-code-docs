# Source: https://developer.nvidia.com/cudnn.md

1. [Home  
](/)

[CUDA-X Libraries](/gpu-accelerated-libraries)

cuDNN

# NVIDIA cuDNN

NVIDIA® CUDA® Deep Neural Network library (cuDNN) is a GPU-accelerated library of primitives for deep neural networks. cuDNN provides highly tuned implementations for standard routines, such as forward and backward convolution, attention, matmul, pooling, and normalization.

* * *

## Download cuDNN

[Download cuDNN Library](/rdp/cudnn-download &quot;vMaterials for Windows&quot;)[Download cuDNN Frontend  
  
   
  
  
(GitHub)](https://github.com/NVIDIA/cudnn-frontend &quot;vMaterials for Linux &quot;)

cuDNN is also available to download via one of the package managers below.

 

### Quick Install with conda

    conda install nvidia::cudnn cuda-version=12

Installs the cuDNN library

### Quick Pull with Docker

    docker pull nvidia/cuda:12.8.1-cudnn-devel-ubuntu22.04

Installs the cuDNN lLibrary

### Quick Install with pip

    pip install nvidia-cudnn

Installs the cuDNN library

###   

    pip install nvidia-cudnn-frontend

Installs the cuDNN Frontend API

[Documentation](https://docs.nvidia.com/deeplearning/cudnn/latest/)

[Forum](https://forums.developer.nvidia.com/c/ai-data-science/deep-learning/cudnn/90)

* * *

## How cuDNN Works 

- 

**Accelerated Llearning:** cuDNN provides kernels, targeting Tensor Cores whenever it makes sense, to deliver best- available performance on compute-bound operations. It offers heuristics for choosing the right kernel for a given problem size.

- 

**Fusion Support:** cuDNN supports fusion of compute-bound and memory-bound operations. Common generic fusion patterns are typically implemented by runtime kernel generation. Specialized fusion patterns are optimized with pre-written kernels.

- 

**Expressive Op Graph API:** The user defines computations as a graph of operations on tensors. The cuDNN library has both a direct C API and an open-source C++ frontend for convenience. Most users choose the frontend as their entry point to cuDNN

### cuDNN API Code Sample

The code performs a batched matrix multiplication with bias using the cuDNN PyTorch integration.

    import torch import cudnn # Prepare sample input data. nvmath-python accepts input tensors from pytorch, cupy, and # numpy. b, m, n, k = 1, 1024, 1024, 512 A = torch.randn(b, m, k, dtype=torch.float32, device=&quot;cuda&quot;) B = torch.randn(b, k, n, dtype=torch.float32, device=&quot;cuda&quot;) bias = torch.randn(b, m, 1, dtype=torch.float32, device=&quot;cuda&quot;) result = torch.empty(b, m, n, dtype=torch.float32, device=&quot;cuda&quot;) # Use the stateful Graph object in order to perform multiple matrix multiplications # without replanning. The cudnn API allows us to fine-tune our operations by, for # example, selecting a mixed-precision compute type. graph = cudnn.pygraph( intermediate\_data\_type=cudnn.data\_type.FLOAT, compute\_data\_type=cudnn.data\_type.FLOAT, ) a\_cudnn\_tensor = graph.tensor\_like(A) b\_cudnn\_tensor = graph.tensor\_like(B) bias\_cudnn\_tensor = graph.tensor\_like(bias) c\_cudnn\_tensor = graph.matmul(name=&quot;matmul&quot;, A=a\_cudnn\_tensor, B=b\_cudnn\_tensor) d\_cudnn\_tensor = graph.bias(name=&quot;bias&quot;, input=c\_cudnn\_tensor, bias=bias\_cudnn\_tensor) # Build the matrix multiplication. Building returns a sequence of algorithms that can be # configured. Each algorithm is a JIT generated function that can be executed on the GPU. graph.build([cudnn.heur\_mode.A]) workspace = torch.empty(graph.get\_workspace\_size(), device=&quot;cuda&quot;, dtype=torch.uint8) # Execute the matrix multiplication. graph.execute( { a\_cudnn\_tensor: A, b\_cudnn\_tensor: B, bias\_cudnn\_tensor: bias, d\_cudnn\_tensor: result, }, workspace )

### Sample Operation Graphs Described by the cuDNN Graph API
 ![](https://developer.download.nvidia.com/images/conv_bias_relu.png)

_ConvolutionFwd followed by a DAG with two operations_

### Documentation

Complete guides on installing and using the cuDNN frontend and cuDNN backend.

[Read Docs](https://docs.nvidia.com/deeplearning/cudnn/latest/)

### Frontend Samples

Samples illustrate usage of the Python and C++ frontend APIs.

[View Samples](https://docs.nvidia.com/deeplearning/cudnn/frontend/latest/samples.html)

### 
### Latest Release Blog  

Learn how to accelerate transformers with scaled dot product attention (SDPA) in cuDNN 9.

[Read Blog](https://developer.nvidia.com/blog/accelerating-transformers-with-nvidia-cudnn-9/)

### cuDNN on NVIDIA Blackwell  

Learn about new/updated APIs of cuDNN pertaining to NVIDIA Blackwell’s microscaling format and how to program against those APIs.

[Watch Session](https://www.nvidia.com/en-us/on-demand/session/gtc25-s73071/)

* * *

## Key Features

### Deep Neural Networks  

Deep learning neural networks span computer vision, conversational AI, and recommendation systems and have led to breakthroughs like autonomous vehicles and intelligent voice assistants. NVIDIA&#39;s GPU-accelerated deep learning frameworks speed up training time for these technologies, reducing multi-day sessions to just a few hours.

cuDNN supplies foundational libraries for high-performance, low-latency inference for deep neural networks in the cloud, on embedded devices, and in self-driving cars.

- 

Accelerated compute-bound operations like attention training/prefill, convolution, and matmul

- 

Optimized memory-bound operations like attention decode, pooling, softmax, normalization, activation, pointwise, and tensor transformation

- 

Fusions of compute-bound and memory-bound operations

- 

Runtime fusion engine to generate kernels at runtime for common fusion patterns

- 

Optimizations for important specialized patterns like fused attention

- 

Heuristics to choose the right implementation for a given problem size

### cuDNN Graph API and Fusion  

The cuDNN Graph API is designed to express common computation patterns in deep learning. A cuDNN graph represents operations as nodes and tensors as edges, similar to a dataflow graph in a typical deep learning framework.

Access to the cuDNN Graph API is conveniently available through the [Python/C++ Frontend API](https://github.com/NVIDIA/cudnn-frontend) (recommended) as well as the lower-level C Backend API (for legacy use cases or special cases where Python/C++ isn’t appropriate).

- 

Flexible fusions of memory-limited operations into the input and output of matmul and convolution

- 

Specialized fusions for patterns like attention and convolution with normalization

- 

Support for both forward and backward propagation

- 

Heuristics for predicting the best implementation for a given problem size

- 

Open-source Python/C++ Frontend API

- 

Serialization and deserialization support

* * *

## cuDNN Accelerated Frameworks

cuDNN accelerates widely used deep learning frameworks, including PyTorch, JAX, Caffe2, Chainer, Keras, MATLAB, MxNet, PaddlePaddle, and TensorFlow.

 ![cuDNN Accelerated Framework - Caffe2](https://developer.download.nvidia.com/images/caffe2-logo.svg)

 ![cuDNN Accelerated Framework - Chainer](https://developer.download.nvidia.com/images/chainer-logo.svg)

 ![cuDNN Accelerated Framework - JAX](https://developer.download.nvidia.com/images/jax-logo.svg)

 ![cuDNN Accelerated Framework - MATLAB](https://developer.download.nvidia.com/images/matlab-logo.svg)

 ![cuDNN Accelerated Framework - Microsoft Cognitive Toolkit](https://developer.download.nvidia.com/images/microsoft-cognitive-toolkit-logo.svg)

 ![cuDNN Accelerated Framework - MXNet](https://developer.download.nvidia.com/images/mxnet-logo.svg)

 ![cuDNN Accelerated Framework - PaddlePaddle](https://developer.download.nvidia.com/images/paddle-paddle-logo.svg)

 ![cuDNN Accelerated Framework - PyTorch](https://developer.download.nvidia.com/images/pytorch-logo.svg)

 ![cuDNN Accelerated Framework - TensorFlow](https://developer.download.nvidia.com/images/tensorflow-logo.svg)

 ![cuDNN Accelerated Framework - Wolfram Language](https://developer.download.nvidia.com/images/wolfram-language-logo.svg)

 ![cuDNN Accelerated Framework - XLA](https://developer.download.nvidia.com/images/xla-logo.svg)

* * *

## Related Libraries and Software

### NVIDIA NeMo™  

NeMo is an end-to-end cloud-native framework for developers to build, customize, and deploy generative AI models with billions of parameters.

[Learn More](/nemo)

### NVIDIA TensorRT™  

TensorRT is a software development kit for high-performance deep learning inference.

[Learn More](/tensorrt)

### 
### NVIDIA Optimized Frameworks

Deep learning frameworks offer building blocks for designing, training, and validating deep neural networks through a high-level programming interface.

[Learn More](https://docs.nvidia.com/deeplearning/frameworks/index.html#undefined&#39;)

### NVIDIA Collective Communication Library

NCCL is a communication library for high-bandwidth, low-latency, GPU-accelerated networking.

[Learn More](/nccl)

* * *

## More Resources

 ![Join the Developer Community](https://developer.download.nvidia.com/images/omniverse/m48-people-group.svg)
### Join the Community  

 ![Join the NVIDIA Developer Program](https://developer.download.nvidia.com/icons/m48-developer-1.svg)
### Join the NVIDIA Developer Program

 ![NVIDIA Inception Program](https://developer.download.nvidia.com/icons/m48-ai-startup.svg)
### Accelerate Your Startup

* * *

## Ethical AI 

NVIDIA believes Trustworthy AI is a shared responsibility, and we have established policies and practices to enable development for a wide array of AI applications. When downloading or using a model in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   
  
Please report security vulnerabilities or NVIDIA AI concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Get Started With cuDNN Today

[Download cuDNN Library](/rdp/cudnn-download &quot;vMaterials for Windows&quot;)[Download cuDNN Frontend  
  
   
  
  
(GitHub)](https://github.com/NVIDIA/cudnn-frontend &quot;vMaterials for Linux &quot;)


