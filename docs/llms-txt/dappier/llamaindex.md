# LlamaIndex
Source: https://docs.dappier.com/integrations/llama-index-integration



[**LlamaIndex**](https://www.llamaindex.ai/) is a data framework designed to connect custom
data sources with large language models (LLMs). It helps in structuring, indexing, and
querying data, making it easy for LLMs to understand and retrieve relevant information
efficiently. LlamaIndex supports a wide variety of data connectors and offers tools for
building powerful retrieval-augmented generation (RAG) applications.

[**Dappier**](https://dappier.com/developers/) is a platform that connects
LLMs and Agentic AI agents to real-time, rights-cleared data from trusted
sources, including web search, finance, and news. By providing enriched,
prompt-ready data, Dappier empowers AI with verified and up-to-date
information for a wide range of applications.

## Overview

The LlamaIndex integration with [Dappier](https://dappier.com/) allows developers to enhance their LLM applications with real-time search and AI-powered recommendation tools. By leveraging Dappier’s pre-trained, RAG-ready APIs, LLMs can retrieve accurate, up-to-date information across key domains such as news, finance, weather, sports, and lifestyle content. This integration includes two tools:

* **DappierRealTimeSearchToolSpec**: Enables LLMs to access live web and financial data using natural language queries.
* **DappierAIRecommendationsToolSpec**: Provides intelligent content recommendations from trusted media sources based on user intent and query context.

Together, these tools help ensure your LLM outputs are factual, relevant, and enriched with trusted real-world data.

## Installation

To get started, install the required Python packages:

```bash  theme={null}
!pip install llama-index llama-index-tools-dappier
```

## Setup API Keys

To authenticate and use Dappier tools, you’ll need a valid API key. You can generate one for free from your [Dappier API dashboard](https://platform.dappier.com/profile/api-keys).

Once you have the key, set it in your environment using the following code:

```python Python theme={null}
import os
from getpass import getpass