# Source: https://braintrust.dev/docs/observability.md

# Observability quickstart

> Get started logging traces to Braintrust

This quickstart shows you how to automatically [log your application's LLM calls](/core/logs/write) to Braintrust using native SDK wrappers for common AI providers. Wrappers are available for [TypeScript](/reference/sdks/typescript), [Python](/reference/sdks/python), and [other languages](/reference/sdks).

Specifically, these guides show how to wrap [OpenAI](/integrations/ai-providers/openai), [Anthropic](/integrations/ai-providers/anthropic), and [Gemini](/integrations/ai-providers/gemini) calls and send those log traces to Braintrust. We also provide native SDK wrappers for a range of other providers through our AI proxy.

<Tabs>
  <Tab title="OpenAI">
    OpenAI provides access to GPT models including GPT-5 and other cutting-edge language models. Braintrust integrates seamlessly with OpenAI through direct API access, wrapper functions for automatic tracing, and proxy support.

    ### 1. Configure your API keys

    You need both Braintrust and OpenAI API keys to set up logging OpenAI LLM calls.

    * To create a new OpenAI API key, visit [OpenAI's API platform](https://platform.openai.com/api-keys)
    * To create a Braintrust API key, navigate to [**Settings > API keys**](https://www.braintrust.dev/app/settings?subroute=api-keys) and select **Create new API key**

    <CodeGroup>
      ```bash .env theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      OPENAI_API_KEY=<your-openai-api-key>
      BRAINTRUST_API_KEY=<your-braintrust-api-key>
      ```
    </CodeGroup>

    <Note>
      API keys are encrypted using 256-bit AES-GCM encryption and are not stored or logged by Braintrust.
    </Note>

    ### 2. Install Braintrust and OpenAI libraries

    Install the Braintrust and OpenAI libraries for your programming language.

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

    ### 3. Send logs to Braintrust

    Braintrust provides automatic tracing for OpenAI API calls, handling streaming, metrics collection, and other details.

    * **TypeScript & Python**: Use `wrapOpenAI` / `wrap_openai` wrapper functions
    * **Go**: Use the tracing middleware with the OpenAI client
    * **Ruby**: Use `Braintrust::Trace::OpenAI.wrap` to wrap the OpenAI client
    * **Java**: Use the tracing interceptor with the OpenAI client
    * **C#**: Use `BraintrustOpenAI.WrapOpenAI()` to wrap the OpenAI client

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
        model: "gpt-5",
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

    ### 4. View your logs

    Select <Icon icon="activity" /> **Logs** in the Braintrust dashboard to view your log traces.
  </Tab>

  <Tab title="Anthropic">
    Anthropic provides access to Claude models including Claude 4 Sonnet, Claude 4.1 Opus, and other cutting-edge language models. Braintrust integrates seamlessly with Anthropic through direct API access, wrapper functions for automatic tracing, and proxy support.

    ### 1. Configure your API keys

    You need both Braintrust and Anthropic API keys to set up logging Anthropic LLM calls.

    * To create a new Anthropic API key, visit [Anthropic's API platform](https://console.anthropic.com/settings/keys)
    * To create a Braintrust API key, navigate to [**Settings > API keys**](https://www.braintrust.dev/app/settings?subroute=api-keys) and select **Create new API key**

    <CodeGroup>
      ```bash .env theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      ANTHROPIC_API_KEY=<your-anthropic-api-key>
      BRAINTRUST_API_KEY=<your-braintrust-api-key>
      ```
    </CodeGroup>

    <Note>
      API keys are encrypted using 256-bit AES-GCM encryption and are not stored or logged by Braintrust.
    </Note>

    ### 2. Install Braintrust and Anthropic libraries

    Install the Braintrust and Anthropic libraries for your programming language.

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      npm install braintrust @anthropic-ai/sdk
      ```

      ```bash pnpm theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pnpm add braintrust @anthropic-ai/sdk
      ```

      ```bash pip theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pip install braintrust @anthropic-ai/sdk
      ```

      ```bash Go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      go get github.com/braintrustdata/braintrust-sdk-go
      go get github.com/anthropics/anthropic-sdk-go
      ```

      ```bash gem theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      gem install braintrust anthropic-sdk-ruby
      ```

      ```bash gradle theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      // add to build.gradle dependencies{} block
      implementation 'dev.braintrust:braintrust-sdk-java:<version-goes-here>'
      implementation 'com.anthropic:anthropic-sdk-java:<version-goes-here>'
      ```
    </CodeGroup>

    ### 3. Send logs to Braintrust

    Braintrust provides automatic tracing for Anthropic API calls. Braintrust handles streaming, metric collection (including cached tokens), and other details.

    * **TypeScript & Python**: Use `wrapAnthropic` / `wrap_anthropic` wrapper functions
    * **Go**: Use the tracing middleware with the Anthropic client
    * **Ruby**: Use `Braintrust::Trace::Anthropic.wrap` to wrap the Anthropic client
    * **Java**: Use the tracing interceptor with the Anthropic client

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

    ### 4. View your logs

    Select <Icon icon="activity" /> **Logs** in the Braintrust dashboard to view your log traces.
  </Tab>

  <Tab title="Gemini">
    Google's Gemini models include Gemini 2.0 Flash, Gemini 2.5 Pro, and other advanced multimodal language models. Braintrust integrates seamlessly with Gemini through direct API access, wrapper functions for automatic tracing, and proxy support.

    ### 1. Configure your API keys

    You need both Braintrust and Gemini API keys to set up logging Gemini LLM calls.

    * To create a new Gemini API key, visit [Google AI Studio](https://aistudio.google.com/app/apikey)
    * To create a Braintrust API key, navigate to [**Settings > API keys**](https://www.braintrust.dev/app/settings?subroute=api-keys) and select **Create new API key**

    <CodeGroup>
      ```bash .env theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      GEMINI_API_KEY=<your-gemini-api-key>
      BRAINTRUST_API_KEY=<your-braintrust-api-key>
      ```
    </CodeGroup>

    <Note>
      API keys are encrypted using 256-bit AES-GCM encryption and are not stored or logged by Braintrust.
    </Note>

    ### 2. Install Braintrust and OpenAI libraries

    Install the Braintrust and OpenAI libraries for your programming language.

    <CodeGroup>
      ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # pnpm
      pnpm add braintrust @google/genai
      # npm
      npm install braintrust @google/genai
      ```

      ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pip install braintrust google-genai
      ```
    </CodeGroup>

    ### 3. Send logs to Braintrust

    Braintrust provides wrapper functions that automatically log Google GenAI API calls. All subsequent API calls will be automatically traced.

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import * as googleGenAI from "@google/genai";
      import { wrapGoogleGenAI, initLogger } from "braintrust";

      // Initialize Braintrust tracing
      initLogger({ projectName: "My Project" });

      // Use wrapGoogleGenAI to wrap the Google GenAI module for automatic tracing
      const { GoogleGenAI } = wrapGoogleGenAI(googleGenAI);

      // Create a native Google GenAI client
      const client = new GoogleGenAI({
        apiKey: process.env.GEMINI_API_KEY || "",
      });

      // All API calls are automatically logged
      const response = await client.models.generateContent({
        model: "gemini-2.5-flash",
        contents: "What is machine learning?",
        config: {
          maxOutputTokens: 100,
        },
      });
      console.log(response.text);
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import os

      from braintrust.wrappers.google_genai import setup_genai
      from google.genai import types
      from google.genai.client import Client

      # Use setup_genai to automatically trace all Google GenAI API calls
      setup_genai(project_name="My Project")

      # Create a native Google GenAI client
      client = Client(api_key=os.environ["GEMINI_API_KEY"])

      # All API calls are automatically logged
      response = client.models.generate_content(
          model="gemini-2.5-flash",
          contents="What is machine learning?",
          config=types.GenerateContentConfig(
              max_output_tokens=100,
          ),
      )
      print(response.text)
      ```
    </CodeGroup>

    ### 4. View your logs

    Select <Icon icon="activity" /> **Logs** in the Braintrust dashboard to view your log traces.
  </Tab>

  <Tab title="Other AI providers">
    ## Proxy AI providers

    Braintrust comes with several pre-configured providers that you can use to interact with different AI language models. These guides show how to wrap these providers to send logs, create evals, and connect using the Braintrust AI proxy.

    <CardGroup cols={3}>
      <Card title="OpenAI" href="/integrations/ai-providers/openai" arrow icon="https://img.logo.dev/openai.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Anthropic" href="/integrations/ai-providers/anthropic" arrow icon="https://img.logo.dev/anthropic.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Gemini" href="/integrations/ai-providers/gemini" arrow icon="https://img.logo.dev/google.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Mistral" href="/integrations/ai-providers/mistral" arrow icon="https://img.logo.dev/mistral.ai?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Together" href="/integrations/ai-providers/together" arrow icon="https://img.logo.dev/together.ai?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Fireworks" href="/integrations/ai-providers/fireworks" arrow icon="https://img.logo.dev/fireworks.ai?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Perplexity" href="/integrations/ai-providers/perplexity" arrow icon="https://img.logo.dev/perplexity.ai?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="xAI" href="/integrations/ai-providers/xai" arrow icon="https://img.logo.dev/x.ai?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Groq" href="/integrations/ai-providers/groq" arrow icon="https://img.logo.dev/groq.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Lepton" href="/integrations/ai-providers/lepton" arrow icon="https://img.logo.dev/lepton.ai?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Cerebras" href="/integrations/ai-providers/cerebras" arrow icon="https://img.logo.dev/cerebras.ai?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Replicate" href="/integrations/ai-providers/replicate" arrow icon="https://img.logo.dev/replicate.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Baseten" href="/integrations/ai-providers/baseten" arrow icon="https://img.logo.dev/baseten.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />
    </CardGroup>

    ## Proxy cloud providers

    Braintrust also supports several cloud providers by default. These guides show how to configure access these models from Braintrust.

    <CardGroup cols={3}>
      <Card title="AWS Bedrock" href="/integrations/ai-providers/bedrock" arrow icon="https://img.logo.dev/aws.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Vertex AI" href="/integrations/ai-providers/google" arrow icon="https://img.logo.dev/google.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Azure" href="/integrations/ai-providers/azure" arrow icon="https://img.logo.dev/azure.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />

      <Card title="Databricks" href="/integrations/ai-providers/databricks" arrow icon="https://img.logo.dev/databricks.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" />
    </CardGroup>

    ## Custom AI providers

    Braintrust supports a wide range of model providers out of the box via the [Braintrust AI Proxy](/guides/proxy). This allows you to add custom providers to work with any AI service. Braintrust provides the logging, evaluation, and observability tools you need regardless of which models you choose.

    <CardGroup cols={3}>
      <Card title="Custom" href="/integrations/ai-providers/custom" arrow icon="box" />
    </CardGroup>
  </Tab>

  <Tab title="SDK integrations">
    ## SDK integrations

    Trace your apps using existing frameworks to quickly add observability. These guides show how to configure logging via code samples.

    <Columns cols={2}>
      <Card horizontal href="/integrations/sdk-integrations/opentelemetry" title="OpenTelemetry" icon="https://img.logo.dev/opentelemetry.io?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/vercel" title="Vercel" icon="https://img.logo.dev/vercel.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/openai-agents-sdk" title="Agents SDK" icon="https://img.logo.dev/openai.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/claude-agent-sdk" title="Claude Agent SDK" icon="https://img.logo.dev/claude.ai?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/instructor" title="Instructor" icon="circle-dashed" arrow />

      <Card horizontal href="/integrations/sdk-integrations/langchain" title="LangChain" icon="https://img.logo.dev/langchain.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/langgraph" title="LangGraph" icon="https://img.logo.dev/langgraph.langchain.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/google" title="Google ADK" icon="https://img.logo.dev/google.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/mastra" title="Mastra" icon="https://img.logo.dev/mastra.ai?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/pydantic-ai" title="Pydantic AI" icon="https://img.logo.dev/pydantic.ai?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/dspy" title="DSPy" icon="https://img.logo.dev/dspy.ai?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/litellm" title="LiteLLM" icon="https://img.logo.dev/litellm.ai?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/autogen" title="Autogen" icon="https://img.logo.dev/autogenai.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/crew-ai" title="CrewAI" icon="https://img.logo.dev/crewai.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/strands-agent" title="Strands Agent SDK" icon="https://img.logo.dev/strandsagents.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/cloudflare" title="Cloudflare" icon="https://img.logo.dev/cloudflare.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/agno" title="Agno" icon="https://img.logo.dev/agno.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/livekit-agents" title="LiveKit Agents" icon="https://img.logo.dev/livekit.io?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/traceloop" title="Traceloop" icon="https://img.logo.dev/traceloop.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/llamaindex" title="LlamaIndex" icon="https://img.logo.dev/llamaindex.ai?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />

      <Card horizontal href="/integrations/sdk-integrations/apollo-graphql" title="Apollo GraphQL" icon="https://img.logo.dev/apollographql.com?token=pk_BdcHD9e5SCW3j1rnJkNyMQ" arrow />
    </Columns>
  </Tab>
</Tabs>

## Next steps

* [View, filter, and query](/core/logs/view) your logs
* [Create a custom dashboard](/core/monitor) to visualize log metrics
* [Create a dataset](/core/datasets) from a subset of your logs and use it to [write and run an eval](/core/experiments)
* Learn more about [what's in a log trace](/guides/traces)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt