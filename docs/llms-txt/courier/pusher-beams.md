# Source: https://www.courier.com/docs/external-integrations/push/pusher-beams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pusher Beams

> Learn how to send push notifications using Pusher Beams via Courier, including examples for targeting users or interests with APNs or FCM delivery modes.

## Setup

You will need a [Pusher Beams](https://pusher.com/beams) account with an instance configured. In Courier, navigate to the [Pusher Beams Integration](https://app.courier.com/integrations/catalog/pusher-beams) page, enter your instance ID and secret key, then click "Save."

## Profile Requirements

Pusher Beams can send to either users or interests. At least one `mode` out of `web`, `apns`, or `fcm` is required.

### Send to interests

```json  theme={null}
{
  "message": {
    "to": {
      "pusherBeams": {
        "interests": ["interest-1", "interest-2"],
        "mode": ["apns", "fcm"]
      }
    }
  }
}
```

### Send to users

```json  theme={null}
{
  "message": {
    "to": {
      "pusherBeams": {
        "userIds": ["user-id-1", "user-id-2"],
        "mode": ["apns", "fcm"]
      }
    }
  }
}
```

## Overrides

### Body Overrides

Overrides can be used to change the request body that Courier sends to Pusher Beams' API.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "pusherBeams": {
        "interests": ["interest-1"],
        "mode": ["fcm"]
      }
    },
    "providers": {
      "pusher-beams": {
        "override": {
          "body": {
            "fcm": {
              "notification": {
                "title": "Custom Title",
                "body": "Custom body text"
              }
            }
          }
        }
      }
    }
  }
}
```

### Config Overrides

You can swap the instance ID or secret key at send time:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "pusherBeams": {
        "interests": ["interest-1"],
        "mode": ["fcm"]
      }
    },
    "providers": {
      "pusher-beams": {
        "override": {
          "config": {
            "instanceId": "RUNTIME_INSTANCE_ID",
            "secretKey": "RUNTIME_SECRET_KEY"
          }
        }
      }
    }
  }
}
```
