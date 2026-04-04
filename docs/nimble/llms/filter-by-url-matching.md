# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/network-capture/filter-by-url-matching.md

# Filter by URL Matching

## URL Filtering&#x20;

Requests can be captured by using the **`network_capture`** field, which receives a JSON array that can include one or more filters. Each filter specifies which requests should be collected for later inspection.

The below example demonstrates two simple network capture filters, and how they are performed:

<table><thead><tr><th width="159">Parameter</th><th width="265">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>url.type</code></td><td>Optional (default = <code>exact</code>) </td><td>Enum: |<code>exact</code>, <code>contains</code> - choosing which type of URL filtering to apply</td></tr><tr><td><code>url.value</code></td><td>Required when filtering by URL</td><td>String | The URL or URL portion to match to.</td></tr><tr><td><code>method</code></td><td>Optional (default = <code>Any</code>)</td><td>Enum |  HTTP method should be filtered for. Examples: <code>GET</code>, <code>POST</code>, <code>PUT</code>. </td></tr></tbody></table>

### Exact Match Filtering

In the this example, we ask to capture requests that match the URL we've provided exactly and that only use the **GET** method. Exact matches are very precise and can be used when you've determined exactly which network request you'd like to capture.

### Containing a Match Filtering

In the this example, we ask to capture all .css requests by searching for requests to URLs that include "`.css`". The request method has been intentionally left out to capture requests using any method.

Using containing filters helps broaden our network captures, and can be very useful when needing all files of a certain type (css, js, etc.), a particular request that includes dynamic variables, or when the exact request is still not fully known.

### Example Request

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com/",
    "render": true,
    "network_capture": [
            {
                "method": "GET",
                "url": {
                    "type": "exact",
                    "value": "https://i5.walmartimages.com/a14/capabilities.min.js"
                }
            },
            {
                "url": {
                    "type": "contains",
                    "value": ".css"
                }
            }
        ]
}'
```

{% endtab %}
{% endtabs %}

### Example Response

In the example response above, we see that network capture returns:

* **filter -** the filter that was defined initially.
* **result** - the requests found that match the filter
  * **request** - the headers and metadata of the request.
  * **response** - the headers and data of the response.
    * **body** - under response, `body` will contain the contents of the captured resource.

```json
{
...
"network_capture": {
    "filter":
    {
        "method": "GET",
        "url":
        {
            "type": "exact",
            "value": "https://i5.walmartimages.com/a14/capabilities.min.js"
        }
    },
    "results":
    [
        {
            "request":
            {
                "method": "GET",
                "url": "https://i5.walmartimages.com/a14/capabilities.min.js",
                "headers":
                {
                    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
                    "referer": "https://www.example.com/",
                    "accept-language": "en,en;q=0.9",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                    "sec-ch-ua-platform": "\"Windows\""
                }
            },
            "response":
            {
                "status": 200,
                "status_text": "",
                "headers":
                {
                    "accept-ranges": "bytes",
                    "cache-control": "max-age=2702",
                    "content-length": "538511",
                    "content-type": "application/javascript",
                    "date": "...",
                    "etag": "\"6a6c1c29ddb3737a4398ff1f7b1063bf\"",
                    "last-modified": "...",
                    "strict-transport-security": "max-age=15552000; includeSubDomains; preload",
                    "vary": "Access-Control-Request-Headers,Access-Control-Request-Method,Origin",
                    "x-amz-request-id": "tx00000000000002e8d4651-0064943c55-6d194055-nyc3c",
                    "x-hw": "1687437271.dop007.ml1.t,1687437271.cds219.ml1.hn,1687437271.cds216.ml1.c",
                    "x-rgw-object-type": "Normal"
                },
                "serialization": "none"
            },
            "body": "..."
        },
        {
        "filter": {
                "url": {
                    "type": "contains",
                    "value": ".css"
                }
            },
            "results": [
                {
                    "request": {
                        "method": "GET",
                        "url": "https://www.example.com/wp-content/cache/min/1/10069917ea6c78bacd530335b1684679.css",
                        "headers": {
                            "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
                            "referer": "https://www.example.com/",
                            "accept-language": "en,en;q=0.9",
                            "sec-ch-ua-mobile": "?0",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                            "sec-ch-ua-platform": "\"Windows\""
                        }
                    },
                    "response": {
                        "status": 200,
                        "status_text": "",
                        "headers": {
                            "cache-control": "max-age=31536000",
                            "content-encoding": "gzip",
                            "content-length": "81027",
                            "content-type": "text/css",
                            "date": "Thu, 22 Jun 2023 12:34:30 GMT",
                            "etag": "\"647713da-13c83\"",
                            "expires": "Fri, 21 Jun 2024 12:34:30 GMT",
                            "last-modified": "Wed, 31 May 2023 09:31:06 GMT",
                            "server": "nginx",
                            "vary": "Accept-Encoding"
                        },
                        "serialization": "none",
                        "body": "..."
      }
                }
            ]
        }
    ]
}
}
```
