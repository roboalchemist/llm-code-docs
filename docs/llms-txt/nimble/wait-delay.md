# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/wait-delay.md

# Wait (delay)

## wait Function

The `wait` function allows you to add a delay between actions in your scraping sequence. This can be useful for simulating human-like behavior or waiting for certain elements on the page to load. The delay is specified in milliseconds.

<table><thead><tr><th width="149">Parameter</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>delay</code></td><td>Required when <code>wait</code> is being used</td><td>Integer | The required delay to be added in ms </td></tr></tbody></table>

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
            "wait": {
                "delay": 500
        }
    }]
}'
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Like all Page Interactions, infinite scrolling is capped by the global 120-second session timeout, and will be terminated if this limit is reached.
{% endhint %}
