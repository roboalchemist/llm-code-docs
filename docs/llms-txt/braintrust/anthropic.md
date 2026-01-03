# Source: https://braintrust.dev/docs/integrations/ai-providers/anthropic.md

# Anthropic

> Anthropic model provider configuration and integration guide

Anthropic provides access to Claude models including Claude 4 Sonnet, Claude 4.1 Opus, and other cutting-edge language models. Braintrust integrates seamlessly with Anthropic through direct API access, `wrapAnthropic` wrapper functions for automatic tracing, and proxy support.

## Setup

To use Anthropic with Braintrust, you'll need an Anthropic API key.

1. Visit [Anthropic's Console](https://console.anthropic.com/settings/keys) and create a new API key
2. Add the Anthropic API key to your organization's [AI providers](https://www.braintrust.dev/app/settings/secrets)
3. Set the Anthropic API key and your Braintrust API key as environment variables

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
ANTHROPIC_API_KEY=<your-anthropic-api-key>
BRAINTRUST_API_KEY=<your-braintrust-api-key>

# If you are self-hosting Braintrust, set the URL of your hosted dataplane
# BRAINTRUST_API_URL=<your-braintrust-api-url>
```

<Note>
  API keys are encrypted using 256-bit AES-GCM encryption and are not stored or logged by Braintrust.
</Note>

Install the `braintrust` and `@anthropic-ai/sdk` packages.

<CodeGroup>
  ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # pnpm
  pnpm add braintrust @anthropic-ai/sdk
  # npm
  npm install braintrust @anthropic-ai/sdk
  ```

  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install braintrust anthropic
  ```

  ```bash Go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  go get github.com/braintrustdata/braintrust-sdk-go
  go get github.com/anthropics/anthropic-sdk-go
  ```

  ```bash Ruby theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  gem install braintrust anthropic-sdk-ruby
  ```

  ```bash Java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # add to build.gradle dependencies{} block
  implementation 'dev.braintrust:braintrust-sdk-java:<version-goes-here>'
  implementation 'com.anthropic:anthropic-sdk-java:<version-goes-here>'
  ```
</CodeGroup>

## Trace with Anthropic

[Trace](/guides/traces) your Anthropic LLM calls for observability and monitoring.

### Trace automatically

Braintrust provides automatic tracing for Anthropic API calls. Braintrust handles streaming, metric collection (including cached tokens), and other details.

* **TypeScript & Python**: Use `wrapAnthropic` / `wrap_anthropic` wrapper functions
* **Go**: Use the tracing middleware with the Anthropic client
* **Ruby**: Use `Braintrust::Trace::Anthropic.wrap` to wrap the Anthropic client
* **Java**: Use the tracing interceptor with the Anthropic client

<Tip>
  For more control over tracing, learn how to [customize traces](/guides/traces/customize).
</Tip>

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import Anthropic from "@anthropic-ai/sdk";
  import { wrapAnthropic, initLogger } from "braintrust";

  // Initialize the Braintrust logger
  const logger = initLogger({
    projectName: "My Project", // Your project name
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  // Wrap the Anthropic client with the Braintrust logger
  const client = wrapAnthropic(
    new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY }),
  );

  // All API calls are automatically logged
  const result = await client.messages.create({
    model: "claude-sonnet-4-5-20250929",
    max_tokens: 1024,
    messages: [{ role: "user", content: "What is machine learning?" }],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  import anthropic
  from braintrust import init_logger, wrap_anthropic

  # Initialize the Braintrust logger
  logger = init_logger(project="My Project")

  # Wrap the Anthropic client with the Braintrust logger
  client = wrap_anthropic(anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"]))

  # All API calls are automatically logged
  result = client.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=1024,
      messages=[{"role": "user", "content": "What is machine learning?"}],
  )
  ```

  ```go  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  package main

  import (
  	"context"
  	"log"
  	"os"

  	"github.com/anthropics/anthropic-sdk-go"
  	"github.com/anthropics/anthropic-sdk-go/option"
  	"go.opentelemetry.io/otel"
  	"go.opentelemetry.io/otel/sdk/trace"

  	"github.com/braintrustdata/braintrust-sdk-go"
  	traceanthropic "github.com/braintrustdata/braintrust-sdk-go/trace/contrib/anthropic"
  )

  func main() {
  	ctx := context.Background()

  	// Set up OpenTelemetry TracerProvider
  	tp := trace.NewTracerProvider()
  	defer tp.Shutdown(ctx)
  	otel.SetTracerProvider(tp)

  	// Initialize Braintrust client
  	_, err := braintrust.New(tp,
  		braintrust.WithProject("My Project"),
  		braintrust.WithAPIKey(os.Getenv("BRAINTRUST_API_KEY")),
  	)
  	if err != nil {
  		log.Fatal(err)
  	}

  	// Create Anthropic client with tracing middleware
  	client := anthropic.NewClient(
  		option.WithMiddleware(traceanthropic.NewMiddleware()),
  	)

  	// All API calls are automatically logged
  	message, err := client.Messages.New(ctx, anthropic.MessageNewParams{
  		Model: anthropic.ModelClaude3_7SonnetLatest,
  		Messages: []anthropic.MessageParam{
  			anthropic.NewUserMessage(anthropic.NewTextBlock("What is machine learning?")),
  		},
  		MaxTokens: 1024,
  	})
  	if err != nil {
  		log.Fatal(err)
  	}
  	_ = message
  }
  ```

  ```ruby  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  require 'braintrust'
  require 'anthropic'

  # Initialize Braintrust
  Braintrust.init(project: 'My Project')

  # Create Anthropic client
  client = Anthropic::Client.new(api_key: ENV.fetch('ANTHROPIC_API_KEY', nil))

  # Wrap the client with Braintrust tracing
  Braintrust::Trace::Anthropic.wrap(client)

  # All API calls are automatically logged
  client.messages.create(
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 1024,
    messages: [{ role: 'user', content: 'What is machine learning?' }]
  )
  ```

  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;
  import dev.braintrust.Braintrust;
  import dev.braintrust.instrumentation.anthropic.BraintrustAnthropic;

  class AnthropicTracing {
      public static void main(String[] args) {
          var braintrust = Braintrust.get();
          var openTelemetry = braintrust.openTelemetryCreate();

          // Wrap the Anthropic client with Braintrust instrumentation
          AnthropicClient client = BraintrustAnthropic.wrap(openTelemetry, AnthropicOkHttpClient.fromEnv());

          // All API calls are automatically logged
          var result = client.messages().create(
              MessageCreateParams.builder()
                  .model(Model.CLAUDE_3_5_HAIKU_20241022)
                  .maxTokens(1024)
                  .addUserMessage("What is machine learning?")
                  .build());
      }
  }
  ```
</CodeGroup>

## Evaluate with Anthropic

Evaluations distill the non-deterministic outputs of Anthropic models into an effective feedback loop that enables you to ship more reliable, higher quality products. The Braintrust `Eval` function is composed of a dataset of user inputs, a task, and a set of scorers. To learn more about evaluations, see the [Experiments](/core/experiments) guide.

### Basic Anthropic eval setup

Evaluate the outputs of Anthropic models with Braintrust.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import Anthropic from "@anthropic-ai/sdk";

  const client = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  Eval("Anthropic Evaluation", {
    // An array of user inputs and expected outputs
    data: () => [
      { input: "What is 2+2?", expected: "4" },
      { input: "What is the capital of France?", expected: "Paris" },
    ],
    task: async (input) => {
      // Your Anthropic LLM call
      const response = await client.messages.create({
        model: "claude-sonnet-4-5-20250929",
        max_tokens: 1024,
        messages: [{ role: "user", content: input }],
      });
      return response.content[0].text;
    },
    scores: [
      {
        name: "accuracy",
        // A simple scorer that returns 1 if the output matches the expected output, 0 otherwise
        scorer: (args) => (args.output === args.expected ? 1 : 0),
      },
    ],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  import anthropic
  from braintrust import Eval

  client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


  def task(input):
      response = client.messages.create(
          model="claude-sonnet-4-5-20250929",
          max_tokens=1024,
          messages=[{"role": "user", "content": input}],
      )
      return response.content[0].text


  def accuracy_scorer(output, expected, **kwargs):
      return 1 if output == expected else 0


  Eval(
      "Anthropic Evaluation",
      data=[
          {"input": "What is 2+2?", "expected": "4"},
          {"input": "What is the capital of France?", "expected": "Paris"},
      ],
      task=task,
      scores=[accuracy_scorer],
  )
  ```

  ```go  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  package main

  import (
  	"context"
  	"log"
  	"os"

  	"github.com/anthropics/anthropic-sdk-go"
  	"github.com/anthropics/anthropic-sdk-go/option"
  	"go.opentelemetry.io/otel"
  	"go.opentelemetry.io/otel/sdk/trace"

  	"github.com/braintrustdata/braintrust-sdk-go"
  	"github.com/braintrustdata/braintrust-sdk-go/eval"
  	traceanthropic "github.com/braintrustdata/braintrust-sdk-go/trace/contrib/anthropic"
  )

  func main() {
  	ctx := context.Background()

  	// Set up OpenTelemetry TracerProvider
  	tp := trace.NewTracerProvider()
  	defer tp.Shutdown(ctx)
  	otel.SetTracerProvider(tp)

  	// Initialize Braintrust
  	bt, err := braintrust.New(tp,
  		braintrust.WithAPIKey(os.Getenv("BRAINTRUST_API_KEY")),
  	)
  	if err != nil {
  		log.Fatal(err)
  	}

  	// Create Anthropic client with tracing
  	client := anthropic.NewClient(
  		option.WithMiddleware(traceanthropic.NewMiddleware()),
  	)

  	// Create evaluator
  	evaluator := braintrust.NewEvaluator[string, string](bt)

  	// Run evaluation
  	_, err = evaluator.Run(ctx, eval.Opts[string, string]{
  		Experiment: "Anthropic Evaluation",
  		// Dataset of user inputs and expected outputs
  		Dataset: eval.NewDataset([]eval.Case[string, string]{
  			{Input: "What is 2+2?", Expected: "4"},
  			{Input: "What is the capital of France?", Expected: "Paris"},
  		}),
  		// Task function with Anthropic LLM call
  		Task: eval.T(func(ctx context.Context, input string) (string, error) {
  			message, err := client.Messages.New(ctx, anthropic.MessageNewParams{
  				Model: anthropic.ModelClaude3_7SonnetLatest,
  				Messages: []anthropic.MessageParam{
  					anthropic.NewUserMessage(anthropic.NewTextBlock(input)),
  				},
  				MaxTokens: 1024,
  			})
  			if err != nil {
  				return "", err
  			}
  			return message.Content[0].Text, nil
  		}),
  		// Simple scorer that returns 1 if output matches expected, 0 otherwise
  		Scorers: []eval.Scorer[string, string]{
  			eval.NewScorer("accuracy", func(ctx context.Context, r eval.TaskResult[string, string]) (eval.Scores, error) {
  				score := 0.0
  				if r.Output == r.Expected {
  					score = 1.0
  				}
  				return eval.S(score), nil
  			}),
  		},
  	})
  	if err != nil {
  		log.Fatal(err)
  	}
  }
  ```

  ```ruby  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  require 'braintrust'
  require 'anthropic'

  Braintrust.init

  client = Anthropic::Client.new(api_key: ENV.fetch('ANTHROPIC_API_KEY', nil))

  Braintrust::Eval.run(
    project: 'Anthropic Evaluation',
    experiment: 'basic-eval',
    # An array of user inputs and expected outputs
    cases: [
      { input: 'What is 2+2?', expected: '4' },
      { input: 'What is the capital of France?', expected: 'Paris' }
    ],
    # Your Anthropic LLM call
    task: lambda do |input|
      response = client.messages.create(
        model: 'claude-sonnet-4-5-20250929',
        max_tokens: 1024,
        messages: [{ role: 'user', content: input }]
        )
      response.content[0].text
    end,
    # A simple scorer that returns 1 if the output matches the expected output, 0 otherwise
    scorers: [
      Braintrust::Eval.scorer('accuracy') do |_input, expected, output|
        output == expected ? 1.0 : 0.0
      end
    ]
  )
  ```

  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;
  import dev.braintrust.Braintrust;
  import dev.braintrust.eval.DatasetCase;
  import dev.braintrust.eval.Scorer;
  import dev.braintrust.instrumentation.anthropic.BraintrustAnthropic;
  import java.util.function.Function;

  class AnthropicEvaluation {
      public static void main(String[] args) {
          var braintrust = Braintrust.get();
          var openTelemetry = braintrust.openTelemetryCreate();
          AnthropicClient client = BraintrustAnthropic.wrap(openTelemetry, AnthropicOkHttpClient.fromEnv());

          Function<String, String> taskFunction = (String input) -> {
              var request = MessageCreateParams.builder()
                  .model(Model.CLAUDE_3_5_HAIKU_20241022)
                  .maxTokens(1024)
                  .addUserMessage(input)
                  .build();
              var response = client.messages().create(request);
              return response.content().get(0).text().map(block -> block.text()).orElse("");
          };

          var eval = braintrust.<String, String>evalBuilder()
              .name("Anthropic Evaluation")
              .cases(
                  DatasetCase.of("What is 2+2?", "4"),
                  DatasetCase.of("What is the capital of France?", "Paris"))
              .taskFunction(taskFunction)
              .scorers(
                  Scorer.of("contains_answer", output ->
                      output.contains("4") || output.contains("Paris") ? 1.0 : 0.0))
              .build();

          var result = eval.run();
          System.out.println(result.createReportString());
      }
  }
  ```
</CodeGroup>

<Tip>
  Learn more about eval [data](/core/experiments/write#data) and [scorers](/core/experiments/write#scorers).
</Tip>

### Use Anthropic as an LLM judge

You can use Anthropic models to score the outputs of other AI systems. This example uses  the `LLMClassifierFromSpec` scorer to score the relevance of the outputs of an AI system.

Install the `autoevals` package to use the `LLMClassifierFromSpec` scorer.

<CodeGroup>
  ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # pnpm
  pnpm add autoevals
  # npm
  npm install autoevals
  ```

  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install autoevals
  ```
</CodeGroup>

Create a scorer that uses the `LLMClassifierFromSpec` scorer to score the relevance of the output. You can then include `relevanceScorer` as a scorer in your `Eval` function (see above).

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { LLMClassifierFromSpec } from "autoevals";

  const relevanceScorer = LLMClassifierFromSpec("Relevance", {
    choice_scores: { Relevant: 1, Irrelevant: 0 },
    model: "claude-sonnet-4-5-20250929",
    use_cot: true,
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import LLMClassifierFromSpec

  relevance_scorer = LLMClassifierFromSpec(
      "Relevance",
      choice_scores={"Relevant": 1, "Irrelevant": 0},
      model="claude-sonnet-4-5-20250929",
      use_cot=True,
  )
  ```
</CodeGroup>

## Additional features

### Tool use

Anthropic's tool use (function calling) is fully supported:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import Anthropic from "@anthropic-ai/sdk";

  const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

  const tools = [
    {
      name: "get_weather",
      description: "Get current weather for a location",
      input_schema: {
        type: "object",
        properties: {
          location: { type: "string", description: "City name" },
        },
        required: ["location"],
      },
    },
  ];

  const response = await client.messages.create({
    model: "claude-sonnet-4-5-20250929",
    max_tokens: 1024,
    messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
    tools,
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from anthropic import Anthropic

  client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

  tools = [
      {
          "name": "get_weather",
          "description": "Get current weather for a location",
          "input_schema": {
              "type": "object",
              "properties": {
                  "location": {"type": "string", "description": "City name"},
              },
              "required": ["location"],
          },
      }
  ]

  response = client.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=1024,
      messages=[{"role": "user", "content": "What's the weather in San Francisco?"}],
      tools=tools,  # [!code highlight]
  )
  ```
</CodeGroup>

### System prompts

Anthropic models support system prompts for better instruction following.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import Anthropic from "@anthropic-ai/sdk";

  const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

  const response = await client.messages.create({
    model: "claude-sonnet-4-5-20250929",
    max_tokens: 1024,
    system: "You are a helpful assistant that responds in JSON format.",
    messages: [{ role: "user", content: "What is the capital of France?" }],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from anthropic import Anthropic

  client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

  response = client.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=1024,
      system="You are a helpful assistant that responds in JSON format.",  # [!code highlight]
      messages=[{"role": "user", "content": "What is the capital of France?"}],
  )
  ```
</CodeGroup>

### Cached tokens

Anthropic supports prompt caching to reduce costs and latency for repeated content.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import Anthropic from "@anthropic-ai/sdk";

  const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

  const response = await client.messages.create({
    model: "claude-sonnet-4-5-20250929",
    max_tokens: 1024,
    system: [
      {
        type: "text",
        text: "You are an AI assistant analyzing the following document...",
        cache_control: { type: "ephemeral" },
      },
    ],
    messages: [{ role: "user", content: "Summarize the key points." }],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from anthropic import Anthropic

  client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

  response = client.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=1024,
      system=[
          {
              "type": "text",
              "text": "You are an AI assistant analyzing the following document...",
              "cache_control": {"type": "ephemeral"},  # [!code highlight]
          }
      ],
      messages=[{"role": "user", "content": "Summarize the key points."}],
  )
  ```
</CodeGroup>

### Multimodal content, attachments, errors, and masking sensitive data

To learn more about these topics, check out the [customize traces](/guides/traces/customize) guide.

## Use Anthropic with Braintrust AI proxy

You can also access Anthropic models through the [Braintrust AI Proxy](/guides/proxy), which provides a unified, OpenAI-compatible interface for multiple providers.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const response = await client.chat.completions.create({
    model: "claude-sonnet-4-5-20250929",
    messages: [{ role: "user", content: "What is a proxy?" }],
    seed: 1, // A seed activates the proxy's cache
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
      model="claude-sonnet-4-5-20250929",
      messages=[{"role": "user", "content": "What is a proxy?"}],
      seed=1,  # A seed activates the proxy's cache
  )
  ```
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt