# Source: https://www.courier.com/docs/external-integrations/email/mailjet.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Mailjet

> Learn how to send email notifications using Courier and Mailjet, including setting up recipient profiles, using message overrides, and attaching files via Mailjet’s Send API.

## Setup

You will need a [Mailjet](https://www.mailjet.com/) account. In Mailjet, navigate to [API Key Management](https://app.mailjet.com/account/apikeys) to get your Public Key and Private Key. In Courier, navigate to the [Mailjet Integration](https://app.courier.com/integrations/catalog/mailjet) page, enter both keys and your From Address, then click "Save."

## Profile Requirements

To deliver a message to a recipient over Mailjet, Courier must be provided the recipient's email address. This value should be included in the recipient profile as `email`.

```json  theme={null}
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

You can use a provider override to replace what we send to Mailjet's Send API. For example, you can add an attachment to your request:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "providers": {
      "mailjet": {
        "override": {
          "body": {
            "Attachments": [
              {
                "ContentType": "text/plain",
                "Filename": "test.txt",
                "content": "VGhpcyBpcyB5b3VyIGF0dGFjaGVkIGZpbGUhISEK"
              }
            ]
          }
        }
      }
    }
  }
}
```

Everything inside of `message.providers.mailjet.override` will replace what we send to Mailjet's Send API. You can see all the available options by visiting [Mailjet API docs](https://dev.mailjet.com/email/guides/send-api-V3/).
