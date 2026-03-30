# Agentic Generative UI

Render the state of your agent with custom UI components.

This video demonstrates the [implementation](https://docs.copilotkit.ai/coagents/generative-ui/agentic#implementation) section applied to our [coagents starter project](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-starter).

## [What is this?](https://docs.copilotkit.ai/coagents/generative-ui/agentic\#what-is-this)

All LangGraph agents are stateful. This means that as your agent progresses through nodes, a state object is passed between them perserving
the overall state of a session. CopilotKit allows you to render this state in your application with custom UI components, which we call **Agentic Generative UI**.

## [When should I use this?](https://docs.copilotkit.ai/coagents/generative-ui/agentic\#when-should-i-use-this)

Rendering the state of your agent in the UI is useful when you want to provide the user with feedback about the overall state of a session. A great example of this
is a situation where a user and an agent are working together to solve a problem. The agent can store a draft in its state which is then rendered in the UI.

## [Implementation](https://docs.copilotkit.ai/coagents/generative-ui/agentic\#implementation)

### [Run and Connect your LangGraph to CopilotKit](https://docs.copilotkit.ai/coagents/generative-ui/agentic\#run-and-connect-your-langgraph-to-copilotkit)

First, you'll need to make sure you have a running LangGraph. If you haven't already done this, you can follow the [getting started guide](https://docs.copilotkit.ai/coagents/quickstart/langgraph)

This guide uses the [CoAgents starter repo](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-starter) as its starting point.

### [Define your agent state](https://docs.copilotkit.ai/coagents/generative-ui/agentic\#define-your-agent-state)

If you're not familiar with LangGraph, your graphs are stateful. As you progress through nodes, a state object is passed between them. CopilotKit
allows you to easily render this state in your application.

For the sake of this guide, let's say our state looks like this in our agent.

PythonTypeScript

agent-py/sample\_agent/agent.py

```