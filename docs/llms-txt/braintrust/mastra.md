# Source: https://braintrust.dev/docs/integrations/agent-frameworks/mastra.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Mastra

[Mastra](https://mastra.ai/) is a TypeScript framework for building AI agents. Braintrust integrates with Mastra's observability system to automatically trace agent executions, LLM calls, and tool usage.

## Setup

Install Mastra with the Braintrust exporter:

<CodeGroup>
  ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # pnpm
  pnpm add @mastra/core @mastra/braintrust @mastra/observability braintrust
  # npm
  npm install @mastra/core @mastra/braintrust @mastra/observability braintrust
  ```
</CodeGroup>

## Trace with Mastra

Configure the `BraintrustExporter` in Mastra's observability settings:

```typescript title="trace-mastra.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Agent } from "@mastra/core/agent";
import { Mastra } from "@mastra/core/mastra";
import { Observability } from "@mastra/observability";
import { BraintrustExporter } from "@mastra/braintrust";
import { initLogger } from "braintrust";

const logger = initLogger({ projectName: "mastra-demo" });

const exporter = new BraintrustExporter({
  braintrustLogger: logger,
});

const mastra = new Mastra({
  agents: {
    assistant: new Agent({
      name: "Assistant",
      instructions: "You only respond in haikus.",
      model: "openai/gpt-4o-mini",
    }),
  },
  observability: new Observability({
    configs: {
      braintrust: {
        serviceName: "demo",
        exporters: [exporter],
      },
    },
  }),
});

async function main() {
  const agent = mastra.getAgent("assistant");
  const response = await agent.generate("Tell me about recursion in programming.");
  console.log(response.text);
}

main();
```

<Note>
  The `BraintrustExporter` constructor can accept a `braintrust.Span`, `braintrust.Experiment`, or `braintrust.Logger` as the `braintrustLogger` option. This enables automatic nesting of Mastra traces within Braintrust contexts like evals or traced functions.
</Note>

## Evaluate with Mastra

Use Mastra agents as the `task` in a Braintrust `Eval` to build and evaluate agentic workflows:

```typescript title="eval-mastra.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { Agent } from "@mastra/core/agent";
import { Mastra } from "@mastra/core/mastra";
import { Observability } from "@mastra/observability";
import { BraintrustExporter } from "@mastra/braintrust";
import { Eval, initLogger } from "braintrust";

const logger = initLogger({ projectName: "mastra-demo" });

const exporter = new BraintrustExporter({
  braintrustLogger: logger,
});

const mastra = new Mastra({
  agents: {
    assistant: new Agent({
      name: "Assistant",
      instructions: "You only respond in haikus.",
      model: "openai/gpt-4o-mini",
    }),
  },
  observability: new Observability({
    configs: {
      braintrust: {
        serviceName: "demo",
        exporters: [exporter],
      },
    },
  }),
});

Eval('mastra-demo', {
  data: () => [
    { input: 'What is the capital of France?', expected: 'Paris' },
    { input: 'What is 2+2?', expected: '4' },
  ],
  task: async (input: string) => {
    const agent = mastra.getAgent('assistant');
    return (await agent.generate(input)).text;
  },
  scores: [
    (args: { output: string; expected: string }) => ({
      name: 'contains_answer',
      score: String(args.output).toLowerCase().includes(String(args.expected).toLowerCase()) ? 1 : 0,
    }),
  ],
});
```

## Resources

* [Mastra documentation](https://mastra.ai/)
* [Mastra observability guide](https://mastra.ai/en/docs/observability/ai-tracing)
* [Braintrust Eval guide](/evaluate/run-evaluations)
