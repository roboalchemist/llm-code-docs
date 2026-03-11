# Source: https://www.courier.com/docs/external-integrations/push/magicbell.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MagicBell

> Learn how to integrate MagicBell with Courier to send in-app push notifications using email or external ID, with support for override fields like category and action URL.

## Setup

You will need a [MagicBell](https://www.magicbell.com/) account with a project configured. In Courier, navigate to the [MagicBell Integration](https://app.courier.com/integrations/catalog/magicbell) page, enter your API key and API secret, then click "Save."

## Profile Requirements

To deliver a message to in-app using MagicBell, Courier must be provided with either the email address of the recipient or an external ID.

### Email example:

```json  theme={null}
{
  "message": {
    "to": {
      "email": "recipient@example.com"
    }
  }
}
```

### External ID:

```json  theme={null}
{
  "message": {
    "to": {
      "magicbell": {
        "external_id": "user123"
      }
    }
  }
}
```

## Overrides

Overrides can be used to change the request body that Courier uses to send a message to MagicBell.

Below is an example of overriding the Category & Action URL parameters in MagicBell:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "recipient@example.com"
    },
    "data": {},
    "providers": {
      "magicbell": {
        "override": {
          "body": {
            "category": "new_message",
            "action_url": "https://example.com/example_link"
          }
        }
      }
    }
  }
}
```
