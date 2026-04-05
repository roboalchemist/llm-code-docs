<!--
source: https://desearch.ai/docs/guide/sdk/javascript-sdk
title: JavaScript SDK Specification - SDK Documentation | Desearch
captured: 2026-04-04
-->
# JavaScript SDK Specification - SDK Documentation | Desearch

Source: https://desearch.ai/docs/guide/sdk/javascript-sdk

---

Home
Guide
API Reference
SDKs
API Console
API Status
GitHub
Discord
Blog
Search guides...
⌘K
INTRODUCTION
Desearch AI
Desearch Console
Glossary
APIS
Desearch API
Desearch x Bittensor
API Keys
Authorization
Pricing and Billing
SDK
Desearch API SDK
Python SDK Specification
JavaScript SDK Specification
INTEGRATIONS
MCP
OpenAI Wrapper
Function Calling with GPT
Function Calling with Claude
RAG with LangChain x Desearch
RAG with LlmaIndex x Desearch
ElizaOs Agents with Desearch
CrewAI Agents with Desearch
Browser Use x Desearch
OpenClaw Agent with Desearch
Numinous SN6 × Desearch Integration
USE CASES
Search Engine Use Cases
AI-Driven Chat Use Cases
Intelligent Agent Task Automation
CAPABILITIES
X (Twitter) Queries
JavaScript SDK Specification

The Desearch JavaScript SDK provides a seamless way to integrate AI-powered search functionalities into your applications. This guide outlines the installation process, available methods, and example implementations.

Installation

To install the desearch-js SDK, use the following command:

BASH
npm install desearch-js

Once installed, you can initialize the Desearch client as follows:

TYPESCRIPT
import Desearch from "desearch-js";

const desearch = new Desearch("your-api-key");

📘 API Keys

Get API Key (Follow link to get your API key) https://console.desearch.ai/api-keys.

Methods and Usage

The Desearch SDK provides the following methods for AI-powered search:

aiSearch Method

AI-powered multi-source contextual search. Searches across web, X (Twitter), Reddit, YouTube, HackerNews, Wikipedia, and arXiv and returns results with optional AI-generated summaries.

Example Usage
TYPESCRIPT
desearch
  .aiSearch({
    prompt: "Bittensor",
    tools: ["web", "hackernews", "reddit", "wikipedia", "youtube", "twitter", "arxiv"],
    date_filter: "PAST_24_HOURS",
    result_type: "LINKS_WITH_FINAL_SUMMARY",
    count: 20,
  })
  .then((result) => {
    console.log(result);
  });
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| prompt | string | Yes | — | Search query prompt |
| tools | (ToolEnum \| string)[] | Yes | — | A list of tools to be used for the search |
| start_date | string \| null | No | null | The start date for the search query (YYYY-MM-DDTHH:MM:SSZ) |
| end_date | string \| null | No | null | The end date for the search query (YYYY-MM-DDTHH:MM:SSZ) |
| date_filter | DateFilterEnum \| null | No | 'PAST_24_HOURS' | Predefined date filter for search results |
| result_type | ResultTypeEnum \| null | No | 'LINKS_WITH_FINAL_SUMMARY' | The result type for the search |
| system_message | string \| null | No | '' | System message for the search |
| scoring_system_message | string \| null | No | null | System message for scoring the response |
| count | number \| null | No | 10 | Number of results per source (10–200) |

Sample Response
JSON
{
    "youtube_search_results": {
        "organic_results": [
        {
            "title": "Did The FED Do The Impossible? [Huge Implications For Bitcoin]",
            "link": "https://www.youtube.com/watch?v=Ycq1u2zWfr8",
            "snippet": "Did we avoid a recession and is there still more upside for Bitcoin? GET MY FREE NEWSLETTER ...",
            "summary_description": "Did The FED Do The Impossible? [Huge Implications For Bitcoin]"
        }
        ]
    },
    // ... other search results ...
}
aiWebLinksSearch Method

Search for raw links across web sources (web, HackerNews, Reddit, Wikipedia, YouTube, arXiv). Returns structured link results without AI summaries.

Example Usage
TYPESCRIPT
desearch
  .aiWebLinksSearch({
    prompt: "What are the recent sport events?",
    tools: ["web", "hackernews", "reddit", "wikipedia", "youtube", "arxiv"],
    count: 20,
  })
  .then((result) => {
    console.log(result);
  });

Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| prompt | string | Yes | — | Search query prompt |
| tools | (WebToolEnum \| string)[] | Yes | — | List of tools to search with |
| count | number \| null | No | 10 | Number of results per source (10–200) |

aiXLinksSearch Method

Search for X (Twitter) post links matching a prompt using AI-powered models. Returns tweet objects from the miner network.

Example Usage
TYPESCRIPT
desearch
  .aiXLinksSearch({
    prompt: "What are the recent sport events?",
    count: 20,
  })
  .then((result) => {
    console.log(result);
  });

Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| prompt | string | Yes | — | Search query prompt |
| count | number \| null | No | 10 | Number of results per source (10–200) |

Sample Response
JSON
{
    "miner_tweets": [
        {
        "user": {
            "id": "123456789",
            "url": "https://twitter.com/example_user",
            "name": "John Doe",
            "username": "johndoe",
            "created_at": "2023-01-01T00:00:00Z",
            "description": "This is an example user description.",
            "favourites_count": 100,
            "followers_count": 1500,
            "listed_count": 10,
            "media_count": 50,
            "profile_image_url": "https://example.com/profile.jpg",
            "statuses_count": 500,
            "verified": true
        },
        "id": "987654321",
        "text": "This is an example tweet.",
        "reply_count": 10,
        "retweet_count": 5,
        "like_count": 100,
        "view_count": 1000,
        "quote_count": 2,
        "impression_count": 1500,
        "bookmark_count": 3,
        "url": "https://twitter.com/example_tweet",
        "created_at": "2023-01-01T00:00:00Z",
        "media": [],
        "is_quote_tweet": false,
        "is_retweet": false,
        "entities": {},
        "summary_description": "This is a summary of the tweet."
        }
    ]
}
xSearch Method

X (Twitter) search with extensive filtering options: date range, user, language, verification status, media type (image/video/quote), and engagement thresholds (min likes, retweets, replies). Sort by Top or Latest.

Example Usage
TYPESCRIPT
desearch
  .xSearch({
    query: "Whats going on with Bittensor",
    sort: "Top",
    user: "elonmusk",
    start_date: "2024-12-01",
    end_date: "2025-02-25",
    lang: "en",
    verified: true,
    blue_verified: true,
    count: 20,
  })
  .then((result) => {
    console.log(result);
  });

Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| query | string | Yes | — | Advanced search query |
| sort | string \| null | No | 'Top' | Sort by Top or Latest |
| user | string \| null | No | null | User to search for |
| start_date | string \| null | No | null | Start date in UTC (YYYY-MM-DD) |
| end_date | string \| null | No | null | End date in UTC (YYYY-MM-DD) |
| lang | string \| null | No | null | Language code (e.g., en, es, fr) |
| verified | boolean \| null | No | null | Filter for verified users |
| blue_verified | boolean \| null | No | null | Filter for blue checkmark verified users |
| is_quote | boolean \| null | No | null | Include only tweets with quotes |
| is_video | boolean \| null | No | null | Include only tweets with videos |
| is_image | boolean \| null | No | null | Include only tweets with images |
| min_retweets | number \| string \| null | No | null | Minimum number of retweets |
| min_replies | number \| string \| null | No | null | Minimum number of replies |
| min_likes | number \| string \| null | No | null | Minimum number of likes |
| count | number \| null | No | 20 | Number of tweets to retrieve (1–100) |

Sample Response
JSON
{
    "user": {
    "id": "1453417787746029577",
    "url": "https://x.com/firsttensor",
    "name": "Firsττensor - Biττensor Validator",
    "username": "firsttensor",
    "created_at": "2021-10-27",
    "followers_count": 4669,
    "profile_image_url": "https://pbs.twimg.com/profile_images/1890150870563614720/L3PGGoUs_normal.jpg"
    },
    "id": "1891203972003684353",
    "text": "How to Stake/Unstake $TAO to the FirstTensor Validator Using the YUMA Platform.\n\n✅ Make sure your wallet is imported into the Polkadot.js or Bittensor Wallet extension.\n\n👇Share this so everyone can use it! \n\n#bittensor #delegate #root",
    "retweet_count": 2,
    "like_count": 7,
    "created_at": "2025-02-16",
    "url": "https://x.com/firsttensor/status/1891203972003684353",
    "media": [
    {
        "media_url": "https://pbs.twimg.com/ext_tw_video_thumb/1891202584314105856/pu/img/nzOtIMS_Zz7YWHJY.jpg",
        "type": "video"
    }
    ],
    "hashtags": ["bittensor", "delegate", "root"]
}
xPostsByUrls Method

Fetch full post data for a list of X (Twitter) post URLs. Returns metadata, content, and engagement metrics for each URL.

Example Usage
TYPESCRIPT
desearch
  .xPostsByUrls({
    urls: ["https://x.com/RacingTriple/status/1892527552029499853"],
  })
  .then((result) => {
    console.log(result);
  });

Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| urls | string[] | Yes | — | List of post URLs to retrieve |

xPostById Method

Fetch a single X (Twitter) post by its unique ID. Returns metadata, content, and engagement metrics.

Example Usage
TYPESCRIPT
desearch
  .xPostById({
    id: "1892527552029499853",
  })
  .then((result) => {
    console.log(result);
  });

Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| id | string | Yes | — | The unique ID of the post |

xPostsByUser Method

Search X (Twitter) posts by a specific user, with optional keyword filtering.

Example Usage
TYPESCRIPT
desearch
  .xPostsByUser({
    user: "elonmusk",
    query: "Whats going on with Bittensor",
    count: 20,
  })
  .then((result) => {
    console.log(result);
  });

Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| user | string | Yes | — | User to search for |
| query | string | No | '' | Advanced search query |
| count | number | No | 10 | Number of tweets to retrieve (1–100) |
xPostRetweeters Method

Retrieve the list of users who retweeted a specific post by its ID. Supports cursor-based pagination.

Example Usage
TYPESCRIPT
desearch
  .xPostRetweeters({
    id: "1982770537081532854",
  })
  .then((result) => {
    console.log(result);
  });
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| id | string | Yes | — | The ID of the post to get retweeters for |
| cursor | string \| null | No | null | Cursor for pagination |

xUserPosts Method

Retrieve a user's timeline posts by their username. Fetches the latest tweets posted by that user. Supports cursor-based pagination.

Example Usage
TYPESCRIPT
desearch
  .xUserPosts({
    username: "elonmusk",
  })
  .then((result) => {
    console.log(result);
  });
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| username | string | Yes | — | Username to fetch posts for |
| cursor | string \| null | No | null | Cursor for pagination |

xUserReplies Method

Fetch tweets and replies posted by a specific user, with optional keyword filtering.

Example Usage
TYPESCRIPT
desearch
  .xUserReplies({
    user: "elonmusk",
    count: 20,
    query: "latest news on AI",
  })
  .then((result) => {
    console.log(result);
  });
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| user | string | Yes | — | The username of the user to search for |
| count | number | No | 10 | The number of tweets to fetch (1–100) |
| query | string | No | '' | Advanced search query |

xPostReplies Method

Fetch replies to a specific X (Twitter) post by its post ID.

Example Usage
TYPESCRIPT
desearch
  .xPostReplies({
    post_id: "1234567890",
    count: 20,
    query: "latest news on AI",
  })
  .then((result) => {
    console.log(result);
  });
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| post_id | string | Yes | — | The ID of the post to search for |
| count | number | No | 10 | The number of tweets to fetch (1–100) |
| query | string | No | '' | Advanced search query |

xTrends Method

Retrieve trending topics on X for a given location using its WOEID (Where On Earth ID).

Example Usage
TYPESCRIPT
desearch
  .xTrends({
    woeid: 23424977,
    count: 30,
  })
  .then((result) => {
    console.log(result);
  });
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| woeid | number | Yes | — | The WOEID of the location (e.g. 23424977 for United States) |
| count | number \| null | No | 30 | The number of trends to return (30–100) |

webSearch Method

SERP web search. Returns paginated web search results, replicating a typical search engine experience.

Example Usage
TYPESCRIPT
desearch
  .webSearch({
    query: "latest news on AI",
    start: 10,
  })
  .then((result) => {
    console.log(result);
  });
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| query | string | Yes | — | The search query string |
| start | number | No | 0 | How many results to skip for pagination (0, 10, 20, etc.) |

Sample Response
JSON
{
    "data": [
        {
            "title": "AI News & Artificial Intelligence | TechCrunch",
            "snippet": "TechCrunch covers the latest news and trends on artificial intelligence and machine learning tech, the companies building them, and the ethical issues they raise.",
            "link": "https://techcrunch.com/category/artificial-intelligence/",
            "date": null
        },
        {
            "title": "Artificial Intelligence News -- ScienceDaily",
            "snippet": "Find the latest news and research on artificial intelligence, robotics, machine learning, and related fields.",
            "link": "https://www.sciencedaily.com/news/computers_math/artificial_intelligence/",
            "date": null
        }
    ]
}
webCrawl Method

Crawl a URL and return its content as plain text or HTML.

Example Usage
TYPESCRIPT
desearch
  .webCrawl({
    url: "https://en.wikipedia.org/wiki/Artificial_intelligence",
    format: "html",
  })
  .then((result) => {
    console.log(result);
  });
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| url | string | Yes | — | URL to crawl |
| format | 'html' \| 'text' | No | 'text' | Format of the content to be returned |

Check out example use cases here:

desearch-js-examples

🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
