<!--
source: https://desearch.ai/docs/guide/integrations/rag-llamaindex
title: RAG with LlmaIndex x Desearch - Integrations Documentation | Desearch
captured: 2026-04-04
-->
# RAG with LlmaIndex x Desearch - Integrations Documentation | Desearch

Source: https://desearch.ai/docs/guide/integrations/rag-llamaindex

---

Home
Guide
API Reference
SDKs
API Console
API Status
GitHub
Discord
Blog
Search guides...
⌘K
INTRODUCTION
Desearch AI
Desearch Console
Glossary
APIS
Desearch API
Desearch x Bittensor
API Keys
Authorization
Pricing and Billing
SDK
Desearch API SDK
Python SDK Specification
JavaScript SDK Specification
INTEGRATIONS
MCP
OpenAI Wrapper
Function Calling with GPT
Function Calling with Claude
RAG with LangChain x Desearch
RAG with LlmaIndex x Desearch
ElizaOs Agents with Desearch
CrewAI Agents with Desearch
Browser Use x Desearch
OpenClaw Agent with Desearch
Numinous SN6 × Desearch Integration
USE CASES
Search Engine Use Cases
AI-Driven Chat Use Cases
Intelligent Agent Task Automation
CAPABILITIES
X (Twitter) Queries
RAG with LlmaIndex x Desearch

LlamaIndex is a framework for building LLM applications powered by structured data. In this guide, we’ll use Desearch’s LlamaIndex integration to:

This guide demonstrates how to enhance a LlamaIndex agent with Desearch’s web search capabilities.

- Specify Desearch’s Search and Retrieve Tool as a LlamaIndex retriever
- Set up an OpenAI Agent that uses this tool in its response generation

## Quick Start

### Install Required Packages

BASH
pip install llama-index llama-index-core llama-index-desearch

### Instantiate the Desearch Tool

Also ensure API keys are initialized properly. The following code uses the DESEARCH_API_KEY as the relevant environment variable name.

**Desearch API Key**
PYTHON
from llama_index_desearch.tools import DesearchToolSpec
import os

desearch_tool = DesearchToolSpec(
    api_key=os.environ["DESEARCH_API_KEY"],
)

### Select Desearch Methods to Use

For this example, we are only interested in passing the ai_search_tool method to our agent, so we specify this using the .to_tool_list LlamaIndex method.

PYTHON
search_and_retrieves_tool = desearch_tool.to_tool_list(
    spec_functions=["ai_search_tool"]
)

### Set Up the OpenAI Agent

Set up the OpenAIAgent, passing the filtered down toolset from above.

PYTHON
from llama_index.agent.openai import OpenAIAgent

agent = OpenAIAgent.from_tools(
    search_and_retrieves_tool,
    verbose=True,
)

We can then use the chat method to interact with the agent.

PYTHON
agent.chat(
    "Can you summarize the news from the last month related to the US stock market?"
)

## Desearch Tool Functions

- ai_search_tool: The Desearch API allows you to perform AI-powered web searches, gathering relevant information from multiple sources, including web pages, research papers, and social media discussions.
- twitter_search_tool: The X Search API enables users to retrieve relevant links and tweets based on specified search queries without utilizing AI-driven models. It analyzes links from X posts that align with the provided search criteria.
- web_search_tool: This API allows users to search for any information on the web. This replicates a typical search engine experience, where users can search for any information they need.

For more details, see Desearch Tool API Reference.

## Additional Resources

- Desearch Documentation
- LlamaIndex Documentation
- LlamaIndex GitHub
- Example Notebook
🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
