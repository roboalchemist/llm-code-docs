<!--
source: https://desearch.ai/docs/api-reference
endpoint: POST AI Web Search
captured: 2026-04-04
-->
# POST AI Web Search — Desearch API Reference

Home
Guide
API Reference
SDKs
API Console
API Reference

v1.0.0

AI SEARCH
POST
AI Contextual Search
POST
AI Web Search
POST
AI Х Posts Search
X SEARCH
GET
X Search API
GET
Fetch Posts by URLs
GET
Retrieve Post by ID
GET
Search X Posts by User
GET
Get Retweeters of a Post
GET
Get X Posts by Username
GET
Fetch User's Tweets and Replies
GET
Retrieve Replies for a Post
GET
Get X Trends
WEB SEARCH
GET
SERP Web Search API
GET
Crawl API
NUMINOUS FORECASTING
POST
Create Forecast Job
GET
Get Forecast Result
POST
/desearch/ai/search/links/web
AI Web Search

This API allows users to search for links related to a given query (prompt) using multiple tools, excluding X (Twitter) Search. The API returns a list of relevant sources from selected platforms such as web pages, YouTube, Wikipedia, and ArXiv.

Base URL

https://api.desearch.ai
Body Parameters
prompt
string
required

Search query prompt

tools
array
required

List of tools to search with

web
hackernews
reddit
wikipedia
youtube
arxiv
count
string

The number of results to return per source. Min 10. Max 200.

Default: 10

Responses
200
A JSON object mapping tool names to their search results.
301
Moved Permanently
304
Not Modified
401
Unauthorized
422
Validation Error
429
Too Many Requests
500
Internal Server Error
Authorization

Your API key will be sent in the Authorization header

Shell
Node
JavaScript
Python
Request
Copy
curl -X POST "https://api.desearch.ai/desearch/ai/search/links/web" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "prompt": "What are the recent sport events?",
  "tools": [
    "web",
    "hackernews",
    "reddit",
    "wikipedia",
    "youtube",
    "arxiv"
  ]
}'
Try It!
RESPONSE
Schema
Copy
{
  "youtube_search_results": [
    {
      "title": "Title",
      "snippet": "Snippet",
      "link": "https://example.com"
    }
  ],
  "hacker_news_search_results": [
    {
      "title": "Title",
      "snippet": "Snippet",
      "link": "https://example.com"
    }
  ],
  "reddit_search_results": [
    {
      "title": "Title",
      "snippet": "Snippet",
      "link": "https://example.com"
    }
  ],
  "arxiv_search_results": [
    {
      "title": "Title",
      "snippet": "Snippet",
      "link": "https://example.com"
    }
  ],
  "wikipedia_search_results": [
    {
      "title": "Title",
      "snippet": "Snippet",
      "link": "https://example.com"
    }
  ],
  "search_results": [
    {
      "title": "Title",
      "snippet": "Snippet",
      "link": "https://example.com"
    }
  ]
}

Possible status codes:

200
401
422
429
500
🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
