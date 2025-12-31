# Source: https://docs.agent.ai/actions/search_bluesky_posts.md

# Search Bluesky Posts

## Overview

Search for Bluesky posts matching specific keywords or criteria to gather social media insights.

### Use Cases

* **Keyword Monitoring**: Track specific terms or hashtags on Bluesky.
* **Trend Analysis**: Identify trending topics or content on the platform.

## Configuration Fields

### Search Query

* **Description**: Enter keywords or hashtags to search for relevant Bluesky posts.
* **Example**: "#AI" or "climate change."
* **Required**: Yes

### Number of Posts to Retrieve

* **Description**: Specify how many posts to fetch.
* **Options**: 1, 5, 10, 25, 50, 100
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the search results.
* **Example**: "bluesky\_search\_results" or "matching\_posts."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
