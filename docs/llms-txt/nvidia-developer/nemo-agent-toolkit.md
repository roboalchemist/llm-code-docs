# Source: https://developer.nvidia.com/nemo-agent-toolkit.md

1. [Topics](/topics)

[AI](/topics/ai)
2. [Generative AI](/topics/ai/generative-ai)

NeMo Agent Toolkit

# NVIDIA NeMo Agent Toolkit

NVIDIA NeMo™ Agent Toolkit is an open-source AI framework for building, profiling, and optimizing agents and tools from any framework, enabling unified, cross-framework integration across connected [AI agent](https://www.nvidia.com/en-us/glossary/ai-agents/) systems. By exposing hidden bottlenecks and costs and optimizing the workflow, it helps enterprises scale [agentic systems](https://www.nvidia.com/en-us/glossary/multi-agent-systems/) efficiently while maintaining reliability.

NeMo Agent Toolkit is part of the [NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/) software suite for managing the AI agent lifecycle, providing telemetry, orchestration, and observability tools that accelerate development, uncover bottlenecks, and streamline performance across multi-agent systems.

[Access GitHub](https://github.com/NVIDIA/NeMo-Agent-Toolkit)[Documentation](https://docs.nvidia.com/nemo/agent-toolkit/latest/index.html)[Forum](https://forums.developer.nvidia.com/tags/c/ai-data-science/nvidia-nemo/715/nemo-agent-toolkit)

* * *

## See NeMo Agent Toolkit in Action
  

| 
- [**Create Your Own AI Agent**](https://www.youtube.com/watch?v=NsogD7UhZ4Q)

 | 18:31 |
| 
- [**Benchmarking and Optimizing AI Agents**](https://www.youtube.com/watch?v=CpuOJwVFmCg&amp;t)

 | 11:04 |
| 
- [**How To Develop Teams of AI Agents**](https://www.youtube.com/watch?v=H65OluZaiZQ)

 | 23:06 |
| 
- [**Optimize Your AI Agent Workflows**](https://www.youtube.com/watch?v=yrqdvBLAI3k)

 | 05:29 |

* * *

## How NeMo Agent Toolkit Works

NVIDIA NeMo Agent Toolkit provides unified monitoring and optimization for AI agent systems, working across LangChain, CrewAI, and custom frameworks. It captures granular metrics on cross-agent coordination, tool usage efficiency, and computational costs, enabling data-driven optimizations through NVIDIA Accelerated Computing. It can be used to parallelize slow workflows, cache expensive operations, and maintain and evaluate system accuracy quickly. Compatible with OpenTelemetry and major agent frameworks, the toolkit reduces cloud spend and enhances performance while providing insights to scale from single agents to enterprise-grade digital workforces.  
  
NeMo Agent Toolkit supports the Model Context Protocol (MCP), enabling developers to use the toolkit to access tools served by remote MCP servers, or as a server to make their own tools available to others via MCP. This means agents built with the toolkit can easily use any tool registered in an MCP registry.

### Simplify Development  

Experiment and prototype new agentic AI applications quickly and easily with the toolkit’s YAML configuration builder. With universal descriptors for agents, tools, and workflows, you can flexibly choose and connect agent frameworks best suited to each task in a workflow. Access a reusable collection of tools, pipelines, and agentic workflows to ease the development of agentic AI systems.

### Accelerate Development and Improve Reliability  

Build agentic systems with ease and repeatability. In the tool registry, access the best [retrieval-augmented generation (RAG)](https://www.nvidia.com/en-us/glossary/retrieval-augmented-generation/) architectures, workflows, and search tools available across your organization, or leverage the [AI-Q NVIDIA Blueprint](https://build.nvidia.com/nvidia/aiq), built with NVIDIA NIM™ and NeMo. With the AI-Q blueprint, developers have an example to build highly accurate, scalable multimodal ingestion and [RAG](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline?ncid=pa-srch-goog-898408-API-Build-Exact) pipelines that connect AI agents to enterprise data and reasoning for various use cases, including AI agents for research and reporting.

### Streamline Agent Optimization   

Use the Agent Hyperparameter Optimizer to automatically select the best hyperparameters, such as the type of large language model (LLM), its temperature, and max\_token, by optimizing the agentic workflow on metrics including accuracy, groundedness, latency, token counts, or custom. The toolkit also supports prompt optimization to further refine agent performance. This allows developers to quickly identify optimal settings for agents, tools, and workflows, reducing trial and error while accelerating innovation across projects.

### Accelerate Agent Responses   

Use fine-grained telemetry to enhance agentic AI workflows. This profiling data can be used by [NVIDIA NIM](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/?ncid=pa-srch-goog-157409-prsp) and [NVIDIA Dynamo](/dynamo) to optimize the performance of agentic systems. These forecasted metrics—which can include details about an inference call to an LLM for a particular agent, such as what prompt is in memory, where it might reside, and which other agents are likely to call it—can be used to drive a more efficient workflow, enabling better business outcomes without requiring an upgrade to underlying infrastructure.

### Increase Accuracy   

Evaluate an agentic system’s accuracy using metrics collected with NeMo Agent Toolkit, and connect them with your preferred observability and orchestration tools. Understand and debug inputs and outputs for each component in an agentic workflow, and identify areas for improvement. Swap out tools or models and use the toolkit’s YAML config to quickly reevaluate the pipeline to understand its impact.

 ![A flowchart showing how NeMo Agent Toolkit works](https://developer.download.nvidia.com/images/in-action-diagram.jpg)

### Introductory Blog

Learn how to leverage AI code generation with NeMo Agent Toolkit to build a test-driven coding agent.

[Read Blog](https://developer.nvidia.com/blog/improve-ai-code-generation-using-nvidia-agentiq-open-source-toolkit/)

### Introductory Video

Watch a video walk-through to see how you can get started with NeMo Agent Toolkit.

[Watch Video](https://www.youtube.com/watch?v=H65OluZaiZQ)

### Tutorial Blog

Take a technical deep dive to learn how to extend the toolkit by adding integration with an additional agentic framework, such as Agno.

[Read Blog](https://developer.nvidia.com/blog/extending-the-nvidia-agent-intelligence-toolkit-to-support-new-agentic-frameworks/)

### Notebooks

Through this series of notebooks, we demonstrate how you can use NeMo Agent Toolkit to build, connect, evaluate, profile, and deploy an agentic system.

[Explore Notebooks](https://github.com/NVIDIA/NeMo-Agent-Toolkit/tree/develop/examples/notebooks)

* * *

## Get Started With NeMo Agent Toolkit

### Quick Install With Pip (Recommended)

    pip install nvidia-nat # Verify the library installation: nat --help nat --version

### Local Installer Instructions (For running examples)

    # Clone the repo: git clone -b main git@github.com:NVIDIA/NeMo-Agent-Toolkit.git nemo-agent-toolkit cd nemo-agent-toolkit # Initialize the Git repository: git submodule update --init --recursive # Download the datasets: git lfs install git lfs fetch git lfs pull # Create a Python environment: uv sync --all-groups --all-extras uv venv --python 3.12 --seed .venv source .venv/bin/activate uv sync --all-groups --all-extras # Verify the library installation: nat --help nat --version

**Note:** For the instructions above, you must have uv already installed. If you do not, to install uv, get started [here](https://docs.astral.sh/uv/getting-started/installation/).

* * *

## Starter Kits

Start developing agentic AI applications with NeMo Agent Toolkit with tutorials, best practices, and documentation. The [AI-Q NVIDIA Blueprint](https://blogs.nvidia.com/ai-agents-blueprint/) showcases [examples](https://github.com/NVIDIA-AI-Blueprints/aiq-research-assistant) for building agentic workflows that use the toolkit.

#### Getting Started With NeMo Agent Toolkit  

Access the toolkit documentation, and start building, connecting, and evaluating agentic AI systems.

- 

[Get Quick-Start Setup Guide](https://docs.nvidia.com/nemo/agent-toolkit/latest/quick-start/installing.html)

- 

[Read Troubleshooting Guide](https://docs.nvidia.com/nemo/agent-toolkit/latest/troubleshooting.html)

- 

[Read Release Notes](https://docs.nvidia.com/nemo/agent-toolkit/latest/release-notes.html)

* * *

## NeMo Agent Toolkit Learning Library

Tech Blog 

### How To Scale Your LangGraph Agents

**NVIDIA NeMo Agent Toolkit**  
  
This post will cover the tools and techniques from NVIDIA NeMo Agent Toolkit that can be used to deploy and scale an agentic AI application into production.

Video 

### Benchmarking and Optimizing AI Agents

**NVIDIA NeMo Agent Toolkit**  
  
In this step-by-step tutorial, we show you how to get started using the NeMo Agent Toolkit test time compute module with searching, editing, scoring, and selection.

Video 

### Connect MCP Tools and NVIDIA NIM for Building Optimized Agentic Systems

**NVIDIA NeMo Agent Toolkit**  
  
Discover how the latest release of NVIDIA NeMo Agent Toolkit streamlines multi-agent interoperability through deep Model Context Protocol (MCP) integration.

Video 

### How To Build Custom AI Agents

**NVIDIA NeMo Agent Toolkit**  
  
Learn how to use the toolkit to build custom AI agents and add advanced AI capabilities into your projects.

Tech Blog 

### Extending NeMo Agent Toolkit To Support New Agentic Frameworks   

**NVIDIA NeMo Agent  Toolkit**  
  
Take a technical deep dive to learn how to extend the toolkit by adding integration with an additional agentic framework, such as Agno.

Video 

### How To Develop Teams of AI Agents

**NVIDIA NeMo Agent Toolkit**  
  
Learn how to use NeMo Agent Toolkit Python library to build agentic AI applications in this step-by-step tutorial video.

Video 

### Optimize Your AI Agent Workflows

**NVIDIA NeMo Agent Toolkit**  
  
Learn how to use the toolkit profiler to get deeper insights into the performance and behavioral characteristics of your AI agent workflows.

Tech Blog 

### Improving AI Code Generation

**NVIDIA NeMo Agent Toolkit, USD, Cosmos**  
  
Learn how to leverage AI code generation with the toolkit to build a test-driven coding agent.

Documentation 

### NeMo Agent Toolkit Documentation

**NVIDIA NeMo Agent Toolkit**  
  
Read a troubleshooting guide, release notes, quick-start guide, and more to get started.

Guide 

### Building Multi-Agent Systems the Easy Way

**NVIDIA NeMo Agent Toolkit**  
  
Read a hands-on guide to using the toolkit, including what you can build, what’s under the hood, and more, published by The BIG DATA guy.

Tech Blog 

### Scaling Synthetic Data Generation With Multi-Agent AI

**NVIDIA NeMo Agent Toolkit, USD, NVIDIA Cosmos™**  
  
Learn about a multi-agent approach utilizing generative AI for the systematic, automated creation of top-tier synthetic datasets to advance physical AI development and deployment.

Tech Blog 

### Chat With Your Enterprise Data Through Open-Source AI-Q NVIDIA Blueprint

**NVIDIA NeMo Agent Toolkit**  
  
Read how you can get started with AI-Q, a free reference implementation for building advanced AI agents.

* * *

## More Resources

 ![Decorative image representing forums](https://developer.download.nvidia.com/images/omniverse/m48-people-group.svg)
### Explore the Community  

 ![](https://developer.download.nvidia.com/images/isaac/m48-certification-ribbon-2-256px-blk.png)
### Get Training and Certification  

 ![](https://developer.download.nvidia.com/images/isaac/m48-ai-startup-256px-blk.png)
### Read the FAQ

## Ethical AI   

NVIDIA believes trustworthy AI is a shared responsibility, and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure their model meets the requirements for the relevant industry and use case and addresses unforeseen product misuse.   
  
For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety and Security, and Privacy Subcards. Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Get started with NeMo Agent Toolkit today.

[Access GitHub](http://github.com/NVIDIA/AgentIQ)


