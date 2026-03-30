# Source: https://docs.nimbleway.io/nimble-sdk/search-api.md

# Search API

Execute web searches and retrieve clean, parsed content from top results in two modes:

* **Fast Mode** — Quickly discovers high-value URLs or generates fast web answers for your agents It’s ideal for lightweight discovery or pairing with /extract when you want to selectively fetch full content only from the URLs you choose.  Costs 1 credit per search.
* **Deep Search** — Performs real-time webpage extraction for full, rich context, automatically calling /extract to retrieve complete webpage content for deeper research tasks.  Deep Search costs 1 credit per search, plus 1 additional credit for each webpage extracted.&#x20;

Both Fast Mode and Deep Search support [advanced search filtering](#request-body-parameters), location targeting, max result limits, and additional web-search refinement tools.

### Basic Usage&#x20;

#### Fast Mode Search

```bash
curl -X POST https://nimble-retriever.webit.live/search \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest AI trends 2025",
    "max_results": 10,
    "deep_search": false,
    "country": "US",
    "locale": "en"
  }'
```

**Response format example:**

```json
{
  "results": [
    {
      "title": "Latest GenAI Trends: 5 Key Developments to Watch",
      "description": "Explore the top trends in generative AI including agentic AI, retrieval-augmented generation, self-training models, and ethical AI implementations.",
      "url": "https://example.com/genai-trends-2025",
      "content": "",
      "metadata": {
        "position": 1,
        "entity_type": "OrganicResult",
        "country": "US",
        "locale": "en"
      }
    },
    {
      "title": "GenAI Investment and Market Analysis 2025",
      "description": "Despite challenges, investment in generative AI continues to grow. Analysis of market trends, adoption rates, and future projections for enterprise AI.",
      "url": "https://example.com/genai-investment-analysis",
      "content": "",
      "metadata": {
        "position": 2,
        "entity_type": "OrganicResult",
        "country": "US",
        "locale": "en"
      }
    }
  ]
}
```

### Fast Mode with - `Include Answer`

Optional AI-generated answer summaries that provide quick insights from search results without reading full content. *This costs 1 additional credit per request.*

```bash
curl -X POST https://nimble-retriever.webit.live/search \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest developments in quantum computing",
    "max_results": 5,
    "deep_search": false,
    "include_answer": true
  }'
```

#### **Response:**

```json
{
  "answer": "Recent developments in quantum computing include significant advances in error correction, with researchers achieving quantum advantage in specific computational tasks. Major tech companies have announced new quantum processors with increased qubit counts and improved coherence times, moving closer to practical quantum applications in cryptography and drug discovery.",
  "results": [...]
}
```

### Deep Search&#x20;

```bash
curl -X POST https://nimble-retriever.webit.live/search \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest AI trends 2025",
    "max_results": 5,
    "deep_search": true,
    "output_format": "markdown",
    "country": "US",
    "locale": "en"
  }'
```

**Response format example:**

```json
{
  "results": [
    {
      "title": "Top AI Trends Shaping 2025 - Tech Insights",
      "description": "Explore the latest artificial intelligence trends transforming industries in 2025...",
      "url": "https://example.com/ai-trends-2025",
      "content": "# Latest AI Trends in 2025\n\nThe artificial intelligence landscape has evolved dramatically...",
      "metadata": {
        "position": 1,
        "entity_type": "OrganicResult",
        "country": "US",
        "locale": "en",
        "driver": "vx10"
      }
    },
    {
      "title": "AI Revolution: What to Expect in 2025",
      "description": "From generative AI to autonomous systems...",
      "url": "https://example.com/ai-revolution",
      "content": "# The AI Revolution\n\nArtificial intelligence continues to reshape...",
      "metadata": {
        "position": 2,
        "entity_type": "OrganicResult",
        "country": "US",
        "locale": "en",
        "driver": "vx10"
      }
    }
  ]
}
```

***

### **Request Body Parameters**

| Parameter         | Type                                                                                        | Required | Default    | Description                                                                                                                                                                                                                                                         |
| ----------------- | ------------------------------------------------------------------------------------------- | -------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`           | string                                                                                      | Yes      | -          | The search query to execute                                                                                                                                                                                                                                         |
| `max_results`     | integer                                                                                     | No       | 3          | Number of search results to return (max: 100)                                                                                                                                                                                                                       |
| `focus`           | <p>enum\["general", "news", "location", </p><p>"social",</p><p>"geo",</p><p>"shopping"]</p> | No       | general    | The search topic type. `news` returns real-time news articles with publication dates. `location` returns places with ratings, addresses, and reviews (restaurants, businesses, venues). `general` (default) returns standard web search results across all sources. |
| `deep_search`     | boolean                                                                                     | No       | true       | When `true`, fetches and parses full page content. When `false`, return only meta\_data.                                                                                                                                                                            |
| `output_format`   | enum                                                                                        | No       | `markdown` | Output format. Options: `plain_text`, `markdown`, `simplified_html`                                                                                                                                                                                                 |
| `locale`          | string                                                                                      | No       | `en`       | Locale for search results (e.g., `en`, `fr`, `de`)                                                                                                                                                                                                                  |
| `country`         | string                                                                                      | No       | `US`       | Country code for search results (e.g., `US`, `FR`, `GB`)                                                                                                                                                                                                            |
| `include_answer`  | boolean                                                                                     | No       | false      | Generate LLM answer summary (only available when deep\_search=False)                                                                                                                                                                                                |
| `include_domains` | string\[]                                                                                   | No       |            | List of domains to include in search results. Maximum 50 domains.                                                                                                                                                                                                   |
| `exclude_domains` | string\[]                                                                                   | No       |            | List of domains to exclude from search results. Maximum 50 domains.                                                                                                                                                                                                 |
| `time_range`      | enum\["hour", "day", "week", "month", "year"]                                               | No       |            | Restrict results to recent time period                                                                                                                                                                                                                              |
| `start_date`      | string                                                                                      | No       |            | Filter results after this date (format: YYYY-MM-DD or YYYY)                                                                                                                                                                                                         |
| `end_date`        | string                                                                                      | No       |            | Filter results before this date (format: YYYY-MM-DD or YYYY)                                                                                                                                                                                                        |

***

### Best Practices

1. **Deep Search vs Fast Mode**:
   * Use Fast Mode + `include_answer` for quick summaries (2 credits total)
   * Use Deep Search when you need full content analysis (1 + N credits)
2. **Domain Filtering**:
   * Use `include_domains` to focus on trusted sources
   * Use `exclude_domains` to filter out unwanted content
3. **Time Filtering**:

   * Use `time_range` for simple recency filters (last hour/day/week)
   * Use `start_date`/`end_date` for specific date ranges

***

### **End-to-end examples**

Our [Nimble Cookbook](https://github.com/Nimbleway/cookbook) offers hands-on guides that show you how to use our Search API for real use cases like LLM grounding, real-time web extraction, and AI workflow automation.
