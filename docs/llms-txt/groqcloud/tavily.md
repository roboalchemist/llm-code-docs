# Source: https://console.groq.com/docs/tavily

---
description: Learn how to use Tavily with Groq to build AI agents that search the web, extract content from pages, and crawl websites with advanced filtering and real-time access.
title: Tavily + Groq: Real-Time Search, Scraping &amp; Crawling for AI - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [Tavily + Groq: Real-Time Search, Scraping & Crawling for AI](#tavily--groq-realtime-search-scraping--crawling-for-ai)

[Tavily](https://tavily.com) is a comprehensive web search, scraping, and crawling API designed specifically for AI agents. It provides real-time web access, content extraction, and advanced search capabilities. Combined with Groq's ultra-fast inference through MCP, you can build intelligent agents that research topics, monitor websites, and extract structured data in seconds.

**Key Features:**

* **Multi-Modal Search:** Web search, content extraction, and crawling in one API
* **AI-Optimized Results:** Clean, structured data designed for LLM consumption
* **Advanced Filtering:** Search by date range, domain, content type, and more
* **Content Extraction:** Pull complete article content from any URL
* **Search Depth Control:** Choose between basic and advanced search
* **Fast Execution:** Groq's inference makes synthesis nearly instant

## [Quick Start](#quick-start)

#### [1\. Install the required packages:](#1-install-the-required-packages)

curl

```
pip install openai python-dotenv
```

#### [2\. Get your API keys:](#2-get-your-api-keys)

* **Groq:** [console.groq.com/keys](https://console.groq.com/keys)
* **Tavily:** [app.tavily.com](https://app.tavily.com/home)

curl

```
export GROQ_API_KEY="your-groq-api-key"
export TAVILY_API_KEY="your-tavily-api-key"
```

#### [3\. Create your first research agent:](#3-create-your-first-research-agent)

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
    "server_url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={os.getenv('TAVILY_API_KEY')}",
    "server_label": "tavily",
    "require_approval": "never",
}]

response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="What are recent AI startup funding announcements?",
    tools=tools,
    temperature=0.1,
    top_p=0.4,
)

print(response.output_text)
```

## [Advanced Examples](#advanced-examples)

### [Time-Filtered Research](#timefiltered-research)

Search within specific time ranges:

Python

```
response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="""Find AI model releases from past month.
    Use tavily_search with:
    - time_range: month
    - search_depth: advanced
    - max_results: 10
    
    Provide details about models, companies, and capabilities.""",
    tools=tools,
    temperature=0.1,
)

print(response.output_text)
```

### [Product Information Extraction](#product-information-extraction)

Extract structured product data:

Python

```
response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="""Find iPhone models on apple.com.
    Use tavily_search then tavily_extract to get:
    - Model names
    - Prices
    - Key features
    - Availability""",
    tools=tools,
    temperature=0.1,
)

print(response.output_text)
```

### [Multi-Source Content Extraction](#multisource-content-extraction)

Extract and compare content from multiple URLs:

Python

```
urls = [
    "https://example.com/article1",
    "https://example.com/article2",
    "https://example.com/article3"
]

response = client.responses.create(
    model="openai/gpt-oss-120b",
    input=f"""Extract content from: {', '.join(urls)}
    
    Analyze and compare:
    - Main themes
    - Key differences in perspective
    - Common facts
    - Author conclusions""",
    tools=tools,
    temperature=0.1,
)

print(response.output_text)
```

## [Available Tavily Tools](#available-tavily-tools)

| Tool                      | Description                                                    |
| ------------------------- | -------------------------------------------------------------- |
| **tavily\_search**        | Search with advanced filters (time, depth, topic, max results) |
| **tavily\_extract**       | Extract full content from specific URLs                        |
| **tavily\_scrape**        | Scrape single pages with clean output                          |
| **tavily\_batch\_scrape** | Scrape multiple URLs in parallel                               |
| **tavily\_crawl**         | Crawl websites with depth and pattern controls                 |

### [Search Parameters](#search-parameters)

**Search Depth:**

* `basic` \- Fast, surface-level results (under 3 seconds)
* `advanced` \- Comprehensive, deep results (5-10 seconds)

**Time Range:**

* `day`, `week`, `month`, `year`

**Topic:**

* `general`, `news`

**Challenge:** Build an automated content curation system that monitors news sources, filters by relevance, extracts key information, generates summaries, and publishes daily digests!

## [Additional Resources](#additional-resources)

* [Tavily Documentation](https://docs.tavily.com)
* [Tavily API Reference](https://docs.tavily.com/api-reference)
* [Tavily App](https://app.tavily.com/home)
* [Groq Responses API](https://console.groq.com/docs/api-reference#responses)