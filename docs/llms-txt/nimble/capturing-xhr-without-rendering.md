# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/network-capture/capturing-xhr-without-rendering.md

# Capturing XHR without Rendering

## is\_xhr Param

Introduction the `is_xhr` parameter is a boolean option designed to capture internal API calls without requiring page rendering. While the network capture feature requires that rendering is enabled, `is_xhr` provides a workaround by allowing data collection from internal APIs that do not depend on rendering.&#x20;

This feature is particularly useful for efficiently gathering data from sources where rendering is not needed (internal API is accessible directly) , optimizing performance and reducing resource usage during the scraping process.

* When enabled, the browser sends different headers for XHR against DOC requests
* The target URL in this case would be the XHR/AJAX URL

<table><thead><tr><th width="141">Parameter</th><th width="152">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>is_xhr</code></td><td>Optional (default = false)</td><td>Boolean | Instructs the Web API that the target page is an XHR request instead of a standard webpage. Only available when <code>render</code> is set to <code>false</code> (default)</td></tr></tbody></table>

### Example Request

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.lowes.com/purchase/api/items/1003130714/additionalServices?storeNumber=1792&quantity=1&stateCode=FL&userType=REGULAR&isSDV2Enabled=true",
    "country": "US",
    "is_xhr": true
}'
```

{% endtab %}
{% endtabs %}
