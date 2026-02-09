# Source: https://docs.lunary.ai/docs/integrations/python/installation.md

# Source: https://docs.lunary.ai/docs/integrations/javascript/installation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# JavaScript SDK

## Installation

The `lunary` module is lightweight and works with Node JS, Deno, Cloudflare Workers, Vercel Edge functions and even Bun.

### Node

```bash  theme={null}
npm install lunary
```

<Warning>
  ### For Cloudflare Workers

  In your `wrangler.toml` file, make sure to add the Node.js compatibility flag:

  ```toml  theme={null}
  compatibility_flags = [ "nodejs_compat" ]
  ```
</Warning>

## Setup

Start by importing the `lunary` module:

```js  theme={null}
import lunary from "lunary";
```

If you're using in the browser, import like this:

```js  theme={null}
import lunary from "lunary/browser";
```

Then initialize the module with your unique app ID.

Option 1: Automatic using environment variables (recommended):

```bash  theme={null}
LUNARY_PUBLIC_KEY="0x0"
```

Option 2: Manually using the `.init` method:

```ts  theme={null}
// Initialize the Lunary module with your unique app ID
lunary.init({
  publicKey: "0x0",
});
```

The `.init` method accepts the following arguments:

```ts  theme={null}
{
  "appId": string, // Your unique app ID obtained from the dashboard
  "apiUrl": string, // Optional: Use a custom endpoint if you're self-hosting (you can also set LUNARY_API_URL)
  "verbose": boolean // Optional: Enable verbose logging for debugging
}
```

<CardGroup cols={2}>
  <Card title="LangChain" icon="box" href="/docs/integrations/langchain">
    Usage with LangChain JS.
  </Card>

  <Card title="OpenAI" icon="microchip-ai" href="/docs/integrations/javascript/openai">
    Automatically track your OpenAI calls.
  </Card>

  <Card title="User Tracking" icon="users" href="/docs/features/users">
    Identify your users.
  </Card>

  <Card title="Tagging" icon="tags" href="/docs/features/tags">
    Segment your queries with tags.
  </Card>

  <Card title="Chats" icon="messages" href="/docs/features/conversations">
    Record user interactions with your chatbot.
  </Card>

  <Card title="Manual Integration" icon="code" href="/docs/integrations/javascript/manual">
    Learn how to use .trackEvent().
  </Card>

  <Card title="Serverless" icon="lambda" href="/docs/integrations/javascript/serverless">
    Use with Lambda, Cloudflare Workers, Edge Functions, etc.
  </Card>

  <Card title="Agents & Tools" icon="robot" href="/docs/features/observability">
    Setup tracing by tracking agents & tools.
  </Card>

  <Card title="API Reference" icon="terminal" href="/docs/api/introduction">
    Full list of methods and classes.
  </Card>
</CardGroup>
