# Source: https://dub.co/docs/concepts/webhooks/verify-webhook-requests.md

# Verify webhook requests

> Learn how to verify webhook requests to ensure they're coming from Dub.

With signature verification, you can determine if the webhook came from Dub, and has not been tampered with in transit.

All webhooks are delivered with a `Dub-Signature` header. Dub generates this header using a secret key that only you and Dub know.

An example header looks like this:

```
Dub-Signature: c9ed6a2abf93f59d761eea69908d8de00f4437b5b6d7cd8b9bf5719cbe61bf46
```

## Finding your webhook's signing secret

You can find your webhook's signing secret in the **Update Details** tab:

<Frame>
  <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/webhook-signing-secret.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=5b4981b13c208e6a1154bb19bacbfc9e" alt="Webhook signing secret" data-og-width="1365" width="1365" data-og-height="637" height="637" data-path="images/webhook-signing-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/webhook-signing-secret.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=98c661b22f788931de377d14635bbbbd 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/webhook-signing-secret.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=4fb8a1c7a021f29092d905be0e7fb47f 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/webhook-signing-secret.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=be47edc7c2b1165dd48770372fb71abd 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/webhook-signing-secret.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=504d649b366a25bb2301176da1a38f4a 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/webhook-signing-secret.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=fb900830d3708b801bed6028eba3cd17 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/webhook-signing-secret.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=098916459faa6a0203bfa05d1312a0d5 2500w" />
</Frame>

Make sure to keep this secret safe by only storing it in a secure environment variable (e.g. `DUB_WEBHOOK_SECRET`). Do not commit it to git or add it in any client-side code.

## Verifying a webhook request

To verify, you can use the secret key to generate your own signature for each webhook. If both signatures match then you can be sure that a received event came from Dub.

The steps required are:

1. Get the raw body of the request.
2. Extract the signature from the `Dub-Signature` header.
3. Calculate the HMAC of the raw body using the `SHA-256` hash function and the secret.
4. Compare the calculated `HMAC` with the one sent in the `Dub-Signature` header. If they match, the webhook is verified.

Here's an example of how you can verify a webhook request in different languages:

<CodeGroup>
  ```javascript Next.js theme={null}
  export const POST = async (req: Request) => {
    const webhookSignature = req.headers.get("Dub-Signature");
    if (!webhookSignature) {
      return new Response("No signature provided.", { status: 401 });
    }

    // Copy this from the webhook details page
    const secret = process.env.DUB_WEBHOOK_SECRET;
    if (!secret) {
      return new Response("No secret provided.", { status: 401 });
    }

    // Make sure to get the raw body from the request
    const rawBody = await req.text();

    const computedSignature = crypto
      .createHmac("sha256", secret)
      .update(rawBody)
      .digest("hex");

    if (webhookSignature !== computedSignature) {
      return new Response("Invalid signature", { status: 400 });
    }

    // Handle the webhook event
    // ...
  };
  ```

  ```python Python theme={null}
  import hmac
  import hashlib

  def webhook():
      # Get the signature from the header
      webhook_signature = request.headers.get('Dub-Signature')
      if not webhook_signature:
          abort(401, 'No signature provided.')

      # Copy this from the webhook details page
      secret = os.environ.get('DUB_WEBHOOK_SECRET')
      if not secret:
          abort(401, 'No secret provided.')

      # Get the raw body of the request
      raw_body = request.data

      # Calculate the HMAC
      computed_signature = hmac.new(
          secret.encode('utf-8'),
          raw_body,
          hashlib.sha256
      ).hexdigest()

      if webhook_signature != computed_signature:
          abort(400, 'Invalid signature')

      # Handle the webhook event
      # ...

      return 'OK', 200
  ```

  ```go Go theme={null}

  import (
  	"crypto/hmac"
  	"crypto/sha256"
  	"encoding/hex"
  	"io/ioutil"
  	"net/http"
  	"os"
  )

  func webhookHandler(w http.ResponseWriter, r *http.Request) {
  	// Get the signature from the header
  	webhookSignature := r.Header.Get("Dub-Signature")
  	if webhookSignature == "" {
  		http.Error(w, "No signature provided.", http.StatusUnauthorized)
  		return
  	}

  	// Copy this from the webhook details page
  	secret := os.Getenv("DUB_WEBHOOK_SECRET")
  	if secret == "" {
  		http.Error(w, "No secret provided.", http.StatusUnauthorized)
  		return
  	}

  	// Read the raw body
  	body, err := ioutil.ReadAll(r.Body)
  	if err != nil {
  		http.Error(w, "Error reading request body", http.StatusInternalServerError)
  		return
  	}

  	// Calculate the HMAC
  	h := hmac.New(sha256.New, []byte(secret))
  	h.Write(body)
  	computedSignature := hex.EncodeToString(h.Sum(nil))

  	if webhookSignature != computedSignature {
  		http.Error(w, "Invalid signature", http.StatusBadRequest)
  		return
  	}

  	// Handle the webhook event
  	// ...

  	w.WriteHeader(http.StatusOK)
  	w.Write([]byte("OK"))
  }
  ```
</CodeGroup>

## Why is signature verification important?

Signature verification is a crucial security measure that protects against request forgery and data tampering. Without verification, malicious actors could send fake webhook events to your endpoint, potentially triggering unauthorized actions.

The HMAC-SHA256 signature verification process ensures that only Dub can generate valid webhook requests and that payloads haven't been modified in transit. This provides both authentication (confirming the sender is Dub) and integrity (ensuring the message hasn't been tampered with).
