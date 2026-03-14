# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/wait-and-type.md

# Wait and Type

## wait\_and\_type Function

The `wait_and_type` function allows you to input text into a specified field after waiting for the field to appear. This function is essential for filling out forms or entering search queries during the scraping process.

<table><thead><tr><th width="173">Parameter</th><th width="183">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>selector</code></td><td>Required when <code>wait_and_type</code> is being used</td><td>String | The selector for the desired element to be typed on</td></tr><tr><td><code>value</code></td><td>Required when <code>wait_and_type</code> is being used</td><td>String | the text input to be typed on desured elemnt</td></tr><tr><td><code>timeout</code></td><td>Optional</td><td>Integer | Controls the time to allow the type action run in ms</td></tr><tr><td><code>delay</code></td><td>Optional</td><td>Integer | The required delay to be added in ms </td></tr><tr><td><code>click_on_element</code></td><td>Optional</td><td>Bool | When <code>true</code>, the element would be clicked before typing</td></tr><tr><td><code>visible</code></td><td>Optional</td><td>Bool | when true, the request will wait for the element to be present in the DOM and to be visible, i.e. to not have display: none or visibility: hidden CSS properties.</td></tr></tbody></table>

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
            "wait_and_type": {
                "selector": "input[type='\''search'\'']",
                "timeout": 20000,
                "delay": 500,
                "value": "eggplant",
                "click_on_element": true,
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
