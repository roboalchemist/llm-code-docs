# Desearch AI

> Decentralized AI-powered search infrastructure built on Bittensor subnet 22

Desearch is a decentralized search engine providing AI-powered web search, X (Twitter) search, and deep research capabilities through a unified API. Built on the Bittensor network, it leverages decentralized miners and validators to deliver unbiased, censorship-resistant search results.

## Quick Links

- Website: https://desearch.ai
- Console: https://console.desearch.ai
- API Documentation: https://desearch.ai/guide
- API Reference: https://desearch.ai/api-reference
- Pricing: https://desearch.ai/pricing

## API Capabilities

### AI Search
Intelligent search with AI-generated responses combining web results and reasoning.
- Endpoint: POST /api/v1/search/ai
- Returns AI-synthesized answers with source citations

### Web Search
Fast basic web search functionality.
- Endpoint: POST /api/v1/search/web
- Returns ranked web results with snippets

### X/Twitter Search
Search tweets and social content from X (formerly Twitter).
- Endpoint: POST /api/v1/search/x
- Supports user search, keyword search, and recent tweets

### Deep Research
Comprehensive research reports with multi-source analysis.
- Endpoint: POST /api/v1/search/research
- Generates detailed research documents with citations

### Web Links Search
Extract and analyze content from specific URLs.
- Endpoint: POST /api/v1/search/links
- Retrieves structured data from web pages

## Authentication

All API requests require an API key passed in the Authorization header:
```
Authorization: Bearer YOUR_API_KEY
```

Get your API key at: https://console.desearch.ai

## Rate Limits

- Free tier: 100 requests/day
- Paid tiers: Based on subscription level
- See pricing: https://desearch.ai/pricing

## SDKs

- Python SDK: Available via pip
- JavaScript SDK: Available via npm
- Documentation: https://desearch.ai/guide/SDK

## Integrations

Desearch integrates with:
- OpenAI function calling
- Claude/Anthropic function calling
- LangChain
- LlamaIndex
- CrewAI agents
- ElizaOS agents
- Model Context Protocol (MCP)
- Browser Use

## About Bittensor Integration

Desearch runs on Bittensor Subnet 22, utilizing:
- Decentralized network of miners for search indexing
- Validators for result quality assurance
- TAO token economics for incentive alignment

## Contact

- Website: https://desearch.ai
- Twitter/X: @desikiofficial
- Support: https://desearch.ai/contact
