# Source: https://www.courier.com/docs/external-integrations/direct-message/viber.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Viber

> Send Viber notifications via Courier by registering a webhooks server, obtaining the recipient's UserID, and including it as viber.receiver in the recipient profile.

## Setup

You will need:

1. A Viber [bot account](https://partners.viber.com/account/create-bot-account). Make a note of the auth token.
2. An active webhooks server that can receive POST requests from Viber. Viber provides a [Node.js utility](https://www.npmjs.com/package/viber-bot) for handling these requests.

In Courier, navigate to the [Viber Integration](https://app.courier.com/integrations/catalog/viber) page, enter your auth token and sender name, then click "Save."

### Webhooks Server

Before sending notifications, Viber requires a webhooks server to be registered:

```bash  theme={null}
curl -X POST 'https://chatapi.viber.com/pa/set_webhook' \
     -H 'Content-Type: application/json' \
     -H 'X-Viber-Auth-Token: VIBER_AUTH_TOKEN' \
     -d '{ "url": "YOUR_WEBHOOK_SERVER_URL", "event_types": ["delivered"] }'
```

This server will receive events from Viber such as UserIDs of users who subscribe, as well as delivery status events.

## Profile Requirements

To send a direct message to a user, supply the Viber `UserID` to the `viber.receiver` property of the recipient profile. The recipient must have an active [Viber](https://www.viber.com/en/) account. The `UserID` is sent to your webhooks server after a user messages the Viber bot.

```json  theme={null}
{
  "message": {
    "to": {
      "viber": {
        "receiver": "12943673=="
      }
    }
  }
}
```

## Overrides

### Body Overrides

You can override the request body that Courier sends to the Viber [Send Message API](https://developers.viber.com/docs/api/rest-bot-api/#send-message).

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "viber": {
        "receiver": "12943673=="
      }
    },
    "providers": {
      "viber": {
        "override": {
          "body": {
            "type": "picture",
            "media": "https://example.com/image.jpg"
          }
        }
      }
    }
  }
}
```

### Config Overrides

You can swap the auth token, sender name, or API URL at send time:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "viber": {
        "receiver": "12943673=="
      }
    },
    "providers": {
      "viber": {
        "override": {
          "config": {
            "token": "RUNTIME_AUTH_TOKEN",
            "name": "My Bot Name"
          }
        }
      }
    }
  }
}
```
