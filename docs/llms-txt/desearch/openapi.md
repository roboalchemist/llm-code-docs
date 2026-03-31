# Desearch API

Version: 1.0.0

The Desearch API is a powerful suite of AI-driven tools designed to integrate natural language processing, AI-powered search, image generation, and data extraction into your applications. Whether you’re building intelligent search engines, automating content creation, analyzing text data, or generating AI-based media, Desearch provides a robust and scalable solution.

## Servers

- https://api.desearch.ai

## POST /desearch/ai/search

**AI Contextual Search**

The Desearch API allows you to perform AI-powered web searches, gathering relevant information from multiple sources, including web pages, research papers, and social media discussions.

### Request Body

Content-Type: `application/json`

Schema: ScraperStreamingSynapseRequest

### Responses

- **200**: A JSON object mapping tool names to their search results.
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## POST /desearch/ai/search/links/web

**AI Web Search**

This API allows users to search for links related to a given query (prompt) using multiple tools, excluding X (Twitter) Search. The API returns a list of relevant sources from selected platforms such as web pages, YouTube, Wikipedia, and ArXiv.

### Request Body

Content-Type: `application/json`

Schema: LinksSearchRequestWeb

### Responses

- **200**: A JSON object mapping tool names to their search results.
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## POST /desearch/ai/search/links/twitter

**AI Х Posts Search**

The Х Posts Search API allows users to search for relevant links based on Х search queries with leveraging AI-powered models. This API analyze links from Х posts that match the given prompt. This API is useful for tracking trends, gathering insights, and retrieving real-time information from Х.

### Request Body

Content-Type: `application/json`

Schema: LinksSearchRequestTwitter

### Responses

- **200**: A JSON object mapping Х Search to its search results.
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## GET /twitter

**X Search API**

The X Search API enables users to retrieve relevant links and tweets based on specified search queries without utilizing AI-driven models. It analyzes links from X posts that align with the provided search criteria.

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| query | query | string | True | Advanced search query |
| sort | query |  | False | Sort by Top or Latest |
| user | query |  | False | User to search for |
| start_date | query |  | False | Start date in UTC (YYYY-MM-DD format) |
| end_date | query |  | False | End date in UTC (YYYY-MM-DD format) |
| lang | query |  | False | Language code (e.g., en, es, fr) |
| verified | query |  | False | Filter for verified users |
| blue_verified | query |  | False | Filter for blue checkmark verified users |
| is_quote | query |  | False | Include only tweets with quotes |
| is_video | query |  | False | Include only tweets with videos |
| is_image | query |  | False | Include only tweets with images |
| min_retweets | query |  | False | Minimum number of retweets |
| min_replies | query |  | False | Minimum number of replies |
| min_likes | query |  | False | Minimum number of likes |
| count | query |  | False | Number of tweets to retrieve |

### Responses

- **200**: A JSON object mapping X Search to its search results.
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## GET /twitter/urls

**Fetch Posts by URLs**

Retrieve detailed information for multiple posts by providing their respective URLs. This endpoint extracts metadata, content, and relevant engagement metrics associated with each specified URL.

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| urls | query | array | True | List of urls that is to be retrieved. |

### Responses

- **200**: A JSON object mapping tweet URLs to their details.
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## GET /twitter/post

**Retrieve Post by ID**

Retrieve comprehensive details of a post by specifying its unique ID. This endpoint provides metadata, content, and engagement metrics associated with the specified post.

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| id | query | string | True |  |

### Responses

- **200**: A JSON object representing the post details.
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## GET /twitter/post/user

**Search X Posts by User**

The X posts search by user API allows users to search for relevant links or tweets based on X search queries without leveraging AI-powered models. This API analyze links from X posts that match the given prompt.

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| user | query | string | True | User to search for |
| query | query | string | False | Advanced search query |
| count | query | integer | False | Number of tweets to retrieve |

### Responses

- **200**: A JSON object mapping Twitter Search to its search results.
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## GET /twitter/post/retweeters

**Get Retweeters of a Post**

Retrieve the list of users who retweeted a specific post by its ID. Supports pagination via cursor.

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| id | query | string | True | The ID of the post to get retweeters for |
| cursor | query |  | False | Cursor for pagination |

### Responses

- **200**: A JSON object containing the list of users who retweeted the post.
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## GET /twitter/user/posts

**Get X Posts by Username**

Retrieve user's timeline posts by specifying their username. This endpoint fetches the latest tweets posted by the user associated with the provided username.

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| username | query | string | True | Username to fetch posts for |
| cursor | query |  | False | Cursor for pagination |

### Responses

- **200**: A JSON object mapping X Posts
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## GET /twitter/replies

**Fetch User's Tweets and Replies**

The tweets and replies by user API allows users to search for relevant links or tweets based on X search queries without leveraging AI-powered models. This API analyze links from X posts that match the given prompt.

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| user | query | string | True | The username of the user to search for. |
| count | query | integer | False | The number of tweets to fetch. |
| query | query | string | False | Advanced search query |

### Responses

- **200**: A JSON object mapping Twitter Search to its search results.
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## GET /twitter/replies/post

**Retrieve Replies for a Post**

The Tweets and Replies by User API enables users to retrieve relevant tweets and replies based on specified search queries without relying on AI-powered models. It analyzes and extracts links from X posts that align with the provided search criteria.

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| post_id | query | string | True | The ID of the post to search for. |
| count | query | integer | False | The number of tweets to fetch. |
| query | query | string | False | Advanced search query |

### Responses

- **200**: A JSON object mapping Twitter Search to its search results.
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## GET /twitter/trends

**Get X Trends**

Retrieve trending topics on X for a given location using its WOEID (Where On Earth ID).

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| woeid | query | integer | True | The WOEID of the location (e.g. 23424977 for United States). WOEID List: https://gist.github.com/tedyblood/5bb5a9f78314cc1f478b3dd7cde790b9 |
| count | query |  | False | The number of trends to return. Minimum is 30, maximum is 100. |

### Responses

- **200**: A JSON object containing the list of trending topics.
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## GET /web

**SERP Web Search API**

This API allows users to search for any information over the web. This replicates a typical search engine experience, where users can search for any information they need.

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| query | query | string | True | The search query string, e.g., 'latest news on AI'. |
| start | query | integer | False | How many results to skip. It's used for pagination. (e.g., 0 (default) is the first page of results, 10 is the 2nd page of results, 20 is the 3rd page of results, etc.). |

### Responses

- **201**: A JSON object mapping Web Search to its search results.
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## GET /web/crawl

**Crawl API**

The Desearch API allows you to crawl web content

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| url | query | string | True | Url to crawl |
| format | query | string | False | Format of the content to be returned. Options are 'html' or 'text'. Default is 'html'. |

### Responses

- **200**: Content of the web link
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error
- **301**: Moved Permanently
- **304**: Not Modified

## POST /numinous/forecasts

**Create Forecast Job**

Submit a forecasting question to the Numinous AI superforecasting system powered by Bittensor Subnet 6. Returns a prediction job ID to poll for results. Supports two modes: **structured** (title + description + cutoff) for precise results, or **query** (natural language question) for quick exploration.

### Request Body

Content-Type: `application/json`

Schema: NuminousForecastRequest

### Responses

- **202**: A prediction job ID and initial PENDING status.
- **401**: Unauthorized
- **422**: Validation Error
- **429**: Too Many Requests
- **500**: Internal Server Error

## GET /numinous/forecasts/{prediction_id}

**Get Forecast Result**

Poll the status of a prediction job created via POST /numinous/forecasts. Poll every 5 seconds — jobs typically complete within 30–120 seconds. The `prediction_id` UUID acts as an access token; no API key is required for polling.

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| prediction_id | path | string | True |  |

### Responses

- **200**: Current job status and result when completed.
- **404**: Prediction job not found
- **500**: Internal Server Error
- **422**: Validation Error

---

# Schemas

## ChatHistoryItem

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| prompt | string | True |  |
| completion | string | False |  Default:  |

## DateFilterEnum

Enum values: PAST_24_HOURS, PAST_2_DAYS, PAST_WEEK, PAST_2_WEEKS, PAST_MONTH, PAST_2_MONTHS, PAST_YEAR, PAST_2_YEARS

## HTTPValidationError

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| detail | array[ValidationError] | False |  |

## InternalServerErrorResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| detail | object | True |  |

## LinksSearchRequestTwitter

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| prompt | string | True | Search query prompt |
| count |  | False | The number of results to return per source. Min 10. Max 200. Default: 10 |

## LinksSearchRequestWeb

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| prompt | string | True | Search query prompt |
| tools | array[] | True | List of tools to search with |
| count |  | False | The number of results to return per source. Min 10. Max 200. Default: 10 |

## MediaSize

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| w | integer | True |  |
| h | integer | True |  |
| resize |  | False |  |

## MovedPermanentlyResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| detail | object | True |  |

## NuminousForecastRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| title |  | False |  |
| description |  | False |  |
| cutoff |  | False |  |
| topics |  | False |  |
| query |  | False |  |
| agent_version_id |  | False |  |

## NuminousForecastResult

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| prediction | number | True | Probability estimate in [0.0, 1.0]. E.g. 0.72 means 72% probability of YES. |
| forecaster_name | string | True | Identifier of the forecaster that produced the result. |
| forecasted_at | string | True | ISO 8601 datetime when the forecast was generated. |
| metadata |  | False | Forecaster metadata including miner info and optional reasoning. |
| parsed_fields |  | False | Fields extracted from the natural language query. Present only in query mode. |

## NuminousForecasterMetadata

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| miner_uid |  | False | Miner UID on the Bittensor subnet. |
| miner_hotkey |  | False | Miner hotkey (SS58 address). |
| pool |  | False | Scoring pool used (e.g. GLOBAL_BRIER). |
| version_id |  | False | Agent version UUID. |
| agent_name |  | False | Agent name. |
| version_number |  | False | Agent version number. |
| raw_prediction |  | False | Raw probability from the miner. |
| event_title |  | False | Event title used for the forecast. |
| event_cutoff |  | False | ISO 8601 cutoff datetime for the event. |
| reasoning |  | False | Optional reasoning from the forecaster. |

## NuminousJobCreatedResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| prediction_id | string | True | Unique identifier for the prediction job. Use this to poll for results. |
| status | NuminousJobStatus | True | Initial job status. Always PENDING on creation. |

## NuminousJobStatus

Enum values: PENDING, RUNNING, COMPLETED, FAILED

## NuminousJobStatusResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| prediction_id | string | True | Job identifier. |
| status | NuminousJobStatus | True | Current job status: PENDING, RUNNING, COMPLETED, or FAILED. |
| created_at |  | False | ISO 8601 datetime when the job was created. |
| result |  | False | Forecast result. Present when status is COMPLETED. |
| error |  | False | Error description. Present when status is FAILED. |

## NuminousParsedFields

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| title |  | False | Extracted event title. |
| description |  | False | Extracted resolution criteria. |
| cutoff |  | False | Extracted ISO 8601 cutoff datetime. |
| topics |  | False | Extracted topic categories. |

## Rect

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| x | integer | True |  |
| y | integer | True |  |
| w | integer | True |  |
| h | integer | True |  |

## ResponseData

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| hacker_news_search |  | False | Search results from Hacker News, listing articles and discussions relevant to the query. |
| reddit_search |  | False | Search results from Reddit, providing discussions and posts related to the search query. |
| search |  | False | General search results related to the query. |
| youtube_search |  | False | Search results from YouTube, including relevant videos matching the search criteria. |
| tweets |  | False | Tweets related to the search query. |
| text |  | False | Additional text related to the search query. |
| miner_link_scores |  | False | A list of miner link scores, typically used in AI-generated content results. |
| completion |  | False | Generated completion text or response, typically used in AI-generated content results. |

## ResultTypeEnum

Enum values: ONLY_LINKS, LINKS_WITH_FINAL_SUMMARY

## ScraperStreamingSynapseRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| prompt | string | True | Search query prompt |
| tools | array[] | True | A list of tools to be used for the search |
| start_date |  | False | The start date for the search query. Format: YYYY-MM-DDTHH:MM:SSZ (UTC) |
| end_date |  | False | The end date for the search query. Format: YYYY-MM-DDTHH:MM:SSZ (UTC) |
| date_filter |  | False | Predefined date filters for the search results, or you can use specific start and end dates Default: PAST_24_HOURS |
| streaming | boolean | False | Whether to stream results Default: True |
| result_type |  | False | The result type to be used for the search Default: LINKS_WITH_FINAL_SUMMARY |
| system_message |  | False | The system message to be used for the search Default:  |
| scoring_system_message |  | False | System message for scoring the response |
| count |  | False | The number of results to return per source. Min 10. Max 200. Default: 10 |

## TooManyRequestsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| detail | object | True |  |

## ToolEnum

Enum values: web, hackernews, reddit, wikipedia, youtube, twitter, arxiv

## TwitterScraperEntities

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| hashtags |  | False |  |
| media |  | False |  |
| symbols |  | False |  |
| timestamps |  | False |  |
| urls |  | False |  |
| user_mentions |  | False |  |

## TwitterScraperEntitiesMedia

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| display_url |  | False |  |
| expanded_url |  | False |  |
| id_str |  | False |  |
| indices |  | False |  |
| media_key |  | False |  |
| media_url_https |  | False |  |
| type |  | False |  |
| url |  | False |  |
| additional_media_info |  | False |  |
| ext_media_availability |  | False |  |
| features |  | False |  |
| sizes |  | False |  |
| original_info |  | False |  |
| allow_download_status |  | False |  |
| video_info |  | False |  |
| media_results |  | False |  |

## TwitterScraperEntitiesMediaAdditionalInfo

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| monetizable |  | False |  |
| source_user |  | False |  |

## TwitterScraperEntitiesMediaAllowDownloadStatus

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| allow_download |  | False |  |

## TwitterScraperEntitiesMediaExtAvailability

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| status |  | False |  |

## TwitterScraperEntitiesMediaFeature

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| faces |  | False |  |

## TwitterScraperEntitiesMediaFeatures

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| large |  | False |  |
| medium |  | False |  |
| small |  | False |  |
| orig |  | False |  |

## TwitterScraperEntitiesMediaOriginalInfo

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| height | integer | True |  |
| width | integer | True |  |
| focus_rects |  | False |  |

## TwitterScraperEntitiesMediaResult

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| media_key | string | True |  |

## TwitterScraperEntitiesMediaResults

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| result |  | False |  |

## TwitterScraperEntitiesMediaSizes

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| large |  | False |  |
| medium |  | False |  |
| small |  | False |  |
| thumb |  | False |  |

## TwitterScraperEntitiesMediaVideoInfo

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| duration_millis |  | False |  |
| aspect_ratio |  | False |  |
| variants |  | False |  |

## TwitterScraperEntitiesMediaVideoInfoVariant

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| content_type | string | True |  |
| url | string | True |  |
| bitrate |  | False |  |

## TwitterScraperEntitiesSymbol

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| indices | array[integer] | True |  |
| text | string | True |  |

## TwitterScraperEntitiesUserMention

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| id_str | string | True |  |
| name | string | True |  |
| screen_name | string | True |  |
| indices | array[integer] | True |  |

## TwitterScraperEntityUrl

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| display_url | string | True |  |
| expanded_url |  | False |  |
| url | string | True |  |
| indices | array[integer] | True |  |

## TwitterScraperExtendedEntities

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| media |  | False |  |

## TwitterScraperMedia

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| media_url | string | False |  Default:  |
| type | string | False |  Default:  |

## TwitterScraperTweet

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| user |  | False |  |
| id | string | True |  |
| text | string | True |  |
| reply_count | integer | True |  |
| view_count |  | False |  |
| retweet_count | integer | True |  |
| like_count | integer | True |  |
| quote_count | integer | True |  |
| bookmark_count | integer | True |  |
| url |  | False |  |
| created_at | string | True |  |
| media |  | False |  |
| is_quote_tweet |  | False |  |
| is_retweet |  | False |  |
| lang |  | False |  |
| conversation_id |  | False |  |
| in_reply_to_screen_name |  | False |  |
| in_reply_to_status_id |  | False |  |
| in_reply_to_user_id |  | False |  |
| quoted_status_id |  | False |  |
| quote |  | False |  |
| replies |  | False |  |
| display_text_range |  | False |  |
| entities |  | False |  |
| extended_entities |  | False |  |
| retweet |  | False |  |

## TwitterScraperUser

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| id | string | True |  |
| url |  | False |  |
| name |  | False |  |
| username | string | True |  |
| created_at |  | False |  |
| description |  | False |  |
| favourites_count |  | False |  |
| followers_count |  | False |  |
| followings_count |  | False |  |
| listed_count |  | False |  |
| media_count |  | False |  |
| profile_image_url |  | False |  |
| profile_banner_url |  | False |  |
| statuses_count |  | False |  |
| verified |  | False |  |
| is_blue_verified |  | False |  |
| entities |  | False |  |
| can_dm |  | False |  |
| can_media_tag |  | False |  |
| location |  | False |  |
| pinned_tweet_ids |  | False |  |
| professional |  | False |  |

## TwitterScraperUserEntities

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| description |  | False |  |
| url |  | False |  |

## TwitterScraperUserEntitiesDescription

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| urls |  | False |  |

## TwitterScraperUserProfessional

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| professional_type | string | True |  |
| category | array[TwitterScraperUserProfessionalCategory] | False |  |

## TwitterScraperUserProfessionalCategory

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| id | integer | True |  |
| name | string | True |  |

## UnauthorizedResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| detail | object | True |  |

## ValidationError

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| loc | array[] | True |  |
| msg | string | True |  |
| type | string | True |  |

## WebSearchResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| youtube_search_results |  | True | Youtube search results |
| hacker_news_search_results |  | True | Hacker News search results |
| reddit_search_results |  | True | Reddit search results |
| arxiv_search_results |  | True | Arxiv search results |
| wikipedia_search_results |  | True | Wikipedia search results |
| search_results |  | True | Search results |

## WebSearchResultItem

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| title | string | True | EXCLUSIVE Major coffee buyers face losses as Colombia ... |
| snippet | string | True | Coffee farmers in Colombia, the world's No. 2 arabica producer, have failed to deliver up to 1 million bags of beans this year or nearly 10% ... |
| link | string | True | https://www.reuters.com/world/americas/exclusive-major-coffee-buyers-face-losses-colombia-farmers-fail-deliver-2021-10-11/ |

## WebSearchResultsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| data | array[WebSearchResultItem] | True |  |

## WebToolEnum

Enum values: web, hackernews, reddit, wikipedia, youtube, arxiv

## XLinksSearchResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| miner_tweets | array[TwitterScraperTweet] | True | Miner tweets |

## XRetweetersResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| users | array[TwitterScraperUser] | True |  |
| next_cursor |  | False | Cursor for pagination |

## XTrendItem

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| name | string | True | The name of the trending topic |
| query |  | False | The search query associated with the trend |
| rank |  | False | The rank of the trend |

## XTrendsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| trends | array[XTrendItem] | True | List of trending topics |
| woeid |  | False | The location for which trends were retrieved |

## XTrendsWoeid

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| name | string | True | The name of the location |
| id | integer | True | The WOEID (Where On Earth ID) of the location |

## XUserPostsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| user | TwitterScraperUser | True |  |
| tweets | array[TwitterScraperTweet] | True |  |
| next_cursor |  | False | Cursor for pagination |
