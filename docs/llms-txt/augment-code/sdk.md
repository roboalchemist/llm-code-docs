# Source: https://docs.augmentcode.com/cli/sdk.md

# Auggie SDK

> Build custom integrations and agents using the Auggie SDK.

<CardGroup cols={2}>
  <Card title="TypeScript SDK" icon="js" href="/cli/sdk-typescript">
    Build Node.js and TypeScript applications with the Auggie SDK
  </Card>

  <Card title="Python SDK" icon="python" href="/cli/sdk-python">
    Build Python applications with the Auggie SDK
  </Card>
</CardGroup>

## Installation

<CodeGroup>
  ```sh TypeScript theme={null}
  npm install @augmentcode/auggie-sdk
  ```

  ```sh Python theme={null}
  pip install auggie-sdk
  ```
</CodeGroup>

## Authentication

The Auggie SDK supports multiple authentication methods:

1. **Passing API Key Directly (Recommended)** - Provide `apiKey` parameter when initializing
2. **Using Environment Variables** - Set `AUGMENT_API_TOKEN` and `AUGMENT_API_URL` environment variables
3. **Using `settings.json`** - Store credentials in `settings.json` file

### Finding Your API keys

<Note>
  **Coming Soon:** Service accounts and team-level tokens will be available for production deployments and CI/CD environments.
</Note>

Running `auggie token print` will print your API keys:

```json  theme={null}
{
  "accessToken": "ABC-XYZ-123", // Use as apiKey
  "tenantURL": "https://...",   // Use as apiUrl
  ...
}
```

## Quick Start

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { Auggie } from "@augmentcode/auggie-sdk";

  const client = await Auggie.create({ model: "sonnet4.5" });
  const response = await client.prompt("What files are in the current directory?");
  console.log(response);
  await client.close();
  ```

  ```python Python theme={null}
  from auggie_sdk import Auggie

  agent = Auggie(model="sonnet4.5")
  result = agent.run("What is 2 + 2?", return_type=int)
  print(result)  # 4
  ```
</CodeGroup>

## Key Features

Both SDKs provide:

* **High-level API** - Simple interface for common tasks
* **Multiple Output Modes** - String responses, typed returns, streaming, and more
* **Codebase Awareness** - Automatic indexing and context from your workspace
* **Custom Tools** - Extend Auggie with your own tools and integrations
