# Source: https://docs.perplexity.ai/guides/returning-videos

## 
[​](https://docs.perplexity.ai/guides/returning-videos#overview)
Overview
Sonar models can return videos as part of their responses to provide rich multimedia content that enhances the information delivered. You can control video returns using the `media_response` parameter with `overrides` to specify when videos should be included in responses.
Use the `media_response.overrides.return_videos` parameter to control when videos are returned in API responses.
Video returns may increase response size and processing time. Use this feature selectively for queries where video content adds significant value.
## 
[​](https://docs.perplexity.ai/guides/returning-videos#basic-usage)
Basic Usage
To enable video returns, include the `media_response` parameter with `overrides.return_videos` set to `true` in your request.
### 
[​](https://docs.perplexity.ai/guides/returning-videos#simple-video-request)
Simple Video Request
cURL
Python
TypeScript
Copy
Ask AI
```
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {
        "role": "user",
        "content": "2024 Olympics highlights"
      }
    ]
  }' | jq

```

Sample Response
Copy
Ask AI
```
{
  "id": "58dee6e4-d2de-4d7e-910f-4048caa6903d",
  "model": "sonar-pro",
  "created": 1758844959,
  "usage": {
    "prompt_tokens": 6,
    "completion_tokens": 542,
    "total_tokens": 548,
    "search_context_size": "low",
    "cost": {
      "input_tokens_cost": 0.0,
      "output_tokens_cost": 0.008,
      "request_cost": 0.006,
      "total_cost": 0.014
    }
  },
  "citations": [
    "https://en.wikipedia.org/wiki/2024_Summer_Olympics",
    "https://www.teamusa.com/news/2024/august/13/top-moments-from-the-paris-2024-olympic-games",
    "https://www.nbcolympics.com/news/olympic-track-and-field-paris-2024-biggest-stories-replays-medal-results-top-athletes-new",
    "https://www.youtube.com/watch?v=WajxULWXIFE",
    "https://www.nbcolympics.com/news/olympic-gymnastics-paris-2024-biggest-stories-replays-medal-results-top-athletes-new-records",
    "https://www.youtube.com/watch?v=vy6FivZHRjQ",
    "https://www.espn.com/olympics/story/_/id/40813327/2024-paris-summer-olympics-live-updates-highlights-results-sunday-closing-ceremony",
    "https://www.youtube.com/watch?v=q4Mujt1wer4",
    "https://www.youtube.com/olympics",
    "https://www.youtube.com/watch?v=OFCVkSQYTjA",
    "https://www.youtube.com/watch?v=7Xnr805bm4E",
    "https://www.nbcolympics.com/videos"
  ],
  "search_results": [
    {
      "title": "2024 Summer Olympics - Wikipedia",
      "url": "https://en.wikipedia.org/wiki/2024_Summer_Olympics",
      "date": "2006-03-05",
      "last_updated": "2025-09-24",
      "snippet": "Paris 2024 featured the debut of breaking as an Olympic sport, and was the final Olympic Games held during the IOC presidency of Thomas Bach. The 2024 Games ..."
    },
    {
      "title": "Top Moments From the Paris 2024 Olympic Games | Team USA",
      "url": "https://www.teamusa.com/news/2024/august/13/top-moments-from-the-paris-2024-olympic-games",
      "date": "2024-08-13",
      "last_updated": "2025-09-25",
      "snippet": "Scottie Scheffler wins his first Olympic Gold Medal | Golf · Victor Montalvo Takes Bronze in Breaking | Breaking · Brooke Raboutou Secures Her ..."
    },
    {
      "title": "Olympic track and field at Paris 2024: Biggest stories, replays, medal ...",
      "url": "https://www.nbcolympics.com/news/olympic-track-and-field-paris-2024-biggest-stories-replays-medal-results-top-athletes-new",
      "date": "2024-08-11",
      "last_updated": "2024-08-11",
      "snippet": "In the Paris Olympic men's 100m final, Lyles edged past Jamaican Kishane Thompson to win his first Olympic gold medal in a lifetime-best 9.784 ..."
    },
    {
      "title": "When Every Millisecond Counts at the Olympics | Top Moments",
      "url": "https://www.youtube.com/watch?v=WajxULWXIFE",
      "date": "2025-01-31",
      "last_updated": "2025-07-29",
      "snippet": "Re-live ALL the incredible #Paris2024 action: ➡️ https://oly.ch/P24Replays The most thrilling finishes of the Olympic Games in Paris 2024 ..."
    },
    {
      "title": "Olympic gymnastics at Paris 2024: Biggest stories, replays, medal ...",
      "url": "https://www.nbcolympics.com/news/olympic-gymnastics-paris-2024-biggest-stories-replays-medal-results-top-athletes-new-records",
      "date": "2024-08-11",
      "last_updated": "2024-08-11",
      "snippet": "Here's a look back at all the action, from highlights to medal results and everything in between. FULL EVENT REPLAYS:ARTISTIC GYMNASTICS"
    },
    {
      "title": "Best of Olympic Games Paris 2024 - YouTube",
      "url": "https://www.youtube.com/watch?v=vy6FivZHRjQ",
      "date": "2024-10-21",
      "last_updated": "2025-07-27",
      "snippet": "the Paris 2024 Olympics! From jaw-dropping athletic feats to ... highlights, including iconic victories, emotional celebrations, and ..."
    },
    {
      "title": "2024 Olympics: Highlights from Sunday in Paris - ESPN",
      "url": "https://www.espn.com/olympics/story/_/id/40813327/2024-paris-summer-olympics-live-updates-highlights-results-sunday-closing-ceremony",
      "date": "2024-08-11",
      "last_updated": "2024-08-11",
      "snippet": "The US Olympic run concluded with Team USA becoming the first team in any sport to win eight consecutive Olympic gold medals with a win over France."
    },
    {
      "title": "Moments that Left Us SPEECHLESS at Paris 2024! ❤️   - YouTube",
      "url": "https://www.youtube.com/watch?v=q4Mujt1wer4",
      "date": "2025-01-13",
      "last_updated": "2025-08-29",
      "snippet": "I'll always love the moment between Tara Davis-Woodhall and her husband Hunter Woodhall, who'd later snag his first gold medal in the Paralympics later on."
    },
    {
      "title": "Olympics - YouTube",
      "url": "https://www.youtube.com/olympics",
      "date": "2025-03-24",
      "last_updated": "2025-03-26",
      "snippet": "Witness the power, dedication, and skill of Olympic athletes as they compete for their chance to shine on the world stage."
    },
    {
      "title": "‍♂️ Best Athletics Moments at #Paris2024 ‍     - YouTube",
      "url": "https://www.youtube.com/watch?v=OFCVkSQYTjA",
      "date": "2025-03-30",
      "last_updated": "2025-07-29",
      "snippet": "Receive the best athletics moments at the olympic games in Paris 2024 ♂️. #Paris2024 ..."
    },
    {
      "title": "Men's 100m Final | Paris Champions - YouTube",
      "url": "https://www.youtube.com/watch?v=7Xnr805bm4E",
      "date": "2024-08-11",
      "last_updated": "2025-07-28",
      "snippet": "Re-live ALL the incredible #Paris2024 action: https://oly.ch/P24Replays Watch Noah Lyles of Team USA celebrate his gold medal victory ..."
    },
    {
      "title": "All Highlights | NBC Olympics",
      "url": "https://www.nbcolympics.com/videos",
      "date": "2025-09-24",
      "last_updated": "2025-09-25",
      "snippet": "All Highlights · Melissa Jefferson-Wooden claps her hands in joy after winning the world women's 200m final · Three runners prepare to cross the finish line in ..."
    }
  ],
  "videos": [
    {
      "url": "https://www.youtube.com/watch?v=lmPuoxNSRr4",
      "duration": null,
      "thumbnail_width": 480,
      "thumbnail_height": 360,
      "thumbnail_url": "https://www.youtube.com/watch?v=lmPuoxNSRr4"
    },
    {
      "url": "https://www.youtube.com/watch?v=cptEWh0yT4E",
      "duration": null,
      "thumbnail_width": 480,
      "thumbnail_height": 360,
      "thumbnail_url": "https://www.youtube.com/watch?v=cptEWh0yT4E"
    },
    {
      "url": "https://www.youtube.com/watch?v=6bhS_AUKjtc",
      "duration": null,
      "thumbnail_width": 480,
      "thumbnail_height": 360,
      "thumbnail_url": "https://www.youtube.com/watch?v=6bhS_AUKjtc"
    },
    {
      "url": "https://www.youtube.com/watch?v=vy6FivZHRjQ",
      "duration": null,
      "thumbnail_width": 480,
      "thumbnail_height": 360,
      "thumbnail_url": "https://www.youtube.com/watch?v=vy6FivZHRjQ"
    },
    {
      "url": "https://www.youtube.com/watch?v=WajxULWXIFE",
      "duration": null,
      "thumbnail_width": 480,
      "thumbnail_height": 360,
      "thumbnail_url": "https://www.youtube.com/watch?v=WajxULWXIFE"
    }
  ],
  "object": "chat.completion",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "The 2024 Summer Olympics in Paris were marked by major milestones, standout athletic performances, record medal hauls, and historic firsts[1][2][3][6].\n\n**Key highlights:**\n\n- **Medal Table Leaders:** The United States and China finished tied with 40 gold medals each, but the U.S. claimed the top spot overall with 126 total medals; China followed with 91 total[1][2]. It was the first time the two Olympic powers tied in golds. Japan (20 golds), Australia (18 golds), and host nation France (16 golds) rounded out the top five[1].\n\n- **Breakdancing Debut:** Paris 2024 introduced **breaking** (breakdancing) as an Olympic sport for the first time[1].\n\n- **Athletics Dominance:** The U.S. displayed overwhelming strength in **track and field**, securing 34 medals—their best since 1984—and sweeping all four hurdle events for the first time[3]. Noah Lyles won his first Olympic gold in the men's 100m with a dramatic, lifetime-best 9.784 seconds[3][4]. Sydney McLaughlin-Levrone broke her own women's 400m hurdles world record yet again[3].\n\n- **Gymnastics Spectacle:** The games featured high drama and new records in **artistic gymnastics**, with full event replays and standout moments available for fans[5].\n\n- **Historic Firsts:** Several nations, including **Dominica, Saint Lucia, Cape Verde, and Albania**, celebrated their first-ever Olympic medals—some of them gold[1]. The **Refugee Olympic Team** won its first medal, a bronze in boxing by Cindy Ngamba[1].\n\n- **Iconic Performances:** Scottie Scheffler secured his first Olympic golf gold for Team USA; Victor Montalvo earned bronze in breaking; and Brooke Raboutou delivered in sport climbing[2].\n\n- **Intensity and Sportsmanship:** Multiple events featured finishes decided by milliseconds and millimeters, capturing the Olympic spirit, as showcased in event highlight reels and replays[4][6].\n\n- **Record-Breaking Tickets:** Paris 2024 broke Olympic records with over 9.5 million tickets sold (12.1 million including Paralympics), becoming a celebrated success despite some controversies around politics and logistics[1].\n\n**Notable Podium Sweep:** France swept all three medals in the men's BMX race, a moment of national pride[1].\n\nThe Paris Olympics were hailed as both a sporting and organizational triumph, celebrated by both locals and worldwide observers[1]."
      },
      "delta": {
        "role": "assistant",
        "content": ""
      }
    }
  ]
}

```

## 
[​](https://docs.perplexity.ai/guides/returning-videos#use-case-examples)
Use Case Examples
### 
[​](https://docs.perplexity.ai/guides/returning-videos#sports-and-events)
Sports and Events
Request videos for major sporting events or news:
cURL
Python
TypeScript
Copy
Ask AI
```
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {
        "role": "user",
        "content": "World Cup 2024 final match highlights"
      }
    ]
  }' | jq

```

### 
[​](https://docs.perplexity.ai/guides/returning-videos#educational-content)
Educational Content
Get instructional videos for learning topics:
cURL
Python
TypeScript
Copy
Ask AI
```
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {
        "role": "user",
        "content": "How to perform CPR tutorial videos"
      }
    ]
  }' | jq

```

### 
[​](https://docs.perplexity.ai/guides/returning-videos#technology-demonstrations)
Technology Demonstrations
Request videos showing product demos or tutorials:
cURL
Python
TypeScript
Copy
Ask AI
```
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {
        "role": "user",
        "content": "iPhone 16 pro camera features demonstration"
      }
    ]
  }' | jq

```

## 
[​](https://docs.perplexity.ai/guides/returning-videos#combined-media-responses)
Combined Media Responses
You can combine video returns with other media response options:
### 
[​](https://docs.perplexity.ai/guides/returning-videos#videos-with-images)
Videos with Images
Copy
Ask AI
```
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "media_response": {
      "overrides": {
        "return_videos": true,
        "return_images": true
      }
    },
    "messages": [
      {
        "role": "user",
        "content": "Mars rover discoveries 2024"
      }
    ]
  }' | jq

```

### 
[​](https://docs.perplexity.ai/guides/returning-videos#videos-with-search-filters)
Videos with Search Filters
Copy
Ask AI
```
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "search_recency_filter": "week",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {
        "role": "user",
        "content": "Latest SpaceX launch footage"
      }
    ]
  }' | jq

```

## 
[​](https://docs.perplexity.ai/guides/returning-videos#advanced-usage)
Advanced Usage
### 
[​](https://docs.perplexity.ai/guides/returning-videos#streaming-with-videos)
Streaming with Videos
Enable streaming responses while including video content:
Copy
Ask AI
```
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "stream": true,
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {
        "role": "user",
        "content": "Breaking news today with video coverage"
      }
    ]
  }'

```

### 
[​](https://docs.perplexity.ai/guides/returning-videos#multi-turn-conversation-with-videos)
Multi-turn Conversation with Videos
Continue a conversation while maintaining video context:
Copy
Ask AI
```
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {
        "role": "user",
        "content": "Show me cooking videos for pasta recipes"
      },
      {
        "role": "assistant",
        "content": "Here are some great pasta cooking videos..."
      },
      {
        "role": "user",
        "content": "Now show me videos for making homemade sauce"
      }
    ]
  }' | jq

```

## 
[​](https://docs.perplexity.ai/guides/returning-videos#best-practices)
Best Practices
Query Optimization
  * **Be specific** : Use descriptive queries that clearly indicate when video content would be valuable
  * **Include context** : Mention specific events, products, or topics that commonly have video coverage
  * **Use recency filters** : Combine with search filters to get the most current video content
  * **Consider query intent** : Videos work best for demonstrations, tutorials, events, and visual explanations


Performance Considerations
  * **Monitor response times** : Video-enabled requests may take longer to process
  * **Handle larger payloads** : Responses containing videos will be larger than text-only responses
  * **Implement timeouts** : Set appropriate timeout values for video-enabled requests
  * **Cache strategically** : Consider caching video responses for frequently requested content


Content Quality
  * **Verify video relevance** : Not all queries will return relevant video content
  * **Handle empty results** : Implement fallback logic when no videos are available
  * **Check video accessibility** : Ensure returned video content is accessible and appropriate
  * **Validate video links** : Test that returned video URLs are functional before displaying


## 
[​](https://docs.perplexity.ai/guides/returning-videos#response-format)
Response Format
When videos are returned, they appear in the response content along with text. The videos will be included as part of the response structure, with video URLs and metadata available for display or processing.
## 
[​](https://docs.perplexity.ai/guides/returning-videos#common-use-cases)
Common Use Cases
### 
[​](https://docs.perplexity.ai/guides/returning-videos#news-and-current-events)
News and Current Events
Copy
Ask AI
```
# Get breaking news with video coverage
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "search_recency_filter": "day",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {"role": "user", "content": "Latest political developments today"}
    ]
  }'

```

### 
[​](https://docs.perplexity.ai/guides/returning-videos#product-reviews-and-demonstrations)
Product Reviews and Demonstrations
Copy
Ask AI
```
# Get product demo videos
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {"role": "user", "content": "MacBook Pro M4 unboxing and first impressions"}
    ]
  }'

```

### 
[​](https://docs.perplexity.ai/guides/returning-videos#educational-and-how-to-content)
Educational and How-to Content
Copy
Ask AI
```
# Get tutorial videos
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar-pro",
    "media_response": {
      "overrides": {
        "return_videos": true
      }
    },
    "messages": [
      {"role": "user", "content": "How to change a car tire step by step"}
    ]
  }'

```

## 
[​](https://docs.perplexity.ai/guides/returning-videos#troubleshooting)
Troubleshooting
No Videos Returned
If your request doesn’t return videos:
  * Verify the `media_response.overrides.return_videos` parameter is set to `true`
  * Check that your query is likely to have video content available
  * Ensure you’re using a model that supports video returns (sonar-pro recommended)
  * Try different query phrasings that explicitly mention video content


Request Timeouts
For timeout issues:
  * Increase your request timeout settings
  * Use streaming responses for better user experience
  * Consider breaking complex queries into smaller parts
  * Implement retry logic for failed requests


Large Response Handling
When dealing with video-heavy responses:
  * Implement proper JSON parsing for large payloads
  * Consider pagination for multiple video results
  * Use appropriate data structures to handle media content
  * Implement progressive loading for video content


## 
[​](https://docs.perplexity.ai/guides/returning-videos#limitations)
Limitations
**Current Limitations:**
  * Video returns may not be available for all query types
  * Response times will be longer when videos are included
  * Video content availability depends on external sources
  * Some video content may be region-restricted
  * No direct video format or quality control options currently available


## 
[​](https://docs.perplexity.ai/guides/returning-videos#environment-variables)
Environment Variables
For security, use environment variables for your API key:
  * macOS/Linux
  * Windows


Copy
Ask AI
```
export PERPLEXITY_API_KEY="your_api_key_here"

```

Then reference it in your requests:
Copy
Ask AI
```
curl https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "sonar-pro", ...}'

```

Start with simple queries to test video returns, then gradually build more complex requests as you understand the response patterns and performance characteristics.
