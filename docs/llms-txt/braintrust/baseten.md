# Source: https://braintrust.dev/docs/integrations/ai-providers/baseten.md

# Baseten

> Baseten model provider configuration and integration guide

Baseten provides scalable infrastructure for deploying and serving machine learning models, including language models and custom AI applications. Braintrust integrates seamlessly with Baseten through direct API access, wrapper functions for automatic tracing, and proxy support.

## Setup

To use Baseten models, configure your Baseten API key in Braintrust.

1. Get a Baseten API key from [Baseten Console](https://app.baseten.co/settings/api-keys)
2. Add the Baseten API key to your organization's [AI providers](https://www.braintrust.dev/app/settings/secrets)
3. Set the Baseten API key and your Braintrust API key as environment variables

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BASETEN_API_KEY=<your-baseten-api-key>
BRAINTRUST_API_KEY=<your-braintrust-api-key>

# If you are self-hosting Braintrust, set the URL of your hosted dataplane
# BRAINTRUST_API_URL=<your-braintrust-api-url>
```

<Note>
  API keys are encrypted using 256-bit AES-GCM encryption and are not stored or logged by Braintrust.
</Note>

## Use Baseten with Braintrust AI proxy

The Braintrust AI Proxy allows you to access Baseten models through a unified OpenAI-compatible interface.

Install the `braintrust` and `openai` packages.

<CodeGroup>
  ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # pnpm
  pnpm add braintrust openai
  # npm
  npm install braintrust openai
  ```

  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install braintrust openai
  ```
</CodeGroup>

Then, initialize the client and make a request to a Baseten model via the Braintrust AI Proxy.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const response = await client.chat.completions.create({
    model: "gpt-oss-120b",
    messages: [{ role: "user", content: "Hello, world!" }],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      api_key=os.environ["BRAINTRUST_API_KEY"],
  )

  response = client.chat.completions.create(
      model="gpt-oss-120b",
      messages=[{"role": "user", "content": "Hello, world!"}],
  )
  ```
</CodeGroup>

## Trace logs with Baseten

[Trace](/guides/traces) your Baseten LLM calls for observability and monitoring.

When using the Braintrust AI Proxy, API calls are automatically logged to the specified project.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";
  import { initLogger } from "braintrust";

  initLogger({
    projectName: "My Project",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  // All API calls are automatically logged
  const result = await client.chat.completions.create({
    model: "gpt-oss-120b",
    messages: [{ role: "user", content: "What is machine learning?" }],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from braintrust import init_logger
  from openai import OpenAI

  init_logger(project="My Project")

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      api_key=os.environ["BRAINTRUST_API_KEY"],
  )

  # All API calls are automatically logged
  result = client.chat.completions.create(
      model="gpt-oss-120b",
      messages=[{"role": "user", "content": "What is machine learning?"}],
  )
  ```
</CodeGroup>

<Tip>
  The Braintrust AI Proxy is not required. For more control, learn how to [customize traces](/guides/traces/customize).
</Tip>

## Evaluate with Baseten

Evaluations distill the non-deterministic outputs of Baseten models into an effective feedback loop that enables you to ship more reliable, higher quality products. Braintrust `Eval` is a simple function composed of a dataset of user inputs, a task, and a set of scorers. To learn more about evaluations, check out the [Experiments](/core/experiments) guide.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  Eval("Baseten Evaluation", {
    data: () => [
      { input: "What is 2+2?", expected: "4" },
      { input: "What is the capital of France?", expected: "Paris" },
    ],
    task: async (input) => {
      const response = await client.chat.completions.create({
        model: "openai/gpt-oss-120b",
        messages: [{ role: "user", content: input }],
      });
      return response.choices[0].message.content;
    },
    scores: [
      {
        name: "accuracy",
        scorer: (args) => (args.output === args.expected ? 1 : 0),
      },
    ],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from braintrust import Eval
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      api_key=os.environ["BRAINTRUST_API_KEY"],
  )


  def task(input):
      response = client.chat.completions.create(
          model="openai/gpt-oss-120b",
          messages=[{"role": "user", "content": input}],
      )
      return response.choices[0].message.content


  def accuracy_scorer(output, expected, **kwargs):
      return 1 if output == expected else 0


  Eval(
      "Baseten Evaluation",
      data=[
          {"input": "What is 2+2?", "expected": "4"},
          {"input": "What is the capital of France?", "expected": "Paris"},
      ],
      task=task,
      scores=[accuracy_scorer],
  )
  ```
</CodeGroup>

<Tip>
  To learn more about tool use, multimodal support, attachments, and masking sensitive data with Baseten, visit the [customize traces](/guides/traces/customize) guide.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt