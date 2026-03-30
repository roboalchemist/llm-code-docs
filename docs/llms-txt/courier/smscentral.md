# Source: https://www.courier.com/docs/external-integrations/sms/smscentral.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SMSCentral

> Send SMS messages through SMSCentral using Courier by including the recipient's phone number in the profile, with support for body and config overrides.

## Setup

You will need an [SMSCentral](https://www.smscentral.com.au/) account with a username and password. In Courier, navigate to the [SMSCentral Integration](https://app.courier.com/integrations/catalog/smscentral) page, enter your username and password, then click "Save."

## Profile Requirements

To deliver an SMS message through SMSCentral, Courier must be provided the recipient's SMS-compatible phone number. This value should be included in the recipient profile as `phone_number`.

```json  theme={null}
{
  "message": {
    "to": {
      "phone_number": "+12025550156"
    }
  }
}
```

## Overrides

Overrides can be used to change the request body and credentials that Courier uses to send a message through SMSCentral. You can override the `username` and `password` via `config`, and the `message`, `originator`, and `reference` fields via `body`.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "phone_number": "+12345678901"
    },
    "providers": {
      "smscentral": {
        "override": {
          "body": {
            "message": "Override message content",
            "originator": "MyCompany",
            "reference": "ref-12345"
          },
          "config": {
            "username": "<override username>",
            "password": "<override password>"
          }
        }
      }
    }
  }
}
```

Everything inside of `message.providers.smscentral.override` will replace what Courier sends to the [SMSCentral API](https://www.smscentral.com.au/sms-api/rest-api/).
