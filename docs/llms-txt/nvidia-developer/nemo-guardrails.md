# Source: https://developer.nvidia.com/nemo-guardrails.md

1. [Topics](/topics)

[AI](/topics/ai)
2. [Generative AI](/topics/ai/generative-ai)

NVIDIA NeMo Guardrails   

# NVIDIA NeMo Guardrails for Developers  

NVIDIA NeMo™ Guardrails is a scalable solution for orchestrating AI guardrails that keep agentic AI applications safe, reliable, and aligned. It allows you to define, orchestrate, and enforce guardrails for topic control, PII detection, retrieval-augmented generation (RAG) grounding, jailbreak prevention, and multilingual, multimodal content safety with reasoning capabilities—all with low latency and seamless integration. Extensible and customizable, NeMo Guardrails integrates with frameworks like LangChain, LangGraph, and LlamaIndex; supports multi-agent deployments; and leverages GPU acceleration for low-latency performance. It works out of the box with [NVIDIA Nemotron™](/nemotron) models packaged as [NVIDIA NIM™ microservices](https://build.nvidia.com/search?q=nemoguard) and available on [Hugging Face](https://huggingface.co/collections/nvidia/nemoguard)—covering content safety, topic control, and jailbreak detection—alongside a [growing ecosystem of AI safety models](https://docs.nvidia.com/nemo/guardrails/latest/user-guides/guardrails-library.html), rails, and observability tools. NeMo Guardrails is part of the larger [NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/) software suite for building, monitoring, and optimizing AI agents across their lifecycle.

[Access Library](https://github.com/NVIDIA-NeMo/Guardrails &quot;Github Repo&quot;)[Try Microservice](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/containers/guardrails?version=25.09 &quot;Download Workflows&quot;)[Documentation  
](https://docs.nvidia.com/nemo/guardrails/latest/index.html &quot;Download Workflows&quot;)

* * *

## See NVIDIA NeMo Guardrails in Action

Enforce content safety, RAG grounding, and jailbreak prevention while building secure, compliant AI agents. This video demonstrates how NeMo Guardrails streamlines guardrail orchestration for safer, more reliable AI applications.

https://www.youtube.com/embed/Hg2KibOvnLM?
 
* * *

## How NVIDIA NeMo Guardrails Works

NeMo Guardrails provides components for building a robust, scalable guardrail solution for LLM applications and agents. It evaluates user inputs and model responses based on use-case-specific policies, providing an additional layer of safeguards beyond what’s natively available.

Key Benefits:

- 

**Programmable Policies:** Supports customizable content moderation, PII detection, topic relevance, and jailbreak detection tailored to your industry and use case.

- 

**Effective Orchestration:** Screens both user inputs and model outputs and effectively orchestrates multiple rails with the lowest latency.

- 

**Enterprise-Grade Support and Scale:** Handles high volume and scale to multiple applications with enterprise-grade support.

- 

**Flow Management:** Blocks, filters, or tailors next action or responses based on your requirements with flexible actions.

### Introductory Blog  

Simplify building trustworthy LLM apps with AI guardrails for safety, security, and control.

[Read Blog](https://developer.nvidia.com/blog/nvidia-enables-trustworthy-safe-and-secure-large-language-model-conversational-systems/)

### Deploy Guardrails Tutorial  

Run inference with parallel rails using NeMo Guardrails microservice.

[Access Tutorial](https://github.com/NVIDIA/GenerativeAIExamples/blob/main/nemo/NeMo-Guardrails/Parallel_Rails_Tutorial.ipynb)

### Example Configurations  

The configurations in this folder showcase various features of NeMo Guardrails, including using a specific LLM and enabling streaming and fact-checking.

[Explore   
Examples](https://docs.nvidia.com/nemo/guardrails/getting-started/3-demo-use-case/README.html)

### Customer Assistant Example

Learn how to integrate advanced content moderation, jailbreak detection, and topic control with NeMo Guardrails microservices.

[Try Notebook](https://github.com/NVIDIA/NeMo-Guardrails/blob/develop/examples/notebooks/safeguard_ai_virtual_assistant_notebook.ipynb)

* * *

## Ways to Get Started With NVIDIA NeMo Guardrails

Use the right tools and technologies to safeguard AI applications with NeMo Guardrails scalable AI guardrail orchestration solution.

 ![AI guardrails code](https://brand-assets.cne.ngc.nvidia.com/assets/marketing-icons/2.3.0/download.svg)
### Download  

Get free access to the NeMo Guardrails microservice for research, development, and testing. You can try the microservice through the [Safety for Agentic AI](https://build.nvidia.com/nvidia/safety-for-agentic-ai) developer example.

[Download Microservice  
](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/collections/nemo-microservices)

 ![AI guardrails code](https://developer.download.nvidia.com/images/icons/m48-coding-256px-blk.png)
### Access 

To use the latest features and source code for adding AI guardrails to LLM applications, NeMo Guardrails is available as an open-source project on GitHub.

[Access Toolkit](https://github.com/NVIDIA/NeMo-Guardrails)

 ![AI guardrails microservice](https://developer.download.nvidia.com/icons/m48-digital-deep-learning-institute-talks-training.svg)
### Try

Try the Nemotron Safety Guard models for content safety, topic control, and jailbreak detection on Hugging Face.

[Try the Models](https://huggingface.co/collections/nvidia/nemoguard)

* * *

## Performance

NeMo Guardrails enables AI guardrails to ensure that LLM responses are safe, secure, and compliant. Experience up to 1.4x improvement in detection rate with a mere half-second of latency. Keep enterprise AI operations safe and reliable by enforcing custom rules for AI models, agents, and systems. Use prepackaged [NVIDIA NIM microservices](https://developer.nvidia.com/nim) that are optimized to make it easier to deploy.

### Experience Over 1.4x Improved Detection Rate With Only Half a Second of Latency With NeMo Guardrails

Evaluated policy compliance with five AI guardrails.

 ![A chart showing 1.5X Improvement in Protection Rate With Only 30 Seconds of Latency With NeMo Guardrails](https://developer.download.nvidia.com/images/NeMo-guardrails-chart-1.4x.svg)

The benchmark shows that orchestrating up to five GPU-accelerated guardrails in parallel with NeMo Guardrails increases detection rate by 1.4x while adding only ~0.5 seconds of latency—delivering ~50% better protection without slowing down responses.

* * *

## Starter Kits

### Hero-Workflow  

Safeguard your deployments with NemoGuard NIM microservices. 

- 

[Integrate NemoGuard Microservice](https://docs.nvidia.com/nemo/microservices/latest/guardrails/tutorials/integrate-nemoguard-nims.html#guardrails-integrate-nemoguard-nims-kubernetes)

- 

[Try Microservice](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/collections/nemo-microservices)

- 

[Try the Tutorial Notebook  
  
](https://github.com/NVIDIA/GenerativeAIExamples/blob/main/nemo/NeMo-Guardrails/Parallel_Rails_Tutorial.ipynb)

### Guardrails for RAG   

Enhance content safety with programmable guardrails while building RAG apps delivering context-aware responses from vast multimodal enterprise data sources.

- 

[Try Blueprint](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline)

- 

[Tutorial](https://github.com/NVIDIA-AI-Blueprints/rag)

### Guardrails Evaluation  

Measure the effectiveness and performance of AI guardrails in generative AI applications with an evaluation tool through NeMo Guardrails.

- 

[Try Microservice](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/collections/nemo-microservices)

- 

[Read Blog](https://developer.nvidia.com/blog/measuring-the-effectiveness-and-performance-of-ai-guardrails-in-generative-ai-applications/)

* * *

## NVIDIA NeMo Guardrails Learning Library  

* * *

## More Resources

 ![AI guardrails community](https://developer.download.nvidia.com/images/omniverse/m48-people-group.svg)
### Explore the Community  

 ![AI guardrails training](https://developer.download.nvidia.com/images/isaac/m48-certification-ribbon-2-256px-blk.png)
### Get Training and Certification  

 ![AI guardrails startup](https://developer.download.nvidia.com/images/isaac/m48-ai-startup-256px-blk.png)
### Accelerate Your Startup  

* * *

## Ethical AI

NVIDIA’s platforms and application frameworks enable developers to build a wide array of AI applications. Consider potential algorithmic bias when choosing or creating the models being deployed. Work with the model’s developer to ensure that it meets the requirements for the relevant industry and use case; that the necessary instructions and documentation are provided to understand error rates, confidence intervals, and results; and that the model is being used under the conditions and in the manner intended.

# Get started with NeMo Guardrails today.

[Download Now](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/collections/nemo-microservices)


