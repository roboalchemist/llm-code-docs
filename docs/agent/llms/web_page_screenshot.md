# Source: https://docs.agent.ai/actions/web_page_screenshot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Page Screenshot

## Overview

Capture a visual screenshot of a specified web page for documentation or analysis.

### Use Cases

* **Archiving**: Save visual records of web pages.
* **Presentation**: Use screenshots for reports or presentations.

## Configuration Fields

### URL

* **Description**: Enter the URL of the web page to capture.
* **Example**: "[https://example.com](https://example.com)."
* **Required**: Yes

### Cache Expiration Time

* **Description**: Specify how often to refresh the screenshot.
* **Options**: 1 hour, 1 day, 1 week, 1 month
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the screenshot.
* **Example**: "web\_screenshot" or "page\_image."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
