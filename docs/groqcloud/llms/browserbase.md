# Source: https://console.groq.com/docs/browserbase

---
description: Learn how to use BrowserBase with Groq to build intelligent browser automation systems that navigate websites, extract data, and test applications at scale.
title: BrowserBase + Groq: Scalable Browser Automation with AI - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [BrowserBase + Groq: Scalable Browser Automation with AI](#browserbase--groq-scalable-browser-automation-with-ai)

[BrowserBase](https://browserbase.com) provides cloud-based headless browser infrastructure that makes browser automation simple and scalable. Combined with Groq's fast inference through MCP, you can control browsers using natural language instructions.

**Key Features:**

* **Natural Language Control:** Describe actions in plain English instead of writing selectors
* **Cloud Infrastructure:** No browser instances or server resources to manage
* **Anti-Detection:** Bypass bot-detection automatically with built-in stealth
* **Session Persistence:** Maintain cookies and authentication across requests
* **Visual Documentation:** Capture screenshots and recordings for debugging

## [Quick Start](#quick-start)

#### [1\. Install the required packages:](#1-install-the-required-packages)

curl

```
pip install openai python-dotenv
```

#### [2\. Get your setup:](#2-get-your-setup)

* **Groq API Key:** [console.groq.com/keys](https://console.groq.com/keys)
* **BrowserBase Account:** [browserbase.com](https://browserbase.com)
* **Smithery MCP URL:** [smithery.ai/server/@browserbasehq/mcp-browserbase](https://smithery.ai/server/@browserbasehq/mcp-browserbase)

Connect your BrowserBase credentials at Smithery and copy your MCP URL.

curl

```
export GROQ_API_KEY="your-groq-api-key"
export SMITHERY_MCP_URL="your-smithery-mcp-url"
```

#### [3\. Create your first browser automation agent:](#3-create-your-first-browser-automation-agent)

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
    "server_url": os.getenv("SMITHERY_MCP_URL"),
    "server_label": "browserbase",
    "require_approval": "never"
}]

response = client.responses.create(
    model="qwen/qwen3-32b",
    input="Navigate to https://news.ycombinator.com and extract the top 3 headlines",
    tools=tools,
    temperature=0.1,
    top_p=0.4
)

print(response.output_text)
```

## [Advanced Examples](#advanced-examples)

### [Multi-Step Workflows](#multistep-workflows)

Chain multiple browser actions together:

Python

```
response = client.responses.create(
    model="qwen/qwen3-32b",
    input="""Navigate to https://example.com/login
    Fill in username: [email protected]
    Fill in password: demo123
    Click login button
    Wait for dashboard
    Extract all table data""",
    tools=tools,
    temperature=0.1
)

print(response.output_text)
```

### [E-commerce Price Monitoring](#ecommerce-price-monitoring)

Automate price tracking across retailers:

Python

```
urls = [
    "https://amazon.com/product1",
    "https://walmart.com/product1",
    "https://target.com/product1"
]

for url in urls:
    response = client.responses.create(
        model="qwen/qwen3-32b",
        input=f"Navigate to {url} and extract product name, price, and availability",
        tools=tools,
        temperature=0.1
    )
    print(response.output_text)
```

### [Form Automation](#form-automation)

Automate form filling:

Python

```
response = client.responses.create(
    model="qwen/qwen3-32b",
    input="""Navigate to https://example.com/contact
    Fill form with:
    - Name: John Doe
    - Email: [email protected]
    - Message: Interested in your services
    Submit form and confirm submission""",
    tools=tools,
    temperature=0.1
)

print(response.output_text)
```

## [Available BrowserBase Actions](#available-browserbase-actions)

| Action                           | Description                     |
| -------------------------------- | ------------------------------- |
| **browserbase\_create\_session** | Start a new browser session     |
| **browserbase\_navigate**        | Navigate to any URL             |
| **browserbase\_click**           | Click on elements               |
| **browserbase\_type**            | Type text into input fields     |
| **browserbase\_screenshot**      | Capture page screenshots        |
| **browserbase\_get\_content**    | Extract page content            |
| **browserbase\_wait**            | Wait for elements or page loads |
| **browserbase\_scroll**          | Scroll to load dynamic content  |

**Challenge:** Build an automated lead generation system that visits business directories, extracts contact information, validates emails, and stores results—all controlled by natural language!

## [Additional Resources](#additional-resources)

* [BrowserBase Documentation](https://docs.browserbase.com)
* [BrowserBase Dashboard](https://browserbase.com/overview)
* [Smithery MCP: BrowserBase](https://smithery.ai/server/@browserbasehq/mcp-browserbase)
* [Groq Responses API](https://console.groq.com/docs/api-reference#responses)