# Source: https://docs.brightdata.com/api-reference/web-scraper-api/social-media-apis/twitter.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Twitter API Scrapers

## Overview

The Twitter API Suite offers multiple types of APIs, each designed for specific data collection needs from Twitter. Below is an overview of how these APIs connect and interact, based on the available features:

<CardGroup cols={1}>
  <Card title="Profiles API" icon="user" href="/api-reference/web-scraper-api/social-media-apis/twitter#profiles-api">
    This API allows users to collect profile details based on a single input: profile URL.

    <br />

    *   **Discovery functionality**:

    *   N/A

    <br />

    *   **Interesting Columns**:

    *   `url`, `profile_name`, `is_verified`, `followers`.
  </Card>

  <Card title="Posts API" icon="images" href="/api-reference/web-scraper-api/social-media-apis/twitter#posts-api">
    This API allows users to collect multiple posts based on a single input URL.

    <br />

    *   **Discovery functionality**:

    *   Discover by profile URL.

    <br />

    *   **Interesting Columns**:

    *   `name`, `description`, `replies`, `likes`.
  </Card>
</CardGroup>

## Profiles API

### Profiles by URL

This API allows users to retrieve detailed Twitter profile information using the provided profile URL.

**Input Parameters**:

<ParamField path="URL" type="string" required="true">
  The Twitter profile URL.
</ParamField>

<ParamField path="max_number_of_posts" type="number">
  The number of posts to collect. If omitted, there is no limit.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Profile Details**:\
  `x_id`, `url`, `id`, `profile_name`, `biography`, `is_verified`, `profile_image_link`, `external_link`, `date_joined`, `location`, `birth_date`, `posts_count`, `posts`, `suggested_profiles`, `is_business_account`, `is_government_account`, `category_name`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lwxmeb2u1cniijd7t4?tab=overview).

* **Engagement Metrics**:\
  `followers`, `following`, `subscriptions`.

* **Post Details**:\
  `posts`.

This API allows users to retrieve detailed Twitter profile information, including user engagement metrics, post details, and more, offering insights into user activity and profile data.

## Posts API

### Collect by URL

This API allows users to retrieve detailed post information from a specific Twitter post using the provided post URL.

**Input Parameters**:

<ParamField path="URL" type="string" required="true">
  The Twitter post URL.
</ParamField>

<Note>API limitations: Up to 1000 posts per input.</Note>

**Output Structure**:\
Includes comprehensive data points:

* **Post Details**:\
  `id`, `user_posted`, `name`, `description`, `date_posted`, `url`, `tagged_users`, `replies`, `reposts`, `likes`, `views`, `external_url`, `hashtags`, `quotes`, `bookmarks`, `external_image_urls`, `videos`, `quoted_post`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lwxkxvnf1cynvib9co?tab=overview).

* **User Profile Details**:\
  `followers`, `biography`, `posts_count`, `profile_image_link`, `following`, `is_verified`.

* **Parent Post Details**:\
  `parent_post_details`.

This API allows users to retrieve detailed information about a specific Twitter post, including user details, engagement metrics, and media content, offering insights into post interactions and user activity.

### Discover by Profile URL

This API allows users to discover and retrieve posts from a specific Twitter profile within a specified date range.

**Input Parameters**:

<ParamField path="URL" type="string" required="true">
  The URL of the Twitter profile.
</ParamField>

<ParamField path="start_date" type="string">
  Start date for filtering posts in MM-DD-YYYY format.
</ParamField>

<ParamField path="end_date" type="string">
  End date for filtering posts in MM-DD-YYYY format.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Post Details**:\
  `id`, `user_posted`, `name`, `description`, `date_posted`, `url`, `tagged_users`, `replies`, `reposts`, `likes`, `views`, `external_url`, `hashtags`, `quotes`, `bookmarks`, `external_image_urls`, `videos`, `quoted_post`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lwxkxvnf1cynvib9co/profile_url?tab=overview).

* **User Profile Details**:\
  `followers`, `biography`, `posts_count`, `profile_image_link`, `following`, `is_verified`.

* **Parent Post Details**:\
  `parent_post_details`.

This API allows users to retrieve posts from a specific Twitter profile within a defined time frame, offering detailed insights into post interactions, user data, and media content.
