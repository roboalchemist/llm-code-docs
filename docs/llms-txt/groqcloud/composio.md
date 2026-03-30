# Source: https://console.groq.com/docs/composio

---
description: Learn how to use Composio with Groq to build fast, tool-using AI agents that can interact with 90+ external applications and automate workflows.
title: Composio + Groq: Tool Management &amp; Agent Automation - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [Composio](#composio)

[Composio](https://composio.ai/) is a platform for managing and integrating tools with LLMs and AI agents. You can build fast, Groq-based assistants to seamlessly interact with external applications through features including:

* **Tool Integration:** Connect AI agents to APIs, RPCs, shells, file systems, and web browsers with 90+ readily available tools
* **Authentication Management:** Secure, user-level auth across multiple accounts and tools
* **Optimized Execution:** Improve security and cost-efficiency with tailored execution environments
* **Comprehensive Logging:** Track and analyze every function call made by your LLMs

### [Python Quick Start (5 minutes to hello world)](#python-quick-start-5-minutes-to-hello-world)

#### [1\. Install the required packages:](#1-install-the-required-packages)

curl

```
pip install composio-langchain langchain-groq
```

#### [2\. Configure your Groq and Composio API keys:](#2-configure-your-groq-and-composio-api-keys)

curl

```
export GROQ_API_KEY="your-groq-api-key"
export COMPOSIO_API_KEY="your-composio-api-key"
```

#### [3\. Connect your first Composio tool:](#3-connect-your-first-composio-tool)

curl

```
# Connect GitHub (you'll be guided through OAuth flow to get things going)
composio add github

# View all available tools
composio apps
```

#### [4\. Create your first Composio-enabled Groq agent:](#4-create-your-first-composioenabled-groq-agent)

Running this code will create an agent that can interact with GitHub through natural language in mere seconds! Your agent will be able to:

* Perform GitHub operations like starring repos and creating issues for you
* Securely manage your OAuth flows and API keys
* Process natural language to convert your requests into specific tool actions
* Provide feedback to let you know about the success or failure of operations

Python

```
from langchain.agents import AgentType, initialize_agent
from langchain_groq import ChatGroq
from composio_langchain import ComposioToolSet, App

# Initialize LLM
llm = ChatGroq(model="llama-3.3-70b-versatile")

# Get Composio tools (GitHub in this example)
composio_toolset = ComposioToolSet()
tools = composio_toolset.get_tools(apps=[App.GITHUB])

# Create agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Define task and run
task = "Star groq/groq-api-cookbook repo on GitHub"
agent.run(task)
```

**Challenge**: Create a Groq-powered agent that can summarize your GitHub issues and post updates to Slack through Composio tools!

For more detailed documentation and resources on building AI agents with Groq and Composio, see:

* [Composio documentation](https://docs.composio.dev/framework/groq)
* [Guide to Building Agents with Composio and Llama 3.1 models powered by Groq](https://composio.dev/blog/tool-calling-in-llama-3-a-guide-to-build-agents/)
* [Groq API Cookbook tutorial](https://github.com/groq/groq-api-cookbook/tree/main/tutorials/composio-newsletter-summarizer-agent)