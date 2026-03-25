# Source: https://docs.brightdata.com/api-reference/web-scraper-api/social-media-apis/tiktok.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TikTok API Scrapers

## Overview

The TikTok API Suite offers multiple types of APIs, each designed for specific data collection needs from TikTok. Below is an overview of how these APIs connect and interact, based on the available features:

<CardGroup cols="1">
  <Card title="Profile API" icon="user" href="/api-reference/web-scraper-api/social-media-apis/tiktok#profile-api">
    This API allows users to collect profile details based on a single input: profile URL.

    <br />

    *   **Discovery functionality**:

    *   Direct URL of the search

    <br />

    *   **Interesting Columns**:

    *   `nickname`, `awg_engagement_rate`, `followers`, `likes`
  </Card>

  <Card title="Posts API" icon="images" href="/api-reference/web-scraper-api/social-media-apis/tiktok#posts-api">
    This API allows users to collect multiple posts based on a single input URL.

    <br />

    *   **Discovery functionality**:

    *   - Direct URL of the TikTok profile

    *   - Discover by keywords

    *   - Direct URL of the discovery

    <br />

    *   **Interesting Columns**:

    *   `url`, `share_count`, `description`, `hashtags`
  </Card>

  <Card title="Comments API" icon="comments" href="/api-reference/web-scraper-api/social-media-apis/tiktok#comments-api">
    This API allows users to collect multiple comments from a post using its URL.

    <br />

    *   **Discovery functionality**:

    *   N/A

    <br />

    *   **Interesting Columns**:

    *   `url`, `comment_text`, `commenter_url`, `num_likes`
  </Card>
</CardGroup>

## Profile API

### Collect by URL

This API allows users to retrieve detailed TikTok profile information using the provided profile URL.

**Input Parameters**:

<ParamField path="URL" type="string" required="true">
  The TikTok profile URL.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Profile Details**:\
  `account_id`, `nickname`, `biography`, `bio_link`, `predicted_lang`, `is_verified`, `followers`, `following`, `likes`, `videos_count`, `create_time`, `id`, `url`, `profile_pic_url`, `profile_pic_url_hd`, and more.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_l1villgoiiidt09ci?tab=overview).

* **Engagement Metrics**:\
  `awg_engagement_rate`, `comment_engagement_rate`, `like_engagement_rate`, `like_count`, `digg_count`.

* **Privacy & Settings**:\
  `is_private`, `relation`, `open_favorite`, `comment_setting`, `duet_setting`, `stitch_setting`, `is_ad_virtual`, `room_id`, `is_under_age_18`.

* **Discovery & Top Videos**:\
  `region`, `top_videos`, `discovery_input`.

This API allows users to retrieve detailed TikTok profile information, including engagement metrics, privacy settings, and top videos, offering insights into user activity and profile data.

### Discover by Search URL

This API allows users to discover TikTok profiles based on a specific search URL and country, providing detailed profile information.

**Input Parameters**:

<ParamField path="search_url" type="string" required="true">
  The TikTok search URL.
</ParamField>

<ParamField path="country" type="string" required="true">
  The country from which to perform the search.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Profile Details**:\
  `account_id`, `nickname`, `biography`, `bio_link`, `predicted_lang`, `is_verified`, `followers`, `following`, `likes`, `videos_count`, `create_time`, `id`, `url`, `profile_pic_url`, `profile_pic_url_hd`, and more.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_l1villgoiiidt09ci/search_url?tab=overview).

* **Engagement Metrics**:\
  `awg_engagement_rate`, `comment_engagement_rate`, `like_engagement_rate`, `like_count`, `digg_count`.

* **Privacy & Settings**:\
  `is_private`, `relation`, `open_favorite`, `comment_setting`, `duet_setting`, `stitch_setting`, `is_ad_virtual`, `room_id`, `is_under_age_18`.

* **Discovery & Top Videos**:\
  `region`, `top_videos`, `discovery_input`.

This API enables users to discover TikTok profiles based on search criteria, offering insights into user activity, engagement, privacy settings, and top content. It helps facilitate efficient discovery and analysis of TikTok users.

## Posts API

### Collect by URL

This API enables users to collect detailed data from TikTok posts by providing a post URL.

**Input Parameters**:

<ParamField path="URL" type="string" required="true">
  The TikTok post URL.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Post Details**:\
  `post_id`, `description`, `create_time`, `share_count`, `collect_count`, `comment_count`, `play_count`, `video_duration`, `hashtags`, `original_sound`, `official_item`, `original_item`, `shortcode`, `video_url`, `music`, `cdn_url`, `width`, `carousel_images`, and more.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lu702nij2f790tmv9h?tab=overview).

* **Profile Details**:\
  `profile_id`, `profile_username`, `profile_url`, `profile_avatar`, `profile_biography`, `account_id`, `profile_followers`, `is_verified`.

* **Tagged Users and Media**:\
  `tagged_user`, `carousel_images`.

* **Additional Information:**:\
  `tt_chain_token`, `secu_id`

### Discover by Profile URL

This API allows users to retrieve posts from a TikTok profile based on a provided profile URL, with filtering options for the number of posts, date range, and post exclusions.

**Input Parameters**:

<ParamField path="URL" type="string" required="true">
  The TikTok profile URL.
</ParamField>

<ParamField path="num_of_posts" type="number">
  The number of posts to collect. If not provided, there is no limit.
</ParamField>

<ParamField path="posts_to_not_include" type="array">
  An array of post IDs to exclude from the collection.
</ParamField>

<ParamField path="start_date" type="string">
  Start date for filtering posts (format: mm-dd-yyyy). Should be lower than `end_date`.
</ParamField>

<ParamField path="end_date" type="string">
  End date for filtering posts (format: mm-dd-yyyy). Should be greater than `start_date`.
</ParamField>

<ParamField path="what_to_collect" type="string">
  Specify the type of posts to collect (e.g., "post" or "reel").
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Post Details**:\
  `post_id`, `description`, `create_time`, `share_count`, `collect_count`, `comment_count`, `play_count`, `video_duration`, `hashtags`, `original_sound`, `official_item`, `original_item`, `shortcode`, `video_url`, `music`, `cdn_url`, `width`, `carousel_images`, and more.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lu702nij2f790tmv9h/profile_url?tab=overview).

* **Profile Details**:\
  `profile_id`, `profile_username`, `profile_url`, `profile_avatar`, `profile_biography`, `account_id`, `profile_followers`, `is_verified`.

* **Tagged Users and Media**:\
  `tagged_user`, `carousel_images`.

* **Additional Information**:\
  `tt_chain_token`, `secu_id`.

This API allows users to discover and retrieve detailed information about posts from a specific TikTok profile, including post-specific metrics, profile details of the creator, and tagged users. It supports efficient content discovery and post analysis.

### Discover by Keywords

This API allows users to search for TikTok posts based on specific keywords or hashtags, offering a powerful tool for discovering relevant content across TikTok's platform.

**Input Parameters**:

<ParamField path="search_keyword" type="string" required="true">
  The keyword or hashtag to search for within TikTok posts.
</ParamField>

<ParamField path="num_of_posts" type="number">
  The number of posts to collect. If not provided, there is no limit.
</ParamField>

<ParamField path="posts_to_not_include" type="array">
  An array of post IDs to exclude from the collection.
</ParamField>

<ParamField path="what_to_collect" type="string">
  Specify the type of posts to collect (e.g., "post" or "reel").
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Post Details**:\
  `post_id`, `description`, `create_time`, `digg_count`, `share_count`, `collect_count`, `comment_count`, `play_count`, `video_duration`, `hashtags`, `original_sound`, `post_type`, `discovery_input`, `official_item`, and more.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lu702nij2f790tmv9h/keyword?tab=overview).

* **Profile Details**:\
  `profile_id`, `profile_username`, `profile_url`, `profile_avatar`, `profile_biography`, `account_id`, `profile_followers`, `is_verified`.

* **Tagged Users and Media**:\
  `tagged_user`, `carousel_images`.

* **Additional Information**:\
  `tt_chain_token`, `secu_id`.

This API allows users to discover posts on TikTok that match specific keywords or hashtags, providing insights into post details, profile information, and media. It’s a great tool for exploring trends, content, and users on TikTok.

### Discover by Discover URL

This API allows users to collect detailed post data from a specific TikTok discover URL.

**Input Parameters**:

<ParamField path="URL" type="string" required="true">
  The TikTok discover URL from which posts will be retrieved.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Post Details**:\
  `post_id`, `description`, `create_time`, `digg_count`, `share_count`, `collect_count`, `comment_count`, `play_count`, `video_duration`, `hashtags`, `original_sound`, `post_type`, `discovery_input`, `official_item`, `original_item`, and more.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lu702nij2f790tmv9h/url?tab=overview).

* **Profile Details**:\
  `profile_id`, `profile_username`, `profile_url`, `profile_avatar`, `profile_biography`, `account_id`, `profile_followers`, `is_verified`.

* **Tagged Users and Media**:\
  `tagged_user`, `carousel_images`.

* **Additional Information**:\
  `tt_chain_token`, `secu_id`.

This API provides detailed insights into TikTok posts discovered via the discover URL, allowing for easy access to trending content, user profiles, and post metadata for analysis and exploration.

## Comments API

### Collect by URL

This API allows users to collect detailed comment data from a specific TikTok post using the provided post URL.

**Input Parameters**:

<ParamField path="URL" type="string" required="true">
  The TikTok post URL.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Post Details**:\
  `post_url`, `post_id`, `post_date_created`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lkf2st302ap89utw5k?tab=overview).

* **Comment Details**:\
  `date_created`, `comment_text`, `num_likes`, `num_replies`, `comment_id`, `comment_url`.

* **Commenter Details**:\
  `commenter_user_name`, `commenter_id`, `commenter_url`.

This API provides detailed insights into TikTok post comments, including comment-specific metrics and information about the commenters, enabling effective comment analysis and interaction tracking.
