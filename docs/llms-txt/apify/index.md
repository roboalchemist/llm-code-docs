# Source: https://docs.apify.com/cli/index.md

# Source: https://docs.apify.com/sdk/python/index.md

# Source: https://docs.apify.com/sdk/js/index.md

# Source: https://docs.apify.com/api/client/python/index.md

# Source: https://docs.apify.com/api/client/js/index.md

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![](/api/client/js/img/apify_sdk.svg)![](/api/client/js/img/apify_sdk_white.svg)](https://docs.apify.com)

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
* [Got Scraping](https://github.com/apify/got-scraping)
* [Fingerprint Suite](https://github.com/apify/fingerprint-suite)
* [Apify on GitHub](https://github.com/apify)
* [Actor whitepaper](https://whitepaper.actor)

[Discord](https://discord.com/invite/jyEM2PRvMU "Chat on Discord")[Go to Console](https://console.apify.com)

[API client for JavaScript](https://docs.apify.com/api/client/js/api/client/js/.md)

[Docs](https://docs.apify.com/api/client/js/api/client/js/docs.md)[Reference](https://docs.apify.com/api/client/js/api/client/js/reference.md)[Changelog](https://docs.apify.com/api/client/js/api/client/js/docs/changelog.md)[GitHub](https://github.com/apify/apify-client-js)

[2.19.1](https://docs.apify.com/api/client/js/api/client/js/docs.md)

* [Next](https://docs.apify.com/api/client/js/api/client/js/docs/next)
* [2.19.1](https://docs.apify.com/api/client/js/api/client/js/docs.md)

# Apify API client for JavaScript

# Apify API client for JavaScript

##

## The official library to interact with Apify API from a web browser, Node.js, JavaScript, or TypeScript applications, providing convenience functions and automatic retries on errors.

[Get Started](https://docs.apify.com/api/client/js/api/client/js/docs.md)[GitHub](https://ghbtns.com/github-btn.html?user=apify\&repo=apify-client-js\&type=star\&count=true\&size=large)

![](/api/client/js/assets/images/logo-blur-5206054b91a93d20690b49e1aeb1f62e.png)

```
npm install apify-client
```

Easily run Actors, await them to finish using the convenient `.call()` <!-- -->method, and retrieve results from the resulting dataset.

```
const { ApifyClient } = require('apify-client');

const client = new ApifyClient({
    token: 'MY-APIFY-TOKEN',
});

// Starts an actor and waits for it to finish.
const { defaultDatasetId } = await client.actor('john-doe/my-cool-actor').call();

// Fetches results from the actor's dataset.
const { items } = await client.dataset(defaultDatasetId).listItems();
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

[](https://apify.com)
