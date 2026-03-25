# Source: https://docs.airbyte.com/integrations/sources/metricool.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-metricool/latest/icon.svg)

# Metricool

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.0.18](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-metricool)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-metricool)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `e4e1ed94-f374-47fe-8dfa-872fb9935fbe`

The Metricool connector enables you to extract comprehensive social media analytics data from multiple platforms through Metricool’s unified API. This connector supports data extraction from Facebook, Instagram, TikTok, LinkedIn, Twitter (X), and YouTube, providing detailed insights into your social media performance.

Key Features:

* Multi-Platform Support: Extract data from 6 major social media platforms in a single connector
* Comprehensive Analytics: Access post-level metrics, timeline data, competitor analysis, and content performance
* Flexible Date Range: Configure custom date ranges for data extraction (defaults to 60 days if not specified)
* Multiple Content Types: Supports various content formats including posts, reels, stories, and videos

Supported Data Streams:

* Brand Information: Basic account and profile data
* Content Analytics: Posts, reels, stories, and videos with engagement metrics
* Timeline Data: Historical performance metrics tracked over time
* Competitor Analysis: Available for Facebook and Instagram

## Configuration[​](#configuration "Direct link to Configuration")

| Input        | Type     | Description                                                                                                                       | Default Value |
| ------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `user_token` | `string` | User Token. User token to authenticate API requests. Find it in the Account Settings menu, API section of your Metricool account. |               |
| `user_id`    | `string` | User ID. Account ID                                                                                                               |               |
| `blog_ids`   | `array`  | Blog IDs. Brand IDs                                                                                                               |               |
| `start_date` | `string` | Start Date. If not set, defaults to 60 days back. If below "End Date", defaults to 1 day before "End Date"                        |               |
| `end_date`   | `string` | End Date. If not set, defaults to current datetime.                                                                               |               |

## Streams[​](#streams "Direct link to Streams")

| Stream Name                   | Primary Key            | Pagination    | Supports Full Sync | Supports Incremental |
| ----------------------------- | ---------------------- | ------------- | ------------------ | -------------------- |
| brands                        | id                     | No pagination | ✅                 | ❌                   |
| facebook\_competitors         | id                     | No pagination | ✅                 | ❌                   |
| facebook\_stories             | blogId.storyId         | No pagination | ✅                 | ❌                   |
| facebook\_posts               | blogId.postId          | No pagination | ✅                 | ❌                   |
| facebook\_reels               | blogId.reelId          | No pagination | ✅                 | ❌                   |
| facebook\_stories\_timelines  | datetime.blogId.metric | No pagination | ✅                 | ✅                   |
| facebook\_posts\_timelines    | datetime.blogId.metric | No pagination | ✅                 | ✅                   |
| facebook\_reels\_timelines    | datetime.blogId.metric | No pagination | ✅                 | ✅                   |
| instagram\_competitors        | id                     | No pagination | ✅                 | ❌                   |
| instagram\_stories            | blogId.postId          | No pagination | ✅                 | ❌                   |
| instagram\_posts              | blogId.postId          | No pagination | ✅                 | ❌                   |
| instagram\_reels              | blogId.reelId          | No pagination | ✅                 | ❌                   |
| instagram\_stories\_timelines | datetime.blogId.metric | No pagination | ✅                 | ✅                   |
| instagram\_posts\_timelines   | datetime.blogId.metric | No pagination | ✅                 | ✅                   |
| instagram\_reels\_timelines   | datetime.blogId.metric | No pagination | ✅                 | ✅                   |
| tiktok\_posts                 | blogId.videoId         | No pagination | ✅                 | ❌                   |
| tiktok\_video\_timelines      | datetime.blogId.metric | No pagination | ✅                 | ✅                   |
| tiktok\_account\_timelines    | datetime.blogId.metric | No pagination | ✅                 | ✅                   |
| linkedin\_posts               | postId                 | No pagination | ✅                 | ❌                   |
| twitter\_posts                | id                     | No pagination | ✅                 | ❌                   |
| youtube\_posts                | videoId                | No pagination | ✅                 | ❌                   |

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

Blog IDs

required

array

blog\_ids

›

User ID

required

string

user\_id

›

User Token

required

string

user\_token

›

End Date

string

end\_date

›

Start Date

string

start\_date

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                                               |
| ------- | ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 0.0.18  | 2026-02-24 | [73809](https://github.com/airbytehq/airbyte/pull/73809) | Update dependencies                                                                   |
| 0.0.17  | 2026-02-17 | [73392](https://github.com/airbytehq/airbyte/pull/73392) | Update dependencies                                                                   |
| 0.0.16  | 2026-02-10 | [73188](https://github.com/airbytehq/airbyte/pull/73188) | Update dependencies                                                                   |
| 0.0.15  | 2026-01-20 | [72034](https://github.com/airbytehq/airbyte/pull/72034) | Update dependencies                                                                   |
| 0.0.14  | 2026-01-14 | [71527](https://github.com/airbytehq/airbyte/pull/71527) | Update dependencies                                                                   |
| 0.0.13  | 2025-12-18 | [70748](https://github.com/airbytehq/airbyte/pull/70748) | Update dependencies                                                                   |
| 0.0.12  | 2025-11-25 | [70118](https://github.com/airbytehq/airbyte/pull/70118) | Update dependencies                                                                   |
| 0.0.11  | 2025-11-18 | [69550](https://github.com/airbytehq/airbyte/pull/69550) | Update dependencies                                                                   |
| 0.0.10  | 2025-10-29 | [69063](https://github.com/airbytehq/airbyte/pull/69063) | Update dependencies                                                                   |
| 0.0.9   | 2025-10-21 | [68413](https://github.com/airbytehq/airbyte/pull/68413) | Update dependencies                                                                   |
| 0.0.8   | 2025-10-14 | [67838](https://github.com/airbytehq/airbyte/pull/67838) | Update dependencies                                                                   |
| 0.0.7   | 2025-10-07 | [67376](https://github.com/airbytehq/airbyte/pull/67376) | Update dependencies                                                                   |
| 0.0.6   | 2025-09-30 | [66340](https://github.com/airbytehq/airbyte/pull/66340) | Update dependencies                                                                   |
| 0.0.5   | 2025-09-09 | [65802](https://github.com/airbytehq/airbyte/pull/65802) | Update dependencies                                                                   |
| 0.0.4   | 2025-08-23 | [65179](https://github.com/airbytehq/airbyte/pull/65179) | Update dependencies                                                                   |
| 0.0.3   | 2025-08-16 | [64965](https://github.com/airbytehq/airbyte/pull/64965) | Update dependencies                                                                   |
| 0.0.2   | 2025-08-15 | [64942](https://github.com/airbytehq/airbyte/pull/64942) | Fix docker image entrypoint for platform syncs                                        |
| 0.0.1   | 2025-08-06 |                                                          | Initial release by [@santigiova](https://github.com/santigiova) via Connector Builder |
