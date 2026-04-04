# Source: https://braintrust.dev/docs/observability.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tracing quickstart

> Log your first trace

export const feature_0 = "Auto-instrumentation"

[Tracing](/instrument) captures the details of each step of an AI application's execution. This lets you debug issues, understand model behavior, and optimize performance in production.

<Tabs>
  <Tab title="Wrap manually" icon="terminal">
    Wrap your AI client with Braintrust to trace all LLM requests. Maximum flexibility and control. Works with any [integration](/integrations).

    ## 1. Sign up

    If you're new to Braintrust, sign up free at [braintrust.dev](https://www.braintrust.dev).

    ## 2. Get API keys

    Create API keys for:

    * [Braintrust](https://www.braintrust.dev/app/settings?subroute=api-keys)
    * Your AI provider or framework ([OpenAI](https://platform.openai.com/api-keys), [Anthropic](https://console.anthropic.com/settings/keys), [Gemini](https://aistudio.google.com/app/apikey), [etc.](/integrations))

    Set them as environment variables:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    export BRAINTRUST_API_KEY="<your-braintrust-api-key>"
    export OPENAI_API_KEY="<your-openai-api-key>" # or ANTHROPIC_API_KEY, GEMINI_API_KEY, etc.
    ```

    <Tip>
      This quickstart uses OpenAI. For other providers, see [Integrations](/integrations).
    </Tip>

    ## 3. Install SDKs

    Install the Braintrust SDK and AI provider SDK for your programming language:

    <CodeGroup>
      ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # pnpm
      pnpm add braintrust openai ts-node
      # npm
      npm install braintrust openai ts-node
      ```

      ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pip install braintrust openai
      ```

      ```bash Go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      go get github.com/braintrustdata/braintrust-sdk-go
      go get github.com/openai/openai-go
      ```

      ```bash Ruby theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # Add to your Gemfile
      gem "braintrust"
      gem "ruby-openai"

      # Install:
      bundle install
      ```

      ```bash Java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # Add to build.gradle dependencies{} block
      implementation 'dev.braintrust:braintrust-sdk-java:<version-goes-here>'
      implementation 'com.openai:openai-java-sdk:<version-goes-here>'
      ```

      ```bash C# theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # Add to .csproj file
      dotnet add package Braintrust.Sdk
      dotnet add package OpenAI
      ```
    </CodeGroup>

    ## 4. Trace LLM calls

    Make a simple LLM request and see it automatically traced in Braintrust. Initialize Braintrust and wrap your OpenAI client:

    * **TypeScript & Python**: Use `wrapOpenAI` / `wrap_openai` wrapper functions
    * **Go**: Use the tracing middleware with the OpenAI client
    * **Ruby**: Use `Braintrust::Trace::OpenAI.wrap` to wrap the OpenAI client
    * **Java**: Use the tracing interceptor with the OpenAI client
    * **C#**: Use `BraintrustOpenAI.WrapOpenAI()` to wrap the OpenAI client

    <CodeGroup dropdown>
      ```typescript quickstart.ts {1,5,6} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { initLogger, wrapOpenAI } from "braintrust";
      import OpenAI from "openai";

      // Initialize Braintrust logger
      const logger = initLogger({ projectName: "Tracing quickstart" });
      const client = wrapOpenAI(new OpenAI());

      // All API calls are automatically logged
      const result = await client.responses.create({
        model: "gpt-5-mini",
        input: [
          { role: "system", content: "You are a helpful assistant." },
          { role: "user", content: "What is machine learning?" },
        ],
      });

      console.log(result.output_text);
      ```

      ```python quickstart.py {1,5,6} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      from braintrust import init_logger, wrap_openai
      from openai import OpenAI

      # Initialize Braintrust logger
      logger = init_logger(project="Tracing quickstart")
      client = wrap_openai(OpenAI())

      # All API calls are automatically logged
      result = client.responses.create(
          model="gpt-5-mini",
          input=[
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "user", "content": "What is machine learning?"},
          ],
      )

      print(result.output_text)
      ```

      ```go main.go {13-14,24-27,33-35} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
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
      		braintrust.WithProject("Tracing quickstart"),
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
      		Model: openai.ChatModelGPT5Mini,
      	})
      	if err != nil {
      		log.Fatal(err)
      	}
      	_ = result
      }
      ```

      ```ruby quickstart.rb {1,5,8,11} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      require 'braintrust'
      require 'openai'

      # Initialize Braintrust
      Braintrust.init(project: 'Tracing quickstart')

      # Create OpenAI client
      client = OpenAI::Client.new(api_key: ENV.fetch('OPENAI_API_KEY', nil))

      # Wrap the client with Braintrust tracing
      Braintrust::Trace::OpenAI.wrap(client)

      # All API calls are automatically logged
      client.chat.completions.create(
        model: 'gpt-5-mini',
        messages: [
          { role: 'system', content: 'You are a helpful assistant.' },
          { role: 'user', content: 'What is machine learning?' }
        ]
      )
      ```

      ```java Quickstart.java {5-6,10-11,14} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import com.openai.client.OpenAIClient;
      import com.openai.client.okhttp.OpenAIOkHttpClient;
      import com.openai.models.ChatModel;
      import com.openai.models.chat.completions.ChatCompletionCreateParams;
      import dev.braintrust.Braintrust;
      import dev.braintrust.instrumentation.openai.BraintrustOpenAI;

      class Quickstart {
          public static void main(String[] args) {
              var braintrust = Braintrust.get();
              var openTelemetry = braintrust.openTelemetryCreate();

              // Wrap the OpenAI client with Braintrust instrumentation
              OpenAIClient client = BraintrustOpenAI.wrapOpenAI(openTelemetry, OpenAIOkHttpClient.fromEnv());

              // All API calls are automatically logged
              var request = ChatCompletionCreateParams.builder()
                  .model(ChatModel.GPT_5_MINI)
                  .addSystemMessage("You are a helpful assistant.")
                  .addUserMessage("What is machine learning?")
                  .build();

              var result = client.chat().completions().create(request);
          }
      }
      ```

      ```csharp Quickstart.cs {3-4,12-13,15,18-19} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      using System;
      using System.Threading.Tasks;
      using Braintrust.Sdk;
      using Braintrust.Sdk.Instrumentation.OpenAI;
      using OpenAI;
      using OpenAI.Chat;

      class Quickstart
      {
          static async Task Main(string[] args)
          {
              var braintrust = Braintrust.Sdk.Braintrust.Get();
              var activitySource = braintrust.GetActivitySource();

              var apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY");

              // Wrap the OpenAI client with Braintrust instrumentation
              var client = BraintrustOpenAI.WrapOpenAI(activitySource, apiKey);
              var chatClient = client.GetChatClient("gpt-5-mini");

              // All API calls are automatically logged
              var messages = new ChatMessage[]
              {
                  new SystemChatMessage("You are a helpful assistant."),
                  new UserChatMessage("What is machine learning?")
              };

              var response = await chatClient.CompleteChatAsync(messages);
              Console.WriteLine(response.Value.Content[0].Text);
          }
      }
      ```
    </CodeGroup>

    Run this code:

    <CodeGroup>
      ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      npx ts-node quickstart.ts
      ```

      ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      python quickstart.py
      ```

      ```bash Go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      go run main.go
      ```

      ```bash Ruby theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      ruby quickstart.rb
      ```

      ```bash Java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # Compile
      javac -cp "path/to/dependencies/*" Quickstart.java
      # Run
      java -cp ".:path/to/dependencies/*" Quickstart
      ```

      ```bash C# theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      dotnet run
      ```
    </CodeGroup>

    All API calls are automatically logged to Braintrust.

    ## 5. View traces

    In the Braintrust UI, go to the "Tracing quickstart" project and select <Icon icon="activity" /> **Logs**. You'll see a trace for each request.

    Click into any trace to see:

    * Complete input prompt and model output
    * Token counts, latency, and cost
    * Model configuration (temperature, max tokens, etc.)
    * Request and response metadata

    **This is the value of observability** - you can see every request, identify issues, and understand how your application behaves in production.

    ## Troubleshoot

    <AccordionGroup>
      <Accordion title="Not seeing traces in the UI?">
        **Check your API key:**

        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
        echo $BRAINTRUST_API_KEY
        ```

        Make sure it's set and starts with `sk-`.

        **Verify the project name:**
        The project is created automatically when you call `initLogger({ projectName: "Tracing quickstart" })`. Check that you're looking at the correct project in the UI.

        **Look for errors:**
        Check your console output for any error messages from Braintrust. Common issues:

        * Invalid API key
        * Network connectivity issues
        * Firewall blocking requests to `api.braintrust.dev`

        **Enable debug logging:**

        <CodeGroup dropdown>
          ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          const logger = initLogger({
            projectName: "Tracing quickstart",
            logLevel: "debug"
          });
          ```

          ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
          logger = init_logger(project="Tracing quickstart", log_level="debug")
          ```
        </CodeGroup>
      </Accordion>

      <Accordion title="Traces look incomplete or missing data?">
        **Check wrapper coverage:**
        Make sure you're wrapping the client **before** making API calls. Calls made with an unwrapped client won't be traced.

        **Verify async/await:**
        If using async functions, ensure you're awaiting API calls properly. Unawaited promises may not be fully traced.

        **Check for errors:**
        If your LLM call throws an error, the trace may be incomplete. Check logs for error messages.
      </Accordion>

      <Accordion title="High latency when logging?">
        **Logging is async:**
        Braintrust logs data asynchronously to avoid blocking your application. Traces should appear in the UI within seconds.

        **Check network:**
        If you're experiencing delays, verify network connectivity to `api.braintrust.dev`.
      </Accordion>

      <Accordion title="Need help?">
        * Join our [Discord](https://discord.gg/6G8s47F44X)
        * Email us at [support@braintrust.dev](mailto:support@braintrust.dev)
        * Use the [Loop](/observe/loop) feature in the Braintrust UI
      </Accordion>
    </AccordionGroup>
  </Tab>

  <Tab title="Auto-instrument" icon="zap">
    Automatically trace all LLM requests with minimal setup. Available for:

    | Language                      | Providers                                                                                   |
    | ----------------------------- | ------------------------------------------------------------------------------------------- |
    | <Icon icon="python" /> Python | OpenAI, Anthropic, LiteLLM, Pydantic AI, Agno, Claude Agent SDK, DSPy                       |
    | <Icon icon="gem" /> Ruby      | OpenAI, Anthropic, and 13+ providers via [RubyLLM](/integrations/sdk-integrations/ruby-llm) |
    | <Icon icon="golang" /> Go     | OpenAI, Anthropic, Gemini                                                                   |

    <Warning>
      {feature_0} is a beta feature.
    </Warning>

    ## 1. Sign up

    If you're new to Braintrust, sign up free at [braintrust.dev](https://www.braintrust.dev).

    ## 2. Get API keys

    Create API keys for:

    * [Braintrust](https://www.braintrust.dev/app/settings?subroute=api-keys)
    * Your AI provider or framework ([OpenAI](https://platform.openai.com/api-keys), [Anthropic](https://console.anthropic.com/settings/keys), [Gemini](https://aistudio.google.com/app/apikey), [etc.](/integrations))

    Set them as environment variables:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    export BRAINTRUST_API_KEY="<your-braintrust-api-key>"
    export OPENAI_API_KEY="<your-openai-api-key>" # or ANTHROPIC_API_KEY, GEMINI_API_KEY, etc.
    ```

    <Tip>
      This quickstart uses OpenAI. For other providers, see [Integrations](/integrations).
    </Tip>

    ## 3. Install SDKs

    <CodeGroup>
      ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pip install braintrust openai
      ```

      ```bash Ruby theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # Add to your Gemfile
      gem "braintrust", require: "braintrust/setup"
      gem "ruby-openai"

      # Install
      bundle install
      ```

      ```bash Go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      // Initialize Go module (if not already done)
      go mod init classifier

      // Install Orchestrion (compile-time instrumentation tool)
      go install github.com/DataDog/orchestrion@latest

      // Install SDKs
      go get github.com/braintrustdata/braintrust-sdk-go
      go get github.com/openai/openai-go

      // Create orchestrion.tool.go in your project root
      cat > orchestrion.tool.go << 'EOF'
      //go:build tools

      package main

      import (
      	_ "github.com/DataDog/orchestrion"
      	_ "github.com/braintrustdata/braintrust-sdk-go/trace/contrib/all"
      )
      EOF
      ```
    </CodeGroup>

    For additional auto-instrumentation methods:

    * [Python SDK documentation](/reference/sdks/python)
    * [Ruby SDK documentation](https://github.com/braintrustdata/braintrust-sdk-ruby)
    * [Go SDK documentation](https://github.com/braintrustdata/braintrust-sdk-go)

    ## 4. Auto-instrument

    Set the default project for auto-instrumentation:

    ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    export BRAINTRUST_DEFAULT_PROJECT="Tracing quickstart"
    ```

    Create a simple AI application that answers questions.

    * **Python**: Call `braintrust.auto_instrument()` once at the start of your application to enable automatic tracing.
    * **Ruby**: With the Gemfile configuration from step 3, all LLM calls are automatically instrumented when your application loads.
    * **Go**: Using Orchestrion, all LLM calls are automatically instrumented at compile time.

    <CodeGroup dropdown>
      ```python quickstart.py theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import os
      import braintrust
      from openai import OpenAI

      # Enable automatic instrumentation - call this once at startup
      braintrust.auto_instrument()

      # Create OpenAI client - no wrapping needed!
      client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

      # All LLM calls are automatically traced
      response = client.chat.completions.create(
          model="gpt-5-mini",
          messages=[
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "user", "content": "What is machine learning?"}
          ]
      )

      print(response.choices[0].message.content)
      ```

      ```ruby quickstart.rb theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      require 'bundler/setup'
      Bundler.require

      # Create OpenAI client - no wrapping needed!
      client = OpenAI::Client.new(access_token: ENV['OPENAI_API_KEY'])

      # All LLM calls are automatically traced
      response = client.chat.completions.create(
        model: 'gpt-5-mini',
        messages: [
          { role: 'system', content: 'You are a helpful assistant.' },
          { role: 'user', content: 'What is machine learning?' }
        ]
      )

      puts response.dig('choices', 0, 'message', 'content')
      ```

      ```go main.go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      package main

      import (
      	"context"
      	"fmt"
      	"log"
      	"os"

      	"github.com/braintrustdata/braintrust-sdk-go"
      	"github.com/openai/openai-go"
      	"go.opentelemetry.io/otel"
      	sdktrace "go.opentelemetry.io/otel/sdk/trace"
      )

      func main() {
      	// Set up OpenTelemetry TracerProvider
      	tp := sdktrace.NewTracerProvider()
      	defer tp.Shutdown(context.Background())
      	otel.SetTracerProvider(tp)

      	// Initialize Braintrust client
      	_, err := braintrust.New(tp,
      		braintrust.WithProject(os.Getenv("BRAINTRUST_DEFAULT_PROJECT")),
      		braintrust.WithAPIKey(os.Getenv("BRAINTRUST_API_KEY")),
      	)
      	if err != nil {
      		log.Fatal(err)
      	}

      	client := openai.NewClient()

      	// All LLM calls are automatically traced
      	response, err := client.Chat.Completions.New(context.Background(), openai.ChatCompletionNewParams{
      		Model: openai.ChatModelGPT5Mini,
      		Messages: []openai.ChatCompletionMessageParamUnion{
      			openai.SystemMessage("You are a helpful assistant."),
      			openai.UserMessage("What is machine learning?"),
      		},
      	})
      	if err != nil {
      		log.Fatal(err)
      	}

      	fmt.Println(response.Choices[0].Message.Content)
      }
      ```
    </CodeGroup>

    Run this code:

    <CodeGroup>
      ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      python quickstart.py
      ```

      ```bash Ruby theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      ruby quickstart.rb
      ```

      ```bash Go theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # Build with Orchestrion to enable auto-instrumentation
      orchestrion go build -o classifier

      # Run the instrumented binary
      ./classifier
      ```
    </CodeGroup>

    All LLM calls are automatically logged to Braintrust - no manual wrapping required!

    ## 5. View traces

    In the Braintrust UI, go to the "Tracing quickstart" project and select <Icon icon="activity" /> **Logs**. You'll see a trace for each request.

    Click into any trace to see:

    * Complete input prompt and model output
    * Token counts, latency, and cost
    * Model configuration (temperature, max tokens, etc.)
    * Request and response metadata

    **This is the value of observability** - you can see every request, identify issues, and understand how your application behaves in production.

    ## Troubleshoot

    <AccordionGroup>
      <Accordion title="Not seeing traces in the dashboard?">
        **Check your API key:**

        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
        echo $BRAINTRUST_API_KEY
        ```

        Make sure it's set and starts with `sk-`.

        **Verify the project name:**
        Check that `BRAINTRUST_DEFAULT_PROJECT` is set to "Tracing quickstart" and that you're looking at the correct project in the dashboard.

        **Look for errors:**
        Check your console output for any error messages from Braintrust. Common issues:

        * Invalid API key
        * Network connectivity issues
        * Firewall blocking requests to `api.braintrust.dev`
      </Accordion>

      <Accordion title="High latency when logging?">
        **Logging is async:**
        Braintrust logs data asynchronously to avoid blocking your application. Traces should appear in the dashboard within seconds.

        **Check network:**
        If you're experiencing delays, verify network connectivity to `api.braintrust.dev`.
      </Accordion>

      <Accordion title="Python auto-instrumentation not working?">
        **Check braintrust.auto\_instrument():**
        Ensure you call `braintrust.auto_instrument()` at the start of your application before any AI library imports or client creation.

        **Environment variables:**
        Verify `BRAINTRUST_API_KEY` and `BRAINTRUST_DEFAULT_PROJECT` are set in your environment.

        **Supported libraries:**
        Auto-instrumentation works with OpenAI, Anthropic, and 15+ other providers. If your library isn't supported, use manual wrapping with `wrap_openai()`, `wrap_anthropic()`, etc.
      </Accordion>

      <Accordion title="Ruby auto-instrumentation not working?">
        **Check Gemfile:**
        Ensure you have `gem "braintrust", require: "braintrust/setup"` in your Gemfile (note the `require:` option).

        **Bundler setup:**
        Make sure your application loads Bundler with `require 'bundler/setup'` and `Bundler.require`. This is present by default in Rails applications, but may need to be added in Sinatra, Rack, or other frameworks.

        **Environment variables:**
        Verify `BRAINTRUST_API_KEY` and `BRAINTRUST_DEFAULT_PROJECT` are set in your environment.
      </Accordion>

      <Accordion title="Go auto-instrumentation not working?">
        **Initialize Go module:**
        Ensure you have a `go.mod` file in your project. If not, run:

        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
        go mod init your-project-name
        ```

        **Check Orchestrion installation:**

        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
        orchestrion version
        ```

        If this fails, reinstall with `go install github.com/DataDog/orchestrion@latest`.

        **Verify orchestrion.tool.go:**
        Ensure you have `orchestrion.tool.go` in your project root with the correct imports:

        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
        //go:build tools

        package main

        import (
        	_ "github.com/DataDog/orchestrion"
        	_ "github.com/braintrustdata/braintrust-sdk-go/trace/contrib/all"
        )
        ```

        **Build with Orchestrion:**
        You must build with `orchestrion go build` - regular `go build` won't instrument your code.

        **Environment variables:**
        Verify `BRAINTRUST_API_KEY` and `BRAINTRUST_DEFAULT_PROJECT` are set in your environment.

        **Go version:**
        Requires Go 1.24 or later. Check with `go version`.
      </Accordion>

      <Accordion title="Need help?">
        * Join our [Discord](https://discord.gg/6G8s47F44X)
        * Email us at [support@braintrust.dev](mailto:support@braintrust.dev)
        * Use the [Loop](/observe/loop) feature in the Braintrust UI
      </Accordion>
    </AccordionGroup>
  </Tab>
</Tabs>

## Next steps

* Explore the full [Braintrust workflow](/workflow)
* Go deeper with tracing:
  * [Explore integrations](/integrations) with AI providers, SDKs, and developer tools
  * [Add custom tracing](/instrument/custom-tracing) for application logic
  * [Capture user feedback](/instrument/user-feedback) like thumbs up/down
  * [Analyze logs](/observe/view-logs) for patterns and issues
