# Source: https://exa.ai/docs/changelog/company-search-launch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Introducing Exa Company Search

> We've added significant improvements to company search due to a fine-tuned retrieval model and entity-matching pipeline. Use `type = "auto"`, `category = "company"` to use this in our search API.

***

**Date: January 21, 2026**

We've added significant improvements to company search due to a fine-tuned retrieval model and entity-matching pipeline for this vertical of queries.

<Info>
  Try Company Search in our API Playground with `type = "auto"`, `category = "company"`. [Try Company Search in the dashboard →](https://dashboard.exa.ai/playground/search?q=fintech%20companies%20in%20Switzerland\&c=company\&filters=%7B%22text%22%3A%22true%22%2C%22type%22%3A%22auto%22%7D)
</Info>

## What's New

**State-of-the-art company search**: We fine-tuned our retrieval model specifically for company search and built an ingestion pipeline optimized for entity matching—delivering accurate results across attributes like industry, geography, funding stage, and employee count.

**Use case focused**: Run queries like "fintech companies in Switzerland" or "Japanese AI companies founded in 2023" and programmatically enrich results with structured company data for sales prospecting, market research, and supply chain workflows.

## How to Use Company Search

Use `type="auto"` and `category="company"` in your search requests:

```bash  theme={null}
curl -X POST https://api.exa.ai/search \
  -H "x-api-key: EXA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Agtech companies optimizing pesticide placement with computer vision",
    "type": "auto",
    "category": "company",
    "numResults": 10
  }'
```

The `company` category supports queries across:

* **Named lookup**: "Sakana AI company" or "Tell me about exa.ai"
* **Attribute filtering**: Industry, geography, founding year, employee count
* **Funding queries**: Stage, amount raised, recent rounds
* **Composite queries**: Multiple constraints like "Israeli security companies founded after 2015"
* **Semantic queries**: Natural language descriptions like "Companies like Bell Labs"

## Structured Entity Data

With this launch, we are introducing entities for company search, a new primitive from Exa that will return high quality, structured information from web data.

Company search results now include structured entity data with detailed company information:

```json  theme={null}
"entities": [
  {
    "id": "https://exa.ai/library/company/metaphor-systems",
    "type": "company",
    "version": 1,
    "properties": {
      "name": "Exa",
      "foundedYear": null,
      "description": "Exa was built with a simple goal — to organize all knowledge...",
      "workforce": {
        "total": 48
      },
      "headquarters": {
        "address": "430 Shotwell St",
        "city": "San Francisco",
        "postalCode": "94110",
        "country": "United States"
      },
      "financials": {
        "revenueAnnual": null,
        "fundingTotal": 107000000,
        "fundingLatestRound": {
          "name": "Series B",
          "date": "2025-09-03",
          "amount": 85000000
        }
      },
      "webTraffic": {
        "total": 477156
      }
    }
  }
]
```

## Learn More

* Read our blog post: [Introducing Exa's Company Search Benchmark](https://exa.ai/blog/company-search-benchmark)
* Try it in the [API Playground](https://dashboard.exa.ai/playground/search?q=fintech%20companies%20in%20Switzerland\&c=company\&filters=%7B%22text%22%3A%22true%22%2C%22type%22%3A%22auto%22%7D)

## Need Help?

If you have questions about company search or want to learn more about optimizing your queries, reach out to [hello@exa.ai](mailto:hello@exa.ai). We're here to help you get the most out of Exa Company Search!
