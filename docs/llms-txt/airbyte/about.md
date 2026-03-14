# Source: https://docs.airbyte.com/ai-agents/about.md

# About Agent Engine

Copy Page

<!-- -->

Airbyte's Agent Engine is a data layer for AI agents. Use the Agent Engine as a cloud platform to manage connectors, credentials, and data replication for your agents. You can also use Airbyte's open source agent connectors as standalone Python packages, import them into your AI agents, and manage storage and credentials yourself.

## The problem with AI agents[​](#the-problem-with-ai-agents "Direct link to The problem with AI agents")

AI agents have almost unlimited potential to scale productivity, accelerate insights, and democratize information. However, most organizations struggle to realize this promise.

* Large language models can reason, but rely on stale public training data that limits their effectiveness. They lack real-time knowledge, are stateless, and can't act on and verify facts.

* Improving context with real business data is difficult. It forces teams to build infrastructure they don't want to own: storage layers, indexing services, pipelines, and permissions models. All of this is maintenance debt just to acquire missing context.

* Even if high-quality data is available, agents still perform poorly. They lack real-time access, can't search, can't write, miss key information, and need human intervention.

Organizations trying to build agents face a problem:

* They need massive upfront investment, or

* Their agents don't perform well, or

* Both

The result is that agentic features never scale. They remain expensive, fragile prototypes that can't support real-world operations.

## How Airbyte solves that problem[​](#how-airbyte-solves-that-problem "Direct link to How Airbyte solves that problem")

Airbyte's Agent Engine solves this problem with three components.

* Open-source, type-safe connectors designed for AI agents. These connectors allow agents to retrieve information they don't have, perform computations or transformations, interact with external systems, and trigger side-effects, like sending emails, updating databases, and starting workflows

* Storage and management of end-user credentials.

* Out of the box entity caching to power low-latency search operations.

It's helpful to think of the Agent Engine as a data layer that makes agentic tool use easy. Tools are external capabilities AI agents can invoke. They allow agents to perceive, decide, and act beyond their training data. They're one of the most critical bridges between agents that aren't effective and agents with broad capabilities.

## Who Agent Engine is for[​](#who-agent-engine-is-for "Direct link to Who Agent Engine is for")

* AI companies building agentic solutions, especially multi-tenant SaaS services.

* Engineering teams building agents for internal use cases.

* Hackers, explorers, innovators, and anyone who needs to empower an agent in minutes.

* People tired of expensive agents that aren't helpful.

## Tools and MCP servers[​](#tools-and-mcp-servers "Direct link to Tools and MCP servers")

It's helpful to think of agent connectors as equivalent to sets of tools. Tools are external capabilities AI agents can invoke. They allow agents to perceive, decide, and act beyond their training data. Tools are one of the most critical bridges between agents that aren't effective and agents with broad capabilities.
