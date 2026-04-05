<!--
source: https://desearch.ai/docs/guide/capabilities/x-queries
title: X (Twitter) Queries - Capabilities Documentation | Desearch
captured: 2026-04-04
-->
# X (Twitter) Queries - Capabilities Documentation | Desearch

Source: https://desearch.ai/docs/guide/capabilities/x-queries

---

Home
Guide
API Reference
SDKs
API Console
API Status
GitHub
Discord
Blog
Search guides...
⌘K
INTRODUCTION
Desearch AI
Desearch Console
Glossary
APIS
Desearch API
Desearch x Bittensor
API Keys
Authorization
Pricing and Billing
SDK
Desearch API SDK
Python SDK Specification
JavaScript SDK Specification
INTEGRATIONS
MCP
OpenAI Wrapper
Function Calling with GPT
Function Calling with Claude
RAG with LangChain x Desearch
RAG with LlmaIndex x Desearch
ElizaOs Agents with Desearch
CrewAI Agents with Desearch
Browser Use x Desearch
OpenClaw Agent with Desearch
Numinous SN6 × Desearch Integration
USE CASES
Search Engine Use Cases
AI-Driven Chat Use Cases
Intelligent Agent Task Automation
CAPABILITIES
X (Twitter) Queries
X (Twitter) Queries
Advanced Search on X (Twitter)

These operators work on Web, Mobile, Tweetdeck.

There is some overlap, but largely these will not work for v1.1 Search, Premium Search, or v2 Search APIs.

Adapted from TweetDeck Help, @lucahammer Guide, @eevee Twitter Manual, @pushshift and Twitter / Tweetdeck itself. Contributions/tests, examples welcome!

Tweet Content

| Operator | Finds Tweets | Example |
|----------|--------------|---------|
| nasa esa (nasa esa) | Containing both "nasa" and "esa". Spaces are implicit AND. Brackets can be used to group individual words when using other operators. | [Link](https://twitter.com/search) |
| nasa OR esa | Either "nasa" or "esa". OR must be in uppercase. | [Link](https://twitter.com/search) |
| "state of the art" | The complete phrase "state of the art". Will also match "state-of-the-art". Also, use quotes to prevent spelling correction. | [Link](https://twitter.com/search) |
| "this is the * time this week" | A complete phrase with a wildcard. Asterisk does not work outside of a quoted phrase or without spaces. | [Link](https://twitter.com/search) |
| +radiooooo | Force a term to be included as-is. Useful to prevent spelling correction. | [Link](https://twitter.com/search) |
| -love -"live laugh love" | Hyphen is used for excluding "love". Also applies to quoted phrases and other operators. | [Link](https://twitter.com/search) |
| #tgif | A hashtag | [Link](https://twitter.com/search) |
| $TWTR | A cashtag, like hashtags but for stock symbols | [Link](https://twitter.com/search) |
| What ? | Question marks are matched | [Link](https://twitter.com/search) |
| :) OR :( | Some emoticons are matched, positive :) :-) :P :D or negative :-( :( | [Link](https://twitter.com/search) |
| 👀 | Emoji searches are also matched. Usually needs another operator to work. | [Link](https://twitter.com/search) |
| url:google.com | URLs are tokenized and matched, working very well for subdomains and domains, but not as well for long URLs, which depend on the specific URL. YouTube IDs work well. Works for both shortened and canonical URLs, eg,gu.com shortener for theguardian.com. When searching for Domains with hyphens in them, you have to replace the hyphen with an underscore (like url:t_mobile.com) but underscores are also tokenized out, and may not match | [Link](https://twitter.com/search) |
| lang:en | Search for tweets in specified language, not always accurate, see the full list and special lang codes below. | [Link](https://twitter.com/search) |

Users

| Operator | Finds Tweets | Example |
|----------|--------------|---------|
| from:user | Sent by a particular @username e.g. "dogs from:NASA" | [Link](https://twitter.com/search) |
| to:user | Replying to a particular @username | [Link](https://twitter.com/search) |
| @user | Mentioning a particular @username. Combine with -from:username to get only mentions | [Link](https://twitter.com/search) |
| list:715919216927322112 list:esa/astronauts | Tweets from members of this public list. Use the list ID from the API or with URLs like twitter.com/i/lists/715919216927322112. List slug is for old list URLs like twitter.com/esa/lists/astronauts. Cannot be negated, so you can't search for "not on list". | [Link](https://twitter.com/search) |
| filter:verified | From verified users | [Link](https://twitter.com/search) |
| filter:blue_verified | From "verified" users who paid $8 for Twitter Blue | [Link](https://twitter.com/search) |
| filter:follows | Only from accounts you follow. Cannot be negated. | [Link](https://twitter.com/search) |
| filter:social filter:trusted | Only from an algorithmically expanded network of accounts based on your own follows and activities. Works on "Top" results not "Latest" | [Link](https://twitter.com/search) |

Geo

| Operator | Finds Tweets | Example |
|----------|--------------|---------|
| near:city | Geotagged in this place. Also supports Phrases, eg: near:"The Hague" | [Link](https://twitter.com/search) |
| near:me | Near where Twitter thinks you are | [Link](https://twitter.com/search) |
| within:radius | Within a specific radius of the "near" operator, to apply a limit. Can use km or mi. e.g. fire near:san-francisco within:10km | [Link](https://twitter.com/search) |
| geocode:lat,long,radius | E.g., to get tweets 10km around Twitter's hq, use geocode:37.7764685,-122.4172004,10km | [Link](https://twitter.com/search) |
| place:96683cc9126741d1 | Search tweets by Place Object ID eg: USA Place ID is 96683cc9126741d1 | [Link](https://twitter.com/search) |

Time

| Operator | Finds Tweets | Example |
|----------|--------------|---------|
| since:2021-12-31 | On or after (inclusive) a specified date. 4 digit year, 2 digit month, 2 digit day separated by dash. | [Link](https://twitter.com/search) |
| until:2021-12-31 | Before (NOT inclusive) a specified date. Combine with a "since" operator for dates between. | [Link](https://twitter.com/search) |
| since:2021-12-31_23:59:59_UTC | On or after (inclusive) a specified date and time in the specified timezone. 4 digit year, 2 digit month, 2 digit day separated by dashes, an underscore separating the 24-hour clock format hours:minutes:seconds and timezone abbreviation. | [Link](https://twitter.com/search) |
| until:2021-12-31_23:59:59_UTC | Before (NOT inclusive) a specified date and time in the specified timezone. Combine with a "since" operator for dates between. | [Link](https://twitter.com/search) |
| since_time:1142974200 | On or after a specified Unix timestamp in seconds. Combine with the "until" operator for dates between. Maybe easier to use than since_id below. | [Link](https://twitter.com/search) |
| until_time:1142974215 | Before a specified Unix timestamp in seconds. Combine with a "since" operator for dates between. Maybe easier to use than max_id below. | [Link](https://twitter.com/search) |
| since_id:tweet_id | After (NOT inclusive) a specified Snowflake ID (See Note below) | [Link](https://twitter.com/search) |
| max_id:tweet_id | At or before (inclusive) a specified Snowflake ID (see Note below) | [Link](https://twitter.com/search) |
| within_time:2d within_time:3h within_time:5m within_time:30s | Search within the last number of days, hours, minutes, or seconds | [Link](https://twitter.com/search) |

Tweet Type

| Operator | Finds Tweets | Example |
|----------|--------------|---------|
| filter:nativeretweets | Only retweets created using the retweet button. Works well combined with from: to show only retweets. Only works within the last 7-10 days or so. | [Link](https://twitter.com/search) |
| include:nativeretweets | Native retweets are excluded by default. This shows them. In contrast to filter:, which indicates only retweets, and this includes retweets in addition to other tweets. Only works within the last 7-10 days or so. | [Link](https://twitter.com/search) |
| filter:retweets | Old-style retweets ("RT") + quoted tweets. | [Link](https://twitter.com/search) |
| filter:replies | The tweet is a reply to another Tweet. good for finding conversations, or threads if you add or remove to:user | [Link](https://twitter.com/search) |
| filter:self_threads | Only self-replies. Tweets that are part of a thread, not replies in other conversations. | [Link](https://twitter.com/search) |
| conversation_id:tweet_id | Tweets that are part of a thread (direct replies and other replies) | [Link](https://twitter.com/search) |
| filter:quote | Contain Quote Tweets | [Link](https://twitter.com/search) |
| quoted_tweet_id:tweet_id | Search for quotes of a specific tweet | [Link](https://twitter.com/search) |
| quoted_user_id:user_id | Search for all quotes of a specific user, by numeric User ID (See Note below) | [Link](https://twitter.com/search) |
| card_name:poll2choice_text_only card_name:poll3choice_text_only card_name:poll4choice_text_only card_name:poll2choice_image card_name:poll3choice_image card_name:poll4choice_image | Tweets containing polls. For polls containing 2, 3, 4, or image choices. | [Link](https://twitter.com/search) |

Engagement

| Operator | Finds Tweets | Example |
|----------|--------------|---------|
| filter:has_engagement | Has some engagement (replies, likes, retweets). Can be negated to find tweets with no engagement. Note all of these are mutually exclusive with filter:nativeretweets or include:nativeretweets, as they apply to the retweet, not the original tweet, so they won't work as expected. | [Link](https://twitter.com/search) |
| min_retweets:5 | A minimum number of Retweets. Counts appear to be approximate for larger values (e.g., 1000+). | [Link](https://twitter.com/search) |
| min_faves:10 | A minimum number of Likes | [Link](https://twitter.com/search) |
| min_replies:100 | A minimum number of replies | [Link](https://twitter.com/search) |
| -min_retweets:500 | A maximum number of Retweets | [Link](https://twitter.com/search) |
| -min_faves:500 | A maximum number of Likes | [Link](https://twitter.com/search) |
| -min_replies:100 | A maximum number of replies | [Link](https://twitter.com/search) |

Media

| Operator | Finds Tweets | Example |
|----------|--------------|---------|
| filter:media | All media types. | [Link](https://twitter.com/search) |
| filter:twimg | Native Twitter images (pic.twitter.com links) | [Link](https://twitter.com/search) |
| filter:images | All images. | [Link](https://twitter.com/search) |
| filter:videos | All video types, including native Twitter video and external sources such as YouTube. | [Link](https://twitter.com/search) |
| filter:periscope | Periscopes | [Link](https://twitter.com/search) |
| filter:native_video | All Twitter-owned video types (native video, Vine, Periscope) | [Link](https://twitter.com/search) |
| filter:vine | Vines (RIP) | [Link](https://twitter.com/search) |
| filter:consumer_video | Twitter native video only | [Link](https://twitter.com/search) |
| filter:pro_video | Twitter pro video (Amplify) only | [Link](https://twitter.com/search) |
| filter:spaces | Twitter Spaces only | [Link](https://twitter.com/search) |

More Filters

| Operator | Finds Tweets | Example |
|----------|--------------|---------|
| filter:links | Only containing some URLs, including media. use -filter:media for urls that aren't media | [Link](https://twitter.com/search) |
| filter:mentions | Containing any sort of @mentions | [Link](https://twitter.com/search) |
| filter:news | It contains a link to a news story. Combine with a list operator to further narrow down the user set. Matches on a list of Domains (See Note for full list) | [Link](https://twitter.com/search) |
| filter:safe | Excluding NSFW content. Excludes content that users have marked as "Potentially Sensitive". Doesn't always guarantee SFW results. | [Link](https://twitter.com/search) |
| filter:hashtags | Only Tweets with Hashtags. | [Link](https://twitter.com/search) |

App Specific

| Operator | Finds Tweets | Example |
|----------|--------------|---------|
| source:client_name | Sent from a specified client e.g., source:tweetdeck (See Note for common ones,) e.g. twitter_ads doesn't work on it's own, but does with another operator. | [Link](https://twitter.com/search) |
| card_domain:pscp.tv | Matches domain name in a Twitter Card. Mostly equivalent to url: operator. | [Link](https://twitter.com/search) |
| card_url:pscp.tv | Matches domain name in a Card, but with different results to card_domain. | [Link](https://twitter.com/search) |
| card_name:audio | Tweets with a Player Card (Links to Audio sources, Spotify, Soundcloud etc.) | [Link](https://twitter.com/search) |
| card_name:animated_gif | Tweets With GIFs | [Link](https://twitter.com/search) |
| card_name:player | Tweets with a Player Card | [Link](https://twitter.com/search) |
| card_name:app card_name:promo_image_app | Tweets with links to an App Card. promo_app does not work, promo_image_app is for an app link with a large image, usually posted in Ads. | [Link](https://twitter.com/search) |
| card_name:summary | Only Small image summary cards | [Link](https://twitter.com/search) |
| card_name:summary_large_image | Only large image Cards | [Link](https://twitter.com/search) |
| card_name:promo_website | Larger than summary_large_image, usually posted via Ads | [Link](https://twitter.com/search) |
| card_name:promo_image_convo card_name:promo_video_convo | Finds Conversational Ads cards. | [Link](https://twitter.com/search) |
| card_name:3260518932:moment | Find Moments cards. 3260518932 is the user ID of @TwitterMoments, but the search finds moments for everyone, not that specific user. | [Link](https://twitter.com/search) |
Matching

On web and mobile, keyword operators can match on: The user's name, the @ screen name, tweet text, and shortened, as well as expanded URL text (eg, url:trib.al finds accounts that use that shortener, even though the full URL is displayed.

By default, "Top" results are shown, where "Top" refers to tweets with some level of engagement (replies, retweets, likes). "Latest" has the most recent tweets. People search will match on descriptions, but not all operators work. "Photos" and "Videos" are presumably equivalent to filter:images and filter:videos.

Exact Tokenization is not known, but it's most likely a custom one to preserve entities. URLs are also tokenized. Spelling correction appears sometimes, and also plurals are matched, eg: bears will also match tweets with bear. - not preceding an operator is removed, so "state-of-the-art" is the same as "state of the art".

Private accounts are not included in the search index, and their tweets do no appear in results. Locked and suspended accounts are also hidden from results. There are other situations where tweets may not appear, such as when anti-spam measures are in effect, or tweets have not been indexed due to server issues.

Twitter is using some words as signal words. E.g., when you search for “photo”, Twitter assumes you’re looking for Tweets with attached photos. If you want to search for Tweets that literally contain the word “photo”, you have to wrap it in double quotes "photo".

Building Queries

Most "filter:type" can also be negated using the "-" symbol, with exceptions like filter:follows which can't be negated. exclude:links is the same as -filter:links. It's sometimes worth trying an alias like that in case the search doesn't work the first time.

Example 1: I want mentions of either "puppy" or "kitten", AND with mentions of either "sweet" or "cute", excluding Retweets, with at least 10 likes.

(puppy OR kitten) (sweet OR cute) -filter:nativeretweets min_faves:10

Example 2: I want Tweets from @Nasa with all types of media except images

from:NASA filter:media -filter:images

Combine complex queries together writh booleans and parentheses to refine your results. Spaces are implicit logical AND, but OR must be explicitly included.

Example 3: I want mentions of "space" and either "big" or "large" by members of the NASA astronauts List, sent from an iPhone or twitter.com, with images, excluding mentions of #asteroid, since 2011.

space (big OR large) list:nasa/astronauts (source:twitter_for_iphone OR source:twitter_web_client) filter:images since:2011-01-01 -#asteroid

Limitations

Known Limitations: card_name:Only works for the last 7-8 days.

The maximum number of operators seems to be about 22 or 23. All the Time operators must be used in conjunction with something else to function properly.

Tweetdeck Equivalents

Tweetdeck options for columns have equivalents you can use on web search:

Tweets with Images: filter:images
Videos: filter:videos
Tweets with GIFs: card_name:animated_gif
"Tweets with broadcasts": (card_domain:pscp.tv OR card_domain:periscope.tv OR "twitter.com/i/broadcasts/")
"Any Media": (filter:images OR filter:videos)
"Any Links (includes media)": filter:links

📘 Standard API Search

Web, Mobile, Tweetdeck Search runs on one type of system (as far as i can tell), Standard API Search is a different index, Premium Search and Enterprise Search is another separate thing based on Gnip products. API docs already exist for the API and Premium but i might add guides for those separately.

Snowflake IDs

All user, tweet, DM, and some other object IDs are snowflake IDs on Twitter since 2010-06-01 and 2013-01-22 for user IDs. In short, each ID contains a timestamp.

An easy way to get a user_id from a @user_name is using tweeterid.com

To use Snowflake Tweet IDs with since_id / max_id as time delimiters, either pick a tweet ID that roughly has a created_at time you need, remembering that all times on Twitter are UTC, or use the following (This works for all tweets after Snowflake was implemented):

Convert Twitter ID to Millisecond Epoch

(tweet_id >> 22) + 1288834974657 -- This gives the millisecond epoch of when the tweet or user was created.

Convert from Epoch back to a Tweet Id

(millisecond_epoch - 1288834974657) << 22 = tweet id

Use Case

You want to start gathering all tweets for specific search terms starting at a particular time. Let's say this time in August 4, 2019 09:00:00 UTC. You can use the max_id parameter by first converting the millisecond epoch time to a tweet id. You can use https://www.epochconverter.com.

August 4, 2019 09:00:00 UTC = 1564909200000 (epoch milliseconds)

(1564909200000 - 1288834974657) << 22 = 1157939227653046272 (tweet id)

So if you set max_id to 1157939227653046272, you will start collecting tweets earlier than that datetime. This can be extremely helpful when you need to get a very specific portion of the timeline.

PYTHON
def convert_milliepoch_to_tweet_id(milliepoch):
    if milliepoch <= 1288834974657:
        raise ValueError("Date is too early (before snowflake implementation)")
    return (milliepoch - 1288834974657) << 22

📘 64 Bit Integer in Javascript

Unfortunately, JavaScript does not support 64bit integers, so these calculations and other operations on IDs often fail in unexpected ways. More details on snowflake can be found in @pushshift document here.

Quote-Tweets

From a technical perspective, Quote-Tweets are Tweets with a URL of another Tweet. It's possible to find Tweets that quote a specific Tweet by searching for the URL of that Tweet. Any parameters need to be removed or only Tweets that contain the parameter as well are found. Twitter appends a Client parameter when copying Tweet URLs through the sharing menu. Eg. ?s=20 for the Web App and ?s=09 for the Android app. Example: twitter.com/jack/status/20/ -from:jack

To find all Tweets that quote a specific user, you search for the first part of the Tweet-URL and exclude Tweets from the user: twitter.com/jack/status/ -from:jack.

Geo Searches

Very few tweets have exact geo coordinates. Exact Geo coordinates are phased out for normal tweets, but will remain for photos: https://twitter.com/TwitterSupport/status/1141039841993355264

Tweets instead can be tagged by Place

Known Unknowns and Assumptions

I have no idea how Twitter decides what should match filter:news, my guess is that it's based on a list of whitelisted domain names, as tweets from anyone can appear as long as they link to a news site, no idea if this list is public. No idea if or how this filter changed over time. But we can try to retrieve tweets and see. lang:und will match most empty tweets or tweets with a single number or link. filter:safe presumably uses the User setting "Contains Sensitive Content" - but may also apply to specific tweets somehow.

It would be great to be able to reliably find promoted tweets - this may be possible with some of the card searches. Tweets composed in Twitter Ads are available with source:twitter_ads but other promoted tweets may not have been created with that app.

I'd also like to search for Collections (Timelines) and Moments, but this seems to work ok with just url: searches. eg: url:twitter.com/i/events and url:twitter.com/i/moments (I think the difference is events are curated?) but url:twitter.com url:timelines has many false positives.

In Search Settings, "Hide Sensitive Content" equivalent is filter:safe - is there an equivalent to "Remove Blocked and Muted Accounts"?

Supported Languages

Language is specified as 2 letter ISO codes. Language is tagged automatically from the tweet text, and not always accurate, see here for notes on accuracy. The list from the TweetDeck dropdown menu has all of them:

Supported Languages

lang:am Amharic (አማርኛ)

lang:ar Arabic (العربية)

lang:bg Bulgarian (Български)

lang:bn Bengali (বাংলা)

lang:bo Tibetan (བོད་སྐད)

lang:ca Catalan (Català)

lang:ch` Cherokee (ᏣᎳᎩ)

lang:cs Czech (čeština)

lang:da Danish (Dansk)

lang:de German (Deutsch)

lang:dv Maldivian (ދިވެހި)

lang:el Greek (Ελληνικά)

lang:en English (English)

lang:es Spanish (Español)

lang:et Estonian (eesti)

lang:fa Persian (فارسی)

lang:fi Finnish (Suomi)

lang:fr French (Français)

lang:gu Gujarati (ગુજરાતી)

lang:hi Hindi (हिंदी)

lang:ht Haitian Creole (Kreyòl ayisyen)

lang:hu Hungarian (Magyar)

lang:hy Armenian (Հայերեն)

lang:in Indonesian (Bahasa Indonesia)

lang:is Icelandic (Íslenska)

lang:it Italian (Italiano)

lang:iu Inuktitut (ᐃᓄᒃᑎᑐᑦ)

lang:iw Hebrew (עברית)

lang:ja Japanese (日本語)

lang:ka Georgian (ქართული)

lang:km Khmer (ខ្មែរ)

lang:kn Kannada (ಕನ್ನಡ)

lang:ko Korean (한국어)

lang:lo Lao (ລາວ)

lang:lt Lithuanian (Lietuvių)

lang:lv Latvian (latviešu valoda)

lang:ml Malayalam (മലയാളം)

lang:my Myanmar (မြန်မာဘာသာ)

lang:ne Nepali (नेपाली)

lang:nl Dutch (Nederlands)

lang:no Norwegian (Norsk)

lang:or Oriya (ଓଡ଼ିଆ)

lang:pa Panjabi (ਪੰਜਾਬੀ)

lang:pl Polish (Polski)

lang:pt Portuguese (Português)

lang:ro Romanian (limba română)

lang:ru Russian (Русский)

lang:si Sinhala (සිංහල)

lang:sk Slovak (slovenčina)

lang:sl Slovene (slovenski jezik)

lang:sv Swedish (Svenska)

lang:ta Tamil (தமிழ்)

lang:te Telugu (తెలుగు)

lang:th Thai (ไทย)

lang:tl Tagalog (Tagalog)

lang:tr Turkish (Türkçe)

lang:uk Ukrainian (українська мова)

lang:ur Urdu (ﺍﺭﺩﻭ)

lang:vi Vietnamese (Tiếng Việt)

lang:zh Chinese (中文)

Searching for lang:chr, lang:iu, lang:sk seems to fail, as tweets matching the keywords are returned instead of the language.

Some special language codes work. For example:

lang:und for undefined language
lang:qam for tweets with mentions only (works for tweets since 2022-06-14)
lang:qct for tweets with cashtags only (works for tweets since 2022-06-14)
lang:qht for tweets with hashtags only (works for tweets since 2022-06-14)
lang:qme for tweets with media links (works for tweets since 2022-06-14)
lang:qst for tweets with a very short text (works for tweets since 2022-06-14)
lang:zxx for tweets with either media or Twitter Card only, without any additional text (works for tweets since 2022-06-14)
Common Clients

source: should work for any API client, try putting the client name in quotes or replace spaces with underscores. This is the App name field that you can alter in the developer app configuration page, so anyone can set anything here and appear to tweet from a made-up client.

You cannot copy an existing name. This operator needs to be combined with something else to work, eg: lang:en These are some common ones:

Official Twitter Clients

witter_web_client

twitter_web_app

twitter_for_iphone

twitter_for_ipad

twitter_for_mac

twitter_for_android

twitter_ads

tweetdeck

tweetdeck_web_app

twitter_for_advertisers

twitter_media_studio

cloudhopper (tweets via sms service)

🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
