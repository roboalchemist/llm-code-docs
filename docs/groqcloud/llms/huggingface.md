# Source: https://console.groq.com/docs/huggingface

---
description: Learn how to use HuggingFace with Groq to discover trending models, explore datasets, and access the latest AI resources with fast inference and MCP integration.
title: HuggingFace + Groq: Real-Time Model &amp; Dataset Discovery - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [HuggingFace + Groq: Real-Time Model & Dataset Discovery](#huggingface--groq-realtime-model--dataset-discovery)

[HuggingFace](https://huggingface.co) hosts over 500,000 models and 100,000 datasets. Combined with HuggingFace's MCP server and Groq's fast inference, you can build intelligent agents that discover, analyze, and recommend models and datasets using natural language—accessing information about resources published hours ago, not months.

**Key Features:**

* **Real-Time Discovery:** Access models and datasets published recently, beyond LLM training cutoffs
* **Trending Models:** Find what's popular right now in the AI community
* **Smart Recommendations:** AI-powered suggestions based on your use case
* **Dataset Exploration:** Discover datasets by task, modality, size, or domain
* **Model Analysis:** Detailed information about architectures and performance
* **Fast Responses:** Sub-5 second queries with Groq's inference

## [Quick Start](#quick-start)

#### [1\. Install the required packages:](#1-install-the-required-packages)

curl

```
pip install openai python-dotenv
```

#### [2\. Get your API keys:](#2-get-your-api-keys)

* **Groq:** [console.groq.com/keys](https://console.groq.com/keys)
* **HuggingFace:** [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

curl

```
export GROQ_API_KEY="your-groq-api-key"
export HF_TOKEN="your-huggingface-token"
```

#### [3\. Create your first model discovery agent:](#3-create-your-first-model-discovery-agent)

Python

```
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/api/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

tools = [{
    "type": "mcp",
    "server_url": "https://huggingface.co/mcp",
    "server_label": "huggingface",
    "require_approval": "never",
    "headers": {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"},
}]

response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="Find the top trending AI model on HuggingFace and tell me about it",
    tools=tools,
    temperature=0.1,
    top_p=0.4,
)

print(response.output_text)
```

## [Advanced Examples](#advanced-examples)

### [Find Models for Specific Tasks](#find-models-for-specific-tasks)

Discover models optimized for your use case:

Python

```
tasks = [
    "text-to-image generation with high quality",
    "code generation in multiple languages",
    "multilingual translation for Asian languages",
    "sentiment analysis for customer reviews"
]

for task in tasks:
    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input=f"Find best models for: {task}. Include downloads and recent updates.",
        tools=tools,
        temperature=0.1,
    )
    print(f"{task}:\n{response.output_text}\n")
```

### [Dataset Discovery](#dataset-discovery)

Find the perfect dataset for training:

Python

```
response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="""Find datasets for customer support chatbot:
    - Conversational data
    - English language
    - At least 10K examples
    - Recently updated (2024-2025)
    - Include licensing info""",
    tools=tools,
    temperature=0.1,
)

print(response.output_text)
```

### [Model Comparison](#model-comparison)

Compare multiple models:

Python

```
response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="""Compare text-to-image models:
    - Stable Diffusion XL
    - DALL-E variants on HF
    - Midjourney alternatives
    
    For each: size, speed, quality metrics, hardware requirements, licensing""",
    tools=tools,
    temperature=0.1,
)

print(response.output_text)
```

## [Available HuggingFace Tools](#available-huggingface-tools)

| Tool                         | Description                                                 |
| ---------------------------- | ----------------------------------------------------------- |
| **search\_models**           | Search for models by name, task, framework, or organization |
| **get\_model\_info**         | Get detailed information about a specific model             |
| **list\_trending\_models**   | Find currently trending models across categories            |
| **search\_datasets**         | Search for datasets by task, size, language, or modality    |
| **get\_dataset\_info**       | Get detailed information about a specific dataset           |
| **list\_trending\_datasets** | Find currently trending datasets                            |

**Challenge:** Build an automated model monitoring system that tracks releases in your domain, evaluates them against requirements, notifies you of promising models, and generates weekly digests!

## [Additional Resources](#additional-resources)

* [HuggingFace Hub Documentation](https://huggingface.co/docs/hub)
* [HuggingFace MCP Server](https://huggingface.co/settings/mcp)
* [HuggingFace Models](https://huggingface.co/models)
* [HuggingFace Datasets](https://huggingface.co/datasets)
* [Groq Responses API](https://console.groq.com/docs/api-reference#responses)