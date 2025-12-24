# Source: https://developer.nvidia.com/nemo-evaluator.md

1. [Topics](/topics)

[AI](/topics/ai)
2. [Generative AI](/topics/ai/generative-ai)

NVIDIA NeMo Evaluator

# NVIDIA NeMo Evaluator for Developers

NVIDIA NeMo™ Evaluator is a scalable solution for evaluating generative AI applications—including large language models (LLMs), retrieval-augmented generation (RAG) pipelines, and AI agents—available as both an open-source SDK for experimentation and a cloud-native microservice for automated, enterprise-grade workflows. NeMo Evaluator SDK supports over 100 built-in academic benchmarks and an easy-to-follow process for adding customizable metrics via open-source contribution. In addition to academic benchmarks, NeMo Evaluator microservice provides LLM-as-a-judge scoring, RAG, and agent metrics that make it easy to assess and optimize models across environments. NeMo Evaluator is a part of the NVIDIA NeMo™ software suite for building, monitoring, and optimizing AI agents across their lifecycle at enterprise scale.

[Access SDK Quickstart](https://github.com/NVIDIA-NeMo/Evaluator?tab=readme-ov-file#-quickstart &quot;Access SDK Quickstart &quot;)[Download Microservice](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/containers/evaluator?version=25.09 &quot;Download Microservice&quot;)[Documentation](https://docs.nvidia.com/nemo/microservices/latest/evaluate/index.html &quot;Documentation&quot;)

* * *

## NVIDIA NeMo Evaluator Key Features

NeMo Evaluator is built on a single-core engine that powers both the open-source SDK and the enterprise-ready microservice.

# SDK

An open-source SDK for running academic benchmarks with reproducibility and scale. Built on the [nemo-evaluator core and launcher](https://github.com/NVIDIA-NeMo/Evaluator?tab=readme-ov-file#how-it-works-launcher-and-core-engine), it provides code-native access for experimentation on LLMs, embeddings, and reranking models.

- 

Reproducible by default: Captures configs, seeds, and software provenance for auditable, repeatable results.

- 

Comprehensive benchmarks: Over 100 academic benchmarks across leading harnesses and modalities, [continuously updated](https://github.com/NVIDIA-NeMo/Evaluator?tab=readme-ov-file#supported-benchmarks-and-evaluation-harnesses).

- 

Python-native and ready to run: Configs and containers deliver results directly in notebooks or scripts.

- 

Flexible and scalable: Run locally with Docker or scale out to Slurm clusters.

[Go to GitHub](https://github.com/NVIDIA-NeMo/Evaluator)

# Microservice

An enterprise-grade, cloud-native REST API that automates scalable evaluation pipelines. Teams can submit jobs, configure parameters, and monitor results centrally—ideal for CI/CD integration and production-ready generative AI operations workflows.

- 

Automates scalable evaluation pipelines with a simple REST API.

- 

Abstracts complexity: Submit “jobs,” configure parameters, and monitor results centrally.

[Try Microservice](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/containers/evaluator?version=25.09)

 
* * *

## How NVIDIA NeMo Microservices Evaluator Works

NeMo Evaluator microservice allows a user to run various evaluation jobs for agentic AI applications through a REST API. Evaluation flows enabled include: academic benchmarking, agentic and RAG metrics, and LLM-as-a-judge. A user can also tune their judge model via the prompt optimization feature.

![Diagram of how NeMo evaluator works](https://developer.download.nvidia.com/images/nemo-llm/llm-diagram-evaluator.jpg)

* * *

## Introductory Resources

### Introductory Blog  

Read how the NeMo Evaluator microservice simplifies end-to-end evaluation of generative AI systems.

[Read Blog](/blog/streamline-evaluation-of-llms-for-accuracy-with-nvidia-nemo-evaluator/)

### Tutorial Notebook

Explore tutorials designed to help you evaluate generative AI models with the NeMo Evaluator microservice.

[Explore Tutorials](https://github.com/NVIDIA/GenerativeAIExamples/tree/main/nemo/Evaluator)

### Introductory Webinar

Understand the architecture of data flywheels and their role in enhancing agentic AI systems and learn best practices for integrating NeMo components to optimize AI agent performance.

[Watch Now](https://www.nvidia.com/en-us/events/supercharge-agentic-ai-build-scalable-data-flywheels/)

### How-To Blog  

Dive deeper into how NVIDIA NeMo microservices help build data flywheels with a case study and a quick overview of the steps in an end-to-end pipeline.

[Read Blog](/blog/enhance-your-ai-agent-with-data-flywheels-using-nvidia-nemo-microservices/)

* * *

## Ways to Get Started With NVIDIA NeMo Evaluator

Use the right tools and technologies to assess generative AI models and pipelines across academic and custom LLM benchmarks on any platform.

 ![](https://developer.download.nvidia.com/icons/m48-download.svg)
# Download

Get free access to the NeMo Evaluator microservice for research, development, and testing.

[Download Microservice](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/containers/evaluator?version=25.09)

 ![Buiild icon](https://developer.download.nvidia.com/icons/m48-coding.svg)
### Access

Get free access to the NeMo Evaluator microservice for research, development, and testing.

[Access SDK](https://github.com/NVIDIA-NeMo/Evaluator?tab=readme-ov-file#-quickstart)

 ![](https://developer.download.nvidia.com/images/isaac/m48-digital-deep-learning-institute-talks-training.svg)
# Try

Jump-start building your AI solutions with NVIDIA AI Blueprints, customizable reference applications, available on the NVIDIA API catalog.

[Try the Blueprint](https://build.nvidia.com/nvidia/build-an-enterprise-data-flywheel)

* * *

## See NVIDIA NeMo Evaluator Microservice in Action

Watch these demos to see how the NeMo Evaluator microservice simplifies the evaluation and optimization of AI agents, RAG, and LLMs.

### Evaluate LLMs With NeMo Evaluator and Docker Compose

This step-by-step guide walks through deploying the NeMo Evaluator microservice using Docker Compose and running custom evaluations.

[Watch Video](https://www.youtube.com/watch?v=Fo9kNJE5nC8)

### Scale AI Agent Evaluation With NeMo Evaluator LLM-as-a-Judge

In this step-by-step tutorial, you’ll discover how to scale your AI agent evaluation workflows with NeMo Evaluator LLM-as-a-judge.

[Watch Video](https://www.youtube-nocookie.com/watch?v=IDXWrlWKr4c)

### Set Up a Data Flywheel to Optimize AI Models and Agents

Get an overview of the data flywheel blueprint, understand how to do model evaluation and cost optimization, explore the evaluation report, and more.

[Watch Video](https://www.youtube.com/watch?v=rjLUm_7CDkM&amp;t=133s)

### Customizing AI Agents for Tool Calling With NeMo Microservices

Learn how to customize AI agents for precise function calling with this end-to-end example with NeMo microservices. 

[Watch Video](https://www.youtube.com/watch?v=TX-NNK2FRdY)

* * *

## Starter Kits

### LLM-as-a-Judge

Automate subjective evaluation of open-ended responses, RAG systems, or AI agents. Ensures structured scoring and consistency.

- 

[Try Microservice](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/containers/evaluator?version=25.09)

- 

[Read Docs](https://docs.nvidia.com/nemo/microservices/latest/evaluate/flows/llm-as-a-judge.html)

- [Try the Tutorial Notebook](https://github.com/NVIDIA/GenerativeAIExamples/blob/main/nemo/Evaluator/LLMAsAJudge/LLM%20As%20a%20Judge.ipynb)  

### Similarity Metrics

Measure how well LLMs or retrieval models handle domain-specific queries using F1, ROUGE, or other metrics.

- 

[Try Microservice](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/containers/evaluator?version=25.09)

- 

[Read Docs](https://docs.nvidia.com/nemo/microservices/latest/evaluate/flows/template.html#chat-completion-tasks)

- [Try the Tutorial Notebook](https://github.com/NVIDIA/GenerativeAIExamples/blob/main/nemo/Evaluator/GettingStarted/Getting%20Started%20with%20NeMo%20Evaluator.ipynb)

- 

[Try the RAG Evaluation Tutorial Notebook](https://github.com/NVIDIA/GenerativeAIExamples/blob/main/nemo/Evaluator/EmbeddingAndRAG/NeMo_Evaluator_Retriever_and_RAG_Evaluation.ipynb)

- 

[Try the Retrieval Evaluation With Synthetic Data Notebook](https://github.com/NVIDIA/GenerativeAIExamples/tree/main/nemo/retriever-synthetic-data-generation)

### Agent Evaluation 

Evaluate whether agents call the right functions with the correct parameters; integrates with CI/CD pipelines.

- 

[Try Microservice](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/containers/evaluator?version=25.09)

- [Try the Tutorial ](https://docs.nvidia.com/nemo/microservices/latest/evaluate/flows/agentic.html)

### LLM Benchmarks

Standardized evaluation of model performance across reasoning, math, coding, and instruction-following. Supports regression testing.

- 

[Try Microservice](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/containers/evaluator?version=25.09)

- 

[Read Docs](https://docs.nvidia.com/nemo/microservices/latest/evaluate/flows/academic-benchmarks/index.html)

- [Try the Tutorial Notebook](https://github.com/NVIDIA/GenerativeAIExamples/blob/main/nemo/Evaluator/GettingStarted/Getting%20Started%20with%20NeMo%20Evaluator.ipynb)

* * *

## NVIDIA NeMo Evaluator Learning Library

* * *

## More Resources

 ![](https://developer.download.nvidia.com/images/omniverse/m48-people-group.svg)
### Explore the Community  

 ![](https://developer.download.nvidia.com/images/isaac/m48-certification-ribbon-2-256px-blk.png)
### Get Training and Certification  

 ![](https://developer.download.nvidia.com/images/isaac/m48-ai-startup-256px-blk.png)
### Meet the Program for Startups  

## Ethical AI   

NVIDIA believes Trustworthy AI is a shared responsibility, and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. Please report security vulnerabilities or NVIDIA AI concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

**Get started with NeMo Evaluator today.**

[Download Now](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo-microservices/collections/nemo-microservices &quot;Download Now&quot;)


