# Source: https://docs.agent.ai/actions/google_news_data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Google News Data

## Overview

Fetch news articles based on queries and date ranges to stay updated on relevant topics or trends.

### Use Cases

* **Market Analysis**: Track news articles for industry trends.
* **Brand Monitoring**: Stay updated on mentions of your company or competitors.

## Configuration Fields

### Query

* **Description**: Enter search terms to find news articles.
* **Example**: "AI advancements" or "global market trends."
* **Required**: Yes

### Since

* **Description**: Select the timeframe for news articles.
* **Options**: Last 24 hours, 7 days, 30 days, 90 days
* **Required**: Yes

### Location

* **Description**: Specify a location to filter news results (optional).
* **Example**: "New York" or "London."
* **Required**: No

### Output Variable Name

* **Description**: Assign a variable name to store the news data.
* **Example**: "news\_data" or "articles."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
