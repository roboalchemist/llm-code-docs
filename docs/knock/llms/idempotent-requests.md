# Source: https://docs.knock.app/api-reference/overview/idempotent-requests.md

# Idempotent requests

Knock supports [idempotency](https://en.wikipedia.org/wiki/Idempotence) so that requests can be retried safely without unintended side effects.

To perform an idempotent request, set an `Idempotency-Key` header on your request. This idempotency key is a unique string of up to 255 characters that you generate for each request. It is used to identify and prevent the duplicate processing of requests. If you retry a request with the same idempotency key within 24 hours from the original request, Knock will return the same response as the original request. Idempotent requests are expected to be identical. To prevent accidental misuse, Knock returns an error when incoming parameters don't match those from the original request.

Idempotency keys can be random UUIDs, or they can have some meaning in your application. For example, if you are sending a notification after a user has placed an order, you could use a key that is a combination of the reason for the notification, the user ID, and the order ID (e.g. `order-placed:user-123:order-456`). If your user then cancels the order, you could use an idempotency key like `order-cancelled:user-123:order-456`. This will ensure each type of notification is only sent once, even if your system retries the request multiple times.

If you are making calls to Knock from a job queue, the ID of the job can be a good choice for an idempotency key. If the job fails and is retried, the same idempotency key will be used.

> **The default idempotency window for the Knock API is 24 hours.** support@knock.app.

```json title="Response headers"
{
  "idempotent-replayed": "true",
  "original-x-request-id": "F1FIj5XwD_m4h0sAASfi"
}
```
