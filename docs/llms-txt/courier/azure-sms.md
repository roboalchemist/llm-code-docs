# Source: https://www.courier.com/docs/external-integrations/sms/azure-sms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure SMS

> Step-by-step guide for integrating Azure Communication Service SMS with Courier, including required recipient profile structure and how to use overrides for customizing sender, message content, and authentication settings.

## Setup

You will need an [Azure Communication Services](https://azure.microsoft.com/en-us/products/communication-services/) resource with an SMS-capable phone number. In the Azure portal, navigate to your Communication Services resource to get your endpoint URL and access key. In Courier, navigate to the [Azure SMS Integration](https://app.courier.com/integrations/catalog/azure-sms) page, enter your access key, endpoint, and from number, then click "Save."

## Profile Requirements

To deliver an SMS message through Azure SMS, Courier must be provided the recipient's SMS-compatible phone number. This value should be included in the recipient profile as `phone_number`.

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

Overrides can be used to change the request that Courier makes to Azure Communication Services. You can override the `accessKey`, `endpoint`, and `from` number via `config`, as well as the `message` text and `to` number via `body`.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "phone_number": "+12345678901"
    },
    "providers": {
      "azure-sms": {
        "override": {
          "body": {
            "to": "+10987654321",
            "message": "Override message content"
          },
          "config": {
            "from": "<override from number>",
            "accessKey": "<override access key>",
            "endpoint": "<override endpoint>"
          }
        }
      }
    }
  }
}
```
