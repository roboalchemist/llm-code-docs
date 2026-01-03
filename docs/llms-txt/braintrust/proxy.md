# Source: https://braintrust.dev/docs/guides/proxy.md

# AI proxy

> Access models from OpenAI, Anthropic, Google, AWS, Mistral, and more

The Braintrust AI Proxy is a powerful tool that enables you to access models from [OpenAI](https://platform.openai.com/docs/models),
[Anthropic](https://docs.anthropic.com/claude/reference/getting-started-with-the-api), [Google](https://ai.google.dev/gemini-api/docs),
[AWS](https://aws.amazon.com/bedrock), [Mistral](https://mistral.ai/), and third-party inference providers like [Together](https://www.together.ai/) which offer
open source models like [LLaMa 3](https://ai.meta.com/llama/) — all through a single, unified API.

With the AI proxy, you can:

* **Simplify your code** by accessing many AI providers through a single API.
* **Reduce your costs** by automatically caching results when possible.
* **Increase observability** by optionally logging your requests to Braintrust.

Best of all, the AI proxy is free to use, even if you don't have a Braintrust account.

To read more about why we launched the AI proxy, check out our [blog post](https://www.braintrust.dev/blog/ai-proxy) announcing the feature.

<Note>
  The AI proxy is free for all users. You can access it without a Braintrust
  account by using your API key from any of the supported providers. With a
  Braintrust account, you can use a single Braintrust API key to access all AI
  providers.
</Note>

## Quickstart

The Braintrust Proxy is fully compatible with applications written using the
[OpenAI SDK]. You can get started without making any code changes. Just set the
API URL to `https://api.braintrust.dev/v1/proxy`.

Try running the following script in your favorite language, twice:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";
  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.OPENAI_API_KEY, // Can use Braintrust, Anthropic, etc. API keys here
  });

  async function main() {
    const start = performance.now();
    const response = await client.chat.completions.create({
      model: "gpt-4o-mini", // Can use claude-3-5-sonnet-latest, gemini-2.5-flash, etc. here
      messages: [{ role: "user", content: "What is a proxy?" }],
      seed: 1, // A seed activates the proxy's cache
    });
    console.log(response.choices[0].message.content);
    console.log(`Took ${(performance.now() - start) / 1000}s`);
  }

  main();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  import time

  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      api_key=os.environ["OPENAI_API_KEY"],  # Can use Braintrust, Anthropic, etc. API keys here
  )

  start = time.time()
  response = client.chat.completions.create(
      model="gpt-4o-mini",  # Can use claude-3-5-sonnet-latest, gemini-2.5-flash, etc. here
      messages=[{"role": "user", "content": "What is a proxy?"}],
      seed=1,  # A seed activates the proxy's cache
  )
  print(response.choices[0].message.content)
  print(f"Took {time.time() - start}s")
  ```

  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  time curl -i https://api.braintrust.dev/v1/proxy/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
      "model": "gpt-4o-mini",
      "messages": [
        {
          "role": "user",
          "content": "What is a proxy?"
        }
      ],
      "seed": 1
    }' \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    --compress
  ```
</CodeGroup>

<Note>
  Anthropic users can pass their Anthropic API key with a model such as
  `claude-3-5-sonnet-20240620`.
</Note>

The second run will be significantly faster because the proxy served your
request from its cache, rather than rerunning the AI provider's model. Under the
hood, your request is served from a [Cloudflare Worker] that caches your request
with end-to-end encryption.

[OpenAI SDK]: https://platform.openai.com/docs/libraries

[Cloudflare Worker]: https://workers.cloudflare.com/

## Key features

The proxy is a drop-in replacement for the OpenAI API, with a few killer features:

* Automatic caching of results, with configurable semantics
* Interopability with other providers, including a wide range of open source models
* Run reasoning models across providers with a single call
* API key management

The proxy also supports the Anthropic and Gemini APIs for making requests to Anthropic and Gemini models.

### Caching

The proxy automatically caches results, and reuses them when possible. Because the proxy runs on the edge,
expect cached requests to be returned in under 100ms. This is especially useful when you're developing
and frequently re-running or evaluating the same prompts many times.

#### Cache modes

There are three caching modes: `auto` (default), `always`, `never`:

* In `auto` mode, requests are cached if they have `temperature=0` or the
  [`seed` parameter](https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter) set and they are one of the supported paths.
* In `always` mode, requests are cached as long as they are one of the supported paths.
* In `never` mode, the cache is never read or written to.

The supported paths are:

* `/auto`
* `/embeddings`
* `/chat/completions`
* `/completions`
* `/moderations`

Set the cache mode by passing the `x-bt-use-cache` header to your request.

#### Cache TTL

By default, cached results expire after 1 week. The TTL for individual requests can be set by passing the `x-bt-cache-ttl` header to your request. The TTL is specified in seconds and must be between 1 and 604800 (7 days).

#### Cache control

The proxy supports a limited set of [Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) directives:

* To bypass the cache, set the `Cache-Control` header to `no-cache, no-store`. Note that this is semantically equivalent to setting the `x-bt-use-cache` header to `never`.
* To force a fresh request, set the `Cache-Control` header to `no-cache`. Note that without the `no-store` directive the response will be cached for subsequent requests.
* To request a cached response with a maximum age, set the `Cache-Control` header to `max-age=<seconds>`. If the cached data is older than the specified age that the cache will be bypassed and a new response will be generated. Combine this with `no-store` to bypass the cache for a request without overwriting the currently cached response.

When cache control directives conflict with the `x-bt-use-cache` header, the cache control directives take precedence.

The proxy will return the `x-bt-cached` header in the response with `HIT` or `MISS` to indicate whether the response was served from the cache, the `Age` header to indicate the age of the cached response, and the `Cache-Control` header with the `max-age` directive to return the TTL/max age of the cached response.

For example, to set the cache mode to `always` with a TTL of 2 days,

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    defaultHeaders: {
      "x-bt-use-cache": "always",
      "Cache-Control": "max-age=172800",
    },
    apiKey: process.env.OPENAI_API_KEY, // Can use Braintrust, Anthropic, etc. API keys here
  });

  async function main() {
    const response = await client.chat.completions.create({
      model: "gpt-4o", // Can use claude-3-5-sonnet-latest, gemini-2.5-flash, etc. here
      messages: [{ role: "user", content: "What is a proxy?" }],
    });
    console.log(response.choices[0].message.content);
  }

  main();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      default_headers={"x-bt-use-cache": "always", "Cache-Control": "max-age=1209600"},
      api_key=os.environ["OPENAI_API_KEY"],  # Can use Braintrust, Anthropic, etc. API keys here
  )

  response = client.chat.completions.create(
      model="gpt-4o",  # Can use claude-3-5-sonnet-latest, gemini-2.5-flash, etc. here
      messages=[{"role": "user", "content": "What is a proxy?"}],
  )
  print(response.choices[0].message.content)
  ```

  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  time curl -i https://api.braintrust.dev/v1/proxy/chat/completions \
    -H "Content-Type: application/json" \
    -H "x-bt-use-cache: always" \
    -H "Cache-Control: max-age=1209600" \
    -d '{
      "model": "gpt-4o",
      "messages": [
        {
          "role": "user",
          "content": "What is a proxy?"
        }
      ]
    }' \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    --compress
  ```
</CodeGroup>

#### Encryption

We use [AES-GCM](https://en.wikipedia.org/wiki/Galois/Counter_Mode) to encrypt the cache, using a key derived from your
API key. Results are cached for 1 week unless otherwise specified in request headers.

This design ensures that the cache is only accessible to you, and that we cannot see your data. We also do not store
or log API keys.

<Note>
  Because the cache's encryption key is your API key, cached results are scoped
  to an individual user. However, Braintrust customers can opt-into sharing
  cached results across users within their organization.
</Note>

### Tracing

To log requests that you make through the proxy, specify an `x-bt-parent` header with the project or
experiment you'd like to log to. While tracing, you must also use a `BRAINTRUST_API_KEY` rather than a provider's
key. Behind the scenes, the proxy will derive your provider's key and facilitate tracing using the `BRAINTRUST_API_KEY`.

For example,

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    defaultHeaders: {
      "x-bt-parent": "project_id:<YOUR PROJECT ID>",
    },
    apiKey: process.env.BRAINTRUST_API_KEY, // Must use Braintrust API key
  });

  async function main() {
    const response = await client.chat.completions.create({
      model: "gpt-4o", // Can use claude-3-5-sonnet-latest, gemini-2.5-flash, etc. here
      messages: [{ role: "user", content: "What is a proxy?" }],
    });
    console.log(response.choices[0].message.content);
  }

  main();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      default_headers={"x-bt-parent": "project_id:<YOUR PROJECT ID>"},
      api_key=os.environ["BRAINTRUST_API_KEY"],  # Must use Braintrust API key
  )

  response = client.chat.completions.create(
      model="gpt-4o",  # Can use claude-3-5-sonnet-latest, gemini-2.5-flash, etc. here
      messages=[{"role": "user", "content": "What is a proxy?"}],
  )
  print(response.choices[0].message.content)
  ```

  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  time curl -i https://api.braintrust.dev/v1/proxy/chat/completions \
    -H "Content-Type: application/json" \
    -H "x-bt-parent: project_id:<YOUR PROJECT ID>" \
    -d '{
      "model": "gpt-4o",
      "messages": [
        {
          "role": "user",
          "content": "What is a proxy?"
        }
      ]
    }' \
    -H "Authorization: Bearer $BRAINTRUST_API_KEY" \
    --compress
  ```
</CodeGroup>

The `x-bt-parent` header sets the trace's parent project or experiment. You can use
a prefix like `project_id:`, `project_name:`, or `experiment_id:` or pass in
a [span slug](/guides/traces#distributed-tracing)
(`span.export()`) to nest the trace under a span within the parent object.

<Note>
  To find your project ID, navigate to your project's configuration page and find the **Copy Project ID** button at the bottom of the page.
</Note>

### Supported models

The proxy supports over 100 models, including popular models like o4-mini, Claude
4 Sonnet, Llama 2, and Gemini Pro 2.5. It also supports third-party inference
providers, including the [Azure OpenAI Service], [Amazon Bedrock], and
[Together AI]. See the [full list of models and providers](#appendix) at the
bottom of this page.

We are constantly adding new models. If you have a model you'd like to see
supported, please [let us know](mailto:support@braintrust.dev)!

[Azure OpenAI Service]: https://azure.microsoft.com/en-us/products/ai-services/openai-service

[Amazon Bedrock]: https://aws.amazon.com/bedrock/

[Together AI]: https://www.together.ai/

### Supported protocols

#### HTTP-based models

On the `/auto`, and `/chat/completions` endpoints,
the proxy receives HTTP requests in the [OpenAI API schema] and automatically
translates OpenAI requests into various providers' APIs. That means you can
interact with other providers like Anthropic by using OpenAI client libraries
and API calls.

For example,

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
curl -X POST https://api.braintrust.dev/v1/proxy/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $BRAINTRUST_API_KEY" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "What is a proxy?"}]
  }'
```

The proxy can also receive requests in the Anthropic and Gemini API schemas
for making requests to those respective models.

For example, you can make an Anthropic request with the following curl command:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
curl -X POST https://api.braintrust.dev/v1/proxy/anthropic/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $BRAINTRUST_API_KEY" \
  -d '{
    "model": "claude-3-5-sonnet-20240620",
    "messages": [{"role": "user", "content": "What is a proxy?"}]
  }'
```

Note that the `anthropic-version` and `x-api-key` headers do not need to be set.

Similarly, you can make a Gemini request with the following curl command:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
curl -X POST https://api.braintrust.dev/v1/proxy/google/models/gemini-2.5-flash:generateContent \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $BRAINTRUST_API_KEY" \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "What is a proxy?"
          }
        ]
      }
    ]
  }'
```

[OpenAI API schema]: https://platform.openai.com/docs/api-reference/introduction

### Reasoning models

<Note>
  If you are on a hybrid deployment, reasoning support is available starting with `v0.0.74`.
</Note>

The Braintrust proxy lets you write one chat completion call that works across multiple providers by standardizing support for reasoning-specific features.

* **Supported providers:** We support reasoning models from OpenAI, Anthropic, and Google.
* **Unified parameters:** We use a consistent set of parameters related to reasoning:
  * `reasoning_effort`: Compatible with OpenAI's `reasoning_effort`, this parameter allows you to specify the desired level of reasoning complexity.
  * `reasoning_enabled`: An explicit flag to enable or disable reasoning output. Note: has no effect when using an OpenAI model.
  * `reasoning_budget`: Allows you to specify a budget for the reasoning process. Note: you must provide either `reasoning_effort` or `reasoning_enabled` (for models that support it).
* **Structured reasoning output:** Responses from models that support reasoning will include a list of `reasoning` objects as part of the assistant's message. Each object contains the `content` of the reasoning step and a unique `id`. Include these `reasoning` objects from previous turns in subsequent requests to maintain context in multi-turn conversations.
* **Streaming support:** For streaming responses, a new `reasoning_delta` is available, allowing you to process reasoning output as it is generated by the model.
* **Type safety:** To provide a better developer experience when using SDKs like OpenAI's, we offer type augmentations. For JavaScript/TypeScript, use the `@braintrust/proxy/types` module to extend OpenAI's types. For Python, the `braintrust-proxy` package provides casting utilities for input parameters and output objects, helping avoid type errors in your IDEs.

#### Non-streaming request with reasoning parameters

Here's a non-streaming chat completion request using a Google model, explicitly enabling reasoning with `reasoning_enabled` and setting a `reasoning_budget`:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";
  import "@braintrust/proxy/types"; // to avoid IDE and build type errors ... need a minimum of node16 moduleResolution for this to work

  async function main() {
    const openai = new OpenAI({
      baseURL: `${process.env.BRAINTRUST_API_URL || "https://api.braintrust.dev"}/v1/proxy`,
      apiKey: process.env.BRAINTRUST_API_KEY,
    });

    try {
      const response = await openai.chat.completions.create({
        model: "gemini-2.5-flash",
        reasoning_enabled: true,
        reasoning_budget: 1024,
        stream: false,
        messages: [
          {
            role: "user",
            content: "How many rs in 'ferrocarril'",
          },
          {
            role: "assistant",
            content: "There are 4 letter 'r's in the word \"ferrocarril\".",
            reasoning: [
              {
                id: "", //  just an example, but make sure to include any id(entifiers) as provided by the previous AI response
                content:
                  "To count the number of 'r's in the word 'ferrocarril', I'll just go through the word letter by letter.\n\n'ferrocarril' has the following letters:\nf-e-r-r-o-c-a-r-r-i-l\n\nLooking at each letter:\n- 'f': not an 'r'\n- 'e': not an 'r'\n- 'r': This is an 'r', so that's 1.\n- 'r': This is an 'r', so that's 2.\n- 'o': not an 'r'\n- 'c': not an 'r'\n- 'a': not an 'r'\n- 'r': This is an 'r', so that's 3.\n- 'r': This is an 'r', so that's 4.\n- 'i': not an 'r'\n- 'l': not an 'r'\n\nSo there are 4 'r's in the word 'ferrocarril'.",
              },
            ],
          },
          {
            role: "user",
            content: "How many e in what you said?",
          },
        ],
      });

      console.log({
        message: response.choices[0].message,
        reasoning: response.choices[0].reasoning,
      });
    } catch (error) {
      console.error("Error during non-streaming request:", error);
    }
  }

  main().catch(console.error);
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import json
  import os

  from braintrust_proxy import as_openai_chat_message_param
  from openai import OpenAI

  client = OpenAI(
      base_url=f"{os.getenv('BRAINTRUST_API_URL') or 'https://api.braintrust.dev'}/v1/proxy",
      api_key=os.getenv("BRAINTRUST_API_KEY"),
  )

  try:
      print("Non-streaming Response:")
      response = client.chat.completions.create(
          model="gemini-2.5-flash",
          # provide extra reasoning parameters with extra_body
          extra_body={
              "reasoning_enabled": True,
              "reasoning_budget": 1024,
          },
          stream=False,
          messages=[
              {
                  "role": "user",
                  "content": "How many rs in 'ferrocarril'",
              },
              as_openai_chat_message_param(
                  {
                      "role": "assistant",
                      "content": "There are 4 letter 'r's in the word \"ferrocarril\".",
                      "reasoning": [
                          {
                              "id": "",  # just an example, but make sure to include any id(entifiers) as provided by the previous AI response
                              "content": "To count the number of 'r's in the word 'ferrocarril', I'll just go through the word letter by letter.\n\n'ferrocarril' has the following letters:\nf-e-r-r-o-c-a-r-r-i-l\n\nLooking at each letter:\n- 'f': not an 'r'\n- 'e': not an 'r'\n- 'r': This is an 'r', so that's 1.\n- 'r': This is an 'r', so that's 2.\n- 'o': not an 'r'\n- 'c': not an 'r'\n- 'a': not an 'r'\n- 'r': This is an 'r', so that's 3.\n- 'r': This is an 'r', so that's 4.\n- 'i': not an 'r'\n- 'l': not an 'r'\n\nSo there are 4 'r's in the word 'ferrocarril'.",
                          },
                      ],
                  }
              ),
              {
                  "role": "user",
                  "content": "How many e in what you said?",
              },
          ],
      )

      print(
          json.dumps(
              {
                  "message": response.choices[0].message.dict(),
                  "reasoning": getattr(response.choices[0].message, "reasoning", None),
              },
              indent=2,
          )
      )
  except Exception as e:
      print("Error during non-streaming request:", e)
  ```
</CodeGroup>

#### Streaming request with reasoning delta

This example shows how to handle the `reasoning_delta` when streaming chat completion responses:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";
  import "@braintrust/proxy/types"; // to avoid IDE and build type errors

  async function main() {
    const openai = new OpenAI({
      baseURL: `${process.env.BRAINTRUST_API_URL || "https://api.braintrust.dev"}/v1/proxy`,
      apiKey: process.env.BRAINTRUST_API_KEY,
    });

    try {
      console.log("Streaming Request:");
      const stream = await openai.chat.completions.create({
        model: "claude-sonnet-4",
        messages: [
          {
            role: "user",
            content: "Tell me a short story.",
          },
        ],
        reasoning_effort: "high",
        stream: true,
      });

      for await (const event of stream) {
        if (event.choices && event.choices[0].delta) {
          const delta = event.choices[0].delta;
          if (delta.content) {
            process.stdout.write(`Content: ${delta.content}`);
          }
          if (delta.reasoning) {
            console.log("\nReasoning delta:", delta.reasoning);
          }
        }
      }
      console.log("\nStreaming Finished.");
    } catch (error) {
      console.error("Error during streaming request:", error);
    }
  }

  main().catch(console.error);
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import json
  import os

  from braintrust_proxy import from_openai_chat_completion_choice_delta
  from openai import OpenAI

  client = OpenAI(
      base_url=f"{os.getenv('BRAINTRUST_API_URL') or 'https://api.braintrust.dev'}/v1/proxy",
      api_key=os.getenv("BRAINTRUST_API_KEY"),
  )

  try:
      print("Streaming Request:")
      stream = client.chat.completions.create(
          model="claude-sonnet-4",
          reasoning_effort="high",
          stream=True,
          messages=[
              {
                  "role": "user",
                  "content": "Tell me a short story.",
              },
          ],
      )

      for event in stream:
          delta = from_openai_chat_completion_choice_delta(event.choices[0].delta)
          if delta.content:
              print(f"Content delta: {delta.content}")
          if delta.reasoning:
              print(f"Reasoning delta: {delta.reasoning.dict()}")
      print("Streaming Finished.")

  except Exception as e:
      print("Error during streaming request:", e)
  ```
</CodeGroup>

### WebSocket-based models

The proxy supports the [OpenAI Realtime API](https://platform.openai.com/images/guides/realtime) at the
`/realtime` endpoint. Use the official OpenAI SDK (version 6.0+) to connect to the proxy's realtime endpoint.

<Note>
  You must use [https://braintrustproxy.com/v1](https://braintrustproxy.com/v1), not [https://api.braintrust.dev/v1/proxy](https://api.braintrust.dev/v1/proxy), for WebSocket-based proxying
</Note>

#### Node.js with ws library

In Node.js environments, use `OpenAIRealtimeWS` from the `openai/realtime/ws` module:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAIRealtimeWS } from "openai/realtime/ws";

  const rt = new OpenAIRealtimeWS(
    {
      model: "gpt-realtime",
    },
    {
      apiKey: process.env.BRAINTRUST_API_KEY!,
      baseURL: "https://braintrustproxy.com/v1",
    },
  );

  // Access the underlying `ws.WebSocket` instance
  rt.socket.addEventListener("open", () => {
    console.log("Connection opened!");

    // Configure the session
    rt.send({
      type: "session.update",
      session: {
        output_modalities: ["text"], // or ["audio"]
        model: "gpt-realtime",
        type: "realtime",
      },
    });

    rt.send({
      type: "conversation.item.create",
      item: {
        type: "message",
        role: "user",
        content: [{ type: "input_text", text: "Say a couple paragraphs!" }],
      },
    });

    rt.send({ type: "response.create" });
  });

  // Handle errors
  rt.on("error", (err) => {
    console.error("Error:", err);
  });

  // Listen to events
  rt.on("response.output_text.delta", (event) => {
    process.stdout.write(event.delta);
  });

  rt.on("response.done", () => rt.close());

  rt.socket.addEventListener("close", () => {
    console.log("\nConnection closed!");
  });
  ```
</CodeGroup>

##### Log realtime sessions

To log realtime sessions to Braintrust, pass the `x-bt-parent` header when creating the connection. You must use a `BRAINTRUST_API_KEY` to enable logging:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAIRealtimeWS } from "openai/realtime/ws";
  import { initLogger } from "braintrust";

  async function main() {
    const logger = initLogger({ projectName: "My Realtime Project" });

    const rt = new OpenAIRealtimeWS(
      {
        model: "gpt-realtime",
        options: {
          headers: {
            "x-bt-parent": `project_id:${(await logger.project).id}`,
          },
        },
      },
      {
        apiKey: process.env.BRAINTRUST_API_KEY!,
        baseURL: "https://braintrustproxy.com/v1",
      },
    );

    rt.socket.addEventListener("open", () => {
      console.log("Connection opened!");

      // Configure the session
      rt.send({
        type: "session.update",
        session: {
          output_modalities: ["text"], // or ["audio"]
          model: "gpt-realtime",
          type: "realtime",
        },
      });

      // Send a message
      rt.send({
        type: "conversation.item.create",
        item: {
          type: "message",
          role: "user",
          content: [{ type: "input_text", text: "Say hello!" }],
        },
      });

      rt.send({ type: "response.create" });
    });

    // Handle errors
    rt.on("error", (err) => {
      console.error("Error:", err);
    });

    // Listen to text output
    rt.on("response.output_text.delta", (event) =>
      process.stdout.write(event.delta),
    );

    rt.on("response.done", () => rt.close());

    rt.socket.addEventListener("close", () => {
      console.log("\nConnection closed!");
    });
  }

  main();
  ```
</CodeGroup>

The proxy automatically logs audio, transcripts, and metadata to the specified project. Pass an experiment ID or span slug to log to a specific location.

The OpenAI Realtime API uses different event names for output depending on the modality:

* Text output: `response.output_text.delta` and `response.output_text.done`
* Audio output: `response.output_audio.delta` and `response.output_audio.done`
* Audio transcripts: `response.output_audio_transcript.delta` and `response.output_audio_transcript.done`

##### Compress audio

To reduce storage costs, enable audio compression by setting the `x-bt-compress-audio` header to `true` or `1`:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAIRealtimeWS } from "openai/realtime/ws";

  async function main() {
    const projectId = "your-project-id";

    const rt = new OpenAIRealtimeWS(
      {
        model: "gpt-realtime",
        options: {
          headers: {
            "x-bt-parent": `project_id:${projectId}`,
            "x-bt-compress-audio": "true", // Enable audio compression
          },
        },
      },
      {
        apiKey: process.env.BRAINTRUST_API_KEY!,
        baseURL: "https://braintrustproxy.com/v1",
      },
    );
  }

  main();
  ```
</CodeGroup>

When enabled, the proxy compresses audio using MP3 encoding before logging it to Braintrust to significantly reduce storage requirements.

#### Browser or Cloudflare workers

For browser and Cloudflare Workers environments, use `OpenAIRealtimeWebSocket`:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAIRealtimeWebSocket } from "openai/realtime/websocket";

  const rt = new OpenAIRealtimeWebSocket(
    {
      model: "gpt-realtime",
    },
    {
      apiKey: process.env.BRAINTRUST_API_KEY!,
      baseURL: "https://braintrustproxy.com/v1",
    },
  );

  // Access the underlying WebSocket instance
  rt.socket.addEventListener("open", () => {
    console.log("Connection opened!");

    // Configure the session
    rt.send({
      type: "session.update",
      session: {
        output_modalities: ["text"], // or ["audio"]
        model: "gpt-realtime",
        type: "realtime",
      },
    });

    // Send a message
    rt.send({
      type: "conversation.item.create",
      item: {
        type: "message",
        role: "user",
        content: [{ type: "input_text", text: "Say a couple paragraphs!" }],
      },
    });

    // Request a response
    rt.send({ type: "response.create" });
  });

  // Handle errors
  rt.on("error", (err) => {
    console.error("Error:", err);
  });

  // Listen to events
  rt.on("response.output_text.delta", (event) => {
    console.log(event.delta);
  });

  rt.on("response.done", () => rt.close());

  rt.socket.addEventListener("close", () => {
    console.log("\nConnection closed!");
  });
  ```
</CodeGroup>

##### Temporary credentials

For frontend or mobile applications, use [temporary credentials](#temporary-credentials-for-end-user-access) to avoid exposing your API key. Pass the temporary credential as the `apiKey`:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAIRealtimeWebSocket } from "openai/realtime/websocket";

  async function main() {
    // Get temporary credential from your backend
    const tempCredential = await fetchTempCredentialFromBackend();

    const rt = new OpenAIRealtimeWebSocket(
      {
        model: "gpt-realtime",
      },
      {
        apiKey: tempCredential,
        baseURL: "https://braintrustproxy.com/v1",
      },
    );

    rt.socket.addEventListener("open", () => {
      console.log("Connection opened!");

      // Configure the session
      rt.send({
        type: "session.update",
        session: {
          output_modalities: ["text"], // or ["audio"]
          model: "gpt-realtime",
          type: "realtime",
        },
      });

      // Send a message
      rt.send({
        type: "conversation.item.create",
        item: {
          type: "message",
          role: "user",
          content: [{ type: "input_text", text: "Say hello!" }],
        },
      });

      rt.send({ type: "response.create" });
    });

    // Handle errors
    rt.on("error", (err) => {
      console.error("Error:", err);
    });

    // Listen to events
    rt.on("response.output_text.delta", (event) => {
      console.log(event.delta);
    });

    rt.on("response.done", () => rt.close());

    rt.socket.addEventListener("close", () => {
      console.log("\nConnection closed!");
    });
  }

  declare function fetchTempCredentialFromBackend(): Promise<string>;

  main();
  ```
</CodeGroup>

### Authorization

The proxy allows you to use either a provider's API key or your Braintrust
API key.

If you use a provider's API key, use the proxy without a
Braintrust account to take advantage of low-latency edge caching (scoped to your
API key).

#### Using Braintrust API keys

Use a Braintrust API key to access multiple model providers through
the proxy and manage all your API keys in one place. [Sign up for a Braintrust account](https://www.braintrust.dev/signup) and add each provider's API key on the
[AI providers](https://www.braintrust.dev/app/settings?subroute=secrets) page in your settings. Then create
an [API key](https://www.braintrust.dev/app/settings?subroute=api-keys) to use in your requests.

The proxy response returns the `x-bt-used-endpoint` header, which specifies
which of your configured providers was used to complete the request.

![Secret configuration](https://www.braintrust.dev/blog/img/secret-config.png)

#### Custom models

If you have custom models as part of your OpenAI or other accounts, add a custom provider to use them with the proxy. For example, if you have a
custom model called `gpt-3.5-acme`, add it to your
[organization settings](https://www.braintrust.dev/docs/reference/organizations#custom-ai-providers) by navigating to
**Settings** > **Organization** > **AI providers**:

<img src="https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=0d1b7607bdf5536b75e97be19278a912" className="box-content" alt="Add provider dialog in Braintrust" data-og-width="4146" width="4146" data-og-height="3054" height="3054" data-path="images/guides/traces/trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?w=280&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=19f4c1bd01265dc56b53044a069eea28 280w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?w=560&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=27a3148ed8c298bbd7323cb6cf7c1930 560w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?w=840&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=ac9e22c98152cada01437f56b06e5233 840w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?w=1100&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=2ee489a6dc1f282d4d164e1af27fc9de 1100w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?w=1650&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=95429ed64c90e811151c3fe7d70f37d1 1650w, https://mintcdn.com/braintrust/vRnsqWnu5sp0FN9X/images/guides/traces/trace.png?w=2500&fit=max&auto=format&n=vRnsqWnu5sp0FN9X&q=85&s=73c4e519960e3d829406acff196ff0a5 2500w" />

Any headers you add to the configuration will be passed through in the request to the custom endpoint.
The values of the headers can also be templated using Mustache syntax.
Currently, the supported template variables are `{{email}}` and `{{model}}`.
which will be replaced with the email of the user whom the Braintrust API key belongs to and the model name, respectively.

If the endpoint is non-streaming, set the `Endpoint supports streaming` flag to false. The proxy will
convert the response to streaming format, allowing the models to work in the playground.

Each custom model must have a flavor (`chat` or `completion`) and format (`openai`, `anthropic`, `google`, `window` or `js`). Additionally, they can
optionally have a boolean flag if the model is multimodal and an input cost and output cost, which will only be used to calculate and display estimated
prices for experiment runs.

#### Specify an org

If you are part of multiple organizations, specify which organization to use by passing the `x-bt-org-name`
header in the SDK:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    defaultHeaders: {
      "x-bt-org-name": "Acme Inc",
    },
    apiKey: process.env.OPENAI_API_KEY, // Can use Braintrust, Anthropic, etc. API keys here
  });

  async function main() {
    const response = await client.chat.completions.create({
      model: "gpt-4o", // Can use claude-3-5-sonnet-latest, gemini-2.5-flash, etc. here
      messages: [{ role: "user", content: "What is a proxy?" }],
    });
    console.log(response.choices[0].message.content);
  }

  main();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      default_headers={"x-bt-org-name": "Acme Inc"},
      api_key=os.environ["OPENAI_API_KEY"],  # Can use Braintrust, Anthropic, etc. API keys here
  )

  response = client.chat.completions.create(
      model="gpt-4o",  # Can use claude-3-5-sonnet-latest, gemini-2.5-flash, etc. here
      messages=[{"role": "user", "content": "What is a proxy?"}],
  )
  print(response.choices[0].message.content)
  ```

  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  time curl -i https://api.braintrust.dev/v1/proxy/chat/completions \
    -H "Content-Type: application/json" \
    -H "x-bt-org-name: Acme Inc" \
    -d '{
      "model": "gpt-4o",
      "messages": [
        {
          "role": "user",
          "content": "What is a proxy?"
        }
      ]
    }' \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    --compress
  ```
</CodeGroup>

### Temporary credentials for end user access

A **temporary credential** converts your Braintrust API key (or model provider
API key) to a time-limited credential that can be safely shared with end users.

* Temporary credentials can also carry additional information to limit access to
  a particular model and/or enable logging to Braintrust.
* They can be used in the `Authorization` header anywhere you'd use a Braintrust
  API key or a model provider API key.

Use temporary credentials if you'd like your frontend or mobile app to send AI
requests to the proxy directly, minimizing latency without exposing your API
keys to end users.

#### Issue temporary credential in code

Call the [`/credentials` endpoint][cred-api-doc] from a privileged
location, such as your app's backend, to issue temporary credentials. The
temporary credential will be allowed to make requests on behalf of the
Braintrust API key (or model provider API key) provided in the `Authorization`
header.

The body should specify the restrictions to be applied to the temporary
credentials as a JSON object. Additionally, if the `logging` key is present, the
proxy will log to Braintrust any requests made with this temporary credential.
See the [`/credentials` API spec][cred-api-doc] for details.

The following example grants access to `gpt-4o-realtime-preview-2024-10-01` on
behalf of the key stored in the `BRAINTRUST_API_KEY` environment variable for 10
minutes, logging the requests to the project named "My project."

[cred-api-doc]: /docs/reference/api/Proxy#create-temporary-credential

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  const PROXY_URL =
    process.env.BRAINTRUST_PROXY_URL || "https://braintrustproxy.com/v1";
  // Braintrust API key starting with `sk-...`.
  const BRAINTRUST_API_KEY = process.env.BRAINTRUST_API_KEY;

  async function main() {
    const response = await fetch(`${PROXY_URL}/credentials`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${BRAINTRUST_API_KEY}`,
      },
      body: JSON.stringify({
        // Leave undefined to allow all models.
        model: "gpt-4o-realtime-preview-2024-10-01",
        // TTL for starting the request. Once started, the request can stream
        // for as long as needed.
        ttl_seconds: 60 * 10, // 10 minutes.
        logging: {
          project_name: "My project",
        },
      }),
      cache: "no-store",
    });

    if (!response.ok) {
      const error = await response.text();
      throw new Error(`Failed to request temporary credentials: ${error}`);
    }

    const { key: tempCredential } = await response.json();
    console.log(`Authorization: Bearer ${tempCredential}`);
  }

  main();
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  import requests

  PROXY_URL = os.getenv("BRAINTRUST_PROXY_URL", "https://braintrustproxy.com/v1")
  # Braintrust API key starting with `sk-...`.
  BRAINTRUST_API_KEY = os.getenv("BRAINTRUST_API_KEY")

  def main():
      response = requests.post(
          f"{PROXY_URL}/credentials",
          headers={
              "Authorization": f"Bearer {BRAINTRUST_API_KEY}",
          },
          json={
              # Leave unset to allow all models.
              "model": "gpt-4o-realtime-preview-2024-10-01",
              # TTL for starting the request. Once started, the request can stream
              # for as long as needed.
              "ttl_seconds": 60 * 10,  # 10 minutes.
              "logging": {
                  "project_name": "My project",
              },
          },
      )

      if response.status_code != 200:
          raise Exception(f"Failed to request temporary credentials: {response.text}")

      temp_credential = response.json().get("key")
      print(f"Authorization: Bearer {temp_credential}")

  if __name__ == "__main__":
      main()
  ```

  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  curl -X POST "${BRAINTRUST_PROXY_URL:-https://api.braintrust.dev/v1/proxy}/credentials" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${BRAINTRUST_API_KEY}" \
    --data '{
      "model": "gpt-4o-realtime-preview-2024-10-01",
      "ttl_seconds": 600,
      "logging": {
        "project_name": "My project"
      }
    }'
  ```
</CodeGroup>

#### Issue temporary credential in browser

Generate a temporary credential using [this form](https://www.braintrust.dev/blog/realtime-api#generate-temporary-credentials).

#### Inspect temporary credential grants

The temporary credential is formatted as a [JSON Web Token (JWT)][jwt-intro].
Inspect the JWT's payload using a library such as
[`jsonwebtoken`][jwt-lib] or a web-based tool like [JWT.io](https://jwt.io/) to
determine the expiration time and granted models.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { decode as jwtDecode } from "jsonwebtoken";

  const tempCredential = "<your temporary credential>";
  const payload = jwtDecode(tempCredential, { complete: false, json: true });
  // Example output:
  // {
  //   "aud": "braintrust_proxy",
  //   "bt": {
  //     "model": "gpt-4o",
  //     "secret": "nCCxgkBoyy/zyOJlikuHILBMoK78bHFosEzy03SjJF0=",
  //     "logging": {
  //       "project_name": "My project"
  //     }
  //   },
  //   "exp": 1729928077,
  //   "iat": 1729927977,
  //   "iss": "braintrust_proxy",
  //   "jti": "bt_tmp:331278af-937c-4f97-9d42-42c83631001a"
  // }
  console.log(JSON.stringify(payload, null, 2));
  ```
</CodeGroup>

<Note>
  Do not modify the JWT payload. This will invalidate the signature. Instead,
  issue a new temporary credential using the `/credentials` endpoint.
</Note>

[jwt-intro]: https://jwt.io/introduction

[jwt-lib]: https://www.npmjs.com/package/jsonwebtoken

### Load balancing

If you have multiple API keys for a given model type, e.g. OpenAI and Azure for `gpt-4o`, the proxy will
automatically load balance across them. This is a useful way to work around per-account rate limits and provide
resiliency in case one provider is down.

Set up endpoints directly on the [secrets page](https://www.braintrust.dev/app/settings?subroute=secrets) in your Braintrust account
by adding endpoints:

![Configure secrets](https://www.braintrust.dev/blog/img/secrets-endpoint-config.gif)

### PDF input

The proxy extends the OpenAI API to support PDF input.
To use it, pass the PDF's URL or base64-encoded PDF data with MIME type `application/pdf` in the request body.
For example,

<CodeGroup dropdown>
  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  curl https://api.braintrust.dev/v1/proxy/auto \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $BRAINTRUST_API_KEY" \
    -d '{
      "model": "gpt-4o",
      "messages": [
        {"role": "user", "content": [
          {
            "type": "text",
            "text": "Extract the text from the PDF."
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://example.com/my-pdf.pdf"
            }
          }
        ]},
      ]
    }'
  ```
</CodeGroup>

or

<CodeGroup dropdown>
  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  curl https://api.braintrust.dev/v1/proxy/auto \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $BRAINTRUST_API_KEY" \
    -d '{
      "model": "gpt-4o",
      "messages": [
        {"role": "user", "content": [
          {
            "type": "text",
            "text": "Extract the text from the PDF."
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "data:application/pdf;base64,$PDF_BASE64_DATA"
            }
          }
        ]},
      ]
    }'
  ```
</CodeGroup>

## Advanced configuration

The following headers allow you to configure the proxy's behavior:

* `x-bt-use-cache`: `auto | always | never`. See [Caching](#caching)
* `x-bt-use-creds-cache`: `auto | always | never`. Similar to `x-bt-use-cache`, but controls whether to cache the
  credentials used to access the provider's API. This is useful if you are rapidly tweaking credentials and don't
  want to wait \~60 seconds for the credentials cache to expire.
* `x-bt-org-name`: Specify if you are part of multiple organizations and want to use API keys/log to a specific org.
* `x-bt-endpoint-name`: Specify to use a particular endpoint (by its name).
* `x-bt-parent`: Specify a project, experiment, or span to log traces to. See [Tracing](#tracing).
* `x-bt-compress-audio`: `true | false | 1 | 0`. Enable audio compression for realtime API sessions to reduce storage costs. See [WebSocket-based models](#websocket-based-models).

## Integration with Braintrust platform

Several features in Braintrust are powered by the proxy. For example, when you create a [playground](/core/playground),
the proxy handles running the LLM calls. Similarly, if you [create a prompt](/core/functions/prompts), when you preview the
prompt's results, the proxy is used to run the LLM. However, the proxy is *not* required when you:

* Run evals in your code
* Load prompts to run in your code
* Log traces to Braintrust

If you'd like to use it in your code to help with caching, secrets management, and other features, follow the [instructions
above](#quickstart) to set it as the base URL in your OpenAI client.

### Self-hosting

If you're self-hosting Braintrust, your API service (serverless functions or containers) contain a built-in proxy that runs
within your own environment. See the [self-hosting](/guides/self-hosting) docs for more information on how to set up
self-hosting.

## Open source

The AI proxy is open source. Find the code on
[GitHub](https://github.com/braintrustdata/braintrust-proxy).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt