# Source: https://www.courier.com/docs/external-integrations/push/airship.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Airship

> Step-by-step guide for integrating Airship with Courier, including how to configure user profiles, use provider overrides for authentication, and track push notification events via Courier's global attributes.

## Setup

You will need an [Airship](https://www.airship.com/) account with a project configured. In Courier, navigate to the [Airship Integration](https://app.courier.com/integrations/catalog/airship) page, enter your auth token and base URL, then click "Save."

## Profile Requirements

To deliver a push notification to a recipient over Airship, Courier must be provided the recipient's Airship audience and device types. These values should be included in the recipient profile as `airship`.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "airship": {
        "audience": {
          "named_user": "user-123"
        },
        "device_types": ["ios"]
      }
    },
    "data": {
      "username": "Steph Courier"
    }
  }
}
```

## Overrides

You can use a provider override to replace what Courier sends to Airship's API. For example, you can use basic auth with your send request:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "airship": {
        "audience": {
          "named_user": "user-123"
        },
        "device_types": ["ios"]
      }
    },
    "data": {
      "dataForPushMessage": true
    },
    "providers": {
      "airship": {
        "override": {
          "body": {},
          "headers": {
            "Authorization": "Basic <EncodedAppKey:AppSecret>"
          }
        }
      }
    }
  }
}
```

Everything inside of `message.providers.airship.override` will replace what Courier sends to Airship's API. You can see all the available options by visiting [Airship's API docs](https://docs.airship.com/api/ua/).

## Tracking Events

Courier will include tracking URL information in the `global_attributes` data bag. See [push notification tracking](/external-integrations/push/intro-to-push#tracking) for details.
