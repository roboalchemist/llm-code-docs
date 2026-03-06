# Source: https://io.net/docs/reference/ai-agents/getting-started-with-api-agents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with AI Agents API

<Warning>
  Beta Notice: This project is in rapid development and may not be stable for production use.
</Warning>

***AI Agents*** in **IO Intelligence** are specialized assistants designed to handle a variety of tasks, from reasoning and summarization to sentiment analysis and translation. These agents leverage advanced AI capabilities to automate complex workflows, enhance decision-making, and streamline information processing.

Each ***AI Agent*** is tailored for a specific function — whether it is extracting key information, classifying data, moderating content, or translating languages. By integrating these agents into your applications, you can harness powerful AI-driven automation with ease.

### Important Note on Usage Limits

Each model within **IO Intelligence** has its own value and credit consumption rate based on its complexity, capability, and computational cost.

For **plan subscribers** (*Basic*, *Professional*, or higher tiers), all model interactions draw from a **shared usage pool**. This means you can use any model available under your plan, and your total usage will count toward a single shared credit allowance — rather than having separate limits for each model.

This shared system provides maximum flexibility, allowing you to switch between models seamlessly while staying within your daily or hourly quota.

This limit is designed to ensure fair and balanced usage for all users. If you anticipate needing a higher request limit, please consider optimizing your implementation or reach out to us for assistance.

For further details on **usage limits, full breakdown of rates, and how IO Credits are billed**, refer to the [**IO Intelligence Payments**](/guides/payment/io-intelligence-payments) page.

## Introduction

You can interact with the API using HTTP requests from any programming language or by using the official Python.

To install the official Python library, run the following command:

```
pip install iointel
```

### Example: Using the AI Agents API in Python

The following is an example of how you can use the `iointel Python` library to interact with the *IO Intelligence APIs*:

<CodeGroup>
  ```python Python theme={null}
  from iointel import (
      Agent,
      Workflow
  )

  import os
  import asyncio

  api_key = os.environ["OPENAI_API_KEY"]  # Replace with your actual IO.net API key

  text = """In the rapidly evolving landscape of artificial intelligence, the ability to condense vast amounts of information into concise and meaningful summaries is crucial. From research papers and business reports to legal documents and news articles, professionals across industries rely on summarization to extract key insights efficiently. Traditional summarization techniques often struggle with maintaining coherence and contextual relevance. However, advanced AI models now leverage natural language understanding to identify core ideas, eliminate redundancy, and generate human-like summaries. As organizations continue to deal with an ever-growing influx of data, the demand for intelligent summarization tools will only increase. Whether enhancing productivity, improving decision-making, or streamlining workflows, AI-powered summarization is set to become an indispensable asset in the digital age."""

  agent = Agent(
      name="Summarize Agent",
      instructions="You are an assistant specialized in summarization.",
      model="meta-llama/Llama-3.3-70B-Instruct",
      api_key=api_key,
      base_url="https://api.intelligence.io.solutions/api/v1"
  )

  workflow = Workflow(objective=text, client_mode=False)

  async def run_workflow():
      results = (await workflow.summarize_text(max_words=50,agents=[agent]).run_tasks())["results"]
      return results

  results = asyncio.run(run_workflow())
  print(results)
  ```
</CodeGroup>

This snippet demonstrates how to configure the client, send a chat completion request using the `Llama-3.3-70B-Instruct` agent, and retrieve a response.

<Warning>
  `run_tasks()` is now asynchronous. All usage must be wrapped inside an async function. Use asyncio.run() to execute it.
</Warning>

## Authentication

### API Keys

*IO Intelligence APIs* authenticate requests using **API keys**. You can generate API keys from the [API Keys tab](https://ai.io.net/ai/api-keys) under **IO Intelligence**.

<Warning>
  Always treat your API key as a secret. Do not share it or expose it in client-side code (e.g., browsers or mobile apps). Instead, store it securely in an environment variable or a key management service on your backend server.
</Warning>

Include the API key in an `Authorization` HTTP header for all API requests:

```
Authorization: Bearer \$IOINTELLIGENCE_API_KEY
```

### Example: List Available Agents

The following is an example `curl` command to list all agents available in **IO Intelligence**:

<CodeGroup>
  ```curl curl theme={null}
  curl https://api.intelligence.io.solutions/api/v1/agents /
    -H "Authorization: Bearer \$IOINTELLIGENCE_API_KEY" 
  ```
</CodeGroup>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/d662245a9a9e42e605edab5851966cd24a7c8ec6bea32ef23aac82f57ea300cc-agents.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=f2cd3b065a7c838f02ebfc848c7ea347" alt="" data-og-width="1870" width="1870" data-og-height="1100" height="1100" data-path="images/reference/d662245a9a9e42e605edab5851966cd24a7c8ec6bea32ef23aac82f57ea300cc-agents.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/d662245a9a9e42e605edab5851966cd24a7c8ec6bea32ef23aac82f57ea300cc-agents.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=63bb29b051e60852fdf38a76402e2892 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/d662245a9a9e42e605edab5851966cd24a7c8ec6bea32ef23aac82f57ea300cc-agents.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=a10e8750fa8afcc7c94782ebd85aadcb 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/d662245a9a9e42e605edab5851966cd24a7c8ec6bea32ef23aac82f57ea300cc-agents.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=2c42af0af2f1c910873c1ee50cd1cd93 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/d662245a9a9e42e605edab5851966cd24a7c8ec6bea32ef23aac82f57ea300cc-agents.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=869e553e7d4a1e1b4ee80f74778960bd 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/d662245a9a9e42e605edab5851966cd24a7c8ec6bea32ef23aac82f57ea300cc-agents.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=f564e510394c741b1b67340f577c3f92 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/d662245a9a9e42e605edab5851966cd24a7c8ec6bea32ef23aac82f57ea300cc-agents.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=5c1001d77cca04e1aa2def7154e0250c 2500w" />
</Frame>

This request should return a response as follows:

<CodeGroup>
  ```json json theme={null}
  {
    "agents": {
      "reasoning_agent": {
        "name": "Reasoning Agent",
        "description": "A logic-driven problem solver that breaks down complex scenarios into clear, step-by-step conclusions. Whether evaluating arguments, making inferences, or troubleshooting issues, this agent excels at structured thinking and insightful analysis.",
        "persona": null,
        "metadata": {
          "image_url": null,
          "tags": [
            "text"
          ]
        }
      },
      "summary_agent": {
        ...
      },
      "sentiment_analysis_agent": {
       ...
      },
      ...
    }
  }
  ```
</CodeGroup>

With these steps, you have successfully made your first request to the ***IO Intelligence Agents API***.

For further details on **Agents, Workflows, and API Endpoints**, check out the [IO Intelligence Agent Framework](/guides/intelligence/agent-framework).
