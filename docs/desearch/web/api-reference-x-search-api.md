<!--
source: https://desearch.ai/docs/api-reference
endpoint: GET X Search API
captured: 2026-04-04
-->
# GET X Search API — Desearch API Reference

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
/twitter
X Search API

The X Search API enables users to retrieve relevant links and tweets based on specified search queries without utilizing AI-driven models. It analyzes links from X posts that align with the provided search criteria.

Base URL

https://api.desearch.ai
Query Parameters
query
string
required

Advanced search query

sort
string

Sort by Top or Latest

Default: Top

user
string

User to search for

start_date
string

Start date in UTC (YYYY-MM-DD format)

Select date (YYYY-MM-DD)
end_date
string

End date in UTC (YYYY-MM-DD format)

Select date (YYYY-MM-DD)
lang
string

Language code (e.g., en, es, fr)

verified
string

Filter for verified users

blue_verified
string

Filter for blue checkmark verified users

is_quote
string

Include only tweets with quotes

is_video
string

Include only tweets with videos

is_image
string

Include only tweets with images

min_retweets
string

Minimum number of retweets

min_replies
string

Minimum number of replies

min_likes
string

Minimum number of likes

count
string

Number of tweets to retrieve

Default: 20

Responses
200
A JSON object mapping X Search to its search results.
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
curl -X GET "https://api.desearch.ai/twitter?query=Whats+going+on+with+Bittensor" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
Try It!
RESPONSE
Schema
Copy
[
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
      "professional": {
        "professional_type": "Business",
        "category": []
      }
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
        "can_dm": true,
        "can_media_tag": true,
        "location": "Jamaica",
        "pinned_tweet_ids": [
          "123456789",
          "987654321"
        ]
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
        "display_text_range": [
          0,
          280
        ]
      },
      "replies": [
        {}
      ],
      "display_text_range": [
        0,
        280
      ],
      "entities": {},
      "extended_entities": {},
      "retweet": {
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
        "display_text_range": [
          0,
          280
        ]
      }
    },
    "replies": [
      {
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
    ],
    "display_text_range": [
      0,
      280
    ],
    "entities": {
      "hashtags": [
        {}
      ],
      "media": [
        {}
      ],
      "symbols": [
        {}
      ],
      "timestamps": [],
      "urls": [
        {}
      ],
      "user_mentions": [
        {}
      ]
    },
    "extended_entities": {
      "media": [
        {}
      ]
    },
    "retweet": {
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
        "can_dm": true,
        "can_media_tag": true,
        "location": "Jamaica",
        "pinned_tweet_ids": [
          "123456789",
          "987654321"
        ]
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
        "display_text_range": [
          0,
          280
        ]
      },
      "replies": [
        {}
      ],
      "display_text_range": [
        0,
        280
      ],
      "entities": {},
      "extended_entities": {},
      "retweet": {
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
        "display_text_range": [
          0,
          280
        ]
      }
    }
  }
]

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
