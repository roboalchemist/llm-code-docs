# Source: https://zinc-staging.vercel.app/docs/v2/api-reference/introduction/error-handling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Error Handling

> Understanding error responses from the Zinc API

The Zinc API uses conventional HTTP response codes to indicate the success or failure of an API request.

## HTTP Status Codes

| Status Code | Description                                                   |
| ----------- | ------------------------------------------------------------- |
| `200`       | Success - The request was successful                          |
| `201`       | Created - A new resource was created successfully             |
| `400`       | Bad Request - The request was malformed or invalid            |
| `401`       | Unauthorized - Invalid or missing authentication              |
| `402`       | Payment Required - Payment or wallet issue                    |
| `403`       | Forbidden - You don't have permission to access this resource |
| `404`       | Not Found - The requested resource does not exist             |
| `409`       | Conflict - Resource already exists                            |
| `422`       | Unprocessable Entity - Validation error                       |
| `500`       | Internal Server Error - Something went wrong on our end       |
| `502`       | Bad Gateway - External service error                          |

## Error Response Format

All error responses follow a consistent structure:

```json  theme={null}
{
  "code": "error_code",
  "message": "Human-readable error message",
  "details": {
    "field": "Additional context about the error"
  }
}
```

## API Error Codes

### General Errors

| Error Code         | Description                                                              |
| ------------------ | ------------------------------------------------------------------------ |
| `not_found`        | Resource was not found                                                   |
| `validation_error` | A parameter was incorrect or missing. Check details for more information |
| `bad_request`      | The request was malformed or invalid                                     |
| `already_exists`   | Resource already exists (e.g., duplicate idempotency key)                |
| `internal_error`   | Something went wrong with our internal systems                           |

#### Example

```json  theme={null}
{
  "code": "validation_error",
  "message": "Invalid request parameters",
  "details": {
    "products": "At least one product is required"
  }
}
```

### Authentication Errors

| Error Code      | Description                                |
| --------------- | ------------------------------------------ |
| `unauthorized`  | Authentication is required for this action |
| `forbidden`     | You do not have permission for this action |
| `invalid_token` | Your API token is invalid                  |
| `token_expired` | Your API token has expired                 |

#### Example

```json  theme={null}
{
  "code": "invalid_token",
  "message": "The provided API token is not valid"
}
```

### Wallet & Payment Errors

| Error Code                | Description                                |
| ------------------------- | ------------------------------------------ |
| `insufficient_funds`      | Insufficient funds in wallet for the order |
| `payment_failed`          | Payment operation failed                   |
| `payment_method_required` | No default payment method configured       |
| `invalid_payment_method`  | The provided payment method is invalid     |

#### Example

```json  theme={null}
{
  "code": "insufficient_funds",
  "message": "Your wallet balance is insufficient for this order",
  "details": {
    "required": 4999,
    "available": 1000
  }
}
```

### Order Request Errors

| Error Code                 | Description                                               |
| -------------------------- | --------------------------------------------------------- |
| `invalid_shipping_address` | The shipping address failed validation                    |
| `url_unreachable`          | The product URL provided is inaccessible                  |
| `invalid_variant`          | Product variant not provided or not found on product page |
| `out_of_stock`             | Product is not currently available for purchase           |
| `shipping_unavailable`     | Shipping to this address is not available                 |
| `non_us_retailer`          | Only US retailer sites are supported                      |
| `order_not_cancellable`    | Order cannot be cancelled due to its current status       |

#### Example

```json  theme={null}
{
  "code": "invalid_shipping_address",
  "message": "The shipping address could not be validated",
  "details": {
    "field": "postal_code",
    "reason": "Postal code does not match city/state"
  }
}
```

### External Service Errors

| Error Code               | Description                     |
| ------------------------ | ------------------------------- |
| `external_service_error` | An external service call failed |

#### Example

```json  theme={null}
{
  "code": "external_service_error",
  "message": "Unable to connect to external service. Please try again."
}
```

## Order Processing Errors

When an order fails during processing, the `error_type` field in the order response or webhook payload contains one of these codes:

### Product Errors

| Error Type                     | Description                                  |
| ------------------------------ | -------------------------------------------- |
| `product_not_found`            | Product page doesn't exist or was removed    |
| `product_out_of_stock`         | Product is out of stock                      |
| `product_unavailable`          | Product exists but cannot be purchased       |
| `invalid_product_url`          | URL is malformed or not a valid product page |
| `product_variant_required`     | Product requires a variant selection         |
| `product_variant_unavailable`  | Selected variant is not available            |
| `product_quantity_unavailable` | Requested quantity is not available          |

#### Example

```json  theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "product_out_of_stock",
    "error": "The requested product is currently out of stock"
  }
}
```

### Price Errors

| Error Type           | Description                               |
| -------------------- | ----------------------------------------- |
| `max_price_exceeded` | Total price exceeds the `max_price` limit |

#### Example

```json  theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "max_price_exceeded",
    "error": "Order total of $52.99 exceeds max_price of $50.00"
  }
}
```

### Cart & Checkout Errors

| Error Type           | Description                                    |
| -------------------- | ---------------------------------------------- |
| `add_to_cart_failed` | Could not add product to cart                  |
| `cart_empty`         | Cart became empty during checkout              |
| `checkout_blocked`   | Checkout blocked (captcha, verification, etc.) |
| `checkout_failed`    | Generic checkout failure                       |

#### Example

```json  theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "checkout_blocked",
    "error": "Checkout requires additional verification"
  }
}
```

### Shipping Errors

| Error Type                    | Description                                |
| ----------------------------- | ------------------------------------------ |
| `shipping_address_invalid`    | Address validation failed on retailer site |
| `shipping_unavailable`        | Cannot ship to the given address           |
| `shipping_method_unavailable` | No shipping methods available              |

#### Example

```json  theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "shipping_unavailable",
    "error": "This item cannot be shipped to the selected address"
  }
}
```

### Payment Errors

| Error Type               | Description                      |
| ------------------------ | -------------------------------- |
| `payment_declined`       | Payment was declined by retailer |
| `payment_method_invalid` | Payment method not accepted      |
| `payment_failed`         | Generic payment failure          |

#### Example

```json  theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "payment_declined",
    "error": "The payment method was declined by the retailer"
  }
}
```

### Account Errors

| Error Type                      | Description                             |
| ------------------------------- | --------------------------------------- |
| `login_failed`                  | Could not log into retailer account     |
| `session_expired`               | Session expired during checkout         |
| `account_locked`                | Retailer account is locked or suspended |
| `account_verification_required` | Account needs verification              |

#### Example

```json  theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "login_failed",
    "error": "Unable to authenticate with retailer account"
  }
}
```

### Retailer Errors

| Error Type               | Description                              |
| ------------------------ | ---------------------------------------- |
| `retailer_unavailable`   | Retailer website is down or inaccessible |
| `retailer_not_supported` | Retailer is not supported                |
| `retailer_rate_limited`  | Rate limited by retailer                 |

#### Example

```json  theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "retailer_unavailable",
    "error": "The retailer website is currently unavailable"
  }
}
```

### Quantity Limit Errors

| Error Type                | Description                           |
| ------------------------- | ------------------------------------- |
| `quantity_limit_exceeded` | Retailer has purchase quantity limits |
| `order_limit_exceeded`    | Account has reached order limits      |

#### Example

```json  theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "quantity_limit_exceeded",
    "error": "Maximum purchase quantity for this item is 3"
  }
}
```


Built with [Mintlify](https://mintlify.com).