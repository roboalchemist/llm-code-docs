# Source: https://scrapfly.io/docs/scrape-api/custom

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/custom

Markdown Content:
Customize Requests
------------------

All Scrapfly HTTP requests can be customized with custom headers, methods, cookies and other HTTP parameters. Let's take a look at the available options.

[Method](https://scrapfly.io/docs/scrape-api/custom#method)
-----------------------------------------------------------

The scrape requests method is equivalent to the HTTP method used to call the API. For example, calling Scrapfly through `POST` will forward the request as a `POST` request to the upstream website. 

 Available methods are: `GET`, `PUT`, `POST`, `PATCH`, `HEAD`

*   [GET](https://scrapfly.io/docs/scrape-api/custom#get)
*   [POST](https://scrapfly.io/docs/scrape-api/custom#post)
*   [PUT](https://scrapfly.io/docs/scrape-api/custom#put)
*   [PATCH](https://scrapfly.io/docs/scrape-api/custom#patch)
*   [HEAD](https://scrapfly.io/docs/scrape-api/custom#head)

`GET` request is the most common request type used in web scraping. `GET` requests are used for retrieving data from a server without providing any data in the body of the request.

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://httpbin.dev/html"
```

`https://api.scrapfly.io/scrape?key=&url=https%3A%2F%2Fhttpbin.dev%2Fhtml`

`POST` requests are most commonly used to submit forms or documents. This HTTP method usually requires a `body` parameter to be sent with the request which stores the posted data. To indicate the type of posted data the `content-type` header is used and if it is not set explicitly, it'll default to `application/x-www-form-urlencoded` which stands for **urlencoded data**. Another popular alternative is `JSON` and for posting `JSON` data, the `content-type` header has to be specified as `application/json`.

```
curl \
--request "POST" \
--url "https://api.scrapfly.io/scrape?key=__API_KEY__&url=https%3A%2F%2Fhttpbin.dev%2Fpost" \
--data-raw "{\"example\":\"value\"}"
```

`https://api.scrapfly.io/scrape?key=&url=https%3A%2F%2Fhttpbin.dev%2Fpost`

And here's a full example with for posting JSON and configuring the content-type header:

```
curl \
--request "POST" \
--url "https://api.scrapfly.io/scrape?key=__API_KEY__&url=https%3A%2F%2Fhttpbin.dev%2Fpost&headers%5Bcontent-type%5D=application%2Fjson" \
--data-raw "{\"example\":\"value\"}"
```

`https://api.scrapfly.io/scrape?key=&url=https%3A%2F%2Fhttpbin.dev%2Fpost&headers%5Bcontent-type%5D=application%2Fjson`

`PUT` requests are used to submit forms and upload user-created content. When using this method, if `content-type` header is not set explicitly, it'll default to `application/x-www-form-urlencoded` as we assume you send **urlencoded data**. For putting `JSON` data, specify `content-type: application/json` header.

```
curl \
--request "PUT" \
--url "https://api.scrapfly.io/scrape?key=__API_KEY__&url=https%3A%2F%2Fhttpbin.dev%2Fput&headers%5Bcontent-type%5D=application%2Fjson" \
--data-raw "{\"example\":\"value\"}"
```

`PATCH` requests are used to submit forms and update user-created content. When using this method, if `content-type` header is not set explicitly, it'll default to `application/x-www-form-urlencoded` as we assume you send **urlencoded data**. For patching `JSON` data, specify `content-type: application/json` header.

```
curl \
--request "PATCH" \
--url "https://api.scrapfly.io/scrape?key=__API_KEY__&url=https%3A%2F%2Fhttpbin.dev%2Fput&headers%5Bcontent-type%5D=application%2Fjson" \
--data-raw "{\"example\":\"value\"}"
```

`HEAD` requests are used to retrieve page metadata like response headers and status codes without fetching the content. When `HEAD` method is used, headers of the upstream website are directly forwarded to the API response. This means that Scrapfly response headers match the headers of the scraped website.

> **`HEAD` do not follow redirections**, if you want so, you must retrieve the `Location`header and make a new request to that URL. 
> **NOTE:** The URL in location header is not always absolute, it can also be relative. Handle it accordingly.

```
curl \
--head \
--url "https://api.scrapfly.io/scrape?key=__API_KEY__&url=https%3A%2F%2Fhttpbin.dev%2Fhead"
```

Request headers sent by Scrapfly can be customized through the [headers](https://scrapfly.io/docs/scrape-api/getting-started#api_param_headers) parameter. Note that the value of headers must be [urlencoded](https://www.w3schools.com/tags/ref_urlencode.ASP) to prevent any side effects. When in doubt, use Scrapfly's [url encoding web tool](https://scrapfly.io/web-scraping-tools/urlencode "URL encode").

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://httpbin.dev/headers" \
--data-urlencode "headers[foo]=bar"
```

`https://api.scrapfly.io/scrape?key=&url=https%3A%2F%2Fhttpbin.dev%2Fheaders&headers%5Bfoo%5D=bar`

_You can also pass multiple time the same header e.g: `headers[X-foo][0]=bar&headers[X-foo][1]=baz` and the order order and structure will be replicated_

By default, **Scrapfly** handles most default and basic headers to replicate a real web browser so you don't need to set User-Agent or other basic headers manually. You learn more about headers in [this dedicated article](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-headers/)

> When [Anti Scraping Protection](https://scrapfly.io/docs/scrape-api/anti-scraping-protection)is enabled, **headers are fine-tuned**on target you scrape is also done at header level to **maximize your success rate**

Important headers to keep in mind in web scraping context:

#### Content-Type

Specifies the media type of the resource being sent in the HTTP message body. It tells the recipient what kind of data to expect and how to interpret it. The Content-Type header is typically used in HTTP requests and responses, particularly in responses from servers to clients.

Example, sending a `POST` request with a body of `JSON` data, you must specify `application/json`.

By default, if you send a POST request without `Content-Type` header, `application/x-www-form-urlencoded` will be set.

> If this Header is not correctly configured, the target website respond with a `400, 406`or block you

#### Accept

Indicates the media types that the client is willing to receive in the response. Helps servers determine the appropriate representation of the requested resource.

Default mimics a real web browser.

Example for a JSON API expecting a response in JSON: `Accept: application/json`

> If this Header is not correctly configured, the target website respond with a `400`or block you

#### Referer

Indicates the URL of the web page from which the request originated. Often used by servers to track the source of incoming requests.

By default, this header is not sent if not specified

Example: `Referer: https://www.web-scraping.dev/page1.html`

> This header can be mutated while using Anti-Scraping Protection feature

#### Behavior And Interaction With Other Features

When the [ASP is activated](https://scrapfly.io/docs/scrape-api/getting-started#api_param_asp) or a specific [os](https://scrapfly.io/docs/scrape-api/getting-started#api_param_os) is set, following headers become immutable or limited

*   `user-agent`: If you set a custom chrome user agent, it will be ignored to keep our actual version
*   `sec-ch-ua`: Ignored
*   `sec-ch-ua-arch`: Ignored
*   `sec-ch-ua-platform`: Ignored
*   `sec-ch-ua-platform-version`: Ignored
*   `sec-ch-ua-full-version`: Ignored
*   `sec-ch-ua-bitness`: Ignored

With [ASP activated](https://scrapfly.io/docs/scrape-api/getting-started#api_param_asp), referer header is auto handled if no header set. However on specific target you might want to disable this. Setting `referer` header to `none` will prevent it

[Cookies](https://scrapfly.io/docs/scrape-api/custom#cookies)
-------------------------------------------------------------

Cookies are regaular HTTP [headers](https://scrapfly.io/docs/scrape-api/getting-started#api_param_headers) and shouldn't be treated in a special way. While most HTTP clients and libraries have a dedicated API to manage cookies, to manage cookies with Scrapfly API simply set the appropriate headers.

This header should never be sent from the client’s side. It's a response header sent when upstream wants to register a cookie with the client.

This header contains the cookie values held by the client. So, when scraping this should be used to include cookie data. The `Cookie` header contains key-to-value pairs of data separated by semicolons. For example:

*   Single cookie: `Cookie: test=1`
*   Multiple cookie: `Cookie: test=1;lang=fr;currency=USD`

> You can also pass multiple `Cookie`headers to send multiple time the cookie headers Example: `headers[Cookie][0]=foo%3Dbar&headers[Cookie][1]=bar%3Dbaz`
> 
> ```
> Cookie: foo=bar
> Cookie: bar=baz
> ```
> 
> _Note: `%3D` is the [urlencoded](https://scrapfly.io/web-scraping-tools/urlencode) version of `=`, do not forget to [urlencode](https://scrapfly.io/web-scraping-tools/urlencode) the header value to not conflict with the actual url structure. Otherwise inside cookie value `=` would be interpreted as query params of the url._

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://httpbin.dev/cookies" \
--data-urlencode "headers[cookie]=lang=fr;currency=USD;test=1"
```

`https://api.scrapfly.io/scrape?key=&url=https%3A%2F%2Fhttpbin.dev%2Fcookies&headers%5Bcookie%5D=lang%3Dfr%3Bcurrency%3DUSD%3Btest%3D1`

[Geo Targeting](https://scrapfly.io/docs/scrape-api/custom#geo_targeting)
-------------------------------------------------------------------------

Each Scrapfly request can be sent from a specific country. This is called Geo-Targetting and is managed by Scrapfly's proxy network.

The desired country can be specified 2-letter country codes ([ISO 3166-1 alpha-2](https://fr.wikipedia.org/wiki/ISO_3166-1_alpha-2)). Available countries are defined on the [proxy pool](https://scrapfly.io/dashboard/proxy/scraper-api) dashboard. If the country is not available in the **Public Pool** a personal private pool can be created with desired countries. Note that restricting countries also restricts the available proxy IP pool.

To specify geo targetting the [country](https://scrapfly.io/docs/scrape-api/getting-started#api_param_country) parameter can be used:

*   Single country selection: `country=us`
*   Multi country selection with random selection: `country=us,ca,mx`
*   Multi country selection with weighted random selection (higher weights have higher probability): `country=us:1,ca:5,mx:3`
*   Country exclusion: `country=-gb`

For example, to send request through the United States the `country=us` would be used:

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "country=us" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://httpbin.dev/anything"
```

`https://api.scrapfly.io/scrape?country=us&key=&url=https%3A%2F%2Fhttpbin.dev%2Fanything`

> For more on proxies, see the [proxy documentation page](https://scrapfly.io/docs/scrape-api/proxy)

For spoofing the latitude and longitude of web browser's location services, the [geolocation](https://scrapfly.io/docs/scrape-api/getting-started#api_param_geolocation) parameter can be used, for example: `geolocation=48.856614,2.3522219` (latitude, longitude):

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://httpbin.dev/anything"
```

`https://api.scrapfly.io/scrape?key=&url=https%3A%2F%2Fhttpbin.dev%2Fanything`

The available country options depend on the selected [proxy_pool](https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxy_pool). See this table for available options for your account:

[Language](https://scrapfly.io/docs/scrape-api/custom#lang)
-----------------------------------------------------------

Content language can be configured through the [lang](https://scrapfly.io/docs/scrape-api/getting-started#api_param_lang) parameter. By default the language is inferred from the proxy location. So, if proxy of France is used the scrape request will be configured with french language preferences.

Behind the scenes, this is done by configuring the `Accept-Language` HTTP header. If the website supports this header and the requested language, the content will be returned in that language.

Multiple language options can be passed as well by providing multiple comma-separated values. Country locale is also supported in `{lang iso2}-{country iso2}` format. Note that the order matters as the website will negotiate the content language based on this order.

For example, `lang=fr,en-US,en` will result in final header `Accept-Language: fr-{proxy country iso2},fr;q=0.9,en-US;q=0.8,en;q=0.7`

> Most users prefer English regardless of the proxy location. For that, use `lang=en-US,en`

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "lang=en-us,en" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://httpbin.dev/anything"
```

`https://api.scrapfly.io/scrape?lang=en-us%2Cen&key=&url=https%3A%2F%2Fhttpbin.dev%2Fanything`

[Operating System](https://scrapfly.io/docs/scrape-api/custom#os)
-----------------------------------------------------------------

> We do not recommend using this feature unless it's absolutely necessary as it can impact scraper blocking rates.

By default, Scrapfly automatically selects the most suitable Operating System for all outgoing requests. To configure operating system explicitly the [os](https://scrapfly.io/docs/scrape-api/getting-started#api_param_os) parameter can be used.

The supported values are: `win11,mac,linux`

> Because of potential conflicts, the `os`parameter and `User-Agent`header cannot be set at the same time.

For example, to set Operating System to Windows 11 the `os=win11` parameter would be used:

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "os=win11" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://httpbin.dev/anything"
```

`https://api.scrapfly.io/scrape?os=win11&key=&url=https%3A%2F%2Fhttpbin.dev%2Fanything`

[Integration](https://scrapfly.io/docs/scrape-api/custom#integration)
---------------------------------------------------------------------

*   [Geo Targeting example with Python SDK](https://scrapfly.io/docs/onboarding#proxy)
*   [Request customization example with Python SDK](https://scrapfly.io/docs/onboarding#custom_request)
*   [Request customization example with Typescript SDK](https://scrapfly.io/docs/onboarding#configuring_scrape)
