---
---
title: Instrument AI Agents
description: "Learn how to manually instrument your code to use Sentry's Agents module."
---

With Sentry AI Agent Monitoring, you can monitor and debug your AI systems with full-stack context. You'll be able to track key insights like token usage, latency, tool usage, and error rates. AI Agent Monitoring data will be fully connected to your other Sentry data like logs, errors, and traces.

As a prerequisite to setting up AI Agent Monitoring with Python, you'll need to first set up tracing. Once this is done, the Python SDK will automatically instrument AI agents created with supported libraries. If that doesn't fit your use case, you can use custom instrumentation described below.

## Automatic Instrumentation

The Python SDK supports automatic instrumentation for some AI libraries. We recommend adding their integrations to your Sentry configuration to automatically capture spans for AI agents.

- Anthropic
- Google Gen AI
- OpenAI
- OpenAI Agents SDK
- LangChain
- LangGraph
- LiteLLM
- Pydantic AI

## Manual Instrumentation

For your AI agents data to show up in the Sentry [AI Agents Insights](https://sentry.io/orgredirect/organizations/:orgslug/insights/ai/agents/), two spans must be created and have well-defined names and data attributes. See below.

The [@sentry_sdk.trace()](/platforms/python/tracing/instrumentation/custom-instrumentation/#span-templates) decorator can also be used to create these spans.

## Spans

### AI Request span

This span represents a request to a LLM model or service that generates a response based on the input prompt.

  

#### Example AI Request span

```python
import sentry_sdk

messages = [{"role": "user", "content": "Tell me a joke"}]

with sentry_sdk.start_span(op="gen_ai.request", name="chat o3-mini") as span:
    span.set_data("gen_ai.request.model", "o3-mini")
    span.set_data("gen_ai.request.messages", json.dumps(messages))
    span.set_data("gen_ai.operation.name", "invoke_agent")

    # Call your LLM here
    result = client.chat.completions.create(model="o3-mini", messages=messages)

    span.set_data("gen_ai.response.text", json.dumps([result.choices[0].message.content]))
    # Set token usage
    span.set_data("gen_ai.usage.input_tokens", result.usage.prompt_tokens)
    span.set_data("gen_ai.usage.output_tokens", result.usage.completion_tokens)
```

### Invoke Agent Span

This span represents the execution of an AI agent, capturing the full lifecycle from receiving a task to producing a final response.

  

#### Example of an Invoke Agent Span:

```python
import sentry_sdk

with sentry_sdk.start_span(op="gen_ai.invoke_agent", name="invoke_agent Weather Agent") as span:
    span.set_data("gen_ai.request.model", "o3-mini")
    span.set_data("gen_ai.agent.name", "Weather Agent")

    # Run the agent
    final_output = my_agent.run()

    span.set_data("gen_ai.response.text", str(final_output))
    # Set token usage
    span.set_data("gen_ai.usage.input_tokens", result.usage.input_tokens)
    span.set_data("gen_ai.usage.output_tokens", result.usage.output_tokens)
```

### Execute Tool Span

This span represents the execution of a tool or function that was requested by an AI model, including the input arguments and resulting output.

  

#### Example Execute Tool Span

```python
import sentry_sdk

with sentry_sdk.start_span(op="gen_ai.execute_tool", name="execute_tool get_weather") as span:
    span.set_data("gen_ai.tool.name", "get_weather")
    span.set_data("gen_ai.tool.input", json.dumps({"location": "Paris"}))

    # Call the tool
    result = get_weather(location="Paris")

    span.set_data("gen_ai.tool.output", json.dumps(result))
```

### Handoff Span

This span marks the transition of control from one agent to another, typically when the current agent determines another agent is better suited to handle the task.

  

#### Example of a Handoff Span

```python
import sentry_sdk

with sentry_sdk.start_span(op="gen_ai.handoff", name="handoff from Weather Agent to Travel Agent"):
    pass  # Handoff span just marks the transition

with sentry_sdk.start_span(op="gen_ai.invoke_agent", name="invoke_agent Travel Agent"):
    # Run the target agent here
    pass
```

## Common Span Attributes

