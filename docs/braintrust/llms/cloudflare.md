# Source: https://braintrust.dev/docs/integrations/sdk-integrations/cloudflare.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloudflare

> Trace AI requests through Cloudflare AI Gateway with Braintrust

[Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) provides a unified interface to access multiple AI providers with observability, caching, and rate limiting. Braintrust automatically traces requests through Cloudflare AI Gateway across all supported providers.

## Setup

Install the Braintrust SDK and OpenAI client:

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

Configure your environment variables:

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
OPENAI_API_KEY=<your-provider-api-key>
CLOUDFLARE_ACCOUNT_ID=<your-cloudflare-account-id>
CLOUDFLARE_AI_GATEWAY_NAME=<your-gateway-name>
BRAINTRUST_API_KEY=<your-braintrust-api-key>
```

## Trace with Cloudflare AI Gateway

Use `wrapOpenAI` to automatically trace requests through Cloudflare's unified API endpoint:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";
  import { initLogger, wrapOpenAI } from "braintrust";

  // Initialize Braintrust logging
  initLogger({
    projectName: "My Project",
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  // Create OpenAI client configured for Cloudflare AI Gateway
  const client = wrapOpenAI(
    new OpenAI({
      // OpenAI SDK automatically adds /chat/completions
      baseURL: `https://gateway.ai.cloudflare.com/v1/${process.env.CLOUDFLARE_ACCOUNT_ID}/${process.env.CLOUDFLARE_AI_GATEWAY_NAME}/compat`,
      apiKey: process.env.OPENAI_API_KEY,
    }),
  );

  // This request will be automatically traced by Braintrust
  const result = await client.chat.completions.create({
    model: "openai/gpt-4o",
    messages: [{ role: "user", content: "What is 1+1?" }],
  });

  console.log(result);
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  import openai
  from braintrust import init_logger, wrap_openai

  # Initialize Braintrust logging
  logger = init_logger(project="My Project")

  # Create OpenAI client configured for Cloudflare AI Gateway
  client = wrap_openai(
      # OpenAI client automatically adds /chat/completions
      openai.OpenAI(
          base_url=f"https://gateway.ai.cloudflare.com/v1/{os.getenv('CLOUDFLARE_ACCOUNT_ID')}/{os.getenv('CLOUDFLARE_AI_GATEWAY_NAME')}/compat",
          api_key=os.getenv("OPENAI_API_KEY"),
      )
  )

  # This request will be automatically traced by Braintrust
  result = client.chat.completions.create(
      model="openai/gpt-4o",
      messages=[{"role": "user", "content": "What is 1+1?"}],
  )

  print(result)
  ```
</CodeGroup>

## Switching providers

Cloudflare AI Gateway's unified API allows you to easily switch between different AI providers by changing the `model` parameter and corresponding API key. All requests are automatically traced by Braintrust regardless of which provider you use.

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";
  import { wrapOpenAI } from "braintrust";

  // Switch to Anthropic
  const client = wrapOpenAI(
    new OpenAI({
      baseURL: `https://gateway.ai.cloudflare.com/v1/${process.env.CLOUDFLARE_ACCOUNT_ID}/${process.env.CLOUDFLARE_AI_GATEWAY_NAME}/compat`,
      apiKey: process.env.ANTHROPIC_API_KEY, // Use Anthropic's API key
    }),
  );

  const result = await client.chat.completions.create({
    model: "anthropic/claude-sonnet-4-5-20250929", // Use Anthropic model
    messages: [{ role: "user", content: "Hello!" }],
  });
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os
  import openai
  from braintrust import wrap_openai

  # Switch to Anthropic
  client = wrap_openai(
      openai.OpenAI(
          base_url=f"https://gateway.ai.cloudflare.com/v1/{os.getenv('CLOUDFLARE_ACCOUNT_ID')}/{os.getenv('CLOUDFLARE_AI_GATEWAY_NAME')}/compat",
          api_key=os.getenv("ANTHROPIC_API_KEY"),  # Use Anthropic's API key
      )
  )

  result = client.chat.completions.create(
      model="anthropic/claude-sonnet-4-5-20250929",  # Use Anthropic model
      messages=[{"role": "user", "content": "Hello!"}],
  )
  ```
</CodeGroup>

Cloudflare AI Gateway supports OpenAI, Anthropic, Google AI Studio, Groq, Mistral, Cohere, Perplexity, DeepSeek, Cerebras, xAI, and Workers AI. See the [Cloudflare documentation](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) for the complete list.

## Resources

* [Cloudflare AI Gateway documentation](https://developers.cloudflare.com/ai-gateway/)
* [Supported providers](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/)
