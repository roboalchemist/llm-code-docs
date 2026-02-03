# Source: https://braintrust.dev/docs/integrations/ai-providers/gemini.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemini

> Google Gemini model provider configuration and integration guide

Google's Gemini models include Gemini 2.0 Flash, Gemini 2.5 Pro, and other advanced multimodal language models. Braintrust integrates seamlessly with Gemini through direct API access, wrapper functions for automatic tracing, and proxy support.

## Setup

To use Gemini models, configure your Gemini API key in Braintrust.

1. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Add the Gemini API key to your [organization's AI providers](/admin/organizations#configure-ai-providers) or to a [project's AI providers](/admin/projects#configure-ai-providers)
3. Set the Gemini API key and your Braintrust API key as environment variables

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
GEMINI_API_KEY=<your-gemini-api-key>
BRAINTRUST_API_KEY=<your-braintrust-api-key>

# If you are self-hosting Braintrust, set the URL of your hosted dataplane
# BRAINTRUST_API_URL=<your-braintrust-api-url-here>
```

<Note>
  API keys are encrypted at rest using [transparent data encryption](https://en.wikipedia.org/wiki/Transparent_data_encryption) with a [unique 256-bit key and nonce](https://libsodium.gitbook.io/doc/secret-key_cryptography/aead).
</Note>

## Trace with Gemini

[Trace](/instrument/custom-tracing) your Gemini LLM calls for observability and monitoring using either the native [Google GenAI SDK](https://cloud.google.com/vertex-ai/generative-ai/docs/sdks/overview) or the [Braintrust AI proxy](/deploy/ai-proxy).

### Trace automatically with native Google GenAI SDK

Braintrust provides wrapper functions that automatically log Google GenAI API calls. All subsequent API calls will be automatically traced.

<Tip>
  These wrapper functions are convenience functions that integrate the Braintrust logger with the Google GenAI client. For more control, see the [manual wrapping](#manual-wrapping-for-more-control) section below.
</Tip>

Install the required packages:

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

  ```bash Java theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # add to build.gradle dependencies{} block
  implementation 'dev.braintrust:braintrust-sdk-java:<version-goes-here>'
  implementation 'com.google.genai:google-genai:1.20.0'
  ```
</CodeGroup>

Then wrap the Google GenAI client:

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

  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import com.google.genai.Client;
  import com.google.genai.types.GenerateContentConfig;
  import dev.braintrust.Braintrust;
  import dev.braintrust.instrumentation.genai.BraintrustGenAI;
  import io.opentelemetry.api.OpenTelemetry;

  class GeminiExample {
      public static void main(String[] args) {
          // Initialize Braintrust and create OpenTelemetry instance
          Braintrust braintrust = Braintrust.get();
          OpenTelemetry openTelemetry = braintrust.openTelemetryCreate();

          // Wrap the Google GenAI client for automatic tracing
          Client client = BraintrustGenAI.wrap(openTelemetry, new Client.Builder());

          // All API calls are automatically logged
          GenerateContentConfig config = GenerateContentConfig.builder()
              .maxOutputTokens(100)
              .build();

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

### Stream responses with native Google GenAI SDK

The native Google GenAI client supports streaming with automatic tracing of token metrics.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  const stream = await client.models.generateContentStream({
    model: "gemini-2.5-flash",
    contents: "Count from 1 to 10 slowly.",
    config: {
      maxOutputTokens: 200,
    },
  });

  // All streaming chunks are automatically logged
  for await (const chunk of stream) {
    if (chunk.text) {
      process.stdout.write(chunk.text);
    }
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  stream = client.models.generate_content_stream(
      model="gemini-2.5-flash",
      contents="Count from 1 to 10 slowly.",
      config=types.GenerateContentConfig(
          max_output_tokens=200,
      ),
  )

  # All streaming chunks are automatically logged
  for chunk in stream:
      if chunk.text:
          print(chunk.text, end="")
  ```

  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import com.google.genai.Client;
  import com.google.genai.types.GenerateContentConfig;
  import dev.braintrust.Braintrust;
  import dev.braintrust.instrumentation.genai.BraintrustGenAI;
  import io.opentelemetry.api.OpenTelemetry;

  class GeminiStreamingExample {
      public static void main(String[] args) {
          Braintrust braintrust = Braintrust.get();
          OpenTelemetry openTelemetry = braintrust.openTelemetryCreate();
          Client client = BraintrustGenAI.wrap(openTelemetry, new Client.Builder());

          GenerateContentConfig config = GenerateContentConfig.builder()
              .maxOutputTokens(200)
              .build();

          var stream = client.models.generateContentStream(
              "gemini-2.5-flash",
              "Count from 1 to 10 slowly.",
              config
          );

          // All streaming chunks are automatically logged
          for (var chunk : stream) {
              String text = chunk.text();
              if (text != null && !text.isEmpty()) {
                  System.out.print(text);
              }
          }
      }
  }
  ```
</CodeGroup>

### Manual wrapping for more control

If you need more control over when tracing is enabled, you can manually wrap the client.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import * as googleGenAI from "@google/genai";
  import { wrapGoogleGenAI, initLogger } from "braintrust";

  initLogger({ projectName: "My Project" });

  // Wrap only when needed
  const { GoogleGenAI } = wrapGoogleGenAI(googleGenAI);

  const client = new GoogleGenAI({
    apiKey: process.env.GEMINI_API_KEY || "",
  });

  const response = await client.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Hello, world!",
  });

  console.log(response.text);
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from braintrust import init_logger
  from braintrust.wrappers.google_genai import wrap_async_models, wrap_client, wrap_models
  from google.genai import Client as BaseClient

  init_logger(project="My Project")


  @wrap_client
  class Client(BaseClient):
      @property
      def models(self):
          return wrap_models(super().models)

      @property
      def aio(self):
          @wrap_client
          class AsyncClient:
              def __init__(self, parent):
                  self._parent = parent._aio

              @property
              def models(self):
                  return wrap_async_models(self._parent.models)

          return AsyncClient(super())


  client = Client(api_key=os.environ["GEMINI_API_KEY"])
  response = client.models.generate_content(
      model="gemini-1.5-flash",
      contents="Hello, world!",
  )

  # Async operations are also traced
  import asyncio


  async def generate_async():
      response = await client.aio.models.generate_content(
          model="gemini-1.5-flash", contents="Write a haiku about coding"
      )
      return response


  # Run async generation
  result = asyncio.run(generate_async())
  ```

  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import com.google.genai.Client;
  import com.google.genai.types.GenerateContentConfig;
  import dev.braintrust.Braintrust;
  import dev.braintrust.instrumentation.genai.BraintrustGenAI;
  import io.opentelemetry.api.OpenTelemetry;

  class GeminiManualWrappingExample {
      public static void main(String[] args) {
          Braintrust braintrust = Braintrust.get();
          OpenTelemetry openTelemetry = braintrust.openTelemetryCreate();

          // Wrap the client when you need tracing enabled
          Client client = BraintrustGenAI.wrap(openTelemetry, new Client.Builder());

          GenerateContentConfig config = GenerateContentConfig.builder()
              .temperature(0.0f)
              .build();

          var response = client.models.generateContent(
              "gemini-1.5-flash",
              "Hello, world!",
              config
          );

          System.out.println(response.text());
      }
  }
  ```
</CodeGroup>

## Use Gemini with Braintrust AI proxy

The [Braintrust AI Proxy](/deploy/ai-proxy) allows you to access Gemini models through a unified OpenAI-compatible interface.

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

Then, initialize the client and make a request to a Gemini model via the Braintrust AI Proxy.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const response = await client.chat.completions.create({
    model: "gemini-2.5-flash",
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
      model="gemini-2.5-flash",
      messages=[{"role": "user", "content": "Hello, world!"}],
  )
  ```
</CodeGroup>

### Trace AI proxy calls

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
    model: "gemini-2.5-flash",
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
      model="gemini-2.5-flash",
      messages=[{"role": "user", "content": "What is machine learning?"}],
  )
  ```
</CodeGroup>

### Stream with proxy

Gemini models support streaming through the proxy.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  const stream = await client.chat.completions.create({
    model: "gemini-2.5-flash",
    messages: [{ role: "user", content: "Count to 10" }],
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || "");
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  stream = client.chat.completions.create(
      model="gemini-2.5-flash",
      messages=[{"role": "user", "content": "Count to 10"}],
      stream=True,
  )

  for chunk in stream:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="")
  ```
</CodeGroup>

## Evaluate with Gemini

Evaluations distill the non-deterministic outputs of Gemini models into an effective feedback loop that enables you to ship more reliable, higher quality products. Braintrust `Eval` is a simple function composed of a dataset of user inputs, a task, and a set of scorers. To learn more about evaluations, see the [Experiments](/evaluate/run-evaluations) guide.

### Evaluate with native SDK

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import * as googleGenAI from "@google/genai";
  import { Eval, wrapGoogleGenAI, initLogger } from "braintrust";

  // Setup tracing
  initLogger({ projectName: "Gemini Evaluation" });
  const { GoogleGenAI } = wrapGoogleGenAI(googleGenAI);

  const client = new GoogleGenAI({
    apiKey: process.env.GEMINI_API_KEY || "",
  });

  Eval("Gemini Native Evaluation", {
    data: () => [
      { input: "What is 2+2?", expected: "4" },
      { input: "What is the capital of France?", expected: "Paris" },
    ],
    task: async (input) => {
      const response = await client.models.generateContent({
        model: "gemini-2.5-flash",
        contents: input,
        config: {
          maxOutputTokens: 100,
        },
      });
      return response.text;
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
  from braintrust import Eval
  from braintrust.wrappers.google_genai import setup_genai
  from google.genai import types
  from google.genai.client import Client

  # Setup tracing
  setup_genai(project_name="Gemini Evaluation")

  client = Client(api_key=os.environ["GEMINI_API_KEY"])


  def task(input):
      response = client.models.generate_content(
          model="gemini-2.5-flash",
          contents=input,
          config=types.GenerateContentConfig(
              max_output_tokens=100,
          ),
      )
      return response.text


  def accuracy_scorer(output, expected, **kwargs):
      return 1 if output == expected else 0


  Eval(
      "Gemini Native Evaluation",
      data=[
          {"input": "What is 2+2?", "expected": "4"},
          {"input": "What is the capital of France?", "expected": "Paris"},
      ],
      task=task,
      scores=[accuracy_scorer],
  )
  ```
</CodeGroup>

### Evaluate with proxy

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { Eval } from "braintrust";
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  Eval("Gemini Evaluation", {
    data: () => [
      { input: "What is 2+2?", expected: "4" },
      { input: "What is the capital of France?", expected: "Paris" },
    ],
    task: async (input) => {
      const response = await client.chat.completions.create({
        model: "gemini-2.5-flash",
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
          model="gemini-2.5-flash",
          messages=[{"role": "user", "content": input}],
      )
      return response.choices[0].message.content


  def accuracy_scorer(output, expected, **kwargs):
      return 1 if output == expected else 0


  Eval(
      "Gemini Evaluation",
      data=[
          {"input": "What is 2+2?", "expected": "4"},
          {"input": "What is the capital of France?", "expected": "Paris"},
      ],
      task=task,
      scores=[accuracy_scorer],
  )
  ```
</CodeGroup>

## Additional features

### Reasoning models

Gemini 2.5 models (`gemini-2.5-flash`, `gemini-2.5-pro`) have built-in reasoning capabilities enabled by default. You can configure reasoning behavior using `thinkingConfig`.

#### Native SDK

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import * as googleGenAI from "@google/genai";
  import { wrapGoogleGenAI, initLogger } from "braintrust";

  // Setup automatic tracing
  initLogger({ projectName: "My Project" });
  const { GoogleGenAI } = wrapGoogleGenAI(googleGenAI);

  const client = new GoogleGenAI({
    apiKey: process.env.GEMINI_API_KEY || "",
  });

  // Use reasoning model - reasoning tokens are automatically tracked
  const response = await client.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "What is the derivative of x^2 + 3x + 5? Think step by step.",
    config: {
      maxOutputTokens: 1000,
    },
  });

  // The response includes both the reasoning and final answer
  console.log(response.text);

  // Metrics automatically include reasoning tokens
  // The wrapper captures completion_reasoning_tokens in the metrics
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from braintrust.wrappers.google_genai import setup_genai
  from google import genai
  from google.genai import types

  # Setup automatic tracing
  setup_genai(project_name="My Project")
  client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

  # Use reasoning model - reasoning tokens are automatically tracked
  response = client.models.generate_content(
      model="gemini-2.5-flash",
      contents="What is the derivative of x^2 + 3x + 5? Think step by step.",
      config=types.GenerateContentConfig(
          max_output_tokens=1000,
      ),
  )

  # The response includes both the reasoning and final answer
  print(response.text)


  # Metrics automatically include reasoning tokens
  # The wrapper captures completion_reasoning_tokens in the metrics

  ```

  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import com.google.genai.Client;
  import com.google.genai.types.GenerateContentConfig;
  import dev.braintrust.Braintrust;
  import dev.braintrust.instrumentation.genai.BraintrustGenAI;
  import io.opentelemetry.api.OpenTelemetry;

  class GeminiReasoningExample {
      public static void main(String[] args) {
          // Setup automatic tracing
          Braintrust braintrust = Braintrust.get();
          OpenTelemetry openTelemetry = braintrust.openTelemetryCreate();
          Client client = BraintrustGenAI.wrap(openTelemetry, new Client.Builder());

          // Use reasoning model - reasoning tokens are automatically tracked
          GenerateContentConfig config = GenerateContentConfig.builder()
              .maxOutputTokens(1000)
              .build();

          var response = client.models.generateContent(
              "gemini-2.5-flash",
              "What is the derivative of x^2 + 3x + 5? Think step by step.",
              config
          );

          // The response includes both the reasoning and final answer
          System.out.println(response.text());

          // Metrics automatically include reasoning tokens
          // The wrapper captures completion_reasoning_tokens in the metrics
      }
  }
  ```
</CodeGroup>

### Structured outputs

Gemini supports structured JSON outputs using response schemas.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import * as googleGenAI from "@google/genai";
  import { wrapGoogleGenAI, initLogger } from "braintrust";

  // Setup automatic tracing
  initLogger({ projectName: "My Project" });
  const { GoogleGenAI } = wrapGoogleGenAI(googleGenAI);

  const client = new GoogleGenAI({
    apiKey: process.env.GEMINI_API_KEY || "",
  });

  // Define a schema for the response
  interface Person {
    name: string;
    age: number;
    occupation: string;
  }

  const response = await client.models.generateContent({
    model: "gemini-1.5-flash",
    contents:
      "Extract information about: John Smith is a 30-year-old software engineer.",
    config: {
      responseMimeType: "application/json",
      responseSchema: {
        type: "object",
        properties: {
          name: { type: "string" },
          age: { type: "number" },
          occupation: { type: "string" },
        },
        required: ["name", "age", "occupation"],
      },
      maxOutputTokens: 200,
    },
  });

  // Parse the JSON response
  const personData: Person = JSON.parse(response.text);
  console.log(`Name: ${personData.name}, Age: ${personData.age}`);
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from typing import TypedDict

  from braintrust.wrappers.google_genai import setup_genai
  from google import genai
  from google.genai import types

  # Setup automatic tracing
  setup_genai(project_name="My Project")
  client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


  # Define a schema for the response
  class Person(TypedDict):
      name: str
      age: int
      occupation: str


  response = client.models.generate_content(
      model="gemini-1.5-flash",
      contents="Extract information about: John Smith is a 30-year-old software engineer.",
      config=types.GenerateContentConfig(
          response_mime_type="application/json",
          response_schema=Person,
          max_output_tokens=200,
      ),
  )

  # Parse the JSON response
  import json

  person_data = json.loads(response.text)
  print(f"Name: {person_data['name']}, Age: {person_data['age']}")
  ```
</CodeGroup>

### Function calling and tools

Gemini supports function calling for building AI agents with tools.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import * as googleGenAI from "@google/genai";
  import { wrapGoogleGenAI, initLogger } from "braintrust";

  // Setup automatic tracing
  initLogger({ projectName: "My Project" });
  const { GoogleGenAI } = wrapGoogleGenAI(googleGenAI);

  const client = new GoogleGenAI({
    apiKey: process.env.GEMINI_API_KEY || "",
  });

  // Define functions for the model to call
  function getWeather(location: string, unit: string = "celsius"): string {
    // In a real app, this would call a weather API
    return `22 degrees ${unit} and sunny in ${location}`;
  }

  function searchWeb(query: string): string {
    return `Search results for: ${query}`;
  }

  // Define function declarations
  const tools = [
    {
      functionDeclarations: [
        {
          name: "get_weather",
          description: "Get the current weather for a location",
          parameters: {
            type: "object",
            properties: {
              location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA",
              },
              unit: {
                type: "string",
                enum: ["celsius", "fahrenheit"],
                description: "The unit of temperature",
              },
            },
            required: ["location"],
          },
        },
        {
          name: "search_web",
          description: "Search the web for information",
          parameters: {
            type: "object",
            properties: {
              query: {
                type: "string",
                description: "The search query",
              },
            },
            required: ["query"],
          },
        },
      ],
    },
  ];

  // Generate with tools
  const response = await client.models.generateContent({
    model: "gemini-1.5-flash",
    contents:
      "What's the weather in Paris and what tourist sites should I visit?",
    config: {
      tools: tools,
      maxOutputTokens: 500,
    },
  });

  // Handle function calls
  if (response.candidates[0].content.parts) {
    for (const part of response.candidates[0].content.parts) {
      if (part.functionCall) {
        const fc = part.functionCall;
        console.log(`Function: ${fc.name}`);
        console.log(`Arguments: ${JSON.stringify(fc.args)}`);

        // Execute the function
        if (fc.name === "get_weather") {
          const result = getWeather(fc.args.location, fc.args.unit);
          // Send result back to model for final response
        }
      }
    }
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from braintrust.wrappers.google_genai import setup_genai
  from google import genai
  from google.genai import types

  # Setup automatic tracing
  setup_genai(project_name="My Project")
  client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


  # Define functions for the model to call
  def get_weather(location: str, unit: str = "celsius") -> str:
      """Get the current weather for a location.

      Args:
          location: The city and state, e.g. San Francisco, CA
          unit: The unit of temperature (celsius or fahrenheit)
      """
      # In a real app, this would call a weather API
      return f"22 degrees {unit} and sunny in {location}"


  def search_web(query: str) -> str:
      """Search the web for information.

      Args:
          query: The search query
      """
      return f"Search results for: {query}"


  # Generate with tools
  response = client.models.generate_content(
      model="gemini-1.5-flash",
      contents="What's the weather in Paris and what tourist sites should I visit?",
      config=types.GenerateContentConfig(
          tools=[get_weather, search_web],  # Pass functions as tools
          max_output_tokens=500,
      ),
  )

  # Handle function calls
  if response.candidates[0].content.parts:
      for part in response.candidates[0].content.parts:
          if hasattr(part, "function_call"):
              fc = part.function_call
              print(f"Function: {fc.name}")
              print(f"Arguments: {fc.args}")

              # Execute the function
              if fc.name == "get_weather":
                  result = get_weather(**fc.args)
                  # Send result back to model for final response
  ```
</CodeGroup>

### Multimodal content

Gemini models support multimodal inputs including images, audio, and video.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import * as googleGenAI from "@google/genai";
  import { wrapGoogleGenAI, initLogger } from "braintrust";
  import * as fs from "fs";

  // Setup automatic tracing
  initLogger({ projectName: "My Project" });
  const { GoogleGenAI } = wrapGoogleGenAI(googleGenAI);

  const client = new GoogleGenAI({
    apiKey: process.env.GEMINI_API_KEY || "",
  });

  // Image analysis
  const imageData = fs.readFileSync("image.jpg");

  const response = await client.models.generateContent({
    model: "gemini-1.5-flash",
    contents: [
      { text: "What's in this image?" },
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: imageData.toString("base64"),
        },
      },
    ],
  });

  // Audio transcription
  const audioData = fs.readFileSync("audio.mp3");

  const audioResponse = await client.models.generateContent({
    model: "gemini-1.5-flash",
    contents: [
      { text: "Transcribe this audio:" },
      {
        inlineData: {
          mimeType: "audio/mp3",
          data: audioData.toString("base64"),
        },
      },
    ],
  });

  // The wrapper automatically handles binary data serialization
  // Binary attachments are converted to Braintrust Attachment objects
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from braintrust.wrappers.google_genai import setup_genai
  from google import genai
  from google.genai import types

  # Setup automatic tracing
  setup_genai(project_name="My Project")
  client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

  # Image analysis
  with open("image.jpg", "rb") as f:
      image_data = f.read()

  response = client.models.generate_content(
      model="gemini-1.5-flash",
      contents=["What's in this image?", types.Part.from_bytes(data=image_data, mime_type="image/jpeg")],
  )

  # Audio transcription
  with open("audio.mp3", "rb") as f:
      audio_data = f.read()

  response = client.models.generate_content(
      model="gemini-1.5-flash",
      contents=["Transcribe this audio:", types.Part.from_bytes(data=audio_data, mime_type="audio/mp3")],
  )

  # The wrapper automatically handles binary data serialization
  # Binary attachments are converted to Braintrust Attachment objects
  ```
</CodeGroup>

### Streaming with token metrics

Stream responses with automatic token tracking.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import * as googleGenAI from "@google/genai";
  import { wrapGoogleGenAI, initLogger } from "braintrust";

  // Setup automatic tracing
  initLogger({ projectName: "My Project" });
  const { GoogleGenAI } = wrapGoogleGenAI(googleGenAI);

  const client = new GoogleGenAI({
    apiKey: process.env.GEMINI_API_KEY || "",
  });

  // Stream responses - automatically tracked
  const stream = await client.models.generateContentStream({
    model: "gemini-1.5-flash",
    contents: "Write a story about a robot learning to paint.",
    config: {
      maxOutputTokens: 500,
    },
  });

  // Streaming automatically tracks:
  // - time_to_first_token
  // - prompt_tokens, completion_tokens, total_tokens
  // - prompt_cached_tokens (if using caching)
  for await (const chunk of stream) {
    if (chunk.text) {
      process.stdout.write(chunk.text);
    }
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from braintrust.wrappers.google_genai import setup_genai
  from google import genai
  from google.genai import types

  # Setup automatic tracing
  setup_genai(project_name="My Project")
  client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

  # Stream responses - automatically tracked
  stream = client.models.generate_content_stream(
      model="gemini-1.5-flash",
      contents="Write a story about a robot learning to paint.",
      config=types.GenerateContentConfig(
          max_output_tokens=500,
      ),
  )

  # Streaming automatically tracks:
  # - time_to_first_token
  # - prompt_tokens, completion_tokens, total_tokens
  # - prompt_cached_tokens (if using caching)
  for chunk in stream:
      if chunk.text:
          print(chunk.text, end="")

  # Async streaming is also supported
  import asyncio


  async def stream_async():
      stream = await client.aio.models.generate_content_stream(
          model="gemini-1.5-flash",
          contents="Count from 1 to 10 slowly.",
          config=types.GenerateContentConfig(
              max_output_tokens=200,
          ),
      )

      async for chunk in stream:
          if chunk.text:
              print(chunk.text, end="")


  asyncio.run(stream_async())
  ```

  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import com.google.genai.Client;
  import com.google.genai.types.GenerateContentConfig;
  import dev.braintrust.Braintrust;
  import dev.braintrust.instrumentation.genai.BraintrustGenAI;
  import io.opentelemetry.api.OpenTelemetry;

  class GeminiStreamingMetricsExample {
      public static void main(String[] args) {
          // Setup automatic tracing
          Braintrust braintrust = Braintrust.get();
          OpenTelemetry openTelemetry = braintrust.openTelemetryCreate();
          Client client = BraintrustGenAI.wrap(openTelemetry, new Client.Builder());

          // Stream responses - automatically tracked
          GenerateContentConfig config = GenerateContentConfig.builder()
              .maxOutputTokens(500)
              .build();

          var stream = client.models.generateContentStream(
              "gemini-1.5-flash",
              "Write a story about a robot learning to paint.",
              config
          );

          // Streaming automatically tracks:
          // - time_to_first_token
          // - prompt_tokens, completion_tokens, total_tokens
          // - prompt_cached_tokens (if using caching)
          for (var chunk : stream) {
              if (chunk.text() != null) {
                  System.out.print(chunk.text());
              }
          }
      }
  }
  ```
</CodeGroup>

### Context caching

Gemini supports context caching for efficient reuse of large contexts.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import * as googleGenAI from "@google/genai";
  import { wrapGoogleGenAI, initLogger } from "braintrust";

  // Setup automatic tracing
  initLogger({ projectName: "My Project" });
  const { GoogleGenAI } = wrapGoogleGenAI(googleGenAI);

  const client = new GoogleGenAI({
    apiKey: process.env.GEMINI_API_KEY || "",
  });

  // Create a cache for a large document
  const documentContent = "... very long document content ...";

  // Note: Caching API requires the full Vertex AI SDK
  // This example shows the structure - refer to Google's documentation
  // for complete caching implementation

  const response = await client.models.generateContent({
    model: "gemini-1.5-flash",
    contents: "Summarize the key points from the document",
    config: {
      // cachedContent would be configured here
      maxOutputTokens: 500,
    },
  });

  // The wrapper tracks cached tokens in metrics
  // Look for prompt_cached_tokens in the logged metrics
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from datetime import timedelta

  from braintrust.wrappers.google_genai import setup_genai
  from google import genai
  from google.genai import caching, types

  # Setup automatic tracing
  setup_genai(project_name="My Project")
  client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

  # Create a cache for a large document
  document_content = "... very long document content ..."

  cache = caching.CachedContent.create(
      model="gemini-1.5-flash",
      contents=[document_content],
      ttl=timedelta(hours=1),
  )

  # Use the cache in subsequent requests
  response = client.models.generate_content(
      model="gemini-1.5-flash",
      contents="Summarize the key points from the document",
      config=types.GenerateContentConfig(
          cached_content=cache,
          max_output_tokens=500,
      ),
  )

  # The wrapper tracks cached tokens in metrics
  # Look for prompt_cached_tokens in the logged metrics
  ```

  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import com.google.genai.Client;
  import com.google.genai.types.GenerateContentConfig;
  import dev.braintrust.Braintrust;
  import dev.braintrust.instrumentation.genai.BraintrustGenAI;
  import io.opentelemetry.api.OpenTelemetry;

  class GeminiCachingExample {
      public static void main(String[] args) {
          // Setup automatic tracing
          Braintrust braintrust = Braintrust.get();
          OpenTelemetry openTelemetry = braintrust.openTelemetryCreate();
          Client client = BraintrustGenAI.wrap(openTelemetry, new Client.Builder());

          // Create a cache for a large document
          String documentContent = "... very long document content ...";

          // Note: Caching API requires the full Vertex AI SDK
          // This example shows the structure - refer to Google's documentation
          // for complete caching implementation

          GenerateContentConfig config = GenerateContentConfig.builder()
              // cachedContent would be configured here
              .maxOutputTokens(500)
              .build();

          var response = client.models.generateContent(
              "gemini-1.5-flash",
              "Summarize the key points from the document",
              config
          );

          // The wrapper tracks cached tokens in metrics
          // Look for prompt_cached_tokens in the logged metrics
      }
  }
  ```
</CodeGroup>

### Use with Spring AI

For Java applications using [Spring AI](https://spring.io/projects/spring-ai), you can integrate Braintrust by wrapping the underlying Google GenAI client and passing it to Spring AI's `GoogleGenAiChatModel`.

<CodeGroup dropdown>
  ```java  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import com.google.genai.Client;
  import dev.braintrust.Braintrust;
  import dev.braintrust.config.BraintrustConfig;
  import dev.braintrust.instrumentation.genai.BraintrustGenAI;
  import io.opentelemetry.api.OpenTelemetry;
  import io.opentelemetry.api.trace.Tracer;

  // Spring AI imports (requires spring-ai-google-genai dependency)
  // import org.springframework.ai.chat.model.ChatModel;
  // import org.springframework.ai.chat.prompt.Prompt;
  // import org.springframework.ai.google.genai.GoogleGenAiChatModel;
  // import org.springframework.ai.google.genai.GoogleGenAiChatOptions;
  // import org.springframework.boot.CommandLineRunner;
  // import org.springframework.boot.SpringApplication;
  // import org.springframework.boot.autoconfigure.SpringBootApplication;
  // import org.springframework.context.annotation.Bean;

  // @SpringBootApplication
  class SpringAIExample {

      public static void main(String[] args) {
          // SpringApplication.run(SpringAIExample.class, args);

          // Key pattern for Spring AI integration:
          // 1. Initialize Braintrust
          Braintrust braintrust = Braintrust.get(BraintrustConfig.fromEnvironment());
          OpenTelemetry openTelemetry = braintrust.openTelemetryCreate();

          // 2. Wrap the Google GenAI client with Braintrust
          Client genAIClient = BraintrustGenAI.wrap(openTelemetry, new Client.Builder());

          // 3. Pass the wrapped client to Spring AI's GoogleGenAiChatModel
          // ChatModel chatModel = GoogleGenAiChatModel.builder()
          //     .genAIClient(genAIClient)
          //     .defaultOptions(
          //         GoogleGenAiChatOptions.builder()
          //             .model("gemini-2.0-flash-lite")
          //             .temperature(0.0)
          //             .maxOutputTokens(50)
          //             .build())
          //     .build();

          // 4. Use the ChatModel in your Spring application
          // All calls through ChatModel are automatically traced to Braintrust
      }
  }
  ```
</CodeGroup>

This pattern works with all Spring AI features including streaming, function calling, and structured outputs. All calls through the `ChatModel` are automatically traced to Braintrust.

### Error handling, attachments, and masking sensitive data

To learn more about these topics, check out the [customize traces](/instrument/advanced-tracing) guide.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";
  import "@braintrust/proxy/types"; // for type safety

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const response = await client.chat.completions.create({
    model: "gemini-2.5-flash",
    reasoning_enabled: true,
    reasoning_budget: 1024,
    messages: [{ role: "user", content: "How many rs in 'ferrocarril'?" }],
  });

  console.log(response.choices[0].reasoning); // Access reasoning steps
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      api_key=os.environ["BRAINTRUST_API_KEY"],
  )

  response = client.chat.completions.create(
      model="gemini-2.5-flash",
      reasoning_enabled=True,
      reasoning_budget=1024,
      messages=[{"role": "user", "content": "How many rs in 'ferrocarril'?"}],
  )

  print(response.choices[0].reasoning)  # Access reasoning steps
  ```
</CodeGroup>

<Tip>
  To learn more about multimodal support, attachments, error handling, and masking sensitive data with Gemini, visit the [customize traces](/instrument/advanced-tracing) guide.
</Tip>
