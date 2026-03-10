# Source: https://console.groq.com/docs/browseruse

---
description: Learn how to use Browser Use with Groq to build AI agents that autonomously browse websites, compare products, and conduct real-time research with fast inference.
title: Browser Use + Groq: Intelligent Web Research &amp; Product Comparison - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [Browser Use + Groq: Intelligent Web Research & Product Comparison](#browser-use--groq-intelligent-web-research--product-comparison)

[Browser Use](https://browser-use.com) enables AI models to autonomously browse the web and extract information through natural language instructions. Combined with Groq's fast inference speeds, you can build research agents that deliver comprehensive insights in seconds.

**Key Features:**

* **Autonomous Browsing:** AI navigates websites and clicks links without pre-programmed scripts
* **Natural Language:** Describe research tasks—the AI figures out how to execute them
* **Multi-Source Comparison:** Gather and compare information across different websites automatically
* **Real-Time Data:** Access live information beyond any LLM's training cutoff
* **Fast Execution:** Groq's 500+ tokens/second enables rapid decision-making

## [Quick Start](#quick-start)

#### [1\. Install required packages:](#1-install-required-packages)

curl

```
pip install openai python-dotenv
```

#### [2\. Get your API keys:](#2-get-your-api-keys)

* **Groq:** [console.groq.com/keys](https://console.groq.com/keys)
* **Browser Use:** [browser-use.com](https://browser-use.com)

curl

```
export GROQ_API_KEY="your-groq-api-key"
export BROWSER_USE_API_KEY="your-browser-use-api-key"
```

#### [3\. Create your first web research agent:](#3-create-your-first-web-research-agent)

Python

```
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/api/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
    timeout=300
)

tools = [{
    "type": "mcp",
    "server_url": "https://api.browser-use.com/mcp/",
    "server_label": "browseruse",
    "require_approval": "never",
    "headers": {"X-Browser-Use-API-Key": os.getenv("BROWSER_USE_API_KEY")}
}]

response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="What's the current price of Google stock?",
    instructions="Use browseruse tools to find accurate, up-to-date information. Keep tasks focused and fast.",
    tools=tools,
    temperature=0.3,
    top_p=0.8,
    timeout=300
)

print(response.output_text)
```

## [Advanced Examples](#advanced-examples)

### [Product Comparison](#product-comparison)

Compare products across multiple retailers:

Python

```
response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="""Compare iPhone 16 Pro across:
    - Apple.com
    - Amazon.com
    - Best Buy
    
    For each: price, availability, promotions, shipping""",
    tools=tools,
    temperature=0.3
)

print(response.output_text)
```

### [Competitive Analysis](#competitive-analysis)

Monitor competitors:

Python

```
companies = ["OpenAI", "Anthropic", "Mistral AI"]

for company in companies:
    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input=f"""Research {company}:
        - Latest product announcements
        - Pricing information
        - Recent news
        - Key differentiators""",
        tools=tools,
        temperature=0.3
    )
    print(f"\n{company}:\n{response.output_text}")
```

### [Real-Time Market Data](#realtime-market-data)

Get current financial information:

Python

```
stocks = ["GOOGL", "MSFT", "NVDA"]

for ticker in stocks:
    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input=f"Get current stock price, daily change, and 52-week high/low for {ticker}",
        tools=tools,
        temperature=0.3
    )
    print(f"{ticker}: {response.output_text}")
```

## [Available Browser Use Tools](#available-browser-use-tools)

| Tool                           | Description                                          |
| ------------------------------ | ---------------------------------------------------- |
| **browser\_task**              | Execute complex browsing tasks with natural language |
| **get\_browser\_task\_status** | Check status of running browser tasks                |
| **create\_session**            | Start new browser session with persistent state      |
| **navigate\_to\_url**          | Direct navigation to specific URLs                   |
| **extract\_data**              | Extract specific data from web pages                 |
| **interact\_with\_page**       | Click, type, and interact with page elements         |

**Challenge:** Build an automated deal finder that monitors shopping sites, compares prices, tracks changes, and alerts you when the best deals appear!

## [Additional Resources](#additional-resources)

* [Browser Use Documentation](https://docs.browser-use.com)
* [Browser Use Platform](https://browser-use.com)
* [Groq Responses API](https://console.groq.com/docs/api-reference#responses)