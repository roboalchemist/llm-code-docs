# Perplexity with LangChain
Source: https://docs.perplexity.ai/docs/getting-started/integrations/langchain

Use Perplexity's chat models and search tool in your LangChain applications.

## Overview

The `langchain-perplexity` package provides LangChain integrations for Perplexity's API, enabling you to build LLM applications with real-time web search capabilities.

<Info>
  **LangChain** is a popular Python framework for building applications powered by large language models. It provides composable components for chains, agents, and retrieval-augmented generation (RAG). Learn more at [langchain.com](https://www.langchain.com).
</Info>

The integration includes:

* **ChatPerplexity** - Chat model with Pro Search, streaming, and search controls
* **PerplexitySearchRetriever** - Retriever for RAG applications
* **PerplexitySearchResults** - Tool for LangChain agents

## Installation

<Tabs>
  <Tab title="pip">
    ```bash theme={null}
    pip install langchain-perplexity
    ```
  </Tab>

  <Tab title="uv">
    ```bash theme={null}
    uv add langchain-perplexity
    ```
  </Tab>
</Tabs>

## API Key Setup

Set your Perplexity API key as an environment variable:

```python theme={null}
import os

os.environ["PPLX_API_KEY"] = "your_api_key_here"
```

<Card title="Get API Key" icon="key" href="https://www.perplexity.ai/settings/api">
  Generate your API key from the Perplexity dashboard.
</Card>

## Quick Start: Chat Models

Use `ChatPerplexity` for conversational AI with web search:

```python theme={null}
from langchain_perplexity import ChatPerplexity

chat = ChatPerplexity(model="sonar")

response = chat.invoke("What are the latest developments in AI?")
print(response.content)
```

### Pro Search

Enable multi-step reasoning with Pro Search:

```python theme={null}
from langchain_perplexity import ChatPerplexity, WebSearchOptions

chat = ChatPerplexity(
    model="sonar-pro",
    web_search_options=WebSearchOptions(search_type="pro")
)

response = chat.invoke("How does the electoral college work?")
