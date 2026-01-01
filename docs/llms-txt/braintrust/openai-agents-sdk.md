# Source: https://braintrust.dev/docs/integrations/sdk-integrations/openai-agents-sdk.md

# OpenAI Agents SDK

The [OpenAI Agents SDK](https://openai.com/index/introducing-the-openai-agents-sdk/) is OpenAI's official framework for building AI agents. Braintrust integrates with the OpenAI Agents SDK using trace processors to capture agent execution, tool calls, and LLM interactions.

## Setup

Install the Braintrust trace processor for OpenAI Agents:

<CodeGroup>
  ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # pnpm
  pnpm add braintrust @braintrust/openai-agents @openai/agents
  # npm
  npm install braintrust @braintrust/openai-agents @openai/agents
  ```

  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install braintrust[openai-agents]
  ```
</CodeGroup>

## Trace with OpenAI Agents SDK

Configure Braintrust's trace processor to automatically send agent traces to Braintrust:

<CodeGroup dropdown>
  ```python title="trace-agents.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import asyncio

  from agents import Agent, Runner, set_trace_processors
  from braintrust import init_logger
  from braintrust.wrappers.openai import BraintrustTracingProcessor

  async def main():
      agent = Agent(
          name="Assistant",
          instructions="You only respond in haikus.",
      )

      result = await Runner.run(agent, "Tell me about recursion in programming.")
      print(result.final_output)

  if __name__ == "__main__":
      set_trace_processors([BraintrustTracingProcessor(init_logger("openai-agent"))])
      asyncio.run(main())
  ```

  ```typescript title="trace-agents.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initLogger } from "braintrust";
  import { OpenAIAgentsTraceProcessor } from "@braintrust/openai-agents";
  import { Agent, run, addTraceProcessor } from "@openai/agents";

  // Initialize Braintrust logger
  const logger = initLogger({
    projectName: "openai-agent",
  });

  // Create the tracing processor
  const processor = new OpenAIAgentsTraceProcessor({ logger });

  // Add the processor to OpenAI Agents
  addTraceProcessor(processor);

  async function main() {
    const agent = new Agent({
      name: "Assistant",
      model: "gpt-4o-mini",
      instructions: "You only respond in haikus.",
    });

    const result = await run(agent, "Tell me about recursion in programming.");
    console.log(result.finalOutput);
  }

  main().catch(console.error);
  ```
</CodeGroup>

<Note>
  The trace processor constructor can accept a `braintrust.Span`, `braintrust.Experiment`, or `braintrust.Logger` as the root for logging. If not provided, it automatically selects the current span, experiment, or logger.
</Note>

<img src="https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-logs.png?fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=8ff62f2519983498a1ea5f1c5f070a5d" alt="OpenAI Agents SDK Logs" data-og-width="2594" width="2594" data-og-height="1850" height="1850" data-path="images/integrations/oai-agents-sdk-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-logs.png?w=280&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=5b309f9ecbeac58f8410d3d71d2c79ed 280w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-logs.png?w=560&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=3e85c4203f59353f17f57b4b88d7e32e 560w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-logs.png?w=840&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=cf786b5c6350fd7a81aff3a286cde45f 840w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-logs.png?w=1100&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=1abf92fc4fb7f201b7cc9ea6096af760 1100w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-logs.png?w=1650&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=07ad477f46a5a9d2d37a533ac05ebd8e 1650w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-logs.png?w=2500&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=d3108ff175dd55f1e205832190780dbe 2500w" />

## Evaluate with OpenAI Agents SDK

Use OpenAI Agents SDK as the `task` in a Braintrust `Eval` to build and evaluate agentic workflows:

<CodeGroup dropdown>
  ```python title="eval-agents.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from agents import Agent, Runner, set_trace_processors
  from autoevals import ClosedQA
  from braintrust import Eval
  from braintrust.wrappers.openai import BraintrustTracingProcessor

  set_trace_processors([BraintrustTracingProcessor()])

  async def task(input: str):
      agent = Agent(
          name="Assistant",
          instructions="You only respond in haikus.",
      )

      result = await Runner.run(agent, input)
      return result.final_output

  Eval(
      name="openai-agent",
      data=[
          {
              "input": "Tell me about recursion in programming.",
          }
      ],
      task=task,
      scores=[
          ClosedQA.partial(
              criteria="The response should respond to the prompt and be a haiku.",
          )
      ],
  )
  ```

  ```typescript title="eval-agents.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Agent, run, addTraceProcessor } from "@openai/agents";
  import { OpenAIAgentsTraceProcessor } from "@braintrust/openai-agents";
  import { Eval } from "braintrust";

  // Set up the trace processor
  const processor = new OpenAIAgentsTraceProcessor();
  addTraceProcessor(processor);

  async function task(input: string) {
    const agent = new Agent({
      name: "Assistant",
      model: "gpt-4o-mini",
      instructions: "You only respond in haikus.",
    });

    const result = await run(agent, input);
    return result.finalOutput;
  }

  Eval("openai-agent", {
    data: [
      {
        input: "Tell me about recursion in programming.",
      },
    ],
    task,
    scores: [
      // You can use autoevals or custom scoring functions
      {
        name: "haiku_check",
        scorer: async ({ output }) => {
          // Custom scoring logic for haiku validation
          const lines = output.split("\n").filter((line) => line.trim());
          return lines.length === 3 ? 1 : 0;
        },
      },
    ],
  });
  ```
</CodeGroup>

<img src="https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-eval.png?fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=2688026fccaa524e2f28bca6c89b584d" alt="OpenAI Agents SDK Eval" data-og-width="3148" width="3148" data-og-height="1736" height="1736" data-path="images/integrations/oai-agents-sdk-eval.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-eval.png?w=280&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=afef10cd35ed134c45a4820a9ba2f0e2 280w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-eval.png?w=560&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=731e0ba7295c10fe4fd40b3b01931a41 560w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-eval.png?w=840&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=0af1271a75f733ba23ac0a203b56cf06 840w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-eval.png?w=1100&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=fd77e711a39507d73e360b32903bfa66 1100w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-eval.png?w=1650&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=d61c690ad4870c6cb78e5efa5774b927 1650w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/oai-agents-sdk-eval.png?w=2500&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=a5957948ecce3555a67af847d0d438fb 2500w" />

## Resources

* [OpenAI Agents SDK documentation](https://openai.com/index/introducing-the-openai-agents-sdk/)
* [Braintrust Eval guide](/core/experiments)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt