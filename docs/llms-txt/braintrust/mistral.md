# Source: https://braintrust.dev/docs/integrations/ai-providers/mistral.md

# Mistral

> Mistral AI model provider configuration and integration guide

Mistral AI provides access to state-of-the-art language models including Mistral Large, Mistral Medium, and other advanced models. Braintrust integrates seamlessly with Mistral through direct API access, wrapper functions for automatic tracing, and proxy support.

## Setup

To use Mistral models, configure your Mistral API key in Braintrust.

1. Get a Mistral API key from [Mistral AI Console](https://console.mistral.ai/)
2. Add the Mistral API key to your organization's [AI providers](https://www.braintrust.dev/app/settings/secrets)
3. Set the Mistral API key and your Braintrust API key as environment variables

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
MISTRAL_API_KEY=<your-mistral-api-key>
BRAINTRUST_API_KEY=<your-braintrust-api-key>

# If you are self-hosting Braintrust, set the URL of your hosted dataplane
# BRAINTRUST_API_URL=<your-braintrust-api-url>
```

<Note>
  API keys are encrypted using 256-bit AES-GCM encryption and are not stored or logged by Braintrust.
</Note>

## Use Mistral with Braintrust AI proxy

The [Braintrust AI Proxy](/guides/proxy) allows you to access Mistral models through a unified OpenAI-compatible interface.

First, install the `braintrust` and `openai` packages.

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

Then, initialize the client and make a request to a Mistral model via the Braintrust AI Proxy.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const response = await client.chat.completions.create({
    model: "mistral-large-latest",
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
      model="mistral-large-latest",
      messages=[{"role": "user", "content": "Hello, world!"}],
  )
  ```
</CodeGroup>

## Trace logs with Mistral

[Trace](/guides/traces) your Mistral LLM calls for observability and monitoring.

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
    model: "mistral-large-latest",
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
      model="mistral-large-latest",
      messages=[{"role": "user", "content": "What is machine learning?"}],
  )
  ```
</CodeGroup>

<Tip>
  The Braintrust AI Proxy is not required. For more control, learn how to [customize traces](/guides/traces/customize).
</Tip>

## Evaluate with Mistral

Evaluations distill the non-deterministic outputs of Mistral models into an effective feedback loop that enables you to ship more reliable, higher quality products. Braintrust `Eval` is a simple function composed of a dataset of user inputs, a task, and a set of scorers. To learn more about evaluations, see the [Experiments](/core/experiments) guide.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  Eval("Mistral Evaluation", {
    data: () => [
      { input: "What is 2+2?", expected: "4" },
      { input: "What is the capital of France?", expected: "Paris" },
    ],
    task: async (input) => {
      const response = await client.chat.completions.create({
        model: "mistral-large-latest",
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
          model="mistral-large-latest",
          messages=[{"role": "user", "content": input}],
      )
      return response.choices[0].message.content


  def accuracy_scorer(output, expected, **kwargs):
      return 1 if output == expected else 0


  Eval(
      "Mistral Evaluation",
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
  To learn more about tool use, multimodal support, attachments, and masking sensitive data with Mistral, visit the [customize traces](/guides/traces/customize) guide.
</Tip>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt