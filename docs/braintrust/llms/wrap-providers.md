# Source: https://braintrust.dev/docs/instrument/wrap-providers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wrap AI providers

> Automatically log all LLM calls with native SDK wrappers

The simplest way to instrument your application is to wrap your [AI provider](/integrations#ai-providers) clients. Braintrust provides native wrappers for popular providers that automatically log all requests, responses, streaming data, token usage, and timing information.

## How it works

Wrapping a client takes just a few lines of code and captures everything automatically:

<CodeGroup dropdown>
  ```typescript {1,4-5} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initLogger, wrapOpenAI } from "braintrust";
  import OpenAI from "openai";

  const logger = initLogger({ projectName: "My Project" });
  const client = wrapOpenAI(new OpenAI());

  // All calls are automatically logged
  const response = await client.chat.completions.create({
    model: "gpt-4o",
    messages: [{ role: "user", content: "Hello!" }],
  });
  ```

  ```python {1,4-5} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init_logger, wrap_openai
  from openai import OpenAI

  logger = init_logger(project="My Project")
  client = wrap_openai(OpenAI())

  # All calls are automatically logged
  response = client.chat.completions.create(
      model="gpt-4o",
      messages=[{"role": "user", "content": "Hello!"}],
  )
  ```
</CodeGroup>

The wrapper automatically captures:

* Request inputs (messages, parameters)
* Model outputs (completions, tool calls)
* Metadata (model, temperature, token usage)
* Timing (start time, duration)
* Streaming chunks (if applicable)
* Errors and exceptions

## Supported providers

Braintrust provides native wrappers for major AI providers:

### OpenAI

Wrap the OpenAI client to log GPT models, embeddings, and other OpenAI APIs. See the [OpenAI integration guide](/integrations/ai-providers/openai) for complete documentation.

<Steps>
  <Step title="Install packages">
    <CodeGroup>
      ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
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
  </Step>

  <Step title="Set API keys">
    Set your API keys as environment variables:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    export BRAINTRUST_API_KEY=<your-braintrust-api-key>
    export OPENAI_API_KEY=<your-openai-api-key>
    ```

    Get your Braintrust API key from [Settings > API keys](https://www.braintrust.dev/app/settings?subroute=api-keys).
  </Step>

  <Step title="Wrap the client">
    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { initLogger, wrapOpenAI } from "braintrust";
      import OpenAI from "openai";

      const logger = initLogger({ projectName: "My Project" });
      const client = wrapOpenAI(
        new OpenAI({
          apiKey: process.env.OPENAI_API_KEY,
        }),
      );

      const response = await client.chat.completions.create({
        model: "gpt-4o",
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

      response = client.chat.completions.create(
          model="gpt-4o",
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
      	tp := trace.NewTracerProvider()
      	defer tp.Shutdown(context.Background())
      	otel.SetTracerProvider(tp)

      	_, err := braintrust.New(tp,
      		braintrust.WithProject("My Project"),
      		braintrust.WithAPIKey(os.Getenv("BRAINTRUST_API_KEY")),
      	)
      	if err != nil {
      		log.Fatal(err)
      	}

      	client := openai.NewClient(
      		option.WithMiddleware(traceopenai.NewMiddleware()),
      	)

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

      Braintrust.init(project: 'My Project')
      client = OpenAI::Client.new(api_key: ENV.fetch('OPENAI_API_KEY', nil))
      Braintrust::Trace::OpenAI.wrap(client)

      client.chat.completions.create(
        model: 'gpt-4o',
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

      class OpenAIExample {
          public static void main(String[] args) {
              var braintrust = Braintrust.get();
              var openTelemetry = braintrust.openTelemetryCreate();

              OpenAIClient client = BraintrustOpenAI.wrapOpenAI(
                  openTelemetry,
                  OpenAIOkHttpClient.fromEnv()
              );

              var result = client.chat().completions().create(
                  ChatCompletionCreateParams.builder()
                      .model(ChatModel.GPT_4O)
                      .addSystemMessage("You are a helpful assistant.")
                      .addUserMessage("What is machine learning?")
                      .build()
              );
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

      class OpenAIExample
      {
          static async Task Main(string[] args)
          {
              var braintrust = Braintrust.Sdk.Braintrust.Get();
              var activitySource = braintrust.GetActivitySource();

              var client = BraintrustOpenAI.WrapOpenAI(
                  activitySource,
                  Environment.GetEnvironmentVariable("OPENAI_API_KEY")
              );

              var chatClient = client.GetChatClient("gpt-4o");
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
  </Step>
</Steps>

### Anthropic

Wrap the Anthropic client to log Claude models. See the [Anthropic integration guide](/integrations/ai-providers/anthropic) for complete documentation.

<Steps>
  <Step title="Install packages">
    <CodeGroup>
      ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # pnpm
      pnpm add braintrust @anthropic-ai/sdk
      # npm
      npm install braintrust @anthropic-ai/sdk
      ```

      ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pip install braintrust anthropic
      ```
    </CodeGroup>
  </Step>

  <Step title="Set API keys">
    Set your API keys as environment variables:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    export BRAINTRUST_API_KEY=<your-braintrust-api-key>
    export ANTHROPIC_API_KEY=<your-anthropic-api-key>
    ```

    Get your Braintrust API key from [Settings > API keys](https://www.braintrust.dev/app/settings?subroute=api-keys).
  </Step>

  <Step title="Wrap the client">
    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { initLogger, wrapAnthropic } from "braintrust";
      import Anthropic from "@anthropic-ai/sdk";

      const logger = initLogger({ projectName: "My Project" });
      const client = wrapAnthropic(
        new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY }),
      );

      const response = await client.messages.create({
        model: "claude-sonnet-4-5-20250929",
        max_tokens: 1024,
        messages: [{ role: "user", content: "What is machine learning?" }],
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import os
      from braintrust import init_logger, wrap_anthropic
      import anthropic

      logger = init_logger(project="My Project")
      client = wrap_anthropic(
          anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
      )

      response = client.messages.create(
          model="claude-sonnet-4-5-20250929",
          max_tokens=1024,
          messages=[{"role": "user", "content": "What is machine learning?"}],
      )
      ```
    </CodeGroup>
  </Step>
</Steps>

### Google Gemini

Wrap the Google GenAI client to log Gemini models. See the [Gemini integration guide](/integrations/ai-providers/gemini) for complete documentation.

<Steps>
  <Step title="Install packages">
    <CodeGroup>
      ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # pnpm
      pnpm add braintrust @google/genai
      # npm
      npm install braintrust @google/genai
      ```

      ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pip install braintrust google-genai
      ```

      ```bash Java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # add to build.gradle dependencies{} block
      implementation 'dev.braintrust:braintrust-sdk-java:<version-goes-here>'
      implementation 'com.google.genai:google-genai:1.20.0'
      ```
    </CodeGroup>
  </Step>

  <Step title="Set API keys">
    Set your API keys as environment variables:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    export BRAINTRUST_API_KEY=<your-braintrust-api-key>
    export GEMINI_API_KEY=<your-gemini-api-key>
    ```

    Get your Braintrust API key from [Settings > API keys](https://www.braintrust.dev/app/settings?subroute=api-keys).
  </Step>

  <Step title="Wrap the client">
    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import * as googleGenAI from "@google/genai";
      import { wrapGoogleGenAI, initLogger } from "braintrust";

      initLogger({ projectName: "My Project" });

      const { GoogleGenAI } = wrapGoogleGenAI(googleGenAI);
      const client = new GoogleGenAI({
        apiKey: process.env.GEMINI_API_KEY || "",
      });

      const response = await client.models.generateContent({
        model: "gemini-2.5-flash",
        contents: "What is machine learning?",
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      from braintrust.wrappers.google_genai import setup_genai
      from google.genai import types
      from google.genai.client import Client

      setup_genai(project_name="My Project")
      client = Client(api_key=os.environ["GEMINI_API_KEY"])

      response = client.models.generate_content(
          model="gemini-2.5-flash",
          contents="What is machine learning?",
      )
      ```

      ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import com.google.genai.Client;
      import com.google.genai.types.GenerateContentConfig;
      import dev.braintrust.Braintrust;
      import dev.braintrust.instrumentation.genai.BraintrustGenAI;
      import io.opentelemetry.api.OpenTelemetry;

      class GeminiExample {
          public static void main(String[] args) {
              Braintrust braintrust = Braintrust.get();
              OpenTelemetry openTelemetry = braintrust.openTelemetryCreate();

              Client client = BraintrustGenAI.wrap(openTelemetry, new Client.Builder());

              var config = GenerateContentConfig.builder().build();
              var response = client.models.generateContent(
                  "gemini-2.5-flash",
                  "What is machine learning?",
                  config
              );

              System.out.println(response.text());
          }
      }
      ```
    </CodeGroup>
  </Step>
</Steps>

## Other providers

Braintrust provides wrappers for many additional AI providers:

<CardGroup cols={2}>
  <Card title="AWS Bedrock" href="/integrations/ai-providers/bedrock" icon="aws">
    Claude, Llama, and other models on AWS
  </Card>

  <Card title="Azure OpenAI" href="/integrations/ai-providers/azure" icon="microsoft">
    OpenAI models hosted on Azure
  </Card>

  <Card title="Google Vertex AI" href="/integrations/ai-providers/google" icon="google">
    Gemini and other models on Google Cloud
  </Card>

  <Card title="Mistral" href="/integrations/ai-providers/mistral" icon="sparkles">
    Mistral and Mixtral models
  </Card>

  <Card title="Together AI" href="/integrations/ai-providers/together" icon="circle-nodes">
    Open-source models at scale
  </Card>

  <Card title="Groq" href="/integrations/ai-providers/groq" icon="bolt">
    Ultra-fast LLM inference
  </Card>
</CardGroup>

See the [integrations overview](/integrations) for all supported providers.

## Streaming support

Wrappers automatically handle streaming responses. No special configuration needed - just enable streaming in your API call and the wrapper collects all chunks and logs the complete request once streaming finishes.

<CodeGroup dropdown>
  ```typescript {10} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initLogger, wrapOpenAI } from "braintrust";
  import OpenAI from "openai";

  const logger = initLogger({ projectName: "My Project" });
  const client = wrapOpenAI(new OpenAI());

  const stream = await client.chat.completions.create({
    model: "gpt-4o",
    messages: [{ role: "user", content: "Count to 10" }],
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || "");
  }
  // Streaming data is automatically logged when complete
  ```

  ```python {10} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init_logger, wrap_openai
  from openai import OpenAI

  logger = init_logger(project="My Project")
  client = wrap_openai(OpenAI())

  stream = client.chat.completions.create(
      model="gpt-4o",
      messages=[{"role": "user", "content": "Count to 10"}],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="")
  # Streaming data is automatically logged when complete
  ```
</CodeGroup>

### Stream from prompts

When executing prompts through the Braintrust API, you can stream results using Server-Sent Events (SSE). This works for both direct API calls and playground execution.

Braintrust uses a simplified SSE format optimized for common LLM use cases:

* **Text streaming**: For chat message content
* **JSON streaming**: For structured tool call arguments
* **Progress events**: For intermediate function execution steps

See the [prompts documentation](/deploy/prompts#streaming) for detailed streaming examples and the [SSE format reference](/reference/streaming) for the complete specification.

## Next steps

* [Integrate with frameworks](/instrument/frameworks) like LangChain or OpenTelemetry
* [Add custom tracing](/instrument/custom-tracing) for non-LLM application logic
* [View your logs](/observe/view-logs) in the Braintrust dashboard
