# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/scroll.md

# Scroll

## scroll Function

The `scroll` function allows you to scroll the page vertically to a specific position. This can be useful for loading content that becomes visible as you scroll, or for moving to a specific part of the page to interact with elements that are not immediately in view.

<table><thead><tr><th width="190">Parameter</th><th width="183">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>x</code></td><td>Required when <code>scroll</code> is being used</td><td>Integer | The x-axis position to scroll to</td></tr><tr><td><code>y</code></td><td>Required when <code>scroll</code> is being used</td><td>Integer | The y-axis position to scroll to</td></tr><tr><td><code>timeout</code></td><td>Optional</td><td>Integer | Controls the time to allow the scroll action run in ms</td></tr><tr><td><code>scroll_in_element</code></td><td>Optional</td><td>String | Enables scrolling inside a specific element (e.g., sidebar, modal, or div).</td></tr></tbody></table>

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
            "scroll": {
                "x": 0,
                "y": 100,
                "timeout": 20000
        }
    }]
}'
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Like all Page Interactions, infinite scrolling is capped by the global 120-second session timeout, and will be terminated if this limit is reached.
{% endhint %}
