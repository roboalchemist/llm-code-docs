# Source: https://braintrust.dev/docs/deploy/ai-proxy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use the AI Proxy

> Call any AI provider through a unified interface

The Braintrust AI Proxy provides unified access to models from OpenAI, Anthropic, Google, AWS, Mistral, and third-party providers through a single API. Point your OpenAI SDK to the proxy URL and immediately get automatic caching, observability, and multi-provider support.

## Set up the proxy

Change your base URL to `https://api.braintrust.dev/v1/proxy` and use any provider's model:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const response = await client.chat.completions.create({
    model: "claude-sonnet-4-5-20250929", // Any provider's model
    messages: [{ role: "user", content: "Hello!" }],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      api_key=os.getenv("BRAINTRUST_API_KEY"),
  )

  response = client.chat.completions.create(
      model="claude-sonnet-4-5-20250929",
      messages=[{"role": "user", "content": "Hello!"}],
  )
  ```

  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  curl https://api.braintrust.dev/v1/proxy/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $BRAINTRUST_API_KEY" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "messages": [{"role": "user", "content": "Hello!"}]
    }'
  ```
</CodeGroup>

The proxy supports over 100 models including GPT-5, Claude 4, Gemini 2.5, and Llama models through providers like Together AI and AWS Bedrock.

## Configure API keys

Add provider API keys in your [organization settings](/admin/organizations#configure-ai-providers) under **AI providers**, configure them at the [project level](/admin/projects#configure-ai-providers) to override organization defaults, or set them up inline when running playgrounds or prompts. Then use your Braintrust API key to access all providers through the proxy.

Project-level API keys take precedence over organization-level keys when making proxy requests in a project context. Use project-level keys to isolate API usage, manage separate billing, or use different credentials per project.

Without a Braintrust account, you can still use the proxy with individual provider API keys to get automatic caching.

## Enable caching

The proxy automatically caches responses to reduce costs and latency. Cached requests return in under 100ms from edge locations.

### Cache modes

Set the cache mode with the `x-bt-use-cache` header:

* **auto** (default): Caches when `temperature=0` or `seed` parameter is set
* **always**: Always caches supported endpoints
* **never**: Never reads or writes to cache

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    defaultHeaders: {
      "x-bt-use-cache": "always",
    },
    apiKey: process.env.BRAINTRUST_API_KEY,
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      default_headers={"x-bt-use-cache": "always"},
      api_key=os.getenv("BRAINTRUST_API_KEY"),
  )
  ```
</CodeGroup>

The response includes `x-bt-cached: HIT` or `MISS` to indicate cache status.

### Cache control

The proxy supports Cache-Control directives for fine-grained cache control:

* **no-cache, no-store**: Bypass cache completely (equivalent to `x-bt-use-cache: never`)
* **no-cache**: Force fresh request but cache the response for future requests
* **max-age=\<seconds>**: Request cached response with maximum age. Combine with `no-store` to bypass cache without overwriting it

The response includes:

* `x-bt-cached: HIT` or `MISS` - Whether response was served from cache
* `Age` - Age of the cached response in seconds
* `Cache-Control` with `max-age` - TTL/max age of cached response

### Cache encryption

Responses are encrypted with AES-GCM using a key derived from your API key. Only you can access your cached data. Cached results expire after 1 week by default. Configure TTL with the `x-bt-cache-ttl` header (max 7 days).

Cached results are scoped to individual users by default. Braintrust customers can opt into sharing cached results across users within their organization.

## Enable logging

Log all proxy requests to Braintrust by setting the `x-bt-parent` header:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    defaultHeaders: {
      "x-bt-parent": "project_id:YOUR_PROJECT_ID",
    },
    apiKey: process.env.BRAINTRUST_API_KEY, // Must use Braintrust API key
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      default_headers={"x-bt-parent": "project_id:YOUR_PROJECT_ID"},
      api_key=os.getenv("BRAINTRUST_API_KEY"),
  )
  ```
</CodeGroup>

The `x-bt-parent` header accepts:

* `project_id:...` - Log to a project
* `project_name:...` - Log to a project by name
* `experiment_id:...` - Log to an experiment
* Span slugs from `span.export()` - Nest under a specific span

Find your project ID in the project's **Configuration** page.

## Use reasoning models

The proxy standardizes reasoning across OpenAI, Anthropic, and Google models. Set `reasoning_effort` (low, medium, high) or `reasoning_budget` (token limit):

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";
  import "@braintrust/proxy/types";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const response = await client.chat.completions.create({
    model: "claude-sonnet-4-5-20250929",
    reasoning_effort: "medium",
    messages: [{ role: "user", content: "Solve this problem..." }],
  });

  // Access reasoning steps
  console.log(response.choices[0].reasoning);
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      api_key=os.getenv("BRAINTRUST_API_KEY"),
  )

  response = client.chat.completions.create(
      model="claude-sonnet-4-5-20250929",
      reasoning_effort="medium",
      messages=[{"role": "user", "content": "Solve this problem..."}],
  )

  # Access reasoning steps
  print(getattr(response.choices[0], "reasoning", None))
  ```
</CodeGroup>

Responses include a `reasoning` array with step-by-step thinking. See [Evaluate reasoning models](/evaluate/reasoning) for details.

## Use alternative protocols

The proxy translates OpenAI requests into various provider APIs automatically. You can also use native Anthropic and Gemini API schemas.

### Anthropic API

<CodeGroup dropdown>
  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  curl -X POST https://api.braintrust.dev/v1/proxy/anthropic/messages \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $BRAINTRUST_API_KEY" \
    -d '{
      "model": "claude-3-5-sonnet-20240620",
      "messages": [{"role": "user", "content": "What is a proxy?"}]
    }'
  ```
</CodeGroup>

The `anthropic-version` and `x-api-key` headers are not required.

### Gemini API

<CodeGroup dropdown>
  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  curl -X POST https://api.braintrust.dev/v1/proxy/google/models/gemini-2.5-flash:generateContent \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $BRAINTRUST_API_KEY" \
    -d '{
      "contents": [
        {
          "role": "user",
          "parts": [{"text": "What is a proxy?"}]
        }
      ]
    }'
  ```
</CodeGroup>

## Add custom providers

Add custom models or endpoints in your [organization settings](https://www.braintrust.dev/app/settings?subroute=secrets) under **Custom providers**. Custom endpoints support templated headers using `{{email}}` and `{{model}}`.

Configure the model's flavor (chat or completion), format (OpenAI, Anthropic, Google), and pricing to use it throughout Braintrust.

If the endpoint is non-streaming, disable the **This endpoint supports streaming** flag. The proxy will convert the response to streaming format for use in playgrounds.

## Load balance across providers

If you configure multiple API keys for the same model (e.g., OpenAI and Azure for GPT-4o), the proxy automatically load balances across them. This provides resilience and works around per-account rate limits.

## Use realtime models

The proxy supports the OpenAI Realtime API at the `/realtime` endpoint using WebSockets. Use `https://braintrustproxy.com/v1` (not `api.braintrust.dev`) for WebSocket connections.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAIRealtimeWS } from "openai/realtime/ws";

  const rt = new OpenAIRealtimeWS(
    {
      model: "gpt-realtime",
    },
    {
      apiKey: process.env.BRAINTRUST_API_KEY,
      baseURL: "https://braintrustproxy.com/v1",
    },
  );

  rt.socket.addEventListener("open", () => {
    console.log("Connected!");

    rt.send({
      type: "session.update",
      session: { output_modalities: ["text"], model: "gpt-realtime" },
    });

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

  rt.on("response.output_text.delta", (event) => {
    process.stdout.write(event.delta);
  });

  rt.on("response.done", () => rt.close());
  ```
</CodeGroup>

Enable logging by passing `x-bt-parent` in the connection options. Enable audio compression with `x-bt-compress-audio: true` to reduce storage costs.

## Create temporary credentials

Generate time-limited credentials for frontend or mobile apps to safely call the proxy without exposing your API key:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  const response = await fetch("https://braintrustproxy.com/v1/credentials", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${process.env.BRAINTRUST_API_KEY}`,
    },
    body: JSON.stringify({
      model: "gpt-4o", // Optional: restrict to specific model
      ttl_seconds: 600, // 10 minutes
      logging: {
        project_name: "My Project",
      },
    }),
  });

  const { key: tempCredential } = await response.json();
  // Pass tempCredential to frontend
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  import requests

  response = requests.post(
      "https://braintrustproxy.com/v1/credentials",
      headers={"Authorization": f"Bearer {os.getenv('BRAINTRUST_API_KEY')}"},
      json={
          "model": "gpt-4o",
          "ttl_seconds": 600,
          "logging": {"project_name": "My Project"},
      },
  )

  temp_credential = response.json()["key"]
  # Pass temp_credential to frontend
  ```
</CodeGroup>

Temporary credentials are JWT tokens that can be inspected to verify expiration and model grants. They work anywhere you'd use a Braintrust API key.

### Inspect temporary credentials

Temporary credentials are formatted as JSON Web Tokens (JWTs). Inspect the payload to determine expiration time and granted models:

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
  //     "logging": {"project_name": "My project"}
  //   },
  //   "exp": 1729928077,
  //   "iat": 1729927977
  // }
  console.log(JSON.stringify(payload, null, 2));
  ```
</CodeGroup>

Generate temporary credentials using the [web form](https://www.braintrust.dev/blog/realtime-api#generate-temporary-credentials) or programmatically via the API.

## Use PDF input

The proxy extends the OpenAI API to support PDF input. Pass PDF URLs or base64-encoded PDFs with MIME type `application/pdf`:

<CodeGroup dropdown>
  ```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  curl https://api.braintrust.dev/v1/proxy/auto \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $BRAINTRUST_API_KEY" \
    -d '{
      "model": "gpt-4o",
      "messages": [
        {"role": "user", "content": [
          {"type": "text", "text": "Extract the text from this PDF."},
          {"type": "image_url", "image_url": {"url": "https://example.com/document.pdf"}}
        ]}
      ]
    }'
  ```
</CodeGroup>

For base64-encoded PDFs, use `data:application/pdf;base64,<BASE64_DATA>` as the URL.

## Specify an organization

If you're part of multiple organizations, specify which to use with the `x-bt-org-name` header:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";

  const client = new OpenAI({
    baseURL: "https://api.braintrust.dev/v1/proxy",
    defaultHeaders: {
      "x-bt-org-name": "Acme Inc",
    },
    apiKey: process.env.BRAINTRUST_API_KEY,
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.braintrust.dev/v1/proxy",
      default_headers={"x-bt-org-name": "Acme Inc"},
      api_key=os.getenv("BRAINTRUST_API_KEY"),
  )
  ```
</CodeGroup>

## Advanced configuration

Configure proxy behavior with these headers:

* **x-bt-use-cache**: `auto | always | never` - Control caching behavior
* **x-bt-cache-ttl**: Seconds (max 604800) - Set cache TTL
* **x-bt-use-creds-cache**: `auto | always | never` - Control credentials caching (useful when rapidly updating credentials)
* **x-bt-org-name**: Organization name - Specify organization for multi-org users
* **x-bt-endpoint-name**: Endpoint name - Use a specific configured endpoint
* **x-bt-parent**: Project/experiment/span - Enable logging to Braintrust
* **x-bt-compress-audio**: `true | false` - Enable audio compression for realtime sessions

## Integration with Braintrust

The proxy powers several Braintrust features:

* **Playgrounds** use the proxy to run LLM calls
* **Prompt previews** use the proxy to show results
* **Online scoring** routes requests through the proxy

The proxy is not required when you run evaluations, load prompts in code, or log traces directly using the SDK.

## Self-hosting

Self-hosted Braintrust deployments include a built-in proxy that runs in your environment. See [Self-hosting](/admin/self-hosting) for details.

## Open source

The AI Proxy is open source. View the code on [GitHub](https://github.com/braintrustdata/braintrust-proxy).

## Next steps

* [Deploy prompts](/deploy/prompts) to call versioned prompts through the proxy
* [Evaluate reasoning models](/evaluate/reasoning) with standardized reasoning parameters
* [Monitor deployments](/deploy/monitor) to track production performance
* [Manage environments](/deploy/environments) to separate dev and production
