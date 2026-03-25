# Source: https://docs.brightdata.com/api-reference/web-scraper-api/social-media-apis/reddit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reddit API Scrapers

## Overview

The Reddit API Suite offers multiple types of APIs, each designed for specific data collection needs from Reddit. Below is an overview of how these APIs connect and interact, based on the available features:

<CardGroup cols={1}>
  <Card title="Posts API" icon="images" href="/api-reference/web-scraper-api/social-media-apis/reddit#posts-api">
    This API allows users to collect multiple posts based on a single input URL.

    <br />

    *   **Discovery functionality**:

    *   Discover by subreddit URL.

    *   Discover by Keywords.

    <br />

    *   **Interesting Columns**:

    *   `url`, `title`, `num_comments`, `description`
  </Card>

  <Card title="Comments API" icon="comments" href="/api-reference/web-scraper-api/social-media-apis/reddit#comments-api">
    This API allows users to collect multiple comments from a post using its URL.

    <br />

    *   **Discovery functionality**:

    *   N/A

    <br />

    *   **Interesting Columns**:

    *   `url`, `comment`, `community_name`, `num_replies`
  </Card>
</CardGroup>

## Posts API

### Collect by URL

This API allows users to retrieve detailed post data from a specific Reddit post using the provided URL.

**Input Parameters**

<ParamField path="URL" type="string" required="true">
  The URL of the Reddit post to be retrieved.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Post Details**:\
  `post_id`, `url`, `title`, `description`, `num_comments`, `date_posted`, `tag`, `related_posts`, `comments`, `photos`, `videos`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lvz8ah06191smkebj4?tab=overview).

* **User Details**:\
  `user_posted`.

* **Community Details**:\
  `community_name`, `community_url`, `community_description`, `community_members_num`, `community_rank`.

* **Engagement Metrics**:\
  `num_upvotes`.

This API enables efficient retrieval of Reddit post information, including user engagement metrics, community details, and multimedia content, supporting advanced analysis and content tracking.

### Discover by Keywords

This API allows users to discover Reddit posts by specific keywords, with options to filter by date and the number of posts to retrieve.

**Input Parameters**

<ParamField path="keyword" type="string" required="true">
  The search term to find relevant posts.
</ParamField>

<ParamField path="date" type="string" required="true">
  The date to filter posts by, ensuring results fall within the specified timeframe.
</ParamField>

<ParamField path="num_of_posts" type="number">
  The number of posts to collect. If not provided, all matching posts are retrieved.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Post Details**:\
  `post_id`, `url`, `user_posted`, `title`, `description`, `num_comments`, `date_posted`, `tag`, `related_posts`, `comments`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lvz8ah06191smkebj4/keyword?tab=overview).

* **Community Details**:\
  `community_name`, `community_url`, `community_description`, `community_members_num`, `community_rank`.

* **Media Details**:\
  `photos`, `videos`.

This API enables users to efficiently discover and analyze Reddit posts related to specific keywords, providing valuable insights into community discussions, post popularity, and associated media content.

### Discover by subreddit URL

This API allows users to retrieve posts from a specific subreddit using the subreddit URL, with an option to sort results based on specific criteria.

**Input Parameters**

<ParamField path="URL" type="string" required="true">
  The URL of the subreddit to collect posts from.
</ParamField>

<ParamField path="sort_by" type="string">
  Determines the sorting method for the posts (e.g., `new`, `top`, `hot`).
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Post Details**:\
  `post_id`, `url`, `user_posted`, `title`, `description`, `num_comments`, `date_posted`, `tag`, `related_posts`, `comments`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lvz8ah06191smkebj4/subreddit_url).

* **Community Details**:\
  `community_name`, `community_url`, `community_description`, `community_members_num`, `community_rank`.

* **Media Details**:\
  `photos`, `videos`.

This API provides a streamlined way to explore and analyze posts within a subreddit, offering insights into post content, community dynamics, and associated media files. Perfect for monitoring subreddit activity or extracting post-level data for further analysis.

## Comments API

### Collect by URL

This API allows users to collect detailed comment data from a specific Reddit post or comment URL, with the option to filter comments based on the number of days since they were published.

**Input Parameters**

<ParamField path="URL" type="string" required="true">
  The URL of the Reddit post or comment to retrieve comments from.
</ParamField>

<ParamField path="days_back" type="number">
  Collect all comments published no later than the specified number of days.
</ParamField>

**Output Structure**:\
Includes comprehensive data points:

* **Comment Details**:\
  `comment_id`, `user_posted`, `comment`, `date_posted`, `replies`, `num_upvotes`, `num_replies`.

  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_lvzdpsdlw09j6t702?tab=overview).

* **Post Details**:\
  `post_url`, `post_id`, `post_language`, `post_state`, `post_type`, `images`.

* **Community Details**:\
  `community_name`, `community_url`, `community_description`, `community_members_num`, `community_rank`.

* **Post Attributes**:\
  `is_moderator`, `is_pinned`, `has_bot_in_username`, `is_locked`, `is_admin_post`, `is_archived_post`, `is_moderator_post`, `is_quarantined_post`, `is_not_safe_for_work_post`, `is_eligible_for_content_blocking_post`, `is_promoted_post`.

This API provides comprehensive insights into Reddit comments and their associated posts, enabling users to analyze engagement, user activity, and content trends effectively.
