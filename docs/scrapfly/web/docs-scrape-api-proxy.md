# Source: https://scrapfly.io/docs/scrape-api/proxy

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/proxy

Markdown Content:
Proxy
-----

Proxies are at the core of every modern web scraper as they allow traffic distribution through multiple connection agents. In other words, proxies in web scraping allow to:

*   Change origin country to access geographically locked content.
*   Bypass scraper blocking and anti-bot detection solutions.
*   Bypass scraper throttling.

All Scrapfly requests go through proxies and are automatically configured for the best scraping experience. However, each scrapfly API call can be additionally configured manually via [proxy_pool](https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxy_pool) and [country](https://scrapfly.io/docs/scrape-api/getting-started#api_param_country) parameters.

[See Your Proxy Dashboard](https://scrapfly.io/dashboard/proxy/scraper-api)

[What are Proxies?](https://scrapfly.io/docs/scrape-api/proxy#what)
-------------------------------------------------------------------

Each address is associated with an Autonomous System Number ([ASN](https://en.wikipedia.org/wiki/Autonomous_system_(Internet))) and linked to a proxy. This is how anti-bot solutions track the origin of the IP and limit requests per IP. Our proxy pool rotates IPs, cools them down, and excludes underperforming proxies to increase success rates. We offer two public proxy pools by default, with the option to set up a custom pool. We manage and monitor our proxy pool for optimal performance, with both datacenter and residential proxies available.

Different kind of proxies exists, by types of IP address issuer:

*   **Datacenter**: Cheap but are detected by advanced anti-bot solutions.
*   **Residential**: More expensive than **datacenter** and often required to bypass most anti-bot solutions.

### [Why are Proxies Needed?](https://scrapfly.io/docs/scrape-api/proxy#why)

Anti-bot solutions rate-limit the number of requests per connecting [IP address](https://en.wikipedia.org/wiki/IP_address). Meaning, to scrape more than a page or two scrapers need to distribute traffic through multiple IP addresses. This limit is why we need to manage the proxy pool, rotate IPs, and cool them to increase the success rate.

[Available Proxy Pools](https://scrapfly.io/docs/scrape-api/proxy#proxy-pools)
------------------------------------------------------------------------------

A proxy pool represents a group of proxies. By default, proxies are grouped by network type like **datacenter**, **residential**, **4g** etc. One of the main challenges with proxies is the reliability, it's complex to maintain a network of healthy proxies and routing the traffic to them. You don't have to manage proxies yourself - simply select a proxy pool and we'll route the traffic using a healthy proxy meeting your requirements.

All available proxy pools are listed in the [proxy section on your dashboard](https://scrapfly.io/dashboard/proxy/scraper-api). Each proxy pool has its own cost (mostly due to network type). By default, these public pools are available:

*   **Public Datacenter Pool**: `public_datacenter_pool` - 1 API Credits will be counted 
*   **Public Residential Pool**: `public_residential_pool` - 25 API Credits will be counted 

For example, to use residential proxies configure requests with the `proxy_pool=public_residential_pool` parameter:

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "proxy_pool=public_residential_pool" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://httpbin.dev/anything"
```

`https://api.scrapfly.io/scrape?proxy_pool=public_residential_pool&key=&url=https%3A%2F%2Fhttpbin.dev%2Fanything`

[Geo Targeting](https://scrapfly.io/docs/scrape-api/proxy#geo)
--------------------------------------------------------------

All Scrapfly scrape requests go through a proxy meaning geo-targeting is available at all times. By default, Scrapfly will smartly select a random proxy from the selected pool for the highest success probability.

To set the desired country, the [country](https://scrapfly.io/docs/scrape-api/getting-started#api_param_country) parameter can be used, and the available country options depend on the selected [proxy_pool](https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxy_pool):

*   [Public Datacenter Pool](https://scrapfly.io/docs/scrape-api/proxy#public_datacenter_pool)
*   [Public Residential Pool](https://scrapfly.io/docs/scrape-api/proxy#public_residential_pool)

**API Pool Name:**`public_datacenter_pool`

*    United Arab Emirates : `ae`
*    Albania : `al`
*    Armenia : `am`
*    Argentina : `ar`
*    Austria : `at`
*    Australia : `au`
*    Bangladesh : `bd`
*    Belgium : `be`
*    Bulgaria : `bg`
*    Bolivia : `bo`
*    Brazil : `br`
*    Bahamas : `bs`
*    Belarus : `by`
*    Canada : `ca`
*    Switzerland : `ch`
*    Chile : `cl`
*    China : `cn`
*    Colombia : `co`
*    Costa Rica : `cr`
*    Cyprus : `cy`
*    Czechia : `cz`
*    Germany : `de`
*    Denmark : `dk`
*    Ecuador : `ec`
*    Estonia : `ee`
*    Egypt : `eg`
*    Spain : `es`
*    Finland : `fi`
*    France : `fr`
*    United Kingdom : `gb`
*    Georgia : `ge`
*    Greece : `gr`
*    Hong Kong SAR China : `hk`
*    Honduras : `hn`
*    Croatia : `hr`
*    Hungary : `hu`
*    Indonesia : `id`
*    Ireland : `ie`
*    Israel : `il`
*    India : `in`
*    Iraq : `iq`
*    Iceland : `is`
*    Italy : `it`
*    Jamaica : `jm`
*    Jordan : `jo`
*    Japan : `jp`
*    Cambodia : `kh`
*    South Korea : `kr`
*    Lithuania : `lt`
*    Latvia : `lv`
*    Morocco : `ma`
*    Moldova : `md`
*    Madagascar : `mg`
*    Mongolia : `mn`
*    Mexico : `mx`
*    Malaysia : `my`
*    Nigeria : `ng`
*    Netherlands : `nl`
*    Norway : `no`
*    New Zealand : `nz`
*    Panama : `pa`
*    Peru : `pe`
*    Philippines : `ph`
*    Pakistan : `pk`
*    Poland : `pl`
*    Portugal : `pt`
*    Romania : `ro`
*    Russia : `ru`
*    Saudi Arabia : `sa`
*    Sweden : `se`
*    Singapore : `sg`
*    Slovakia : `sk`
*    Thailand : `th`
*    Turkmenistan : `tm`
*    Tunisia : `tn`
*    Türkiye : `tr`
*    Taiwan : `tw`
*    Ukraine : `ua`
*    United States : `us`
*    Uzbekistan : `uz`
*    Venezuela : `ve`
*    British Virgin Islands : `vg`
*    Vietnam : `vn`
*    South Africa : `za`

**API Pool Name:**`public_residential_pool`

*    United Arab Emirates : `ae`
*    Albania : `al`
*    Armenia : `am`
*    Argentina : `ar`
*    Austria : `at`
*    Australia : `au`
*    Bangladesh : `bd`
*    Belgium : `be`
*    Bulgaria : `bg`
*    Bolivia : `bo`
*    Brazil : `br`
*    Bahamas : `bs`
*    Belarus : `by`
*    Canada : `ca`
*    Switzerland : `ch`
*    Chile : `cl`
*    China : `cn`
*    Colombia : `co`
*    Costa Rica : `cr`
*    Cyprus : `cy`
*    Czechia : `cz`
*    Germany : `de`
*    Denmark : `dk`
*    Ecuador : `ec`
*    Estonia : `ee`
*    Egypt : `eg`
*    Spain : `es`
*    Finland : `fi`
*    France : `fr`
*    United Kingdom : `gb`
*    Georgia : `ge`
*    Greece : `gr`
*    Hong Kong SAR China : `hk`
*    Honduras : `hn`
*    Croatia : `hr`
*    Hungary : `hu`
*    Indonesia : `id`
*    Ireland : `ie`
*    Israel : `il`
*    India : `in`
*    Iraq : `iq`
*    Iceland : `is`
*    Italy : `it`
*    Jamaica : `jm`
*    Jordan : `jo`
*    Japan : `jp`
*    Cambodia : `kh`
*    South Korea : `kr`
*    Lithuania : `lt`
*    Latvia : `lv`
*    Morocco : `ma`
*    Moldova : `md`
*    Madagascar : `mg`
*    Mongolia : `mn`
*    Mexico : `mx`
*    Malaysia : `my`
*    Nigeria : `ng`
*    Netherlands : `nl`
*    Norway : `no`
*    New Zealand : `nz`
*    Panama : `pa`
*    Peru : `pe`
*    Philippines : `ph`
*    Pakistan : `pk`
*    Poland : `pl`
*    Portugal : `pt`
*    Romania : `ro`
*    Russia : `ru`
*    Saudi Arabia : `sa`
*    Sweden : `se`
*    Singapore : `sg`
*    Slovakia : `sk`
*    Thailand : `th`
*    Turkmenistan : `tm`
*    Tunisia : `tn`
*    Türkiye : `tr`
*    Taiwan : `tw`
*    Ukraine : `ua`
*    United States : `us`
*    Uzbekistan : `uz`
*    Venezuela : `ve`
*    British Virgin Islands : `vg`
*    Vietnam : `vn`
*    South Africa : `za`

For example, to target Canada configure requests with the `country=CA` parameter:

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "country=ca" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://httpbin.dev/anything"
```

`https://api.scrapfly.io/scrape?country=ca&key=&url=https%3A%2F%2Fhttpbin.dev%2Fanything`

_You can also declare multiple country `ca,us` and you can also exclude some `-mx,-au`. To know more, you can check the [API parameters country](https://scrapfly.io/docs/scrape-api/getting-started#api\_param\_country) section._

All related errors are listed below. You can see full description and example of error response on [Errors section](https://scrapfly.io/docs/scrape-api/errors#proxy)

*   [ERR::PROXY::POOL_NOT_AVAILABLE_FOR_TARGET](https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::POOL_NOT_AVAILABLE_FOR_TARGET) - The desired proxy pool is not available for the given domain - mostly well known protected domain which require at least residential networks
*   [ERR::PROXY::POOL_NOT_FOUND](https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::POOL_NOT_FOUND) - Provided Proxy Pool Name do not exists
*   [ERR::PROXY::POOL_UNAVAILABLE_COUNTRY](https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::POOL_UNAVAILABLE_COUNTRY) - Country not available for given proxy pool
*   [ERR::PROXY::RESOURCES_SATURATION](https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::RESOURCES_SATURATION) - Proxy are saturated for the desired country, you can try on other countries. They will come back as soon as possible
*   [ERR::PROXY::TIMEOUT](https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::TIMEOUT) - Proxy connection or website was too slow and timeout
*   [ERR::PROXY::UNAVAILABLE](https://scrapfly.io/docs/scrape-api/error/ERR::PROXY::UNAVAILABLE) - Proxy is unavailable - The domain (mainly gov website) is restricted, You are using session feature and the proxy is unreachable at the moment

[Pricing](https://scrapfly.io/docs/scrape-api/proxy#pricing)
------------------------------------------------------------

Each call using the residential proxy pool will count for 25 Scrape API Credits. API responses contain a header `X-Scrapfly-Api-Cost` which indicate the total billed amount.
