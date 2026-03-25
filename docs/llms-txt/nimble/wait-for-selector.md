# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/wait-for-selector.md

# Wait for Selector

## wait\_for Function

The `wait_for` function pauses the operation until a specific element, identified by a CSS selector, is present on the page. This ensures that the desired element is loaded before performing subsequent actions, which is crucial for interacting with dynamic content.

<table><thead><tr><th width="190">Parameter</th><th width="234">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>selectors</code></td><td>Required when <code>wait_for</code> is being used</td><td>String | Wait until the listed selector(s) have loaded.</td></tr><tr><td><code>timeout</code></td><td>Optional</td><td>Integer | Controls the time to allow until a selector is loaded in ms.</td></tr></tbody></table>

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
            "wait_for": {
                "selectors": [”body",”id”],
                "timeout": 2000
        }
    }]
}'
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Like all Page Interactions, infinite scrolling is capped by the global 120-second session timeout, and will be terminated if this limit is reached.
{% endhint %}
