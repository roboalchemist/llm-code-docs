<!--
source: https://desearch.ai/docs/api-reference
endpoint: GET Get Forecast Result
captured: 2026-04-04
-->
# GET Get Forecast Result — Desearch API Reference

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
/numinous/forecasts/{prediction_id}
Get Forecast Result

Poll the status of a prediction job created via POST /numinous/forecasts. Poll every 5 seconds — jobs typically complete within 30–120 seconds. The `prediction_id` UUID acts as an access token; no API key is required for polling.

Base URL

https://api.desearch.ai
Query Parameters
prediction_id
string
required
Responses
200
Current job status and result when completed.
404
Prediction job not found
422
Validation Error
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
curl -X GET "https://api.desearch.ai/numinous/forecasts/{prediction_id}" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
Try It!
RESPONSE
Schema
Copy
{
  "prediction_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "status": "PENDING",
  "created_at": "2026-02-17T18:00:00Z",
  "result": {
    "prediction": 0.72,
    "forecaster_name": "pool_based_miner_forecaster",
    "forecasted_at": "2026-02-17T18:00:45Z",
    "metadata": {
      "miner_uid": 0,
      "miner_hotkey": "string",
      "pool": "string",
      "version_id": "string",
      "agent_name": "string",
      "version_number": 0,
      "raw_prediction": 0,
      "event_title": "string",
      "event_cutoff": "string",
      "reasoning": "string"
    },
    "parsed_fields": {
      "title": "string",
      "description": "string",
      "cutoff": "string",
      "topics": [
        "string"
      ]
    }
  },
  "error": "string"
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
