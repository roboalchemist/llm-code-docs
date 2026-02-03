# Source: https://docs.apify.com/sdk.md



https://docs.apify.com

[Academy](https://docs.apify.com/academy)[Platform](https://docs.apify.com/platform)

[API](https://docs.apify.com/api)

* [Reference](https://docs.apify.com/api/v2)
* [Client for JavaScript](https://docs.apify.com/api/client/js/)
* [Client for Python](https://docs.apify.com/api/client/python/)

[SDK](https://docs.apify.com/sdk)

* [SDK for JavaScript](https://docs.apify.com/sdk/js/)
* [SDK for Python](https://docs.apify.com/sdk/python/)

[CLI](https://docs.apify.com/cli/)

[Open source](https://docs.apify.com/open-source)

* [Crawlee](https://crawlee.dev)
* [Fingerprint Suite](https://github.com/apify/fingerprint-suite)
* [impit](https://github.com/apify/impit)
* [MCP CLI](https://github.com/apify/mcp-cli)
* [Actor whitepaper](https://whitepaper.actor)
* [proxy-chain](https://github.com/apify/proxy-chain)
* [Apify on GitHub](https://github.com/apify)

[Chat on Discord](https://discord.com/invite/jyEM2PRvMU)[Go to Console](https://console.apify.com)

# Apify SDK

The Apify SDK is a toolkit for building Actors—serverless microservices running on the Apify platform. Apify comes with first-class support for JavaScript/TypeScript and Python, but you can run any containerized code as Actors.

![](/img/javascript-40x40.svg)![](/img/javascript-40x40.svg)

## Apify SDK for JavaScript

The official library for creating Apify Actors in Python, with full lifecycle management, local storage, and event handling.

[Star](https://github.com/apify/apify-sdk-js)

[Get started](https://docs.apify.com/sdk/js/docs/guides/apify-platform)[View reference](https://docs.apify.com/sdk/js/reference)


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

## Apify SDK for Python

The official library for creating Apify Actors in Python, with full lifecycle management, local storage, and event handling.

[Star](https://github.com/apify/apify-sdk-python)

[Get started](https://docs.apify.com/sdk/python/docs/overview)[View reference](https://docs.apify.com/sdk/python/reference)


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

* [Academy](https://docs.apify.com/academy)
* [Platform](https://docs.apify.com/platform)

API

* [Reference](https://docs.apify.com/api/v2)
* [Client for JavaScript](https://docs.apify.com/api/client/js/)
* [Client for Python](https://docs.apify.com/api/client/python/)

SDK

* [SDK for JavaScript](https://docs.apify.com/sdk/js/)
* [SDK for Python](https://docs.apify.com/sdk/python/)

Other

* [CLI](https://docs.apify.com/cli/)
* [Open source](https://docs.apify.com/open-source)

More

* [Crawlee](https://crawlee.dev)
* [GitHub](https://github.com/apify)
* [Discord](https://discord.com/invite/jyEM2PRvMU)
* [Trust Center](https://trust.apify.com)

https://apify.com
