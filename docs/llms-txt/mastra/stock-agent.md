# Source: https://mastra.ai/guides/guide/stock-agent

# Building an AI Stock Agent

In this guide, you're going to create an agent that fetches the last day's closing stock price for a given symbol. You'll learn how to create a tool, add it to an agent, and use the agent to fetch stock prices.

[YouTube video player](https://www.youtube-nocookie.com/embed/rIaZ4l7y9wo)

## Prerequisites

- Node.js `v22.13.0` or later installed
- An API key from a supported [Model Provider](https://mastra.ai/models)
- An existing Mastra project (Follow the [installation guide](https://mastra.ai/guides/getting-started/quickstart) to set up a new project)

## Creating the Agent

To create an agent in Mastra use the `Agent` class to define it and then register it with Mastra.

1. Create a new file `src/mastra/agents/stockAgent.ts` and define your agent:

   ```ts
   import { Agent } from '@mastra/core/agent'

   export const stockAgent = new Agent({
     id: 'stock-agent',
     name: 'Stock Agent',
     instructions:
       'You are a helpful assistant that provides current stock prices. When asked about a stock, use the stock price tool to fetch the stock price.',
     model: 'openai/gpt-5.1',
   })
   ```

2. In your `src/mastra/index.ts` file, register the agent:

   ```ts
   import { Mastra } from '@mastra/core'
   import { stockAgent } from './agents/stockAgent'

   export const mastra = new Mastra({
     agents: { stockAgent },
   })
   ```

## Creating the Stock Price Tool

The Stock Agent doesn't yet know anything about current stock prices. To change this, create a tool and add it to the agent.

1. Create a new file `src/mastra/tools/stockPrices.ts`. Inside, add a `stockPrices` tool that will fetch the last day's closing stock price for a given symbol:

   ```ts
   import { createTool } from '@mastra/core/tools'
   import { z } from 'zod'

   const getStockPrice = async (symbol: string) => {
     const data = await fetch(
       `https://mastra-stock-data.vercel.app/api/stock-data?symbol=${symbol}`,
     ).then(r => r.json())
     return data.prices['4. close']
   }

   export const stockPrices = createTool({
     id: 'Get Stock Price',
     inputSchema: z.object({
       symbol: z.string(),
     }),
     description: `Fetches the last day's closing stock price for a given symbol`,
     execute: async inputData => {
       console.log('Using tool to fetch stock price for', inputData.symbol)
       return {
         symbol: inputData.symbol,
         currentPrice: await getStockPrice(inputData.symbol),
       }
     },
   })
   ```

2. Inside `src/mastra/agents/stockAgent.ts` import your newly created `stockPrices` tool and add it to the agent.

   ```ts
   import { Agent } from '@mastra/core/agent'
   import { stockPrices } from '../tools/stockPrices'

   export const stockAgent = new Agent({
     id: 'stock-agent',
     name: 'Stock Agent',
     instructions:
       'You are a helpful assistant that provides current stock prices. When asked about a stock, use the stock price tool to fetch the stock price.',
     model: 'openai/gpt-5.1',
     tools: {
       stockPrices,
     },
   })
   ```

## Running the Agent Server

Learn how to interact with your agent through Mastra's API.

1. You can run your agent as a service using the `mastra dev` command:

   ```bash
   mastra dev
   ```

   This will start a server exposing endpoints to interact with your registered agents. Within [Studio](https://mastra.ai/docs/getting-started/studio) you can test your `stockAgent` and `stockPrices` tool through a UI.

2. By default, `mastra dev` runs on `http://localhost:4111`. Your Stock agent will be available at:

   ```text
   POST http://localhost:4111/api/agents/stockAgent/generate
   ```

3. You can interact with the agent using `curl` from the command line:

   ```bash
   curl -X POST http://localhost:4111/api/agents/stockAgent/generate \
     -H "Content-Type: application/json" \
     -d '{
       "messages": [
         { "role": "user", "content": "What is the current stock price of Apple (AAPL)?" }
       ]
     }'
   ```

   You should receive a JSON response similar to:

   ```json
   {
     "text": "The current price of Apple (AAPL) is $174.55.",
     "agent": "Stock Agent"
   }
   ```

   This indicates that your agent successfully processed the request, used the `stockPrices` tool to fetch the stock price, and returned the result.