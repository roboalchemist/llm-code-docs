# Source: https://www.courier.com/docs/external-integrations/push/onesignal-push.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OneSignal Push

> Learn how to send push notifications via OneSignal using Courier by configuring App ID and REST API Key, and passing either Player ID or External User ID in the recipient profile.

## Setup

You can get your OneSignal `App ID` and `REST API Key` by following [these instructions](https://documentation.onesignal.com/docs/accounts-and-keys). In Courier, navigate to the [OneSignal Integration](https://app.courier.com/integrations/catalog/onesignal) page, enter those values, then click "Save."

## Profile Requirements

To deliver a message to a recipient over OneSignal, Courier must be provided the recipient's [PlayerId](https://documentation.onesignal.com/docs/users#section-player-id) or [ExternalId](https://documentation.onesignal.com/docs/user-model-migration-guide#user-model). This ID should be included in the recipient profile as `oneSignalPlayerID` or `oneSignalExternalUserId`.

```json  theme={null}
{
  "message": {
    "to": {
       "oneSignalPlayerID": "..."
    }
  }
}
// or
{
  "message": {
    "to": {
       "oneSignalExternalUserId": "..."
    }
  }
}
```

## Overrides

Overrides can be used to change the request body that Courier sends to OneSignal's API. You can override any of the fields supported by OneSignal's [Create notification](https://documentation.onesignal.com/reference/create-notification) endpoint.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "oneSignalPlayerID": "player-id-123"
    },
    "providers": {
      "onesignal": {
        "override": {
          "body": {
            "priority": 10,
            "ttl": 3600,
            "small_icon": "ic_notification"
          }
        }
      }
    }
  }
}
```

## Data Mapping

OneSignal imposes a limit to push notification payloads. When sending push notifications through automated workflows that include batching, data payloads can become too large, which will result in a failed send.

Push channels can have data mapping enabled to customize which data you want passed down to the push channel provider. See [Data Mapping](/external-integrations/push/intro-to-push#data-mapping) for details.

<Frame caption="OneSignal Data Mapping">
  <img src="https://mintcdn.com/courier-4f1f25dc/iVP74UFk7QJhIlA6/assets/platform/channels/onesignal-data-map.png?fit=max&auto=format&n=iVP74UFk7QJhIlA6&q=85&s=33c5e4c40b88c3d0303f34206918a5ce" width="1025" height="601" data-path="assets/platform/channels/onesignal-data-map.png" />
</Frame>
