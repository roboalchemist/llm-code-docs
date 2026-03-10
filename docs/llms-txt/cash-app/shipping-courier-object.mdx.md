# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/data-models/shipping-courier-object.mdx

***

## stoplight-id: 612qub8eb719h

# Shipping Courier object

## Attributes

| Attribute | Type   | Description                                                                                                                 |
| --------- | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| shippedAt | string | The date and time when the order was shipped, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. |
| name      | string | The name of the courier. This is limited to 128 characters.                                                                 |
| tracking  | string | The tracking number provided by the courier. Limited to 128 characters.                                                     |
| priority  | string | The shipping priority. If provided, must be either "STANDARD" or "EXPRESS".                                                 |

## Example Shipping Courier object

```json
{
  "shippedAt": "2024-01-01T00:00:00-08:00",
  "name": "FedEx",
  "tracking": "000 000 000 000",
  "priority": "STANDARD"
}
```
