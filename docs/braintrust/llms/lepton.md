# Source: https://braintrust.dev/docs/integrations/ai-providers/lepton.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Lepton

> Lepton AI model provider configuration and integration guide

Lepton AI provides efficient inference for open-source language models with optimized deployment and scaling. Braintrust integrates seamlessly with Lepton through direct API access, wrapper functions for automatic tracing, and proxy support.

## Setup

To use Lepton models, configure your Lepton API key in Braintrust.

1. Get a Lepton API key from [Lepton AI Dashboard](https://dashboard.lepton.ai/)
2. Add the Lepton API key to your [organization's AI providers](/admin/organizations#configure-ai-providers) or to a [project's AI providers](/admin/projects#configure-ai-providers)
3. Set the Lepton API key and your Braintrust API key as environment variables

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
LEPTON_API_KEY=<your-lepton-api-key>
BRAINTRUST_API_KEY=<your-braintrust-api-key>

# If you are self-hosting Braintrust, set the URL of your hosted dataplane
# BRAINTRUST_API_URL=<your-braintrust-api-url>
```

<Note>
  API keys are encrypted at rest using [transparent data encryption](https://en.wikipedia.org/wiki/Transparent_data_encryption) with a [unique 256-bit key and nonce](https://libsodium.gitbook.io/doc/secret-key_cryptography/aead).
</Note>

## Use Lepton with Braintrust AI proxy

The [Braintrust AI Proxy](/deploy/ai-proxy) allows you to access Lepton models through a unified OpenAI-compatible interface.

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

Then, initialize the client and make a request to a Lepton model via the Braintrust AI Proxy.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const response = await client.chat.completions.create({
    model: "openai/gpt-oss-120b",
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
      model="openai/gpt-oss-120b",
      messages=[{"role": "user", "content": "Hello, world!"}],
  )
  ```
</CodeGroup>

## Trace logs with Lepton

[Trace](/instrument/custom-tracing) your Lepton LLM calls for observability and monitoring.

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
    model: "openai/gpt-oss-120b",
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
      model="openai/gpt-oss-120b",
      messages=[{"role": "user", "content": "What is machine learning?"}],
  )
  ```
</CodeGroup>

<Note>
  The Braintrust AI Proxy is not required to trace Lepton API calls. For more control, learn how to [customize traces](/instrument/advanced-tracing).
</Note>

## Evaluate with Lepton

Evaluations distill the non-deterministic outputs of Lepton models into an effective feedback loop that enables you to ship more reliable, higher quality products. Braintrust `Eval` is a simple function composed of a dataset of user inputs, a task, and a set of scorers. To learn more about evaluations, see the [Experiments](/evaluate/run-evaluations) guide.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  Eval("Lepton Evaluation", {
    data: () => [
      { input: "What is 2+2?", expected: "4" },
      { input: "What is the capital of France?", expected: "Paris" },
    ],
    task: async (input) => {
      const response = await client.chat.completions.create({
        model: "llama3-3-70b",
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
          model="llama3-3-70b",
          messages=[{"role": "user", "content": input}],
      )
      return response.choices[0].message.content


  def accuracy_scorer(output, expected, **kwargs):
      return 1 if output == expected else 0


  Eval(
      "Lepton Evaluation",
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
  To learn more about tool use, multimodal support, attachments, and masking sensitive data with Lepton, visit the [customize traces](/instrument/advanced-tracing) guide.
</Tip>
