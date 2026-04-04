# Source: https://docs.apify.com/platform/integrations/api.md

# Source: https://docs.apify.com/academy/api.md

# Source: https://docs.apify.com/api.md



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

# Apify API documentation

Learn how to use the [Apify platform](https://docs.apify.com/platform.md) programmatically.

## REST API

The Apify API is built around HTTP REST, uses predictable resource-oriented URLs, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

[View API reference](https://docs.apify.com/api/v2.md)

cURL


```
# Prepare Actor input and run it synchronously
echo '{ "searchStringsArray": ["Apify"] }' |
curl -X POST -d @- \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_API_TOKEN>' \
  -L 'https://api.apify.com/v2/acts/compass~crawler-google-places/run-sync-get-dataset-items'
```


## API clients

The client libraries are a more convenient way to interact with the Apify platform than the HTTP REST API.

##### ![](/img/javascript-40x40.svg)![](/img/javascript-40x40.svg)JavaScript

##### ![](/img/python-40x40.svg)![](/img/python-40x40.svg)Python

### JavaScript API client

For web browser, JavaScript/TypeScript applications, Node.js, Deno, or Bun.[Star](https://github.com/apify/apify-client-js)

[Get started](https://docs.apify.com/api/client/js/docs)[View reference](https://docs.apify.com/api/client/js/reference)


```
npm install apify-client
```



```
// Easily run Actors, await them to finish using the convenient .call() method, and retrieve results from the resulting dataset.
const { ApifyClient } = require('apify-client');

const client = new ApifyClient({
    token: 'MY-APIFY-TOKEN',
});

// Starts an actor and waits for it to finish.
const { defaultDatasetId } = await client.actor('john-doe/my-cool-actor').call();

// Fetches results from the actor's dataset.
const { items } = await client.dataset(defaultDatasetId).listItems();
```


## Related articles

https://blog.apify.com/web-scraping-with-client-side-vanilla-javascript/

[Web scraping with client-side Vanilla JavaScript](https://blog.apify.com/web-scraping-with-client-side-vanilla-javascript/)

[Read more](https://blog.apify.com/web-scraping-with-client-side-vanilla-javascript/)

https://blog.apify.com/apify-python-api-client/

[Apify ❤️ Python, so we’re releasing a Python API client](https://blog.apify.com/apify-python-api-client/)

[Read more](https://blog.apify.com/apify-python-api-client/)

https://blog.apify.com/api-for-dummies/

[API for dummies](https://blog.apify.com/api-for-dummies/)

[Read more](https://blog.apify.com/api-for-dummies/)

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
