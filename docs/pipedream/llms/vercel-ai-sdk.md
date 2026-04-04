# Source: https://pipedream.com/docs/connect/mcp/ai-frameworks/vercel-ai-sdk.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pipedream MCP with Vercel's AI SDK

> Use Pipedream MCP with the Vercel AI SDK

<Note>
  Make sure to complete the [setup steps](/connect/mcp/developers#prerequisites) before continuing.
</Note>

<Card title="Try MCP Chat" icon="comments" href="https://chat.pipedream.com">
  Check out our open source chat app built with the AI SDK. Explore the code [here](https://github.com/PipedreamHQ/mcp-chat).
</Card>

## Installation

```bash  theme={null}
npm install ai @ai-sdk/openai @pipedream/sdk @modelcontextprotocol/sdk
```

## Basic Usage

Complete example showing Pipedream MCP with the Vercel AI SDK:

```typescript TypeScript theme={null}
import { openai } from '@ai-sdk/openai';
import { UIMessage, convertToModelMessages, experimental_createMCPClient, generateText, stepCountIs } from 'ai';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp';
import { PipedreamClient } from '@pipedream/sdk';

// Environment variables
const PIPEDREAM_CLIENT_ID = process.env.PIPEDREAM_CLIENT_ID!;
const PIPEDREAM_CLIENT_SECRET = process.env.PIPEDREAM_CLIENT_SECRET!;
const PIPEDREAM_PROJECT_ID = process.env.PIPEDREAM_PROJECT_ID!;
const PIPEDREAM_ENVIRONMENT = process.env.PIPEDREAM_ENVIRONMENT as 'development' | 'production';

async function runAIWithMCP() {
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
  const appSlug = 'notion'; // The app you want to use

  // Create MCP transport with authentication headers
  const transport = new StreamableHTTPClientTransport(
    new URL('https://remote.mcp.pipedream.net'),
    {
      requestInit: {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'x-pd-project-id': PIPEDREAM_PROJECT_ID,
          'x-pd-environment': PIPEDREAM_ENVIRONMENT,
          'x-pd-external-user-id': externalUserId,
          'x-pd-app-slug': appSlug,
        }
      }
    }
  );

  // Create MCP client using AI SDK
  const mcpClient = await experimental_createMCPClient({
    transport,
  });

  const messages: UIMessage[] = [
    {
      id: 'system-1',
      role: 'system',
      parts: [
        { type: 'text', text: 'You are a helpful assistant that can use Pipedream tools to help users with their tasks.' },
      ],
    },
    {
      id: 'user-1',
      role: 'user',
      parts: [
        { type: 'text', text: 'Find my most recent Notion page and summarize it for me' },
      ],
    },
  ];

  try {
    // Generate response with tools available from MCP
    const result = await generateText({
      model: openai('gpt-4'),
      // Convert UI messages (with parts) into model messages required by generateText
      messages: convertToModelMessages(messages),
      tools: await mcpClient.tools(), // Automatically loads all available tools
      stopWhen: stepCountIs(5), // Equivalent to allowing up to 5 tool-call steps
    });

    console.log('AI Response:', result.text);
    
    // Log any tool calls that were made
    if (result.toolCalls.length > 0) {
      console.log('\nTool calls made:');
      result.toolCalls.forEach((toolCall, index) => {
        console.log(`${index + 1}. ${toolCall.toolName}`);
        console.log(`   Input: ${JSON.stringify(toolCall.input, null, 2)}`);
      });
      
      console.log('\nTool results:');
      result.toolResults.forEach((toolResult, index) => {
        console.log(`${index + 1}. ${JSON.stringify(toolResult.output, null, 2)}`);
      });
    }
  } finally {
    // Clean up MCP client
    await mcpClient.close();
  }
}

// Run the example
runAIWithMCP().catch(console.error);
```

Built with [Mintlify](https://mintlify.com).
