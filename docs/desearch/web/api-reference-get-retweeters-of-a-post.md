<!--
source: https://desearch.ai/docs/api-reference
endpoint: GET Get Retweeters of a Post
captured: 2026-04-04
-->
# GET Get Retweeters of a Post — Desearch API Reference

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
/twitter/post/retweeters
Get Retweeters of a Post

Retrieve the list of users who retweeted a specific post by its ID. Supports pagination via cursor.

Base URL

https://api.desearch.ai
Query Parameters
id
string
required

The ID of the post to get retweeters for

cursor
string

Cursor for pagination

Responses
200
A JSON object containing the list of users who retweeted the post.
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
curl -X GET "https://api.desearch.ai/twitter/post/retweeters?id=1982770537081532854" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
Try It!
RESPONSE
Schema
Copy
{
  "users": [
    {
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
      "entities": {
        "description": {},
        "url": {}
      },
      "can_dm": true,
      "can_media_tag": true,
      "location": "Jamaica",
      "pinned_tweet_ids": [
        "123456789",
        "987654321"
      ],
      "professional": {
        "professional_type": "Business",
        "category": [
          {}
        ]
      }
    }
  ],
  "next_cursor": "string"
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
