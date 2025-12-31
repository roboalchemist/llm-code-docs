# Source: https://docs.agent.ai/actions/get_linkedin_activity.md

# Get LinkedIn Activity

## Overview

Retrieve recent LinkedIn posts from specified profiles to analyze professional activity and engagement.

### Use Cases

* **Recruitment**: Monitor LinkedIn activity for potential candidates.
* **Industry Trends**: Analyze posts for emerging topics.

## Configuration Fields

### LinkedIn Profile URLs

* **Description**: Enter one or more LinkedIn profile URLs, each on a new line.
* **Example**: "[https://linkedin.com/in/janedoe](https://linkedin.com/in/janedoe)."
* **Required**: Yes

### Number of Posts to Retrieve

* **Description**: Specify how many recent posts to fetch from each profile.
* **Options**: 1, 5, 10, 25, 50, 100
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store LinkedIn activity data.
* **Example**: "linkedin\_activity" or "recent\_posts."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
