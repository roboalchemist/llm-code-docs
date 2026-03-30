# Source: https://exa.ai/docs/changelog/livecrawl-preferred-option.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.


## # New Livecrawl Option: Preferred

> Introducing the 'preferred' livecrawl option that tries to fetch fresh content but gracefully falls back to cached results when crawling fails, providing the best of both worlds.

*__

__Date: 7 June 2025**

We've added a new `livecrawl` option called `"preferred"` that provides a more resilient approach to content fetching. This option attempts to crawl fresh content but gracefully falls back to cached results when live crawling fails.

<Info>
  The `preferred` option is now available in both `/contents` and `/search_and_contents` endpoints.
</Info>

## What's New

The new `livecrawl: "preferred"` option provides intelligent fallback behavior:

* __First__: Attempts to crawl fresh content from the live webpage
* __If crawling succeeds__: Returns the fresh, up-to-date content
* __If crawling fails but cached content exists__: Returns cached content instead of failing
* __If crawling fails and no cached content exists__: Returns the crawl error

## How It Differs from "Always"

The key difference between `"preferred"` and `"always"`:

| Option        | Crawl Fails + Cache Available | Crawl Fails + No Cache |
| ------------- | ----------------------------- | ---------------------- |
| `"preferred"` | Returns cached content        | Returns crawl error    |
| `"always"`    | Returns crawl error           | Returns crawl error    |

This makes `"preferred"` more resilient for production applications where you want fresh content when possible, but don't want requests to fail when websites are temporarily unavailable.

If content freshness is critical and you want nothing else, then using `"always"` might be better.

## When to Use "Preferred"

The `"preferred"` option is ideal when:

* You want the freshest content available but need reliability
* Building production applications that can't afford to fail on crawl errors
* Content freshness is important but not critical enough to fail the request
* You're crawling websites that might be occasionally unavailable

## Complete Livecrawl Options Overview

Here are all four livecrawl options and their behaviors:

| Option        | Crawl Behavior   | Cache Fallback              | Best For                                            |
| ------------- | ---------------- | --------------------------- | --------------------------------------------------- |
| `"always"`    | Always crawls    | Never falls back            | Critical real-time data, willing to accept failures |
| `"preferred"` | Always crawls    | Falls back on crawl failure | Fresh content with reliability                      |
| `"fallback"`  | Only if no cache | Uses cache first            | Balanced speed and freshness                        |
| `"never"`     | Never crawls     | Always uses cache           | Maximum speed                                       |

## Migration Guide

If you're currently using `livecrawl: "always"` but experiencing reliability issues:

```python  theme={null}
# Before - fails when crawling fails
result = exa.get_contents(urls, livecrawl="always")

# After - more resilient with cache fallback
result = exa.get_contents(urls, livecrawl="preferred")
```text

This change maintains your preference for fresh content while improving reliability.
