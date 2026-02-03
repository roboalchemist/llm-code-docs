# Source: https://docs.agent.ai/actions/search_results.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Search Results

## Overview

Fetch search results from Google or YouTube for specific queries, providing valuable insights and content.

### Use Cases

* **Market Research**: Gather data on trends or competitors.
* **Content Discovery**: Find relevant articles or videos for your workflow.

<iframe width="560" height="315" src="https://www.youtube.com/embed/U7CpTt-Fpco?si=EhprGYprRGY5vuTm" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Configuration Fields

### Query

* **Description**: Enter search terms to find relevant results.
* **Example**: "Best AI tools" or "Marketing strategies."
* **Required**: Yes

### Search Engine

* **Description**: Choose the search engine to use for the query.
* **Options**: Google, YouTube
* **Required**: Yes

### Number of Results to Retrieve

* **Description**: Specify how many results to fetch.
* **Options**: 1, 5, 10, 25, 50, 100
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the search results.
* **Example**: "search\_results" or "google\_data."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
