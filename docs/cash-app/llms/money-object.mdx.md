# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/data-models/money-object.mdx

***

## stoplight-id: r9l2ogztad4v6

# Money object

## Attributes

| Attribute | Type   | Status   | Description                                                                                                                                                                                                        |
| --------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| amount    | string | required | The amount is a string representation of a decimal number, rounded to 2 decimal places.                                                                                                                            |
| currency  | string | required | The currency in [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format. Supported values include "USD". However, the value provided must correspond to the currency of the Merchant account making the request. |

## 422 Errors

Where a Money object is included in an API request, it will be validated according to the specification above. Invalid Money objects will trigger a **422 Unprocessable Entity response**. The following is a list of common examples.

| Example                                                                              | errorCode              | message                                                                    |
| ------------------------------------------------------------------------------------ | ---------------------- | -------------------------------------------------------------------------- |
| `amount` is omitted or null                                                          | invalid\_object        | `{Money object}.amount` Amount field required                              |
| `amount` has more than 2 decimal places                                              | invalid\_object	amount | must be a valid ISO 4217 format value                                      |
| `amount` includes a thousands separator comma, for example: "1,000"                  | invalid\_amount        | Amount must be a valid ISO 4217 format value                               |
| `amount` is not a decimal number, for example: "FREE", "\$2" or an empty string      | invalid\_object        | `{Money object}.amount` Amount field must be a valid ISO 4217 format value |
| `currency` is omitted or null                                                        | invalid\_object        | `{Money object}.currency` Currency field required                          |
| `currency` is not a valid currency code, not all uppercase or an empty string        | invalid\_object        | `{Money object}.currency` Currency not supported for this merchant         |
| `currency` is supported by Cash App Afterpay, but not valid for the Merchant account | unsupported\_currency  | An error occurred                                                          |

## Example Money object

```json
{
  "amount": "29.99",
  "currency": "USD"
}

```
