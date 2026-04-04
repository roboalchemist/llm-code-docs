# Source: https://docs.brightdata.com/datasets/scraper-studio/worker-types.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Worker types

> This article explains the behavior difference between worker types, how to choose the right one for your project

Browser worker and code worker are two technical approaches for scraping, and you should choose between them based on your needs and  technical challenges you're facing with the website you're scraping.

## Browser worker vs Code worker

**Browser Workers:**

* Can simulate a user's interaction with the website via a headless browser
* Handles complex scraping tasks like filling forms, and dynamic content loading.

**Code workers:**

* Roughly equivalent to doing a curl or python `requests.get(url)`
* Work by sending HTTP requests to the target website
* Can only work in situations that don't require interacting with the website UI

## Choose the optimal worker type

Choose the appropriate worker type based on the website's technology and the navigation required to scrape your target data.

**Best practice:** Start with the Code worker type and only switch if you can't extract the data you need.

**When to use Browser worker:**

* You need to click elements to load additional data
* You need to scroll to load more content
* You need to capture network traffic from inside the browser (using `tag_script` or `tag_response`)
* You need to type text to perform searches or trigger dynamic content"

## Align your code with worker type

Some functions in our library are only available when using Browser workers and will throw an error if you try to use them with Code workers.

Below is a list of functions that can only be used with Browser workers:

* `wait_*` (any wait function)
* `scroll_*` (any scroll function)
* `tag_*` (any tag function)
* `type`
* `browser_size`
* `emulate_device`
* `freeze_page`
* `click`
* `hover`
* `right_click`
* `mouse_to`
* `press_key`
* `solve_captcha`
* `capture_graphql`
* `close_popup`
