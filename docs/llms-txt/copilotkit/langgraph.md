# LangGraph

An agentic framework for building LLM applications that can be used with CopilotKit.

![CoAgents High Level Overview](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/coagents/coagents-highlevel-overview.png)

LangGraph is an agentic framework for building LLM applications that can be used with CopilotKit. It is built on top of LangChain's
[LangGraph](https://langchain-ai.github.io/langgraph/) library and extends it with additional functionality for building agentic
applications.

## [CoAgents and LangGraph](https://docs.copilotkit.ai/coagents/concepts/langgraph\#coagents-and-langgraph)

How do CoAgents extend LangGraph? Let's read the first sentence of their [project page](https://langchain-ai.github.io/langgraph/) to understand.

> LangGraph is a library for building stateful, multi-actor applications with LLMs, used to create agent and multi-agent workflows.

There are some key terms here so let's break them down and understand how they relate to and are implemented by CoAgents.

- **Stateful**: CoAgents have bi-directional state sharing with the agent and UI. This allows for the agent to remember
information from previous messages and the UI to update the agent with new information. Read more about how state sharing works
[here](https://docs.copilotkit.ai/coagents/shared-state).
- **Multi-actor**: CoAgents allow for multiple agents to interact with each other. CopilotKit acts as the "ground-truth"
when transitioning between agents. Read more about how multi-actor workflows work [here](https://docs.copilotkit.ai/coagents/multi-agent-flows)
and how messages are managed [here](https://docs.copilotkit.ai/coagents/concepts/message-management).
- **LLMs**: CoAgents use large language models to generate responses. This is useful for building applications that need to
generate natural language responses.

Some additional functionality not mentioned here is:

- **Human in the loop**: CoAgents enabled human review and approval of generated responses. Read more about how this works
[here](https://docs.copilotkit.ai/coagents/human-in-the-loop).
- **Tool calling**: Tool calling is a fundamental building block for agentic workflows. They allow for greater control over what
the agent can do and can be used to interact with external systems. CoAgents allow you to easily render in-progress
tool calls in the UI so your users know what's happening. Read more about streaming tool calls [here](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates).

## [Building with Python or JavaScript](https://docs.copilotkit.ai/coagents/concepts/langgraph\#building-with-python-or-javascript)

You can natively build LangGraph applications using Python or JavaScript. Throughout our documentation of integrating with LangGraph
you will see options for building in Python or JavaScript.

For a quick refresher on each, check out the [Python](https://langchain-ai.github.io/langgraph) and
[JavaScript](https://langchain-ai.github.io/langgraphjs/) guides from LangGraph:

## [LangGraph Platform](https://docs.copilotkit.ai/coagents/concepts/langgraph\#langgraph-platform)

LangGraph Platform is a platform for building and deploying LangGraph applications. It is built on top of the LangGraph library and
allows you to build, manage, and deploy graphs that CopilotKit can interface with. For more information checkout the official
[LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform) documentation.

If you want to take the next step to deploy your LangGraph application as an CoAgent, check out our [quickstart guide](https://docs.copilotkit.ai/coagents/quickstart/langgraph).

[Previous\\
\\
Agentic Copilots](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots) [Next\\
\\
Message flow](https://docs.copilotkit.ai/coagents/concepts/message-management)

### On this page

[CoAgents and LangGraph](https://docs.copilotkit.ai/coagents/concepts/langgraph#coagents-and-langgraph) [Building with Python or JavaScript](https://docs.copilotkit.ai/coagents/concepts/langgraph#building-with-python-or-javascript) [LangGraph Platform](https://docs.copilotkit.ai/coagents/concepts/langgraph#langgraph-platform)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/concepts/langgraph.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Backend Actions Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this page