# Source: https://exa.ai/docs/sdks/typescript-sdk-specification.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TypeScript SDK Specification

> Enumeration of methods and types in the Exa TypeScript SDK (exa-js).

## Getting started

Install the [exa-js](https://github.com/exa-labs/exa-js) SDK

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

and then instantiate an Exa client

```typescript  theme={null}
import Exa from "exa-js";

const exa = new Exa();  // Reads EXA_API_KEY from environment
// or explicitly: const exa = new Exa("your-api-key");
```

<Card title="Get API Key" icon="key" horizontal href="https://dashboard.exa.ai/api-keys">
  Follow this link to get your API key
</Card>

## `search` Method

<Note>The `options.type` parameter accepts: `"auto"` (default), `"fast"`, `"deep"`, or `"neural"`. See [RegularSearchOptions](#regularsearchoptions) for all available options.</Note>

### Input Example

```typescript  theme={null}
const result = await exa.search("hottest AI startups", {
  numResults: 10
});
```

### Input Parameters

| Parameter | Type                                                                    | Description | Default  |
| --------- | ----------------------------------------------------------------------- | ----------- | -------- |
| query     | `string`                                                                | -           | Required |
| options   | `RegularSearchOptions & { contents?: T \| false \| null \| undefined }` | -           | Required |

### Return Example

```json  theme={null}
{
  "autopromptString": "Here is a link to one of the hottest AI startups:",
  "results": [
    {
      "title": "Adept: Useful General Intelligence",
      "id": "https://www.adept.ai/",
      "url": "https://www.adept.ai/",
      "publishedDate": "2000-01-01",
      "author": null,
      "text": "Adept is building AI that can automate any software process..."
    }
  ],
  "requestId": "a78ebce717f4d712b6f8fe0d5d7753f8"
}
```

### Result Object

| Field       | Type                      | Description                                   |
| ----------- | ------------------------- | --------------------------------------------- |
| results     | `SearchResult&lt;T&gt;[]` | The list of search results.                   |
| requestId   | `string`                  | The request ID for the search.                |
| context     | `string`                  | The context for the search (for deep search). |
| autoDate    | `string`                  | The autoprompt date, if applicable.           |
| statuses    | `Status[]`                | Status information for each result.           |
| costDollars | `CostDollars`             | The cost breakdown for this request.          |

## `searchAndContents` Method

<Note>The `options.type` parameter accepts: `"auto"` (default), `"fast"`, `"deep"`, or `"neural"`. See [RegularSearchOptions](#regularsearchoptions) for all available options.</Note>

### Input Example

```typescript  theme={null}
const result = await exa.searchAndContents("AI in healthcare", {
  text: true,
  highlights: true,
  numResults: 5
});
```

### Input Parameters

| Parameter | Type                       | Description          | Default  |
| --------- | -------------------------- | -------------------- | -------- |
| query     | `string`                   | The query string. \* | Required |
| options   | `RegularSearchOptions & T` | -                    | Required |

### Return Example

```json  theme={null}
{
  "results": [
    {
      "title": "2023 AI Trends in Health Care",
      "id": "https://aibusiness.com/verticals/2023-ai-trends-in-health-care-",
      "url": "https://aibusiness.com/verticals/2023-ai-trends-in-health-care-",
      "publishedDate": "2022-12-29",
      "author": "Wylie Wong",
      "text": "While the health care industry was initially slow to adopt AI...",
      "highlights": [
        "AI is transforming healthcare through improved diagnostics and personalized treatment plans."
      ],
      "highlightScores": [
        0.85
      ]
    }
  ],
  "requestId": "b89fcd823e4f5a91c7d0fe1e6e8864f9"
}
```

### Result Object

| Field       | Type                      | Description                                   |
| ----------- | ------------------------- | --------------------------------------------- |
| results     | `SearchResult&lt;T&gt;[]` | The list of search results.                   |
| requestId   | `string`                  | The request ID for the search.                |
| context     | `string`                  | The context for the search (for deep search). |
| autoDate    | `string`                  | The autoprompt date, if applicable.           |
| statuses    | `Status[]`                | Status information for each result.           |
| costDollars | `CostDollars`             | The cost breakdown for this request.          |

## `findSimilar` Method

<Note>See [FindSimilarOptions](#findsimilaroptions) for all available options including `excludeSourceDomain`.</Note>

### Input Example

```typescript  theme={null}
const result = await exa.findSimilar("https://www.example.com/article", {
  numResults: 10,
  excludeSourceDomain: true
});
```

### Input Parameters

| Parameter | Type                                                                  | Description | Default  |
| --------- | --------------------------------------------------------------------- | ----------- | -------- |
| url       | `string`                                                              | -           | Required |
| options   | `FindSimilarOptions & { contents?: T \| false \| null \| undefined }` | -           | Required |

### Return Example

```json  theme={null}
{
  "results": [
    {
      "title": "Similar Article: AI and Machine Learning",
      "id": "https://www.similarsite.com/ai-ml-article",
      "url": "https://www.similarsite.com/ai-ml-article",
      "publishedDate": "2023-05-15",
      "author": "Jane Doe",
      "text": "Artificial Intelligence (AI) and Machine Learning (ML) are revolutionizing various industries..."
    }
  ],
  "requestId": "08fdc6f20e9f3ea87f860af3f6ccc30f"
}
```

### Result Object

| Field       | Type                      | Description                                   |
| ----------- | ------------------------- | --------------------------------------------- |
| results     | `SearchResult&lt;T&gt;[]` | The list of search results.                   |
| requestId   | `string`                  | The request ID for the search.                |
| context     | `string`                  | The context for the search (for deep search). |
| autoDate    | `string`                  | The autoprompt date, if applicable.           |
| statuses    | `Status[]`                | Status information for each result.           |
| costDollars | `CostDollars`             | The cost breakdown for this request.          |

## `findSimilarAndContents` Method

<Note>See [FindSimilarOptions](#findsimilaroptions) for all available options including `excludeSourceDomain`.</Note>

### Input Example

```typescript  theme={null}
const result = await exa.findSimilarAndContents("https://www.example.com/article", {
  text: true,
  highlights: true,
  numResults: 5
});
```

### Input Parameters

| Parameter | Type                     | Description                                 | Default  |
| --------- | ------------------------ | ------------------------------------------- | -------- |
| url       | `string`                 | The URL for which to find similar links. \* | Required |
| options   | `FindSimilarOptions & T` | -                                           | Required |

### Return Example

```json  theme={null}
{
  "results": [
    {
      "title": "The Impact of AI on Modern Technology",
      "id": "https://www.techblog.com/ai-impact",
      "url": "https://www.techblog.com/ai-impact",
      "publishedDate": "2023-06-01",
      "author": "John Smith",
      "text": "In recent years, artificial intelligence has made significant strides...",
      "highlights": [
        "AI is reshaping industries and creating new opportunities for innovation."
      ],
      "highlightScores": [
        0.92
      ]
    }
  ],
  "requestId": "c90gde934f5g6b02d8e1gf2f7f9975g0"
}
```

### Result Object

| Field       | Type                      | Description                                   |
| ----------- | ------------------------- | --------------------------------------------- |
| results     | `SearchResult&lt;T&gt;[]` | The list of search results.                   |
| requestId   | `string`                  | The request ID for the search.                |
| context     | `string`                  | The context for the search (for deep search). |
| autoDate    | `string`                  | The autoprompt date, if applicable.           |
| statuses    | `Status[]`                | Status information for each result.           |
| costDollars | `CostDollars`             | The cost breakdown for this request.          |

## `getContents` Method

Retrieves contents of documents based on URLs.

### Input Example

```typescript  theme={null}
const result = await exa.getContents([
  "https://www.example.com/article1",
  "https://www.example.com/article2"
], {
  text: { maxCharacters: 1000 },
  highlights: { query: "AI", maxCharacters: 2000 }
});
```

### Input Parameters

| Parameter | Type                                            | Description                                                     | Default  |
| --------- | ----------------------------------------------- | --------------------------------------------------------------- | -------- |
| urls      | `string \| string[] \| SearchResult&lt;T&gt;[]` | A URL or array of URLs, or an array of SearchResult objects. \* | Required |
| options   | `T`                                             | -                                                               | Required |

### Return Example

```json  theme={null}
{
  "results": [
    {
      "url": "https://example.com/article",
      "id": "https://example.com/article",
      "title": "Example Article",
      "text": "The full text content of the article..."
    }
  ]
}
```

### Result Object

| Field       | Type                      | Description                                   |
| ----------- | ------------------------- | --------------------------------------------- |
| results     | `SearchResult&lt;T&gt;[]` | The list of search results.                   |
| requestId   | `string`                  | The request ID for the search.                |
| context     | `string`                  | The context for the search (for deep search). |
| autoDate    | `string`                  | The autoprompt date, if applicable.           |
| statuses    | `Status[]`                | Status information for each result.           |
| costDollars | `CostDollars`             | The cost breakdown for this request.          |

## `answer` Method

### Input Example

```typescript  theme={null}
const result = await exa.answer("What is the capital of France?", {
  text: true,
  model: "exa"
});
```

### Input Parameters

| Parameter | Type                                                      | Description | Default  |
| --------- | --------------------------------------------------------- | ----------- | -------- |
| query     | `string`                                                  | -           | Required |
| options   | `AnswerOptions \| AnswerOptionsTyped&lt;ZodSchema<T&gt;>` | -           | Required |

### Return Example

```json  theme={null}
{
  "answer": "The capital of France is Paris.",
  "citations": [
    {
      "id": "https://www.example.com/france",
      "url": "https://www.example.com/france",
      "title": "France - Wikipedia",
      "publishedDate": "2023-01-01",
      "author": null,
      "text": "France, officially the French Republic, is a country in... [truncated for brevity]"
    }
  ],
  "requestId": "abc123"
}
```

### Result Object

| Field       | Type                                      | Description                                                              |
| ----------- | ----------------------------------------- | ------------------------------------------------------------------------ |
| answer      | `string \| Record&lt;string, unknown&gt;` | The generated answer text (or object matching outputSchema if provided). |
| citations   | `SearchResult&lt;{}&gt;[]`                | The sources used to generate the answer.                                 |
| requestId   | `string`                                  | The request ID for the answer.                                           |
| costDollars | `CostDollars`                             | The cost breakdown for this request.                                     |

## `streamAnswer` Method

### Input Example

```typescript  theme={null}
for await (const chunk of exa.streamAnswer("What is quantum computing?", {
  text: true,
  model: "exa"
})) {
  if (chunk.content) process.stdout.write(chunk.content);
  if (chunk.citations) console.log("Citations:", chunk.citations);
}
```

### Input Parameters

| Parameter | Type                                                                                                                                         | Description | Default  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- |
| query     | `string`                                                                                                                                     | -           | Required |
| options   | `{ text?: boolean; model?: "exa" \| "exa-pro"; systemPrompt?: string; outputSchema?: Record&lt;string, unknown&gt; \| ZodSchema&lt;T&gt;; }` | -           | Required |

### Return Example

```json  theme={null}
{
  "content": "The capital of France is Paris.",
  "citations": [
    {
      "id": "https://www.example.com/france",
      "url": "https://www.example.com/france",
      "title": "France - Wikipedia"
    }
  ]
}
```

### Result Object

| Field     | Type                                                             | Description                                                        |
| --------- | ---------------------------------------------------------------- | ------------------------------------------------------------------ |
| content   | `string`                                                         | The partial text content of the answer (if present in this chunk). |
| citations | `Array&lt;{id, url, title?, publishedDate?, author?, text?}&gt;` | Citations associated with the current chunk of text (if present).  |

## `research.create` Method

### Input Example

```typescript  theme={null}
const task = await exa.research.create({
  instructions: "Research the latest AI developments",
  model: "exa-research-fast"
});
```

### Input Parameters

| Parameter | Type                                                                                                                                    | Description | Default  |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- |
| params    | `{ instructions: string; model?: ResearchCreateRequest["model"]; outputSchema?: Record&lt;string, unknown&gt; \| ZodSchema&lt;T&gt;; }` | -           | Required |

### Return Example

```json  theme={null}
{
  "researchId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "status": "pending"
}
```

## `research.get` Method

<Note>When called with `stream: true`, returns an `AsyncGenerator<ResearchStreamEvent>` for real-time SSE updates instead of a `Promise<Research>`.</Note>

### Input Example

```typescript  theme={null}
const result = await exa.research.get("a1b2c3d4-e5f6-7890-abcd-ef1234567890");
```

### Input Parameters

| Parameter  | Type                                                                         | Description | Default  |
| ---------- | ---------------------------------------------------------------------------- | ----------- | -------- |
| researchId | `string`                                                                     | -           | Required |
| options    | `{ stream?: boolean; events?: boolean; outputSchema?: ZodSchema&lt;T&gt;; }` | -           | Required |

### Return Example

```json  theme={null}
{
  "researchId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "status": "completed",
  "instructions": "What is the latest valuation of SpaceX?",
  "output": {
    "parsed": {
      "valuation": "$350 billion",
      "date": "December 2024",
      "source": "Financial Times"
    }
  }
}
```

## `research.pollUntilFinished` Method

<Note>Options include `pollInterval` (default 1000ms), `timeoutMs` (default 10 minutes), and `events` (boolean to include event log).</Note>

### Input Example

```typescript  theme={null}
const result = await exa.research.pollUntilFinished("a1b2c3d4-e5f6-7890-abcd-ef1234567890", {
  pollInterval: 1000,
  timeoutMs: 600000
});
```

### Input Parameters

| Parameter  | Type                                                                                                  | Description | Default  |
| ---------- | ----------------------------------------------------------------------------------------------------- | ----------- | -------- |
| researchId | `string`                                                                                              | -           | Required |
| options    | `{ pollInterval?: number; timeoutMs?: number; events?: boolean; outputSchema?: ZodSchema&lt;T&gt;; }` | -           | Required |

## `research.list` Method

### Input Example

```typescript  theme={null}
const tasks = await exa.research.list({ limit: 10 });
```

### Input Parameters

| Parameter | Type                  | Description | Default  |
| --------- | --------------------- | ----------- | -------- |
| options   | `ListResearchRequest` | -           | Required |

### Return Example

```json  theme={null}
{
  "data": [
    {
      "researchId": "task-1",
      "status": "completed",
      "instructions": "Research SpaceX valuation"
    }
  ],
  "hasMore": true,
  "nextCursor": "eyJjcmVhdGVkQXQiOiIyMDI0LTAxLTE1VDE4OjMwOjAwWiIsImlkIjoidGFzay0yIn0="
}
```

***

## Types Reference

This section documents the types used throughout the SDK.

### Content Options

These types configure content retrieval options for the `contents` parameter.

#### `ContentsOptions`

Options for retrieving page contents

| Field              | Type                                | Description                                                                                                                                                                                                                         |
| ------------------ | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| text               | `TextContentsOptions \| true`       | Options for retrieving text contents.                                                                                                                                                                                               |
| highlights         | `HighlightsContentsOptions \| true` | Options for retrieving highlights.                                                                                                                                                                                                  |
| summary            | `SummaryContentsOptions \| true`    | Options for retrieving summary.                                                                                                                                                                                                     |
| maxAgeHours        | `number`                            | Maximum age of cached content in hours. If content is older, it will be fetched fresh. Special values: 0 = always fetch fresh content, -1 = never fetch fresh (cache only). Example: 168 = fetch fresh for pages older than 7 days. |
| filterEmptyResults | `boolean`                           | If true, filters out results with no contents. Default is true.                                                                                                                                                                     |
| subpages           | `number`                            | Number of subpages to return for each result.                                                                                                                                                                                       |
| subpageTarget      | `string \| string[]`                | Text used to match/rank subpages in the returned list.                                                                                                                                                                              |
| extras             | `ExtrasOptions`                     | Miscellaneous data derived from results.                                                                                                                                                                                            |
| context            | `ContextOptions \| true`            | Options for retrieving context.                                                                                                                                                                                                     |

#### `BaseSearchOptions`

Options for performing a search query

| Field              | Type                                                                                                                  | Description |
| ------------------ | --------------------------------------------------------------------------------------------------------------------- | ----------- |
| contents           | `ContentsOptions`                                                                                                     | -           |
| numResults         | `number`                                                                                                              | -           |
| includeDomains     | `string[]`                                                                                                            | -           |
| excludeDomains     | `string[]`                                                                                                            | -           |
| startCrawlDate     | `string`                                                                                                              | -           |
| endCrawlDate       | `string`                                                                                                              | -           |
| startPublishedDate | `string`                                                                                                              | -           |
| endPublishedDate   | `string`                                                                                                              | -           |
| category           | `\| "company" \| "research paper" \| "news" \| "pdf" \| "tweet" \| "personal site" \| "financial report" \| "people"` | -           |
| includeText        | `string[]`                                                                                                            | -           |
| excludeText        | `string[]`                                                                                                            | -           |
| flags              | `string[]`                                                                                                            | -           |
| userLocation       | `string`                                                                                                              | -           |

#### `RegularSearchOptions`

Search options for performing a search query.
Uses a discriminated union to ensure additionalQueries is only allowed when type is "deep".

| Field              | Type                                                                                                               | Description                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| type               | `"auto" \| "fast" \| "deep" \| "neural"`                                                                           | The type of search to perform. Default is "auto".                                        |
| numResults         | `number`                                                                                                           | Number of search results to return. Default 10. Max 10 for basic plans.                  |
| includeDomains     | `string[]`                                                                                                         | List of domains to include in the search.                                                |
| excludeDomains     | `string[]`                                                                                                         | List of domains to exclude in the search.                                                |
| startCrawlDate     | `string`                                                                                                           | Start date for results based on crawl date (ISO format).                                 |
| endCrawlDate       | `string`                                                                                                           | End date for results based on crawl date (ISO format).                                   |
| startPublishedDate | `string`                                                                                                           | Start date for results based on published date (ISO format).                             |
| endPublishedDate   | `string`                                                                                                           | End date for results based on published date (ISO format).                               |
| category           | `"company" \| "research paper" \| "news" \| "pdf" \| "tweet" \| "personal site" \| "financial report" \| "people"` | A data category to focus on.                                                             |
| includeText        | `string[]`                                                                                                         | List of strings that must be present in webpage text. Max 1 string of up to 5 words.     |
| excludeText        | `string[]`                                                                                                         | List of strings that must not be present in webpage text. Max 1 string of up to 5 words. |
| contents           | `ContentsOptions`                                                                                                  | Options for retrieving page contents for each result.                                    |
| moderation         | `boolean`                                                                                                          | If true, the search results are moderated for safety.                                    |
| useAutoprompt      | `boolean`                                                                                                          | If true, uses autoprompt to enhance the query.                                           |
| userLocation       | `string`                                                                                                           | The two-letter ISO country code of the user, e.g. US.                                    |
| additionalQueries  | `string[]`                                                                                                         | Alternative query formulations for deep search. Max 5 queries. Only for type: "deep".    |

#### `FindSimilarOptions`

Options for finding similar links.

**Type:** `BaseSearchOptions & { excludeSourceDomain?: boolean; }`

#### `ExtrasOptions`

| Field      | Type     | Description |
| ---------- | -------- | ----------- |
| links      | `number` | -           |
| imageLinks | `number` | -           |

#### `TextContentsOptions`

Options for retrieving text from page.

| Field           | Type               | Description |
| --------------- | ------------------ | ----------- |
| maxCharacters   | `number`           | -           |
| includeHtmlTags | `boolean`          | -           |
| verbosity       | `VerbosityOptions` | -           |
| includeSections | `SectionTag[]`     | -           |
| excludeSections | `SectionTag[]`     | -           |

#### `HighlightsContentsOptions`

Options for retrieving highlights from page.
NOTE: For search type "deep", these options will not be respected. Highlights will be generated with respect
to your initial query, and may vary in quantity and length.

| Field         | Type     | Description                        |
| ------------- | -------- | ---------------------------------- |
| query         | `string` | -                                  |
| maxCharacters | `number` | Maximum characters for highlights. |

#### `SummaryContentsOptions`

Options for retrieving summary from page.

| Field  | Type                                         | Description |
| ------ | -------------------------------------------- | ----------- |
| query  | `string`                                     | -           |
| schema | `Record&lt;string, unknown&gt; \| ZodSchema` | -           |

#### `ContextOptions`

Options for retrieving the context from a list of search results. The context is a string
representation of all the search results.

| Field         | Type     | Description |
| ------------- | -------- | ----------- |
| maxCharacters | `number` | -           |

#### `AnswerOptions`

Options for the answer endpoint

| Field        | Type                            | Description                                                                  |
| ------------ | ------------------------------- | ---------------------------------------------------------------------------- |
| text         | `boolean`                       | Whether to include text in the source results. Default false.                |
| model        | `"exa"`                         | The model to use for generating the answer. Default "exa".                   |
| stream       | `boolean`                       | Whether to stream the response. Default false.                               |
| systemPrompt | `string`                        | A system prompt to guide the LLM's behavior when generating the answer.      |
| outputSchema | `Record&lt;string, unknown&gt;` | A JSON Schema specification for the structure you expect the output to take. |
| userLocation | `string`                        | The two-letter ISO country code of the user, e.g. US.                        |

### Response Types

These types represent API response objects.

#### `CostDollars`

Represents the total cost breakdown. Only non-zero costs are included.

| Field    | Type                  | Description |
| -------- | --------------------- | ----------- |
| total    | `number`              | -           |
| search   | `CostDollarsSeearch`  | -           |
| contents | `CostDollarsContents` | -           |

#### `SearchResult`

Represents a search result object.

| Field           | Type             | Description                                                  |
| --------------- | ---------------- | ------------------------------------------------------------ |
| title           | `string \| null` | The title of the search result.                              |
| url             | `string`         | The URL of the search result.                                |
| id              | `string`         | The temporary ID for the document.                           |
| publishedDate   | `string`         | The estimated creation date of the content.                  |
| author          | `string`         | The author of the content, if available.                     |
| score           | `number`         | Similarity score between the query/url and the result.       |
| image           | `string`         | A representative image for the content, if any.              |
| favicon         | `string`         | A favicon for the site, if any.                              |
| text            | `string`         | The text content of the page (if text option enabled).       |
| highlights      | `string[]`       | Highlighted text snippets (if highlights option enabled).    |
| highlightScores | `number[]`       | Scores for each highlight.                                   |
| summary         | `string`         | Summary of the content (if summary option enabled).          |
| entities        | `Entity[]`       | Structured entity data for company or person search results. |

#### `SearchResponse`

Represents a search response object.

| Field       | Type                      | Description                                   |
| ----------- | ------------------------- | --------------------------------------------- |
| results     | `SearchResult&lt;T&gt;[]` | The list of search results.                   |
| requestId   | `string`                  | The request ID for the search.                |
| context     | `string`                  | The context for the search (for deep search). |
| autoDate    | `string`                  | The autoprompt date, if applicable.           |
| statuses    | `Status[]`                | Status information for each result.           |
| costDollars | `CostDollars`             | The cost breakdown for this request.          |

#### `Status`

| Field  | Type     | Description |
| ------ | -------- | ----------- |
| id     | `string` | -           |
| status | `string` | -           |
| source | `string` | -           |

#### `AnswerResponse`

Represents an answer response object from the /answer endpoint.

| Field       | Type                                      | Description                                                              |
| ----------- | ----------------------------------------- | ------------------------------------------------------------------------ |
| answer      | `string \| Record&lt;string, unknown&gt;` | The generated answer text (or object matching outputSchema if provided). |
| citations   | `SearchResult&lt;{}&gt;[]`                | The sources used to generate the answer.                                 |
| requestId   | `string`                                  | The request ID for the answer.                                           |
| costDollars | `CostDollars`                             | The cost breakdown for this request.                                     |

#### `AnswerStreamChunk`

| Field     | Type                                                             | Description                                                        |
| --------- | ---------------------------------------------------------------- | ------------------------------------------------------------------ |
| content   | `string`                                                         | The partial text content of the answer (if present in this chunk). |
| citations | `Array&lt;{id, url, title?, publishedDate?, author?, text?}&gt;` | Citations associated with the current chunk of text (if present).  |

### Entity Types

These types represent structured entity data returned for company or person searches.

#### `ResearchModel`

The model to use for research tasks.

**Type:** 'exa-research-fast' | 'exa-research' | 'exa-research-pro'

#### `EntityCompanyProperties`

Structured properties for a company entity.

| Field        | Type                                          | Description                                            |
| ------------ | --------------------------------------------- | ------------------------------------------------------ |
| name         | `string \| null`                              | The company name.                                      |
| foundedYear  | `number \| null`                              | The year the company was founded.                      |
| description  | `string \| null`                              | A description of the company.                          |
| workforce    | `EntityCompanyPropertiesWorkforce \| null`    | Information about the company's workforce.             |
| headquarters | `EntityCompanyPropertiesHeadquarters \| null` | Information about the company's headquarters location. |
| financials   | `EntityCompanyPropertiesFinancials \| null`   | Financial information about the company.               |
| webTraffic   | `EntityCompanyPropertiesWebTraffic \| null`   | Web traffic statistics for the company.                |

#### `EntityPersonProperties`

Structured properties for a person entity.

| Field       | Type                                       | Description                |
| ----------- | ------------------------------------------ | -------------------------- |
| name        | `string \| null`                           | The person's name.         |
| location    | `string \| null`                           | The person's location.     |
| workHistory | `EntityPersonPropertiesWorkHistoryEntry[]` | The person's work history. |

#### `CompanyEntity`

Structured entity data for a company.

| Field      | Type                      | Description                            |
| ---------- | ------------------------- | -------------------------------------- |
| id         | `string`                  | Unique identifier for the entity.      |
| type       | `"company"`               | The entity type (always "company").    |
| version    | `number`                  | The version of the entity schema.      |
| properties | `EntityCompanyProperties` | Structured properties for the company. |

#### `PersonEntity`

Structured entity data for a person.

| Field      | Type                     | Description                           |
| ---------- | ------------------------ | ------------------------------------- |
| id         | `string`                 | Unique identifier for the entity.     |
| type       | `"person"`               | The entity type (always "person").    |
| version    | `number`                 | The version of the entity schema.     |
| properties | `EntityPersonProperties` | Structured properties for the person. |
