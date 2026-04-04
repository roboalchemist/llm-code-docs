# Source: https://developer.nvidia.com/nemo-customizer.md

1. [Topics](/topics)

[AI](/topics/ai)
2. [Generative AI](/topics/ai/generative-ai)

NVIDIA NeMo Customizer

# NVIDIA NeMo Customizer for Developers

[NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/)™ Customizer is a high-performance, scalable microservice that simplifies fine-tuning and alignment of generative AI models for building domain-specific AI agents. Through an API-first approach, this microservice supports popular [customization](https://developer.nvidia.com/blog/mastering-llm-techniques-training/) and post-training techniques such as low-rank adaptation (LoRA), full supervised fine-tuning (SFT), direct preference optimization (DPO), and Group Relative Policy Optimization (GRPO) with continued integration of the latest customization and alignment techniques.   
  
For broader reinforcement learning support with advanced RL algorithms and large-scale post-training, explore the open-source [NeMo RL library](https://docs.nvidia.com/nemo/rl/latest/index.html#), part of the NeMo framework.  
  
NeMo Customizer, part of the [NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/) software suite for managing the AI agent lifecycle, enables developers to seamlessly build [data flywheels](https://www.nvidia.com/en-us/glossary/data-flywheel/) that continuously optimize AI agents for improved performance, efficiency, and cost.

[Download Now](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/helm-charts/nemo-microservices-helm-chart &quot;Download on NGC&quot;)[Read Documentation](https://docs.nvidia.com/nemo/microservices/latest/fine-tune/index.html &quot;Read the Documentation&quot;)

* * *

## See NVIDIA NeMo Customizer in Action

Learn how NeMo Customizer enables developers to fine-tune large language models using domain-specific data—enabling the creation of tailored AI agents for tasks such as customer support, healthcare insights, enterprise automation, and many other applications.

https://www.youtube-nocookie.com/embed/TX-NNK2FRdY?
 

* * *

## How NVIDIA NeMo Customizer Works

NeMo Customizer provides an easy-to-use API that lets you customize generative AI models. Simply provide the dataset, model name, hyperparameters, and type of customization in the API payload. NeMo Customizer will initiate a job to tune the model, resulting in a customized version.  
  
The architecture diagram below illustrates the flow for using NeMo Customizer, letting you seamlessly launch multiple customization jobs. In the depicted scenario, you can utilize NeMo Customizer to create two customization workflows: one for fine-tuning and one for alignment tuning. These outputs, along with NVIDIA NIM™, allow you to deploy a customized model tailored to your specific use case.   
  
NeMo Customizer currently supports DPO and GRPO for reinforcement learning (RL). For broader RL support with advanced algorithms and large-scale post-training, explore the open-source [NeMo RL library](https://docs.nvidia.com/nemo/rl/latest/index.html#) part of the NeMo framework.

![A flowchart of how NVIDIA NeMo Customizer works](https://developer.download.nvidia.com/images/nemo-llm/llm-nemo-dz.jpg)

### Introductory Blog

Read how NeMo Customizer simplifies the alignment and customization of generative AI models.

[Read Blog](https://developer.nvidia.com/blog/maximize-ai-agent-performance-with-data-flywheels-using-nvidia-nemo-microservices/)

### Tutorials

Explore tutorials designed to help you build custom generative AI models with the NeMo Customizer microservice.

[Try Tutorials](https://docs.nvidia.com/nemo/microservices/latest/fine-tune/index.html)

### Introductory Webinar  

Learn how data flywheels enhance self-improving agentic AI systems and explore best practices for integrating NeMo components to optimize agent performance and cost-efficiency.

[Watch Now](https://www.nvidia.com/en-us/events/supercharge-agentic-ai-build-scalable-data-flywheels/)

### How-To Blog  

Dive deeper into how NVIDIA NeMo microservices help build data flywheels with a case study and a quick overview of the steps in an end-to-end pipeline.

[Read Blog](https://developer.nvidia.com/blog/enhance-your-ai-agent-with-data-flywheels-using-nvidia-nemo-microservices/)

* * *

## Ways to Get Started With NVIDIA NeMo Customizer

Get started with NeMo Customizer to simplify fine-tuning and alignment of large language models (LLMs) for domain-specific use cases, and for broader RL support with advanced algorithms and large-scale post-training, explore the open-source [NeMo RL library](https://docs.nvidia.com/nemo/rl/latest/index.html#), part of the NeMo framework.

 ![Download icon](https://developer.download.nvidia.com/icons/m48-download.svg)
### Download

Get free access to the NeMo Customizer microservice for research, development, and testing.

[Download Microservices](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/helm-charts/nemo-microservices-helm-chart?version=25.9.0)

 ![Blueprint icon](https://developer.download.nvidia.com/icons/m48-digital-deep-learning-institute-talks-training.svg)
### Try

Jump-start building your AI solutions with [NVIDIA AI Blueprints](https://www.nvidia.com/en-us/ai-data-science/ai-workflows/), customizable reference applications, available on the NVIDIA API catalog.

[Try the Blueprint](https://build.nvidia.com/nvidia/build-an-enterprise-data-flywheel)

* * *

## Performance

NeMo Customizer uses several parallelism techniques to reduce the training time for large models with support for multi-GPU and multi-node infrastructure. These methods operate together to enhance the training process, ensuring optimal use of resources and improved training performance.

**Experience 1.8x Faster Customization With NeMo Customizer**

![A chart showing 2x faster customization with NeMo Customizer](https://developer.download.nvidia.com/images/graph-nemo-training-throughput.svg)

The benchmark represents customizing Llama-3-8B on one 8xH100 80G SXM with sequence packing (4096 pack size, 0.9958 packing efficiency).   
On: customized with NeMo Customizer.   
Off: customized with leading market alternatives.

* * *

## Starter Kits

Start tuning your generative AI models with NeMo Customizer by accessing tutorials, best practices, and documentation for various use cases.

### Customizing LLMs

Get started with popular customization techniques, such as LoRA, SFT, and p-tuning.

- 

[Explore the Getting Started Guide](https://docs.nvidia.com/nemo/microservices/latest/get-started/index.html)

- 

[Try the Tutorial on Customizing and Evaluating LLMs](https://docs.nvidia.com/nemo/microservices/latest/get-started/tutorials/customize-eval-loop.html)

### Data Flywheel  

Enable self-improving agentic AI workflows by automating model optimization.

- 

[Try the Data Flywheel Blueprint](https://build.nvidia.com/nvidia/build-an-enterprise-data-flywheel)

- 

[Learn How to Get Started with the Blueprint](https://developer.nvidia.com/blog/build-efficient-ai-agents-through-model-distillation-with-nvidias-data-flywheel-blueprint/)

### NeMo RL

Open-source library with support for advanced reinforcement learning algorithms and large-scale post-training of LLMs.

- 

[Explore the Getting Started Guide](https://docs.nvidia.com/nemo/rl/latest/local-workstation.html)

- 

[Try the Tutorial to Build Reasoning Models With GRPO](https://docs.nvidia.com/nemo/rl/latest/guides/grpo-deepscaler.html)

* * *

## NVIDIA NeMo Customizer Learning Library

* * *

## More Resources

 ![](https://developer.download.nvidia.com/images/omniverse/m48-people-group.svg)
### Explore the Community  

 ![](https://developer.download.nvidia.com/images/isaac/m48-certification-ribbon-2-256px-blk.png)
### Get Training and Certification  

 ![](https://developer.download.nvidia.com/images/isaac/m48-ai-startup-256px-blk.png)
### Meet the Program for Startups  

## Ethical AI   

NVIDIA’s platforms and application frameworks enable developers to build a wide array of AI applications. Consider potential algorithmic bias when choosing or creating the models being deployed. Work with the model’s developer to ensure that it meets the requirements for the relevant industry and use case; that the necessary instruction and documentation are provided to understand error rates, confidence intervals, and results; and that the model is being used under the conditions and in the manner intended.

# Get started with NeMo Customizer today.

[Download Now](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/helm-charts/nemo-microservices-helm-chart &quot;Download Now&quot;)


