# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/network-capture/filter-by-resource-type.md

# Filter By Resource Type

## Resource Type Filtering

Websites load hundreds of resources every time a webpage is loaded. Filtering through all of these requests is critical to identifying and capturing Internal APIs.

Nimble's Network Capture can filter requests by one or more resource types to help isolate relevant network requests.

<table><thead><tr><th width="182">Parameter</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>method</code></td><td>Optional (default = <code>Any</code>)</td><td>Enum |  HTTP method should be filtered for. Examples: <code>GET</code>, <code>POST</code>, <code>PUT</code>. </td></tr><tr><td><code>resource_type</code></td><td>Required when filtering by resource type</td><td>List [Enums] | set all required resource type to filter.</td></tr></tbody></table>

### Supported Resource Types <a href="#supported-resource-types" id="supported-resource-types"></a>

Some commonly used resource types include:

* **xhr** - XHR is an object used to interact with a server. It allows retrieving data from the server without triggering a full page refresh.
* **fetch** - Fetch is a method that provides an easy, logical way to fetch resources asynchronously across the network.
* **stylesheet** - This element corresponds to a Cascading Style Sheet.
* **script** - This element is used to embed executable code or data; this is typically used to embed or refer to JavaScript code.
* **document** - returns the main HTML document.

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
            "resource_type": [
                "xhr", "script"
            ]
        }
    ]
}'
```

{% endtab %}
{% endtabs %}

### Example Response

```json
{
    "url": "https://www.example.com/",
    "status": "success",
    "query_time": "2024-04-04T11:10:43.567Z",
    "html_content": "...",
    "status_code": 200,
    "headers": {
        ...
    },
    "input_url": "https://www.example.com/",
    "network_capture": [
        {
            "filter": {
                "method": "GET",
                "resource_type": [
                    "xhr",
                    "script"
                ]
            },
            "results": [
                {
                    "request": {
                        "resource_type": "script",
                        "method": "GET",
                        "url": "https://www.example.com/script/0001.js",
                        "headers": {
                            ...
                        }
                    },
                    "response": {
                        "status": 200,
                        "status_text": "",
                        "headers": {
                            ...
                        },
                        "serialization": "none",
   "body": "..."
                    }
                },
                {
                    "request": {
                        "resource_type": "xhr",
                        "method": "GET",
                        "url": "https://www.example.com/script/0002.js",
                        "headers": {
                            ...
                        }
                    },
                    "response": {
                        "status": 200,
                        "status_text": "",
                        "headers": {
                           ...
                        },
                        "serialization": "none",
   "body": "..."
                    }
                }
            ]
        }
    ]
}
```
