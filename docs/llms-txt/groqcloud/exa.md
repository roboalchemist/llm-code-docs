# Source: https://console.groq.com/docs/exa

---
description: Learn how to use Exa with Groq to build intelligent search applications that find relevant content, research companies, and discover information with semantic understanding.
title: Exa + Groq: AI-Powered Web Search &amp; Content Discovery - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [Exa + Groq: AI-Powered Web Search & Content Discovery](#exa--groq-aipowered-web-search--content-discovery)

[Exa](https://exa.ai) is an AI-native search engine built specifically for LLMs. Unlike keyword-based search, Exa understands meaning and context, returning high-quality results that AI models can process. Combined with Groq's fast inference through MCP, you can build intelligent search applications that find exactly what you need in seconds.

**Key Features:**

* **Semantic Understanding:** Searches by meaning, not just keywords
* **AI-Ready Results:** Clean, structured data designed for LLM consumption
* **Company Research:** Dedicated tools for researching businesses
* **Content Extraction:** Pull full article content from any URL
* **LinkedIn Search:** Find companies and people on professional networks
* **Deep Research:** Multi-hop research synthesizing multiple sources

## [Quick Start](#quick-start)

#### [1\. Install the required packages:](#1-install-the-required-packages)

curl

```
pip install openai python-dotenv
```

#### [2\. Get your API keys:](#2-get-your-api-keys)

* **Groq:** [console.groq.com/keys](https://console.groq.com/keys)
* **Exa:** [dashboard.exa.ai/api-keys](https://dashboard.exa.ai/api-keys)

curl

```
export GROQ_API_KEY="your-groq-api-key"
export EXA_API_KEY="your-exa-api-key"
```

#### [3\. Create your first intelligent search agent:](#3-create-your-first-intelligent-search-agent)

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
    "server_url": f"https://mcp.exa.ai/mcp?exaApiKey={os.getenv('EXA_API_KEY')}",
    "server_label": "exa",
    "require_approval": "never",
}]

response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="Find recent breakthroughs in quantum computing research",
    tools=tools,
    temperature=0.1,
    top_p=0.4,
)

print(response.output_text)
```

## [Advanced Examples](#advanced-examples)

### [Company Research](#company-research)

Deep dive into a company:

Python

```
response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="""Research Anthropic:
    - What they do
    - Main products
    - Recent news and announcements
    - Company size and funding
    Use company_research tool""",
    tools=tools,
    temperature=0.1,
)

print(response.output_text)
```

### [Content Extraction](#content-extraction)

Extract and analyze article content:

Python

```
response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="""Extract content from these AI inference articles:
    - https://example.com/article1
    - https://example.com/article2
    
    Summarize key points and trends""",
    tools=tools,
    temperature=0.1,
)

print(response.output_text)
```

### [LinkedIn Professional Search](#linkedin-professional-search)

Find companies in specific industries:

Python

```
response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="""Find AI infrastructure startups on LinkedIn:
    - 50-200 employees
    - SF or NYC
    - Founded last 3 years
    Use linkedin_search for detailed profiles""",
    tools=tools,
    temperature=0.1,
)

print(response.output_text)
```

## [Available Exa Search Tools](#available-exa-search-tools)

| Tool                        | Description                                           |
| --------------------------- | ----------------------------------------------------- |
| **web\_search\_exa**        | Semantic web search understanding meaning and context |
| **company\_research**       | Research companies by crawling official websites      |
| **crawling**                | Extract complete content from specific URLs           |
| **linkedin\_search**        | Search LinkedIn with specific criteria                |
| **deep\_researcher\_start** | Begin comprehensive multi-hop research                |
| **deep\_researcher\_check** | Check status and retrieve completed reports           |

**Challenge:** Build an automated market intelligence system that monitors your industry for competitors, tracks technology trends, identifies customers, and generates weekly reports!

## [Additional Resources](#additional-resources)

* [Exa Documentation](https://docs.exa.ai)
* [Exa MCP Reference](https://docs.exa.ai/reference/exa-mcp)
* [Exa MCP GitHub](https://github.com/exa-labs/exa-mcp-server)
* [Groq Responses API](https://console.groq.com/docs/api-reference#responses)