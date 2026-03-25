# Source: https://www.courier.com/docs/external-integrations/email/amply.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Amply

> Send email notifications via Amply using Courier by including the recipient’s email in their profile, and optionally overriding fields like sender name or adding attachments through the providers.amply.override object.

## Setup

You will need a [Amply (SendAmply)](https://sendamply.com/) account. In Amply, create an Access Token from your account settings. In Courier, navigate to the [Amply Integration](https://app.courier.com/integrations/catalog/amply) page, enter your Access Token, From Email, and From Name, then click "Save."

## Profile Requirements

To deliver a message to a recipient over Amply, Courier must be provided the recipient's email address. This value should be included in the recipient profile as `email`.

```json title=JSON theme={null}
{
  "message": {
    // Recipient Profile
    "to": {
      "email": "alice@acme.com"
    }

    // ... rest of message definition
  }
}
```

## Overrides

You can use a provider override to replace what we send to Amply's Mail Send API. For example, you can use the following payload to override the sender name:

```json title=JSON theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "providers": {
      "amply": {
        "override": {
          "config": {
            "fromName": "Acme Notifications"
          }
        }
      }
    }
  }
}
```

Everything inside of `message.providers.amply.override` will replace what we send to Amply's Messages API. You can see all the available options by visiting [Amply API docs](https://docs.sendamply.com/reference/mail-send).

## Sending Attachments

To include an attachment in the email, you can use the following override:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "data": {
      "hello": "world"
    },
    "providers": {
      "amply": {
        "override": {
          "attachments": [
            {
              "filename": "billing.pdf",
              "contentType": "application/pdf",
              "data": "Q29uZ3JhdHVsYXRpb25zLCB5b3UgY2FuIGJhc2U2NCBkZWNvZGUh"
            }
          ]
        }
      }
    }
  }
}
```
