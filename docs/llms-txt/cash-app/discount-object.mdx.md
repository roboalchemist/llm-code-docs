# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/data-models/discount-object.mdx

***

## stoplight-id: 1ffjj1ey7gb0t

# Discount object

## Attributes

| Attribute   | Type                                                                         | Status   | Description                                                 |
| ----------- | ---------------------------------------------------------------------------- | -------- | ----------------------------------------------------------- |
| displayName | string                                                                       | required | A display name for the discount. Limited to 128 characters. |
| amount      | [Money](/cash-app-afterpay/api-reference/reference/data-models/money-object) | required | The discount amount.                                        |

## Example Discount object

```json
{
  "displayName": "New Customer Coupon",
  "amount": {
    "amount": "29.99",
    "currency": "USD"
  }
}
```
