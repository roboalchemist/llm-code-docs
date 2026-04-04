# Source: https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api.md

# Manage orders with the API

## Here you can find everything you need to integrate Order management using our API.

The actions you can execute on Klarna orders are grouped into three main categories:

- View and change orders
- Capture and track orders
- Refund and extend orders

In this section, you can find technical details of the API calls per category. Here are examples of common errors with troubleshooting suggestions:

| HTTP status code | Error code | Error message | Description |
|----------------|----------|-------------|-----------|
| * `502` * 503 * `504` | * `TEMPORARILY_UNAVAILABLE` | * "Temporarily unavailable". | The service is temporarily unavailable. For more information, see our [Escalation and retry policy.](https://docs.klarna.com/api/escalation-and-retry-policy/#escalation--retry-policy) |
| * `500` | * `INTERNAL_SERVER_ERROR` * `UNEXPECTED_ERROR` | * "Unexpected server error". | An unexpected server error occurred. For more information, see our [Escalation and retry policy.](https://docs.klarna.com/api/escalation-and-retry-policy/#escalation--retry-policy) |
| * `429` | * `TOO_MANY_REQUESTS` | * "Too many requests". | We received too many requests in a given amount of time (rate limiting). For more information, see the [Rate limit guide](https://docs.klarna.com/api/rate-limit/#rate-limit) . |
| * `422` | * `UNPROCESSABLE_ENTITY` * `INVALID_ADDRESS` | * "The size of the `shipping_info/shipping_company` value must be between 0 and 100". * "The shipping and/or billing address is invalid". | The service is unable to process this request. Refer to the [OpenAPI documentation](https://spec.openapis.org/oas/latest.html) to see if the request is valid. |
| * `413` | * `REQUEST_TOO_LARGE` | * "Request is too large". | This request is too large. Refer to the [OpenAPI documentation](https://spec.openapis.org/oas/latest.html) to see if the request is valid. |
| * `409` | * `CONFLICT` | N/A | This request conflicts with the current state of the target resource. For more information, see our [Escalation and retry policy.](https://docs.klarna.com/api/escalation-and-retry-policy/#escalation--retry-policy) |
| * `403` | * `NOT_ALLOWED` * REFUND_NOT_ALLOWED * `CANCEL_NOT_ALLOWED` | * "Resulting authorization amount 7000 cannot be less than the captured amount 8000 for order. Order authorization cannot be updated". * "Order has no captures. Refund not possible". * "Order has previous captures. Cancel not possible". | This operation is not allowed based on business rules. For more information, see our [Escalation and retry policy.](https://docs.klarna.com/api/escalation-and-retry-policy/#escalation--retry-policy) |
| * `404` | * `NO_SUCH_ORDER` * NO_SUCH_CAPTURE * `NOT_FOUND` | * "Order 5ef9a5b3-6c08-42e1-91a3-065dcae5c5dd cannot be found". * "Capture could not be found. Shipping info cannot be added to capture d25fb1a0-a6d9-4a65-8dac-cd7fb3a8dd24". * "Refund ec2119a1-cbb9-40a3-8fb8-ad7b7c109c87 cannot be found for order 5ef9a5b3-6c08-42e1-91a3-065dcae5c5dd". | The requested resource (order, capture, or refund) could not be found. Check if their IDs are correct. |
| * `400` | * `NOT_FOUND` | * "Refund ec2119a1-cbb9-40a3-8fb8-ad7b7c109c87 cannot be found for order 5ef9a5b3-6c08-42e1-91a3-065dcae5c5dd". | This is an invalid request. Refer to the [OpenAPI documentation](https://spec.openapis.org/oas/latest.html) to check validation rules. |