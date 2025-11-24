# Source: https://docs.apify.com/sdk/python/docs/guides/parsel-impit.md

# Using Parsel with Impit

Copy for LLM

In this guide, you'll learn how to combine the [Parsel](https://github.com/scrapy/parsel) and [Impit](https://github.com/apify/impit) libraries when building Apify Actors.

## Introduction[](#introduction)

[Parsel](https://github.com/scrapy/parsel) is a Python library for extracting data from HTML and XML documents using CSS selectors and [XPath](https://en.wikipedia.org/wiki/XPath) expressions. It offers an intuitive API for navigating and extracting structured data, making it a popular choice for web scraping. Compared to [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), it also delivers better performance.

[Impit](https://github.com/apify/impit) is Apify's high-performance HTTP client for Python. It supports both synchronous and asynchronous workflows and is built for large-scale web scraping, where making thousands of requests efficiently is essential. With built-in browser impersonation and anti-blocking features, it simplifies handling modern websites.

## Example Actor[](#example-actor)

The following example shows a simple Actor that recursively scrapes titles from linked pages, up to a user-defined maximum depth. It uses [Impit](https://github.com/apify/impit) to fetch pages and [Parsel](https://github.com/scrapy/parsel) to extract titles and discover new links.

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuZnJvbSB1cmxsaWIucGFyc2UgaW1wb3J0IHVybGpvaW5cXG5cXG5pbXBvcnQgaW1waXRcXG5pbXBvcnQgcGFyc2VsXFxuXFxuZnJvbSBhcGlmeSBpbXBvcnQgQWN0b3IsIFJlcXVlc3RcXG5cXG5cXG5hc3luYyBkZWYgbWFpbigpIC0-IE5vbmU6XFxuICAgICMgRW50ZXIgdGhlIGNvbnRleHQgb2YgdGhlIEFjdG9yLlxcbiAgICBhc3luYyB3aXRoIEFjdG9yOlxcbiAgICAgICAgIyBSZXRyaWV2ZSB0aGUgQWN0b3IgaW5wdXQsIGFuZCB1c2UgZGVmYXVsdCB2YWx1ZXMgaWYgbm90IHByb3ZpZGVkLlxcbiAgICAgICAgYWN0b3JfaW5wdXQgPSBhd2FpdCBBY3Rvci5nZXRfaW5wdXQoKSBvciB7fVxcbiAgICAgICAgc3RhcnRfdXJscyA9IGFjdG9yX2lucHV0LmdldCgnc3RhcnRfdXJscycsIFt7J3VybCc6ICdodHRwczovL2FwaWZ5LmNvbSd9XSlcXG4gICAgICAgIG1heF9kZXB0aCA9IGFjdG9yX2lucHV0LmdldCgnbWF4X2RlcHRoJywgMSlcXG5cXG4gICAgICAgICMgRXhpdCBpZiBubyBzdGFydCBVUkxzIGFyZSBwcm92aWRlZC5cXG4gICAgICAgIGlmIG5vdCBzdGFydF91cmxzOlxcbiAgICAgICAgICAgIEFjdG9yLmxvZy5pbmZvKCdObyBzdGFydCBVUkxzIHNwZWNpZmllZCBpbiBBY3RvciBpbnB1dCwgZXhpdGluZy4uLicpXFxuICAgICAgICAgICAgYXdhaXQgQWN0b3IuZXhpdCgpXFxuXFxuICAgICAgICAjIE9wZW4gdGhlIGRlZmF1bHQgcmVxdWVzdCBxdWV1ZSBmb3IgaGFuZGxpbmcgVVJMcyB0byBiZSBwcm9jZXNzZWQuXFxuICAgICAgICByZXF1ZXN0X3F1ZXVlID0gYXdhaXQgQWN0b3Iub3Blbl9yZXF1ZXN0X3F1ZXVlKClcXG5cXG4gICAgICAgICMgRW5xdWV1ZSB0aGUgc3RhcnQgVVJMcyB3aXRoIGFuIGluaXRpYWwgY3Jhd2wgZGVwdGggb2YgMC5cXG4gICAgICAgIGZvciBzdGFydF91cmwgaW4gc3RhcnRfdXJsczpcXG4gICAgICAgICAgICB1cmwgPSBzdGFydF91cmwuZ2V0KCd1cmwnKVxcbiAgICAgICAgICAgIEFjdG9yLmxvZy5pbmZvKGYnRW5xdWV1aW5nIHt1cmx9IC4uLicpXFxuICAgICAgICAgICAgbmV3X3JlcXVlc3QgPSBSZXF1ZXN0LmZyb21fdXJsKHVybCwgdXNlcl9kYXRhPXsnZGVwdGgnOiAwfSlcXG4gICAgICAgICAgICBhd2FpdCByZXF1ZXN0X3F1ZXVlLmFkZF9yZXF1ZXN0KG5ld19yZXF1ZXN0KVxcblxcbiAgICAgICAgIyBDcmVhdGUgYW4gSW1waXQgY2xpZW50IHRvIGZldGNoIHRoZSBIVE1MIGNvbnRlbnQgb2YgdGhlIFVSTHMuXFxuICAgICAgICBhc3luYyB3aXRoIGltcGl0LkFzeW5jQ2xpZW50KCkgYXMgY2xpZW50OlxcbiAgICAgICAgICAgICMgUHJvY2VzcyB0aGUgVVJMcyBmcm9tIHRoZSByZXF1ZXN0IHF1ZXVlLlxcbiAgICAgICAgICAgIHdoaWxlIHJlcXVlc3QgOj0gYXdhaXQgcmVxdWVzdF9xdWV1ZS5mZXRjaF9uZXh0X3JlcXVlc3QoKTpcXG4gICAgICAgICAgICAgICAgdXJsID0gcmVxdWVzdC51cmxcXG5cXG4gICAgICAgICAgICAgICAgaWYgbm90IGlzaW5zdGFuY2UocmVxdWVzdC51c2VyX2RhdGFbJ2RlcHRoJ10sIChzdHIsIGludCkpOlxcbiAgICAgICAgICAgICAgICAgICAgcmFpc2UgVHlwZUVycm9yKCdSZXF1ZXN0LmRlcHRoIGlzIGFuIHVuZXhwZWN0ZWQgdHlwZS4nKVxcblxcbiAgICAgICAgICAgICAgICBkZXB0aCA9IGludChyZXF1ZXN0LnVzZXJfZGF0YVsnZGVwdGgnXSlcXG4gICAgICAgICAgICAgICAgQWN0b3IubG9nLmluZm8oZidTY3JhcGluZyB7dXJsfSAoZGVwdGg9e2RlcHRofSkgLi4uJylcXG5cXG4gICAgICAgICAgICAgICAgdHJ5OlxcbiAgICAgICAgICAgICAgICAgICAgIyBGZXRjaCB0aGUgSFRUUCByZXNwb25zZSBmcm9tIHRoZSBzcGVjaWZpZWQgVVJMIHVzaW5nIEltcGl0LlxcbiAgICAgICAgICAgICAgICAgICAgcmVzcG9uc2UgPSBhd2FpdCBjbGllbnQuZ2V0KHVybClcXG5cXG4gICAgICAgICAgICAgICAgICAgICMgUGFyc2UgdGhlIEhUTUwgY29udGVudCB1c2luZyBQYXJzZWwgU2VsZWN0b3IuXFxuICAgICAgICAgICAgICAgICAgICBzZWxlY3RvciA9IHBhcnNlbC5TZWxlY3Rvcih0ZXh0PXJlc3BvbnNlLnRleHQpXFxuXFxuICAgICAgICAgICAgICAgICAgICAjIElmIHRoZSBjdXJyZW50IGRlcHRoIGlzIGxlc3MgdGhhbiBtYXhfZGVwdGgsIGZpbmQgbmVzdGVkIGxpbmtzXFxuICAgICAgICAgICAgICAgICAgICAjIGFuZCBlbnF1ZXVlIHRoZW0uXFxuICAgICAgICAgICAgICAgICAgICBpZiBkZXB0aCA8IG1heF9kZXB0aDpcXG4gICAgICAgICAgICAgICAgICAgICAgICAjIEV4dHJhY3QgYWxsIGxpbmtzIHVzaW5nIENTUyBzZWxlY3RvclxcbiAgICAgICAgICAgICAgICAgICAgICAgIGxpbmtzID0gc2VsZWN0b3IuY3NzKCdhOjphdHRyKGhyZWYpJykuZ2V0YWxsKClcXG4gICAgICAgICAgICAgICAgICAgICAgICBmb3IgbGlua19ocmVmIGluIGxpbmtzOlxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBsaW5rX3VybCA9IHVybGpvaW4odXJsLCBsaW5rX2hyZWYpXFxuXFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlmIGxpbmtfdXJsLnN0YXJ0c3dpdGgoKCdodHRwOi8vJywgJ2h0dHBzOi8vJykpOlxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgQWN0b3IubG9nLmluZm8oZidFbnF1ZXVpbmcge2xpbmtfdXJsfSAuLi4nKVxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbmV3X3JlcXVlc3QgPSBSZXF1ZXN0LmZyb21fdXJsKFxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxpbmtfdXJsLFxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHVzZXJfZGF0YT17J2RlcHRoJzogZGVwdGggKyAxfSxcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIClcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGF3YWl0IHJlcXVlc3RfcXVldWUuYWRkX3JlcXVlc3QobmV3X3JlcXVlc3QpXFxuXFxuICAgICAgICAgICAgICAgICAgICAjIEV4dHJhY3QgdGhlIGRlc2lyZWQgZGF0YSB1c2luZyBQYXJzZWwgc2VsZWN0b3JzLlxcbiAgICAgICAgICAgICAgICAgICAgdGl0bGUgPSBzZWxlY3Rvci5jc3MoJ3RpdGxlOjp0ZXh0JykuZ2V0KClcXG4gICAgICAgICAgICAgICAgICAgIGgxcyA9IHNlbGVjdG9yLmNzcygnaDE6OnRleHQnKS5nZXRhbGwoKVxcbiAgICAgICAgICAgICAgICAgICAgaDJzID0gc2VsZWN0b3IuY3NzKCdoMjo6dGV4dCcpLmdldGFsbCgpXFxuICAgICAgICAgICAgICAgICAgICBoM3MgPSBzZWxlY3Rvci5jc3MoJ2gzOjp0ZXh0JykuZ2V0YWxsKClcXG5cXG4gICAgICAgICAgICAgICAgICAgIGRhdGEgPSB7XFxuICAgICAgICAgICAgICAgICAgICAgICAgJ3VybCc6IHVybCxcXG4gICAgICAgICAgICAgICAgICAgICAgICAndGl0bGUnOiB0aXRsZSxcXG4gICAgICAgICAgICAgICAgICAgICAgICAnaDFzJzogaDFzLFxcbiAgICAgICAgICAgICAgICAgICAgICAgICdoMnMnOiBoMnMsXFxuICAgICAgICAgICAgICAgICAgICAgICAgJ2gzcyc6IGgzcyxcXG4gICAgICAgICAgICAgICAgICAgIH1cXG5cXG4gICAgICAgICAgICAgICAgICAgICMgU3RvcmUgdGhlIGV4dHJhY3RlZCBkYXRhIHRvIHRoZSBkZWZhdWx0IGRhdGFzZXQuXFxuICAgICAgICAgICAgICAgICAgICBhd2FpdCBBY3Rvci5wdXNoX2RhdGEoZGF0YSlcXG5cXG4gICAgICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjpcXG4gICAgICAgICAgICAgICAgICAgIEFjdG9yLmxvZy5leGNlcHRpb24oZidDYW5ub3QgZXh0cmFjdCBkYXRhIGZyb20ge3VybH0uJylcXG5cXG4gICAgICAgICAgICAgICAgZmluYWxseTpcXG4gICAgICAgICAgICAgICAgICAgICMgTWFyayB0aGUgcmVxdWVzdCBhcyBoYW5kbGVkIHRvIGVuc3VyZSBpdCBpcyBub3QgcHJvY2Vzc2VkIGFnYWluLlxcbiAgICAgICAgICAgICAgICAgICAgYXdhaXQgcmVxdWVzdF9xdWV1ZS5tYXJrX3JlcXVlc3RfYXNfaGFuZGxlZChyZXF1ZXN0KVxcblxcblxcbmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6XFxuICAgIGFzeW5jaW8ucnVuKG1haW4oKSlcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5IjoxMDI0LCJ0aW1lb3V0IjoxODB9fQ.3r0f1jubg5CgFH9S61z3twbDdyblGtwK8nI6SDEeiUU\&asrc=run_on_apify)

```
import asyncio
from urllib.parse import urljoin

import impit
import parsel

from apify import Actor, Request


async def main() -> None:
    # Enter the context of the Actor.
    async with Actor:
        # Retrieve the Actor input, and use default values if not provided.
        actor_input = await Actor.get_input() or {}
        start_urls = actor_input.get('start_urls', [{'url': 'https://apify.com'}])
        max_depth = actor_input.get('max_depth', 1)

        # Exit if no start URLs are provided.
        if not start_urls:
            Actor.log.info('No start URLs specified in Actor input, exiting...')
            await Actor.exit()

        # Open the default request queue for handling URLs to be processed.
        request_queue = await Actor.open_request_queue()

        # Enqueue the start URLs with an initial crawl depth of 0.
        for start_url in start_urls:
            url = start_url.get('url')
            Actor.log.info(f'Enqueuing {url} ...')
            new_request = Request.from_url(url, user_data={'depth': 0})
            await request_queue.add_request(new_request)

        # Create an Impit client to fetch the HTML content of the URLs.
        async with impit.AsyncClient() as client:
            # Process the URLs from the request queue.
            while request := await request_queue.fetch_next_request():
                url = request.url

                if not isinstance(request.user_data['depth'], (str, int)):
                    raise TypeError('Request.depth is an unexpected type.')

                depth = int(request.user_data['depth'])
                Actor.log.info(f'Scraping {url} (depth={depth}) ...')

                try:
                    # Fetch the HTTP response from the specified URL using Impit.
                    response = await client.get(url)

                    # Parse the HTML content using Parsel Selector.
                    selector = parsel.Selector(text=response.text)

                    # If the current depth is less than max_depth, find nested links
                    # and enqueue them.
                    if depth < max_depth:
                        # Extract all links using CSS selector
                        links = selector.css('a::attr(href)').getall()
                        for link_href in links:
                            link_url = urljoin(url, link_href)

                            if link_url.startswith(('http://', 'https://')):
                                Actor.log.info(f'Enqueuing {link_url} ...')
                                new_request = Request.from_url(
                                    link_url,
                                    user_data={'depth': depth + 1},
                                )
                                await request_queue.add_request(new_request)

                    # Extract the desired data using Parsel selectors.
                    title = selector.css('title::text').get()
                    h1s = selector.css('h1::text').getall()
                    h2s = selector.css('h2::text').getall()
                    h3s = selector.css('h3::text').getall()

                    data = {
                        'url': url,
                        'title': title,
                        'h1s': h1s,
                        'h2s': h2s,
                        'h3s': h3s,
                    }

                    # Store the extracted data to the default dataset.
                    await Actor.push_data(data)

                except Exception:
                    Actor.log.exception(f'Cannot extract data from {url}.')

                finally:
                    # Mark the request as handled to ensure it is not processed again.
                    await request_queue.mark_request_as_handled(request)


if __name__ == '__main__':
    asyncio.run(main())
```

## Conclusion[](#conclusion)

In this guide, you learned how to use [Parsel](https://github.com/scrapy/parsel) with [Impit](https://github.com/apify/impit) in your Apify Actors. By combining these libraries, you get a powerful and efficient solution for web scraping: [Parsel](https://github.com/scrapy/parsel) provides excellent CSS selector and XPath support for data extraction, while [Impit](https://github.com/apify/impit) offers a fast and simple HTTP client built by Apify. This combination makes it easy to build scalable web scraping tasks in Python. See the [Actor templates](https://apify.com/templates/categories/python) to get started with your own scraping tasks. If you have questions or need assistance, feel free to reach out on our [GitHub](https://github.com/apify/apify-sdk-python) or join our [Discord community](https://discord.com/invite/jyEM2PRvMU). Happy scraping!
