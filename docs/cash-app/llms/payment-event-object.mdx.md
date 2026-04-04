# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/data-models/payment-event-object.mdx

***

## stoplight-id: wd8kdpsmfwytj

# Payment Event object

## Attributes

| Attribute                     | Type                                                                         | Description                                                                                                                                                                                                                                            |
| ----------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id                            | string                                                                       | The unique, Cash App Afterpay-generated event ID.                                                                                                                                                                                                      |
| created                       | string                                                                       | A UTC timestamp of the event creation time, in ISO 8601 format.                                                                                                                                                                                        |
| expires                       | string                                                                       | A UTC timestamp of the "AUTH\_APPROVED" event expiration time, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. Null for other event types.                                                                               |
| type                          | string                                                                       | The event type. Will be one of: "AUTH\_APPROVED", "AUTH\_DECLINED", "CAPTURED", "CAPTURE\_DECLINED", "VOIDED", "EXPIRED".                                                                                                                              |
| amount                        | [Money](/cash-app-afterpay/api-reference/reference/data-models/money-object) | The amount associated with the event.                                                                                                                                                                                                                  |
| paymentEventMerchantReference | string                                                                       | A unique reference for an individual payment capture event. If provided on [Capture Full Payment](/cash-app-afterpay/api-reference/reference/payments/capture-full-payment), the value will appear in the daily settlement file as "Payment Event ID". |

## Example Payment Event object

```json
{
  "id" : "1OUR16OTqL3DgJ3ELlwKowU9v6K",
  "created" : "2024-01-01T00:00:00.000Z",
  "expires" : "2024-01-01T00:00:00.000Z",
  "type" : "AUTH_APPROVED",
  "amount" : {
    "amount" : "100.00",
    "currency" : "USD"
  },
  "paymentEventMerchantReference" : null
}
```
