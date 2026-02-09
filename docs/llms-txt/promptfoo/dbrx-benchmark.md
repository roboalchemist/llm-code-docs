# Source: https://www.promptfoo.dev/docs/guides/dbrx-benchmark/

# DBRX vs Mixtral vs GPT: create your own benchmark

There are many generic benchmarks that measure LLMs like DBRX, Mixtral, and others in a similar performance class. But public benchmarks are often gamed and don't always reflect real use cases.

How well do these models actually perform for _your specific needs_? As a developer, it's good to understand the tradeoffs between each model.

In this guide, we'll walk through how to create your own personalized benchmark comparing DBRX, Mixtral 8x7b, and GPT-3.5 on use cases that are relevant to you.

The end result will be a custom benchmark that looks similar to this:

![dbrx, mixtral, and gpt comparison](https://www.promptfoo.dev/assets/images/dbrx-mixtral-gpt-comparison-73f928d72db9569523bfcd817c845b31.png)

## Requirements

- OpenRouter API key for DBRX and Mixtral.
- OpenAI API key for gpt-5-mini
- Node 18+

## Step 1: Initial Setup

Create a new directory for your comparison project and initialize it with `promptfoo init`.

```sh
npx promptfoo@latest init dbrx-benchmark
```

For more details on promptfoo setup, see [Installation](https://www.promptfoo.dev/docs/installation/).

## Step 2: Configure the models

After entering the `dbrx-benchmark` directory, edit the `promptfooconfig.yaml` to include the models you want to compare.

OpenRouter uses the OpenAI format, so we'll just override the base URL of the OpenAI provider. Here's an example configuration with DBRX, Mixtral, and GPT-3.5:

```yaml
providers:
  - id: openai:chat:databricks/dbrx-instruct
    config:
      apiBaseUrl: https://openrouter.ai/api/v1
      apiKeyEnvar: OPENROUTER_API_KEY
      temperature: 0
  - id: openai:chat:mistralai/mixtral-8x7b-instruct
    config:
      apiBaseUrl: https://openrouter.ai/api/v1
      apiKeyEnvar: OPENROUTER_API_KEY
      temperature: 0
  - id: openai:gpt-5-mini
```

Set your API keys as environment variables:

```sh
export OPENROUTER_API_KEY=your_openrouter_api_key
export OPENAI_API_KEY=your_openai_api_key
```

### Optional: Configure model parameters

Customize the behavior of each model by setting parameters such as `temperature` and `max_tokens` or `max_length`:

```yaml
providers:
  - id: openai:chat:databricks/dbrx-instruct
    config:
      apiBaseUrl: https://openrouter.ai/api/v1
      apiKeyEnvar: OPENROUTER_API_KEY
      temperature: 0
  - id: openai:chat:mistralai/mixtral-8x7b-instruct
    config:
      apiBaseUrl: https://openrouter.ai/api/v1
      apiKeyEnvar: OPENROUTER_API_KEY
      temperature: 0
  - id: openai:gpt-5-mini
    config:
      temperature: 0
```

### Optional: Add more models

If you're interested in comparing Llama-70B or Gemma, for example, add `meta-llama/llama-2-70b-chat` and `google/gemma-7b-it`.

If you're locally hosting, you can use [ollama](https://www.promptfoo.dev/docs/providers/ollama/), [LocalAI](https://www.promptfoo.dev/docs/providers/localai/), [vllm](https://www.promptfoo.dev/docs/providers/vllm/), etc.

## Step 3: Set up prompts

Set up the prompts that you want to run for each model. In this case, we'll just use a simple prompt, because we want to compare model performance.

```yaml
prompts:
  - Think deeply and answer concisely: {{query}}
```

If desired, you can test multiple prompts (just add more to the list), test [different prompts for each model](https://www.promptfoo.dev/docs/configuration/prompts/#model-specific-prompts), send [custom JSON](https://www.promptfoo.dev/docs/providers/openai/#formatting-chat-messages), or [call your own application logic](https://www.promptfoo.dev/docs/configuration/prompts/#dynamic-prompts-functions).

## Step 4: Add test cases

Define the test cases that you want to use for the evaluation. This includes setting up variables that will be interpolated into the prompts.

We're just going to make up some questions as an example. You should modify the prompt and test cases to reflect your own LLM use case:

```yaml
tests:
  - vars:
      query: What is the capital of France?
  - vars:
      query: Explain the theory of relativity.
  - vars:
      query: Write a poem about the sea.
  - vars:
      query: What are the health benefits of eating apples?
  - vars:
      query: "Translate 'Hello, how are you?' into Spanish."
  - vars:
      query: Output a JSON list of colors
```

For automated testing, add assertions. These are automatically checked against the outputs:

```yaml
tests:
  - vars:
      query: What is the capital of France?
    assert:
      - type: contains
        value: Paris
  - vars:
      query: Explain the theory of relativity.
    assert:
      - type: contains
        value: Einstein
  - vars:
      query: Write a poem about the sea.
    assert:
      - type: llm-rubric
        value: The poem should evoke imagery such as waves or the ocean.
  - vars:
      query: What are the health benefits of eating apples?
    assert:
      - type: contains
        value: vitamin
  - vars:
      query: "Translate 'Hello, how are you?' into Spanish."
    assert:
      - type: similar
        value: Hola, ¿cómo estás?
  - vars:
      query: Output a JSON list of colors
    assert:
      - type: is-json
      - type: latency
        threshold: 5000
```

Many types of assertions are supported, both deterministic and LLM-graded. See [Assertions and Metrics](https://www.promptfoo.dev/docs/configuration/expected-outputs/) to find assertions that match your needs.

## Step 5: Run the comparison

With everything configured, run the evaluation using the `promptfoo` CLI:

```sh
npx promptfoo@latest eval
```

This command will execute each test case against each configured model and record the results.

To visualize the results, use the `promptfoo` viewer:

```sh
npx promptfoo@latest view
```

It will show results like so:

![dbrx, mixtral, and gpt comparison](https://www.promptfoo.dev/assets/images/dbrx-mixtral-gpt-comparison-73f928d72db9569523bfcd817c845b31.png)

Clicking into a specific output will show details on the assertions:

![dbrx eval details](https://www.promptfoo.dev/assets/images/dbrx-mixtral-gpt-comparison-details-d1f5bbfe570d2f5263054a430dd51775.png)

You can also output the results to a file in various formats, such as JSON, YAML, or CSV:

```sh
npx promptfoo@latest eval -o results.csv
```

## Analysis

The comparison provides a side-by-side performance view of DBRX, Mistral, and GPT-3.5 based on your test cases. Use this data to make informed decisions about which LLM best suits your application.

In the very basic example we ran above, DBRX tends to answer verbosely, which caused some failures:

![dbrx eval failures](https://www.promptfoo.dev/assets/images/dbrx-mixtral-gpt-comparison-failures-719f7b40bb3e0bb6e5d1537361d95b24.png)

This doesn't mean DBRX is not capable of answering well - it probably just means we need to tweak the prompt a bit in order to get output quality similar to the other models.

Our benchmark for our custom use case rated DBRX at 66%, Mixtral at 100%, and GPT 3.5 at 83%. While public benchmarks can provide a general sense of model performance, they are no substitute for running a benchmark on your own data and use cases.

## Next steps

promptfoo is a completely [open source](https://github.com/promptfoo/promptfoo) eval project. If you're interested in running your own evals, head over to [Getting Started](https://www.promptfoo.dev/docs/getting-started/).