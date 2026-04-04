# Source: https://developer.nvidia.com/ai-apps-for-rtx-pcs/inference-backends.md

1. [Home](https://developer.nvidia.com/)
2. [RTX AI PCs](/ai-apps-for-rtx-pcs/)

NVIDIA AI Inference Backends

# Accelerate AI On NVIDIA RTX PCs

NVIDIA RTX™ PCs accelerate your AI features for maximum performance and lowest latency. NVIDIA offers broad support on all major AI inference backends to meet every developer’s needs.

* * *

## Overview of AI Inference Backends

Developers need to consider several factors before choosing a deployment ecosystem and path for their application. Each inference backend offers specific model optimization tools and deployment mechanisms for efficient application integration. Inference backends map model execution to hardware, with top options optimized for NVIDIA RTX GPUs. Achieving peak AI performance requires model optimization techniques like quantization and pruning. Higher-level interfaces streamline application packaging, installation, and integration, enhancing efficiency.

Windows ML with   
NVIDIA TensorRT for RTX  

NVIDIA TensorRT for   
RTX

Ollama /  
Llama.cpp  

PyTorch

### Who Is Windows ML with TensorRT for RTX For?  

For developers who want to deploy performant, cross-vendor apps across Windows OS.

### Inferencing Backends  

Windows ML Runtime, built on ONNX Runtime, allows developers to run ONNX models locally across the entirety of PC hardware—including CPUs, NPUs, and GPUs.   
  
Windows ML automatically picks what execution provider to use, depending on the hardware available on the user’s PC, then downloads all the files necessary for that hardware.   
  
Windows ML is powered by NVIDIA TensorRT™ for RTX on NVIDIA GPUs for maximum performance.

[Get Started With Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)

[See Windows ML Example Samples](https://github.com/microsoft/WindowsAppSDK-Samples/tree/feature/winml-stable/Samples/WindowsML)

[See ONNX Runtime API Samples](https://github.com/microsoft/onnxruntime-inference-examples/tree/main)

### Model Optimization  

The Olive optimization toolkit offers hardware-aware quantization across CPUs, NPUs, and NVIDIA RTX GPUs—with easy integration into the Windows ML inferencing backend.

[Get Started With Olive](https://microsoft.github.io/Olive/)

### Deployment Mechanisms  

Packaging and deploying Windows ML-based apps on PCs is simple. Your application and the Windows ML are decoupled, allowing for OTA updates. Just add a reference to Windows ML within your project, and Windows ML will manage the download and install everything else—including versioning, execution providers, runtime, and all the dependencies. 

[Get Started With Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)

### Introduction to ONNX Runtime  
  

https://www.youtube-nocookie.com/embed/Wp5PaRpudlk?
[Watch Video (8:12)](https://www.youtube.com/watch?v=Wp5PaRpudlk) 

### ONNXRuntime-GenAI Installation and Inference Walkthrough

https://www.youtube-nocookie.com/embed/tNq9MP9wlBg?
[Watch Video (6:00)](https://www.youtube.com/watch?v=tNq9MP9wlBg) 

### Who Is Ollama and Llama.cpp For?

For large language model (LLM) developers who want wide reach with cross-vendor and cross-OS support.

### Inferencing Backends  

Ollama and Llama.cpp enable LLM-only inferencing across a variety of devices and platforms with unified APIs. This requires minimal setup, delivers good performance, and is a lightweight package. Ollama and Llama.cpp are powered by the GGML runtime and compatible with GGUF model formats.

[Get Started With Ollama](https://github.com/ollama/ollama)[Get Started With Llama.cpp](https://github.com/ggml-org/llama.cpp)

### Model Optimization

Ollama leverages model optimization formats, such as GGUF, both within and outside Llama.cpp tooling. This format allows for optimal model performance and lightweight deployment. It uses quantization techniques to reduce the size and computational requirements of the model to run across a variety of platforms.

[Get Started With Ollama / Llama.cpp Model Quantization](https://github.com/ggerganov/llama.cpp/blob/master/examples/quantize/README.md)

### Deployment Mechanisms  

With Ollama, you can deploy in an out-of-process format, with a server running on localhost. Apps communicate with this server using a REST API.

[Get Started With Ollama](https://github.com/ollama/ollama)[Get Started With Llama.cpp](https://github.com/ggml-org/llama.cpp)[See How to Deploy LLMs on RTX PCs](https://forums.developer.nvidia.com/t/how-to-deploy-llms-on-rtx-pcs/317354)

### Who Is NVIDIA TensorRT for RTX SDK For?

For developers looking for full behavior control on NVIDIA RTX GPUs.

### Inferencing Backends  

NVIDIA TensorRT™ for RTX offers full behavior control on RTX PCs, is lightweight for easy packaging into applications, and can generate optimized engines in just seconds on device.  

[Get Started With TensorRT for RTX SDK ](https://developer.nvidia.com/tensorrt-rtx)

### Optimize Your Models  

TensorRT for RTX uses a just-in-time (JIT) engine builder to compile any ONNX model with optimizations that take full advantage of the user’s specific GPU-configuration. It happens transparently to the user, taking less than 30 seconds on first setup.

[Get Started With TensorRT for RTX SDK](https://developer.nvidia.com/tensorrt-rtx)

### Deployment Mechanisms  

With TensorRT for RTX, deploying AI apps is easier. Developers can include both the model and the lightweight TensorRT runtime (under 200 MB) inside their applications. When a user installs the app or on first run, TensorRT-RTX quickly compiles the model for their specific hardware in under 30 seconds, ensuring peak performance.

[Get Started with TensorRT for RTX SDK](https://developer.nvidia.com/tensorrt-rtx)

### Who Is PyTorch For?

For developers looking to experiment with and evaluate AI while maintaining cohesion with model training pipelines.

### Inferencing Backends  

PyTorch is a popular open-source machine learning library that offers cross-platform and cross-device inferencing options.

[Get Started With PyTorch](https://pytorch.org/get-started/locally/)

### Model Optimization  

PyTorch offers several leading algorithms for model quantization, ranging from quantization-aware training (QAT) to post-training quantization (PTQ), as well as sparsity for in-framework model optimization.

[Get Started With torchao](https://github.com/pytorch/ao/)

### Deployment Mechanisms  

To serve models in production applications within PyTorch, developers often deploy using an out-of-process format. This would require building python packages, generating model files and standing up a localhost server. This can be streamlined with frameworks such as tocrchserve and HuggingFace Accelerate.

[Get Started With PyTorch ](https://github.com/pytorch/pytorch?tab=readme-ov-file#nvidia-cuda-support)[Get Started With torchserve](https://github.com/pytorch/serve/tree/master)[Get Started With HuggingFace Accelerate](https://github.com/pytorch/serve/tree/master/examples/large_models/Huggingface_accelerate)[Recommendations on How to Deploy Diffusion Models on NVIDIA RTX PCs](https://forums.developer.nvidia.com/t/recommendations-on-how-to-deploy-diffusion-models-on-nvidia-rtx-pcs/341946)

* * *

## Choosing an Inferencing Backend

| | Windows ML with NVIDIA TensorRT for RTX | TensorRT for RTX | Ollama / Llama.cpp | PyTorch |
| --- | --- | --- | --- | --- |
| **For** | Windows application developers building AI features for Windows PC | Windows application developers who want maximum control and flexibility of AI behavior on NVIDIA RTX GPUs | LLM developers who want wide reach with cross-vendor and cross-OS support | Developers experimenting with and evaluating AI while maintaining cohesion with model training pipelines |
| **Performance** | Fastest | Fastest | Fast | Good |
| **OS Support** | Windows | Windows and Linux  | Windows, Linux, and Mac | Windows and Linux |
| **Hardware Support** | Any GPU or CPU | NVIDIA RTX GPUs | Any GPU or CPU | Any GPU or CPU |
| **Model Checkpoint Format** | ONNX | ONNX | GGUF or GGML | PyT |
| **Installation Process** | Pre-installed on Windows | Install SDK and Python bindings | Installation of Python packages required | Installation of Python packages required |
| **LLM Support** | ![](https://developer.download.nvidia.com/icons/check.svg) | ![](https://developer.download.nvidia.com/icons/check.svg) | ![](https://developer.download.nvidia.com/icons/check.svg) | ![](https://developer.download.nvidia.com/icons/check.svg) |
| **CNN Support** | ![](https://developer.download.nvidia.com/icons/check.svg) | ![](https://developer.download.nvidia.com/icons/check.svg) | - | ![](https://developer.download.nvidia.com/icons/check.svg) |
| **Model Optimizations** | Microsoft Olive | TensorRT-Model Optimizer | Llama.cpp | - |
| **Python** | ![](https://developer.download.nvidia.com/icons/check.svg) | ![](https://developer.download.nvidia.com/icons/check.svg) | ![](https://developer.download.nvidia.com/icons/check.svg) | ![](https://developer.download.nvidia.com/icons/check.svg) |
| **C/C++** | ![](https://developer.download.nvidia.com/icons/check.svg) | ![](https://developer.download.nvidia.com/icons/check.svg) | ![](https://developer.download.nvidia.com/icons/check.svg) | ![](https://developer.download.nvidia.com/icons/check.svg) |
| **C#/.NET** | ![](https://developer.download.nvidia.com/icons/check.svg) | - | ![](https://developer.download.nvidia.com/icons/check.svg) | - |
| **Javascript** | ![](https://developer.download.nvidia.com/icons/check.svg) | - | ![](https://developer.download.nvidia.com/icons/check.svg) | - |

* * *

## Latest NVIDIA News  

NVIDIA TensorRT for RTX

Ollama

* * *

Stay up to date on how to power your AI apps with NVIDIA RTX PCs.

[Learn More](https://developer.nvidia.com/ai-apps-for-rtx-pcs)


