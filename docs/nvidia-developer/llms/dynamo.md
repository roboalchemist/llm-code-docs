# Source: https://developer.nvidia.com/dynamo.md

# NVIDIA Dynamo

[NVIDIA Dynamo](https://www.nvidia.com/en-us/ai-data-science/products/triton-inference-server/)is an open-source, low-latency, modular inference framework for serving generative AI models in distributed environments. It enables seamless scaling of inference workloads across large GPU fleets with intelligent resource scheduling and request routing, optimized memory management, and seamless data transfer. NVIDIA Dynamo supports all major AI inference backends and features large language model (LLM)-specific optimizations, such as disaggregated serving.

When serving the open-source DeepSeek-R1 671B reasoning model on [NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/), NVIDIA Dynamo increased throughput—measured in tokens per second per GPU—by up to 30x. Serving the Llama 70B model on NVIDIA Hopper™, it increased throughput by more than 2x. NVIDIA Dynamo is the ideal solution for developers looking to accelerate and scale generative AI models with the highest efficiency at the lowest cost.  
  
NVIDIA Dynamo builds on the successes of the [NVIDIA Triton Inference Server](https://github.com/triton-inference-server/server), an open-source software that standardizes AI model deployment and execution across every workload.

[Get Started](https://github.com/ai-dynamo/dynamo)[Documentation](https://docs.nvidia.com/dynamo/latest/)

* * *

## See NVIDIA Dynamo in Action

https://www.youtube-nocookie.com/embed/1bRmskFCnqY?
 

### See How to Quickly Set up and Deploy NVIDIA Dynamo
[Watch Video](https://youtu.be/1bRmskFCnqY)

https://www.youtube-nocookie.com/embed/PRCZZKQirN8?
 

### Watch KV Cache-Aware Smart Router With NVIDIA Dynamo
[Watch Video](https://youtu.be/PRCZZKQirN8)

https://www.youtube-nocookie.com/embed/PRCZZKQirN8?
 

### Learn How NVIDIA Dynamo Enables Disaggregated Serving
[Watch Video](https://www.youtube.com/watch?v=PRCZZKQirN8)

 
* * *

## How NVIDIA Dynamo Works

Models are becoming larger and more integrated into AI workflows that require interaction with multiple models. Deploying these models at scale involves distributing them across multiple nodes, requiring careful coordination across GPUs. The complexity increases with inference optimization methods, like disaggregated serving, which splits responses across different GPUs, adding challenges in collaboration and data transfer.

**NVIDIA Dynamo addresses the challenges of distributed and disaggregated inference serving. It includes four key components:**

- 

**GPU Resource Planner:** A planning and scheduling engine that monitors capacity and prefill activity in multi-node deployments to adjust GPU resources and allocate them across prefill and decode.

- 

**Smart Router:** A KV-cache-aware routing engine that efficiently directs incoming traffic across large GPU fleets in multi-node deployments to minimize costly re-computations.

- 

**Low Latency Communication Library:** State-of-the-art inference data transfer library that accelerates the transfer of KV cache between GPUs and across heterogeneous memory and storage types.

- 

**KV Cache Manager:** A cost-aware KV cache offloading engine designed to transfer KV cache across various memory hierarchies, freeing up valuable GPU memory while maintaining user experience.

 ![A flowchart of how NVIDIA Dynamo works](https://developer.download.nvidia.com/images/how-it-works.jpg) 
* * *
 

https://www.youtube-nocookie.com/embed/3C-6STonTLU?

#### NVIDIA Dynamo Key Moments From GTC25

Watch the recording to learn about NVIDIA Dynamo’s key components and architecture and how they enable seamless scaling and optimized inference in distributed environments.  
  
[Watch Now](https://www.nvidia.com/gtc/session-catalog/?search=S73042&amp;tab.catalogallsessionstab=16566177511100015Kus#/)

* * *

## Get Started With NVIDIA Dynamo

[Find](https://www.nvidia.com/en-us/ai-data-science/products/triton-inference-server/get-started/) the right license to deploy, run, and scale AI inference for any application on any platform.

 ![](https://developer.download.nvidia.com/icons/m48-download.svg)
### Download Code for Development

NVIDIA Dynamo and NVIDIA Dynamo-Triton are available as open-source software on GitHub with end-to-end examples.

[Go to NVIDIA Dynamo Repository (Github)](https://github.com/ai-dynamo/dynamo)

[Go to NVIDIA Dynamo-Triton Repository (Github](https://github.com/triton-inference-server/server)

 ![](https://developer.download.nvidia.com/icons/m48-digital-deep-learning-institute-talks-training.svg)
### Purchase NVIDIA AI Enterprise

NVIDIA Dynamo-Triton is available with enterprise-grade support, security, stability, and manageability with [NVIDIA AI Enterprise](https://www.nvidia.com/en-us/ai-data-science/products/triton-inference-server/get-started/). NVIDIA Dynamo will be included in NVIDIA AI Enterprise for production inference in a future release.   
  
Get a free license to try NVIDIA AI Enterprise in production for 90 days using your existing infrastructure.

[Request a 90-Day License](https://enterpriseproductregistration.nvidia.com/?LicType=EVAL&amp;ProductFamily=NVAIEnterprise)

[View NVIDIA Dynamo-Triton Licensing Options](https://www.nvidia.com/en-us/ai-data-science/products/triton-inference-server/get-started/#nv-accordion-d76f4815d2-item-cc46c5bf45)

[Contact Us to Learn More About NVIDIA Dynamo](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/contact-sales/)

### Quick-Start Guide

Learn the basics for getting started with NVIDIA Dynamo, including how to deploy a model in a disaggregated server setup and how to launch the smart router.

[Get Started](https://github.com/ai-dynamo/dynamo)

### Introductory Blog  

Read about how NVIDIA Dynamo helps simplify AI inference in production, the tools that help with deployments, and ecosystem integrations.

[Read Blog](/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/)

### Deploy LLM Inference With NVIDIA Dynamo and vLLM

NVIDIA Dynamo supports all major backends, including vLLM. Check out the tutorial to learn how to deploy with vLLM.

[Read Docs](https://github.com/ai-dynamo/dynamo/blob/main/docs/guides/)

### Multi-Node Deployment With NVIDIA Dynamo and Grove on Kubernetes

Learn how to deploy multi-node models using NVIDIA Dynamo with Grove API, which enables efficient scaling and declarative startup ordering of interdependent AI inference components across multiple nodes.

Get Started

* * *

## Starter Kits

Access technical content on inference topics like prefill optimizations, decode optimizations, and multi-GPU inference.

#### Multi-GPU Inference 

Models have grown in size and can no longer fit on a single GPU. Deploying these models involves distributing them across multiple GPUs and nodes. This kit shares key optimization techniques for multi-GPU inference.

- 

[MultiShot communication protocol](https://developer.nvidia.com/blog/3x-faster-allreduce-with-nvswitch-and-tensorrt-llm-multishot/)

- 

[Pipeline parallelism for high-concurrency efficiency](https://developer.nvidia.com/blog/boosting-llama-3-1-405b-throughput-by-another-1-5x-on-nvidia-h200-tensor-core-gpus-and-nvlink-switch/)

- 

[Large NVIDIA NVLink™ domains](https://developer.nvidia.com/blog/low-latency-inference-chapter-2-blackwell-is-coming-nvidia-gh200-nvl32-with-nvlink-switch-gives-signs-of-big-leap-in-time-to-first-token-performance/)

#### Prefill Optimizations

When a user submits a request to a large language model, it generates a KV cache to compute a contextual understanding of the request. This process is computationally intensive and requires specialized optimizations. This kit presents essential KV cache optimization techniques for inference.

- 

[Key-value (KV) cache early reuse](https://developer.nvidia.com/blog/5x-faster-time-to-first-token-with-nvidia-tensorrt-llm-kv-cache-early-reuse/)

- 

[Chunked prefill](https://developer.nvidia.com/blog/streamlining-ai-inference-performance-and-deployment-with-nvidia-tensorrt-llm-chunked-prefill/)

- 

[Supercharging multiturn interactions](https://developer.nvidia.com/blog/nvidia-gh200-superchip-accelerates-inference-by-2x-in-multiturn-interactions-with-llama-models/)

#### Decode Optimizations 

Once the LLM generates the KV cache and the first token, it moves into the decode phase, where it autoregressively generates the remaining output tokens. This kit highlights key optimization techniques for the decoding process.

- 

[Multiblock attention for long sequences](https://developer.nvidia.com/blog/nvidia-tensorrt-llm-multiblock-attention-boosts-throughput-by-more-than-3x-for-long-sequence-lengths-on-nvidia-hgx-h200/)

- 

[Speculative decoding for accelerated throughput](https://developer.nvidia.com/blog/tensorrt-llm-speculative-decoding-boosts-inference-throughput-by-up-to-3-6x/)

- 

[Speculative decoding with Medusa](https://developer.nvidia.com/blog/low-latency-inference-chapter-1-up-to-1-9x-higher-llama-3-1-performance-with-medusa-on-nvidia-hgx-h200-with-nvlink-switch/)

#### Topology Optimized Serving on Kubernetes

AI workloads have evolved into complex multi-component systems spanning multiple nodes. Grove bridges AI inference frameworks and Kubernetes scheduling, enabling efficient scaling and declarative startup ordering of interdependent components through unified custom resources. This kit introduces Grove&#39;s capabilities and guides you through topology-optimized model deployment on Kubernetes.

- 

Optimizing the Deployment of Interdependent AI Inference Components

- 

Developer Workflow of Grove API

- 

[NVIDIA Grove Github Repository](https://github.com/ai-dynamo/grove)

* * *

#### NVIDIA Blackwell Delivers Unmatched Performance and ROI for AI Inference

The NVIDIA Blackwell platform—including NVFP4 low precision format, fifth-generation NVIDIA NVLink and NVLink Switch, and the NVIDIA TensorRT-LLM and NVIDIA Dynamo inference frameworks—enables the highest AI factory revenue: A $5M investment in GB200 NVL72 generates $75 million in token revenue—a 15x return on investment. This includes development with community frameworks such as SGLang, vLLM, and more.

[Explore technical results](https://developer.nvidia.com/blog/nvidia-blackwell-leads-on-new-semianalysis-inferencemax-benchmarks/)

![NVIDIA Rivermax provides real-time streaming for the Las Vegas Sphere, world’s largest LED display](https://developer.download.nvidia.com/images/tensorrt/inference-tech-blog-sa-external-think-smart-1920x1080.png)

* * *

## More Resources

 ![Decorative image representing forums](https://developer.download.nvidia.com/images/omniverse/m48-people-group.svg)
### Explore Developer Discord

 ![](https://developer.download.nvidia.com/images/isaac/m48-certification-ribbon-2-256px-blk.png)
### Get Training and Certification  

 ![](https://developer.download.nvidia.com/icons/m48-developer-1.svg)
### Watch Dynamo Office Hours On-Demand

 ![Decorative image representing forums](https://developer.download.nvidia.com/icons/m48-email-settings.svg)
### Sign Up for Inference-Related Developer News

 ![](https://developer.download.nvidia.com/icons/m48-misc-question-faq.svg)
### Read NVIDIA Dynamo FAQ

 ![](https://developer.download.nvidia.com/icons/m48-developer-1.svg)
### Join the NVIDIA Developer Program

* * *

## Ethical AI   

NVIDIA believes trustworthy AI is a shared responsibility, and we have established policies and practices to support the development of AI across a wide array of applications. When downloading or using this model in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   
  
For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety &amp; Security, and Privacy Subcards. Please report security vulnerabilities or NVIDIA AI concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Get Started With NVIDIA Dynamo Today

[Download Now](https://github.com/ai-dynamo/dynamo)


