# Source: https://www.courier.com/docs/external-integrations/email/sparkpost.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SparkPost

> Send emails via SparkPost using Courier by including the recipient’s email in their profile and optionally using overrides to customize the Transmissions API request, such as adding attachments or modifying email content.

## Setup

You will need a [SparkPost](https://www.sparkpost.com/) account. In SparkPost, create an API key with "Transmissions: Read/Write" permissions. In Courier, navigate to the [SparkPost Integration](https://app.courier.com/integrations/catalog/sparkpost) page, enter your API key and From Address, then click "Save."

## Profile Requirements

To deliver a message to a recipient over SparkPost, Courier must be provided the recipient's email address. This value should be included in the recipient profile as `email`.

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

You can use a provider override to replace what we send to SparkPost's Transmissions API. For example, you can add an attachment to your request:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "email": "alice@acme.com"
    },
    "providers": {
      "sparkpost": {
        "override": {
          "body": {
            "content": {
              "attachments": [
                {
                  "name": "billing.pdf",
                  "type": "application/pdf",
                  "data": "Q29uZ3JhdHVsYXRpb25zLCB5b3UgY2FuIGJhc2U2NCBkZWNvZGUh"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Everything inside of `message.providers.sparkpost.override` will replace what we send to SparkPost's Transmissions API. You can see all the available options by visiting [SparkPost API docs](https://developers.sparkpost.com/api/transmissions/#header-request-body).
