# 🕵🏻 Building an AI-Powered Travel Itinerary Assistant using OpenAI Agents SDK and Dappier
Source: https://docs.dappier.com/cookbook/recipes/open-ai-agent-travel-assistant



You can also check this cookbook in colab [here](https://colab.research.google.com/drive/1HVMyM-O5KviSBXO56H6_ssQLH1C9okFN?usp=sharing)

## Introduction

This notebook provides a **step-by-step guide** to building an **AI-powered travel assistant** using **OpenAI's Agents SDK** and **Dappier**. The assistant generates a **real-time travel itinerary** based on user input, fetching **weather updates, live events, and hotel deals** dynamically.

## Watch the Video Guide

If you prefer a visual walkthrough, check out the accompanying video guide below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/4aU8BK8pfmU?si=bEgCtPqcQmFLZIsu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## OpenAI Agents SDK

The OpenAI Agents SDK enables you to build **agentic AI applications** with a **lightweight and production-ready** API.

It consists of:

* **Agents** – LLMs equipped with instructions and tools
* **Handoffs** – Delegation of tasks to specialized agents
* **Guardrails** – Input validation for enhanced reliability

The SDK also provides **built-in tracing** for debugging and evaluation, making **AI-powered workflows easy to build and scale**.

***

## Dappier

Dappier is a **real-time AI data platform** that connects **LLMs and AI agents** to **rights-cleared data from trusted sources**.

It specializes in **web search, finance, news, and live events**, ensuring AI applications can **access up-to-date and verified information** without hallucinations.

***

## Install Dependencies

```bash  theme={null}
!pip install openai-agents dappier colorama nest-asyncio
```

***

## Import Required Libraries

```python Python theme={null}
import os
import getpass
import nest_asyncio
import asyncio
from agents import Agent, FunctionTool, Runner, function_tool
from colorama import Fore, Style
from dappier import Dappier
from openai.types.responses import ResponseTextDeltaEvent
```

***

## Set Up API Keys Securely

To prevent **exposing API keys in shared environments**, use **getpass** to enter them securely.

```python Python theme={null}
os.environ["DAPPIER_API_KEY"] = getpass.getpass("Enter your Dappier API Key: ")
os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API Key: ")
```

Initialize Dappier Client:

```python Python theme={null}
dappier_client = Dappier(api_key=os.environ["DAPPIER_API_KEY"])
```

Enable **tracing for OpenAI Agents SDK**:

```python Python theme={null}
from agents import set_tracing_export_api_key

set_tracing_export_api_key(os.environ["OPENAI_API_KEY"])
```

***

## Define AI Functions for Real-Time Data Fetching

### Fetching Real-Time Search Results

This function fetches real-time search results from Dappier based on the user's query.

```python Python theme={null}