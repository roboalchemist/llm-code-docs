# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/geo-location-targeting.md

# Geo Location Targeting

## What? <a href="#what-and-why" id="what-and-why"></a>

Geo-targeting is the ability to route requests through proxies located in specific geographical locations. This capability is particularly valuable for data collection that varies based on the user's geographic location, which can be crucial for businesses that require localized content or need to adhere to regional regulations and settings at scale.

Geo-targeting is an actual feature of **Nimble IP**, but it is exposed via **Nimble API**

<figure><img src="https://1919898886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FZNy4aqrBN53tR8DpTEuW%2Fuploads%2FTBs8yZRCsoKdpebdlnIU%2Fimage.png?alt=media&#x26;token=b1db6c4b-56c1-4ff3-8907-7ca06bb66eb7" alt=""><figcaption></figcaption></figure>

## &#x20;Why? <a href="#what-and-why" id="what-and-why"></a>

Built on top ***Nimble IP*** our premium Residential Proxy product offering, with high reputation, fast performance, and high availability **worldwide** to ensure requests always get through and are never rate limited. Nimble's Proxy help users with:

* **Geo-Restrictions**: Some businesses only operate in certain countries, or may localize information by the user's locale. Nimble AI Browser again uses residential proxies to empower users to send requests for anywhere in the world - ensuring access and localized data accuracy.
* **SEO and Market Research**: Companies can see how their or competitors’ websites appear in different regions, which is crucial for strategies involving search engine optimization (SEO) and localized marketing analysis.
* **Unlocking**: Helps in mimicking the behavior of local users, reducing the likelihood of being blocked by the target websites which might have anti-scraping measures in place.

## Additional Information <a href="#how" id="how"></a>

* <mark style="color:green;">Supported</mark> by real-time, asynchronous, and batch requests.
* <mark style="color:green;">Supported</mark> endpoints: [Web](https://docs.nimbleway.io/nimble-sdk/web-api), [SERP](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api), [Maps](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api) and [eCommerce](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api).
* <mark style="color:red;">Not supported</mark> endpoints: [Social](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/social-api).
* You can retrieve a comprehensive list of supported countries, states, and cities by using the [/location/cities endpoint](https://api.nimbleway.com/api/v1/location/cities) of the Admin API.
* See the full list of [ISO 3166 alpha-2 country codes](https://www.iban.com/country-codes)

## Request Option <a href="#request-option" id="request-option"></a>

<table><thead><tr><th width="140">Parameter</th><th width="262">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>url</code></td><td>Required <br>(In case of Web API Endpoint)</td><td>URL | The page or resource to be fetched. Note: when using a URL with a query string, encode the URL and place it at the end of the query string - Web API endpoint.</td></tr><tr><td><code>country</code></td><td>Optional (default = <code>all</code>)</td><td>String | Country used to access the target URL, use ISO Alpha-2 Country Codes i.e. US, DE, GB</td></tr><tr><td><code>state</code></td><td>Optional (default = <code>null</code>)</td><td>String | State used to access the target URL, use ISO Alpha-2 Country Codes i.e. NY, AZ, CA</td></tr><tr><td><code>city</code></td><td>Optional (default = <code>null</code>)</td><td>String | City used to access the target URL i.e. paris, london</td></tr><tr><td><code>locale</code></td><td>Optional (default = <code>auto</code>)</td><td>String | LCID standard locale used for the URL request. Alternatively, user can use <code>auto</code> for automatic locale based on geo-location.</td></tr></tbody></table>

{% hint style="info" %}
If no peers are available in a supported country/state/city, Nimble IP will return a 525 response.
{% endhint %}

### Example Request <a href="#example" id="example"></a>

A simple real-time request with `state` targeting and locale set to EN, meaning the request will be routed from New York State and the LCID standard will be set to English (which is the default value).

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://ipinfo.io/json",
    "country": "US",
    "render":true,
    "state": "NY",
    "locale": "en-US"
}'
```

{% hint style="warning" %}
Targeting a state is only available when the country parameter is set to US.
{% endhint %}
