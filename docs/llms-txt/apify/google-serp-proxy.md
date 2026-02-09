# Source: https://docs.apify.com/platform/proxy/google-serp-proxy.md

# Google SERP proxy

**Learn how to collect search results from Google Search-powered tools. Get search results from localized domains in multiple countries, e.g. the US and Germany.**

***

Google SERP proxy allows you to extract search results from Google Search-powered services. It allows searching in  and to dynamically switch between country domains.

Our Google SERP proxy currently supports the below services.

* Google Search (`http://www.google.<country domain>/search`).
* Google Shopping (`http://www.google.<country domain>/shopping/product/<product ID>`).
* Google Shopping Search (`http://www.google.<country domain>/search?tbm=shop`).

> Google SERP proxy can **only** be used for Google Search and Shopping. It cannot be used to access other websites.

When using the proxy, **pricing is based on the number of requests made**.

## Connecting to Google SERP proxy

Requests made through the proxy are automatically routed through a proxy server from the selected country and pure **HTML code of the search result page is returned**.

**Important:** Only HTTP requests are allowed, and the Google hostname needs to start with the `www.` prefix.

For code examples on how to connect to Google SERP proxies, see the  section.

### Username parameters

The `username` field enables you to pass various [parameters](https://docs.apify.com/platform/proxy/usage.md#username-parameters), such as groups and country, for your proxy connection.

When using Google SERP proxy, the username should always be:


```
groups-GOOGLE_SERP
```


Unlike [datacenter](https://docs.apify.com/platform/proxy/datacenter-proxy.md) or [residential](https://docs.apify.com/platform/proxy/residential-proxy.md) proxies, there is no [session](https://docs.apify.com/platform/proxy/usage.md#sessions) parameter.

If you use the `country` [parameter](https://docs.apify.com/platform/proxy/usage.md), the Google proxy location is used if you access a website whose hostname (stripped of `www.`) starts with **google**.

## Country selection

You must use the correct Google domain to get results for your desired country code.

For example:

* Search results from the USA: `http://www.google.com/search?q=<query>`

* Shopping results from Great Britain: `http://www.google.co.uk/seach?tbm=shop&q=<query>`

See a [full list](https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/List_of_Google_domains.html) of available domain names for specific countries. When using them, remember to prepend the domain name with the `www.` prefix.

## Examples

### Using the Apify SDK

If you are developing your own Apify [Actor](https://docs.apify.com/platform/actors.md) using the [Apify SDK](https://docs.apify.com/sdk.md) and [Crawlee](https://crawlee.dev/), the most efficient way to use Google SERP proxy is [CheerioCrawler](https://crawlee.dev/api/cheerio-crawler/class/CheerioCrawler). This is because Google SERP proxy [only returns a page's HTML](https://docs.apify.com/platform/proxy.md). Alternatively, you can use the [got-scraping](https://github.com/apify/got-scraping) [npm package](https://www.npmjs.com/package/got-scraping) by specifying the proxy URL in the options. For Python, you can leverage the [requests](https://pypi.org/project/requests/) library along with the Apify SDK.

The following examples get a list of search results for the keyword **wikipedia** from the USA (`google.com`).

* CheerioCrawler
* Python SDK with requests
* gotScraping()


```
import { Actor } from 'apify';
import { CheerioCrawler } from 'crawlee';

await Actor.init();

const proxyConfiguration = await Actor.createProxyConfiguration({
    groups: ['GOOGLE_SERP'],
});

const crawler = new CheerioCrawler({
    proxyConfiguration,
    async requestHandler({ body }) {
        // ...
        console.log(body);
    },
});

await crawler.run(['http://www.google.com/search?q=wikipedia']);

await Actor.exit();
```



```
from apify import Actor
import requests, asyncio

async def main():
    async with Actor:
        proxy_configuration = await Actor.create_proxy_configuration(groups=['GOOGLE_SERP'])
        proxy_url = await proxy_configuration.new_url()
        proxies = {
            'http': proxy_url,
            'https': proxy_url,
        }

        response = requests.get('http://www.google.com/search?q=wikipedia', proxies=proxies)
        print(response.text)

if __name__ == '__main__':
    asyncio.run(main())
```



```
import { Actor } from 'apify';
import { gotScraping } from 'got-scraping';

await Actor.init();

const proxyConfiguration = await Actor.createProxyConfiguration({
    groups: ['GOOGLE_SERP'],
});
const proxyUrl = await proxyConfiguration.newUrl();

const { body } = await gotScraping({
    url: 'http://www.google.com/search?q=wikipedia',
    proxyUrl,
});

console.log(body);

await Actor.exit();
```


### Using standard libraries and languages

You can find your proxy password on the [Proxy page](https://console.apify.com/proxy/access) of Apify Console.

> The `username` field is **not** your Apify username.<br />Instead, you specify proxy settings (e.g. `groups-GOOGLE_SERP`).<br />Use `groups-GOOGLE_SERP` to use proxies from all available countries.

For examples using [PHP](https://www.php.net/), you need to have the [cURL](https://www.php.net/manual/en/book.curl.php) extension enabled in your PHP installation. See [installation instructions](https://www.php.net/manual/en/curl.installation.php) for more information.

Examples in [Python 2](https://www.python.org/download/releases/2.0/) use the [six](https://pypi.org/project/six/) library. Run `pip install six` to enable it.

The following examples get the HTML of search results for the keyword **wikipedia** from the USA (**google.com**).

Select this option by setting the `username` parameter to `groups-GOOGLE_SERP`. Add the item you want to search to the `query` parameter.

* Node.js (axios)
* Python 3
* Python 2
* PHP
* PHP (Guzzle)


```
import axios from 'axios';

const proxy = {
    protocol: 'http',
    host: 'proxy.apify.com',
    port: 8000,
    // Replace <YOUR_PROXY_PASSWORD> below with your password
    // found at https://console.apify.com/proxy
    auth: { username: 'groups-GOOGLE_SERP', password: '<YOUR_PROXY_PASSWORD>' },
};

const url = 'http://www.google.com/search';
const params = { q: 'wikipedia' };

const { data } = await axios.get(url, { proxy, params });

console.log(data);
```



```
import urllib.request as request
import urllib.parse as parse

# Replace <YOUR_PROXY_PASSWORD> below with your password
# found at https://console.apify.com/proxy
password = '<YOUR_PROXY_PASSWORD>'
proxy_url = f"http://groups-GOOGLE_SERP:{password}@proxy.apify.com:8000"

proxy_handler = request.ProxyHandler({
    'http': proxy_url,
})

opener = request.build_opener(proxy_handler)

query = parse.urlencode({ 'q': 'wikipedia' })
print(opener.open(f"http://www.google.com/search?{query}").read())
```



```
import six
from six.moves.urllib import request, urlencode

# Replace <YOUR_PROXY_PASSWORD> below with your password
# found at https://console.apify.com/proxy
password = '<YOUR_PROXY_PASSWORD>'
proxy_url = (
    'http://groups-GOOGLE_SERP:%s@proxy.apify.com:8000' %
    (password)
)
proxy_handler = request.ProxyHandler({
    'http': proxy_url,
})
opener = request.build_opener(proxy_handler)
query = parse.urlencode({ 'q': 'wikipedia' })
url = (
    'http://www.google.com/search?%s' %
    (query)
)
print(opener.open(url).read())
```



```
<?php
$query = urlencode('wikipedia');
$curl = curl_init('http://www.google.com/search?q=' . $query);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($curl, CURLOPT_PROXY, 'http://proxy.apify.com:8000');
// Replace <YOUR_PROXY_PASSWORD> below with your password
// found at https://console.apify.com/proxy
curl_setopt($curl, CURLOPT_PROXYUSERPWD, 'groups-GOOGLE_SERP:<YOUR_PROXY_PASSWORD>');
$response = curl_exec($curl);
curl_close($curl);
echo $response;
?>
```



```
<?php
require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client([
    // Replace <YOUR_PROXY_PASSWORD> below with your password
    // found at https://console.apify.com/proxy
    'proxy' => 'http://groups-GOOGLE_SERP:<YOUR_PROXY_PASSWORD>@proxy.apify.com:8000'
]);

$response = $client->get("http://www.google.com/search", [
    'query' => ['q' => 'wikipedia']
]);
echo $response->getBody();
```
