# Source: https://docs.agent.ai/actions/web_page_content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Page Content

## Overview

Extract text content from a specified web page for analysis or use in workflows.

### Use Cases

* **Data Extraction**: Retrieve content from web pages for structured analysis.
* **Content Review**: Automate the review of online articles or blogs.

## Configuration Fields

### URL

* **Description**: Enter the URL of the web page to extract content from.
* **Example**: "[https://example.com/article](https://example.com/article)."
* **Required**: Yes

### Mode

* **Description**: Choose between scraping a single page or crawling multiple pages.
* **Options**: Single Page, Multi-page Crawl
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the extracted content.
* **Example**: "web\_content" or "page\_text."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
