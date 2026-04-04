# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/network-capture/wait-for-requests.md

# Wait for Requests

## Wait for Request Counter

The Network Capture feature includes two parameters that work together to ensure you capture the necessary network requests during a scraping session:

1. **wait\_for\_requests\_count**: This parameter allows you to set the minimum number of network requests that must be captured. If this minimum is not reached within the standard request duration, the duration will be extended until the specified number of requests is captured, or until the timeout limit is reached.
2. **wait\_for\_requests\_count\_timeout**: This parameter defines the maximum amount of time the request duration can be extended to capture the minimum number of network requests specified by the `wait_for_requests_count` parameter. This ensures that the scraping process remains efficient and does not exceed a reasonable time limit.

These parameters are essential for scenarios where capturing a specific amount of network data is critical, offering precise control over the scraping process.

<table><thead><tr><th width="182">Parameter</th><th width="135">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>wait_for_requests_count</code></td><td>Optional (default = 0 )</td><td>Integer |  Setting the minimum number to be captured. When set, the request duration will be extended to ensure that the requests are captured or until 'wait_for_requests_count_timeout' is reached.</td></tr><tr><td><code>wait_for_requests_count_timeout</code></td><td>Optional (default = 10 seconds)</td><td>Integer | Defines the maximum duration an API request can be extended to capture the minimum number of requests specified by 'wait_for_requests_count'</td></tr></tbody></table>

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
            ],
            wait_for_requests_count: 3,
            wait_for_requests_count_timeout: 5000
        }
    ]
}'
```

{% endtab %}
{% endtabs %}
