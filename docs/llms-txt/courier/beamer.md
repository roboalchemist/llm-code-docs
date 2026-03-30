# Source: https://www.courier.com/docs/external-integrations/push/beamer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Beamer

> Learn how to use Courier to send Beamer push notifications with customizable override options like user targeting, push toggle, and publish status.

## Setup

You will need a [Beamer](https://www.getbeamer.com/) account. In Courier, navigate to the [Beamer Integration](https://app.courier.com/integrations/catalog/beamer) page, enter your API key, then click "Save."

## Profile Requirements

No profile data is required for Beamer.

## Overrides

Overrides can be used to change the request body that Courier uses to send a push message. You can override the following fields from Beamer's `postcreation` object ([documented here in Beamer's API docs](https://www.getbeamer.com/api#definition-PostCreation)).

```json  theme={null}
{
  "filter": "",
  "filterUserId": "",
  "filterUrl": "",
  "sendPushNotification": "",
  "publish": ""
}
```

Below is an example of using the override to deliver a post to a specific known user id.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {},
    "providers": {
      "beamer": {
        "override": {
          "body": {
            "filterUserId": "user-123",
            "sendPushNotification": "false",
            "publish": "true"
          }
        }
      }
    }
  }
}
```
