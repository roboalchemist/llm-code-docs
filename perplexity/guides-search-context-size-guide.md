# Source: https://docs.perplexity.ai/guides/search-context-size-guide

The `search_context_size` parameter allows you to control how much search context is retrieved from the web during query resolution, letting you balance cost and comprehensiveness.
  * Default `search_context_size` is `low`
  * Selecting `"high"` increases search costs due to more extensive web retrieval. Use `"low"` when cost efficiency is critical.


## 
[​](https://docs.perplexity.ai/guides/search-context-size-guide#overview)
Overview
The `search_context_size` field—passed via the `web_search_options` object—determines how much search context is retrieved by the Sonar models. This setting can help you optimize for either:
  * Cost savings with minimal search input (`low`)
  * Comprehensive answers by maximizing retrieved information (`high`)
  * A balance of both (`medium`)

This flexibility allows teams to tune their API usage to their budget and use case. To enable this feature, include the web_search_options.search_context_size parameter in your request payload:
Copy
Ask AI
```
"web_search_options": {
  "search_context_size": "medium"
}

```

## 
[​](https://docs.perplexity.ai/guides/search-context-size-guide#best-practices)
Best Practices
**Choosing the Right Context Size**
  * `low`: Best for short factual queries or when operating under strict token cost constraints.
  * `medium`: The default and best suited for general use cases.
  * `high`: Use for deep research, exploratory questions, or when citations and evidence coverage are critical.

**Cost Optimization**
  * Selecting `low` or `medium` can significantly reduce overall token usage, especially at scale.
  * Consider defaulting to `low` for high-volume endpoints and selectively upgrading to `high` for complex user prompts.

Combining with Other Filters
  * You can use `search_context_size` alongside other features like `search_domain_filter` to further control the scope of search.
  * Combining `medium` with a focused domain filter often gives a good tradeoff between quality and cost.

Performance Considerations
  * Larger context sizes may slightly increase response latency due to more extensive search and reranking.
  * If you’re batching queries or supporting real-time interfaces, test with different settings to balance user experience and runtime.


## 
[​](https://docs.perplexity.ai/guides/search-context-size-guide#examples)
Examples
**1. Minimal Search Context (“low”)** This option limits the search context retrieved for the model, reducing cost per request while still producing useful responses for simpler questions.
## 
[​](https://docs.perplexity.ai/guides/search-context-size-guide#request)
Request
cURL
Python
TypeScript
Copy
Ask AI
```
curl --request POST \
  --url https://api.perplexity.ai/chat/completions \
  --header "Authorization: Bearer $SONAR_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "sonar",
    "messages": [
      {
        "role": "system",
        "content": "Be precise and concise."
      },
      {
        "role": "user",
        "content": "How many stars are there in our galaxy?"
      }
    ],
    "web_search_options": {
      "search_context_size": "low"
    }
  }' | jq

```

**Pro-tip** : Use `low` when cost optimization is more important than answer completeness. **2. Comprehensive Search Context (“high”)** This option maximizes the amount of search context used to answer the question, resulting in more thorough and nuanced responses.
## 
[​](https://docs.perplexity.ai/guides/search-context-size-guide#request-2)
Request
cURL
Python
TypeScript
Copy
Ask AI
```
curl --request POST \
  --url https://api.perplexity.ai/chat/completions \
  --header "Authorization: Bearer $SONAR_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "sonar",
    "messages": [
      {
        "role": "system",
        "content": "Be precise and concise."
      },
      {
        "role": "user",
        "content": "Explain the economic causes of the 2008 financial crisis."
      }
    ],
    "web_search_options": {
      "search_context_size": "high"
    }
  }' | jq

```

**Pro-tip** : Use `high` for research-heavy or nuanced queries where coverage matters more than cost. ⸻
