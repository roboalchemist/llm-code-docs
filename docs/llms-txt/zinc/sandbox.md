# Source: https://zinc-staging.vercel.app/docs/v2/api-reference/introduction/sandbox.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sandbox & Testing

> Test your integration without placing real orders

The Zinc API provides a sandbox environment for testing your integration without placing real orders or incurring charges. Test mode uses isolated data and simulates various order scenarios.

## Enabling Test Mode

Use an API key with the `zn_test_` prefix:

```bash  theme={null}
curl https://api.zinc.com/orders \
  -H "Authorization: Bearer zn_test_abc123..."
```

<Info>
  Test mode uses a separate sandbox database. Orders created in test mode are
  completely isolated from production data.
</Info>

## Test Products

Use these special product URLs to simulate different order scenarios:

| Product URL                                                | Scenario             | Description                       |
| ---------------------------------------------------------- | -------------------- | --------------------------------- |
| `https://zinc.com/shop/products/test-success`              | Success              | Order completes successfully      |
| `https://zinc.com/shop/products/test-out-of-stock`         | Out of Stock         | Product is unavailable            |
| `https://zinc.com/shop/products/test-price-exceeded`       | Price Exceeded       | Total exceeds `max_price`         |
| `https://zinc.com/shop/products/test-invalid-address`      | Invalid Address      | Shipping address validation fails |
| `https://zinc.com/shop/products/test-url-unreachable`      | URL Unreachable      | Product URL is inaccessible       |
| `https://zinc.com/shop/products/test-invalid-variant`      | Invalid Variant      | Variant selection required        |
| `https://zinc.com/shop/products/test-shipping-unavailable` | Shipping Unavailable | Cannot ship to address            |
| `https://zinc.com/shop/products/test-insufficient-funds`   | Insufficient Funds   | Wallet balance too low            |

### Get Test Products Programmatically

```bash  theme={null}
curl https://api.zinc.com/orders/test-products \
  -H "Authorization: Bearer <your_api_key>"
```

#### Response

```json  theme={null}
{
  "products": [
    {
      "url": "https://zinc.com/shop/products/test-success",
      "scenario": "success",
      "name": "Success",
      "is_synchronous_error": false
    },
    {
      "url": "https://zinc.com/shop/products/test-invalid-address",
      "scenario": "invalid_address",
      "name": "Invalid Address",
      "is_synchronous_error": true
    }
  ]
}
```

## Error Timing

Test scenarios produce errors at different stages:

### Synchronous Errors

These errors occur immediately when creating the order:

* `test-invalid-address` - Returns `invalid_shipping_address` error
* `test-url-unreachable` - Returns `url_unreachable` error
* `test-insufficient-funds` - Returns `insufficient_funds` error

#### Example

```bash  theme={null}
curl -X POST https://api.zinc.com/orders \
  -H "Authorization: Bearer zn_test_abc123..." \
  -H "Content-Type: application/json" \
  -d '{
    "products": [{"url": "https://zinc.com/shop/products/test-invalid-address"}],
    "shipping_address": {...},
    "max_price": 5000
  }'
```

```json  theme={null}
{
  "code": "invalid_shipping_address",
  "message": "The shipping address failed validation (test scenario)"
}
```

### Asynchronous Errors

These errors occur during order processing and are delivered via webhooks:

* `test-out-of-stock` - Order fails with `product_out_of_stock`
* `test-price-exceeded` - Order fails with `max_price_exceeded`
* `test-invalid-variant` - Order fails with `invalid_variant`
* `test-shipping-unavailable` - Order fails with `shipping_unavailable`

The order is created successfully, but transitions to `failed` status during processing.

## Test Success Scenario

The `test-success` product simulates a complete successful order:

```bash  theme={null}
curl -X POST https://api.zinc.com/orders \
  -H "Authorization: Bearer zn_test_abc123..." \
  -H "Content-Type: application/json" \
  -d '{
    "products": [{"url": "https://zinc.com/shop/products/test-success"}],
    "shipping_address": {
      "name": "John Smith",
      "address_line_1": "123 Main Street",
      "city": "Seattle",
      "state": "WA",
      "postal_code": "98101",
      "country": "US",
      "phone": "206-555-0100"
    },
    "max_price": 5000
  }'
```

### Successful Test Order Response

When retrieved after processing:

```json  theme={null}
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "order_placed",
  "merchant_order_id": "TEST-550e8400",
  "tracking_numbers": [
    {
      "carrier": "usps",
      "tracking_number": "ZINC_TEST_123456789"
    }
  ],
  "price_components": {
    "subtotal": 4500,
    "tax": 250,
    "shipping": 150,
    "total": 4900
  }
}
```

## Skipped Validations

In test mode, the following validations are bypassed to simplify testing:

* Wallet balance checks
* US retailer URL validation
* URL reachability validation
* Shipping address country validation
* Address verification via external APIs

<Warning>
  Test mode behavior differs from production. Always perform final testing with
  real orders before going live.
</Warning>

## Data Isolation

Test mode data is completely isolated:

* Orders created in test mode are stored in a sandbox database
* Test orders do not appear in production order lists
* Production orders do not appear in test mode
* Wallet balances are separate between test and production

## Best Practices

1. **Start with test mode** - Build and test your entire integration using test products before switching to production

2. **Test all scenarios** - Use each test product to verify your error handling works correctly

3. **Test webhooks** - Configure webhooks and verify you receive events for both successful and failed test orders

4. **Verify error handling** - Ensure your application gracefully handles both synchronous and asynchronous errors

5. **Use consistent mode** - Don't mix test and production API keys in the same environment


Built with [Mintlify](https://mintlify.com).