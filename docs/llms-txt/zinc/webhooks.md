# Source: https://zinc-staging.vercel.app/docs/v2/api-reference/order-updates/webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Webhooks

> Receive real-time notifications about order events

Webhooks allow you to receive real-time HTTP notifications when events occur on your orders. Instead of polling the API for updates, configure a webhook URL to receive automatic notifications.

## Configuration

Configure your webhook URL in the [Zinc dashboard](https://app.zinc.com) under Settings. You can also generate a webhook secret for signature verification.

### Webhook Secret

Your webhook secret is used to verify that incoming webhook requests are from Zinc. The secret format is:

```
zn_whsec_XXXXXXXXXXXXXXXXXXXXXXXX
```

<Warning>
  Keep your webhook secret secure. If compromised, rotate it immediately in the dashboard. Rotating the secret invalidates the previous one.
</Warning>

## Events

Zinc sends webhooks for the following order events:

| Event           | Description                                          |
| --------------- | ---------------------------------------------------- |
| `order.started` | Order has been created and queued for processing     |
| `order.placed`  | Order was successfully placed with the retailer      |
| `order.failed`  | Order failed after all retry attempts were exhausted |

## Payload Structure

All webhook payloads follow this structure:

```json  theme={null}
{
  "event": "order.placed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "order_placed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {}
}
```

### Payload Fields

| Field       | Type              | Description                                                            |
| ----------- | ----------------- | ---------------------------------------------------------------------- |
| `event`     | string            | The event type (e.g., `order.started`, `order.placed`, `order.failed`) |
| `order_id`  | string            | The UUID of the order                                                  |
| `status`    | string            | Current order status                                                   |
| `timestamp` | string (ISO 8601) | When the event occurred                                                |
| `data`      | object            | Additional event-specific data                                         |

### Event-Specific Data

**`order.placed`** includes price components:

```json  theme={null}
{
  "event": "order.placed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "order_placed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "price_components": {
      "subtotal": 1999,
      "shipping": 499,
      "tax": 150,
      "total": 2648
    }
  }
}
```

**`order.failed`** includes error information:

```json  theme={null}
{
  "event": "order.failed",
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "timestamp": "2026-01-15T14:30:00Z",
  "data": {
    "error_type": "product_not_found",
    "error": "The product is no longer available"
  }
}
```

## Security

Webhook requests include headers for verification:

| Header                | Description                          |
| --------------------- | ------------------------------------ |
| `Content-Type`        | Always `application/json`            |
| `X-Webhook-Signature` | HMAC-SHA256 signature of the payload |
| `X-Webhook-Event`     | The event type                       |

### Verifying Signatures

To verify a webhook is from Zinc, compute the HMAC-SHA256 signature of the raw request body using your webhook secret and compare it to the `X-Webhook-Signature` header.

**Python Example:**

```python  theme={null}
import hmac
import hashlib

def verify_webhook(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(
        secret.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)

# In your webhook handler
@app.post("/webhook")
async def handle_webhook(request: Request):
    payload = await request.body()
    signature = request.headers.get("X-Webhook-Signature")

    if not verify_webhook(payload, signature, WEBHOOK_SECRET):
        raise HTTPException(status_code=401, detail="Invalid signature")

    data = json.loads(payload)
    # Process the webhook event
```

**Node.js Example:**

```javascript  theme={null}
const crypto = require('crypto');

function verifyWebhook(payload, signature, secret) {
  const expected = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');
  return crypto.timingSafeEqual(
    Buffer.from(expected),
    Buffer.from(signature)
  );
}

// In your webhook handler
app.post('/webhook', (req, res) => {
  const signature = req.headers['x-webhook-signature'];

  if (!verifyWebhook(req.rawBody, signature, WEBHOOK_SECRET)) {
    return res.status(401).send('Invalid signature');
  }

  const event = req.body;
  // Process the webhook event
});
```

<Info>
  Always verify webhook signatures before processing the payload to ensure the request originated from Zinc.
</Info>

## Best Practices

1. **Respond quickly** - Return a 2xx status code as soon as possible. Process the webhook asynchronously if needed.

2. **Handle duplicates** - Webhooks may occasionally be delivered more than once. Use the `order_id` to deduplicate.

3. **Verify signatures** - Always validate the `X-Webhook-Signature` header before trusting the payload.

4. **Use HTTPS** - Configure an HTTPS endpoint to ensure webhook data is encrypted in transit.

5. **Log events** - Keep records of received webhooks for debugging and auditing.


Built with [Mintlify](https://mintlify.com).