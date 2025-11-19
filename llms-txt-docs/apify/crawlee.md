# Source: https://docs.apify.com/sdk/python/docs/guides/crawlee.md

# Using Crawlee

Copy for LLM

In this guide you'll learn how to use the [Crawlee](https://crawlee.dev/python) library in your Apify Actors.

## Introduction[](#introduction)

[Crawlee](https://crawlee.dev/python) is a Python library for web scraping and browser automation that provides a robust and flexible framework for building web scraping tasks. It seamlessly integrates with the Apify platform and supports a variety of scraping techniques, from static HTML parsing to dynamic JavaScript-rendered content handling. Crawlee offers a range of crawlers, including HTTP-based crawlers like [`HttpCrawler`](https://crawlee.dev/python/api/class/HttpCrawler), [`BeautifulSoupCrawler`](https://crawlee.dev/python/api/class/BeautifulSoupCrawler) and [`ParselCrawler`](https://crawlee.dev/python/api/class/ParselCrawler), and browser-based crawlers like [`PlaywrightCrawler`](https://crawlee.dev/python/api/class/PlaywrightCrawler), to suit different scraping needs.

In this guide, you'll learn how to use Crawlee with [`BeautifulSoupCrawler`](https://crawlee.dev/python/api/class/BeautifulSoupCrawler), [`ParselCrawler`](https://crawlee.dev/python/api/class/ParselCrawler), and [`PlaywrightCrawler`](https://crawlee.dev/python/api/class/PlaywrightCrawler) to build Apify Actors for web scraping.

## Actor with BeautifulSoupCrawler[](#actor-with-beautifulsoupcrawler)

The [`BeautifulSoupCrawler`](https://crawlee.dev/python/api/class/BeautifulSoupCrawler) is ideal for extracting data from static HTML pages. It uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for parsing and [`ImpitHttpClient`](https://crawlee.dev/python/api/class/ImpitHttpClient) for HTTP communication, ensuring efficient and lightweight scraping. If you do not need to execute JavaScript on the page, [`BeautifulSoupCrawler`](https://crawlee.dev/python/api/class/BeautifulSoupCrawler) is a great choice for your scraping tasks. Below is an example of how to use it\` in an Apify Actor.

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuXFxuZnJvbSBjcmF3bGVlLmNyYXdsZXJzIGltcG9ydCBCZWF1dGlmdWxTb3VwQ3Jhd2xlciwgQmVhdXRpZnVsU291cENyYXdsaW5nQ29udGV4dFxcblxcbmZyb20gYXBpZnkgaW1wb3J0IEFjdG9yXFxuXFxuIyBDcmVhdGUgYSBjcmF3bGVyLlxcbmNyYXdsZXIgPSBCZWF1dGlmdWxTb3VwQ3Jhd2xlcihcXG4gICAgIyBMaW1pdCB0aGUgY3Jhd2wgdG8gbWF4IHJlcXVlc3RzLiBSZW1vdmUgb3IgaW5jcmVhc2UgaXQgZm9yIGNyYXdsaW5nIGFsbCBsaW5rcy5cXG4gICAgbWF4X3JlcXVlc3RzX3Blcl9jcmF3bD01MCxcXG4pXFxuXFxuXFxuIyBEZWZpbmUgYSByZXF1ZXN0IGhhbmRsZXIsIHdoaWNoIHdpbGwgYmUgY2FsbGVkIGZvciBldmVyeSByZXF1ZXN0LlxcbkBjcmF3bGVyLnJvdXRlci5kZWZhdWx0X2hhbmRsZXJcXG5hc3luYyBkZWYgcmVxdWVzdF9oYW5kbGVyKGNvbnRleHQ6IEJlYXV0aWZ1bFNvdXBDcmF3bGluZ0NvbnRleHQpIC0-IE5vbmU6XFxuICAgIEFjdG9yLmxvZy5pbmZvKGYnU2NyYXBpbmcge2NvbnRleHQucmVxdWVzdC51cmx9Li4uJylcXG5cXG4gICAgIyBFeHRyYWN0IHRoZSBkZXNpcmVkIGRhdGEuXFxuICAgIGRhdGEgPSB7XFxuICAgICAgICAndXJsJzogY29udGV4dC5yZXF1ZXN0LnVybCxcXG4gICAgICAgICd0aXRsZSc6IGNvbnRleHQuc291cC50aXRsZS5zdHJpbmcgaWYgY29udGV4dC5zb3VwLnRpdGxlIGVsc2UgTm9uZSxcXG4gICAgICAgICdoMXMnOiBbaDEudGV4dCBmb3IgaDEgaW4gY29udGV4dC5zb3VwLmZpbmRfYWxsKCdoMScpXSxcXG4gICAgICAgICdoMnMnOiBbaDIudGV4dCBmb3IgaDIgaW4gY29udGV4dC5zb3VwLmZpbmRfYWxsKCdoMicpXSxcXG4gICAgICAgICdoM3MnOiBbaDMudGV4dCBmb3IgaDMgaW4gY29udGV4dC5zb3VwLmZpbmRfYWxsKCdoMycpXSxcXG4gICAgfVxcblxcbiAgICAjIFN0b3JlIHRoZSBleHRyYWN0ZWQgZGF0YSB0byB0aGUgZGVmYXVsdCBkYXRhc2V0LlxcbiAgICBhd2FpdCBjb250ZXh0LnB1c2hfZGF0YShkYXRhKVxcblxcbiAgICAjIEVucXVldWUgYWRkaXRpb25hbCBsaW5rcyBmb3VuZCBvbiB0aGUgY3VycmVudCBwYWdlLlxcbiAgICBhd2FpdCBjb250ZXh0LmVucXVldWVfbGlua3Moc3RyYXRlZ3k9J3NhbWUtZG9tYWluJylcXG5cXG5cXG5hc3luYyBkZWYgbWFpbigpIC0-IE5vbmU6XFxuICAgICMgRW50ZXIgdGhlIGNvbnRleHQgb2YgdGhlIEFjdG9yLlxcbiAgICBhc3luYyB3aXRoIEFjdG9yOlxcbiAgICAgICAgIyBSZXRyaWV2ZSB0aGUgQWN0b3IgaW5wdXQsIGFuZCB1c2UgZGVmYXVsdCB2YWx1ZXMgaWYgbm90IHByb3ZpZGVkLlxcbiAgICAgICAgYWN0b3JfaW5wdXQgPSBhd2FpdCBBY3Rvci5nZXRfaW5wdXQoKSBvciB7fVxcbiAgICAgICAgc3RhcnRfdXJscyA9IFtcXG4gICAgICAgICAgICB1cmwuZ2V0KCd1cmwnKVxcbiAgICAgICAgICAgIGZvciB1cmwgaW4gYWN0b3JfaW5wdXQuZ2V0KCdzdGFydF91cmxzJywgW3sndXJsJzogJ2h0dHBzOi8vYXBpZnkuY29tJ31dKVxcbiAgICAgICAgXVxcblxcbiAgICAgICAgIyBFeGl0IGlmIG5vIHN0YXJ0IFVSTHMgYXJlIHByb3ZpZGVkLlxcbiAgICAgICAgaWYgbm90IHN0YXJ0X3VybHM6XFxuICAgICAgICAgICAgQWN0b3IubG9nLmluZm8oJ05vIHN0YXJ0IFVSTHMgc3BlY2lmaWVkIGluIEFjdG9yIGlucHV0LCBleGl0aW5nLi4uJylcXG4gICAgICAgICAgICBhd2FpdCBBY3Rvci5leGl0KClcXG5cXG4gICAgICAgICMgUnVuIHRoZSBjcmF3bGVyIHdpdGggdGhlIHN0YXJ0aW5nIHJlcXVlc3RzLlxcbiAgICAgICAgYXdhaXQgY3Jhd2xlci5ydW4oc3RhcnRfdXJscylcXG5cXG5cXG5pZiBfX25hbWVfXyA9PSAnX19tYWluX18nOlxcbiAgICBhc3luY2lvLnJ1bihtYWluKCkpXFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6MTAyNCwidGltZW91dCI6MTgwfX0.qEKrhRL6m-xKuWonxRaNR98DD4mmfFTIHr58mLDsE0k\&asrc=run_on_apify)

```
import asyncio

from crawlee.crawlers import BeautifulSoupCrawler, BeautifulSoupCrawlingContext

from apify import Actor

# Create a crawler.
crawler = BeautifulSoupCrawler(
    # Limit the crawl to max requests. Remove or increase it for crawling all links.
    max_requests_per_crawl=50,
)


# Define a request handler, which will be called for every request.
@crawler.router.default_handler
async def request_handler(context: BeautifulSoupCrawlingContext) -> None:
    Actor.log.info(f'Scraping {context.request.url}...')

    # Extract the desired data.
    data = {
        'url': context.request.url,
        'title': context.soup.title.string if context.soup.title else None,
        'h1s': [h1.text for h1 in context.soup.find_all('h1')],
        'h2s': [h2.text for h2 in context.soup.find_all('h2')],
        'h3s': [h3.text for h3 in context.soup.find_all('h3')],
    }

    # Store the extracted data to the default dataset.
    await context.push_data(data)

    # Enqueue additional links found on the current page.
    await context.enqueue_links(strategy='same-domain')


async def main() -> None:
    # Enter the context of the Actor.
    async with Actor:
        # Retrieve the Actor input, and use default values if not provided.
        actor_input = await Actor.get_input() or {}
        start_urls = [
            url.get('url')
            for url in actor_input.get('start_urls', [{'url': 'https://apify.com'}])
        ]

        # Exit if no start URLs are provided.
        if not start_urls:
            Actor.log.info('No start URLs specified in Actor input, exiting...')
            await Actor.exit()

        # Run the crawler with the starting requests.
        await crawler.run(start_urls)


if __name__ == '__main__':
    asyncio.run(main())
```

## Actor with ParselCrawler[](#actor-with-parselcrawler)

The [`ParselCrawler`](https://crawlee.dev/python/api/class/ParselCrawler) works in the same way as [`BeautifulSoupCrawler`](https://crawlee.dev/python/api/class/BeautifulSoupCrawler), but it uses the [Parsel](https://parsel.readthedocs.io/en/latest/) library for HTML parsing. This allows for more powerful and flexible data extraction using [XPath](https://en.wikipedia.org/wiki/XPath) selectors. It should be faster than [`BeautifulSoupCrawler`](https://crawlee.dev/python/api/class/BeautifulSoupCrawler). Below is an example of how to use [`ParselCrawler`](https://crawlee.dev/python/api/class/ParselCrawler) in an Apify Actor.

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuXFxuZnJvbSBjcmF3bGVlLmNyYXdsZXJzIGltcG9ydCBQYXJzZWxDcmF3bGVyLCBQYXJzZWxDcmF3bGluZ0NvbnRleHRcXG5cXG5mcm9tIGFwaWZ5IGltcG9ydCBBY3RvclxcblxcbiMgQ3JlYXRlIGEgY3Jhd2xlci5cXG5jcmF3bGVyID0gUGFyc2VsQ3Jhd2xlcihcXG4gICAgIyBMaW1pdCB0aGUgY3Jhd2wgdG8gbWF4IHJlcXVlc3RzLiBSZW1vdmUgb3IgaW5jcmVhc2UgaXQgZm9yIGNyYXdsaW5nIGFsbCBsaW5rcy5cXG4gICAgbWF4X3JlcXVlc3RzX3Blcl9jcmF3bD01MCxcXG4pXFxuXFxuXFxuIyBEZWZpbmUgYSByZXF1ZXN0IGhhbmRsZXIsIHdoaWNoIHdpbGwgYmUgY2FsbGVkIGZvciBldmVyeSByZXF1ZXN0LlxcbkBjcmF3bGVyLnJvdXRlci5kZWZhdWx0X2hhbmRsZXJcXG5hc3luYyBkZWYgcmVxdWVzdF9oYW5kbGVyKGNvbnRleHQ6IFBhcnNlbENyYXdsaW5nQ29udGV4dCkgLT4gTm9uZTpcXG4gICAgQWN0b3IubG9nLmluZm8oZidTY3JhcGluZyB7Y29udGV4dC5yZXF1ZXN0LnVybH0uLi4nKVxcblxcbiAgICAjIEV4dHJhY3QgdGhlIGRlc2lyZWQgZGF0YS5cXG4gICAgZGF0YSA9IHtcXG4gICAgICAgICd1cmwnOiBjb250ZXh0LnJlcXVlc3QudXJsLFxcbiAgICAgICAgJ3RpdGxlJzogY29udGV4dC5zZWxlY3Rvci54cGF0aCgnLy90aXRsZS90ZXh0KCknKS5nZXQoKSxcXG4gICAgICAgICdoMXMnOiBjb250ZXh0LnNlbGVjdG9yLnhwYXRoKCcvL2gxL3RleHQoKScpLmdldGFsbCgpLFxcbiAgICAgICAgJ2gycyc6IGNvbnRleHQuc2VsZWN0b3IueHBhdGgoJy8vaDIvdGV4dCgpJykuZ2V0YWxsKCksXFxuICAgICAgICAnaDNzJzogY29udGV4dC5zZWxlY3Rvci54cGF0aCgnLy9oMy90ZXh0KCknKS5nZXRhbGwoKSxcXG4gICAgfVxcblxcbiAgICAjIFN0b3JlIHRoZSBleHRyYWN0ZWQgZGF0YSB0byB0aGUgZGVmYXVsdCBkYXRhc2V0LlxcbiAgICBhd2FpdCBjb250ZXh0LnB1c2hfZGF0YShkYXRhKVxcblxcbiAgICAjIEVucXVldWUgYWRkaXRpb25hbCBsaW5rcyBmb3VuZCBvbiB0aGUgY3VycmVudCBwYWdlLlxcbiAgICBhd2FpdCBjb250ZXh0LmVucXVldWVfbGlua3Moc3RyYXRlZ3k9J3NhbWUtZG9tYWluJylcXG5cXG5cXG5hc3luYyBkZWYgbWFpbigpIC0-IE5vbmU6XFxuICAgICMgRW50ZXIgdGhlIGNvbnRleHQgb2YgdGhlIEFjdG9yLlxcbiAgICBhc3luYyB3aXRoIEFjdG9yOlxcbiAgICAgICAgIyBSZXRyaWV2ZSB0aGUgQWN0b3IgaW5wdXQsIGFuZCB1c2UgZGVmYXVsdCB2YWx1ZXMgaWYgbm90IHByb3ZpZGVkLlxcbiAgICAgICAgYWN0b3JfaW5wdXQgPSBhd2FpdCBBY3Rvci5nZXRfaW5wdXQoKSBvciB7fVxcbiAgICAgICAgc3RhcnRfdXJscyA9IFtcXG4gICAgICAgICAgICB1cmwuZ2V0KCd1cmwnKVxcbiAgICAgICAgICAgIGZvciB1cmwgaW4gYWN0b3JfaW5wdXQuZ2V0KCdzdGFydF91cmxzJywgW3sndXJsJzogJ2h0dHBzOi8vYXBpZnkuY29tJ31dKVxcbiAgICAgICAgXVxcblxcbiAgICAgICAgIyBFeGl0IGlmIG5vIHN0YXJ0IFVSTHMgYXJlIHByb3ZpZGVkLlxcbiAgICAgICAgaWYgbm90IHN0YXJ0X3VybHM6XFxuICAgICAgICAgICAgQWN0b3IubG9nLmluZm8oJ05vIHN0YXJ0IFVSTHMgc3BlY2lmaWVkIGluIEFjdG9yIGlucHV0LCBleGl0aW5nLi4uJylcXG4gICAgICAgICAgICBhd2FpdCBBY3Rvci5leGl0KClcXG5cXG4gICAgICAgICMgUnVuIHRoZSBjcmF3bGVyIHdpdGggdGhlIHN0YXJ0aW5nIHJlcXVlc3RzLlxcbiAgICAgICAgYXdhaXQgY3Jhd2xlci5ydW4oc3RhcnRfdXJscylcXG5cXG5cXG5pZiBfX25hbWVfXyA9PSAnX19tYWluX18nOlxcbiAgICBhc3luY2lvLnJ1bihtYWluKCkpXFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6MTAyNCwidGltZW91dCI6MTgwfX0.GSr4fwvtZLa8Wxowow-qLnfBaUfyJwYcJphrK5EqIRo\&asrc=run_on_apify)

```
import asyncio

from crawlee.crawlers import ParselCrawler, ParselCrawlingContext

from apify import Actor

# Create a crawler.
crawler = ParselCrawler(
    # Limit the crawl to max requests. Remove or increase it for crawling all links.
    max_requests_per_crawl=50,
)


# Define a request handler, which will be called for every request.
@crawler.router.default_handler
async def request_handler(context: ParselCrawlingContext) -> None:
    Actor.log.info(f'Scraping {context.request.url}...')

    # Extract the desired data.
    data = {
        'url': context.request.url,
        'title': context.selector.xpath('//title/text()').get(),
        'h1s': context.selector.xpath('//h1/text()').getall(),
        'h2s': context.selector.xpath('//h2/text()').getall(),
        'h3s': context.selector.xpath('//h3/text()').getall(),
    }

    # Store the extracted data to the default dataset.
    await context.push_data(data)

    # Enqueue additional links found on the current page.
    await context.enqueue_links(strategy='same-domain')


async def main() -> None:
    # Enter the context of the Actor.
    async with Actor:
        # Retrieve the Actor input, and use default values if not provided.
        actor_input = await Actor.get_input() or {}
        start_urls = [
            url.get('url')
            for url in actor_input.get('start_urls', [{'url': 'https://apify.com'}])
        ]

        # Exit if no start URLs are provided.
        if not start_urls:
            Actor.log.info('No start URLs specified in Actor input, exiting...')
            await Actor.exit()

        # Run the crawler with the starting requests.
        await crawler.run(start_urls)


if __name__ == '__main__':
    asyncio.run(main())
```

## Actor with PlaywrightCrawler[](#actor-with-playwrightcrawler)

The [`PlaywrightCrawler`](https://crawlee.dev/python/api/class/PlaywrightCrawler) is built for handling dynamic web pages that rely on JavaScript for content rendering. Using the [Playwright](https://playwright.dev/) library, it provides a browser-based automation environment to interact with complex websites. Below is an example of how to use [`PlaywrightCrawler`](https://crawlee.dev/python/api/class/PlaywrightCrawler) in an Apify Actor.

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuXFxuZnJvbSBjcmF3bGVlLmNyYXdsZXJzIGltcG9ydCBQbGF5d3JpZ2h0Q3Jhd2xlciwgUGxheXdyaWdodENyYXdsaW5nQ29udGV4dFxcblxcbmZyb20gYXBpZnkgaW1wb3J0IEFjdG9yXFxuXFxuIyBDcmVhdGUgYSBjcmF3bGVyLlxcbmNyYXdsZXIgPSBQbGF5d3JpZ2h0Q3Jhd2xlcihcXG4gICAgIyBMaW1pdCB0aGUgY3Jhd2wgdG8gbWF4IHJlcXVlc3RzLiBSZW1vdmUgb3IgaW5jcmVhc2UgaXQgZm9yIGNyYXdsaW5nIGFsbCBsaW5rcy5cXG4gICAgbWF4X3JlcXVlc3RzX3Blcl9jcmF3bD01MCxcXG4gICAgIyBSdW4gdGhlIGJyb3dzZXIgaW4gYSBoZWFkbGVzcyBtb2RlLlxcbiAgICBoZWFkbGVzcz1UcnVlLFxcbiAgICBicm93c2VyX2xhdW5jaF9vcHRpb25zPXsnYXJncyc6IFsnLS1kaXNhYmxlLWdwdSddfSxcXG4pXFxuXFxuXFxuIyBEZWZpbmUgYSByZXF1ZXN0IGhhbmRsZXIsIHdoaWNoIHdpbGwgYmUgY2FsbGVkIGZvciBldmVyeSByZXF1ZXN0LlxcbkBjcmF3bGVyLnJvdXRlci5kZWZhdWx0X2hhbmRsZXJcXG5hc3luYyBkZWYgcmVxdWVzdF9oYW5kbGVyKGNvbnRleHQ6IFBsYXl3cmlnaHRDcmF3bGluZ0NvbnRleHQpIC0-IE5vbmU6XFxuICAgIEFjdG9yLmxvZy5pbmZvKGYnU2NyYXBpbmcge2NvbnRleHQucmVxdWVzdC51cmx9Li4uJylcXG5cXG4gICAgIyBFeHRyYWN0IHRoZSBkZXNpcmVkIGRhdGEuXFxuICAgIGRhdGEgPSB7XFxuICAgICAgICAndXJsJzogY29udGV4dC5yZXF1ZXN0LnVybCxcXG4gICAgICAgICd0aXRsZSc6IGF3YWl0IGNvbnRleHQucGFnZS50aXRsZSgpLFxcbiAgICAgICAgJ2gxcyc6IFthd2FpdCBoMS50ZXh0X2NvbnRlbnQoKSBmb3IgaDEgaW4gYXdhaXQgY29udGV4dC5wYWdlLmxvY2F0b3IoJ2gxJykuYWxsKCldLFxcbiAgICAgICAgJ2gycyc6IFthd2FpdCBoMi50ZXh0X2NvbnRlbnQoKSBmb3IgaDIgaW4gYXdhaXQgY29udGV4dC5wYWdlLmxvY2F0b3IoJ2gyJykuYWxsKCldLFxcbiAgICAgICAgJ2gzcyc6IFthd2FpdCBoMy50ZXh0X2NvbnRlbnQoKSBmb3IgaDMgaW4gYXdhaXQgY29udGV4dC5wYWdlLmxvY2F0b3IoJ2gzJykuYWxsKCldLFxcbiAgICB9XFxuXFxuICAgICMgU3RvcmUgdGhlIGV4dHJhY3RlZCBkYXRhIHRvIHRoZSBkZWZhdWx0IGRhdGFzZXQuXFxuICAgIGF3YWl0IGNvbnRleHQucHVzaF9kYXRhKGRhdGEpXFxuXFxuICAgICMgRW5xdWV1ZSBhZGRpdGlvbmFsIGxpbmtzIGZvdW5kIG9uIHRoZSBjdXJyZW50IHBhZ2UuXFxuICAgIGF3YWl0IGNvbnRleHQuZW5xdWV1ZV9saW5rcyhzdHJhdGVneT0nc2FtZS1kb21haW4nKVxcblxcblxcbmFzeW5jIGRlZiBtYWluKCkgLT4gTm9uZTpcXG4gICAgIyBFbnRlciB0aGUgY29udGV4dCBvZiB0aGUgQWN0b3IuXFxuICAgIGFzeW5jIHdpdGggQWN0b3I6XFxuICAgICAgICAjIFJldHJpZXZlIHRoZSBBY3RvciBpbnB1dCwgYW5kIHVzZSBkZWZhdWx0IHZhbHVlcyBpZiBub3QgcHJvdmlkZWQuXFxuICAgICAgICBhY3Rvcl9pbnB1dCA9IGF3YWl0IEFjdG9yLmdldF9pbnB1dCgpIG9yIHt9XFxuICAgICAgICBzdGFydF91cmxzID0gW1xcbiAgICAgICAgICAgIHVybC5nZXQoJ3VybCcpXFxuICAgICAgICAgICAgZm9yIHVybCBpbiBhY3Rvcl9pbnB1dC5nZXQoJ3N0YXJ0X3VybHMnLCBbeyd1cmwnOiAnaHR0cHM6Ly9hcGlmeS5jb20nfV0pXFxuICAgICAgICBdXFxuXFxuICAgICAgICAjIEV4aXQgaWYgbm8gc3RhcnQgVVJMcyBhcmUgcHJvdmlkZWQuXFxuICAgICAgICBpZiBub3Qgc3RhcnRfdXJsczpcXG4gICAgICAgICAgICBBY3Rvci5sb2cuaW5mbygnTm8gc3RhcnQgVVJMcyBzcGVjaWZpZWQgaW4gQWN0b3IgaW5wdXQsIGV4aXRpbmcuLi4nKVxcbiAgICAgICAgICAgIGF3YWl0IEFjdG9yLmV4aXQoKVxcblxcbiAgICAgICAgIyBSdW4gdGhlIGNyYXdsZXIgd2l0aCB0aGUgc3RhcnRpbmcgcmVxdWVzdHMuXFxuICAgICAgICBhd2FpdCBjcmF3bGVyLnJ1bihzdGFydF91cmxzKVxcblxcblxcbmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6XFxuICAgIGFzeW5jaW8ucnVuKG1haW4oKSlcXG5cIn0iLCJvcHRpb25zIjp7ImJ1aWxkIjoibGF0ZXN0IiwiY29udGVudFR5cGUiOiJhcHBsaWNhdGlvbi9qc29uOyBjaGFyc2V0PXV0Zi04IiwibWVtb3J5Ijo0MDk2LCJ0aW1lb3V0IjoxODB9fQ.RtazYJOYFATXGeOjDLcNBhc7XsSht-HPp8l7PcGGRNo\&asrc=run_on_apify)

```
import asyncio

from crawlee.crawlers import PlaywrightCrawler, PlaywrightCrawlingContext

from apify import Actor

# Create a crawler.
crawler = PlaywrightCrawler(
    # Limit the crawl to max requests. Remove or increase it for crawling all links.
    max_requests_per_crawl=50,
    # Run the browser in a headless mode.
    headless=True,
    browser_launch_options={'args': ['--disable-gpu']},
)


# Define a request handler, which will be called for every request.
@crawler.router.default_handler
async def request_handler(context: PlaywrightCrawlingContext) -> None:
    Actor.log.info(f'Scraping {context.request.url}...')

    # Extract the desired data.
    data = {
        'url': context.request.url,
        'title': await context.page.title(),
        'h1s': [await h1.text_content() for h1 in await context.page.locator('h1').all()],
        'h2s': [await h2.text_content() for h2 in await context.page.locator('h2').all()],
        'h3s': [await h3.text_content() for h3 in await context.page.locator('h3').all()],
    }

    # Store the extracted data to the default dataset.
    await context.push_data(data)

    # Enqueue additional links found on the current page.
    await context.enqueue_links(strategy='same-domain')


async def main() -> None:
    # Enter the context of the Actor.
    async with Actor:
        # Retrieve the Actor input, and use default values if not provided.
        actor_input = await Actor.get_input() or {}
        start_urls = [
            url.get('url')
            for url in actor_input.get('start_urls', [{'url': 'https://apify.com'}])
        ]

        # Exit if no start URLs are provided.
        if not start_urls:
            Actor.log.info('No start URLs specified in Actor input, exiting...')
            await Actor.exit()

        # Run the crawler with the starting requests.
        await crawler.run(start_urls)


if __name__ == '__main__':
    asyncio.run(main())
```

## Conclusion[](#conclusion)

In this guide, you learned how to use the [Crawlee](https://crawlee.dev/python) library in your Apify Actors. By using the [`BeautifulSoupCrawler`](https://crawlee.dev/python/api/class/BeautifulSoupCrawler), [`ParselCrawler`](https://crawlee.dev/python/api/class/ParselCrawler), and [`PlaywrightCrawler`](https://crawlee.dev/python/api/class/PlaywrightCrawler) crawlers, you can efficiently scrape static or dynamic web pages, making it easy to build web scraping tasks in Python. See the [Actor templates](https://apify.com/templates/categories/python) to get started with your own scraping tasks. If you have questions or need assistance, feel free to reach out on our [GitHub](https://github.com/apify/apify-sdk-python) or join our [Discord community](https://discord.com/invite/jyEM2PRvMU). Happy scraping!
