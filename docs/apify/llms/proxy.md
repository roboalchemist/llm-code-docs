# Source: https://docs.apify.com/platform/proxy.md

# Proxy

**Learn to anonymously access websites in scraping/automation jobs. Improve data outputs and efficiency of bots, and access websites from various geographies.**

***

> [Apify Proxy](https://apify.com/proxy) allows you to change your IP address when web scraping to reduce the chance of being [blocked](https://docs.apify.com/academy/anti-scraping/techniques.md) because of your geographical location.

You can use proxies in your [Actors](https://docs.apify.com/platform/actors.md) or any other application that supports HTTP proxies. Apify Proxy monitors the health of your IP pool and intelligently rotates addresses to prevent IP address-based blocking.

You can view your proxy settings and password on the [Proxy](https://console.apify.com/proxy) page in Apify Console. For pricing information, visit [apify.com/pricing](https://apify.com/pricing).

## Quickstart

Usage of Apify Proxy means just a couple of lines of code, thanks to our [SDKs](https://docs.apify.com/sdk.md):

* JavaScript SDK with PuppeteerCrawler
* Python SDK with requests


```
import { Actor } from 'apify';
import { PuppeteerCrawler } from 'crawlee';

await Actor.init();

const proxyConfiguration = await Actor.createProxyConfiguration();

const crawler = new PuppeteerCrawler({
    proxyConfiguration,
    async requestHandler({ page }) {
        console.log(await page.content());
    },
});

await crawler.run(['https://proxy.apify.com/?format=json']);

await Actor.exit();
```



```
import requests, asyncio
from apify import Actor

async def main():
    async with Actor:
        proxy_configuration = await Actor.create_proxy_configuration()
        proxy_url = await proxy_configuration.new_url()

        proxies = {
            'http': proxy_url,
            'https': proxy_url,
        }

        response = requests.get('https://api.apify.com/v2/browser-info', proxies=proxies)
        print(response.text)

if __name__ == '__main__':
    asyncio.run(main())
```


## Proxy types

Several types of proxy servers exist, each offering distinct advantages, disadvantages, and varying pricing structures. You can use them to access websites from various geographies and with different levels of anonymity.

#### [Datacenter proxy](https://docs.apify.com/platform/proxy/datacenter-proxy.md)

[The fastest and cheapest option. It uses datacenters to change your IP address. Note that there is a chance of being blocked because of the activity of other users.](https://docs.apify.com/platform/proxy/datacenter-proxy.md)

#### [Residential proxy](https://docs.apify.com/platform/proxy/residential-proxy.md)

[IP addresses located in homes and offices around the world. These IPs are the least likely to be blocked.](https://docs.apify.com/platform/proxy/residential-proxy.md)

#### [Google SERP proxy](https://docs.apify.com/platform/proxy/google-serp-proxy.md)

[Download and extract data from Google Search Engine Result Pages (SERPs). You can select country and language to get localized results.](https://docs.apify.com/platform/proxy/google-serp-proxy.md)
