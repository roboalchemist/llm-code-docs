# Source: https://exa.ai/docs/changelog/instant-search-launch.md


> ## Documentation Index
>
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Introducing Exa Instant Search

> Exa Instant delivers improved neural search with better quality and sub-200ms latency. Use `type = "instant"` to enable the fastest search experience.

***

**Date: February 5, 2026**

We're excited to announce Exa Instant, an improved neural search with both quality and latency benefits, designed for real-time applications where speed is critical.

<Info>
  Try Instant Search in our API with `type = "instant"`. [Try Instant Search in the dashboard](https://dashboard.exa.ai/playground/search?type=instant)
</Info>

## What's New

**Sub-150ms latency**: Exa Instant delivers our fastest search response times, optimized for applications where every millisecond counts.

**Real-time use cases**: Perfect for low-latency products like chat apps and voice AI, coding agents that need fast web lookups, autocomplete, and live suggestions.

**Enhanced neural search**: Exa Instant combines our best neural search technology with optimized infrastructure to deliver state-of-the-art quality at unprecedented speed.

## How to Use Instant Search

Use `type="instant"` in your search requests:

```bash  theme={null}
curl -X POST https://api.exa.ai/search \
  -H "x-api-key: EXA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is the capital of France?",
    "type": "instant",
    "numResults": 10,
    "contents": {
      "highlights": {
        "maxCharacters": 1000
      }
    }
  }'
```

### Python SDK

```python  theme={null}
from exa_py import Exa

exa = Exa('YOUR_EXA_API_KEY')

results = exa.search(
    "What is the capital of France?",
    type="instant",
    num_results=10,
    contents = {
      "highlights": {
        "max_characters": 1000
      }
    }
)

print(results)
```

### TypeScript SDK

```typescript  theme={null}
import Exa from 'exa-js';

const exa = new Exa('YOUR_EXA_API_KEY');

const results = await exa.search(
    'What is the capital of France?',
    {
        type: 'instant',
        numResults: 10,
        contents: {
          highlights: {
            maxCharacters: 1000
          }
        }
    }
);

console.log(results);
```

## Search Type Comparison

| Type      | Latency   | Best For                             |
| --------- | --------- | ------------------------------------ |
| `auto`    | \~1s      | Highest quality results (default)    |
| `instant` | sub-150ms | Real-time applications, autocomplete |
| `fast`    | \~500ms   | Balance of speed and quality         |
| `deep`    | \~5s      | Comprehensive research tasks         |

## Need Help?

If you have questions about Instant Search or want to learn more about optimizing for latency, reach out to [hello@exa.ai](mailto:hello@exa.ai).
