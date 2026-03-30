# Source: https://pipedream.com/docs/connect/mcp/ai-frameworks/anthropic.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pipedream MCP with Anthropic

> Use Pipedream MCP with Anthropic's MCP connectors

<Note>
  Make sure to complete the [setup steps](/connect/mcp/developers#prerequisites) before continuing.
</Note>

## Installation

<CodeGroup>
  ```bash TypeScript/JavaScript theme={null}
  npm install @anthropic-ai/sdk @pipedream/sdk
  ```

  ```bash Python theme={null}
  pip install anthropic pipedream
  ```

</CodeGroup>

Set your Anthropic API key:

```env  theme={null}
ANTHROPIC_API_KEY=your_anthropic_api_key
```

## Basic Usage

Claude's MCP connector connects directly to Pipedream's remote MCP server through the Messages API:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { Anthropic } from '@anthropic-ai/sdk';
  import { PipedreamClient } from '@pipedream/sdk';

  // Environment variables
  const ANTHROPIC_API_KEY = process.env.ANTHROPIC_API_KEY!;
  const PIPEDREAM_CLIENT_ID = process.env.PIPEDREAM_CLIENT_ID!;
  const PIPEDREAM_CLIENT_SECRET = process.env.PIPEDREAM_CLIENT_SECRET!;
  const PIPEDREAM_PROJECT_ID = process.env.PIPEDREAM_PROJECT_ID!;
  const PIPEDREAM_ENVIRONMENT = process.env.PIPEDREAM_ENVIRONMENT as 'development' | 'production';

  async function runClaudeWithMCP() {
    // Initialize Pipedream SDK client
    const pd = new PipedreamClient({
      projectEnvironment: PIPEDREAM_ENVIRONMENT,
      clientId: PIPEDREAM_CLIENT_ID,
      clientSecret: PIPEDREAM_CLIENT_SECRET,
      projectId: PIPEDREAM_PROJECT_ID
    });

    // Get access token for MCP authentication
    const accessToken = await pd.rawAccessToken;
    const externalUserId = 'user-123'; // Your user's unique ID
    const appSlug = 'notion'; // App to use

    // Initialize Anthropic client
    const anthropic = new Anthropic({
      apiKey: ANTHROPIC_API_KEY,
    });
    const serverUrl = `https://remote.mcp.pipedream.net?projectId=${PIPEDREAM_PROJECT_ID}&environment=${PIPEDREAM_ENVIRONMENT}&externalUserId=${externalUserId}&app=${appSlug}`;

    const response = await anthropic.beta.messages.create({
      model: "claude-sonnet-4-20250514",
      max_tokens: 1000,
      messages: [
        {
          role: "user",
          content: "Find my most recent Notion page and summarize it",
        },
      ],
      mcp_servers: [
        {
          type: "url",
          url: serverUrl,
          name: "pipedream",
          authorization_token: accessToken,
        },
      ],
      betas: ["mcp-client-2025-04-04"],
    });

    console.log('Claude response:', response.content);
  }

  runClaudeWithMCP().catch(console.error);

  ```

  ```python Python theme={null}
  import anthropic
  import os
  from pipedream import Pipedream

  # Initialize Pipedream client
  pd = Pipedream(
      project_id=os.environ['PIPEDREAM_PROJECT_ID'],
      project_environment=os.environ['PIPEDREAM_ENVIRONMENT'],
      client_id=os.environ['PIPEDREAM_CLIENT_ID'],
      client_secret=os.environ['PIPEDREAM_CLIENT_SECRET'],
  )

  # Get access token
  access_token = await pd.raw_access_token
  external_user_id = 'user-123'
  app_slug = 'notion'

  # Initialize Anthropic client
  client = anthropic.Anthropic(
      api_key=os.environ['ANTHROPIC_API_KEY']
  )

  project_id = os.environ['PIPEDREAM_PROJECT_ID']
  environment = os.environ['PIPEDREAM_ENVIRONMENT']
  server_url = f"https://remote.mcp.pipedream.net?projectId={project_id}&environment={environment}&externalUserId={external_user_id}&app={app_slug}"

  response = client.beta.messages.create(
      model="claude-sonnet-4-20250514",
      max_tokens=1000,
      messages=[{
          "role": "user",
          "content": "Find my most recent Notion page and summarize it"
      }],
      mcp_servers=[{
          "type": "url",
          "url": server_url,
          "name": "pipedream",
          "authorization_token": access_token,
      }],
      betas=["mcp-client-2025-04-04"]
  )

  print("Claude response:", response.content)
  ```

</CodeGroup>

Built with [Mintlify](https://mintlify.com).
