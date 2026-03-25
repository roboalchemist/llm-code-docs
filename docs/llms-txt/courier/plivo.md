# Source: https://www.courier.com/docs/external-integrations/sms/plivo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plivo

> Send SMS notifications via Plivo using Courier by configuring recipient phone numbers in E.164 format, with delivery status tracking.

## Setup

You will need a [Plivo](https://www.plivo.com/) account with an Auth ID, Auth Token, and a from number. In Courier, navigate to the [Plivo Integration](https://app.courier.com/integrations/catalog/plivo) page, enter your Auth ID, Auth Token, and from number, then click "Save."

## Profile Requirements

To deliver a message to a recipient over Plivo, Courier must be provided the recipient's SMS-compatible telephone number. Be sure that all phone numbers include country code, area code, and phone number without spaces or dashes. This value should be included in the recipient profile as `phone_number`.

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

Plivo does not currently support provider-level overrides through Courier.

## Delivery Tracking

Plivo supports automatic delivery status polling. Once the integration is configured, Courier will poll Plivo's API for delivery status updates and reflect them in the [message logs](https://app.courier.com/logs).
