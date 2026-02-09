# Source: https://exa.ai/docs/changelog/people-search-launch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Introducing Exa People Search

> We're launching state-of-the-art people search with 1B+ indexed profiles. The 'linkedin' category is now replaced with 'people' for better results.

***

**Date: December 19, 2025**

We're launching **Exa People Search**, a new way to find and discover people on the web, designed for real production use across sales, recruiting, research, and more.

<Info>
  Try People Search in our API Playground with `category = "people"`. [Try People Search in the dashboard →](https://dashboard.exa.ai/playground/search?q=product%20managers%20at%20microsoft\&c=people\&filters=%7B%22text%22%3A%22true%22%2C%22type%22%3A%22auto%22%7D)
</Info>

## What's New

**State-of-the-art people search**: Exa indexed 1B+ public profiles and trained a hybrid retrieval system (fine-tuned embeddings + Exa Search) to deliver highly accurate role, skill, and company based people search at web scale.

**Usecase focused**: Customers can run queries like "VP of Product at Microsoft" or "enterprise sales reps from Microsoft in EMEA" and programmatically enrich results with profiles for sales, recruiting, and market research workflows.

## What Changed

We're replacing the `linkedin` category with the new `people` category to provide better, more comprehensive people search results.

### Before

```python  theme={null}
# Old approach - limited to LinkedIn
result = exa.search("VP of Product at Microsoft", category="linkedin")
```

### After

```python  theme={null}
# New approach - comprehensive people search across the web
result = exa.search("VP of Product at Microsoft", category="people")
```

## How to Use People Search

Simply use `category="people"` in your search requests:

```bash  theme={null}
curl -X POST https://api.exa.ai/search \
  -H "x-api-key: EXA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Product managers at Microsoft",
    "category": "people",
    "numResults": 10
  }'
```

The new `people` category provides:

* **Broader coverage**: 1B+ profiles across the entire web, not just LinkedIn
* **Better accuracy**: Fine-tuned embeddings specifically for people search
* **More relevant results**: Hybrid retrieval system optimized for role, skill, and company queries

## Learn More

* Read our blog post: [Introducing Exa's People Search Benchmarks](https://exa.ai/blog/people-search-benchmark)
* Follow our announcement: [Twitter/X](https://x.com/ExaAILabs/status/2001373897154007390)
* Try it in the [API Playground](https://dashboard.exa.ai/playground/search?q=product%20managers%20at%20microsoft\&c=people\&filters=%7B%22text%22%3A%22true%22%2C%22type%22%3A%22auto%22%7D)

## Need Help?

If you have questions about migrating from the `linkedin` category or want to learn more about optimizing your people search queries, reach out to [hello@exa.ai](mailto:hello@exa.ai). We're here to help you get the most out of Exa People Search!
