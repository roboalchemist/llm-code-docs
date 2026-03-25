# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/wait-and-click.md

# Wait and Click

## wait\_and\_click Function

The `wait and_click` function waits for a specific element, identified by a selector, to appear on the page and then automatically clicks on it. This is particularly useful for interacting with buttons, links, or other interactive elements on the page.

<table><thead><tr><th width="190">Parameter</th><th width="183">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>selector</code></td><td>Required when <code>wait_and_click</code> is being used</td><td>String | The selector for the desired element to be clicked on</td></tr><tr><td><code>timeout</code></td><td>Optional</td><td>Integer | Controls the time to allow the click action run in ms</td></tr><tr><td><code>delay</code></td><td>Optional</td><td>Integer | The required delay to be added in ms </td></tr><tr><td><code>scroll</code></td><td>Optional</td><td>Bool | When <code>true</code>, scroll the selected element into the visible area if it is not already visible.</td></tr><tr><td><code>visible</code></td><td>Optional</td><td>Bool | when true, the request will wait for the element to be present in the DOM and to be visible, i.e. to not have display: none or visibility: hidden CSS properties.</td></tr></tbody></table>

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
            "wait_and_click": {
                "selector": "input[name='\''Organic'\'']",
                "timeout": 20000,
                "delay": 500,
                "scroll": true,
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
