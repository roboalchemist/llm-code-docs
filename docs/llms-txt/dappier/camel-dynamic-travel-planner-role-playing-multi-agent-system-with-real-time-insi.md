# 🐫 CAMEL Dynamic Travel Planner Role-Playing: Multi-Agent System with Real-Time Insights Powered by Dappier
Source: https://docs.dappier.com/cookbook/recipes/camel-dynamic-travel-planner-role-playing



You can also check this cookbook in colab [here](https://colab.research.google.com/drive/1yYFcgQ0rdAvepTclqLvZR8icqsW4uc-P?usp=sharing)

This notebook demonstrates how to set up and leverage CAMEL's multi-agent combined with Dappier for dynamic travel planning. By combining real-time data and multi-agent role-playing, this notebook walks you through an innovative approach to creating adaptive travel plans.

In this notebook, you'll explore:

* **CAMEL**: A powerful multi-agent framework that enables multi-agent role-playing scenarios, allowing for sophisticated AI-driven tasks.
* **Dappier**: A platform connecting LLMs and Agentic AI agents to real-time, rights-cleared data from trusted sources, specializing in domains like web search, finance, and news. It delivers enriched, prompt-ready data, empowering AI with verified and up-to-date information for diverse applications.
* **OpenAI**: A leading provider of advanced AI models capable of natural language understanding, contextual reasoning, and content generation. It enables intelligent, human-like interactions and supports a wide range of applications across various domains.
* **AgentOps**: Track and analysis the running of CAMEL Agents.

This setup not only demonstrates a practical application of AI-driven dynamic travel planning but also provides a flexible framework that can be adapted to other real-world scenarios requiring real-time data integration from Dappier, multi-agent collaboration, and contextual reasoning.

## Watch the Video Guide

If you prefer a visual walkthrough, check out the accompanying video guide below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/RwB8O7L3mhU?si=2Iyc3Zab0RFNcpnx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## 📦 Installation

First, install the CAMEL package with all its dependencies:

```bash  theme={null}
!pip install "camel-ai[all]==0.2.16"
```

## 🔑 Setting Up API Keys

You'll need to set up your API keys for OpenAI, Dappier and AgentOps.
This ensures that the tools can interact with external services securely.

You can go to [here](https://platform.dappier.com/profile/api-keys) to get API Key from Dappier with **free** credits. The API Key could be found under Settings -> Profile.

```python Python theme={null}
import os
from getpass import getpass