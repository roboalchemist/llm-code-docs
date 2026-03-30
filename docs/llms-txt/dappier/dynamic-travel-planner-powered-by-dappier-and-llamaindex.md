# 🦙 Dynamic Travel Planner | Powered by Dappier and LlamaIndex
Source: https://docs.dappier.com/cookbook/recipes/llama-index-dyamic-travel-planner



[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pYi-KMWPx_wbPfo5iZmYASWwsc8o8eiY?usp=sharing)

This notebook demonstrates how to build a real-time, LLM-powered travel assistant by combining LlamaIndex with Dappier. It walks through creating a dynamic 2-day itinerary for New York City based on current news, weather conditions, and hotel availability.

In this notebook, you’ll explore:

* **Dappier**: A platform that connects LLMs and agentic AI agents to real-time, rights-cleared data from trusted sources. It delivers verified, prompt-ready information across domains like web search, finance, news, and more.

* **LlamaIndex**: A data framework that allows seamless integration of external tools with LLMs. It enables structured workflows for tool use, reasoning, and response generation.

* **OpenAI**: An advanced AI model provider used here to power the assistant’s reasoning, planning, and response generation.

This setup offers a practical example of building context-aware applications with real-time data access. It can be easily extended to other domains requiring live insights and AI-driven decision-making.

## Watch the Video Guide

If you prefer a visual walkthrough, check out the accompanying video guide below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/x2AF66YTP1g?si=QQGv7Ifd-LpUUu4Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Installation

To get started with the dynamic travel planner, install the required packages:

```bash  theme={null}
pip install llama-index llama-index-tools-dappier openai
```

## Setup API Keys

To authenticate and use Dappier and OpenAI, you’ll need valid API keys.

You can generate one for free from your [Dappier API dashboard](https://platform.dappier.com/profile/api-keys).

```python Python theme={null}
import os
from getpass import getpass