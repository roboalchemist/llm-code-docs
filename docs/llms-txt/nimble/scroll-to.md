# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/scroll-to.md

# Scroll to

## scroll\_to Function

The `scroll_to` function scrolls the page to bring a specific element into view. This is useful for interacting with elements that are not initially visible on the page, such as loading more content as you scroll down.

<table><thead><tr><th width="190">Parameter</th><th width="183">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>selector</code></td><td>Required when <code>scroll_to</code> is being used</td><td>String | The selector for the desired element to scroll to</td></tr><tr><td><code>visible</code></td><td>Optional</td><td>Bool | when true, the request will wait for the element to be present in the DOM and to be visible, i.e. to not have display: none or visibility: hidden CSS properties.</td></tr></tbody></table>

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
            "scroll_to": {
                "selector": "input[name='\''Organic'\'']",
                "visible": false
        }
    }]
}'
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Like all Page Interactions, infinite scrolling is capped by the global 120-second session timeout, and will be terminated if this limit is reached.
{% endhint %}
