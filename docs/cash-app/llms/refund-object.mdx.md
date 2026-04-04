# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/data-models/refund-object.mdx

***

## stoplight-id: d50fjlrlx254c

# Refund object

## Attributes

| Attribute               | Type                                                                                    | Description                                                                                                                                                                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| requestId               | string                                                                                  | A unique request ID, required (in conjunction with `merchantReference`) for safe retries. We recommend that merchants generate a UUID for each unique refund. Max character length = 64.                                                |
| amount                  | [Money](/cash-app-afterpay/api-reference/reference/data-models/money-object) (required) | The refund amount.                                                                                                                                                                                                                      |
| merchantReference       | string                                                                                  | The merchant's corresponding refund ID or reference, required (in conjunction with `requestId`) for safe retries. Max character length = 64.                                                                                            |
| refundId                | string                                                                                  | The unique, Cash App Afterpay-generated refund ID.                                                                                                                                                                                      |
| refundedAt              | string                                                                                  | A UTC timestamp of the refund creation time, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.                                                                                                              |
| refundMerchantReference | string                                                                                  | A unique reference for the individual refund event. If provided, the value appears in the daily settlement file as "Payment Event ID". In most cases, this holds the same value as the `merchantReference`. Max character length = 128. |

## Example Refund object

```json
{
  "requestId" : "956946da-4863-4797-aa7c-540050faf922",
  "amount" : {  
    "amount" : "10.00",
    "currency" : "USD"
  },
  "merchantReference" : "merchantRefundId-1234",
  "refundId" : "67890123",
  "refundedAt" : "2024-01-01T00:00:00.000Z",
  "refundMerchantReference" : "merchantRefundId-1234"
}
```
