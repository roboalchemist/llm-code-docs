# Source: https://console.groq.com/docs/agno

---
description: Learn how to use Agno with Groq to build lightning-fast, multi-modal AI agents with tool use, memory, and reasoning capabilities.
title: Agno + Groq: Build Fast, Multi-Modal Agents - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [Agno + Groq: Fast Agents](#agno--groq-fast-agents)

[Agno](https://github.com/agno-agi/agno) is a lightweight framework for building multi-modal Agents. It's easy to use, extremely fast and supports multi-modal inputs and outputs.

With Groq & Agno, you can build:

* **Agentic RAG**: Agents that can search different knowledge stores for RAG or dynamic few-shot learning.
* **Image Agents**: Agents that can understand images and make tool calls accordingly.
* **Reasoning Agents**: Agents that can reason using a reasoning model, then generate a result using another model.
* **Structured Outputs**: Agents that can generate pydantic objects adhering to a schema.

### [Python Quick Start (2 minutes to hello world)](#python-quick-start-2-minutes-to-hello-world)

Agents are autonomous programs that use language models to achieve tasks. They solve problems by running tools, accessing knowledge and memory to improve responses.

Let's build a simple web search agent, with a tool to search DuckDuckGo to get better results.

#### [1\. Create a file called web\_search\_agent.py and add the following code:](#1-create-a-file-called-websearchagentpy-and-add-the-following-code)

Python

```
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

# Initialize the agent with an LLM via Groq and DuckDuckGoTools
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    tools=[DuckDuckGoTools()],      # Add DuckDuckGo tool to search the web
    show_tool_calls=True,           # Shows tool calls in the response, set to False to hide
    markdown=True                   # Format responses in markdown
)

# Prompt the agent to fetch a breaking news story from New York
agent.print_response("Tell me about a breaking news story from New York.", stream=True)
```

#### [3\. Set up and activate your virtual environment:](#3-set-up-and-activate-your-virtual-environment)

shell

```
python3 -m venv .venv
source .venv/bin/activate
```

#### [4\. Install the Groq, Agno, and DuckDuckGo dependencies:](#4-install-the-groq-agno-and-duckduckgo-dependencies)

shell

```
pip install -U groq agno duckduckgo-search
```

#### [5\. Configure your Groq API Key:](#5-configure-your-groq-api-key)

curl

```
GROQ_API_KEY="your-api-key"
```

#### [6\. Run your Agno agent that now extends your LLM's context to include web search for up-to-date information and send results in seconds:](#6-run-your-agno-agent-that-now-extends-your-llms-context-to-include-web-search-for-uptodate-information-and-send-results-in-seconds)

shell

```
python web_search_agent.py
```

### [Multi-Agent Teams](#multiagent-teams)

Agents work best when they have a singular purpose, a narrow scope, and a small number of tools. When the number of tools grows beyond what the language model can handle or the tools belong to different categories, use a **team of agents** to spread the load.

The following code expands upon our quick start and creates a team of two agents to provide analysis on financial markets:

Python

```
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions="Use tables to display data",
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),  # You can use a different model for the team leader agent
    instructions=["Always include sources", "Use tables to display data"],
    # show_tool_calls=True,  # Uncomment to see tool calls in the response
    markdown=True,
)

# Give the team a task
agent_team.print_response("What's the market outlook and financial performance of AI semiconductor companies?", stream=True)
```

### [Additional Resources](#additional-resources)

For additional documentation and support, see the following:

* [Agno Documentation](https://docs.agno.com)
* [Groq via Agno Documentation](https://docs.agno.com/models/groq)
* [Groq via Agno examples](https://docs.agno.com/examples/models/groq/basic)
* [Various industry-ready examples](https://docs.agno.com/examples/introduction)