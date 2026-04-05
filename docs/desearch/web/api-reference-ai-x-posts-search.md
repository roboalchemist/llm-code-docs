<!--
source: https://desearch.ai/docs/api-reference
endpoint: POST AI X Posts Search
captured: 2026-04-04
-->
# POST AI X Posts Search — Desearch API Reference

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
/desearch/ai/search/links/twitter
AI Х Posts Search

The Х Posts Search API allows users to search for relevant links based on Х search queries with leveraging AI-powered models. This API analyze links from Х posts that match the given prompt. This API is useful for tracking trends, gathering insights, and retrieving real-time information from Х.

Base URL

https://api.desearch.ai
Body Parameters
prompt
string
required

Search query prompt

count
string

The number of results to return per source. Min 10. Max 200.

Default: 10

Responses
200
A JSON object mapping Х Search to its search results.
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
curl -X POST "https://api.desearch.ai/desearch/ai/search/links/twitter" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "prompt": "What are the recent sport events?"
}'
Try It!
RESPONSE
Schema
Copy
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
        "followings_count": 100,
        "listed_count": 10,
        "media_count": 50,
        "profile_image_url": "https://example.com/profile.jpg",
        "profile_banner_url": "https://example.com/banner.jpg",
        "statuses_count": 500,
        "verified": true,
        "is_blue_verified": true,
        "entities": {},
        "can_dm": true,
        "can_media_tag": true,
        "location": "Jamaica",
        "pinned_tweet_ids": [
          "123456789",
          "987654321"
        ],
        "professional": {}
      },
      "id": "987654321",
      "text": "This is an example tweet.",
      "reply_count": 10,
      "view_count": 1000,
      "retweet_count": 5,
      "like_count": 100,
      "quote_count": 2,
      "bookmark_count": 3,
      "url": "https://twitter.com/example_tweet",
      "created_at": "2023-01-01T00:00:00Z",
      "media": [],
      "is_quote_tweet": false,
      "is_retweet": false,
      "lang": "en",
      "conversation_id": "987654321",
      "in_reply_to_screen_name": "someuser",
      "in_reply_to_status_id": "987654320",
      "in_reply_to_user_id": "123456789",
      "quoted_status_id": "987654319",
      "quote": {
        "user": {},
        "id": "987654321",
        "text": "This is an example tweet.",
        "reply_count": 10,
        "view_count": 1000,
        "retweet_count": 5,
        "like_count": 100,
        "quote_count": 2,
        "bookmark_count": 3,
        "url": "https://twitter.com/example_tweet",
        "created_at": "2023-01-01T00:00:00Z",
        "media": [],
        "is_quote_tweet": false,
        "is_retweet": false,
        "lang": "en",
        "conversation_id": "987654321",
        "in_reply_to_screen_name": "someuser",
        "in_reply_to_status_id": "987654320",
        "in_reply_to_user_id": "123456789",
        "quoted_status_id": "987654319",
        "quote": {},
        "replies": [],
        "display_text_range": [
          0,
          280
        ],
        "entities": {},
        "extended_entities": {},
        "retweet": {}
      },
      "replies": [
        {
          "id": "987654321",
          "text": "This is an example tweet.",
          "reply_count": 10,
          "view_count": 1000,
          "retweet_count": 5,
          "like_count": 100,
          "quote_count": 2,
          "bookmark_count": 3,
          "url": "https://twitter.com/example_tweet",
          "created_at": "2023-01-01T00:00:00Z",
          "media": [],
          "is_quote_tweet": false,
          "is_retweet": false,
          "lang": "en",
          "conversation_id": "987654321",
          "in_reply_to_screen_name": "someuser",
          "in_reply_to_status_id": "987654320",
          "in_reply_to_user_id": "123456789",
          "quoted_status_id": "987654319",
          "replies": [],
          "display_text_range": [
            0,
            280
          ]
        }
      ],
      "display_text_range": [
        0,
        280
      ],
      "entities": {
        "hashtags": [],
        "media": [],
        "symbols": [],
        "timestamps": [],
        "urls": [],
        "user_mentions": []
      },
      "extended_entities": {
        "media": []
      },
      "retweet": {
        "user": {},
        "id": "987654321",
        "text": "This is an example tweet.",
        "reply_count": 10,
        "view_count": 1000,
        "retweet_count": 5,
        "like_count": 100,
        "quote_count": 2,
        "bookmark_count": 3,
        "url": "https://twitter.com/example_tweet",
        "created_at": "2023-01-01T00:00:00Z",
        "media": [],
        "is_quote_tweet": false,
        "is_retweet": false,
        "lang": "en",
        "conversation_id": "987654321",
        "in_reply_to_screen_name": "someuser",
        "in_reply_to_status_id": "987654320",
        "in_reply_to_user_id": "123456789",
        "quoted_status_id": "987654319",
        "quote": {},
        "replies": [],
        "display_text_range": [
          0,
          280
        ],
        "entities": {},
        "extended_entities": {},
        "retweet": {}
      }
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
