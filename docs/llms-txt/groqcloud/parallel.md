# Source: https://console.groq.com/docs/parallel

---
description: Learn how to use Parallel with Groq to build AI research agents that access real-time web data, compare information sources, and deliver accurate insights with ultra-fast inference.
title: Parallel + Groq: Fast Web Search for Real-Time AI Research - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [Parallel + Groq: Fast Web Search for Real-Time AI Research](#parallel--groq-fast-web-search-for-realtime-ai-research)

[Parallel](https://parallel.ai) provides a web search MCP server that gives AI models access to real-time web data. Combined with Groq's industry-leading inference speeds (1000+ tokens/second), you can build research agents that find and analyze current information in seconds, not minutes.

**Key Features:**

* **Real-Time Information:** Access current events, breaking news, and live data
* **Parallel Processing:** Search multiple sources simultaneously
* **Ultra-Fast:** Groq's inference makes tool calling nearly instant
* **Source Transparency:** See exactly which websites were searched
* **Accurate Results:** Fresh data means current answers, not outdated information

## [Quick Start](#quick-start)

#### [1\. Install the required packages:](#1-install-the-required-packages)

curl

```
pip install openai python-dotenv
```

#### [2\. Get your API keys:](#2-get-your-api-keys)

* **Groq:** [console.groq.com/keys](https://console.groq.com/keys)
* **Parallel:** [platform.parallel.ai](https://platform.parallel.ai)

curl

```
export GROQ_API_KEY="your-groq-api-key"
export PARALLEL_API_KEY="your-parallel-api-key"
```

#### [3\. Create your first real-time research agent:](#3-create-your-first-realtime-research-agent)

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
        server_label="parallel_web_search",
        server_url="https://mcp.parallel.ai/v1beta/search_mcp/",
        headers={"x-api-key": os.getenv("PARALLEL_API_KEY")},
        type="mcp",
        require_approval="never",
    )
]

response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="What does Anthropic do? Find recent product launches from past year.",
    tools=tools,
    temperature=0.1,
    top_p=0.4,
)

print(response.output_text)
```

## [Advanced Examples](#advanced-examples)

### [Multi-Company Comparison](#multicompany-comparison)

Compare multiple companies side-by-side:

Python

```
companies = ["OpenAI", "Anthropic", "Google AI", "Meta AI"]

for company in companies:
    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input=f"""Research {company}:
        - Main products
        - Latest announcements (6 months)
        - Company size and funding
        - Key differentiators""",
        tools=tools,
        temperature=0.1,
    )
    print(f"{company}:\n{response.output_text}\n")
```

### [Real-Time Market Data](#realtime-market-data)

Get current financial information:

Python

```
stocks = ["GOOGL", "MSFT", "NVDA", "TSLA"]

for ticker in stocks:
    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input=f"Current stock price of {ticker}? Include today's change and 52-week range.",
        tools=tools,
        temperature=0.1,
    )
    print(f"{ticker}: {response.output_text}")
```

### [Breaking News Monitoring](#breaking-news-monitoring)

Track developing stories:

Python

```
topics = [
    "artificial intelligence breakthroughs",
    "quantum computing developments",
    "renewable energy innovations"
]

for topic in topics:
    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input=f"Latest breaking news about {topic} from today?",
        tools=tools,
        temperature=0.1,
    )
    print(f"{topic}:\n{response.output_text}\n")
```

## [Performance Comparison](#performance-comparison)

Real comparison from testing:

* **Groq (openai/gpt-oss-120b):** 11.15s, 472 chars/sec
* **OpenAI (gpt-5):** 88.38s, 42 chars/sec

**Groq is 8x faster** due to LPU architecture, instant tool call decisions, and fast synthesis of search results.

**Challenge:** Build a real-time market intelligence platform that monitors news, tracks competitor activities, analyzes trends, compares products, and generates daily briefings!

## [Additional Resources](#additional-resources)

* [Parallel Documentation](https://docs.parallel.ai)
* [Parallel Platform](https://platform.parallel.ai)
* [Groq Responses API](https://console.groq.com/docs/api-reference#responses)