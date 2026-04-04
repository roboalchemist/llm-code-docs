# Source: https://docs.nimbleway.io/nimble-sdk/search-api/focus-modes.md

# Focus Modes

Focus modes allow you to specialize search queries to retrieve results from specific sources and platforms. Each focus mode uses one or more Web Search Agents (WSA) to gather results optimized for different use cases

### Available Focus Modes

| Focus Mode          | Description                                                                   | Best For                                                                 |
| ------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `general` (default) | Web search engine (e.g., Google, Bing)                                        | General information, broad topics, web pages                             |
| `news`              | News sources (e.g., Google News)                                              | Current events, breaking stories, journalistic analysis                  |
| `location`          | Local business search engine (e.g., Google Maps)                              | Places, businesses, geographic information                               |
| `coding`            | Developer resources and code                                                  | Finding code examples, debugging help, API documentation                 |
| `academic`          | Scholarly sources and papers                                                  | Scientific research, peer-reviewed studies, scholarly citations          |
| `shopping`          | E-commerce platforms (Amazon, Walmart, Target, ...)                           | Product comparison, price discovery, merchant reviews                    |
| `geo`               | Generative Engine Optimization - AI search engines (ChatGPT, Perplexity, ...) | AI-generated answers, search optimization strategies, synthetic insights |
| `social`            | Social media platforms (TikTok, LinkedIn, YouTube, ...)                       | Social content, influencers, trending topics                             |

### Basic Usage

Specify a focus mode using the `focus` parameter:

```bash
curl -X POST "https://nimble-retriever.webit.live/search" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "best laptops 2026",
    "focus": "shopping",
    "max_results": 10
  }'
```

#### Quick Examples

**General web search:**

```bash
{
  "query": "artificial intelligence trends",
  "focus": "general",
  "deep_search": true
}
```

**News search:**

```bash
{
  "query": "climate policy",
  "focus": "news"
}
```

**Product search:**

```bash
{
  "query": "wireless headphones",
  "focus": "shopping",
  "max_subagents": 5
}
```

**AI search engines:**

```bash
{
  "query": "how to optimize for AI search",
  "focus": "geo"
}
```

**Social media search:**

```bash
{
  "query": "AI tutorials",
  "focus": "social",
  "max_results": 20
}
```

### Key Parameters

#### focus

**Type:** `string` **Default:** `"general"`

Specify which focus mode to use:

```json
{"focus": "shopping"}
```

#### max\_subagents

**Type:** `integer` **Default:** `3` **Range:** `1-5`

Controls how many Web Search Agents (WSA) execute in parallel for focus modes with multiple agents.

```json
{
  "focus": "shopping",
  "max_subagents": 5
}
```

Higher values = more diverse results but slower response.

#### deep\_search

**Type:** `boolean` **Default:** `true`

Extract full page content for each result. Disable for faster responses when only metadata is needed.

```json
{
  "focus": "general",
  "deep_search": false
}
```

#### include\_answer

**Type:** `boolean` **Default:** `false`

Generate an AI summary of search results.

```json
{
  "query": "what is quantum computing",
  "focus": "general",
  "include_answer": true
}
```

### Best Practices

**Choose the right focus mode:**

* Product research → `shopping`
* Current trends → `geo` or `social`
* Technical docs → `coding`
* Academic research → `academic`
* Breaking news → `news`

**Optimize performance:**

* Lower `max_subagents` (1-2) for faster responses
* Disable `deep_search` when only metadata needed
* Choose focused modes for specific use cases

**Maximize quality:**

* Higher `max_subagents` (4-5) for diverse results
* Enable `deep_search` for comprehensive content
* Adjust `max_results` to get more comprehensive data

***

**Need help?** Check the main [Search API documentation](https://docs.nimbleway.com/nimble-sdk/search-api) or contact <support@nimbleway.com>.
