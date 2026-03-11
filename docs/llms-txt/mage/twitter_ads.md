# Source: https://docs.mage.ai/data-integrations/sources/twitter_ads.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Twitter Ads

![Twitter Ads](https://user-images.githubusercontent.com/80284865/233933127-e360397e-5997-4b16-9df3-6363a62809a7.png)

<br />

## Configuration

Connect to the Twitter Ads API and extract campaign and ad performance data by providing the following configuration parameters:

| Key                   | Description                                                                                        | Sample Value                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `start_date`          | Absolute beginning date for syncing bookmarked endpoints (`YYYY-MM-DDTHH:MM:SSZ`).                 | `2023-01-01T00:00:00Z`                                                                                            |
| `consumer_key`        | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) consumer key.        | `YOUR_TWITTER_ADS_CONSUMER_KEY`                                                                                   |
| `consumer_secret`     | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) consumer secret.     | `YOUR_TWITTER_ADS_CONSUMER_SECRET`                                                                                |
| `access_token`        | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) access token.        | `YOUR_TWITTER_ADS_ACCESS_TOKEN`                                                                                   |
| `access_token_secret` | [OAuth 1.0a](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) access token secret. | `YOUR_TWITTER_ADS_ACCESS_TOKEN_SECRET`                                                                            |
| `account_ids`         | Comma-delimited list of Twitter Ad Account IDs.                                                    | `id1, id2, id3`                                                                                                   |
| `attribution_window`  | Number of days for latency look-back period to stabilize analytics reporting.                      | `14`                                                                                                              |
| `with_deleted`        | Include logically deleted records in the results (`true` or `false`).                              | `true`                                                                                                            |
| `country_codes`       | Comma-delimited list of ISO 2-letter country codes for targeting and segmentation.                 | `US, CA, MX, DE`                                                                                                  |
| `page_size`           | Optional: custom `page_size` for pagination.                                                       | `1000`                                                                                                            |
| `reports`             | List of reports with `name`, `entity`, `segment`, and `granularity` details.                       | `[{"name": "campaigns_genders_hourly_report", "entity": "CAMPAIGN", "segment": "GENDER", "granularity": "HOUR"}]` |
| `request_timeout`     | Timeout for the Twitter Ads API client (default: 300 seconds).                                     | `300`                                                                                                             |

<br />

## How to Get Access to the Twitter Ads API

To use the Twitter Ads source, you must first get access to the Twitter Ads API. Follow [this guide](https://developer.twitter.com/en/docs/twitter-ads-api/getting-started) to apply for access and configure your app credentials.

<br />

## What is Twitter Ads?

[Twitter Ads](https://ads.twitter.com/) is an advertising platform that allows businesses to promote content, grow followers, and drive engagement through highly targeted ad campaigns across the Twitter network.

<br />

## Why Integrate Twitter Ads with Mage?

* **Automated marketing insights**: Extract detailed campaign, ad group, and ad-level performance metrics.
* **Advanced segmentation**: Access granular breakdowns by gender, location, device, and more.
* **Real-time reporting**: Keep your analytics and BI dashboards updated with the latest ad performance data.
* **Scalable API extraction**: Efficiently handle large ad accounts and high-volume data reporting.
* **Secure and reliable**: OAuth 1.0a authentication ensures secure API access.

<br />

## Supported Streams

The following Twitter Ads objects are extracted:

* account\_media
* accounts
* advertiser\_business\_categories
* campaigns
* cards
* cards\_image\_conversation
* cards\_poll
* cards\_video\_conversation
* content\_categories
* funding\_instruments
* iab\_categories
* line\_item\_apps
* line\_items
* media\_creatives
* preroll\_call\_to\_actions
* promotable\_users
* promoted\_accounts
* promoted\_tweets
* scheduled\_promoted\_tweets
* tailored\_audiences
* targeting\_app\_store\_categories
* targeting\_conversations
* targeting\_criteria
* targeting\_devices
* targeting\_events
* targeting\_interests
* targeting\_languages
* targeting\_locations
* targeting\_network\_operators
* targeting\_platform\_versions
* targeting\_platforms
* targeting\_tv\_markets
* targeting\_tv\_shows
* tracking\_tags
* tweets

<br />


Built with [Mintlify](https://mintlify.com).