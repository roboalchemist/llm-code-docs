# 🦜 Automated Sports News Summarizer | Powered by Dappier and Langchain
Source: https://docs.dappier.com/cookbook/recipes/langchain-sports-news-summarizer



You can also check this cookbook in colab [here](https://colab.research.google.com/drive/1clJx_ILu5rwBwEAsZgfZQiJ7Xgb_NZZ9?usp=sharing)

This notebook demonstrates how to set up and leverage LangChain's powerful chaining capabilities combined with Dappier's **DappierRetriever** for automated sports news summarization. By integrating real-time sports news data and advanced language models, this notebook walks you through an innovative approach to generating concise and accurate sports news summaries.

In this notebook, you'll explore:

* **LangChain**: A versatile framework for chaining together language models and other components to create sophisticated AI-driven workflows. It enables seamless integration of LLMs with external tools and data sources, making it ideal for tasks like summarization, question-answering, and more.
* **Dappier**: A platform connecting LLMs and Agentic AI agents to real-time, rights-cleared data from trusted sources, specializing in domains like web search, finance, and news. It delivers enriched, prompt-ready data, empowering AI with verified and up-to-date information for diverse applications.
* **OpenAI**: A leading provider of advanced AI models capable of natural language understanding, contextual reasoning, and content generation. It enables intelligent, human-like interactions and supports a wide range of applications across various domains.
* **LangSmith**: A platform for debugging, testing, and monitoring LangChain applications. It provides detailed tracing and analytics to help you understand and optimize the performance of your AI workflows.

This setup not only demonstrates a practical application of AI-driven sports news summarization but also provides a flexible framework that can be adapted to other real-world scenarios requiring real-time data integration from Dappier and advanced language model capabilities.

## Watch the Video Guide

If you prefer a visual walkthrough, check out the accompanying video guide below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/unNEjxPPWdg?si=KQ2l5HvGHxYL3g24" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## 📦 Installation

First, install the Langchain Dappier integration package with all its dependencies:

```bash  theme={null}
!pip install langchain-dappier langchain-openai
```

## 🔑 Setting Up API Keys

You'll need to set up your API keys for Dappier, OpenAI and LangSmith

You can go to [here](https://platform.dappier.com/profile/api-keys) to get API Key from Dappier with **free** credits. The API Key could be found under Settings -> Profile.

```python Python theme={null}
import os
from getpass import getpass