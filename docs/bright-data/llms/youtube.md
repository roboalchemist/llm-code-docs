# Source: https://docs.brightdata.com/api-reference/web-scraper-api/social-media-apis/youtube.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# YouTube API Scrapers

<Note>
  If you are looking to download videos from YouTube, please contact Bright Data sales at [sales@brightdata.com](mailto:sales@brightdata.com).
</Note>

## Overview

The Youtube API Suite offers multiple types of APIs, each designed for specific data collection needs from Youtube. Below is an overview of how these APIs connect and interact, based on the available features:

<CardGroup cols={1}>
  <Card title="Profiles API" icon="user" href="/api-reference/web-scraper-api/social-media-apis/youtube#profiles-api">
    This API allows users to collect profile details based on a single input: profile URL.

    <br />

    *   **Discovery functionality**:
    *   [Discover by Keywords](/api-reference/web-scraper-api/social-media-apis/youtube#discover-profiles-by-keywords)

    <br />

    *   **Interesting Columns**:
    *   `name`, `url`, `videos_count`, `views`.
  </Card>

  <Card title="Posts API" icon="images" href="/api-reference/web-scraper-api/social-media-apis/youtube#posts-api">
    This API allows users to collect multiple posts based on a single input URL.

    <br />

    *   **Discovery functionality**:
    *   Discover by keywords.
    *   Discover by search filters.
    *   Discover by hashtag.
    *   Discover by channel URL.

    <br />

    *   **Interesting Columns**:
    *   `url`, `title`, `likes`, `views`.
  </Card>

  <Card title="Comments API" icon="comments" href="/api-reference/web-scraper-api/social-media-apis/youtube#comments-api">
    This API allows users to collect multiple comments from a post using its URL.

    <br />

    *   **Discovery functionality**:
    *   N/A

    <br />

    *   **Interesting Columns**:
    *   `comment_text`, `replies`, `likes`, `username`.
  </Card>
</CardGroup>

## Profiles API

### Collect by URL

This API allows users to retrieve detailed YouTube channel information using the provided channel URL.

**Input Parameters**:

<ParamField path="URL" type="string" required="true">
  The YouTube channel URL.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Profile Details**:\
  `url`, `handle`, `name`, `description`, `created_date`, `identifier`, `id`, `handle_md5`.
* **Engagement Metrics**:\
  `subscribers`, `videos_count`, `views`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lk538t2k2p1k3oos71?tab=overview).
* **Media Assets**:\
  `profile_image`, `banner_img`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lk538t2k2p1k3oos71?tab=overview).
* **Additional Information**:\
  `details`, `links`, `discovery_input`.

This API provides insights into YouTube channel profiles, including engagement metrics, profile assets, and detailed channel information.

### Discover by Keywords

This API allows users to discover YouTube channel profiles by searching with specific keywords related to the channel or its videos.

**Input Parameters**:

<ParamField path="keyword" type="string" required="true">
  Keyword related to the channel or its videos.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Profile Details**:\
  `url`, `handle`, `name`, `description`, `created_date`, `identifier`, `id`, `handle_md5`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lk538t2k2p1k3oos71/keyword?tab=overview).
* **Engagement Metrics**:\
  `subscribers`, `videos_count`, `views`.
* **Media Assets**:\
  `profile_image`, `banner_img`.
* **Additional Information**:\
  `details`, `links`, `discovery_input`.

This API enables efficient discovery of YouTube channel profiles based on keywords, providing profile information, engagement metrics, and related details.

## Posts API

### Collect by URL

This API allows users to retrieve detailed video information from YouTube using the provided video URL.

**Input Parameters**:

<ParamField path="URL" type="string" required="true">
  The YouTube video URL.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Video Details**:\
  `url`, `title`, `video_url`, `video_length`, `video_id`, `post_type`, `date_posted`, `description`, `music`, `transcript`, `formatted_transcript`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lk56epmy2i5g7lzu0k?tab=overview).
* **Engagement Metrics**:\
  `likes`, `views`, `num_comments`, `related_videos`.
* **Channel Details**:\
  `youtuber`, `youtuber_id`, `handle_name`, `channel_url`, `subscribers`, `verified`, `avatar_img_channel`, `youtuber_md5`.
* **Video Media & Quality**:\
  `preview_image`, `viewport_frames`, `current_optimal_res`, `codecs`, `color`, `quality`, `quality_label`.
* **Additional Information**:\
  `discovery_input`, `shortcode`, `is_sponsored`, `license`.

This API enables users to retrieve detailed insights about a YouTube video, including metadata, engagement metrics, and channel-specific details, supporting content analysis and tracking.

### Discover by Channel URL

This API allows users to collect videos published by a specific YouTube channel using its URL, with optional filters like the number of posts, date range, and sorting order.

**Input Parameters**:

<ParamField path="URL" type="string" required="true">
  The YouTube channel URL.
</ParamField>

<ParamField path="num_of_posts" type="number">
  The number of videos to collect. If omitted, there is no limit.
</ParamField>

<ParamField path="start_date" type="string">
  Start date for filtering videos (MM-DD-YYYY).
</ParamField>

<ParamField path="end_date" type="string">
  End date for filtering videos (MM-DD-YYYY).
</ParamField>

<ParamField path="order_by" type="string">
  Sort the results (e.g., by views, date, or relevance).
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Video Details**:\
  `url`, `title`, `video_url`, `video_id`, `video_length`, `date_posted`, `description`, `post_type`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lk56epmy2i5g7lzu0k/url?tab=overview).
* **Channel Details**:\
  `youtuber`, `youtuber_id`, `channel_url`, `handle_name`, `avatar_img_channel`, `subscribers`, `youtuber_md5`, `verified`.
* **Engagement Metrics**:\
  `likes`, `views`, `num_comments`, `is_sponsored`.
* **Media and Technical Information**:\
  `preview_image`, `related_videos`, `music`, `shortcode`, `viewport_frames`, `current_optimal_res`, `codecs`, `color`, `quality`, `quality_label`, `license`.
* **Transcript**:\
  `transcript`, `formatted_transcript`.

This API allows efficient retrieval of YouTube videos from a specified channel with detailed video, channel, and engagement information, supporting filtering and sorting options for enhanced analysis.

### Discover by Keywords

This API allows users to search for YouTube videos using specific keywords, with optional parameters for filtering results by date range and the number of posts to retrieve.

**Input Parameters**:

<ParamField path="keyword" type="string" required="true">
  The keyword to search for videos.
</ParamField>

<ParamField path="num_of_posts" type="number">
  The number of videos to collect.
</ParamField>

<ParamField path="start_date" type="string">
  Start date for filtering videos (MM-DD-YYYY).
</ParamField>

<ParamField path="end_date" type="string">
  End date for filtering videos (MM-DD-YYYY).
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Video Details**:\
  `url`, `title`, `video_url`, `video_id`, `video_length`, `date_posted`, `description`, `post_type`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lk56epmy2i5g7lzu0k/keyword?tab=overview).
* **Channel Details**:\
  `youtuber`, `youtuber_id`, `channel_url`, `handle_name`, `avatar_img_channel`, `subscribers`, `youtuber_md5`, `verified`.
* **Engagement Metrics**:\
  `likes`, `views`, `num_comments`, `is_sponsored`.
* **Media and Technical Information**:\
  `preview_image`, `related_videos`, `music`, `shortcode`, `viewport_frames`, `current_optimal_res`, `codecs`, `color`, `quality`, `quality_label`, `license`.
* **Transcript**:\
  `transcript`, `formatted_transcript`.

This API enables efficient discovery of YouTube videos using keywords, supporting advanced filtering by date and result count for targeted video analysis and retrieval.

### Discover by Search Filters

This API allows users to search for YouTube videos using advanced search filters such as upload date, video type, duration, and additional features, enabling more refined and targeted video discovery.

**Input Parameters**:

<ParamField path="keyword_search" type="string" required="true">
  The keyword to search for videos.
</ParamField>

<ParamField path="upload_date" type="string">
  Filter results by upload date (e.g., today, this week, this month).
</ParamField>

<ParamField path="type" type="string">
  Specify video type (e.g., video, channel, playlist).
</ParamField>

<ParamField path="duration" type="string">
  Filter by video length (e.g., short, medium, long).
</ParamField>

<ParamField path="features" type="string">
  Specify additional video features (e.g., 4K, HD, subtitles, live).
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Video Details**:\
  `url`, `title`, `video_url`, `video_id`, `video_length`, `date_posted`, `description`, `post_type`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lk56epmy2i5g7lzu0k/search_filters?tab=overview).
* **Channel Details**:\
  `youtuber`, `youtuber_id`, `channel_url`, `handle_name`, `avatar_img_channel`, `subscribers`, `youtuber_md5`, `verified`.
* **Engagement Metrics**:\
  `likes`, `views`, `num_comments`, `is_sponsored`.
* **Media and Technical Information**:\
  `preview_image`, `related_videos`, `music`, `shortcode`, `viewport_frames`, `current_optimal_res`, `codecs`, `color`, `quality`, `quality_label`, `license`.
* **Transcript**:\
  `transcript`, `formatted_transcript`.

This API supports advanced search capabilities on YouTube, allowing users to filter results by multiple parameters for precise and efficient video discovery.

### Discover by Hashtag

This API allows users to search for YouTube posts by a specific hashtag, enabling users to discover videos related to trending topics or specific themes.

**Input Parameters**:

<ParamField path="hashtag" type="string" required="true">
  The hashtag to search for (e.g., #fitness, #travel).
</ParamField>

<ParamField path="num_of_posts" type="number">
  The number of posts to collect. If omitted, there is no limit.
</ParamField>

<ParamField path="posts_to_not_include" type="array">
  An array of post IDs to exclude from the results.
</ParamField>

<ParamField path="start_date" type="string">
  Start date for filtering posts in MM-DD-YYYY format (should be earlier than end\_date).
</ParamField>

<ParamField path="end_date" type="string">
  End date for filtering posts in MM-DD-YYYY format (should be later than start\_date).
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Video Details**:\
  `url`, `title`, `video_url`, `video_id`, `video_length`, `date_posted`, `description`, `post_type`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lk56epmy2i5g7lzu0k/hashtag?tab=overview).
* **Channel Details**:\
  `youtuber`, `youtuber_id`, `channel_url`, `handle_name`, `avatar_img_channel`, `subscribers`, `youtuber_md5`, `verified`.
* **Engagement Metrics**:\
  `likes`, `views`, `num_comments`, `is_sponsored`.
* **Media and Technical Information**:\
  `preview_image`, `related_videos`, `music`, `shortcode`, `viewport_frames`, `current_optimal_res`, `codecs`, `color`, `quality`, `quality_label`, `license`.
* **Transcript**:\
  `transcript`, `formatted_transcript`.

This API enables efficient video discovery by searching posts related to a specific hashtag, with filtering options to refine the results.

## Comments API

### Collect by URL

This API allows users to retrieve detailed comment data from a specific YouTube video using the provided video URL.

**Input Parameters**:

<ParamField path="URL" type="string" required="true">
  The YouTube video URL.
</ParamField>

<ParamField path="load_replies" type="number">
  Number of times to load replies for comments.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Comment Details**:\
  `comment_id`, `comment_text`, `likes`, `replies`, `replies_value`, `replies_without_names`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lk9q0ew71spt1mxywf?tab=overview).
* **User Details**:\
  `username`, `user_channel`, `username_md5`.
* **Additional Information**:\
  `date`, `url`, `video_id`.

This API enables users to analyze YouTube video comments, including replies and user details, providing insights into engagement and audience interactions.
