# Source: https://docs.apify.com/sdk/python/docs/guides/playwright.md

# Using Playwright

Copy for LLM

[Playwright](https://playwright.dev) is a tool for web automation and testing that can also be used for web scraping. It allows you to control a web browser programmatically and interact with web pages just as a human would.

Some of the key features of Playwright for web scraping include:

* **Cross-browser support** - Playwright supports the latest versions of major browsers like Chrome, Firefox, and Safari, so you can choose the one that suits your needs the best.
* **Headless mode** - Playwright can run in headless mode, meaning that the browser window is not visible on your screen while it is scraping, which can be useful for running scraping tasks in the background or in containers without a display.
* **Powerful selectors** - Playwright provides a variety of powerful selectors that allow you to target specific elements on a web page, including CSS selectors, XPath, and text matching.
* **Emulation of user interactions** - Playwright allows you to emulate user interactions like clicking, scrolling, filling out forms, and even typing in text, which can be useful for scraping websites that have dynamic content or require user input.

## Using Playwright in Actors[](#using-playwright-in-actors)

To create Actors which use Playwright, start from the [Playwright & Python](https://apify.com/templates/categories/python) Actor template.

On the Apify platform, the Actor will already have Playwright and the necessary browsers preinstalled in its Docker image, including the tools and setup necessary to run browsers in headful mode.

When running the Actor locally, you'll need to finish the Playwright setup yourself before you can run the Actor.

* Linux / macOS
* Windows

```
source .venv/bin/activate
playwright install --with-deps
```

```
.venv\Scripts\activate
playwright install --with-deps
```

## Example Actor[](#example-actor)

This is a simple Actor that recursively scrapes titles from all linked websites, up to a maximum depth, starting from URLs in the Actor input.

It uses Playwright to open the pages in an automated Chrome browser, and to extract the title and anchor elements after the pages load.

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuZnJvbSB1cmxsaWIucGFyc2UgaW1wb3J0IHVybGpvaW5cXG5cXG5mcm9tIHBsYXl3cmlnaHQuYXN5bmNfYXBpIGltcG9ydCBhc3luY19wbGF5d3JpZ2h0XFxuXFxuZnJvbSBhcGlmeSBpbXBvcnQgQWN0b3IsIFJlcXVlc3RcXG5cXG4jIE5vdGU6IFRvIHJ1biB0aGlzIEFjdG9yIGxvY2FsbHksIGVuc3VyZSB0aGF0IFBsYXl3cmlnaHQgYnJvd3NlcnMgYXJlIGluc3RhbGxlZC5cXG4jIFJ1biBgcGxheXdyaWdodCBpbnN0YWxsIC0td2l0aC1kZXBzYCBpbiB0aGUgQWN0b3IncyB2aXJ0dWFsIGVudmlyb25tZW50IHRvIGluc3RhbGwgdGhlbS5cXG4jIFdoZW4gcnVubmluZyBvbiB0aGUgQXBpZnkgcGxhdGZvcm0sIHRoZXNlIGRlcGVuZGVuY2llcyBhcmUgYWxyZWFkeSBpbmNsdWRlZFxcbiMgaW4gdGhlIEFjdG9yJ3MgRG9ja2VyIGltYWdlLlxcblxcblxcbmFzeW5jIGRlZiBtYWluKCkgLT4gTm9uZTpcXG4gICAgIyBFbnRlciB0aGUgY29udGV4dCBvZiB0aGUgQWN0b3IuXFxuICAgIGFzeW5jIHdpdGggQWN0b3I6XFxuICAgICAgICAjIFJldHJpZXZlIHRoZSBBY3RvciBpbnB1dCwgYW5kIHVzZSBkZWZhdWx0IHZhbHVlcyBpZiBub3QgcHJvdmlkZWQuXFxuICAgICAgICBhY3Rvcl9pbnB1dCA9IGF3YWl0IEFjdG9yLmdldF9pbnB1dCgpIG9yIHt9XFxuICAgICAgICBzdGFydF91cmxzID0gYWN0b3JfaW5wdXQuZ2V0KCdzdGFydF91cmxzJywgW3sndXJsJzogJ2h0dHBzOi8vYXBpZnkuY29tJ31dKVxcbiAgICAgICAgbWF4X2RlcHRoID0gYWN0b3JfaW5wdXQuZ2V0KCdtYXhfZGVwdGgnLCAxKVxcblxcbiAgICAgICAgIyBFeGl0IGlmIG5vIHN0YXJ0IFVSTHMgYXJlIHByb3ZpZGVkLlxcbiAgICAgICAgaWYgbm90IHN0YXJ0X3VybHM6XFxuICAgICAgICAgICAgQWN0b3IubG9nLmluZm8oJ05vIHN0YXJ0IFVSTHMgc3BlY2lmaWVkIGluIGFjdG9yIGlucHV0LCBleGl0aW5nLi4uJylcXG4gICAgICAgICAgICBhd2FpdCBBY3Rvci5leGl0KClcXG5cXG4gICAgICAgICMgT3BlbiB0aGUgZGVmYXVsdCByZXF1ZXN0IHF1ZXVlIGZvciBoYW5kbGluZyBVUkxzIHRvIGJlIHByb2Nlc3NlZC5cXG4gICAgICAgIHJlcXVlc3RfcXVldWUgPSBhd2FpdCBBY3Rvci5vcGVuX3JlcXVlc3RfcXVldWUoKVxcblxcbiAgICAgICAgIyBFbnF1ZXVlIHRoZSBzdGFydCBVUkxzIHdpdGggYW4gaW5pdGlhbCBjcmF3bCBkZXB0aCBvZiAwLlxcbiAgICAgICAgZm9yIHN0YXJ0X3VybCBpbiBzdGFydF91cmxzOlxcbiAgICAgICAgICAgIHVybCA9IHN0YXJ0X3VybC5nZXQoJ3VybCcpXFxuICAgICAgICAgICAgQWN0b3IubG9nLmluZm8oZidFbnF1ZXVpbmcge3VybH0gLi4uJylcXG4gICAgICAgICAgICBuZXdfcmVxdWVzdCA9IFJlcXVlc3QuZnJvbV91cmwodXJsLCB1c2VyX2RhdGE9eydkZXB0aCc6IDB9KVxcbiAgICAgICAgICAgIGF3YWl0IHJlcXVlc3RfcXVldWUuYWRkX3JlcXVlc3QobmV3X3JlcXVlc3QpXFxuXFxuICAgICAgICBBY3Rvci5sb2cuaW5mbygnTGF1bmNoaW5nIFBsYXl3cmlnaHQuLi4nKVxcblxcbiAgICAgICAgIyBMYXVuY2ggUGxheXdyaWdodCBhbmQgb3BlbiBhIG5ldyBicm93c2VyIGNvbnRleHQuXFxuICAgICAgICBhc3luYyB3aXRoIGFzeW5jX3BsYXl3cmlnaHQoKSBhcyBwbGF5d3JpZ2h0OlxcbiAgICAgICAgICAgICMgQ29uZmlndXJlIHRoZSBicm93c2VyIHRvIGxhdW5jaCBpbiBoZWFkbGVzcyBtb2RlIGFzIHBlciBBY3RvciBjb25maWd1cmF0aW9uLlxcbiAgICAgICAgICAgIGJyb3dzZXIgPSBhd2FpdCBwbGF5d3JpZ2h0LmNocm9taXVtLmxhdW5jaChcXG4gICAgICAgICAgICAgICAgaGVhZGxlc3M9QWN0b3IuY29uZmlndXJhdGlvbi5oZWFkbGVzcyxcXG4gICAgICAgICAgICAgICAgYXJncz1bJy0tZGlzYWJsZS1ncHUnXSxcXG4gICAgICAgICAgICApXFxuICAgICAgICAgICAgY29udGV4dCA9IGF3YWl0IGJyb3dzZXIubmV3X2NvbnRleHQoKVxcblxcbiAgICAgICAgICAgICMgUHJvY2VzcyB0aGUgVVJMcyBmcm9tIHRoZSByZXF1ZXN0IHF1ZXVlLlxcbiAgICAgICAgICAgIHdoaWxlIHJlcXVlc3QgOj0gYXdhaXQgcmVxdWVzdF9xdWV1ZS5mZXRjaF9uZXh0X3JlcXVlc3QoKTpcXG4gICAgICAgICAgICAgICAgdXJsID0gcmVxdWVzdC51cmxcXG5cXG4gICAgICAgICAgICAgICAgaWYgbm90IGlzaW5zdGFuY2UocmVxdWVzdC51c2VyX2RhdGFbJ2RlcHRoJ10sIChzdHIsIGludCkpOlxcbiAgICAgICAgICAgICAgICAgICAgcmFpc2UgVHlwZUVycm9yKCdSZXF1ZXN0LmRlcHRoIGlzIGFuIHVuZXhwZWN0ZWQgdHlwZS4nKVxcblxcbiAgICAgICAgICAgICAgICBkZXB0aCA9IGludChyZXF1ZXN0LnVzZXJfZGF0YVsnZGVwdGgnXSlcXG4gICAgICAgICAgICAgICAgQWN0b3IubG9nLmluZm8oZidTY3JhcGluZyB7dXJsfSAoZGVwdGg9e2RlcHRofSkgLi4uJylcXG5cXG4gICAgICAgICAgICAgICAgdHJ5OlxcbiAgICAgICAgICAgICAgICAgICAgIyBPcGVuIGEgbmV3IHBhZ2UgaW4gdGhlIGJyb3dzZXIgY29udGV4dCBhbmQgbmF2aWdhdGUgdG8gdGhlIFVSTC5cXG4gICAgICAgICAgICAgICAgICAgIHBhZ2UgPSBhd2FpdCBjb250ZXh0Lm5ld19wYWdlKClcXG4gICAgICAgICAgICAgICAgICAgIGF3YWl0IHBhZ2UuZ290byh1cmwpXFxuXFxuICAgICAgICAgICAgICAgICAgICAjIElmIHRoZSBjdXJyZW50IGRlcHRoIGlzIGxlc3MgdGhhbiBtYXhfZGVwdGgsIGZpbmQgbmVzdGVkIGxpbmtzXFxuICAgICAgICAgICAgICAgICAgICAjIGFuZCBlbnF1ZXVlIHRoZW0uXFxuICAgICAgICAgICAgICAgICAgICBpZiBkZXB0aCA8IG1heF9kZXB0aDpcXG4gICAgICAgICAgICAgICAgICAgICAgICBmb3IgbGluayBpbiBhd2FpdCBwYWdlLmxvY2F0b3IoJ2EnKS5hbGwoKTpcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgbGlua19ocmVmID0gYXdhaXQgbGluay5nZXRfYXR0cmlidXRlKCdocmVmJylcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgbGlua191cmwgPSB1cmxqb2luKHVybCwgbGlua19ocmVmKVxcblxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpZiBsaW5rX3VybC5zdGFydHN3aXRoKCgnaHR0cDovLycsICdodHRwczovLycpKTpcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIEFjdG9yLmxvZy5pbmZvKGYnRW5xdWV1aW5nIHtsaW5rX3VybH0gLi4uJylcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5ld19yZXF1ZXN0ID0gUmVxdWVzdC5mcm9tX3VybChcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsaW5rX3VybCxcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB1c2VyX2RhdGE9eydkZXB0aCc6IGRlcHRoICsgMX0sXFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICApXFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhd2FpdCByZXF1ZXN0X3F1ZXVlLmFkZF9yZXF1ZXN0KG5ld19yZXF1ZXN0KVxcblxcbiAgICAgICAgICAgICAgICAgICAgIyBFeHRyYWN0IHRoZSBkZXNpcmVkIGRhdGEuXFxuICAgICAgICAgICAgICAgICAgICBkYXRhID0ge1xcbiAgICAgICAgICAgICAgICAgICAgICAgICd1cmwnOiB1cmwsXFxuICAgICAgICAgICAgICAgICAgICAgICAgJ3RpdGxlJzogYXdhaXQgcGFnZS50aXRsZSgpLFxcbiAgICAgICAgICAgICAgICAgICAgfVxcblxcbiAgICAgICAgICAgICAgICAgICAgIyBTdG9yZSB0aGUgZXh0cmFjdGVkIGRhdGEgdG8gdGhlIGRlZmF1bHQgZGF0YXNldC5cXG4gICAgICAgICAgICAgICAgICAgIGF3YWl0IEFjdG9yLnB1c2hfZGF0YShkYXRhKVxcblxcbiAgICAgICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uOlxcbiAgICAgICAgICAgICAgICAgICAgQWN0b3IubG9nLmV4Y2VwdGlvbihmJ0Nhbm5vdCBleHRyYWN0IGRhdGEgZnJvbSB7dXJsfS4nKVxcblxcbiAgICAgICAgICAgICAgICBmaW5hbGx5OlxcbiAgICAgICAgICAgICAgICAgICAgYXdhaXQgcGFnZS5jbG9zZSgpXFxuICAgICAgICAgICAgICAgICAgICAjIE1hcmsgdGhlIHJlcXVlc3QgYXMgaGFuZGxlZCB0byBlbnN1cmUgaXQgaXMgbm90IHByb2Nlc3NlZCBhZ2Fpbi5cXG4gICAgICAgICAgICAgICAgICAgIGF3YWl0IHJlcXVlc3RfcXVldWUubWFya19yZXF1ZXN0X2FzX2hhbmRsZWQocmVxdWVzdClcXG5cXG5cXG5pZiBfX25hbWVfXyA9PSAnX19tYWluX18nOlxcbiAgICBhc3luY2lvLnJ1bihtYWluKCkpXFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6NDA5NiwidGltZW91dCI6MTgwfX0.2h3ZDCzREoxI4Rx8kVO6G_J4I1VE2DRR-bcpuRunsQ8\&asrc=run_on_apify)

```
import asyncio
from urllib.parse import urljoin

from playwright.async_api import async_playwright

from apify import Actor, Request

# Note: To run this Actor locally, ensure that Playwright browsers are installed.
# Run `playwright install --with-deps` in the Actor's virtual environment to install them.
# When running on the Apify platform, these dependencies are already included
# in the Actor's Docker image.


async def main() -> None:
    # Enter the context of the Actor.
    async with Actor:
        # Retrieve the Actor input, and use default values if not provided.
        actor_input = await Actor.get_input() or {}
        start_urls = actor_input.get('start_urls', [{'url': 'https://apify.com'}])
        max_depth = actor_input.get('max_depth', 1)

        # Exit if no start URLs are provided.
        if not start_urls:
            Actor.log.info('No start URLs specified in actor input, exiting...')
            await Actor.exit()

        # Open the default request queue for handling URLs to be processed.
        request_queue = await Actor.open_request_queue()

        # Enqueue the start URLs with an initial crawl depth of 0.
        for start_url in start_urls:
            url = start_url.get('url')
            Actor.log.info(f'Enqueuing {url} ...')
            new_request = Request.from_url(url, user_data={'depth': 0})
            await request_queue.add_request(new_request)

        Actor.log.info('Launching Playwright...')

        # Launch Playwright and open a new browser context.
        async with async_playwright() as playwright:
            # Configure the browser to launch in headless mode as per Actor configuration.
            browser = await playwright.chromium.launch(
                headless=Actor.configuration.headless,
                args=['--disable-gpu'],
            )
            context = await browser.new_context()

            # Process the URLs from the request queue.
            while request := await request_queue.fetch_next_request():
                url = request.url

                if not isinstance(request.user_data['depth'], (str, int)):
                    raise TypeError('Request.depth is an unexpected type.')

                depth = int(request.user_data['depth'])
                Actor.log.info(f'Scraping {url} (depth={depth}) ...')

                try:
                    # Open a new page in the browser context and navigate to the URL.
                    page = await context.new_page()
                    await page.goto(url)

                    # If the current depth is less than max_depth, find nested links
                    # and enqueue them.
                    if depth < max_depth:
                        for link in await page.locator('a').all():
                            link_href = await link.get_attribute('href')
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
                        'title': await page.title(),
                    }

                    # Store the extracted data to the default dataset.
                    await Actor.push_data(data)

                except Exception:
                    Actor.log.exception(f'Cannot extract data from {url}.')

                finally:
                    await page.close()
                    # Mark the request as handled to ensure it is not processed again.
                    await request_queue.mark_request_as_handled(request)


if __name__ == '__main__':
    asyncio.run(main())
```

## Conclusion[](#conclusion)

In this guide you learned how to create Actors that use Playwright to scrape websites. Playwright is a powerful tool that can be used to manage browser instances and scrape websites that require JavaScript execution. See the [Actor templates](https://apify.com/templates/categories/python) to get started with your own scraping tasks. If you have questions or need assistance, feel free to reach out on our [GitHub](https://github.com/apify/apify-sdk-python) or join our [Discord community](https://discord.com/invite/jyEM2PRvMU). Happy scraping!
