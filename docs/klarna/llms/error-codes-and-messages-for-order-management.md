# Source: https://docs.klarna.com/resources/developer-tools/error-handling/error-codes-and-messages-for-order-management.md

# Error codes and messages for Order Management

## Check out our usual error messages and what they mean

## Summary of possible errors

| **HTTPS status code** | **Error code**          |
|-----------------------|-------------------------|
| 400                   | NOT_FOUND               |
| 403                   | XXX_NOT_ALLOWED         |
| 404                   | NO_SUCH_XXX             |
| 404                   | NOT_FOUND               |
| 409                   | CONFLICT                |
| 413                   | REQUEST_TOO_LARGE       |
| 422                   | UNPROCESSABLE_ENTITY    |
| 422                   | INVALID_ADDRESS         |
| 429                   | TOO_MANY_REQUESTS       |
| 500                   | INTERNAL_SERVER_ERROR   |
| 500                   | UNEXPECTED_ERROR        |
| 502/503/504           | TEMPORARILY_UNAVAILABLE |

## Details of possible errors

### 400 - NOT_FOUND

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[Refund xxxxxxx-xxxx-xxxxxxxxxxxxxxx cannot be found for order xxxxxxx-xxxx-xxxxxxxxxxxxxxx]` | This is an invalid request. | Refer to the [OpenAPI documentation](https://spec.openapis.org/oas/latest.html) to check validation rules. |

### 403 - CAPTURE_NOT_ALLOWED

`CAPTURE_NOT_ALLOWED` error is only present as response to `capture` request. There are multiple reasons for this error to occur depending on these the customer may not get the products and the merchant won't get settled for the order. The customer might have to place the same order again.

| **Error message** | **Description** | **Error handling** |
|----|----|----|
| `[Capture not allowed]` | The order might be cancelled or expired, or the captured amount might be higher than the remaining authorized amount. |  |

### 403 - CANCEL_NOT_ALLOWED

`CANCEL_NOT_ALLOWED` error is only present as response to `cancel` request.

| **Error message** | **Description** | **Error handling** |
|----|----|----|
| `[Order has previous captures. Cancel not possible]` | Once an order is captured, it can not be cancelled anymore. For more information, see our [Escalation and retry policy.](https://docs.klarna.com/api/escalation-and-retry-policy.md) |  |

### 403 - NOT_ALLOWED

NOT_ALLOWED error could be present in the following requests:

- `release_authorization`
- `extend_authorization_time`
- `update_authorization`
- `update_order_customer_details`
- `update_merchant_references`

Depending on the operation this error can affect the customer communication, shipping details or authorization expire time.

| **Error message** | **Description** | **Error handling** |
|----|----|----|
| `[Resulting authorization amount xxx cannot be less than the captured amount xxx for order. Order authorization cannot be updated]` | The capture amount must always be higher than the authorized amount. | See our [Escalation and retry policy.](https://docs.klarna.com/api/escalation-and-retry-policy.md) |

### 403 - REFUND_NOT_ALLOWED

REFUND_NOT_ALLOWED error is only present as response to `refund` request. If the order has already been cancelled or fully refunded, the failed refund call doesn't have any impact on the customer. In cases where the attempted refunded amount is greater than the captured amount, the whole refund might fail, and customer's money be left with the merchant.

| **Error message** | **Description** | **Error handling** |
|----|----|----|
| `[Order has no captures. Refund not possible]` | An order or value can only be refunded if it has been previously captured or partially captured. | See our [Escalation and retry policy.](https://docs.klarna.com/api/escalation-and-retry-policy.md) |

### 404 - NO_SUCH_ORDER

`NO_SUCH_ORDER` error is only present as response to `capture` request.

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[Order xxxxxxx-xxxx-xxxxxxxxxxxxxxx cannot be found]` | The requested resource (order, capture, or refund) could not be found. Check if their IDs are correct. | Check if their IDs are correct. |

### 404 - NO_SUCH_CAPTURE

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[Capture could not be found. Shipping info cannot be added to capture xxxxxxx-xxxx-xxxxxxxxxxxxxxx]` | The requested resource (order, capture, or refund) could not be found. | Check if their IDs are correct. |

### 

### 404 - NOT_FOUND

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[Refund xxxxxxx-xxxx-xxxxxxxxxxxxxxx cannot be found for order xxxxxxx-xxxx-xxxxxxxxxxxxxxx]` | The requested resource (order, capture, or refund) could not be found. | Check if their IDs are correct. |

### 409 - CONFLICT

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[]` | This request conflicts with the current state of the target resource. | See our [Escalation and retry policy.](https://docs.klarna.com/api/escalation-and-retry-policy.md) |

### 413 - REQUEST_TOO_LARGE

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[Request is too large]` | This request is too large. | Refer to the [OpenAPI documentation](https://spec.openapis.org/oas/latest.html)to see if the request is valid. |

### 422 - INVALID_ADDRESS

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[The shipping and/or billing address is invalid]` | The service is unable to process this request. | Refer to the [OpenAPI documentation](https://spec.openapis.org/oas/latest.html) to see if the request is valid. |

### 422 - UNPROCESSABLE_ENTITY

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[The size of theshipping_info/shipping_companyvalue must be between 0 and 100]` | The service is unable to process this request. | Refer to the [OpenAPI documentation](https://spec.openapis.org/oas/latest.html) to see if the request is valid. |

### 429 - TOO_MANY_REQUESTS

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[Too many requests]` | We received too many requests in a given amount of time (rate limiting). | For more information, see the [Rate limit guide](https://docs.klarna.com/api/rate-limit.md). |

### 500 - INTERNAL_SERVER_ERROR / UNEXPECTED_ERROR

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[Unexpected server error]` | An unexpected server error occurred. | For more information, see our [Escalation and retry policy.](https://docs.klarna.com/api/escalation-and-retry-policy.md) |

### 503/503/504 - TEMPORARILY_UNAVAILABLE

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[Temporarily unavailable]` | The service is temporarily unavailable. | For more information, see our [Escalation and retry policy.](https://docs.klarna.com/api/escalation-and-retry-policy.md) |