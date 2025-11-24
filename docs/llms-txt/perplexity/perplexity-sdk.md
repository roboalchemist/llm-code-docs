# Source: https://docs.perplexity.ai/guides/perplexity-sdk.md

# Quickstart

> Learn how to use the official Perplexity SDKs for Python and TypeScript/JavaScript to access the Perplexity APIs with type safety and async support.

## Overview

The official Perplexity SDKs provide convenient access to the Perplexity APIs from Python 3.8+ and Node.js applications. Both SDKs include type definitions for all request parameters and response fields, with both synchronous and asynchronous clients.

## Available APIs

<CardGroup cols={2}>
  <Card title="Chat Completions" icon="message" href="/guides/chat-completions-sdk">
    AI responses with web-grounded knowledge, conversation context, and streaming support.
  </Card>

  <Card title="Search" icon="magnifying-glass" href="/guides/perplexity-sdk-search">
    Ranked web search results with filtering, multi-query support, and domain controls.
  </Card>
</CardGroup>

## Installation

Install the SDK for your preferred language:

<CodeGroup>
  ```bash Python theme={null}
  pip install perplexityai
  ```

  ```bash TypeScript/JavaScript theme={null}
  npm install @perplexity-ai/perplexity_ai
  ```
</CodeGroup>

## Authentication

<Card title="Get your Perplexity API Key" icon="key" arrow="True" horizontal="True" iconType="solid" cta="Click here" href="https://perplexity.ai/account/api">
  Navigate to the **API Keys** tab in the API Portal and generate a new key.
</Card>

After generating the key, set it as an environment variable in your terminal:

<Tabs>
  <Tab title="Windows">
    ```bash  theme={null}
    setx PERPLEXITY_API_KEY "your_api_key_here"
    ```
  </Tab>

  <Tab title="MacOS/Linux">
    ```bash  theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```
  </Tab>
</Tabs>

### Using Environment Variables

You can use the environment variable directly:

<CodeGroup>
  ```python Python theme={null}
  import os
  from perplexity import Perplexity

  client = Perplexity() # Automatically uses PERPLEXITY_API_KEY
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity({
    apiKey: process.env['PERPLEXITY_API_KEY'], // This is the default and can be omitted
  });
  ```
</CodeGroup>

Or use [python-dotenv](https://pypi.org/project/python-dotenv/) (Python) or [dotenv](https://www.npmjs.com/package/dotenv) (Node.js) to load the environment variable from a `.env` file:

<CodeGroup>
  ```python Python theme={null}
  import os
  from dotenv import load_dotenv
  from perplexity import Perplexity

  load_dotenv()

  client = Perplexity() # Uses PERPLEXITY_API_KEY from .env file
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import dotenv from 'dotenv';

  dotenv.config();

  const client = new Perplexity(); // Uses PERPLEXITY_API_KEY from .env file
  ```
</CodeGroup>

<Tip>
  Now you're ready to start using the Perplexity APIs! Choose your API below for step-by-step usage guides.
</Tip>

<CardGroup cols={2}>
  <Card title="Chat Completions" icon="message" href="/guides/chat-completions-sdk">
    Get started with AI responses
  </Card>

  <Card title="Search" icon="magnifying-glass" href="/guides/perplexity-sdk-search">
    Get started with web search
  </Card>
</CardGroup>

## Resources

<CardGroup cols={2}>
  <Card title="Python Package" icon="cube" href="https://pypi.org/project/perplexityai/">
    Install from PyPI with pip
  </Card>

  <Card title="Node.js Package" icon="cube" href="https://www.npmjs.com/package/@perplexity-ai/perplexity_ai">
    Install from npm registry
  </Card>
</CardGroup>
