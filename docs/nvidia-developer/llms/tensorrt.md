# Source: https://developer.nvidia.com/tensorrt.md

1. [Topic](/topics/)

[AI Inference](/topics/ai/ai-inference/)

TensorRT  

# NVIDIA TensorRT

NVIDIA® TensorRT™ is an ecosystem of tools for developers to achieve high-performance deep learning inference. TensorRT includes inference compilers, runtimes, and model optimizations that deliver low latency and high throughput for production applications. The TensorRT ecosystem includes the TensorRT compiler, TensorRT-LLM, TensorRT Model Optimizer, TensorRT for RTX, and TensorRT Cloud.

[Download Now](https://developer.nvidia.com/tensorrt/download)[Documentation  
](https://docs.nvidia.com/deeplearning/tensorrt/)[GitHub](https://github.com/NVIDIA/TensorRT)

 
* * *

## How TensorRT Works

Speed up inference by 36X compared to CPU-only platforms.

Built on the NVIDIA® CUDA® parallel programming model, TensorRT includes libraries that optimize neural network models trained on all major frameworks, calibrate them for lower precision with high accuracy, and deploy them to hyperscale data centers, workstations, laptops, and edge devices. TensorRT optimizes inference using quantization, layer and tensor fusion, and kernel tuning techniques.  
  
NVIDIA TensorRT Model Optimizer provides easy-to-use quantization techniques, including post-training quantization and quantization-aware training to compress your models. FP8, FP4, INT8, INT4, and advanced techniques such as AWQ are supported for your deep learning inference optimization needs. Quantized inference significantly minimizes latency and memory bandwidth, which is required for many real-time services, autonomous and embedded applications.

 ![](https://developer.download.nvidia.com/images/tensorrt/how-tensor-rt-works.jpg)

### Read the Introductory TensorRT Blog  

Learn how to apply TensorRT optimizations and deploy a PyTorch model to GPUs.

[Read Blog](https://developer.nvidia.com/blog/speeding-up-deep-learning-inference-using-tensorrt-updated/)

### Watch On-Demand TensorRT Sessions From GTC  

Learn more about TensorRT and its features from a curated list of webinars at GTC.

[Watch Sessions](https://www.nvidia.com/en-us/on-demand/playlist/playList-53110dbc-c11d-4619-b821-987015090afa/)

### Get the Complete Developer Guide  

See how to get started with TensorRT in this step-by-step developer and API reference guide.

[Read Guide](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html)

### Navigate AI infrastructure and Performance  

Learn how to lower your cost per token and get the most out of your AI models with our ebook.

[View Ebook](https://www.nvidia.com/en-us/solutions/ai/inference/balancing-cost-latency-and-performance-ebook/)

* * *

## Key Features 

### Large Language Model Inference

[NVIDIA TensorRT-LLM](https://developer.nvidia.com/blog/optimizing-inference-on-llms-with-tensorrt-llm-now-publicly-available/) is an open-source library that accelerates and optimizes inference performance of large language models (LLMs) on the NVIDIA AI platform with a simplified Python API.  
Developers accelerate LLM performance on NVIDIA GPUs in the data center or on workstation GPUs.

### Compile in the Cloud

NVIDIA TensorRT Cloud is a developer-focused service for generating hyper-optimized engines for given constraints and KPIs. Given an LLM and inference throughput/latency requirements, a developer can invoke TensorRT Cloud service using a command-line interface to hyper-optimize a TensorRT-LLM engine for a target GPU. The cloud service will automatically determine the best engine configuration that meets the requirements. Developers can also use the service to build optimized TensorRT engines from ONNX models on a variety of NVIDIA RTX, GeForce, Quadro®, or Tesla®-class GPUs.  
  
TensorRT Cloud is available with limited access to select partners. [Apply](https://developer.nvidia.com/tensorrt-cloud-program) for access, subject to approval.

### Optimize Neural Networks

[TensorRT Model Optimizer](https://developer.nvidia.com/blog/accelerate-generative-ai-inference-performance-with-nvidia-tensorrt-model-optimizer-now-publicly-available/) is a unified library of state-of-the-art model optimization techniques, including quantization, pruning, speculation, sparsity, and distillation. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, and SGLang to efficiently optimize inference on NVIDIA GPUs. TensorRT Model Optimizer also supports training for inference techniques such as Speculative Decoding Module Training, Pruning/Distillation, and Quantization Aware Training through NeMo and Hugging Face frameworks.

### Major Framework Integrations  
  

TensorRT integrates directly into [PyTorch](https://developer.nvidia.com/blog/accelerating-inference-up-to-6x-faster-in-pytorch-with-torch-tensorrt/) and [Hugging Face](http://hf.co/blog/optimum-nvidia) to achieve 6X faster inference with a single line of code. TensorRT provides an [ONNX](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#fit) parser to import [ONNX](https://github.com/NVIDIA/TensorRT/blob/release/10.9/quickstart/IntroNotebooks/2.%20Using%20PyTorch%20through%20ONNX.ipynb) models from popular frameworks into TensorRT. [MATLAB](https://www.mathworks.com/help/gpucoder/ug/tensorrt-target.html) is integrated with TensorRT through GPU Coder to automatically generate high-performance inference engines for NVIDIA Jetson™, NVIDIA DRIVE®, and data center platforms.

### Deploy, Run, and Scale With Dynamo-Triton

TensorRT-optimized models are deployed, run, and scaled with [NVIDIA Dynamo Triton](https://www.nvidia.com/en-us/ai-data-science/products/triton-inference-server/) inference-serving software that includes TensorRT as a backend. The advantages of using Triton include high throughput with dynamic batching, concurrent model execution, model ensembling, and streaming audio and video inputs.

### Simplify AI deployment on RTX

TensorRT for RTX offers an optimized inference deployment solution for NVIDIA RTX GPUs. It facilitates faster engine build times within 15 to 30s, facilitating apps to build inference engines directly on target RTX PCs during app installation or on first run, and does so within a total library footprint of under 200 MB, minimizing memory footprint. Engines built with TensorRT for RTX are cross-OS, cross-GPU portable, ensuring a build once, deploy anywhere workflow.

### Accelerate Every Inference Platform

TensorRT can optimize models for applications across the edge, laptops, desktops, and data centers. It powers key NVIDIA solutions—such as NVIDIA TAO, NVIDIA DRIVE, NVIDIA Clara™, and NVIDIA JetPack™—and is integrated with application-specific SDKs, such as NVIDIA NIM™, NVIDIA DeepStream, NVIDIA Riva, NVIDIA Merlin™, NVIDIA Maxine™, NVIDIA Morpheus, and NVIDIA Broadcast Engine.   
  
TensorRT provides developers a unified path to deploy intelligent video analytics, speech AI, recommender systems, video conferencing, AI-based cybersecurity, and streaming apps in production.

* * *

## Get Started With TensorRT

TensorRT is an ecosystem of APIs for building and deploying high-performance deep learning inference. It offers a variety of inference solutions for different developer requirements.

| 

Use-case

 | 

Deployment Platform

 | 

Solution

 |
| --- | --- | --- |
| Inference for LLMs | Data center GPUs like GB100, H100, A100, etc. | 

Download TRT-LLM

TensorRT-LLM is available for free on [GitHub](https://github.com/NVIDIA/TensorRT-LLM/tree/rel). 

[Download (GitHub)](https://github.com/NVIDIA/TensorRT-LLM/tree/rel)

[Documentation](https://nvidia.github.io/TensorRT-LLM)

 |
| Inference for non-LLMs like CNNs, Diffusions, Transformers, etc. Safety-compliant and high-performance inference for Automotive Embedded Inference for non-LLMs in robotics and edge applications | Data center GPUs, Embedded, and Edge platforms Automotive platform: NVIDIA DRIVE AGX Edge Platform: Jetson, NVIDIA IGX, etc. | 

Download TensorRT

The TensorRT inference library provides a general-purpose AI compiler and an inference runtime that delivers low latency and high throughput for production applications. 

[Download SDK](https://developer.nvidia.com/nvidia-tensorrt-download)

[Download Container](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorrt)

 |
| AI Model Inferencing on RTX PCs  | NVIDIA GeForce RTX and RTX Pro GPUs in laptops and desktops  | 

Download TensorRT for RTX

TensorRT for RTX is a dedicated inference deployment solution for RTX GPUs. 

[Download SDK](/tensorrt-rtx)

[Documentation](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/index.html)

 |
| Model optimizations like Quantization, Distillation, Sparsity, etc. | Data center GPUs like GB100, H100, etc. | 

Download TensorRT Model Optimizer

TensorRT Model Optimizer is free on NVIDIA PyPI, with examples and recipes on [GitHub](https://github.com/NVIDIA/TensorRT-Model-Optimizer). 

[Download (GitHub)](https://github.com/NVIDIA/TensorRT-Model-Optimizer)

[Documentation](https://nvidia.github.io/TensorRT-Model-Optimizer)

 |

* * *

## Get Started With TensorRT Frameworks  

TensorRT Frameworks add TensorRT compiler functionality to frameworks like PyTorch.

 ![TensorRT speeds up inference by 36X](https://developer.download.nvidia.com/icons/m48-download.svg)
### Download ONNX and Torch-TensorRT

The TensorRT inference library provides a general-purpose AI compiler and an inference runtime that delivers low latency and high throughput for production applications.

**ONYX:**

[Documentation](https://github.com/NVIDIA/TensorRT/blob/release/10.9/quickstart/IntroNotebooks/2.%20Using%20PyTorch%20through%20ONNX.ipynb)

**Torch-TensorRT:**

[Download Container](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch)

[Documentation](https://pytorch.org/TensorRT/)

 ![TensorRT speeds up inference by 36X](https://developer.download.nvidia.com/icons/m48-accellerated-computing-with-cuda-python-256px-blk.png)
### Experience Tripy: Pythonic Inference With TensorRT

Experience high-performance inference and excellent usability with Tripy. Expect intuitive APIs, easy debugging with eager mode, clear error messages, and top-notch documentation to streamline your deep learning deployment.

[Documentation](https://nvidia.github.io/TensorRT-Incubator/index.html)

[Examples](https://github.com/NVIDIA/TensorRT-Incubator/tree/main/tripy/examples)

[Contribute](https://github.com/NVIDIA/TensorRT-Incubator/blob/main/tripy/CONTRIBUTING.md)

 ![TensorRT speeds up inference by 36X](https://developer.download.nvidia.com/icons/m48-digital-deep-learning-institute-talks-training.svg)
### Deploy

Get a free license to try [NVIDIA AI Enterprise](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/) in production for 90 days using your existing infrastructure.

[Request a 90-Day License](https://enterpriseproductregistration.nvidia.com/?LicType=EVAL&amp;ProductFamily=NVAIEnterprise)

* * *

## World-Leading Inference Performance  

TensorRT was behind NVIDIA’s wins across all [inference performance](https://developer.nvidia.com/blog/tag/inference-performance/) tests in the industry-standard benchmark for [MLPerf Inference](https://www.nvidia.com/en-us/data-center/mlperf/). TensorRT-LLM accelerates the latest large language models for [generative AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/), delivering up to 8X more performance, 5.3X better TCO, and nearly 6X lower energy consumption.

[See All Benchmarks](/deep-learning-performance-training-inference/ai-inference)

### 8X Increase in GPT-J 6B Inference Performance

 ![TensorRT-LLM on H100 has 8X increase in GPT-J 6B inference performance](https://developer.download.nvidia.com/images/gpt-j-6b-630x354-1.jpg)

### 4X Higher Llama2 Inference Performance  

 ![TensorRT-LLM on H100 has 4X Higher Llama2 Inference Performance](https://developer.download.nvidia.com/images/llama-2-70b-630x354-1.jpg)

### Total Cost of Ownership

Lower is better

 ![TensorRT-LLM has lower total cost of ownership than GPT-J 6B and Llama 2 70B](https://developer.download.nvidia.com/images/cost-of-ownership-630x354-1.jpg)

### Energy Use

Lower is better

 ![TensorRT-LLM has lower energy use than GPT-J 6B and Llama 2 70B](https://developer.download.nvidia.com/images/energy-use-630x354-1.jpg)

* * *

#### NVIDIA Blackwell Delivers Unmatched Performance and ROI for AI Inference

The NVIDIA Blackwell platform—including NVFP4 low precision format, fifth-generation NVIDIA NVLink and NVLink Switch, and the NVIDIA TensorRT-LLM and NVIDIA Dynamo inference frameworks—enables the highest AI factory revenue: A $5M investment in GB200 NVL72 generates $75 million in token revenue—a 15x return on investment. This includes development with community frameworks such as SGLang, vLLM, and more.

[Explore technical results](https://developer.nvidia.com/blog/nvidia-blackwell-leads-on-new-semianalysis-inferencemax-benchmarks/)

![NVIDIA Rivermax provides real-time streaming for the Las Vegas Sphere, world’s largest LED display](https://developer.download.nvidia.com/images/tensorrt/inference-tech-blog-sa-external-think-smart-1920x1080.png)

* * *

## Starter Kits

### Beginner Guide to TensorRT  

- 

[View Quick-Start Guide](/tensorrt-getting-started)

- 

[View Quick-Start Notebooks](https://docs.nvidia.com/deeplearning/tensorrt/latest/getting-started/quick-start-guide.html)

- 

Read Blog: [Speeding Up Deep Learning Inference Using NVIDIA TensorRT](/blog/speeding-up-deep-learning-inference-using-tensorrt-updated/)

  

- 

Read Blog: [Optimizing and Serving Models With TensorRT and Triton](/blog/optimizing-and-serving-models-with-nvidia-tensorrt-and-nvidia-triton/)

  

- 

Watch Video: [Getting Started With NVIDIA TensorRT](https://www.youtube.com/watch?v=SlUouzxBldU)

  

### Beginner Guide to TensorRT-LLM

- 

[View Quick-Start Guide](/tensorrt-getting-started)

- 

[View Quick-Start Notebooks](https://nvidia.github.io/TensorRT-LLM/quick-start-guide.html)

- 

Read Blog: [Speeding Up Deep Learning Inference Using NVIDIA TensorRT](/blog/speeding-up-deep-learning-inference-using-tensorrt-updated/)

  

- 

Read Blog: [Optimizing and Serving Models With TensorRT and Triton](/blog/optimizing-and-serving-models-with-nvidia-tensorrt-and-nvidia-triton/)

  

- 

Watch Video: [Getting Started With NVIDIA TensorRT](https://www.youtube.com/watch?v=SlUouzxBldU)

  

### Beginner Guide to TensorRT Model Optimizer  

- 

[Reference Architecture](https://docs.omniverse.nvidia.com/simready/latest/sim-needs/synth-data-gen.html)

- 

[Workflow Guide &amp; Documentation](https://docs.omniverse.nvidia.com/extensions/latest/ext_product-configurator.html)

- 

[Training Courses](https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-OV-14+V1)

- 

[NVIDIA Omniverse Blueprint for Precise Visual Generative AI](https://build.nvidia.com/nvidia/conditioning-for-precise-visual-generative-ai)

### Beginner Guide to Torch-TensorRT  

- 

Watch Video: [Getting Started With NVIDIA Torch-TensorRT](https://www.youtube.com/watch?v=TU5BMU6iYZ0)

  

- 

Read Blog: [Accelerate Inference up to 6X in PyTorch](/blog/accelerating-inference-up-to-6x-faster-in-pytorch-with-torch-tensorrt/)

  

- 

Download Notebook: [Object Detection With SSD](https://github.com/NVIDIA/Torch-TensorRT/blob/master/notebooks/ssd-object-detection-demo.ipynb) (Jupyter Notebook)

  

### Beginner Guide to TensorRT Pythonic Frontend: Tripy  

- 

[Introduction Guide](https://nvidia.github.io/TensorRT-Incubator/pre0_user_guides/00-introduction-to-tripy.html)

  

- 

[ResNet-50 notebook](https://github.com/NVIDIA/TensorRT-Incubator/blob/main/tripy/notebooks/resnet50.ipynb)

  

- 

[nanoGPT](https://github.com/NVIDIA/TensorRT-Incubator/tree/main/tripy/examples/nanogpt)

  

- 

[Segment Anything Model V2](https://github.com/NVIDIA/TensorRT-Incubator/tree/main/tripy/examples/segment-anything-model-v2)

  

### Beginner Guide to TensorRT for RTX  

- 

[View Quick Start Guide  
](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/installing.html)

  

- 

[Access Samples and Demos](https://github.com/NVIDIA/TensorRT-RTX/tree/main)

  

- 

[Read Blog: 
# Run High-Performance AI Applications with NVIDIA TensorRT for RTX
   
](https://developer.nvidia.com/blog/run-high-performance-ai-applications-with-nvidia-tensorrt-for-rtx/)

  

- 

[Access TensorRT for RTX through WindowsML   
](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/get-started?tabs=csharp)

  

* * *

## TensorRT Learning Library

OSS (Github) 

Quantization Quickstart

**NVIDIA TensorRT-LLM**  
  
The [PyTorch backend](https://nvidia.github.io/TensorRT-LLM/torch.html#quantization) supports FP8 and NVFP4 quantization. Explore [GitHub](https://nvidia.github.io/TensorRT-LLM/torch.html#quantization) to pass quantized models in the Hugging Face model hub, which are generated by TensorRT Model Optimizer.  
    
[Link to GitHub](https://nvidia.github.io/TensorRT-LLM/torch.html#quantization)  
[Link to PyTorch Documentation](https://nvidia.github.io/TensorRT-Model-Optimizer/guides/_pytorch_quantization.html)

OSS (Github) 

Adding a New Model in PyTorch Backend

This guide provides a step-by-step process for adding a new model in PyTorch Backend.  
  
[Link to GitHub](https://nvidia.github.io/TensorRT-LLM/torch/adding_new_model.html)

OSS (Github) 

Using TensoRT-Model Optimizer for Speculative Decoding

ModelOpt’s Speculative Decoding module enables your model to generate multiple tokens in each generation step. This can be useful for reducing the latency of your model and speeding up inference.  
  
[Link to GitHub](https://nvidia.github.io/TensorRT-Model-Optimizer/guides/7_speculative_decoding.html)

* * *

## TensorRT Ecosystem Ecosystem

Widely Adopted Across Industries

 ![NVIDIA TensorRT is widely adopted by top companies across industries](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/tensorrt/Logo_farm_GTC.png)

* * *

## More Resources

 ![NVIDIA Developer Forums](https://developer.download.nvidia.com/icons/m48-people-group.svg)
### Explore the Community

 ![NVIDIA Training and Certification](https://developer.download.nvidia.com/icons/m48-certification-ribbon-2.svg)
### Get Training and Certification  

 ![NVIDIA Inception Program for Startups](https://developer.download.nvidia.com/images/isaac/m48-ai-startup-256px-blk.png)
### Read Top Stories and Blogs

* * *

## Ethical AI

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  
  
For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety &amp; Security, and Privacy Subcards. Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

**Get started with TensorRT today, and use the right inference tools to develop AI for any application on any platform.**

[Download Now  
](https://developer.nvidia.com/tensorrt/download)


