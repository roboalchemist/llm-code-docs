# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/executing-http-requests.md

# Executing HTTP Requests

## http\_request Function

The `http_request` function allows developers to perform additional HTTP POST/GET requests during a page interaction, unlocking access to more data. By capturing these internal API calls, you can directly access key data in machine-readable formats like JSON, bypassing the need to parse HTML.

{% hint style="warning" %}
**Note:**   `render_flow` may include multiple `http_request` steps, but only the **first** is free of charge. \
**Starting from the 2nd `http_request`**, the request will be classified and charged as a **VX6** request.
{% endhint %}

<table><thead><tr><th width="172">Parameter</th><th width="187">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>url</code></td><td>Required</td><td>URL | The target URL for the HTTP request</td></tr><tr><td><code>method</code></td><td>Optional (Default = <code>GET</code>)</td><td>Enum | The HTTP request method  -<code>GET</code>, <code>POST</code></td></tr><tr><td><code>headers</code></td><td>Optional</td><td>Object | Additional headers required for the request in JSON format </td></tr><tr><td><code>timeout</code></td><td>Optional</td><td>Integer | Controls the timeout if the internal HTTP request being performed in ms</td></tr></tbody></table>

### Example request

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
        "http_request": {
                "url": "https://www.example.com/api/data",
                "method": "POST",
                "headers": {...}
                "timeout": 5000
        }
    }]
}'
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Like all Page Interactions, infinite scrolling is capped by the global 120-second session timeout, and will be terminated if this limit is reached.
{% endhint %}
