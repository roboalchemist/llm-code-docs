# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/capturing-screenshots.md

# Capturing Screenshots

## screenshot Function

Page Interactions can be used to capture screenshots of the desired webpage. To take a screenshot, use the following parameters:

<table><thead><tr><th width="172">Parameter</th><th width="187">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>full_page</code></td><td>Optional<br>Default = <code>false</code></td><td>Bool | Capture a screenshot of the entire page or just the viewable area.</td></tr><tr><td><code>format</code></td><td>Optional<br>Default = <code>png</code></td><td>Enum | The Base64 format of the screenshot image. Supported formats: <code>png</code>, <code>jpeg</code>, <code>webp</code></td></tr><tr><td><code>timeout</code></td><td>Optional<br>Default = <code>30000</code></td><td>Integer | Controls the time to allow screenshots scrolling before terminating screenshot processing in ms.</td></tr></tbody></table>

### Example Request

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com",
    "render": true,
    "render_flow": [{
        "screenshot": {
                "full_page": true,
                "format": "jpeg",
                "timeout": 30000
        }
    }]
}'
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Like all Page Interactions, infinite scrolling is capped by the global 120-second session timeout, and will be terminated if this limit is reached.
{% endhint %}
