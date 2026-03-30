# Source: https://www.courier.com/docs/external-integrations/push/pushbullet.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pushbullet

> Send push notifications via Pushbullet with customizable payloads using Courier's override system—no recipient profile data required.

## Setup

You will need a [Pushbullet](https://www.pushbullet.com/) account. In Courier, navigate to the [Pushbullet Integration](https://app.courier.com/integrations/catalog/pushbullet) page, enter your access token, then click "Save."

## Profile Requirements

No profile data is required for Pushbullet.

## Overrides

Overrides can be used to change the request body that Courier uses to send a push message. You can override any of the fields supported by Pushbullet's `/pushes` endpoint ([see all send request body fields here](https://docs.pushbullet.com/#create-push)).

### Body Overrides

Below is an example using the override to send a `url` by overriding the `type` of the push:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {},
    "providers": {
      "pushbullet": {
        "override": {
          "body": {
            "type": "link",
            "url": "https://www.courier.com"
          }
        }
      }
    }
  }
}
```

### Config Overrides

You can swap the access token at send time using a config override:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {},
    "providers": {
      "pushbullet": {
        "override": {
          "config": {
            "accessToken": "RUNTIME_ACCESS_TOKEN"
          }
        }
      }
    }
  }
}
```
