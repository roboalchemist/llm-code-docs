---
---
title: Instrument AI Agents
description: "Learn how to manually instrument AI agents in browser applications."
---

With Sentry AI Agent Monitoring, you can monitor and debug your AI systems with full-stack context. You'll be able to track key insights like token usage, latency, tool usage, and error rates. AI Agent Monitoring data will be fully connected to your other Sentry data like logs, errors, and traces.

As a prerequisite to setting up AI Agent Monitoring in browser applications, you'll need to first set up tracing.

**Browser applications require manual instrumentation.** Unlike Node.js applications, the JavaScript SDK does not provide automatic instrumentation for AI libraries in the browser. You must use manual instrumentation techniques to capture AI agent spans.

## Manual Instrumentation Options

There are two ways to instrument AI agents in browser applications:

1. **Using Integration Helpers** - For supported AI libraries (recommended)
2. **Custom Span Creation** - For unsupported libraries or custom AI implementations

## Using Integration Helpers

For some AI libraries, Sentry provides manual instrumentation helpers that simplify span creation. These helpers handle the complexity of creating properly structured spans with the correct attributes for AI Agent Monitoring.

### Supported AI Libraries

The following AI libraries have helper functions available for browser applications:

- **OpenAI**
- **Anthropic**
- **Google Gen AI SDK**
- **LangChain**
- **LangGraph**

Each integration page includes browser-specific examples showing how to use the helper functions with options like `recordInputs` and `recordOutputs` to control what data is captured.

## Manual Span Creation

If you're using an AI library that Sentry doesn't provide helpers for, or if you have a custom AI implementation, you can manually create spans to capture AI agent operations. For your AI agents data to show up in the Sentry [AI Agents Insights](https://sentry.io/orgredirect/organizations/:orgslug/insights/ai/agents/), spans must have well-defined names and data attributes following OpenTelemetry Semantic Conventions for Generative AI.

## Spans

### Invoke Agent Span

  

#### Example of an Invoke Agent Span:

```javascript
// Example agent implementation for demonstration
const myAgent = {
  name: "Weather Agent",
  modelProvider: "openai",
  model: "gpt-4o-mini",
  async run() {
    // Agent implementation
    return {
      output: "The weather in Paris is sunny",
      usage: {
        inputTokens: 15,
        outputTokens: 8,
      },
    };
  },
};

Sentry.startSpan(
  {
    op: "gen_ai.invoke_agent",
    name: `invoke_agent ${myAgent.name}`,
    attributes: {
      "gen_ai.operation.name": "invoke_agent",
      "gen_ai.request.model": myAgent.model,
      "gen_ai.agent.name": myAgent.name,
    },
  },
  async (span) => {
    // run the agent
    const result = await myAgent.run();

    // set agent response
    // we assume result.output is a string
    // type of `gen_ai.response.text` needs to be a string
    span.setAttribute("gen_ai.response.text", JSON.stringify([result.output]));

    // set token usage
    // we assume the result includes the tokens used
    span.setAttribute("gen_ai.usage.input_tokens", result.usage.inputTokens);
    span.setAttribute("gen_ai.usage.output_tokens", result.usage.outputTokens);

    return result;
  }
);
```

### AI Client Span

  

#### Example AI Client Span

```javascript
// Example implementation for demonstration
const myAi = {
  modelProvider: "openai",
  model: "gpt-4o-mini",
  modelConfig: {
    temperature: 0.1,
    presencePenalty: 0.5,
  },
  async createMessage(messages, maxTokens) {
    // AI implementation
    return {
      output:
        "Here's a joke: Why don't scientists trust atoms? Because they make up everything!",
      usage: {
        inputTokens: 12,
        outputTokens: 24,
      },
    };
  },
};

Sentry.startSpan(
  {
    op: "gen_ai.chat",
    name: `chat ${myAi.model}`,
    attributes: {
      "gen_ai.operation.name": "chat",
      "gen_ai.request.model": myAi.model,
    },
  },
  async (span) => {
    // set up messages for LLM
    const maxTokens = 1024;
    const prompt = "Tell me a joke";
    const messages = [{ role: "user", content: prompt }];

    // set chat request data
    span.setAttribute("gen_ai.request.messages", JSON.stringify(messages));
    span.setAttribute("gen_ai.request.max_tokens", maxTokens);
    span.setAttribute(
      "gen_ai.request.temperature",
      myAi.modelConfig.temperature
    );
    span.setAttribute(
      "gen_ai.request.presence_penalty",
      myAi.modelConfig.presencePenalty
    );

    // ask the LLM
    const result = await myAi.createMessage(messages, maxTokens);

    // set response
    // we assume result.output is a string
    // type of `gen_ai.response.text` needs to be a string
    span.setAttribute("gen_ai.response.text", JSON.stringify([result.output]));

    // set token usage
    // we assume the result includes the tokens used
    span.setAttribute("gen_ai.usage.input_tokens", result.usage.inputTokens);
    span.setAttribute("gen_ai.usage.output_tokens", result.usage.outputTokens);

    return result;
  }
);
```

### Execute Tool Span

  

#### Example Execute Tool Span

```javascript
// Example implementation for demonstration
const myAi = {
  modelProvider: "openai",
  model: "gpt-4o-mini",
  async createMessage(messages, maxTokens) {
    // AI implementation that returns tool calls
    return {
      toolCalls: [
        {
          name: "random_number",
          description: "Generate a random number",
          arguments: { max: 10 },
        },
      ],
    };
  },
};

const prompt = "Generate a random number between 0 and 10";
const messages = [{ role: "user", content: prompt }];

// First, make the AI call
const result = await Sentry.startSpan(
  { op: "gen_ai.chat", name: `chat ${myAi.model}` },
  () => myAi.createMessage(messages, 1024)
);

// Check if we should call a tool
if (result.toolCalls && result.toolCalls.length > 0) {
  const tool = result.toolCalls[0];

  await Sentry.startSpan(
    {
      op: "gen_ai.execute_tool",
      name: `execute_tool ${tool.name}`,
      attributes: {
        "gen_ai.request.model": myAi.model,
        "gen_ai.tool.type": "function",
        "gen_ai.tool.name": tool.name,
        "gen_ai.tool.description": tool.description,
        "gen_ai.tool.input": JSON.stringify(tool.arguments),
      },
    },
    async (span) => {
      // run tool (example implementation)
      const toolResult = Math.floor(Math.random() * tool.arguments.max);

      // set tool result
      span.setAttribute("gen_ai.tool.output", String(toolResult));

      return toolResult;
    }
  );
}
```

### Handoff Span

  

#### Example of a Handoff Span

```javascript
// Example agent implementation for demonstration
const myAgent = {
  name: "Weather Agent",
  modelProvider: "openai",
  model: "gpt-4o-mini",
  async run() {
    // Agent implementation
    return {
      handoffTo: "Travel Agent",
      output:
        "I need to handoff to the travel agent for booking recommendations",
    };
  },
};

const otherAgent = {
  name: "Travel Agent",
  modelProvider: "openai",
  model: "gpt-4o-mini",
  async run() {
    // Other agent implementation
    return { output: "Here are some travel recommendations..." };
  },
};

// First agent execution
const result = await Sentry.startSpan(
  { op: "gen_ai.invoke_agent", name: `invoke_agent ${myAgent.name}` },
  () => myAgent.run()
);

// Check if we should handoff to another agent
if (result.handoffTo) {
  // Create handoff span
  await Sentry.startSpan(
    {
      op: "gen_ai.handoff",
      name: `handoff from ${myAgent.name} to ${otherAgent.name}`,
      attributes: {
        "gen_ai.request.model": myAgent.model,
      },
    },
    () => {
      // the handoff span just marks the handoff
      // no actual work is done here
    }
  );

  // Execute the other agent
  await Sentry.startSpan(
    { op: "gen_ai.invoke_agent", name: `invoke_agent ${otherAgent.name}` },
    () => otherAgent.run()
  );
}
```

  

