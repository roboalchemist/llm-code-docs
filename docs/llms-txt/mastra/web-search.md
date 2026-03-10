# Source: https://mastra.ai/guides/guide/web-search

# Building an Agent that can search the web

When building a web search agent, you have two main strategies to consider:

1. **Native search tools from the LLM**: Certain language models offer integrated web search capabilities that work out of the box.
2. **Implement a custom search tool**: Develop your own integration with a search provider's API to handle queries and retrieve results.

## Prerequisites

- Node.js `v22.13.0` or later installed
- An API key from a supported [Model Provider](https://mastra.ai/models)
- An existing Mastra project (Follow the [installation guide](https://mastra.ai/guides/getting-started/quickstart) to set up a new project)

## Using native search tools

Some LLM providers include built-in web search capabilities that can be used directly without additional API integrations. OpenAI's GPT-4o-mini and Google's Gemini 2.5 Flash both offer native search tools that the model can invoke during generation.

1. Install dependencies

   **Open AI**:

   **npm**:

   ```bash
   npm install @ai-sdk/openai
   ```

   **pnpm**:

   ```bash
   pnpm add @ai-sdk/openai
   ```

   **Yarn**:

   ```bash
   yarn add @ai-sdk/openai
   ```

   **Bun**:

   ```bash
   bun add @ai-sdk/openai
   ```

   **Gemini**:

   ```bash
   npm install @ai-sdk/openai
   ```

   **Tab 3**:

   ```bash
   pnpm add @ai-sdk/openai
   ```

   **Tab 4**:

   ```bash
   yarn add @ai-sdk/openai
   ```

   **Tab 5**:

   ```bash
   bun add @ai-sdk/openai
   ```

   **Tab 6**:

   **npm**:

   ```bash
   npm install @ai-sdk/google
   ```

   **pnpm**:

   ```bash
   pnpm add @ai-sdk/google
   ```

   **Yarn**:

   ```bash
   yarn add @ai-sdk/google
   ```

   **Bun**:

   ```bash
   bun add @ai-sdk/google
   ```

   **Tab 7**:

   ```bash
   npm install @ai-sdk/google
   ```

   **Tab 8**:

   ```bash
   pnpm add @ai-sdk/google
   ```

   **Tab 9**:

   ```bash
   yarn add @ai-sdk/google
   ```

   **Tab 10**:

   ```bash
   bun add @ai-sdk/google
   ```

2. Create a new file `src/mastra/agents/searchAgent.ts` and define your agent:

   **Open AI**:

   ```ts
   import { Agent } from '@mastra/core/agent'

   export const searchAgent = new Agent({
     id: 'search-agent',
     name: 'Search Agent',
     instructions: 'You are a search agent that can search the web for information.',
     model: 'openai/gpt-5.1',
   })
   ```

   **Gemini**:

   ```ts
   import { Agent } from '@mastra/core/agent'

   export const searchAgent = new Agent({
     id: 'search-agent',
     name: 'Search Agent',
     instructions: 'You are a search agent that can search the web for information.',
     model: 'google/gemini-2.5-flash',
   })
   ```

3. Setup the tool:

   **Open AI**:

   ```ts
   import { openai } from '@ai-sdk/openai'
   import { Agent } from '@mastra/core/agent'

   export const searchAgent = new Agent({
     id: 'search-agent',
     name: 'Search Agent',
     instructions: 'You are a search agent that can search the web for information.',
     model: 'openai/gpt-5.1',
     tools: {
       webSearch: openai.tools.webSearch(),
     },
   })
   ```

   **Gemini**:

   ```ts
   import { google } from '@ai-sdk/google'
   import { Agent } from '@mastra/core/agent'

   export const searchAgent = new Agent({
     id: 'search-agent',
     name: 'Search Agent',
     instructions: 'You are a search agent that can search the web for information.',
     model: 'google/gemini-2.5-flash',
     tools: {
       webSearch: google.tools.googleSearch({
         mode: 'MODE_DYNAMIC',
       }),
     },
   })
   ```

4. In your `src/mastra/index.ts` file, register the agent:

   ```ts
   import { Mastra } from '@mastra/core'
   import { searchAgent } from './agents/searchAgent'

   export const mastra = new Mastra({
     agents: { searchAgent },
   })
   ```

5. You can test your agent with [Studio](https://mastra.ai/docs/getting-started/studio) using the `mastra dev` command:

   ```bash
   mastra dev
   ```

   Inside Studio navigate to the **"Search Agent"** and ask it: "What happened last week in AI news?"

## Using Search APIs

For more control over search behavior, you can integrate external search APIs as custom tools. [Exa](https://exa.ai/) is a search engine built specifically for AI applications, offering semantic search, configurable filters (category, domain, date range), and the ability to retrieve full page contents. The search API is wrapped in a Mastra tool that defines the input schema, output format, and execution logic.

1. Install dependencies

   **npm**:

   ```bash
   npm install exa-js
   ```

   **pnpm**:

   ```bash
   pnpm add exa-js
   ```

   **Yarn**:

   ```bash
   yarn add exa-js
   ```

   **Bun**:

   ```bash
   bun add exa-js
   ```

2. Create a new file `src/mastra/agents/searchAgent.ts` and define your agent:

   ```ts
   import { Agent } from '@mastra/core/agent'

   export const searchAgent = new Agent({
     id: 'search-agent',
     name: 'Search Agent',
     instructions: 'You are a search agent that can search the web for information.',
     model: 'openai/gpt-5.1',
   })
   ```

3. Setup the tool

   ```ts
   import { createTool } from '@mastra/core/tools'
   import z from 'zod'
   import Exa from 'exa-js'

   export const exa = new Exa(process.env.EXA_API_KEY)

   export const webSearch = createTool({
     id: 'exa-web-search',
     description: 'Search the web',
     inputSchema: z.object({
       query: z.string().min(1).max(50).describe('The search query'),
     }),
     outputSchema: z.array(
       z.object({
         title: z.string().nullable(),
         url: z.string(),
         content: z.string(),
         publishedDate: z.string().optional(),
       }),
     ),
     execute: async inputData => {
       const { results } = await exa.searchAndContents(inputData.query, {
         livecrawl: 'always',
         numResults: 2,
       })

       return results.map(result => ({
         title: result.title,
         url: result.url,
         content: result.text.slice(0, 500),
         publishedDate: result.publishedDate,
       }))
     },
   })
   ```

4. Add to your Agent

   ```ts
   import { webSearch } from './tools/searchTool'

   export const searchAgent = new Agent({
     id: 'search-agent',
     name: 'Search Agent',
     instructions: 'You are a search agent that can search the web for information.',
     model: 'openai/gpt-5.1',
     tools: {
       webSearch,
     },
   })
   ```

5. In your `src/mastra/index.ts` file, register the agent:

   ```ts
   import { Mastra } from '@mastra/core'
   import { searchAgent } from './agents/searchAgent'

   export const mastra = new Mastra({
     agents: { searchAgent },
   })
   ```

6. You can test your agent with [Studio](https://mastra.ai/docs/getting-started/studio) using the `mastra dev` command:

   ```bash
   mastra dev
   ```

   Inside Studio navigate to the **"Search Agent"** and ask it: "What happened last week in AI news?"