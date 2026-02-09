# Source: https://braintrust.dev/docs/reference/integrations/langchain-js/0.2.1/langchain-js.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LangChain JS Integration

> LangChain JS Integration v0.2.1

The `@braintrust/langchain-js` package provides seamless integration between Braintrust and LangChain.js.

## Installation

<CodeGroup>
  ```bash npm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  npm install @braintrust/langchain-js
  ```

  ```bash pnpm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pnpm add @braintrust/langchain-js
  ```
</CodeGroup>

## Quick start

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { BraintrustCallbackHandler } from "@braintrust/langchain-js";
import { ChatOpenAI } from "@langchain/openai";

// Create a callback handler
const handler = new BraintrustCallbackHandler();

// Use with any LangChain model
const llm = new ChatOpenAI({ callbacks: [handler] });
```

## API Reference

### Functions

#### setGlobalHandler

setGlobalHandler function.

### Classes

#### BraintrustCallbackHandler

BraintrustCallbackHandler class.

## Source Code

For the complete source code and additional examples, visit the [braintrust-sdk repository](https://github.com/braintrustdata/braintrust-sdk/tree/main/integrations/langchain-js).
