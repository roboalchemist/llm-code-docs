<!--
source: https://desearch.ai/docs/api-reference
endpoint: POST Create Forecast Job
captured: 2026-04-04
-->
# POST Create Forecast Job — Desearch API Reference

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
/numinous/forecasts
Create Forecast Job

Submit a forecasting question to the Numinous AI superforecasting system powered by Bittensor Subnet 6. Returns a prediction job ID to poll for results. Supports two modes: **structured** (title + description + cutoff) for precise results, or **query** (natural language question) for quick exploration.

Base URL

https://api.desearch.ai
Body Parameters
title
string
description
string
cutoff
string
topics
string
query
string
agent_version_id
string
Responses
202
A prediction job ID and initial PENDING status.
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
curl -X POST "https://api.desearch.ai/numinous/forecasts" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
Try It!
RESPONSE
Schema
Copy
{
  "prediction_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "status": "PENDING"
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
