# Source: https://docs.salad.com/container-engine/how-to-guides/job-processing/webhook-signature.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Validating Webhook Signatures

> Learn how to validate webhook signatures for the Job Queue API in SaladCloud.

*Last Updated: June 2, 2025*

# Validating Webhook Signatures

When using the Salad Job Queue API, you can set up webhooks to receive the output of your jobs. To ensure the integrity
and authenticity of the webhook payloads, you can validate the signatures included in the webhook requests.

A webhook request will include headers `webhook-signature`, `webhook-id` and `webhook-timestamp`, which contains a
signature of the payload. This signature can be validated using your webhook secret key, available in the portal, and
the `svix` library.

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/webhook-secret-key.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=542c00d0ed07bc8a45aa71f66f1b2041" alt="Webhook Signature Example" data-og-width="961" width="961" data-og-height="632" height="632" data-path="container-engine/images/webhook-secret-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/webhook-secret-key.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=79fa48f7d69e3585e6cac84852750a87 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/webhook-secret-key.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=a381f91a626cb2c656888154dcc02651 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/webhook-secret-key.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=251e2f77d32e03e12b00767a621f8958 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/webhook-secret-key.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=8b36e73988a1b7939a39c46dbf23b316 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/webhook-secret-key.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=d131721d29b78359c263104405753af4 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/webhook-secret-key.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=113bd7a9ea98e8d09deb9a4b8a2e8590 2500w" />

## Validating the Signature

### Node.js Example

First, install `svix`:

```bash  theme={null}
npm install svix
```

Then, you can use the following code to validate the signature:

```javascript  theme={null}
const { Webhook } = require('svix')

//Express.js middleware
function validateWebhookSignature(req, res, next) {
  const webhook = new Webhook(secret)
  try {
    webhook.verify(req.body, req.headers)
    next()
  } catch (error) {
    console.error('Webhook verification failed:', error)
    return res.status(401).send('Invalid signature')
  }
}
```

### Python Example

First, install `svix`:

```bash  theme={null}
pip install svix
```

Then, you can use the following code to validate the signature:

```python  theme={null}
from fastapi import FastAPI, Request, HTTPException
from svix import Webhook
from typing import Any, Dict

async def validate_webhook(request: Request) -> Dict[str, Any]:
    """
    FastAPI Dependency to validate webhook signatures
    """
    try:
        # Get the raw body
        body = await request.body()

        # Create webhook instance
        webhook = Webhook(webhook_secret)

        # Verify the webhook signature
        payload = webhook.verify(body, dict(request.headers))

        return payload
    except Exception as e:
        print(f"Webhook verification failed: {e}")
        raise HTTPException(status_code=401, detail="Invalid webhook signature")
```
