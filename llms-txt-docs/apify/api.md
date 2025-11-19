# Source: https://docs.apify.com/platform/integrations/api.md

# Source: https://docs.apify.com/academy/api.md

# Source: https://docs.apify.com/api.md



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

# Apify API

Apify API provides programmatic access to the https://docs.apify.com/

## API reference

The Apify API allows developers to interact programmatically with apps using HTTP requests. The Apify API is built around https://en.wikipedia.org/wiki/REST.

The API has predictable resource-oriented URLs, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

https://docs.apify.com/api/v2.md

cURL


```
# Prepare Actor input and run it synchronously
echo '{ "searchStringsArray": ["Apify"] }' |
curl -X POST -d @- \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_API_TOKEN>' \
  -L 'https://api.apify.com/v2/acts/compass~crawler-google-places/run-sync-get-dataset-items'
```


## API client

The official library to interact with Apify API.

##### ![](/img/javascript-40x40.svg)![](/img/javascript-40x40.svg)JavaScript Client

##### ![](/img/python-40x40.svg)![](/img/python-40x40.svg)Python Client

### JavaScript API client

The official library to interact with Apify API from a web browser, Node.js, JavaScript, or Typescript applications.https://github.com/apify/apify-client-js

https://docs.apify.com/api/client/js/docshttps://docs.apify.com/api/client/js/reference


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

https://blog.apify.com/web-scraping-with-client-side-vanilla-javascript/

https://blog.apify.com/web-scraping-with-client-side-vanilla-javascript/

https://blog.apify.com/apify-python-api-client/

https://blog.apify.com/apify-python-api-client/

https://blog.apify.com/apify-python-api-client/

https://blog.apify.com/api-for-dummies/

https://blog.apify.com/api-for-dummies/

https://blog.apify.com/api-for-dummies/

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
