<!--
source: https://desearch.ai/docs/api-reference
endpoint: POST AI Contextual Search
captured: 2026-04-04
-->
# POST AI Contextual Search — Desearch API Reference

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
/desearch/ai/search
AI Contextual Search

The Desearch API allows you to perform AI-powered web searches, gathering relevant information from multiple sources, including web pages, research papers, and social media discussions.

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

A list of tools to be used for the search

web
hackernews
reddit
wikipedia
youtube
twitter
arxiv
start_date
string

The start date for the search query. Format: YYYY-MM-DDTHH:MM:SSZ (UTC)

Select date (YYYY-MM-DD)
end_date
string

The end date for the search query. Format: YYYY-MM-DDTHH:MM:SSZ (UTC)

Select date (YYYY-MM-DD)
date_filter
string

Predefined date filters for the search results, or you can use specific start and end dates

Default: PAST_24_HOURS

streaming
boolean

Whether to stream results

Default: false

result_type
string

The result type to be used for the search

Default: LINKS_WITH_FINAL_SUMMARY

system_message
string

The system message to be used for the search

Default:

scoring_system_message
string

System message for scoring the response

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
curl -X POST "https://api.desearch.ai/desearch/ai/search" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "prompt": "Bittensor",
  "tools": [
    "web",
    "hackernews",
    "reddit",
    "wikipedia",
    "youtube",
    "twitter",
    "arxiv"
  ],
  "streaming": false
}'
Try It!
RESPONSE
Schema
Copy
{
  "hacker_news_search": [
    {
      "link": "https://news.ycombinator.com/item?id=35114983",
      "snippet": "Mar 12, 2023   �   As a decentralized AI network, Bittensor leverages the power of AI to drive innovation and collaboration on a global scale.",
      "title": "How Bittensor Is Pioneering a New Era of AI Innovation - Hacker News"
    }
  ],
  "reddit_search": [
    {
      "link": "https://www.reddit.com/r/bittensor_/comments/1blm5iv/thinking_of_going_in_big_on_bittensor/",
      "snippet": "Mar 23, 2024   �   I have great hopes for Bittensor and am about to commit to a sizeable position to which I will probably be adding over the coming months and even years.",
      "title": "Thinking of going in big on Bittensor : r/bittensor\_ - Reddit"
    }
  ],
  "search": [
    {
      "link": "https://www.thebigwhale.io/tokens/bittensor",
      "snippet": "Bittensor (TAO) is a decentralized, open-source, and permissionless machine learning network that transforms machine intelligence into a tradable commodity.",
      "title": "What is Bittensor?"
    }
  ],
  "youtube_search": [
    {
      "link": "https://www.youtube.com/watch?v=tDWhnsZB6XI",
      "snippet": "In this video, I break down exactly how I'm maximizing my $TAO stack through smart staking strategies on the Bittensor network ...",
      "title": "TAO (Bittensor) is PUMPING - how to make more profit with Staking 💰"
    }
  ],
  "tweets": [
    {
      "bookmark_count": 2,
      "conversation_id": "1932946234920349827",
      "created_at": "2025-06-11T23:41:09.000Z",
      "display_text_range": [
        0,
        269
      ],
      "entities": {
        "hashtags": [],
        "media": [
          {
            "display_url": "pic.x.com/L1icjTabYS",
            "expanded_url": "https://x.com/HOSS_ibc/status/1932946234920349827/photo/1",
            "ext_media_availability": {
              "status": "Available"
            },
            "features": {
              "large": {
                "faces": [
                  {
                    "h": 77,
                    "w": 77,
                    "x": 1877,
                    "y": 521
                  },
                  {
                    "h": 93,
                    "w": 93,
                    "x": 971,
                    "y": 571
                  }
                ]
              },
              "medium": {
                "faces": [
                  {
                    "h": 45,
                    "w": 45,
                    "x": 1100,
                    "y": 305
                  },
                  {
                    "h": 55,
                    "w": 55,
                    "x": 569,
                    "y": 335
                  }
                ]
              },
              "orig": {
                "faces": [
                  {
                    "h": 137,
                    "w": 137,
                    "x": 3301,
                    "y": 917
                  },
                  {
                    "h": 165,
                    "w": 165,
                    "x": 1708,
                    "y": 1005
                  }
                ]
              },
              "small": {
                "faces": [
                  {
                    "h": 25,
                    "w": 25,
                    "x": 623,
                    "y": 173
                  },
                  {
                    "h": 31,
                    "w": 31,
                    "x": 322,
                    "y": 189
                  }
                ]
              }
            },
            "id_str": "1932944082281574400",
            "indices": [
              270,
              293
            ],
            "media_key": "3_1932944082281574400",
            "media_url_https": "https://pbs.twimg.com/media/GtMyZtMWMAAPfq9.jpg",
            "original_info": {
              "focus_rects": [
                {
                  "h": 1800,
                  "w": 3214,
                  "x": 0,
                  "y": 0
                },
                {
                  "h": 1800,
                  "w": 1800,
                  "x": 0,
                  "y": 0
                },
                {
                  "h": 1800,
                  "w": 1579,
                  "x": 0,
                  "y": 0
                },
                {
                  "h": 1800,
                  "w": 900,
                  "x": 0,
                  "y": 0
                },
                {
                  "h": 1800,
                  "w": 3600,
                  "x": 0,
                  "y": 0
                }
              ],
              "height": 1800,
              "width": 3600
            },
            "sizes": {
              "large": {
                "h": 1024,
                "resize": "fit",
                "w": 2048
              },
              "medium": {
                "h": 600,
                "resize": "fit",
                "w": 1200
              },
              "small": {
                "h": 340,
                "resize": "fit",
                "w": 680
              },
              "thumb": {
                "h": 150,
                "resize": "crop",
                "w": 150
              }
            },
            "type": "photo",
            "url": "https://t.co/L1icjTabYS"
          }
        ],
        "symbols": [
          {
            "indices": [
              10,
              14
            ],
            "text": "TAO"
          }
        ],
        "timestamps": [],
        "urls": [],
        "user_mentions": []
      },
      "extended_entities": {
        "media": [
          {
            "display_url": "pic.x.com/L1icjTabYS",
            "expanded_url": "https://x.com/HOSS_ibc/status/1932946234920349827/photo/1",
            "ext_media_availability": {
              "status": "Available"
            },
            "features": {
              "large": {
                "faces": [
                  {
                    "h": 77,
                    "w": 77,
                    "x": 1877,
                    "y": 521
                  },
                  {
                    "h": 93,
                    "w": 93,
                    "x": 971,
                    "y": 571
                  }
                ]
              },
              "medium": {
                "faces": [
                  {
                    "h": 45,
                    "w": 45,
                    "x": 1100,
                    "y": 305
                  },
                  {
                    "h": 55,
                    "w": 55,
                    "x": 569,
                    "y": 335
                  }
                ]
              },
              "orig": {
                "faces": [
                  {
                    "h": 137,
                    "w": 137,
                    "x": 3301,
                    "y": 917
                  },
                  {
                    "h": 165,
                    "w": 165,
                    "x": 1708,
                    "y": 1005
                  }
                ]
              },
              "small": {
                "faces": [
                  {
                    "h": 25,
                    "w": 25,
                    "x": 623,
                    "y": 173
                  },
                  {
                    "h": 31,
                    "w": 31,
                    "x": 322,
                    "y": 189
                  }
                ]
              }
            },
            "id_str": "1932944082281574400",
            "indices": [
              270,
              293
            ],
            "media_key": "3_1932944082281574400",
            "media_url_https": "https://pbs.twimg.com/media/GtMyZtMWMAAPfq9.jpg",
            "original_info": {
              "focus_rects": [
                {
                  "h": 1800,
                  "w": 3214,
                  "x": 0,
                  "y": 0
                },
                {
                  "h": 1800,
                  "w": 1800,
                  "x": 0,
                  "y": 0
                },
                {
                  "h": 1800,
                  "w": 1579,
                  "x": 0,
                  "y": 0
                },
                {
                  "h": 1800,
                  "w": 900,
                  "x": 0,
                  "y": 0
                },
                {
                  "h": 1800,
                  "w": 3600,
                  "x": 0,
                  "y": 0
                }
              ],
              "height": 1800,
              "width": 3600
            },
            "sizes": {
              "large": {
                "h": 1024,
                "resize": "fit",
                "w": 2048
              },
              "medium": {
                "h": 600,
                "resize": "fit",
                "w": 1200
              },
              "small": {
                "h": 340,
                "resize": "fit",
                "w": 680
              },
              "thumb": {
                "h": 150,
                "resize": "crop",
                "w": 150
              }
            },
            "type": "photo",
            "url": "https://t.co/L1icjTabYS"
          }
        ]
      },
      "id": "1932946234920349827",
      "is_quote_tweet": false,
      "is_retweet": false,
      "lang": "en",
      "like_count": 31,
      "media": [
        {
          "media_url": "https://pbs.twimg.com/media/GtMyZtMWMAAPfq9.jpg",
          "type": "photo"
        }
      ],
      "quote_count": 3,
      "reply_count": 16,
      "retweet_count": 3,
      "text": "Bittensor $TAO seems oversold here.\n\nGrowth up but price is down\n\nPrice Valuation (Next 12 Months)\n\nFactors  \n\nTechnical: Trading above 200-day MA; support at $350-$380.  \n\nFundamental: Halving, subnet growth, institutional interest (e.g., Grayscale’s Bittensor Trust).  \n\nSentiment: Strong staking (72%) and developer activity.\n\nForecast (Jun 2025-Jun 2026)  \n\nConservative: $350-$600  \n\nBase: $600-$900  \n\nBullish: $900-$1,200",
      "url": "https://x.com/HOSS_ibc/status/1932946234920349827",
      "user": {
        "can_dm": true,
        "can_media_tag": false,
        "created_at": "Sun Jul 18 05:20:07 +0000 2021",
        "description": "Entrepreneur, Angel Investor & Product Advisor | 4+ years full-time in Crypto | 16+ years building businesses | Passionate about DeFi, Art  & impactful content",
        "entities": {
          "description": {
            "urls": []
          },
          "url": {
            "urls": [
              {
                "display_url": "metimmerse.io/hoss",
                "expanded_url": "https://metimmerse.io/hoss",
                "indices": [
                  0,
                  23
                ],
                "url": "https://t.co/kAQCAPyc7F"
              }
            ]
          }
        },
        "favourites_count": 163851,
        "followers_count": 63156,
        "id": "1416628772565143561",
        "is_blue_verified": true,
        "listed_count": 460,
        "location": "Tweets aren't financial advice",
        "media_count": 8421,
        "name": "Hoss",
        "pinned_tweet_ids": [
          "1932920070222889063"
        ],
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/1416628772565143561/1749700252",
        "profile_image_url": "https://pbs.twimg.com/profile_images/1915178001026723840/s0MX6RPL_normal.jpg",
        "statuses_count": 77157,
        "url": "https://x.com/HOSS_ibc",
        "username": "HOSS_ibc",
        "verified": false
      }
    }
  ],
  "text": "This is some additional text related to the search query.",
  "miner_link_scores": {
    "https://news.ycombinator.com/item?id=35114983": "MEDIUM",
    "https://news.ycombinator.com/item?id=42684057": "MEDIUM"
  },
  "completion": "Bittensor is a decentralized, open-source machine learning network that transforms AI models into tradable commodities."
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
