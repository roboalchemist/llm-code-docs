# Source: https://docs.nimbleway.io/quick-start-tutorials/tutorial-library/reddit-as-a-guerilla-marketing-strategy.md

# Reddit as a Guerilla Marketing Strategy

## Explore new markets using SERP API

Search is the biggest software business in the world. Online businesses rely on Search Engines Results Page for discoverability and community building, fighting over the prime real estate which is above-the-fold (or at least on the first page) of a given search result.

In the past year, [Google has been promoting Reddit pages](https://www.searchenginejournal.com/google-announces-deal-to-show-more-reddit-content/509132/) [more aggressively](https://searchengineland.com/reddit-dominates-google-search-discussions-forums-437501) in their search results which created an enormous opportunity for businesses and marketers in reaching potential customers by tapping into popular, high visibility threads.

### Reddit as a guerrilla marketing strategy

Reddit with its endless lists of sub-reddits has always been a home to passionate communities and can be a powerful tool for niche marketing. In this post we’ll try to build a simple marketing play, harnessing Reddit’s existing SEO prowess in Google search results.

Here’s how this strategy works:

1. Search Google for your business’ relevant keywords
2. Find the top Reddit posts in Google search results
3. Interact with those posts (i.e., comment with your product/service, find relevant leads, etc.)

In short, leveraging Reddit’s existing SEO for relevant posts to boost your product without the legwork of trying to reach the top results page with your original content.

Nimble’s SERP API can help with automating this process and quickly churn out top Reddit posts with the highest impact.

Read ahead for the gory details of how to leverage SERP API for automatic, localised search results:

### How To: Leverage Nimble’s SERP API for finding relevant search results

The SERP API expects a couple of parameters:

`query` - this is the keyword or term you’d like to track

`search_engine` - the engine you’d like to test in. For obvious reasons, we’ll go with `google_search` but Bing and Yandex are also available for the search engines purists

A big advantage of the SERP API being built on top of the extensive Nimble proxy network is the option to specify a `country` and `locale` for keywords that target only specific markets.

As an example, let’s go with searching for recommendations for a calendar app.

The SERP API parameters:

`query`: `calendar app recommendations`

country: `US`

locale: `en`

```bash
curl -X POST '<https://api.webit.live/api/v1/realtime/serp>' \\
-H 'Authorization: Basic <auth_credentials>' \\
-H 'Content-Type: application/json' \\
--data-raw '{
"parse": true,
"query": "calendar app recommendation",
"search_engine": "google_search",
"format": "json",
"render": true,
"country": "US",
"locale": "en"
}'
```

Result: An active Reddit post came up 3rd in the `OrganicResult` API response.

<figure><img src="https://1919898886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FZNy4aqrBN53tR8DpTEuW%2Fuploads%2Frl7V62L0LC30sgBXiOnx%2Fimage.png?alt=media&#x26;token=5e4c91b4-1be7-41bb-a621-9b2653ed0b8f" alt=""><figcaption></figcaption></figure>

There are also several other related posts from other sub-reddits the API returns which we can capture and visit.

#### Top Reddit result

<https://www.reddit.com/r/ios/comments/197kwxt/whats_everyones_preferred_calendar_app/>

#### Other related results

<https://www.reddit.com/r/productivity/comments/10999vx/whats_your_favourite_app_that_can_work_as_a/>

<https://www.reddit.com/r/productivity/comments/10v4d3w/best_calendartodo_app/>

<https://www.reddit.com/r/androidapps/comments/16n7dba/what_you_consider_to_be_the_best_calendar_app/>

<https://www.reddit.com/r/mac/comments/1aw14ff/recommendations_for_a_better_calendar_app/>
