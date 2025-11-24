# Source: https://docs.apify.com/sdk/python/docs/guides/selenium.md

# Using Selenium

Copy for LLM

[Selenium](https://www.selenium.dev/) is a tool for web automation and testing that can also be used for web scraping. It allows you to control a web browser programmatically and interact with web pages just as a human would.

Some of the key features of Selenium for web scraping include:

* **Cross-browser support** - Selenium supports the latest versions of major browsers like Chrome, Firefox, and Safari, so you can choose the one that suits your needs the best.
* **Headless mode** - Selenium can run in headless mode, meaning that the browser window is not visible on your screen while it is scraping, which can be useful for running scraping tasks in the background or in containers without a display.
* **Powerful selectors** - Selenium provides a variety of powerful selectors that allow you to target specific elements on a web page, including CSS selectors, XPath, and text matching.
* **Emulation of user interactions** - Selenium allows you to emulate user interactions like clicking, scrolling, filling out forms, and even typing in text, which can be useful for scraping websites that have dynamic content or require user input.

## Using Selenium in Actors[](#using-selenium-in-actors)

To create Actors which use Selenium, start from the [Selenium & Python](https://apify.com/templates/categories/python) Actor template.

On the Apify platform, the Actor will already have Selenium and the necessary browsers preinstalled in its Docker image, including the tools and setup necessary to run browsers in headful mode.

When running the Actor locally, you'll need to install the Selenium browser drivers yourself. Refer to the [Selenium documentation](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) for installation instructions.

## Example Actor[](#example-actor)

This is a simple Actor that recursively scrapes titles from all linked websites, up to a maximum depth, starting from URLs in the Actor input.

It uses Selenium ChromeDriver to open the pages in an automated Chrome browser, and to extract the title and anchor elements after the pages load.

[Run on](https://console.apify.com/actors/HH9rhkFXiZbheuq1V?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCBhc3luY2lvXFxuZnJvbSB1cmxsaWIucGFyc2UgaW1wb3J0IHVybGpvaW5cXG5cXG5mcm9tIHNlbGVuaXVtIGltcG9ydCB3ZWJkcml2ZXJcXG5mcm9tIHNlbGVuaXVtLndlYmRyaXZlci5jaHJvbWUub3B0aW9ucyBpbXBvcnQgT3B0aW9ucyBhcyBDaHJvbWVPcHRpb25zXFxuZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuY29tbW9uLmJ5IGltcG9ydCBCeVxcblxcbmZyb20gYXBpZnkgaW1wb3J0IEFjdG9yLCBSZXF1ZXN0XFxuXFxuIyBUbyBydW4gdGhpcyBBY3RvciBsb2NhbGx5LCB5b3UgbmVlZCB0byBoYXZlIHRoZSBTZWxlbml1bSBDaHJvbWVkcml2ZXIgaW5zdGFsbGVkLlxcbiMgRm9sbG93IHRoZSBpbnN0YWxsYXRpb24gZ3VpZGUgYXQ6XFxuIyBodHRwczovL3d3dy5zZWxlbml1bS5kZXYvZG9jdW1lbnRhdGlvbi93ZWJkcml2ZXIvZ2V0dGluZ19zdGFydGVkL2luc3RhbGxfZHJpdmVycy9cXG4jIFdoZW4gcnVubmluZyBvbiB0aGUgQXBpZnkgcGxhdGZvcm0sIHRoZSBDaHJvbWVkcml2ZXIgaXMgYWxyZWFkeSBpbmNsdWRlZFxcbiMgaW4gdGhlIEFjdG9yJ3MgRG9ja2VyIGltYWdlLlxcblxcblxcbmFzeW5jIGRlZiBtYWluKCkgLT4gTm9uZTpcXG4gICAgIyBFbnRlciB0aGUgY29udGV4dCBvZiB0aGUgQWN0b3IuXFxuICAgIGFzeW5jIHdpdGggQWN0b3I6XFxuICAgICAgICAjIFJldHJpZXZlIHRoZSBBY3RvciBpbnB1dCwgYW5kIHVzZSBkZWZhdWx0IHZhbHVlcyBpZiBub3QgcHJvdmlkZWQuXFxuICAgICAgICBhY3Rvcl9pbnB1dCA9IGF3YWl0IEFjdG9yLmdldF9pbnB1dCgpIG9yIHt9XFxuICAgICAgICBzdGFydF91cmxzID0gYWN0b3JfaW5wdXQuZ2V0KCdzdGFydF91cmxzJywgW3sndXJsJzogJ2h0dHBzOi8vYXBpZnkuY29tJ31dKVxcbiAgICAgICAgbWF4X2RlcHRoID0gYWN0b3JfaW5wdXQuZ2V0KCdtYXhfZGVwdGgnLCAxKVxcblxcbiAgICAgICAgIyBFeGl0IGlmIG5vIHN0YXJ0IFVSTHMgYXJlIHByb3ZpZGVkLlxcbiAgICAgICAgaWYgbm90IHN0YXJ0X3VybHM6XFxuICAgICAgICAgICAgQWN0b3IubG9nLmluZm8oJ05vIHN0YXJ0IFVSTHMgc3BlY2lmaWVkIGluIGFjdG9yIGlucHV0LCBleGl0aW5nLi4uJylcXG4gICAgICAgICAgICBhd2FpdCBBY3Rvci5leGl0KClcXG5cXG4gICAgICAgICMgT3BlbiB0aGUgZGVmYXVsdCByZXF1ZXN0IHF1ZXVlIGZvciBoYW5kbGluZyBVUkxzIHRvIGJlIHByb2Nlc3NlZC5cXG4gICAgICAgIHJlcXVlc3RfcXVldWUgPSBhd2FpdCBBY3Rvci5vcGVuX3JlcXVlc3RfcXVldWUoKVxcblxcbiAgICAgICAgIyBFbnF1ZXVlIHRoZSBzdGFydCBVUkxzIHdpdGggYW4gaW5pdGlhbCBjcmF3bCBkZXB0aCBvZiAwLlxcbiAgICAgICAgZm9yIHN0YXJ0X3VybCBpbiBzdGFydF91cmxzOlxcbiAgICAgICAgICAgIHVybCA9IHN0YXJ0X3VybC5nZXQoJ3VybCcpXFxuICAgICAgICAgICAgQWN0b3IubG9nLmluZm8oZidFbnF1ZXVpbmcge3VybH0gLi4uJylcXG4gICAgICAgICAgICBuZXdfcmVxdWVzdCA9IFJlcXVlc3QuZnJvbV91cmwodXJsLCB1c2VyX2RhdGE9eydkZXB0aCc6IDB9KVxcbiAgICAgICAgICAgIGF3YWl0IHJlcXVlc3RfcXVldWUuYWRkX3JlcXVlc3QobmV3X3JlcXVlc3QpXFxuXFxuICAgICAgICAjIExhdW5jaCBhIG5ldyBTZWxlbml1bSBDaHJvbWUgV2ViRHJpdmVyIGFuZCBjb25maWd1cmUgaXQuXFxuICAgICAgICBBY3Rvci5sb2cuaW5mbygnTGF1bmNoaW5nIENocm9tZSBXZWJEcml2ZXIuLi4nKVxcbiAgICAgICAgY2hyb21lX29wdGlvbnMgPSBDaHJvbWVPcHRpb25zKClcXG5cXG4gICAgICAgIGlmIEFjdG9yLmNvbmZpZ3VyYXRpb24uaGVhZGxlc3M6XFxuICAgICAgICAgICAgY2hyb21lX29wdGlvbnMuYWRkX2FyZ3VtZW50KCctLWhlYWRsZXNzJylcXG5cXG4gICAgICAgIGNocm9tZV9vcHRpb25zLmFkZF9hcmd1bWVudCgnLS1uby1zYW5kYm94JylcXG4gICAgICAgIGNocm9tZV9vcHRpb25zLmFkZF9hcmd1bWVudCgnLS1kaXNhYmxlLWRldi1zaG0tdXNhZ2UnKVxcbiAgICAgICAgZHJpdmVyID0gd2ViZHJpdmVyLkNocm9tZShvcHRpb25zPWNocm9tZV9vcHRpb25zKVxcblxcbiAgICAgICAgIyBUZXN0IFdlYkRyaXZlciBzZXR1cCBieSBuYXZpZ2F0aW5nIHRvIGFuIGV4YW1wbGUgcGFnZS5cXG4gICAgICAgIGRyaXZlci5nZXQoJ2h0dHA6Ly93d3cuZXhhbXBsZS5jb20nKVxcbiAgICAgICAgaWYgZHJpdmVyLnRpdGxlICE9ICdFeGFtcGxlIERvbWFpbic6XFxuICAgICAgICAgICAgcmFpc2UgVmFsdWVFcnJvcignRmFpbGVkIHRvIG9wZW4gZXhhbXBsZSBwYWdlLicpXFxuXFxuICAgICAgICAjIFByb2Nlc3MgdGhlIFVSTHMgZnJvbSB0aGUgcmVxdWVzdCBxdWV1ZS5cXG4gICAgICAgIHdoaWxlIHJlcXVlc3QgOj0gYXdhaXQgcmVxdWVzdF9xdWV1ZS5mZXRjaF9uZXh0X3JlcXVlc3QoKTpcXG4gICAgICAgICAgICB1cmwgPSByZXF1ZXN0LnVybFxcblxcbiAgICAgICAgICAgIGlmIG5vdCBpc2luc3RhbmNlKHJlcXVlc3QudXNlcl9kYXRhWydkZXB0aCddLCAoc3RyLCBpbnQpKTpcXG4gICAgICAgICAgICAgICAgcmFpc2UgVHlwZUVycm9yKCdSZXF1ZXN0LmRlcHRoIGlzIGFuIHVuZXhwZWN0ZWQgdHlwZS4nKVxcblxcbiAgICAgICAgICAgIGRlcHRoID0gaW50KHJlcXVlc3QudXNlcl9kYXRhWydkZXB0aCddKVxcbiAgICAgICAgICAgIEFjdG9yLmxvZy5pbmZvKGYnU2NyYXBpbmcge3VybH0gKGRlcHRoPXtkZXB0aH0pIC4uLicpXFxuXFxuICAgICAgICAgICAgdHJ5OlxcbiAgICAgICAgICAgICAgICAjIE5hdmlnYXRlIHRvIHRoZSBVUkwgdXNpbmcgU2VsZW5pdW0gV2ViRHJpdmVyLiBVc2UgYXN5bmNpby50b190aHJlYWRcXG4gICAgICAgICAgICAgICAgIyBmb3Igbm9uLWJsb2NraW5nIGV4ZWN1dGlvbi5cXG4gICAgICAgICAgICAgICAgYXdhaXQgYXN5bmNpby50b190aHJlYWQoZHJpdmVyLmdldCwgdXJsKVxcblxcbiAgICAgICAgICAgICAgICAjIElmIHRoZSBjdXJyZW50IGRlcHRoIGlzIGxlc3MgdGhhbiBtYXhfZGVwdGgsIGZpbmQgbmVzdGVkIGxpbmtzXFxuICAgICAgICAgICAgICAgICMgYW5kIGVucXVldWUgdGhlbS5cXG4gICAgICAgICAgICAgICAgaWYgZGVwdGggPCBtYXhfZGVwdGg6XFxuICAgICAgICAgICAgICAgICAgICBmb3IgbGluayBpbiBkcml2ZXIuZmluZF9lbGVtZW50cyhCeS5UQUdfTkFNRSwgJ2EnKTpcXG4gICAgICAgICAgICAgICAgICAgICAgICBsaW5rX2hyZWYgPSBsaW5rLmdldF9hdHRyaWJ1dGUoJ2hyZWYnKVxcbiAgICAgICAgICAgICAgICAgICAgICAgIGxpbmtfdXJsID0gdXJsam9pbih1cmwsIGxpbmtfaHJlZilcXG5cXG4gICAgICAgICAgICAgICAgICAgICAgICBpZiBsaW5rX3VybC5zdGFydHN3aXRoKCgnaHR0cDovLycsICdodHRwczovLycpKTpcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgQWN0b3IubG9nLmluZm8oZidFbnF1ZXVpbmcge2xpbmtfdXJsfSAuLi4nKVxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBuZXdfcmVxdWVzdCA9IFJlcXVlc3QuZnJvbV91cmwoXFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsaW5rX3VybCxcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHVzZXJfZGF0YT17J2RlcHRoJzogZGVwdGggKyAxfSxcXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgKVxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBhd2FpdCByZXF1ZXN0X3F1ZXVlLmFkZF9yZXF1ZXN0KG5ld19yZXF1ZXN0KVxcblxcbiAgICAgICAgICAgICAgICAjIEV4dHJhY3QgdGhlIGRlc2lyZWQgZGF0YS5cXG4gICAgICAgICAgICAgICAgZGF0YSA9IHtcXG4gICAgICAgICAgICAgICAgICAgICd1cmwnOiB1cmwsXFxuICAgICAgICAgICAgICAgICAgICAndGl0bGUnOiBkcml2ZXIudGl0bGUsXFxuICAgICAgICAgICAgICAgIH1cXG5cXG4gICAgICAgICAgICAgICAgIyBTdG9yZSB0aGUgZXh0cmFjdGVkIGRhdGEgdG8gdGhlIGRlZmF1bHQgZGF0YXNldC5cXG4gICAgICAgICAgICAgICAgYXdhaXQgQWN0b3IucHVzaF9kYXRhKGRhdGEpXFxuXFxuICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjpcXG4gICAgICAgICAgICAgICAgQWN0b3IubG9nLmV4Y2VwdGlvbihmJ0Nhbm5vdCBleHRyYWN0IGRhdGEgZnJvbSB7dXJsfS4nKVxcblxcbiAgICAgICAgICAgIGZpbmFsbHk6XFxuICAgICAgICAgICAgICAgICMgTWFyayB0aGUgcmVxdWVzdCBhcyBoYW5kbGVkIHRvIGVuc3VyZSBpdCBpcyBub3QgcHJvY2Vzc2VkIGFnYWluLlxcbiAgICAgICAgICAgICAgICBhd2FpdCByZXF1ZXN0X3F1ZXVlLm1hcmtfcmVxdWVzdF9hc19oYW5kbGVkKHJlcXVlc3QpXFxuXFxuICAgICAgICBkcml2ZXIucXVpdCgpXFxuXFxuXFxuaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzpcXG4gICAgYXN5bmNpby5ydW4obWFpbigpKVxcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjEwMjQsInRpbWVvdXQiOjE4MH19.bukUGO8-9Qj8lp2IIeibm-Md5iXNJIiJIMyDqq_wh6g\&asrc=run_on_apify)

```
import asyncio
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

from apify import Actor, Request

# To run this Actor locally, you need to have the Selenium Chromedriver installed.
# Follow the installation guide at:
# https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
# When running on the Apify platform, the Chromedriver is already included
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

        # Launch a new Selenium Chrome WebDriver and configure it.
        Actor.log.info('Launching Chrome WebDriver...')
        chrome_options = ChromeOptions()

        if Actor.configuration.headless:
            chrome_options.add_argument('--headless')

        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=chrome_options)

        # Test WebDriver setup by navigating to an example page.
        driver.get('http://www.example.com')
        if driver.title != 'Example Domain':
            raise ValueError('Failed to open example page.')

        # Process the URLs from the request queue.
        while request := await request_queue.fetch_next_request():
            url = request.url

            if not isinstance(request.user_data['depth'], (str, int)):
                raise TypeError('Request.depth is an unexpected type.')

            depth = int(request.user_data['depth'])
            Actor.log.info(f'Scraping {url} (depth={depth}) ...')

            try:
                # Navigate to the URL using Selenium WebDriver. Use asyncio.to_thread
                # for non-blocking execution.
                await asyncio.to_thread(driver.get, url)

                # If the current depth is less than max_depth, find nested links
                # and enqueue them.
                if depth < max_depth:
                    for link in driver.find_elements(By.TAG_NAME, 'a'):
                        link_href = link.get_attribute('href')
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
                    'title': driver.title,
                }

                # Store the extracted data to the default dataset.
                await Actor.push_data(data)

            except Exception:
                Actor.log.exception(f'Cannot extract data from {url}.')

            finally:
                # Mark the request as handled to ensure it is not processed again.
                await request_queue.mark_request_as_handled(request)

        driver.quit()


if __name__ == '__main__':
    asyncio.run(main())
```

## Conclusion[](#conclusion)

In this guide you learned how to use Selenium for web scraping in Apify Actors. You can now create your own Actors that use Selenium to scrape dynamic websites and interact with web pages just like a human would. See the [Actor templates](https://apify.com/templates/categories/python) to get started with your own scraping tasks. If you have questions or need assistance, feel free to reach out on our [GitHub](https://github.com/apify/apify-sdk-python) or join our [Discord community](https://discord.com/invite/jyEM2PRvMU). Happy scraping!
