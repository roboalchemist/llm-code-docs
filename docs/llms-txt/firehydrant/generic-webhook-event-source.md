# Source: https://docs.firehydrant.com/docs/generic-webhook-event-source.md

# Generic Webhook Event Source

While you can use provider-specific webhooks to create events, you can also create events by using a standard webhook and ensuring the data matches the expected Event Format.

## Step-by-Step Guide

1. In FireHydrant, navigate to the Signals Sources page (Signals > Sources). Here, you’ll find a webhook URL that you will use for creating Signals. Click the copy icon to the right of the URL to easily copy the URL to your clipboard.

<Image alt="The url for a generic webhook integration" align="center" width="800px" src="https://files.readme.io/8c2ee40-generic-webhook.jpg">
  The url for a generic webhook integration
</Image>

2. Using CURL or your favorite API client, you can create a test signal by sending a POST request to the URL you copied in the first step. The body of your request should use the [Event Data Model](https://docs.firehydrant.com/docs/signals-data-model)

```json
{
  "summary": "CPU Utilization Spiking",
  "body": "The production server is experiencing greater than 99% utilizations of compute.",
  "level": "ERROR",
  "status": "OPEN",
  "idempotency_key": "some_unique_key_for_your_monitor",
  "images": [
    {
      "src": "https://site.com/images/123.png",
      "alt": "A simple, sample image"
    }
  ],
  "links": [
    {
      "href": "https://site.com/monitors/123",
      "text": "Monitoring Source"
    }
  ],
  "annotations": {
    "policy": "escalatable"
  },
  "tags": ["service:api-gateway", "environment:production", "functionality:public-api", "random-tag"],
}
```

3. If your data is formatted correctly, an event will be created in the Events log page in FireHydrant. If the data doesn't match, you can find an error in the Errors tab.

<Image alt="A log of successful Signals" align="center" width="800px" src="https://files.readme.io/a6b8958-logs.jpg">
  A log of successful Signals
</Image>