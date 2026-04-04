# Agentic Copilots

Agentic copilots provide you with advanced control and orchestration over your agents.

Before we dive into what agentic copilots are, help us help you by telling us your level of experience with LangGraph. We'll explain things in a way that best suits your experience level.

![](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/copilotkit-logo.svg)

I'm new to LangGraph

Help me understand what agentic copilots are, where LangGraph fits in, and how to get started.

I'm already using LangGraph

Help me understand what agentic copilots are, what CopilotKit does to integrate with LangGraph, and how to get started.

![CoAgents Shared State](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/coagents/SharedStateCoAgents.gif)

### [What are Agents?](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots\#what-are-agents)

AI agents are intelligent systems that interact with their environment to achieve specific goals. Think of them as 'virtual colleagues' that can handle tasks ranging from
simple queries like "find the cheapest flight to Paris" to complex challenges like "design a new product layout."

As these AI-driven experiences (or 'Agentic Experiences') become more sophisticated, developers need finer control over how agents make decisions. This is where specialized
frameworks like LangGraph become essential.

### [What is LangGraph?](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots\#what-is-langgraph)

LangGraph is a framework that gives you precise control over AI agents. It uses a graph-based approach where each step in an agent's decision-making process is represented
by a `node`. These nodes are connected by `edges` to form a directed acyclic graph (DAG), creating a clear map of possible actions and decisions.

The key advantage of LangGraph is its tight control over the agent's decision making process. Since all of this is defined in code by you, the behavior is much more
deterministic and predictable.

### [What are Agentic Copilots?](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots\#what-are-agentic-copilots)

Agentic copilots are how CopilotKit brings LangGraph agents into your application. If you're familiar with CopilotKit, you know that copilots are AI assistants that
understand your app's context and can take actions within it. While CopilotKit's standard copilots use a simplified [ReAct pattern](https://www.perplexity.ai/search/what-s-a-react-agent-5hu7ZOaKSAuY7YdFjQLCNQ)
for quick implementation, Agentic copilots give you LangGraph's full orchestration capabilities when you need more control over your agent's behavior.

### [What are CoAgents?](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots\#what-are-coagents)

CoAgents are what we call CopilotKit's approach to building agentic experiences! They're interchangeable with agentic copilots being a more descriptive term for the overall concept.

### [When should I use CopilotKit's CoAgents?](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots\#when-should-i-use-copilotkits-coagents)

You should use CoAgents when you require tight control over the Agentic runloop, as facilitated by an Agentic Orchestration framework like [LangGraph](https://langchain-ai.github.io/langgraph/).
With CoAgents, you can carry all of your existing CopilotKit-enabled Copilot capabilities into a customized agentic runloop.

We suggest beginning with a basic Copilot and gradually transitioning specific components to CoAgents.

The need for CoAgents spans a broad spectrum across different applications. At one end, their advanced capabilities might not be required at all, or only for a minimal 10% of the application's
functionality. Progressing further, there are scenarios where they become increasingly vital, managing 60-70% of operations. Ultimately, in some cases, CoAgents are indispensable, orchestrating
up to 100% of the Copilot's tasks (see [agent-lock mode](https://docs.copilotkit.ai/coagents/multi-agent-flows) for the 100% case).

### [Examples](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots\#examples)

An excellent example of the type of experiences you can accomplish with CoAgents applications can be found in our [Research Canvas](https://docs.copilotkit.ai/coagents/videos/research-canvas).

More specifically, it demonstrates how CoAgents allow for AI driven experiences with:

- Precise state management across agent interactions
- Sophisticated multi-step reasoning capabilities
- Seamless orchestration of multiple AI tools
- Interactive human-AI collaboration features
- Real-time state updates and progress streaming

## [Next Steps](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots\#next-steps)

Want to get started? You have some options!

[**Build your first CoAgent** \\
Follow a step-by-step tutorial to build a travel app supercharged with CoAgents.](https://docs.copilotkit.ai/coagents/quickstart/langgraph) [**Learn more CoAgent concepts** \\
Learn more about the concepts used to talk about CoAgents and how to use them.](https://docs.copilotkit.ai/coagents/concepts/terminology) [**Read the reference documentation** \\
Just here for some reference? Checkout the reference documentation for more details.](https://docs.copilotkit.ai/reference) [**See examples of CoAgents in action** \\
Checkout our video examples of CoAgents in action.](https://docs.copilotkit.ai/coagents/videos/research-canvas)

[Previous\\
\\
Terminology](https://docs.copilotkit.ai/coagents/concepts/terminology) [Next\\
\\
LangGraph](https://docs.copilotkit.ai/coagents/concepts/langgraph)

### On this page

[What are Agents?](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots#what-are-agents) [What is LangGraph?](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots#what-is-langgraph) [What are Agentic Copilots?](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots#what-are-agentic-copilots) [What are CoAgents?](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots#what-are-coagents) [When should I use CopilotKit's CoAgents?](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots#when-should-i-use-copilotkits-coagents) [Examples](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots#examples) [Next Steps](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots#next-steps) [What are CoAgents?](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots#what-are-coagents-1) [Next Steps](https://docs.copilotkit.ai/coagents/concepts/agentic-copilots#next-steps-1)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/concepts/agentic-copilots.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Connect Your Data
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this page