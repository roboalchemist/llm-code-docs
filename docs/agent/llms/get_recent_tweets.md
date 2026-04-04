# Source: https://docs.agent.ai/actions/get_recent_tweets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Recent Tweets

## Overview

Fetch recent tweets from a specified Twitter handle, enabling social media tracking and analysis.

### Use Cases

* **Real-time Monitoring**: Track the latest activity from a key influencer or competitor.
* **Sentiment Analysis**: Analyze recent tweets for tone and sentiment.

## Configuration Fields

### Twitter Handle

* **Description**: Enter the Twitter handle to fetch tweets from (without the @ symbol).
* **Example**: "elonmusk."
* **Required**: Yes

### Number of Tweets to Retrieve

* **Description**: Specify how many recent tweets to fetch.
* **Options**: 1, 5, 10, 25, 50, 100
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the retrieved tweets.
* **Example**: "recent\_tweets" or "tweet\_feed."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
