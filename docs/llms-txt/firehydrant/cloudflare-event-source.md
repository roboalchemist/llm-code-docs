# Source: https://docs.firehydrant.com/docs/cloudflare-event-source.md

# Cloudflare Event Source

The Cloudflare Integration for Signals allows any messages or events from Cloudflare to be sent as Events to FireHydrant. If any Teams have configured Alert Rules/triggers to match on these Events, then Alerts will be opened and notify on-call responders.

For a refresher on Signals, visit [Introduction to Signals](https://docs.firehydrant.com/docs/signals-introduction).

## Cloudflare Webhook

To configure a webhook in Cloudflare, refer to [Cloudflare's Webhook instructions here](https://developers.cloudflare.com/notifications/get-started/configure-webhooks/) .

<Image alt="Fetching the URL from the Cloudflare source" align="center" src="https://files.readme.io/0104372-CleanShot_2024-04-25_at_15.21.462x.png">
  Fetching the URL from the Cloudflare source
</Image>

For the **URL** field, go to your organization's [Event Sources](https://app.firehydrant.io/signals/sources)  and click **Copy URL** within the Cloudflare row. Paste that value into the **URL** field in Cloudflare when configuring the Webhook.

## Field Mappings

FireHydrant's Cloudflare transposer will map the following fields to FireHydrant's [Events Data Model](https://docs.firehydrant.com/docs/events-data-model).

| Cloudflare Parameter                          | FireHydrant Parameter                                                                                                       |
| :-------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| -                                             | `idempotency_key` - No parameter, all events from Cloudflare will always open new alerts on FireHydrant                     |
| `Alert from Cloudflare`                       | `summary` - Static message, always "Alert from Cloudflare"                                                                  |
| `payload.text` \|\| `No information provided` | `body` - The body will always be the `payload.text` or "No information provided" if that parameter is empty for some reason |
| `0`                                           | `level` - Always `INFO`                                                                                                     |
| `0`                                           | `status` - Always Open                                                                                                      |
| -                                             | `links`                                                                                                                     |

These mappings mean that an inbound webhook from Azure with the following content:

Once you've configured the webhook in Cloudflare, you can test it. Cloudflare's payload is simplistic and only contains a `text` parameter in the body with Cloudflare's message for what event fired the webhook.

In FireHydrant, we will insert that `text` into the `description` of the Alert, and the alert's title will always default to `Alert from Cloudflare`.

```json Cloudflare Example Payload
{
  "text": "Hello World! This is a test message sent from https://cloudflare.com. If you can see this, your webhook is configured properly."
}
```

```json What FireHydrant Transposes It To
{
  "summary": "Alert from Cloudflare",
  "body": "Hello World! This is a test message sent from https://cloudflare.com. If you can see this, your webhook is configured properly.",
  "level": 0,
  "links": [],
  "idempotency_key": "",
  "status": 0
}
```