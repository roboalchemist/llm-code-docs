# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-functions/unlocker-proxy.md

# Unlocker Proxy

Unlocker Proxy was designed to solve the problem of anti-bot systems for web scraping users seamlessly. It combines our Nimble IP residential proxies with advanced, AI-powered unlocking technology in the form of Nimble Browser.

Users turn to Unlocker Proxy to enjoy a variety of upgrades including:

* [x] smooth and continuous access to any public data source
* [x] scaling their collection ops flexibly on fully-managed infrastructure
* [x] eliminating burdensome maintenance and debugging
* [x] utilizing AI-powered parsing and webpage rendering capabilities

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/N4HPffRWW0T1u2tjW8g8/Nimble%20Browser.png" alt=""><figcaption></figcaption></figure>

### How it works

To make Unlocker Proxy as simple as possible to integrate, we've designed a standard, proxy-style connection API that makes it seamless to move from residential proxies to Unlocker Proxy.

Behind the scenes, Unlocker Proxy automates the key technologies needed to execute the request and bypass anti-bots, including:

* [x] **Fingerprinting engine** - automatic management of TLS fingerprints, canvas checking, headers, cookies, and more.
* [x] **Fully-managed infrastructure** - serverless cloud environments allow for flexible and infinite scalability, managed for you by Nimble.
* [x] **Built-in Proxies** - Nimble IP provides premium networking infrastructure with high quality and performance IPs.

{% hint style="warning" %}
Unlocker Proxy usage is charged according to the [Nimble Web API pricing](https://docs.nimbleway.io/technologies/browserless-drivers/api-driver-based-pricing) <mark style="color:purple;">**per Requests**</mark>**&#x20;and&#x20;**<mark style="color:red;">**not per GB**</mark>\
Make sure you review your plan and monitor usage via your Nimble Dashboard.
{% endhint %}

## Real Time Request

Unlocker Proxy provides a simplified, one-line approach to data collection that is easy to use and implement across a variety of programming languages and environments. Unlocker Proxy accepts fully-formed URLs, and provides access to many of the key features of the Nimble Browser such as page rendering and data parsing.

**Example request**

{% code overflow="wrap" %}

```bash
curl -k \
  --proxy 'http://unlocker.webit.live:8888' \
  --proxy-user 'USERNAME:PASSWORD' \
  -H "Header: custom header value" \
  -H 'x-nimble-country: US' \
  -H 'x-nimble-parse: true' \
  -H 'x-nimble-render: false' \
  -H 'x-nimble-format: json' \
  -H 'x-nimble-locale: en-US' \
  -H 'x-nimble-no-html: true' \
  -H 'x-nimble-session-id: my-session-123' \
  'https://www.ipinfo.com'
```

{% endcode %}

**Request parameters**

<table><thead><tr><th width="185.4296875">Parameter</th><th width="174.55598958333334">Required</th><th>Description</th></tr></thead><tbody><tr><td>x-nimble-country</td><td>optional</td><td>String: Two-letter country code, e.g. US, DE, BR.</td></tr><tr><td>x-nimble-render</td><td>optional</td><td>Boolean: true | false | auto - Whether or not the target resource’s Javascript should be rendered. This is sometimes required in order to properly load some websites.</td></tr><tr><td>x-nimble-parse</td><td>optional</td><td>Enum: true | false - Whether or not the Nimble Browser should parse the requested web data into a JSON structure, or return only the raw HTML. The full raw HTML is returned in both cases.</td></tr><tr><td>x-nimble-format</td><td>optional</td><td>Enum: <code>JSON</code> | <code>HTML</code> | <code>JSON-LINES</code> | <code>RAW</code> - The data response format. HTML - in case of error, returns JSON with error message.</td></tr><tr><td>x-nimble-locale</td><td>optional</td><td>String | LCID standard locale used for the URL request. Alternatively, user can use <code>auto</code> for automatic locale based on geo-location.</td></tr><tr><td>x-nimble-no-html</td><td>optional</td><td>Bool | If set to <code>true</code>, the API will exclude HTML content from the response.</td></tr><tr><td>x-nimble-session-id</td><td>optional</td><td>String | Sticky session ID for multiple related requests.</td></tr><tr><td>Custom-Header</td><td>optional</td><td>String: Add custom headers to the request.</td></tr></tbody></table>

{% hint style="warning" %}
Unlocker Proxy should not be used with headless browsers or their drivers (Puppeteer, Selenium, etc.) All rendering is handled on the server side.
{% endhint %}

**Response**

If the request was executed successfully, the Unlocker Proxy will return a <mark style="color:red;background-color:yellow;">200 OK</mark> message with the following data:

```json
{ 
        "status": "success",
        "html_content": string,
        "parsing": {
             "status" : "success",
             "entities": { },
             "total_entities_count": 0,
             "entities_count": { }
    }
}
```

The <mark style="color:red;background-color:yellow;">html\_content</mark> node contains the full HTML of the requested page, and if parsing was enabled, the <mark style="color:red;background-color:yellow;">parsing</mark> node will contain a structured JSON object of the data.

**Response codes**

| Status | Description                                   |
| ------ | --------------------------------------------- |
| 200    | OK                                            |
| 400    | The requested resource could not be reached   |
| 401    | Unauthorized/Invalid Token                    |
| 500    | Internal service error                        |
| 501    | An error was encountered by the proxy service |
| 555    | Request timeout                               |
