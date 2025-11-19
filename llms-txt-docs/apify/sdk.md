# Source: https://docs.apify.com/sdk.md



https://docs.apify.com

https://docs.apify.com/academyhttps://docs.apify.com/platform

https://docs.apify.com/api

* https://docs.apify.com/api/v2
* https://docs.apify.com/api/client/js/
* https://docs.apify.com/api/client/python/

https://docs.apify.com/sdk

* https://docs.apify.com/sdk/js/
* https://docs.apify.com/sdk/python/

https://docs.apify.com/cli/

https://docs.apify.com/open-source

* https://crawlee.dev
* https://github.com/apify/got-scraping
* https://github.com/apify/fingerprint-suite
* https://github.com/apify
* https://whitepaper.actor

[Chat on Discord](https://discord.com/invite/jyEM2PRvMU)https://console.apify.com

# Apify SDK

The Apify SDK is a toolkit for building Actors—serverless microservices running (not only) on the Apify platform. Apify comes with first-class support for JavaScript/TypeScript and Python, but you can run any containerized code on the Apify platform.

![](/img/javascript-40x40.svg)![](/img/javascript-40x40.svg)

## SDK for JavaScript

Toolkit for building Actors—serverless microservices running (not only) on the Apify platform.

https://github.com/apify/apify-sdk-js

https://docs.apify.com/sdk/js/docs/guides/apify-platformhttps://docs.apify.com/sdk/js/reference


```
npx apify-cli create my-crawler
```



```
// The Apify SDK makes it easy to initialize the actor on the platform with the Actor.init() method,
// and to save the scraped data from your Actors to a dataset by simply using the Actor.pushData() method.

import { Actor } from 'apify';
import { PlaywrightCrawler } from 'crawlee';

await Actor.init();
const crawler = new PlaywrightCrawler({
    async requestHandler({ request, page, enqueueLinks }) {
        const title = await page.title();
        console.log(`Title of ${request.loadedUrl} is '${title}'`);
        await Actor.pushData({ title, url: request.loadedUrl });
        await enqueueLinks();
    }
});
await crawler.run(['https://crawlee.dev']);
await Actor.exit();
```


![](/img/python-40x40.svg)![](/img/python-40x40.svg)

## SDK for Python

The Apify SDK for Python is the official library for creating Apify Actors in Python. It provides useful features like actor lifecycle management, local storage emulation, and actor event handling.

https://github.com/apify/apify-sdk-python

https://docs.apify.com/sdk/python/docs/overview/introductionhttps://docs.apify.com/sdk/python/reference


```
apify create my-python-actor
```



```
# The Apify SDK makes it easy to read the actor input with the Actor.get_input() method,
# and to save the scraped data from your Actors to a dataset by simply using the Actor.push_data() method.

from apify import Actor
from bs4 import BeautifulSoup
import requests

async def main():
    async with Actor:
        actor_input = await Actor.get_input()
        response = requests.get(actor_input['url'])
        soup = BeautifulSoup(response.content, 'html.parser')
        await Actor.push_data({ 'url': actor_input['url'], 'title': soup.title.string })
```


Learn

* https://docs.apify.com/academy
* https://docs.apify.com/platform

API

* https://docs.apify.com/api/v2
* https://docs.apify.com/api/client/js/
* https://docs.apify.com/api/client/python/

SDK

* https://docs.apify.com/sdk/js/
* https://docs.apify.com/sdk/python/

Other

* https://docs.apify.com/cli/
* https://docs.apify.com/open-source

More

* https://crawlee.dev
* https://github.com/apify
* https://discord.com/invite/jyEM2PRvMU
* https://trust.apify.com

https://apify.com
