# Source: https://docs.brightdata.com/api-reference/web-scraper-api/social-media-apis/facebook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Facebook API Scrapers

## Overview

The Facebook API Suite offers multiple types of APIs, each designed for specific data collection needs from Facebook. Below is an overview of how these APIs connect and interact, based on the available features:

<CardGroup cols="1">
  <Card title="Posts API" icon="images" href="/api-reference/web-scraper-api/social-media-apis/facebook#posts-api">
    This API allows users to collect multiple posts based on a single input URL (such as a Facebook page, group, or profile URL).

    <br />

    *   **Discovery functionality**:

    *   Requires the direct URL of the Facebook page, group, or profile.

    <br />

    *   **Interesting Columns**:

    *   `post_url`, `content`, `hashtags`, `likes`
  </Card>

  <Card title="Comments API" icon="comments" href="/api-reference/web-scraper-api/social-media-apis/facebook#comments-api">
    This API allows users to collect multiple comments from a post using its URL.

    <br />

    *   **Discovery functionality**:

    *   `N/A`

    <br />

    *   **Interesting Columns**:

    *   `commenter_url`, `comment_text`, `num_likes`, `num_replies`
  </Card>
</CardGroup>

<Note>There is no discovery capability across Facebook datasets since the data is locked behind login requirements.</Note>

The suite of APIs is designed to offer flexibility for targeted data collection, where users can input specific URLs to gather detailed post and comment data, either in bulk or with precise filtering options.

## Posts API

Posts API allows users to collect detailed post data from Facebook profiles, groups, and pages. The API provides comprehensive data points about posts, including post details, page/profile details, and attachments and media.

### Collect by Profile URL

This API enables users to collect detailed data from Facebook posts by providing a profile URL.

**Input Parameters**

<ParamField path="URL" type="string" required="true">
  The Facebook profile URL.
</ParamField>

<ParamField path="num_of_posts" type="number">
  The number of recent posts to collect. If omitted, there is no limit.
</ParamField>

<ParamField path="posts_to_not_include" type="array">
  Array of post IDs to exclude from the results.
</ParamField>

<ParamField path="start_date" type="string">
  Start date for filtering posts in MM-DD-YYYY format (should be earlier than end\_date).
</ParamField>

<ParamField path="end_date" type="string">
  End date for filtering posts in MM-DD-YYYY format (should be later than start\_date).
</ParamField>

**Output Structure**
Includes comprehensive data points:

* **Post Details**:
  `post_id`, `content`, `hashtags`, `date_posted`, `num_comments`, `num_likes`, and more.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lkaxegm826bjpoo9m5?tab=overview).

* **Page/Profile Details**:
  `page_name`, `page_category`, `page_followers`, `profile_handle`.

  > We provide a limited set of data points about the profile.

* **Attachments and Media**:
  `attachments` and `post_image` (link only, not the file itself), `video_view_count`.

### Collect by Group URL

This API enables users to collect detailed posts from Facebook groups by providing a group URL.

**Input Parameters**

<ParamField path="URL" type="string" required="true">
  The Facebook group URL.
</ParamField>

<ParamField path="num_of_posts" type="number">
  The number of posts to collect. If omitted, there is no limit.
</ParamField>

<ParamField path="posts_to_not_include" type="array">
  Array of post IDs to exclude from the results.
</ParamField>

<ParamField path="start_date" type="string">
  Start date for filtering posts in MM-DD-YYYY format (should be earlier than end\_date).
</ParamField>

<ParamField path="end_date" type="string">
  End date for filtering posts in MM-DD-YYYY format (should be later than start\_date).
</ParamField>

**Output Structure**
Includes comprehensive data points:

* **Post Details**:
  `post_id`, `user_url`, `user_username`, `content`, `date_posted`, `hashtags`, `num_comments`, `num_shares`, `num_likes_type`, and more.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lz11l67o2cb3r0lkj3?tab=overview).

* **Group Details**:
  `group_name`, `group_id`, `group_url`, `group_intro`, `group_category`,  and more.

* **User Details**:
  `user_is_verified`, `profile_handle` and more.

* **Attachments and External Links**:
  `Attachments` (link only, not the file itself), `original_post_url`, `other_posts_url`, `post_external_link` and more.

### Collect by Post URL

This API enables users to collect detailed data from specific Facebook posts using post URLs.

**Input Parameters**

<ParamField path="URL" type="string" required="true">
  The Facebook profile URL.
</ParamField>

**Output Structure**
Includes comprehensive data points:

* **Post Details**:
  `post_id`, `content`, `hashtags`, `date_posted`, `num_comments`, `num_likes`, and more.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lyclm1571iy3mv57zw?tab=overview).

* **Page/Profile Details**:
  `page_name`, `page_category`, `page_followers`, `profile_handle`.

  > We provide a limited set of data points about the profile.

* **Attachments and Media**:
  `attachments` and `post_image` (link only, not the file itself), `video_view_count`.

## Comments API

Comments API allows users to collect detailed comment data from Facebook posts. The API provides comprehensive data points about comments, including comment details, user details, post metadata, and attachments and media.

### Collect by Post URL

This API enables users to collect detailed comment data from Facebook posts by providing a post URL.

**Input Parameters**

<ParamField path="URL" type="string" required="true">
  The Facebook post URL.
</ParamField>

<ParamField path="num_of_comments" type="number">
  The number of comments to collect. If omitted, there is no limit.
</ParamField>

<ParamField path="comments_to_not_include" type="array">
  Array of comment IDs to exclude.
</ParamField>

<ParamField path="start_date" type="string">
  Start date for filtering comments in MM-DD-YYYY format (should be earlier than end\_date).
</ParamField>

<ParamField path="end_date" type="string">
  End date for filtering comments in MM-DD-YYYY format (should be later than start\_date).
</ParamField>

**Output Structure**
Includes comprehensive data points:

* **Comment Details**:
  `comment_id`, `comment_text`, `num_likes`, replies, `num_replies`, and more.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lkay758p1eanlolqw8?tab=overview).

* **User Details**:
  `user_name`, `user_id`, `user_url`

  > We provide a limited set of data points about the profile.

* **Post Metadata**:
  `post_id`, `post_url`.

* **Attachments and Media**:
  `attached_files` (link only, not the file itself) , `video_length`.

## Reels API

Reels API allows users to collect detailed data about Facebook reels from public profiles. The API provides comprehensive data points about reels, including post details, page/profile details, and attachments and media.

### Collect by Profile URL

This API allows users to collect detailed data about Facebook reels from public profiles by providing the profile URL.

**Input Parameters**

<ParamField path="URL" type="string" required="true">
  The Facebook profile URL.
</ParamField>

<ParamField path="num_of_posts" type="number">
  Number of reels to collect (default: up to 1600).
</ParamField>

<ParamField path="posts_to_not_include" type="array">
  Array of reel IDs to exclude.
</ParamField>

<ParamField path="start_date" type="string">
  Start of the date range for filtering reels.
</ParamField>

<ParamField path="end_date" type="string">
  End of the date range for filtering reels.
</ParamField>

**Output Structure**
Includes comprehensive data points:

* **Reel Details**:
  `post_id`, `content`, `hashtags`, `date_posted`, `num_comments`, `num_likes`, `audio` (soundtrack details), `video_view_count` and more.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lyclm3ey2q6rww027t?tab=overview).

* **Page/Profile Details**:
  `page_name`, `page_category`, `page_followers`, `profile_handle`.

  > We provide a limited set of data points about the profile.

* **Attachments and Media**:
  `external_link` (link only, not the file itself)
