# Desearch AI - Complete Documentation

## Overview

Desearch AI is an advanced AI-powered search engine built on Bittensor (Subnet 22). It is designed for profound data discovery and intelligent information aggregation, helping users extract, analyze, and compile insights from multiple sources with precision and efficiency.

### Key Features

- **AI-Powered Search**: Leverage AI-driven natural language processing for intelligent search across multiple sources
- **Decentralized Infrastructure**: Built on Bittensor Subnet 22 for reliable, censorship-resistant search
- **Multi-Source Aggregation**: Aggregate results from web, Hacker News, Reddit, Wikipedia, YouTube, Twitter/X, and ArXiv
- **Real-time Data**: Access current information with streaming capabilities
- **Multiple Integration Patterns**: Supports function calling, RAG frameworks, agent systems, and MCP

### Use Cases

- Search engine applications
- AI-driven chat systems
- Intelligent agent task automation
- X (Twitter) query and trend analysis
- Content research and analysis
- Multi-source data aggregation

## Getting Started

### Authentication

All API requests require an API key passed in the Authorization header:

```text
Authorization: YOUR_API_KEY
```

Get your API key at: [https://console.desearch.ai](https://console.desearch.ai)

### Base URL

```text
https://api.desearch.ai
```

### Rate Limits

- **Free tier**: 100 requests/day
- **Paid tiers**: Based on subscription level
- See [pricing page](https://desearch.ai/pricing) for details

## API Endpoints

### POST /desearch/ai/search

#### AI Contextual Search

The Desearch API allows you to perform AI-powered web searches, gathering relevant information from multiple sources, including web pages, research papers, and social media discussions.

#### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | string | Yes | Search query prompt |
| `tools` | array | Yes | List of tools to search: `web`, `hackernews`, `reddit`, `wikipedia`, `youtube`, `twitter`, `arxiv` |
| `start_date` | string | No | Start date (Format: YYYY-MM-DDTHH:MM:SSZ UTC) |
| `end_date` | string | No | End date (Format: YYYY-MM-DDTHH:MM:SSZ UTC) |
| `date_filter` | string | No | Predefined date filters: `PAST_24_HOURS`, `PAST_2_DAYS`, `PAST_WEEK`, `PAST_2_WEEKS`, `PAST_MONTH`, `PAST_2_MONTHS`, `PAST_YEAR`, `PAST_2_YEARS` (Default: `PAST_24_HOURS`) |
| `streaming` | boolean | No | Whether to stream results (Default: false) |
| `result_type` | string | No | Result format: `ONLY_LINKS` or `LINKS_WITH_FINAL_SUMMARY` (Default: `LINKS_WITH_FINAL_SUMMARY`) |
| `system_message` | string | No | Custom system message for search |
| `scoring_system_message` | string | No | System message for response scoring |
| `count` | integer | No | Number of results per source; range 10-200 (Default: 10) |

#### Request Example

```bash
curl -X POST "https://api.desearch.ai/desearch/ai/search" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "latest AI developments",
    "tools": ["web", "arxiv", "twitter"],
    "streaming": false,
    "count": 20
  }'
```

#### Response

Returns a JSON object mapping tool names to their search results:

```json
{
  "search": [
    {
      "link": "https://example.com/article",
      "snippet": "Preview text...",
      "title": "Article Title"
    }
  ],
  "arxiv_search": [
    {
      "link": "https://arxiv.org/abs/2024.xxxxx",
      "snippet": "Paper abstract...",
      "title": "Paper Title"
    }
  ],
  "tweets": [
    {
      "link": "https://x.com/user/status/xxxxx",
      "snippet": "Tweet content...",
      "title": "Tweet by @user",
      "created_at": "2024-01-01T12:00:00.000Z",
      "bookmark_count": 10,
      "reply_count": 5,
      "retweet_count": 20,
      "like_count": 100
    }
  ],
  "text": "AI-generated summary of results...",
  "miner_link_scores": {
    "https://example.com/article": "0.95"
  }
}
```

#### Response Status Codes

- **200**: Success - JSON object with search results
- **301**: Moved Permanently
- **304**: Not Modified
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error

### POST /desearch/ai/search/links/web

#### AI Web Search (Links Only)

Search for links related to a given query using multiple tools, excluding X (Twitter) Search.

#### Web Search Request Parameters

Same as `/desearch/ai/search` but returns only link-based results from:

- Web pages
- YouTube
- Wikipedia
- ArXiv

### POST /desearch/ai/search/links/twitter

#### AI X Posts Search

Search for relevant links based on X search queries using AI-powered models.

#### Twitter Search Request Parameters

Same as `/desearch/ai/search` but focuses on X/Twitter content.

### GET /twitter

#### X Search API

Retrieve relevant links and tweets based on specified search queries without AI-driven models.

#### X Search Query Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes | Advanced search query |
| `sort` | string | No | Sort by `top` or `latest` |
| `user` | string | No | User to search for |
| `start_date` | string | No | Start date (YYYY-MM-DD format) |
| `end_date` | string | No | End date (YYYY-MM-DD format) |
| `lang` | string | No | Language code (e.g., `en`, `es`, `fr`) |
| `verified` | boolean | No | Filter for verified users |
| `blue_verified` | boolean | No | Filter for blue checkmark users |
| `is_quote` | boolean | No | Include only tweets with quotes |
| `is_video` | boolean | No | Include only tweets with videos |
| `is_image` | boolean | No | Include only tweets with images |
| `min_retweets` | integer | No | Minimum number of retweets |
| `min_replies` | integer | No | Minimum number of replies |
| `min_likes` | integer | No | Minimum number of likes |
| `count` | integer | No | Number of tweets to retrieve |

### GET /twitter/urls

#### Fetch Posts by URLs

Retrieve detailed information for multiple posts by providing their URLs.

#### URL Fetch Query Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `urls` | array | Yes | List of tweet URLs to retrieve |

### GET /twitter/post

#### Retrieve Post by ID

Retrieve comprehensive details of a post by specifying its unique ID.

#### Post ID Query Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | Post ID |

### GET /twitter/user

#### Search X Posts by User

Search for posts from a specific X user.

#### User Posts Query Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `user` | string | Yes | Username (with or without @) |

### GET /twitter/user/{username}

#### Fetch User's Tweets and Replies

Retrieve tweets and replies from a specific user timeline.

#### User Timeline Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `username` | string | Yes | Username |

### GET /twitter/replies/{post_id}

#### Retrieve Replies for a Post

Get all replies to a specific post.

#### Replies Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `post_id` | string | Yes | Post ID |

### GET /twitter/retweets/{post_id}

#### Get Retweeters of a Post

Retrieve list of users who retweeted a specific post.

#### Retweeters Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `post_id` | string | Yes | Post ID |

### GET /twitter/trends

#### Get X Trends

Retrieve trending topics on X.

#### Trends Response

Returns a list of trending topics with metrics.

### GET /web

#### SERP Web Search API

Standard search engine results page search.

#### Web Search Query Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes | Search query |

### GET /web/crawl

#### Crawl API

Crawl and extract content from web pages.

#### Crawl Query Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `url` | string | Yes | URL to crawl |

### POST /forecast

#### Numinous Forecasting

Create and retrieve forecasting jobs.

#### Creating a Forecast Job

**POST** with forecast parameters

#### Getting Forecast Results

**GET** with job ID to retrieve results

## SDKs

### Desearch API SDK

Python and JavaScript SDKs are available for easy integration.

### Python SDK

```bash
pip install desearch-api
```

### JavaScript SDK

```bash
npm install @desearch/api
```

See SDK specifications at [https://desearch.ai/docs/guide/sdk](https://desearch.ai/docs/guide/sdk)

## Integrations

### Model Context Protocol (MCP)

Integrate Desearch into MCP-compatible applications for seamless data retrieval.

### Function Calling

- **OpenAI**: Use with OpenAI function calling
- **Claude/Anthropic**: Use with Claude function calling

### RAG Frameworks

- **LangChain**: Full RAG integration available
- **LlamaIndex**: Integration for document indexing and retrieval

### Agent Frameworks

- **ElizaOS**: Agent integration for autonomous operations
- **CrewAI**: Multi-agent collaboration
- **OpenClaw**: Agentic framework support

### Browser Use

Integrate Desearch for browser automation and data extraction workflows.

### Numinous SN6

Integration with Numinous subnet for enhanced forecasting and analytics.

## Configuration

### API Console

Access the API console at [https://console.desearch.ai](https://console.desearch.ai) to:

- Manage API keys
- Monitor usage and quotas
- Configure integrations
- View billing information

### Pricing

Visit [https://desearch.ai/pricing](https://desearch.ai/pricing) for current pricing plans and tier details.

## Glossary

### Bittensor Subnet 22

The decentralized network powering Desearch, utilizing miners for search indexing and validators for quality assurance.

### Miner Link Scores

Quality scoring metrics provided by the Desearch network miners, indicating relevance and reliability of results.

### Streaming Results

Real-time streaming of search results as they are discovered and processed.

## Support

For inquiries, contact: [contact@desearch.ai](mailto:contact@desearch.ai)

### Additional Resources

- Website: [https://desearch.ai](https://desearch.ai)
- Twitter/X: [@desikiofficial](https://x.com/desikiofficial)
- GitHub: Available for community contributions
- Discord: Community discussions and support

## API Status

Monitor API status at [https://desearch.ai/api-status](https://desearch.ai/api-status)
