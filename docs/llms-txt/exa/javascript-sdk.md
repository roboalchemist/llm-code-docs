# Source: https://exa.ai/docs/sdks/javascript-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# JavaScript SDK

> Install and use the Exa JavaScript SDK

The official JavaScript SDK for Exa. Search the web, get page contents, find similar pages, and get answers with citations.

<Card title="Get API Key" icon="key" horizontal href="https://dashboard.exa.ai/api-keys">
  Get your API key from the dashboard
</Card>

## Install

<Tabs>
  <Tab title="npm">
    ```bash  theme={null}
    npm install exa-js
    ```
  </Tab>

  <Tab title="yarn">
    ```bash  theme={null}
    yarn add exa-js
    ```
  </Tab>

  <Tab title="pnpm">
    ```bash  theme={null}
    pnpm add exa-js
    ```
  </Tab>
</Tabs>

## Quick Start

```ts  theme={null}
import Exa from "exa-js";

const exa = new Exa(); // reads EXA_API_KEY from environment
```

## Search

Search the web and get page contents in one call.

```ts  theme={null}
const result = await exa.search(
  "blog post about artificial intelligence",
  {
    contents: {
      text: true
    }
  }
);
```

```ts  theme={null}
const result = await exa.search("interesting articles about space", {
  numResults: 10,
  includeDomains: ["nasa.gov", "space.com"],
  startPublishedDate: "2024-01-01",
  contents: {
    text: true
  }
});
```

## Get Contents

Get text, summaries, or highlights from URLs.

```ts  theme={null}
const { results } = await exa.getContents(["https://openai.com/research"], {
  text: true
});
```

```ts  theme={null}
const { results } = await exa.getContents(["https://stripe.com/docs/api"], {
  summary: true
});
```

```ts  theme={null}
const { results } = await exa.getContents(["https://arxiv.org/abs/2303.08774"], {
  highlights: {
    maxCharacters: 2000
  }
});
```

## Find Similar

Find pages similar to a URL.

```ts  theme={null}
const result = await exa.findSimilar(
  "https://paulgraham.com/greatwork.html",
  {
    contents: {
      text: true
    }
  }
);
```

```ts  theme={null}
const result = await exa.findSimilar(
  "https://waitbutwhy.com/2015/01/artificial-intelligence-revolution-1.html",
  {
    excludeSourceDomain: true,
    contents: {
      text: true
    }
  }
);
```

## Answer

Get answers to questions with citations.

```ts  theme={null}
const response = await exa.answer("What caused the 2008 financial crisis?");
console.log(response.answer);
```

```ts  theme={null}
for await (const chunk of exa.streamAnswer("Explain quantum computing")) {
  if (chunk.content) {
    process.stdout.write(chunk.content);
  }
}
```

## Research

Run research tasks with structured output.

```ts  theme={null}
const task = await exa.research.create({
  instructions: "Find the top 5 AI startups founded in 2024",
  outputSchema: {
    type: "object",
    properties: {
      startups: { type: "array", items: { type: "string" } }
    }
  }
});

const result = await exa.research.pollUntilFinished(task.researchId);
```

## TypeScript

Full TypeScript support with types for all methods.

```ts  theme={null}
import Exa from "exa-js";
import type { SearchResponse, RegularSearchOptions } from "exa-js";
```

<CardGroup cols={2}>
  <Card title="GitHub" icon="github" iconType="brands" color="#000000" href="https://github.com/exa-labs/exa-js">
    View source code
  </Card>

  <Card title="npm" icon="npm" iconType="brands" color="#000000" href="https://www.npmjs.com/package/exa-js">
    View package
  </Card>
</CardGroup>
