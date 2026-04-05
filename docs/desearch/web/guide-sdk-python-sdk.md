<!--
source: https://desearch.ai/docs/guide/sdk/python-sdk
title: Python SDK Specification - SDK Documentation | Desearch
captured: 2026-04-04
-->
# Python SDK Specification - SDK Documentation | Desearch

Source: https://desearch.ai/docs/guide/sdk/python-sdk

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
Python SDK Specification

The Desearch Python SDK provides a seamless way to integrate AI-powered search functionalities into your applications. This guide outlines the installation process, available methods, and example implementations.

Installation

To install the desearch-py SDK, use the following command.

BASH
pip install desearch-py

Once installed, you can instantiate the Desearch client as follows:

PYTHON
import asyncio
from desearch_py import Desearch

async def main():
    async with Desearch(api_key="your_api_key") as desearch:
        result = await desearch.ai_search(
            prompt="Bittensor",
            tools=["web", "twitter"],
        )
        print(result)

asyncio.run(main())

📘 API Keys

Get API Key (Follow link to get your API key) https://console.desearch.ai/api-keys.

Methods and Usage

The Desearch Python SDK provides the following methods for AI-powered search:

ai_search Method

AI-powered multi-source contextual search. Searches across web, X (Twitter), Reddit, YouTube, HackerNews, Wikipedia, and arXiv and returns results with optional AI-generated summaries. Supports streaming responses.

Example Usage
PYTHON
result = await desearch.ai_search(
    prompt="Bittensor",
    tools=["web", "hackernews", "reddit", "wikipedia", "youtube", "twitter", "arxiv"],
    date_filter="PAST_24_HOURS",
    result_type="LINKS_WITH_FINAL_SUMMARY",
    count=20,
)
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| prompt | str | Yes | — | Search query prompt |
| tools | List[str] | Yes | — | List of tools to search with (e.g. web, twitter, reddit, hackernews, youtube, wikipedia, arxiv) |
| start_date | Optional[str] | No | None | Start date in UTC (YYYY-MM-DDTHH:MM:SSZ) |
| end_date | Optional[str] | No | None | End date in UTC (YYYY-MM-DDTHH:MM:SSZ) |
| date_filter | Optional[str] | No | PAST_24_HOURS | Predefined date filter for search results |
| result_type | Optional[str] | No | LINKS_WITH_FINAL_SUMMARY | Result type (ONLY_LINKS or LINKS_WITH_FINAL_SUMMARY) |
| system_message | Optional[str] | No | None | System message for the search |
| scoring_system_message | Optional[str] | No | None | System message for scoring the response |
| count | Optional[int] | No | None | Number of results per source (10–200) |

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
    "hacker_news_search_results": {
        "organic_results": [
        {
            "title": "latest",
            "link": "https://news.ycombinator.com/latest?id=42816511",
            "snippet": "The streaming app for the Paris Olympics was a revolution from which I can never go back to OTA coverage.",
            "summary_description": ""
        }
        ]
    },
    "completion": {
        "key_posts": [{ "text": "This is an example post text.", "url": "https://x.com/example_post" }],
        "key_tweets": [{ "text": "This is an example tweet text.", "url": "https://x.com/example_tweet" }],
        "key_news": [{ "text": "This is an example news text.", "url": "https://news.example.com/123" }],
        "key_sources": [{ "text": "This is an example source text.", "url": "https://www.example.com" }],
        "twitter_summary": "This is an example Twitter summary.",
        "summary": "This is an example summary.",
        "reddit_summary": "This is an example summary.",
        "hacker_news_summary": "This is an example summary."
    }
}

Here are the details of the above response. The return type depends on the result_type parameter:

A JSON object mapping tool names to their search results with a final AI-generated summary: When result_type is LINKS_WITH_FINAL_SUMMARY
A JSON object with only link results: When result_type is ONLY_LINKS
ai_web_links_search Method

Search for raw links across web sources (web, HackerNews, Reddit, Wikipedia, YouTube, arXiv). Returns structured link results without AI summaries.

Example Usage
PYTHON
result = await desearch.ai_web_links_search(
    prompt="What are the recent sport events?",
    tools=["web", "hackernews", "reddit", "wikipedia", "youtube", "arxiv"],
    count=20,
)

Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| prompt | str | Yes | — | Search query prompt |
| tools | List[str] | Yes | — | List of web tools to search with (e.g. web, hackernews, reddit, wikipedia, youtube, arxiv) |
| count | Optional[int] | No | None | Number of results per source (10–200) |

ai_x_links_search Method

Search for X (Twitter) post links matching a prompt using AI-powered models. Returns tweet objects from the miner network.

Example Usage
PYTHON
result = await desearch.ai_x_links_search(
    prompt="What are the recent sport events?",
    count=20,
)

Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| prompt | str | Yes | — | Search query prompt |
| count | Optional[int] | No | None | Number of results to return (10–200) |

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
x_search Method

X (Twitter) search with extensive filtering options: date range, user, language, verification status, media type (image/video/quote), and engagement thresholds (min likes, retweets, replies). Sort by Top or Latest.

Input Example
PYTHON
result = await desearch.x_search(
    query="Whats going on with Bittensor",
    sort="Top",
    user="elonmusk",
    start_date="2024-12-01",
    end_date="2025-02-25",
    lang="en",
    verified=True,
    blue_verified=True,
    count=20,
)

Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| query | str | Yes | — | Search query. For syntax, check https://docs.desearch.ai/guides/capabilities/twitter-queries |
| sort | Optional[str] | No | Top | Sort by Top or Latest |
| user | Optional[str] | No | None | User to search for |
| start_date | Optional[str] | No | None | Start date in UTC (YYYY-MM-DD) |
| end_date | Optional[str] | No | None | End date in UTC (YYYY-MM-DD) |
| lang | Optional[str] | No | None | Language code (e.g. en, es, fr) |
| verified | Optional[bool] | No | None | Filter for verified users |
| blue_verified | Optional[bool] | No | None | Filter for blue checkmark verified users |
| is_quote | Optional[bool] | No | None | Include only tweets with quotes |
| is_video | Optional[bool] | No | None | Include only tweets with videos |
| is_image | Optional[bool] | No | None | Include only tweets with images |
| min_retweets | Optional[Union[int, str]] | No | None | Minimum number of retweets |
| min_replies | Optional[Union[int, str]] | No | None | Minimum number of replies |
| min_likes | Optional[Union[int, str]] | No | None | Minimum number of likes |
| count | Optional[int] | No | 20 | Number of tweets to retrieve (1–100) |

x_posts_by_urls Method

Fetch full post data for a list of X (Twitter) post URLs. Returns metadata, content, and engagement metrics for each URL.

Example Usage
PYTHON
result = await desearch.x_posts_by_urls(
    urls=["https://x.com/RacingTriple/status/1892527552029499853"],
)

Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| urls | List[str] | Yes | — | List of tweet URLs to retrieve |

x_post_by_id Method

Fetch a single X (Twitter) post by its unique ID. Returns metadata, content, and engagement metrics.

Example Usage
PYTHON
result = await desearch.x_post_by_id(
    id="1892527552029499853",
)

Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| id | str | Yes | — | The unique ID of the post |

x_posts_by_user Method

Search X (Twitter) posts by a specific user, with optional keyword filtering.

Example Usage
PYTHON
result = await desearch.x_posts_by_user(
    user="elonmusk",
    query="Whats going on with Bittensor",
    count=20,
)

Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| user | str | Yes | — | User to search for |
| query | Optional[str] | No | None | Advanced search query |
| count | Optional[int] | No | None | Number of tweets to retrieve (1–100) |
x_post_retweeters Method

Retrieve the list of users who retweeted a specific post by its ID. Supports cursor-based pagination.

Example Usage
PYTHON
result = await desearch.x_post_retweeters(
    id="1982770537081532854",
)
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| id | str | Yes | — | The ID of the post to get retweeters for |
| cursor | Optional[str] | No | None | Cursor for pagination |

x_user_posts Method

Retrieve a user's timeline posts by their username. Fetches the latest tweets posted by that user. Supports cursor-based pagination.

Example Usage
PYTHON
result = await desearch.x_user_posts(
    username="elonmusk",
)
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| username | str | Yes | — | Username to fetch posts for |
| cursor | Optional[str] | No | None | Cursor for pagination |

x_user_replies Method

Fetch tweets and replies posted by a specific user, with optional keyword filtering.

Example Usage
PYTHON
result = await desearch.x_user_replies(
    user="elonmusk",
    query="latest news on AI",
    count=20,
)
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| user | str | Yes | — | The username of the user to search for |
| count | Optional[int] | No | None | The number of tweets to fetch (1–100) |
| query | Optional[str] | No | None | Advanced search query |

x_post_replies Method

Fetch replies to a specific X (Twitter) post by its post ID.

Example Usage
PYTHON
result = await desearch.x_post_replies(
    post_id="1234567890",
    query="latest news on AI",
    count=20,
)
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| post_id | str | Yes | — | The ID of the post to search for |
| count | Optional[int] | No | None | The number of tweets to fetch (1–100) |
| query | Optional[str] | No | None | Advanced search query |

x_trends Method

Retrieve trending topics on X for a given location using its WOEID (Where On Earth ID).

Example Usage
PYTHON
result = await desearch.x_trends(
    woeid=23424977,
    count=30,
)
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| woeid | int | Yes | — | The WOEID of the location (e.g. 23424977 for United States) |
| count | Optional[int] | No | None | The number of trends to return (30–100) |

web_search Method

SERP web search. Returns paginated web search results, replicating a typical search engine experience.

Example Usage
PYTHON
result = await desearch.web_search(
    query="latest news on AI",
    start=10,
)
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| query | str | Yes | — | The search query string |
| start | Optional[int] | No | 0 | Number of results to skip for pagination |

Sample Response
JSON
{
    "data": [
        {
        "title": "EXCLUSIVE Major coffee buyers face losses as Colombia ...",
        "snippet": "Coffee farmers in Colombia, the world's No. 2 arabica producer, have failed to deliver up to 1 million bags of beans this year or nearly 10% ...",
        "link": "https://www.reuters.com/world/americas/exclusive-major-coffee-buyers-face-losses-colombia-farmers-fail-deliver-2021-10-11/",
        "date": "21 hours ago",
        "source": "Reuters",
        "author": "Reuters"
        }
    ]
}
web_crawl Method

Crawl a URL and return its content as plain text or HTML.

Example Usage
PYTHON
result = await desearch.web_crawl(
    url="https://en.wikipedia.org/wiki/Artificial_intelligence",
    format="html",
)
Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| url | str | Yes | — | URL to crawl |
| format | Optional[str] | No | text | Format of content (html or text) |

Check out example use cases here:

desearch-py-examples

🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
