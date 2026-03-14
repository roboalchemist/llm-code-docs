# Source: https://docs.nimbleway.io/technologies/browserless-drivers.md

# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/browserless-drivers.md

# Browserless Drivers

{% hint style="success" %}
Nimble's infrastructure uses specialized **Browserless Drivers** under the hood to optimize performance, rendering, and access behavior based on your use case. By default, the optimal driver is selected automatically. However, for advanced use cases, you can control which driver to use explicitly in your Web API requests.
{% endhint %}

## What? <a href="#what-and-why" id="what-and-why"></a>

Drivers are internal configurations that determine:

* Whether a headless or headfull browser is used.
* If rendering, stealth techniques, or anti-bot mitigation is applied.
* The depth and accuracy of page interaction and data capture.

Nimble's optimization engine intelligently selects the best driver when `driver` is **not** set. However, advanced users can specify a driver manually via the **Web API** endpoint using the `driver` parameter.

read more on Browserless Drivers here - [browserless-drivers](https://docs.nimbleway.io/technologies/browserless-drivers "mention")

{% hint style="warning" %}
**Note:** Driver control is only supported in the Web API. It cannot be set manually in other API verticals.
{% endhint %}

### Available Drivers (Web API Only)

The following drivers are available for **explicit use** only via the Web API endpoint:

<table><thead><tr><th width="123.67578125">Driver</th><th width="118.921875">Rendering</th><th width="169.7421875">Mode</th><th>Description</th></tr></thead><tbody><tr><td><code>vx6</code></td><td>❌</td><td>Headless</td><td>Fastest non-rendering mode for simple page loads and API endpoints.</td></tr><tr><td><code>vx8</code></td><td>✅</td><td>Headless</td><td>Default headless rendering mode. Best for pages requiring light JS rendering.</td></tr><tr><td><code>vx8-pro</code></td><td>✅</td><td>Headfull</td><td>Headfull rendering with more human-like behavior. Ideal for moderate anti-bot protections.</td></tr><tr><td><code>vx10</code></td><td>✅</td><td>Headless Stealth</td><td>Advanced stealth for highly protected websites.</td></tr><tr><td><code>vx10-pro</code></td><td>✅</td><td>Headfull Stealth</td><td>Highest-grade stealth and realism. Best for heavily fortified targets.</td></tr></tbody></table>

> The `driver` parameter **overrides** the `render` flag:
>
> * `render: false` = uses `vx6` which is the default
> * `render: true` = uses `vx8` or `vx10` automatically depending on the domain

***

## When to Use the `driver` Parameter

* You want **guaranteed behavior** for rendering, stealth, or evasion.
* You’re targeting websites with known protection mechanisms.
* You need reproducible results across environments.
* You’re optimizing cost/performance across different types of content.

#### Example Request

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com",
    "driver": "vx6"
}'
```

{% endtab %}
{% endtabs %}

***

## What Happens If I Don’t Set It?

If you omit the `driver` parameter:

* Nimble automatically selects the best driver for the domain.
* The selected driver is **returned in the response payload** for any API request.
* You can also view driver usage and history in the [Nimble App](https://docs.nimbleway.io/technologies/browserless-drivers/api-driver-based-pricing) under your **Dashboard** or **Analytics**.
