# Source: https://www.courier.com/docs/external-integrations/sms/africas-talking.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Africa's Talking

> Guide to integrating Africa's Talking SMS with Courier, including recipient profile setup and override options like custom short codes or sender IDs for advanced message customization.

## Setup

You will need an [Africa's Talking](https://africastalking.com/) account with an API key and application username. In Courier, navigate to the [Africa's Talking Integration](https://app.courier.com/integrations/catalog/africastalking-sms) page, enter your API key, username, and optionally a from short code or sender ID, then click "Save."

## Profile Requirements

To deliver a message to a recipient over Africa's Talking SMS, Courier must be provided the recipient's SMS-compatible telephone number. This value should be included in the recipient profile as `phone_number`.

```json  theme={null}
{
  "message": {
    "to": {
      "phone_number": "+27765559758"
    }
  }
}
```

## Overrides

You can use a provider override to replace what Courier sends to the Africa's Talking SMS API. For example, you can add a registered short code or alphanumeric sender ID from your Africa's Talking application:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "phone_number": "+27765559758"
    },
    "providers": {
      "africastalking-sms": {
        "override": {
          "body": {
            "from": "12345"
          }
        }
      }
    }
  }
}
```

Everything inside of `message.providers.africastalking-sms.override` will replace what Courier sends to the [Africa's Talking SMS API](https://developers.africastalking.com/docs/sms/overview).
