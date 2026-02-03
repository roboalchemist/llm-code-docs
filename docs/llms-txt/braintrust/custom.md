# Source: https://braintrust.dev/docs/integrations/ai-providers/custom.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom providers

> Set up custom AI providers with Braintrust for evaluation and tracing

Braintrust supports custom AI providers, allowing you to integrate any AI model or endpoint into your evaluation and tracing workflows. This includes custom models from existing providers, self-hosted models, or proprietary AI services.

Custom providers appear alongside standard providers in model selection dropdowns.

## Setup

If you have custom models as part of your OpenAI or other accounts, or if you're running your own AI endpoints, you can add them to Braintrust by configuring a custom provider.

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Organization** or **Project**, select **AI providers**.
3. Under **Custom providers**, click **Create**.
4. Configure your custom endpoint with the required parameters.

### Configuration options

Specify the following for your custom provider.

* **Provider name**: A unique name for your custom provider
* **Model name**: The name of your custom model (e.g., `gpt-3.5-acme`, `my-custom-llama`)
* **Endpoint URL**: The API endpoint for your custom model
* **Format**: The API format (`openai`, `anthropic`, `google`, `window`, or `js`)
* **Flavor**: Whether it's a `chat` or `completion` model (default: `chat`)
* **Headers**: Any custom headers required for authentication or configuration

### Custom headers and templating

Any headers you add to the configuration are passed through in the request to the custom endpoint. The values of the headers can be templated using Mustache syntax with these supported variables:

* `{{email}}`: Email of the user associated with the Braintrust API key
* `{{model}}`: The model name being requested

Example header configuration:

```
Authorization: Bearer {{api_key}}
X-User-Email: {{email}}
X-Model: {{model}}
```

### Streaming support

If your endpoint supports streaming natively, enable **This endpoint supports streaming**. Braintrust will automatically convert the response to streaming format, allowing your models to work in the playground and other streaming contexts.

### Model metadata

You can optionally specify:

* **Multimodal**: Whether the model supports multimodal inputs
* **Input cost**: Cost per million input tokens (for experiment cost estimation)
* **Output cost**: Cost per million output tokens (for experiment cost estimation)

<Note>
  API keys are encrypted at rest using [transparent data encryption](https://en.wikipedia.org/wiki/Transparent_data_encryption) with a [unique 256-bit key and nonce](https://libsodium.gitbook.io/doc/secret-key_cryptography/aead).
</Note>

## Trace logs with custom providers

[Trace](/instrument/custom-tracing) custom provider LLM calls for observability and monitoring.

### Automatic tracing

Once your custom provider is configured, tracing works automatically.

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
    model: "my-custom-model", // Your custom model name
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
      model="my-custom-model",  # Your custom model name
      messages=[{"role": "user", "content": "What is machine learning?"}],
  )
  ```
</CodeGroup>

### Manual tracing

For more control over tracing, you can manually log calls to your custom provider.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { trace } from "braintrust";

  // Use your custom provider directly
  const customResponse = await fetch("https://your-custom-endpoint.com/v1/chat", {
    method: "POST",
    headers: {
      Authorization: "Bearer your-custom-api-key",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: "my-custom-model",
      messages: [{ role: "user", content: "Hello!" }],
    }),
  });

  // Manually trace the call
  trace({
    name: "custom-model-call",
    input: { message: "Hello!" },
    output: await customResponse.json(),
    metadata: {
      model: "my-custom-model",
      provider: "custom",
    },
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import requests
  from braintrust import trace

  # Use your custom provider directly
  response = requests.post(
      "https://your-custom-endpoint.com/v1/chat",
      headers={
          "Authorization": "Bearer your-custom-api-key",
          "Content-Type": "application/json",
      },
      json={
          "model": "my-custom-model",
          "messages": [{"role": "user", "content": "Hello!"}],
      },
  )

  # Manually trace the call
  trace(
      name="custom-model-call",
      input={"message": "Hello!"},
      output=response.json(),
      metadata={
          "model": "my-custom-model",
          "provider": "custom",
      },
  )
  ```
</CodeGroup>

## Evaluations

Evaluations distill the non-deterministic outputs of custom models into an effective feedback loop that enables you to ship more reliable, higher quality products. Braintrust `Eval` is a simple function composed of a dataset of user inputs, a task, and a set of scorers. To learn more about evaluations, see the [Experiments guide](/evaluate/run-evaluations).

### Basic evaluation setup

Use your custom models as evaluators in Braintrust experiments.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  Eval("Custom Model Evaluation", {
    data: () => [
      { input: "What is 2+2?", expected: "4" },
      { input: "What is the capital of France?", expected: "Paris" },
    ],
    task: async (input) => {
      const response = await client.chat.completions.create({
        model: "my-custom-model",
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
          model="my-custom-model",
          messages=[{"role": "user", "content": input}],
      )
      return response.choices[0].message.content


  def accuracy_scorer(output, expected, **kwargs):
      return 1 if output == expected else 0


  Eval(
      "Custom Model Evaluation",
      data=[
          {"input": "What is 2+2?", "expected": "4"},
          {"input": "What is the capital of France?", "expected": "Paris"},
      ],
      task=task,
      scores=[accuracy_scorer],
  )
  ```
</CodeGroup>

### Use custom providers for LLM-as-a-judge

Custom models can serve as evaluators for other AI systems.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { LLMClassifierFromSpec } from "autoevals";

  const relevanceScorer = LLMClassifierFromSpec("Relevance", {
    choice_scores: { Relevant: 1, Irrelevant: 0 },
    model: "my-custom-model",
    use_cot: true,
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import LLMClassifierFromSpec

  relevance_scorer = LLMClassifierFromSpec(
      "Relevance",
      choice_scores={"Relevant": 1, "Irrelevant": 0},
      model="my-custom-model",
      use_cot=True,
  )
  ```
</CodeGroup>

### Compare custom models

You can run experiments comparing your custom models against standard providers.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";

  const models = [
    "gpt-4o-mini", // Standard OpenAI model
    "claude-sonnet-4-5-20250929", // Standard Anthropic model
    "my-custom-model", // Your custom model
  ];

  for (const model of models) {
    Eval(`Model Comparison - ${model}`, {
      data: () => [
        { input: "Explain quantum computing", expected: "technical_explanation" },
        { input: "Write a haiku about code", expected: "creative_poetry" },
      ],
      task: async (input) => {
        const response = await client.chat.completions.create({
          model,
          messages: [{ role: "user", content: input }],
        });
        return response.choices[0].message.content;
      },
      scores: [
        {
          name: "quality",
          scorer: LLMClassifierFromSpec("Quality", {
            choice_scores: { High: 1, Medium: 0.5, Low: 0 },
            model: "gpt-4o", // Use a standard model for evaluation
          }),
        },
      ],
    });
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import LLMClassifierFromSpec
  from braintrust import Eval

  models = [
      "gpt-4o-mini",  # Standard OpenAI model
      "claude-sonnet-4-5-20250929",  # Standard Anthropic model
      "my-custom-model",  # Your custom model
  ]

  quality_scorer = LLMClassifierFromSpec(
      "Quality",
      choice_scores={"High": 1, "Medium": 0.5, "Low": 0},
      model="gpt-4o",  # Use a standard model for evaluation
  )

  for model in models:

      def task(input):
          response = client.chat.completions.create(
              model=model,
              messages=[{"role": "user", "content": input}],
          )
          return response.choices[0].message.content

      Eval(
          f"Model Comparison - {model}",
          data=[
              {"input": "Explain quantum computing", "expected": "technical_explanation"},
              {"input": "Write a haiku about code", "expected": "creative_poetry"},
          ],
          task=task,
          scores=[quality_scorer],
      )
  ```
</CodeGroup>

## Common use cases

### Self-hosted models

For self-hosted models (e.g. using Ollama, vLLM, or custom deployments):

1. Set the endpoint URL to your self-hosted service
2. Choose the appropriate format based on your API compatibility
3. Configure any required authentication headers
4. Set streaming support based on your implementation

### Fine-tuned models

For fine-tuned versions of existing models:

1. Use the same format as the base model
2. Set the model name to your fine-tuned model identifier
3. Configure the endpoint URL if using a custom deployment
4. Add any provider-specific headers for accessing fine-tuned models

### Proprietary AI services

For proprietary or enterprise AI services:

1. Configure the endpoint URL provided by your AI service
2. Set up authentication headers as required
3. Choose the format that best matches your service's API
4. Enable or disable streaming based on service capabilities

<Note>
  Test your custom provider configuration in a Braintrust [Playground](/evaluate/playgrounds) before running large-scale evaluations to ensure everything is working correctly.
</Note>
