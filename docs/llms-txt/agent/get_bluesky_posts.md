# Source: https://docs.agent.ai/actions/get_bluesky_posts.md

# Get Bluesky Posts

## Overview

Fetch recent posts from a specified Bluesky user handle, making it easy to monitor activity on the platform.

### Use Cases

* **Social Media Analysis**: Track a user's recent posts for sentiment analysis or topic extraction.
* **Competitor Insights**: Observe recent activity from competitors or key influencers.

## Configuration Fields

### User Handle

* **Description**: Enter the Bluesky handle to fetch posts from.
* **Example**: "jay.bsky.social."
* **Required**: Yes

### Number of Posts to Retrieve

* **Description**: Specify how many recent posts to fetch.
* **Options**: 1, 5, 10, 25, 50, 100
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the retrieved posts.
* **Example**: "recent\_posts" or "bsky\_feed."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
