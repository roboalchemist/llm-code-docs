# Source: https://docs.ultravox.ai/webhooks/securing-webhooks.md

# Securing Webhooks

> Learn how to verify webhook authenticity and protect your endpoints from malicious requests.

Webhook security is crucial for protecting your application from malicious requests and ensuring that you only process authentic notifications from Ultravox. This guide covers how to implement proper webhook verification.

## Why Webhook Security Matters

Without proper verification, anyone could send fake webhook requests to your endpoint, potentially:

* Triggering unauthorized actions in your application or bypassing your business logic
* Corrupting your data with false information
* Overwhelming your system with spam requests

## How Ultravox Secures Webhooks

Ultravox uses HMAC-SHA256 signatures to ensure webhook authenticity. Each webhook request includes cryptographic proof that:

1. The request came from Ultravox
2. The payload hasn't been tampered with
3. The request is recent (not a replay attack)

## Securing Your Webhooks

You can optionally choose to secure your webhooks with a key. When creating a webhook, a secret key is automatically generated for you or you can choose to provide your own secret. You can update or patch your webhooks to change secrets in the event of a leak or as part of regular key rotation.

Each time your server receives an incoming webhook from Ultravox here's how you can ensure the webhook was sent by Ultravox and hasn't been tampered with:

<Steps>
  <Step title="Timestamp Verification">
    * Each incoming webhook request includes a `X-Ultravox-Webhook-Timestamp` header with the time the webhook was sent.
    * Verify that this timestamp is recent (e.g. within the last minute) to prevent replay attacks.
  </Step>

  <Step title="Signature Verification">
    * Ultravox signs each webhook using HMAC-SHA256.
    * The signature is included in the `X-Ultravox-Webhook-Signature` header.
    * To verify the signature:
      * Concatenate the raw request body with the timestamp.
      * Create an HMAC-SHA256 hash of this concatenated string using your webhook secret as the key.
      * Compare this hash with the provided signature.

    ```python Verifying Webhook Signature theme={null}
    import datetime
    import hmac

    request_timestamp = request.headers["X-Ultravox-Webhook-Timestamp"]
    if datetime.datetime.now() - datetime.datetime.fromisoformat(request_timestamp) > datetime.timedelta(minutes=1):
      raise RuntimeError("Expired message")
    expected_signature = hmac.new(WEBHOOK_SECRET.encode(), request.content + request_timestamp.encode(), "sha256").hexdigest()
    for signature in request.headers["X-Ultravox-Webhook-Signature"].split(","):
      if hmac.compare_digest(signature, expected_signature):
        break  # Valid signature
    else:
      raise RuntimeError("Message or timestamp was tampered with")
    ```
  </Step>

  <Step title="Multiple Signatures">
    * `The X-Ultravox-Webhook-Signature` header may contain multiple signatures separated by commas.
    * This allows for key rotation without downtime.
    * Your code should check if any of the provided signatures match your computed signature.
  </Step>
</Steps>

### Testing

During development, you can test your webhook security implementation by:

1. Creating a test webhook with a known secret
2. Manually crafting webhook requests with correct signatures
3. Verifying that invalid signatures are properly rejected
4. Testing with expired timestamps

By implementing these checks, you ensure that only authentic, recent, and unmodified webhooks from Ultravox are processed by your system.
Remember to store your webhook secret securely and never expose it in client-side code or public repositories.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt