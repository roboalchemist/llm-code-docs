# Source: https://www.courier.com/docs/external-integrations/sms/intro-to-sms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SMS Providers

> Learn how to integrate Courier with SMS providers and use provider-level overrides to customize sender numbers, message content, and authentication in SMS notifications.

Courier integrates with a range of SMS providers. To send an SMS, the recipient profile must include a `phone_number` field in E.164 format:

```json  theme={null}
{
  "message": {
    "to": {
      "phone_number": "+12025550156"
    },
    "template": "NOTIFICATION_TEMPLATE_ID"
  }
}
```

When a notification template includes an SMS channel, Courier selects the configured SMS provider based on your [channel priority](/platform/sending/channel-priority) and routing rules. If the primary provider fails, Courier automatically [fails over](/platform/sending/failover) to backup providers when configured.

## Available SMS Providers

| Provider                                                       | Description                                                                   |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [Twilio](/external-integrations/sms/twilio)                    | Full-featured SMS with Messaging Services, delivery tracking, and MMS support |
| [Vonage](/external-integrations/sms/vonage)                    | SMS delivery via the Vonage (formerly Nexmo) API                              |
| [Telnyx](/external-integrations/sms/telnyx)                    | Programmable SMS with config and body overrides                               |
| [Sinch](/external-integrations/sms/sinch)                      | SMS delivery via the Sinch REST API                                           |
| [Plivo](/external-integrations/sms/plivo)                      | SMS delivery via the Plivo API                                                |
| [MessageBird](/external-integrations/sms/messagebird)          | SMS delivery via the MessageBird API                                          |
| [MessageMedia](/external-integrations/sms/messagemedia)        | SMS with HMAC auth and delivery webhooks                                      |
| [Azure SMS](/external-integrations/sms/azure-sms)              | SMS via Azure Communication Services                                          |
| [TextUs](/external-integrations/sms/textus)                    | Business texting via the TextUs API                                           |
| [Africa's Talking](/external-integrations/sms/africas-talking) | SMS delivery for African markets via the Africa's Talking API                 |
| [SMSCentral](/external-integrations/sms/smscentral)            | SMS delivery via the SMSCentral API                                           |

## SMS Provider Overrides

Overrides let you modify parts of an SMS at send time without changing your notification template. They are passed in the `message` payload of a [Send request](/api-reference/send/message) and applied just before Courier hands the message off to the provider.

Provider overrides (`message.providers.<key>.override`) target a single provider and can pass through fields specific to that provider's API. Most SMS providers support:

* **`body`** overrides to change the message text, recipient number, or other request body fields.
* **`config`** overrides to swap credentials or sender numbers at send time.

Each provider page documents its supported override schema.

<Tip>
  Can't find a provider? Send us a chat or email [support@courier.com](mailto:support@courier.com)
</Tip>
