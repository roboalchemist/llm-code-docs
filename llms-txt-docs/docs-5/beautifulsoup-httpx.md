# Source: https://docs.apify.com/sdk/python/docs/guides/beautifulsoup-httpx.md

# Using BeautifulSoup with HTTPX

Copy for LLM

In this guide, you'll learn how to use the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) library with the [HTTPX](https://www.python-httpx.org/) library in your Apify Actors.

## Introduction[](#introduction)

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) is a Python library for extracting data from HTML and XML files. It provides simple methods and Pythonic idioms for navigating, searching, and modifying a website's element tree, enabling efficient data extraction.

[HTTPX](https://www.python-httpx.org/) is a modern, high-level HTTP client library for Python. It provides a simple interface for making HTTP requests and supports both synchronous and asynchronous requests.

To create an Actor which uses those libraries, start from the [BeautifulSoup & Python](https://apify.com/templates/categories/python) Actor template. This template includes the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) and [HTTPX](https://www.python-httpx.org/) libraries preinstalled, allowing you to begin development immediately.

## Example Actor[](#example-actor)

Below is a simple Actor that recursively scrapes titles from all linked websites, up to a specified maximum depth, starting from URLs provided in the Actor input. It uses [HTTPX](https://www.python-httpx.org/) for fetching pages and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for parsing their content to extract titles and links to other pages.

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuZnJvbSB1cmxsaWIucGFyc2UgaW1wb3J0IHVybGpvaW5cXG5cXG5pbXBvcnQgaHR0cHhcXG5mcm9tIGJzNCBpbXBvcnQgQmVhdXRpZnVsU291cFxcblxcbmZyb20gYXBpZnkgaW1wb3J0IEFjdG9yLCBSZXF1ZXN0XFxuXFxuXFxuYXN5bmMgZGVmIG1haW4oKSAtPiBOb25lOlxcbiAgICAjIEVudGVyIHRoZSBjb250ZXh0IG9mIHRoZSBBY3Rvci5cXG4gICAgYXN5bmMgd2l0aCBBY3RvcjpcXG4gICAgICAgICMgUmV0cmlldmUgdGhlIEFjdG9yIGlucHV0LCBhbmQgdXNlIGRlZmF1bHQgdmFsdWVzIGlmIG5vdCBwcm92aWRlZC5cXG4gICAgICAgIGFjdG9yX2lucHV0ID0gYXdhaXQgQWN0b3IuZ2V0X2lucHV0KCkgb3Ige31cXG4gICAgICAgIHN0YXJ0X3VybHMgPSBhY3Rvcl9pbnB1dC5nZXQoJ3N0YXJ0X3VybHMnLCBbeyd1cmwnOiAnaHR0cHM6Ly9hcGlmeS5jb20nfV0pXFxuICAgICAgICBtYXhfZGVwdGggPSBhY3Rvcl9pbnB1dC5nZXQoJ21heF9kZXB0aCcsIDEpXFxuXFxuICAgICAgICAjIEV4aXQgaWYgbm8gc3RhcnQgVVJMcyBhcmUgcHJvdmlkZWQuXFxuICAgICAgICBpZiBub3Qgc3RhcnRfdXJsczpcXG4gICAgICAgICAgICBBY3Rvci5sb2cuaW5mbygnTm8gc3RhcnQgVVJMcyBzcGVjaWZpZWQgaW4gQWN0b3IgaW5wdXQsIGV4aXRpbmcuLi4nKVxcbiAgICAgICAgICAgIGF3YWl0IEFjdG9yLmV4aXQoKVxcblxcbiAgICAgICAgIyBPcGVuIHRoZSBkZWZhdWx0IHJlcXVlc3QgcXVldWUgZm9yIGhhbmRsaW5nIFVSTHMgdG8gYmUgcHJvY2Vzc2VkLlxcbiAgICAgICAgcmVxdWVzdF9xdWV1ZSA9IGF3YWl0IEFjdG9yLm9wZW5fcmVxdWVzdF9xdWV1ZSgpXFxuXFxuICAgICAgICAjIEVucXVldWUgdGhlIHN0YXJ0IFVSTHMgd2l0aCBhbiBpbml0aWFsIGNyYXdsIGRlcHRoIG9mIDAuXFxuICAgICAgICBmb3Igc3RhcnRfdXJsIGluIHN0YXJ0X3VybHM6XFxuICAgICAgICAgICAgdXJsID0gc3RhcnRfdXJsLmdldCgndXJsJylcXG4gICAgICAgICAgICBBY3Rvci5sb2cuaW5mbyhmJ0VucXVldWluZyB7dXJsfSAuLi4nKVxcbiAgICAgICAgICAgIG5ld19yZXF1ZXN0ID0gUmVxdWVzdC5mcm9tX3VybCh1cmwsIHVzZXJfZGF0YT17J2RlcHRoJzogMH0pXFxuICAgICAgICAgICAgYXdhaXQgcmVxdWVzdF9xdWV1ZS5hZGRfcmVxdWVzdChuZXdfcmVxdWVzdClcXG5cXG4gICAgICAgICMgQ3JlYXRlIGFuIEhUVFBYIGNsaWVudCB0byBmZXRjaCB0aGUgSFRNTCBjb250ZW50IG9mIHRoZSBVUkxzLlxcbiAgICAgICAgYXN5bmMgd2l0aCBodHRweC5Bc3luY0NsaWVudCgpIGFzIGNsaWVudDpcXG4gICAgICAgICAgICAjIFByb2Nlc3MgdGhlIFVSTHMgZnJvbSB0aGUgcmVxdWVzdCBxdWV1ZS5cXG4gICAgICAgICAgICB3aGlsZSByZXF1ZXN0IDo9IGF3YWl0IHJlcXVlc3RfcXVldWUuZmV0Y2hfbmV4dF9yZXF1ZXN0KCk6XFxuICAgICAgICAgICAgICAgIHVybCA9IHJlcXVlc3QudXJsXFxuXFxuICAgICAgICAgICAgICAgIGlmIG5vdCBpc2luc3RhbmNlKHJlcXVlc3QudXNlcl9kYXRhWydkZXB0aCddLCAoc3RyLCBpbnQpKTpcXG4gICAgICAgICAgICAgICAgICAgIHJhaXNlIFR5cGVFcnJvcignUmVxdWVzdC5kZXB0aCBpcyBhbiB1bmV4cGVjdGVkIHR5cGUuJylcXG5cXG4gICAgICAgICAgICAgICAgZGVwdGggPSBpbnQocmVxdWVzdC51c2VyX2RhdGFbJ2RlcHRoJ10pXFxuICAgICAgICAgICAgICAgIEFjdG9yLmxvZy5pbmZvKGYnU2NyYXBpbmcge3VybH0gKGRlcHRoPXtkZXB0aH0pIC4uLicpXFxuXFxuICAgICAgICAgICAgICAgIHRyeTpcXG4gICAgICAgICAgICAgICAgICAgICMgRmV0Y2ggdGhlIEhUVFAgcmVzcG9uc2UgZnJvbSB0aGUgc3BlY2lmaWVkIFVSTCB1c2luZyBIVFRQWC5cXG4gICAgICAgICAgICAgICAgICAgIHJlc3BvbnNlID0gYXdhaXQgY2xpZW50LmdldCh1cmwsIGZvbGxvd19yZWRpcmVjdHM9VHJ1ZSlcXG5cXG4gICAgICAgICAgICAgICAgICAgICMgUGFyc2UgdGhlIEhUTUwgY29udGVudCB1c2luZyBCZWF1dGlmdWwgU291cC5cXG4gICAgICAgICAgICAgICAgICAgIHNvdXAgPSBCZWF1dGlmdWxTb3VwKHJlc3BvbnNlLmNvbnRlbnQsICdodG1sLnBhcnNlcicpXFxuXFxuICAgICAgICAgICAgICAgICAgICAjIElmIHRoZSBjdXJyZW50IGRlcHRoIGlzIGxlc3MgdGhhbiBtYXhfZGVwdGgsIGZpbmQgbmVzdGVkIGxpbmtzXFxuICAgICAgICAgICAgICAgICAgICAjIGFuZCBlbnF1ZXVlIHRoZW0uXFxuICAgICAgICAgICAgICAgICAgICBpZiBkZXB0aCA8IG1heF9kZXB0aDpcXG4gICAgICAgICAgICAgICAgICAgICAgICBmb3IgbGluayBpbiBzb3VwLmZpbmRfYWxsKCdhJyk6XFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxpbmtfaHJlZiA9IGxpbmsuZ2V0KCdocmVmJylcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgbGlua191cmwgPSB1cmxqb2luKHVybCwgbGlua19ocmVmKVxcblxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpZiBsaW5rX3VybC5zdGFydHN3aXRoKCgnaHR0cDovLycsICdodHRwczovLycpKTpcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIEFjdG9yLmxvZy5pbmZvKGYnRW5xdWV1aW5nIHtsaW5rX3VybH0gLi4uJylcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5ld19yZXF1ZXN0ID0gUmVxdWVzdC5mcm9tX3VybChcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsaW5rX3VybCxcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB1c2VyX2RhdGE9eydkZXB0aCc6IGRlcHRoICsgMX0sXFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICApXFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhd2FpdCByZXF1ZXN0X3F1ZXVlLmFkZF9yZXF1ZXN0KG5ld19yZXF1ZXN0KVxcblxcbiAgICAgICAgICAgICAgICAgICAgIyBFeHRyYWN0IHRoZSBkZXNpcmVkIGRhdGEuXFxuICAgICAgICAgICAgICAgICAgICBkYXRhID0ge1xcbiAgICAgICAgICAgICAgICAgICAgICAgICd1cmwnOiB1cmwsXFxuICAgICAgICAgICAgICAgICAgICAgICAgJ3RpdGxlJzogc291cC50aXRsZS5zdHJpbmcgaWYgc291cC50aXRsZSBlbHNlIE5vbmUsXFxuICAgICAgICAgICAgICAgICAgICAgICAgJ2gxcyc6IFtoMS50ZXh0IGZvciBoMSBpbiBzb3VwLmZpbmRfYWxsKCdoMScpXSxcXG4gICAgICAgICAgICAgICAgICAgICAgICAnaDJzJzogW2gyLnRleHQgZm9yIGgyIGluIHNvdXAuZmluZF9hbGwoJ2gyJyldLFxcbiAgICAgICAgICAgICAgICAgICAgICAgICdoM3MnOiBbaDMudGV4dCBmb3IgaDMgaW4gc291cC5maW5kX2FsbCgnaDMnKV0sXFxuICAgICAgICAgICAgICAgICAgICB9XFxuXFxuICAgICAgICAgICAgICAgICAgICAjIFN0b3JlIHRoZSBleHRyYWN0ZWQgZGF0YSB0byB0aGUgZGVmYXVsdCBkYXRhc2V0LlxcbiAgICAgICAgICAgICAgICAgICAgYXdhaXQgQWN0b3IucHVzaF9kYXRhKGRhdGEpXFxuXFxuICAgICAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb246XFxuICAgICAgICAgICAgICAgICAgICBBY3Rvci5sb2cuZXhjZXB0aW9uKGYnQ2Fubm90IGV4dHJhY3QgZGF0YSBmcm9tIHt1cmx9LicpXFxuXFxuICAgICAgICAgICAgICAgIGZpbmFsbHk6XFxuICAgICAgICAgICAgICAgICAgICAjIE1hcmsgdGhlIHJlcXVlc3QgYXMgaGFuZGxlZCB0byBlbnN1cmUgaXQgaXMgbm90IHByb2Nlc3NlZCBhZ2Fpbi5cXG4gICAgICAgICAgICAgICAgICAgIGF3YWl0IHJlcXVlc3RfcXVldWUubWFya19yZXF1ZXN0X2FzX2hhbmRsZWQobmV3X3JlcXVlc3QpXFxuXFxuXFxuaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzpcXG4gICAgYXN5bmNpby5ydW4obWFpbigpKVxcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjEwMjQsInRpbWVvdXQiOjE4MH19.30-Z9WmlG6JbrRuux1nDy2CBsFvflstBVxSmJuSoJCA\&asrc=run_on_apify)

```
import asyncio
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup

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

        # Create an HTTPX client to fetch the HTML content of the URLs.
        async with httpx.AsyncClient() as client:
            # Process the URLs from the request queue.
            while request := await request_queue.fetch_next_request():
                url = request.url

                if not isinstance(request.user_data['depth'], (str, int)):
                    raise TypeError('Request.depth is an unexpected type.')

                depth = int(request.user_data['depth'])
                Actor.log.info(f'Scraping {url} (depth={depth}) ...')

                try:
                    # Fetch the HTTP response from the specified URL using HTTPX.
                    response = await client.get(url, follow_redirects=True)

                    # Parse the HTML content using Beautiful Soup.
                    soup = BeautifulSoup(response.content, 'html.parser')

                    # If the current depth is less than max_depth, find nested links
                    # and enqueue them.
                    if depth < max_depth:
                        for link in soup.find_all('a'):
                            link_href = link.get('href')
                            link_url = urljoin(url, link_href)

                            if link_url.startswith(('http://', 'https://')):
                                Actor.log.info(f'Enqueuing {link_url} ...')
                                new_request = Request.from_url(
                                    link_url,
                                    user_data={'depth': depth + 1},
                                )
                                await request_queue.add_request(new_request)

                    # Extract the desired data.
                    data = {
                        'url': url,
                        'title': soup.title.string if soup.title else None,
                        'h1s': [h1.text for h1 in soup.find_all('h1')],
                        'h2s': [h2.text for h2 in soup.find_all('h2')],
                        'h3s': [h3.text for h3 in soup.find_all('h3')],
                    }

                    # Store the extracted data to the default dataset.
                    await Actor.push_data(data)

                except Exception:
                    Actor.log.exception(f'Cannot extract data from {url}.')

                finally:
                    # Mark the request as handled to ensure it is not processed again.
                    await request_queue.mark_request_as_handled(new_request)


if __name__ == '__main__':
    asyncio.run(main())
```

## Conclusion[](#conclusion)

In this guide, you learned how to use the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) with the [HTTPX](https://www.python-httpx.org/) in your Apify Actors. By combining these libraries, you can efficiently extract data from HTML or XML files, making it easy to build web scraping tasks in Python. See the [Actor templates](https://apify.com/templates/categories/python) to get started with your own scraping tasks. If you have questions or need assistance, feel free to reach out on our [GitHub](https://github.com/apify/apify-sdk-python) or join our [Discord community](https://discord.com/invite/jyEM2PRvMU). Happy scraping!
