# LangGraphAgent

LangGraphAgent lets you define your agent for use with CopilotKit.

## [LangGraphAgent](https://docs.copilotkit.ai/reference/sdk/python/LangGraphAgent\#langgraphagent)

LangGraphAgent lets you define your agent for use with CopilotKit.

To install, run:

```
pip install copilotkit
```

### [Examples](https://docs.copilotkit.ai/reference/sdk/python/LangGraphAgent\#examples)

Every agent must have the `name` and `graph` properties defined. An optional `description`
can also be provided. This is used when CopilotKit is dynamically routing requests to the
agent.

```
from copilotkit import LangGraphAgent

LangGraphAgent(
    name="email_agent",
    description="This agent sends emails",
    graph=graph,
)
```

If you have a custom LangGraph/LangChain config that you want to use with the agent, you can
pass it in as the `langgraph_config` parameter.

```
LangGraphAgent(
    ...
    langgraph_config=config,
)
```

### [Parameters](https://docs.copilotkit.ai/reference/sdk/python/LangGraphAgent\#parameters)

namestrrequired

The name of the agent.

graphCompiledGraphrequired

The LangGraph graph to use with the agent.

descriptionOptional\[str\]

The description of the agent.

langgraph\_configOptional\[RunnableConfig\]

The LangGraph/LangChain config to use with the agent.

copilotkit\_configOptional\[CopilotKitConfig\]

The CopilotKit config to use with the agent.

## [CopilotKitConfig](https://docs.copilotkit.ai/reference/sdk/python/LangGraphAgent\#copilotkitconfig)

CopilotKit config for LangGraphAgent

This is used for advanced cases where you want to customize how CopilotKit interacts with
LangGraph.

```