# Source: https://www.courier.com/docs/external-integrations/other/intercom.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Intercom

> Send in-app messages via Intercom by including the user's Intercom ID in their profile, with support for message and sender overrides.

## Setup

Install the Intercom integration from the [Courier integrations catalog](https://app.courier.com/integrations/catalog/intercom). You will need your Intercom access token and an admin/bot user ID to send messages from.

## Profile Requirements

To deliver an in-app push message to a recipient over Intercom, you must provide the recipient's Intercom User ID. Courier assumes the user is of type `user`.

```json  theme={null}
{
  "message": {
    "to": {
      "intercom": {
        "from": "012345",
        "to": {
          "id": "INTERCOM_USER_ID"
        }
      }
    }
  }
}
```

## Overrides

You can use the provider override to replace what Courier sends as an Intercom Message. Supported overrides include the message body and the From User ID. Here's an example where both are overridden:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "intercom": {
        "id": "INTERCOM_USER_ID"
      }
    },
    "providers": {
      "intercom": {
        "override": {
          "body": {
            "body": "I overrode this message",
            "from": {
              "id": "012345"
            }
          }
        }
      }
    }
  }
}
```

Other supported overrides are documented in the [Intercom API reference](https://developers.intercom.com/intercom-api-reference/reference#admin-initiated-conversation).
