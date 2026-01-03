# Source: https://braintrust.dev/docs/integrations/ai-providers/openai.md

# OpenAI

> OpenAI model provider configuration and integration guide

OpenAI provides access to GPT models including GPT-5 and other cutting-edge language models. Braintrust integrates seamlessly with OpenAI through direct API access, `wrapOpenAI` wrapper functions for automatic tracing, and proxy support.

## Setup

To use OpenAI with Braintrust, you'll need an OpenAI API key.

1. Visit [OpenAI's API platform](https://platform.openai.com/api-keys) and create a new API key
2. Add the OpenAI API key to your organization's [AI providers](https://www.braintrust.dev/app/settings/secrets)
3. Set the OpenAI API key and your Braintrust API key as environment variables

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
OPENAI_API_KEY=<your-openai-api-key>
BRAINTRUST_API_KEY=<your-braintrust-api-key>

# If you are self-hosting Braintrust, set the URL of your hosted dataplane
# BRAINTRUST_API_URL=<your-braintrust-api-url>
```

<Note>
  API keys are encrypted using 256-bit AES-GCM encryption and are not stored or logged by Braintrust.
</Note>

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

  ```bash Go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  go get github.com/braintrustdata/braintrust-sdk-go
  go get github.com/openai/openai-go
  ```

  ```bash Ruby theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  gem install braintrust ruby-openai
  ```

  ```bash Java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # add to build.gradle dependencies{} block
  implementation 'dev.braintrust:braintrust-sdk-java:<version-goes-here>'
  implementation 'com.openai:openai-java-sdk:<version-goes-here>'
  ```

  ```bash C# theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # add to .csproj file
  dotnet add package Braintrust.Sdk
  dotnet add package OpenAI
  ```
</CodeGroup>

## Trace with OpenAI

[Trace](/guides/traces) your OpenAI LLM calls for observability and monitoring.

Using the OpenAI Agents SDK? See the [OpenAI Agents SDK](/integrations/sdk-integrations/openai-agents-sdk) framework docs.

### Trace automatically

Braintrust provides automatic tracing for OpenAI API calls, handling streaming, metrics collection, and other details.

* **TypeScript & Python**: Use `wrapOpenAI` / `wrap_openai` wrapper functions
* **Go**: Use the tracing middleware with the OpenAI client
* **Ruby**: Use `Braintrust::Trace::OpenAI.wrap` to wrap the OpenAI client
* **Java**: Use the tracing interceptor with the OpenAI client
* **C#**: Use `BraintrustOpenAI.WrapOpenAI` to wrap the OpenAI client

<Tip>
  For more control over tracing, learn how to [customize traces](/guides/traces/customize).
</Tip>

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import OpenAI from "openai";

  // Initialize the Braintrust logger
  const logger = initLogger({
    projectName: "My Project", // Your project name
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  // Wrap the OpenAI client with wrapOpenAI
  const client = wrapOpenAI(
    new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    }),
  );

  // All API calls are automatically logged
  const result = await client.chat.completions.create({
    model: "gpt-5-mini",
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: "What is machine learning?" },
    ],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from braintrust import init_logger, wrap_openai
  from openai import OpenAI

  logger = init_logger(project="My Project")
  client = wrap_openai(OpenAI(api_key=os.environ["OPENAI_API_KEY"]))

  # All API calls are automatically logged
  result = client.chat.completions.create(
      model="gpt-5-mini",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "What is machine learning?"},
      ],
  )
  ```

  ```go  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  package main

  import (
  	"context"
  	"log"
  	"os"

  	"github.com/openai/openai-go"
  	"github.com/openai/openai-go/option"
  	"go.opentelemetry.io/otel"
  	"go.opentelemetry.io/otel/sdk/trace"

  	"github.com/braintrustdata/braintrust-sdk-go"
  	traceopenai "github.com/braintrustdata/braintrust-sdk-go/trace/contrib/openai"
  )

  func main() {
  	// Set up OpenTelemetry TracerProvider
  	tp := trace.NewTracerProvider()
  	defer tp.Shutdown(context.Background())
  	otel.SetTracerProvider(tp)

  	// Initialize Braintrust client
  	_, err := braintrust.New(tp,
  		braintrust.WithProject("My Project"),
  		braintrust.WithAPIKey(os.Getenv("BRAINTRUST_API_KEY")),
  	)
  	if err != nil {
  		log.Fatal(err)
  	}

  	// Create OpenAI client with tracing middleware
  	client := openai.NewClient(
  		option.WithMiddleware(traceopenai.NewMiddleware()),
  	)

  	// All API calls are automatically logged
  	result, err := client.Chat.Completions.New(context.Background(), openai.ChatCompletionNewParams{
  		Messages: []openai.ChatCompletionMessageParamUnion{
  			openai.SystemMessage("You are a helpful assistant."),
  			openai.UserMessage("What is machine learning?"),
  		},
  		Model: openai.ChatModelGPT4o,
  	})
  	if err != nil {
  		log.Fatal(err)
  	}
  	_ = result
  }
  ```

  ```ruby  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  require 'braintrust'
  require 'openai'

  # Initialize Braintrust
  Braintrust.init(project: 'My Project')

  # Create OpenAI client
  client = OpenAI::Client.new(api_key: ENV.fetch('OPENAI_API_KEY', nil))

  # Wrap the client with Braintrust tracing
  Braintrust::Trace::OpenAI.wrap(client)

  # All API calls are automatically logged
  client.chat.completions.create(
    model: 'gpt-4o-mini',
    messages: [
      { role: 'system', content: 'You are a helpful assistant.' },
      { role: 'user', content: 'What is machine learning?' }
    ]
  )
  ```

  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import com.openai.client.OpenAIClient;
  import com.openai.client.okhttp.OpenAIOkHttpClient;
  import com.openai.models.ChatModel;
  import com.openai.models.chat.completions.ChatCompletionCreateParams;
  import dev.braintrust.Braintrust;
  import dev.braintrust.instrumentation.openai.BraintrustOpenAI;

  class OpenAITracing {
      public static void main(String[] args) {
          var braintrust = Braintrust.get();
          var openTelemetry = braintrust.openTelemetryCreate();

          // Wrap the OpenAI client with Braintrust instrumentation
          OpenAIClient client = BraintrustOpenAI.wrapOpenAI(openTelemetry, OpenAIOkHttpClient.fromEnv());

          // All API calls are automatically logged
          var request = ChatCompletionCreateParams.builder()
              .model(ChatModel.GPT_4O_MINI)
              .addSystemMessage("You are a helpful assistant.")
              .addUserMessage("What is machine learning?")
              .temperature(0.0)
              .build();

          var result = client.chat().completions().create(request);
      }
  }
  ```

  ```csharp  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  using System;
  using System.Threading.Tasks;
  using Braintrust.Sdk;
  using Braintrust.Sdk.Instrumentation.OpenAI;
  using OpenAI;
  using OpenAI.Chat;

  class OpenAITracing
  {
      static async Task Main(string[] args)
      {
          var braintrust = Braintrust.Sdk.Braintrust.Get();
          var activitySource = braintrust.GetActivitySource();

          var apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY");
          if (string.IsNullOrEmpty(apiKey))
          {
              Console.WriteLine("Error: OPENAI_API_KEY environment variable is not set.");
              return;
          }

          // Wrap the OpenAI client with Braintrust instrumentation
          var client = BraintrustOpenAI.WrapOpenAI(
              activitySource,
              apiKey
          );

          // All API calls are automatically logged
          var chatClient = client.GetChatClient("gpt-4o-mini");
          var messages = new ChatMessage[]
          {
              new SystemChatMessage("You are a helpful assistant."),
              new UserChatMessage("What is machine learning?")
          };

          var result = await chatClient.CompleteChatAsync(messages);
      }
  }
  ```
</CodeGroup>

### Stream OpenAI responses

`wrap_openai`/`wrapOpenAI` can automatically log metrics like `prompt_tokens`, `completion_tokens`, and `tokens` for streaming LLM calls if the LLM API returns them. Set `include_usage` to `true` in the `stream_options` parameter to receive these metrics from OpenAI.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  model: "gpt-5-mini",
    messages: [{ role: "user", content: "Count to 10" }],
    stream: true,
    stream_options: {
      include_usage: true, // Required for token metrics
    },
  });

  for await (const chunk of result) {
    process.stdout.write(chunk.choices[0]?.delta?.content || "");
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  model="gpt-5-mini",
      messages=[{"role": "user", "content": "Count to 10"}],
      stream=True,
      stream_options={"include_usage": True},  # Required for token metrics
  )

  for chunk in result:
      print(chunk.choices[0].delta.content or "", end="")
  ```
</CodeGroup>

## Evaluate with OpenAI

Evaluations help you distill the non-deterministic outputs of OpenAI models into an effective feedback loop that enables you to ship more reliable, higher quality products. Braintrust `Eval` is a simple function composed of a dataset of user inputs, a task, and a set of scorers. To learn more about evaluations, see the [Experiments](/core/experiments) guide.

### Basic OpenAI eval setup

Evaluate the outputs of OpenAI models with Braintrust.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import { OpenAI } from "openai";

  const client = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
  });

  Eval("OpenAI Evaluation", {
    // An array of user inputs and expected outputs
    data: () => [
      { input: "What is 2+2?", expected: "4" },
      { input: "What is the capital of France?", expected: "Paris" },
    ],
    task: async (input) => {
      // Your OpenAI LLM call
      const response = await client.chat.completions.create({
        model: "gpt-5-mini",
        messages: [{ role: "user", content: input }],
      });
      return response.choices[0].message.content;
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

  from braintrust import Eval
  from openai import OpenAI

  client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


  def task(input):
      response = client.chat.completions.create(
          model="gpt-5-mini",
          messages=[{"role": "user", "content": input}],
      )
      return response.choices[0].message.content


  def accuracy_scorer(output, expected, **kwargs):
      return 1 if output == expected else 0


  Eval(
      "OpenAI Evaluation",
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

  	"github.com/openai/openai-go"
  	"github.com/openai/openai-go/option"
  	"go.opentelemetry.io/otel"
  	"go.opentelemetry.io/otel/sdk/trace"

  	"github.com/braintrustdata/braintrust-sdk-go"
  	"github.com/braintrustdata/braintrust-sdk-go/eval"
  	traceopenai "github.com/braintrustdata/braintrust-sdk-go/trace/contrib/openai"
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

  	// Create OpenAI client with tracing
  	client := openai.NewClient(
  		option.WithMiddleware(traceopenai.NewMiddleware()),
  	)

  	// Create evaluator
  	evaluator := braintrust.NewEvaluator[string, string](bt)

  	// Run evaluation
  	_, err = evaluator.Run(ctx, eval.Opts[string, string]{
  		Experiment: "OpenAI Evaluation",
  		// Dataset of user inputs and expected outputs
  		Dataset: eval.NewDataset([]eval.Case[string, string]{
  			{Input: "What is 2+2?", Expected: "4"},
  			{Input: "What is the capital of France?", Expected: "Paris"},
  		}),
  		// Task function with OpenAI LLM call
  		Task: eval.T(func(ctx context.Context, input string) (string, error) {
  			response, err := client.Chat.Completions.New(ctx, openai.ChatCompletionNewParams{
  				Model: openai.ChatModelGPT4oMini,
  				Messages: []openai.ChatCompletionMessageParamUnion{
  					openai.UserMessage(input),
  				},
  			})
  			if err != nil {
  				return "", err
  			}
  			return response.Choices[0].Message.Content, nil
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
  require 'openai'

  Braintrust.init

  client = OpenAI::Client.new(api_key: ENV.fetch('OPENAI_API_KEY', nil))

  Braintrust::Eval.run(
    project: 'OpenAI Evaluation',
    experiment: 'basic-eval',
    # An array of user inputs and expected outputs
    cases: [
      { input: 'What is 2+2?', expected: '4' },
      { input: 'What is the capital of France?', expected: 'Paris' }
    ],
    # Your OpenAI LLM call
    task: lambda do |input|
      response = client.chat.completions.create(
        model: 'gpt-4o-mini',
        messages: [{ role: 'user', content: input }]
      )
      response.choices[0].message.content
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
  import com.openai.client.OpenAIClient;
  import com.openai.client.okhttp.OpenAIOkHttpClient;
  import com.openai.models.ChatModel;
  import com.openai.models.chat.completions.ChatCompletionCreateParams;
  import dev.braintrust.Braintrust;
  import dev.braintrust.eval.DatasetCase;
  import dev.braintrust.eval.Scorer;
  import dev.braintrust.instrumentation.openai.BraintrustOpenAI;
  import java.util.function.Function;

  class OpenAIEvaluation {
      public static void main(String[] args) {
          var braintrust = Braintrust.get();
          var openTelemetry = braintrust.openTelemetryCreate();
          OpenAIClient client = BraintrustOpenAI.wrapOpenAI(openTelemetry, OpenAIOkHttpClient.fromEnv());

          Function<String, String> taskFunction = (String input) -> {
              var request = ChatCompletionCreateParams.builder()
                  .model(ChatModel.GPT_4O_MINI)
                  .addUserMessage(input)
                  .temperature(0.0)
                  .build();
              var response = client.chat().completions().create(request);
              return response.choices().get(0).message().content().orElse("");
          };

          var eval = braintrust.<String, String>evalBuilder()
              .name("OpenAI Evaluation")
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

  ```csharp  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  using System;
  using Braintrust.Sdk;
  using Braintrust.Sdk.Eval;
  using Braintrust.Sdk.Instrumentation.OpenAI;
  using OpenAI;
  using OpenAI.Chat;

  class OpenAIEvaluation
  {
      static void Main(string[] args)
      {
          var braintrust = Braintrust.Sdk.Braintrust.Get();
          var activitySource = braintrust.GetActivitySource();

          var apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY");
          if (string.IsNullOrEmpty(apiKey))
          {
              Console.WriteLine("Error: OPENAI_API_KEY environment variable is not set.");
              return;
          }

          var client = BraintrustOpenAI.WrapOpenAI(
              activitySource,
              apiKey
          );

          // Define the task function that uses OpenAI
          string TaskFunction(string input)
          {
              var chatClient = client.GetChatClient("gpt-4o-mini");
              var messages = new ChatMessage[]
              {
                  new UserChatMessage(input)
              };
              var options = new ChatCompletionOptions
              {
                  Temperature = 0.0f
              };
              var response = chatClient.CompleteChat(messages, options);
              return response.Value.Content[0].Text;
          }

          // Create and run the evaluation
          var eval = braintrust
              .EvalBuilder<string, string>()
              .Name("OpenAI Evaluation")
              .Cases(
                  DatasetCase<string, string>.Of("What is 2+2?", "4"),
                  DatasetCase<string, string>.Of("What is the capital of France?", "Paris")
              )
              .TaskFunction(TaskFunction)
              .Scorers(
                  Scorer<string, string>.Of("accuracy", (expected, actual) =>
                      actual.Contains(expected) ? 1.0 : 0.0)
              )
              .Build();

          var result = eval.Run();
          Console.WriteLine(result.CreateReportString());
      }
  }
  ```
</CodeGroup>

<Tip>
  Learn more about eval [data](/core/experiments/write#data) and [scorers](/core/experiments/write#scorers).
</Tip>

### Use OpenAI as an LLM judge

You can use OpenAI models to score the outputs of other AI systems. This example uses the `LLMClassifierFromSpec` scorer to score the relevance of the outputs of an AI system.

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

Create a scorer that uses the `LLMClassifierFromSpec` scorer to score the relevance of the outputs of an AI system. You can then include `relevanceScorer` as a scorer in your `Eval` function (see above).

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { LLMClassifierFromSpec } from "autoevals";

  const relevanceScorer = LLMClassifierFromSpec("Relevance", {
    choice_scores: { Relevant: 1, Irrelevant: 0 },
    model: "gpt-5-mini",
    use_cot: true,
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from autoevals import LLMClassifierFromSpec

  relevance_scorer = LLMClassifierFromSpec(
      "Relevance",
      choice_scores={"Relevant": 1, "Irrelevant": 0},
      model="gpt-5-mini",
      use_cot=True,
  )
  ```
</CodeGroup>

## Additional features

### Structured outputs

OpenAI's structured outputs are supported with the wrapper functions.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { z } from "zod";

  // Define a Zod schema for the response
  const ResponseSchema = z.object({
    name: z.string(),
    age: z.number(),
  });

  const completion = await client.beta.chat.completions.parse({
    model: "gpt-5-mini",
    messages: [
      { role: "system", content: "Extract the person's name and age." },
      { role: "user", content: "My name is John and I'm 30 years old." },
    ],
    response_format: {
      type: "json_schema",
      json_schema: {
        name: "person",
        // The Zod schema for the response
        schema: ResponseSchema,
      },
    },
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from pydantic import BaseModel


  class Person(BaseModel):
      name: str
      age: int


  completion = client.beta.chat.completions.parse(
      model="gpt-5-mini",
      messages=[
          {"role": "system", "content": "Extract the person's name and age."},
          {"role": "user", "content": "My name is John and I'm 30 years old."},
      ],
      response_format=Person,
  )
  ```
</CodeGroup>

### Function calling and tools

Braintrust supports OpenAI function calling for building AI agents with tools.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  const tools = [
    {
      type: "function" as const,
      function: {
        name: "get_weather",
        description: "Get current weather for a location",
        parameters: {
          type: "object",
          properties: {
            location: { type: "string" },
          },
          required: ["location"],
        },
      },
    },
  ];

  const response = await client.chat.completions.create({
    model: "gpt-5-mini",
    messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
    tools,
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description": "Get current weather for a location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string"},
                  },
                  "required": ["location"],
              },
          },
      }
  ]

  response = client.chat.completions.create(
      model="gpt-5-mini",
      messages=[{"role": "user", "content": "What's the weather in San Francisco?"}],
      tools=tools,
  )
  ```
</CodeGroup>

### Multimodal content, attachments, errors, and masking sensitive data

To learn more about these topics, check out the [customize traces](/guides/traces/customize) guide.

## Use OpenAI with Braintrust AI proxy

You can also access OpenAI models through the [Braintrust AI Proxy](/guides/proxy), which provides a unified interface for multiple providers.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",

    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const response = await client.chat.completions.create({
    model: "gpt-5-mini",
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
      model="gpt-5-mini",
      messages=[{"role": "user", "content": "What is a proxy?"}],
      seed=1,  # A seed activates the proxy's cache
  )
  ```

  ```go  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  package main

  import (
  	"context"
  	"log"
  	"os"

  	"github.com/openai/openai-go"
  	"github.com/openai/openai-go/option"
  )

  func main() {
  	ctx := context.Background()

  	client := openai.NewClient(
  		option.WithBaseURL("https://api.braintrust.dev/v1/proxy"),
  		option.WithAPIKey(os.Getenv("BRAINTRUST_API_KEY")),
  	)

  	response, err := client.Chat.Completions.New(ctx, openai.ChatCompletionNewParams{
  		Model: openai.ChatModelGPT4oMini,
  		Messages: []openai.ChatCompletionMessageParamUnion{
  			openai.UserMessage("What is a proxy?"),
  		},
  		Seed: openai.Int(1), // A seed activates the proxy's cache
  	})
  	if err != nil {
  		log.Fatal(err)
  	}
  	_ = response
  }
  ```

  ```ruby  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  require 'openai'

  client = OpenAI::Client.new(
    uri_base: 'https://api.braintrust.dev/v1/proxy',
    access_token: ENV.fetch('BRAINTRUST_API_KEY', nil)
  )

  client.chat.completions.create(
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: 'What is a proxy?' }],
    seed: 1 # A seed activates the proxy's cache
  )
  ```

  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import com.openai.client.OpenAIClient;
  import com.openai.client.okhttp.OpenAIOkHttpClient;
  import com.openai.models.ChatModel;
  import com.openai.models.chat.completions.ChatCompletionCreateParams;

  class OpenAIProxy {
      public static void main(String[] args) {
          OpenAIClient client = OpenAIOkHttpClient.builder()
              .apiKey(System.getenv("BRAINTRUST_API_KEY"))
              .baseUrl("https://api.braintrust.dev/v1/proxy")
              .build();

          var response = client.chat().completions().create(
              ChatCompletionCreateParams.builder()
                  .model(ChatModel.GPT_4O_MINI)
                  .addUserMessage("What is a proxy?")
                  .seed(1L) // A seed activates the proxy's cache
                  .build());
      }
  }
  ```

  ```csharp  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  using System;
  using System.Threading.Tasks;
  using OpenAI;
  using OpenAI.Chat;

  class OpenAIProxy
  {
      static async Task Main(string[] args)
      {
          var apiKey = Environment.GetEnvironmentVariable("BRAINTRUST_API_KEY");
          if (string.IsNullOrEmpty(apiKey))
          {
              Console.WriteLine("Error: BRAINTRUST_API_KEY environment variable is not set.");
              return;
          }

          var client = new OpenAIClient(
              new System.ClientModel.ApiKeyCredential(apiKey),
              new OpenAIClientOptions
              {
                  Endpoint = new Uri("https://api.braintrust.dev/v1/proxy")
              }
          );

          var chatClient = client.GetChatClient("gpt-4o-mini");
          var messages = new ChatMessage[]
          {
              new UserChatMessage("What is a proxy?")
          };

          var response = await chatClient.CompleteChatAsync(messages);
      }
  }
  ```
</CodeGroup>

## Cookbooks

* [Evaluating audio with the OpenAI Realtime API](/cookbook/recipes/Realtime)
* [Using Python functions to extract text from images](/cookbook/recipes/ToolOCR)
* [Using functions to build a RAG agent](/cookbook/recipes/ToolRAG)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt