<!--
source: https://desearch.ai/docs/api-reference
endpoint: GET Get X Trends
captured: 2026-04-04
-->
# GET Get X Trends — Desearch API Reference

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
GET
/twitter/trends
Get X Trends

Retrieve trending topics on X for a given location using its WOEID (Where On Earth ID).

Base URL

https://api.desearch.ai
Query Parameters
woeid
integer
required

The WOEID of the location (e.g. 23424977 for United States). WOEID List: https://gist.github.com/tedyblood/5bb5a9f78314cc1f478b3dd7cde790b9

count
string

The number of trends to return. Minimum is 30, maximum is 100.

Default: 30

Responses
200
A JSON object containing the list of trending topics.
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
curl -X GET "https://api.desearch.ai/twitter/trends?woeid=23424977" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
Try It!
RESPONSE
Schema
Copy
{
  "trends": [
    {
      "name": "Name",
      "query": "string",
      "rank": 0
    }
  ],
  "woeid": {
    "name": "Name",
    "id": 0
  }
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
