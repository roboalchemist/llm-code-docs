# Source: https://braintrust.dev/docs/reference/integrations/openai-agents-js/0.1.2/openai-agents-js.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Agents JS Integration

> OpenAI Agents JS Integration v0.1.2

The `@braintrust/openai-agents` package provides automatic tracing for OpenAI Agents SDK.

## Installation

<CodeGroup>
  ```bash npm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  npm install @braintrust/openai-agents
  ```

  ```bash pnpm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pnpm add @braintrust/openai-agents
  ```
</CodeGroup>

## Quick start

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { wrapOpenAIAgents } from "@braintrust/openai-agents";
import { Agent } from "@openai/agents";

// Wrap the agent for automatic tracing
const agent = wrapOpenAIAgents(new Agent({ name: "my-agent" }));
```

## API Reference

### Classes

#### OpenAIAgentsTraceProcessor

`OpenAIAgentsTraceProcessor` is a tracing processor that logs traces from the OpenAI Agents SDK to Braintrust. Args: options: Configuration options including: - logger: A `Span`, `Experiment`, or `Logger` to use for logging. If `undefined`, the current span, experiment, or logger will be selected exactly as in `startSpan`. - maxTraces: Maximum number of concurrent traces to keep in memory (default: 1000). When exceeded, oldest traces are evicted using LRU policy.

## Source Code

For the complete source code and additional examples, visit the [braintrust-sdk repository](https://github.com/braintrustdata/braintrust-sdk/tree/main/integrations/openai-agents-js).
