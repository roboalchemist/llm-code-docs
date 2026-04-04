# Source: https://docs.apify.com/platform/integrations/mastra.md

# Mastra MCP integration

**Learn how to build AI agents with Mastra and Apify Actors MCP Server.**

***

## What is Mastra

[Mastra](https://mastra.ai) is an open-source TypeScript framework for building AI applications efficiently. It provides essential tools like agents, workflows, retrieval-augmented generation (RAG), integrations, and evaluations. Supporting any LLM (e.g., GPT-4, Claude, Gemini). You can run it locally or deploy it to a serverless cloud like [Apify](https://apify.com).

Explore Mastra

Check out the [Mastra docs](https://mastra.ai/docs) for more information.

## What is MCP server

A [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server exposes specific data sources or tools to agents via a standardized protocol. It acts as a bridge, connecting large language models (LLMs) to external systems like databases, APIs, or local filesystems. Built on a client-server architecture, MCP servers enable secure, real-time interaction, allowing agents to fetch context or execute actions without custom integrations. Think of it as a modular plugin system for agents, simplifying how they access and process data. Apify provides [Actors MCP Server](https://mcp.apify.com/) to expose [Apify Actors](https://docs.apify.com/platform/actors) from the [Apify Store](https://apify.com/store) as tools via the MCP protocol.

## How to use Apify with Mastra via MCP

This guide demonstrates how to integrate Apify Actors with Mastra by building an agent that uses the [RAG Web Browser](https://apify.com/apify/rag-web-browser) Actor to search Google for TikTok profiles and the [TikTok Data Extractor](https://apify.com/clockworks/free-tiktok-scraper) Actor to extract and analyze data from the TikTok profiles via MCP.

### Prerequisites

* *Apify API token*: To use Apify Actors, you need an Apify API token. Learn how to obtain it in the [Apify documentation](https://docs.apify.com/platform/integrations/api).

* *LLM provider API key*: To power the agents, you need an LLM provider API key. For example, get one from the [OpenAI](https://platform.openai.com/account/api-keys) or [Anthropic](https://console.anthropic.com/settings/keys).

* *Node.js*: Ensure you have Node.js installed.

* *Packages*: Install the following packages:


  ```
  npm install @mastra/core @mastra/mcp @ai-sdk/openai
  ```


### Building the TikTok profile search and analysis agent

First, import all required packages:


```
import { Agent } from '@mastra/core/agent';
import { MastraMCPClient } from '@mastra/mcp';
import { openai } from '@ai-sdk/openai';
// For Anthropic use
// import { anthropic } from '@ai-sdk/anthropic';
```


Next, set the environment variables for the Apify API token and OpenAI API key:


```
process.env.APIFY_TOKEN = "your-apify-token";
process.env.OPENAI_API_KEY = "your-openai-api-key";
// For Anthropic use
// process.env.ANTHROPIC_API_KEY = "your-anthropic-api-key";
```


Instantiate the Mastra MCP client:


```
const mcpClient = new MastraMCPClient({
    name: 'apify-client',
    server: {
        url: new URL('https://mcp.apify.com/sse'),
        requestInit: {
            headers: { Authorization: `Bearer ${process.env.APIFY_TOKEN}` }
        },
        // The EventSource package augments EventSourceInit with a "fetch" parameter.
        // You can use this to set additional headers on the outgoing request.
        // Based on this example: https://github.com/modelcontextprotocol/typescript-sdk/issues/118
        eventSourceInit: {
            async fetch(input: Request | URL | string, init?: RequestInit) {
                const headers = new Headers(init?.headers || {});
                headers.set('authorization', `Bearer ${process.env.APIFY_TOKEN}`);
                return fetch(input, { ...init, headers });
            }
        }
    },
    timeout: 300_000, // 5 minutes tool call timeout
});
```


Connect to the MCP server and fetch the tools:


```
console.log('Connecting to Mastra MCP server...');
await mcpClient.connect();
console.log('Fetching tools...');
const tools = await mcpClient.tools();
```


Instantiate the agent with the OpenAI model:


```
const agent = new Agent({
    name: 'Social Media Agent',
    instructions: 'You’re a social media data extractor. Find TikTok URLs and analyze profiles with precision.',
    // You can swap to any other AI-SDK LLM provider
    model: openai('gpt-4o-mini')
});
```


Generate a response using the agent and the Apify tools:


```
const prompt = 'Search the web for the OpenAI TikTok profile URL, then extract and summarize its data.';
console.log(`Generating response for prompt: ${prompt}`);
const response = await agent.generate(prompt, {
    toolsets: { apify: tools }
});
```


Print the response and disconnect from the MCP server:


```
console.log(response.text);
await mcpClient.disconnect();
```


Use any Apify Actor

Since it uses the [Apify MCP Server](https://mcp.apify.com), swap in any Apify Actor from the [Apify Store](https://apify.com/store) by updating the startup request’s `actors` parameter. No other changes are needed in the agent code.

Run the agent:


```
npx tsx mastra-agent.ts
```


Search and analysis may take some time

The agent's execution may take some time as it searches the web for the OpenAI TikTok profile and extracts data from it.

You will see the agent’s output in the console, showing the results of the search and analysis.


```
Connecting to Mastra MCP server...
Fetching tools...
Generating response for prompt: Search the web for the OpenAI TikTok profile URL, then extract and summarize its data.
### OpenAI TikTok Profile Summary
- **Profile URL**: [OpenAI on TikTok](https://www.tiktok.com/@openai?lang=en)              - **Followers**: 608,100
- **Likes**: 3.4 million
- **Videos Posted**: 156
- **Bio**: "low key research previews"
...
```


If you want to test the whole example, create a new file, `mastra-agent.ts`, and copy the full code into it:


```
import { Agent } from '@mastra/core/agent';
import { MastraMCPClient } from '@mastra/mcp';
import { openai } from '@ai-sdk/openai';
// For Anthropic use
// import { anthropic } from '@ai-sdk/anthropic';

process.env.APIFY_TOKEN = "your-apify-token";
process.env.OPENAI_API_KEY = "your-openai-api-key";
// For Anthropic use
// process.env.ANTHROPIC_API_KEY = "your-anthropic-api-key";

const mcpClient = new MastraMCPClient({
    name: 'apify-client',
    server: {
        url: new URL('https://mcp.apify.com/sse'),
        requestInit: {
            headers: { Authorization: `Bearer ${process.env.APIFY_TOKEN}` }
        },
        // The EventSource package augments EventSourceInit with a "fetch" parameter.
        // You can use this to set additional headers on the outgoing request.
        // Based on this example: https://github.com/modelcontextprotocol/typescript-sdk/issues/118
        eventSourceInit: {
            async fetch(input: Request | URL | string, init?: RequestInit) {
            const headers = new Headers(init?.headers || {});
            headers.set('authorization', `Bearer ${process.env.APIFY_TOKEN}`);
            return fetch(input, { ...init, headers });
            }
        }
    },
    timeout: 300_000, // 5 minutes tool call timeout
});

console.log('Connecting to Mastra MCP server...');
await mcpClient.connect();
console.log('Fetching tools...');
const tools = await mcpClient.tools();

const agent = new Agent({
    name: 'Social Media Agent',
    instructions: 'You’re a social media data extractor. Find TikTok URLs and analyze profiles with precision.',
    // You can swap to any other AI-SDK LLM provider
    model: openai('gpt-4o-mini')
});

const prompt = 'Search the web for the OpenAI TikTok profile URL, then extract and summarize its data.';
console.log(`Generating response for prompt: ${prompt}`);
const response = await agent.generate(prompt, {
    toolsets: { apify: tools }
});

console.log(response.text);
await mcpClient.disconnect();
```


## Resources

* [Apify Actors](https://docs.apify.com/platform/actors)
* [Mastra Documentation](https://mastra.ai/docs)
* [Apify MCP Server](https://mcp.apify.com)
* [How to use MCP with Apify Actors](https://blog.apify.com/how-to-use-mcp/)
* [Apify Store](https://apify.com/store)
* [What are AI Agents?](https://blog.apify.com/what-are-ai-agents/)
* [How to Build an AI Agent](https://blog.apify.com/how-to-build-an-ai-agent/)
