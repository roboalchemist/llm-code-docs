<!--
source: https://desearch.ai/docs/guide/integrations/rag-langchain
title: RAG with LangChain x Desearch - Integrations Documentation | Desearch
captured: 2026-04-04
-->
# RAG with LangChain x Desearch - Integrations Documentation | Desearch

Source: https://desearch.ai/docs/guide/integrations/rag-langchain

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
RAG with LangChain x Desearch

Welcome to the comprehensive guide on integrating Desearch with LangChain to enable advanced Retrieval-Augmented Generation (RAG) and agent-style workflows. Desearch is a cutting-edge, privacy-first search API that excels in delivering relevant, real-time web and Twitter content, specifically optimized for use in Large Language Model (LLM) applications.

🚀 What You’ll Learn

In this guide, you will learn:

Setting up Desearch Tools: How to configure and initialize Desearch tools within the LangChain framework.
Content Retrieval: Techniques to retrieve and utilize web and Twitter content for enhancing LLM capabilities.
RAG Pipelines and Agent Workflows: Building sophisticated RAG pipelines and agent workflows to automate and streamline information retrieval and processing.
Testing and Extending: Methods to test the integration and extend its capabilities to suit your specific needs.
📦 Installation

To get started with Desearch's LangChain integration, follow these steps:

Install the Integration: Use pip to install the necessary package.

BASH
pip install langchain-desearch

Configure API Keys: Ensure your Desearch API key is securely stored in a .env file. This key is essential for authenticating your requests to the Desearch API.

```bash
DESEARCH_API_KEY=your_api_key_here
```

## Tools Overview

Desearch provides a suite of modular tools compatible with LangChain, each designed for specific use cases:

### Search Tools

- DesearchTool: A comprehensive tool for searching across web, AI, and Twitter posts.
- BasicWebSearchTool: A lightweight tool focused solely on web searches.
- BasicTwitterSearchTool: A specialized tool for searching tweets with advanced filtering options.

### Twitter Tools

These tools are designed to interact with Twitter data:

- FetchTweetsByUrlsTool: Retrieve tweets using their URLs.
- FetchTweetsByIdTool: Fetch tweets by their unique IDs.
- FetchLatestTweetsTool: Access the latest tweets from a specified user or topic.
- FetchTweetsAndRepliesByUserTool: Gather tweets and their replies from a specific user.
- FetchRepliesByPostTool: Obtain replies to a specific tweet.
- FetchRetweetsByPostTool: Collect retweets of a particular tweet.
- FetchTwitterUserTool: Retrieve detailed information about a Twitter user.

## Quick Examples

### Basic Usage

Here's a simple example to demonstrate how to use the DesearchTool for web searches:

PYTHON
from langchain_desearch.tools import DesearchTool

# Initialize the tool
tool = DesearchTool()

# Run a search query
response = tool._run(
    prompt="Bittensor network activity",
    tool=["web"],
    model="NOVA",
    date_filter="PAST_24_HOURS"
)

# Print the response
print(response)

### Search Twitter

To search Twitter for specific topics, use the BasicTwitterSearchTool:

PYTHON
from langchain_desearch.tools import BasicTwitterSearchTool

# Initialize the Twitter search tool
tool = BasicTwitterSearchTool()

# Execute a search query
response = tool._run(query="AI governance", sort="Top", count=5)

# Display the results
print(response)

## Building a RAG Chain

Creating a RAG chain involves integrating Desearch with LangChain's prompt and LLM capabilities:

PYTHON
from langchain_desearch.tools import DesearchTool
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_deepseek import ChatDeepSeek
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Initialize the Desearch tool
tool = DesearchTool()

# Define a function to fetch context
def fetch_context(query):
    return tool._run(prompt=query, tool="desearch_web", model="NOVA")

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a research assistant."),
    ("human", "Answer this using the provided context:\n\n<context>{context}</context>")
])

# Set up the LLM
llm = ChatDeepSeek(model="deepseek-chat", temperature=0.7)
parser = StrOutputParser()

# Build the RAG chain
chain = RunnableParallel({
    "query": RunnablePassthrough(),
    "context": lambda q: fetch_context(q["query"]),
}) | prompt | llm | parser

# Invoke the chain with a query
result = chain.invoke("What is the latest update on the EU AI Act?")
print(result)

## Using Desearch in a LangChain Agent

Integrate Desearch into a LangChain agent to automate complex workflows:

PYTHON
from langchain_desearch.agent import create_search_agent
from langchain_deepseek import ChatDeepSeek

# Initialize the LLM
llm = ChatDeepSeek(model="deepseek-chat", temperature=0.7)

# Create a search agent
agent = create_search_agent(llm=llm)

# Invoke the agent with an input message
response = agent.invoke({"input_message": "Summarize current AI regulation trends"})
print(response["output"])

## Testing

### Unit Tests (Mocked)

To ensure your integration works as expected, run unit tests:

BASH
pytest tests/test_tools.py

### Live API Tests

For testing with live data, ensure your API key is set and run:

BASH
pytest tests/test_tools_real.py

⚠️ Note: The DESEARCH_API_KEY must be set in your .env file to execute live tests.

🤝 Contributing

We welcome contributions! To contribute:

Fork the Repository: Create your own fork of the project.
Create a Branch: Develop your feature or fix in a new branch.
BASH
git checkout -b feature/my-feature
Make Changes: Implement your changes and commit them.
Submit a Pull Request: Open a pull request to merge your changes.
📜 License

This project is licensed under the MIT License, allowing for open collaboration and sharing.

📬 Contact

For questions or feedback, feel free to open an issue on the repository or reach out via Desearch contact page.

🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
