---
---
title: Instrument AI Agents
description: "Learn how to manually instrument your code to use Sentry's Agents module."
---

With Sentry AI Agent Monitoring, you can monitor and debug your AI systems with full-stack context. You'll be able to track key insights like token usage, latency, tool usage, and error rates. AI Agent Monitoring data will be fully connected to your other Sentry data like logs, errors, and traces.

As a prerequisite to setting up AI Agent Monitoring with JavaScript, you'll need to first set up tracing. Once this is done, the JavaScript SDK will automatically instrument AI agents created with supported libraries. If that doesn't fit your use case, you can use custom instrumentation described below.

## Automatic Instrumentation

The JavaScript SDK supports automatic instrumentation for some AI libraries. We recommend adding their integrations to your Sentry configuration to automatically capture spans for AI agents.

- Vercel AI SDK
- OpenAI
- Anthropic
- Google Gen AI SDK
- LangChain
- LangGraph
  
## Manual Instrumentation

If you're using a library that Sentry does not automatically instrument, you can manually instrument your code to capture spans. For your AI agents data to show up in the Sentry [AI Agents Insights](https://sentry.io/orgredirect/organizations/:orgslug/insights/ai/agents/), two spans must be created and have well-defined names and data attributes. See below.

## Spans

### AI Request Span

This span represents a request to a LLM model or service that generates a response based on the input prompt.

  

#### Example AI Request Span

```javascript
const messages = [{ role: "user", content: "Tell me a joke" }];

await Sentry.startSpan(
  {
    op: "gen_ai.request",
    name: "request o3-mini",
    attributes: {
      "gen_ai.request.model": "o3-mini",
      "gen_ai.request.messages": JSON.stringify(messages),
    },
  },
  async (span) => {
    // Call your LLM here
    const result = await client.chat.completions.create({
      model: "o3-mini",
      messages,
    });

    span.setAttribute(
      "gen_ai.response.text",
      JSON.stringify([result.choices[0].message.content])
    );
    // Set token usage
    span.setAttribute("gen_ai.usage.input_tokens", result.usage.prompt_tokens);
    span.setAttribute(
      "gen_ai.usage.output_tokens",
      result.usage.completion_tokens
    );
  }
);
```

### Invoke Agent Span

This span represents the execution of an AI agent, capturing the full lifecycle from receiving a task to producing a final response.

  

#### Example Invoke Agent Span

```javascript
await Sentry.startSpan(
  {
    op: "gen_ai.invoke_agent",
    name: "invoke_agent Weather Agent",
    attributes: {
      "gen_ai.request.model": "o3-mini",
      "gen_ai.agent.name": "Weather Agent",
    },
  },
  async (span) => {
    // Run the agent
    const result = await myAgent.run();

    span.setAttribute("gen_ai.response.text", JSON.stringify([result.output]));
    // Set token usage
    span.setAttribute("gen_ai.usage.input_tokens", result.usage.inputTokens);
    span.setAttribute("gen_ai.usage.output_tokens", result.usage.outputTokens);
  }
);
```

### Execute Tool Span

This span represents the execution of a tool or function that was requested by an AI model, including the input arguments and resulting output.

  

#### Example Execute Tool Span

```javascript
await Sentry.startSpan(
  {
    op: "gen_ai.execute_tool",
    name: "execute_tool get_weather",
    attributes: {
      "gen_ai.tool.name": "get_weather",
      "gen_ai.tool.input": JSON.stringify({ location: "Paris" }),
    },
  },
  async (span) => {
    // Call the tool
    const result = await getWeather({ location: "Paris" });

    span.setAttribute("gen_ai.tool.output", JSON.stringify(result));
  }
);
```

### Handoff Span

This span marks the transition of control from one agent to another, typically when the current agent determines another agent is better suited to handle the task.

  

#### Example Handoff Span

```javascript
await Sentry.startSpan(
  { op: "gen_ai.handoff", name: "handoff from Weather Agent to Travel Agent" },
  () => {} // Handoff span just marks the transition
);

await Sentry.startSpan(
  { op: "gen_ai.invoke_agent", name: "invoke_agent Travel Agent" },
  async () => {
    // Run the target agent here
  }
);
```

## Common Span Attributes

