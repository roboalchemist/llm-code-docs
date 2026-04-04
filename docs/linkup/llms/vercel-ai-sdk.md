# Source: https://docs.linkup.so/pages/integrations/vercel-ai-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Vercel AI SDK

> How to use Linkup with the Vercel AI SDK

## Overview

Linkup can be used with the [Vercel AI SDK](https://sdk.vercel.ai/) as a tool for web search. This integration allows you to build AI applications that can access real-time information from the internet using any model supported by the AI SDK.

<Card title="GitHub Repository" icon="github" href="https://github.com/LinkupPlatform/linkup-ai-sdk" />

## Getting Started with Linkup in Vercel AI SDK

<Steps>
  <Step title="Install the Linkup AI SDK">
    ```bash  theme={null}
    npm install linkup-ai-sdk ai @ai-sdk/openai
    ```

    <Info>
      We have chosen OpenAI as the default model provider, but you can use any provider supported by the Vercel AI SDK (like `@ai-sdk/anthropic`, `@ai-sdk/mistral`, etc.)
    </Info>
  </Step>

  <Step title="Get your Linkup API Key">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Set up your environment variables">
    Create a `.env` file in your project root:

    ```bash  theme={null}
    LINKUP_API_KEY=your_linkup_api_key_here
    OPENAI_API_KEY=your_openai_api_key_here
    ```
  </Step>

  <Step title="Create and use the Linkup web search tool">
    ```typescript  theme={null}
    import { openai } from '@ai-sdk/openai';
    import { generateText, stepCountIs } from 'ai';
    import { webSearch } from 'linkup-ai-sdk';

    const { text } = await generateText({
      model: openai('gpt-4o-mini'),
      prompt: 'What was Microsoft's revenue last quarter and was it well perceived by the market?',
      tools: {
        webSearch: webSearch({ depth: 'standard' }),
      },
      stopWhen: stepCountIs(3),
    });

    console.log(text);
    ```
  </Step>
</Steps>

## Configuration Options

The `webSearch` tool accepts the following configuration options:

<table>
  <thead>
    <tr>
      <th style={{ color: '#FFFFFF' }}>Parameter</th>
      <th style={{ color: '#FFFFFF' }}>Type</th>
      <th style={{ color: '#FFFFFF' }}>Default</th>
      <th style={{ color: '#FFFFFF' }}>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>apiKey</code></td>
      <td><code>string</code></td>
      <td><code>process.env.LINKUP\_API\_KEY</code></td>
      <td>Your Linkup API key. If not provided, it will be read from the environment variable.</td>
    </tr>

    <tr>
      <td><code>depth</code></td>
      <td><code>'standard' | 'deep'</code></td>
      <td><code>'standard'</code></td>
      <td>Search depth. <code>deep</code> performs more thorough research, <code>standard</code> is faster.</td>
    </tr>

    <tr>
      <td><code>includeImages</code></td>
      <td><code>boolean</code></td>
      <td><code>false</code></td>
      <td>Whether to include images in the search results.</td>
    </tr>

    <tr>
      <td><code>includeDomains</code></td>
      <td><code>string\[]</code></td>
      <td><code>\[]</code></td>
      <td>Array of domains to include in the search results.</td>
    </tr>

    <tr>
      <td><code>excludeDomains</code></td>
      <td><code>string\[]</code></td>
      <td><code>\[]</code></td>
      <td>Array of domains to exclude from the search results.</td>
    </tr>

    <tr>
      <td><code>fromDate</code></td>
      <td><code>Date</code></td>
      <td><code>null</code></td>
      <td>Start date for filtering search results.</td>
    </tr>

    <tr>
      <td><code>toDate</code></td>
      <td><code>Date</code></td>
      <td><code>null</code></td>
      <td>End date for filtering search results.</td>
    </tr>
  </tbody>
</table>

For more details on search capabilities, see our [Search Concepts documentation](/pages/documentation/get-started/concepts).

## Resources

* [Linkup AI SDK on npm](https://www.npmjs.com/package/linkup-ai-sdk)
* [Linkup AI SDK on GitHub](https://github.com/LinkupPlatform/linkup-ai-sdk)
* [Vercel AI SDK Documentation](https://sdk.vercel.ai/)
* [Search Concepts](/pages/documentation/get-started/concepts)

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).