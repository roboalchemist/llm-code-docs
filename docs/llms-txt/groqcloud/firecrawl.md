# Source: https://console.groq.com/docs/firecrawl

---
description: Learn how to use Firecrawl with Groq to build enterprise-grade web scraping, structured data extraction, and deep research applications with fast inference.
title: Firecrawl + Groq: AI-Powered Web Scraping &amp; Data Extraction - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [Firecrawl + Groq: AI-Powered Web Scraping & Data Extraction](#firecrawl--groq-aipowered-web-scraping--data-extraction)

[Firecrawl](https://firecrawl.dev) is an enterprise-grade web scraping platform that turns any website into clean, AI-ready data. Combined with Groq's fast inference through MCP, you can build intelligent agents that scrape websites, extract structured data, and conduct deep research with natural language instructions.

**Key Features:**

* **Enterprise Web Scraping:** Handles JavaScript, authentication, and anti-bot detection automatically
* **Structured Extraction:** Define JSON schemas and get consistent data across sources
* **Deep Research:** Multi-hop reasoning that synthesizes information from multiple pages
* **Batch Processing:** Scrape multiple URLs efficiently with parallel processing
* **Fast Results:** Sub-10 second responses when combined with Groq's inference

## [Quick Start](#quick-start)

#### [1\. Install the required packages:](#1-install-the-required-packages)

curl

```
pip install openai python-dotenv
```

#### [2\. Get your API keys:](#2-get-your-api-keys)

* **Groq:** [console.groq.com/keys](https://console.groq.com/keys)
* **Firecrawl:** [firecrawl.dev/app/api-keys](https://firecrawl.dev/app/api-keys)

curl

```
export GROQ_API_KEY="your-groq-api-key"
export FIRECRAWL_API_KEY="your-firecrawl-api-key"
```

#### [3\. Create your first web scraping agent:](#3-create-your-first-web-scraping-agent)

Python

```
import os
from openai import OpenAI
from openai.types import responses as openai_responses

client = OpenAI(
    base_url="https://api.groq.com/api/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

tools = [
    openai_responses.tool_param.Mcp(
        server_label="firecrawl",
        server_url=f"https://mcp.firecrawl.dev/{os.getenv('FIRECRAWL_API_KEY')}/v2/mcp",
        type="mcp",
        require_approval="never",
    )
]

response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="Scrape https://console.groq.com/docs/models and provide an overview of available models",
    tools=tools,
    temperature=0.1,
    top_p=0.4,
)

print(response.output_text)
```

## [Advanced Examples](#advanced-examples)

### [Structured Data Extraction](#structured-data-extraction)

Extract data in specific JSON formats across multiple sources:

Python

```
response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="""Extract pricing from https://openai.com, https://anthropic.com, https://groq.com
    
    Return JSON:
    {
        "company_name": "string",
        "pricing_plans": [{"plan_name": "string", "price": "string", "features": ["string"]}]
    }""",
    tools=tools,
    temperature=0.1,
)

print(response.output_text)
```

### [Deep Research & Multi-Hop Analysis](#deep-research--multihop-analysis)

Conduct comprehensive research across multiple sources:

Python

```
response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="""Research "latest trends in AI model inference speed and performance":
    1. Recent developments (2024-2025)
    2. Key companies and technologies
    3. Performance benchmarks
    4. Future trends
    
    Provide a comprehensive report with citations.""",
    tools=tools,
    temperature=0.1,
)

print(response.output_text)
```

### [Batch Web Scraping](#batch-web-scraping)

Scrape multiple URLs in parallel:

Python

```
response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="""Batch scrape these URLs and summarize key findings:
    - https://arxiv.org/abs/2401.xxxxx
    - https://arxiv.org/abs/2402.xxxxx
    - https://arxiv.org/abs/2403.xxxxx""",
    tools=tools,
    temperature=0.1,
)

print(response.output_text)
```

## [Available Firecrawl MCP Tools](#available-firecrawl-mcp-tools)

Firecrawl MCP provides several powerful tools for web scraping, data extraction, and research:

| Tool                                | Description                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| **firecrawl\_scrape**               | Scrape content from a single URL with advanced options and formatting                 |
| **firecrawl\_batch\_scrape**        | Scrape multiple URLs efficiently with built-in rate limiting and parallel processing  |
| **firecrawl\_check\_batch\_status** | Check the status of a batch operation and retrieve results                            |
| **firecrawl\_search**               | Search the web and optionally extract content from search results                     |
| **firecrawl\_crawl**                | Start an asynchronous crawl with advanced options for depth and link following        |
| **firecrawl\_extract**              | Extract structured information from web pages using LLM capabilities and JSON schemas |
| **firecrawl\_deep\_research**       | Conduct comprehensive deep web research with intelligent crawling and LLM analysis    |
| **firecrawl\_generate\_llmstxt**    | Generate standardized llms.txt files that define how LLMs should interact with a site |

**Challenge:** Build an AI-powered competitive intelligence system that monitors competitor websites, extracts key business metrics, and generates automated reports using Firecrawl and Groq!

## [Additional Resources](#additional-resources)

For more detailed documentation and resources on building web intelligence applications with Groq and Firecrawl, see:

* [Firecrawl Documentation](https://docs.firecrawl.dev)
* [Firecrawl API Reference](https://docs.firecrawl.dev/api-reference)
* [Firecrawl MCP Server](https://mcp.firecrawl.dev)
* [Groq API Cookbook: Firecrawl MCP Tutorial](https://github.com/groq/groq-api-cookbook/blob/main/tutorials/03-mcp/mcp-firecrawl/mcp-firecrawl.ipynb)
* [Groq Responses API Documentation](https://console.groq.com/docs/api-reference#responses)