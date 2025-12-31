# Source: https://smartcar.com/docs/integrations/webhooks/best-practices/security.md

# Security

> Protect your webhook endpoint from spoofed and malicious requests

Always verify that webhook payloads actually came from Smartcar before processing them.

## Verify Payload Signatures

Every webhook payload includes an `SC-Signature` header containing an HMAC-SHA256 signature. **Always verify this signature** before processing the payload.

### How It Works

1. Smartcar creates an HMAC-SHA256 hash of the payload using your Application Management Token as the secret key
2. The hash is sent in the `SC-Signature` header
3. You recreate the hash using the same secret and compare it to the received signature
4. If they match, the payload is authentic

### Implementation

<CodeGroup>
  ```javascript Node.js theme={null}
  const crypto = require('crypto');

  function verifySignature(payload, signature, managementToken) {
    // Create HMAC hash
    const hmac = crypto
      .createHmac('sha256', managementToken)
      .update(payload)
      .digest('hex');
    
    // Use timingSafeEqual to prevent timing attacks
    return crypto.timingSafeEqual(
      Buffer.from(hmac),
      Buffer.from(signature)
    );
  }

  app.post('/webhooks/smartcar', express.raw({ type: 'application/json' }), (req, res) => {
    // Get signature from header
    const signature = req.headers['sc-signature'];
    
    // Get raw body
    const rawBody = req.body.toString();
    
    // Verify before processing
    if (!verifySignature(rawBody, signature, MANAGEMENT_TOKEN)) {
      return res.status(401).json({ error: 'Invalid signature' });
    }
    
    // Safe to process
    const payload = JSON.parse(rawBody);
    processWebhook(payload);
    res.status(200).json({ status: 'received' });
  });
  ```

  ```python Python theme={null}
  import hmac
  import hashlib

  def verify_signature(payload, signature, management_token):
      """Verify webhook payload authenticity"""
      expected = hmac.new(
          management_token.encode(),
          payload.encode(),
          hashlib.sha256
      ).hexdigest()
      
      # Use compare_digest to prevent timing attacks
      return hmac.compare_digest(expected, signature)

  @app.post("/webhooks/smartcar")
  def webhook_handler():
      # Get signature from header
      signature = request.headers.get('SC-Signature')
      
      # Get raw body (before JSON parsing)
      raw_body = request.data.decode('utf-8')
      
      # Verify before processing
      if not verify_signature(raw_body, signature, MANAGEMENT_TOKEN):
          return {"error": "Invalid signature"}, 401
      
      # Safe to process
      payload = request.get_json()
      process_webhook(payload)
      return {"status": "received"}, 200
  ```

  ```java Java theme={null}
  import javax.crypto.Mac;
  import javax.crypto.spec.SecretKeySpec;
  import java.security.MessageDigest;

  public class WebhookSecurity {
      
      public static boolean verifySignature(
          String payload, 
          String signature, 
          String managementToken
      ) throws Exception {
          // Create HMAC
          Mac hmac = Mac.getInstance("HmacSHA256");
          SecretKeySpec secretKey = new SecretKeySpec(
              managementToken.getBytes(), 
              "HmacSHA256"
          );
          hmac.init(secretKey);
          
          // Generate hash
          byte[] hash = hmac.doFinal(payload.getBytes());
          String expected = bytesToHex(hash);
          
          // Compare securely
          return MessageDigest.isEqual(
              expected.getBytes(),
              signature.getBytes()
          );
      }
      
      private static String bytesToHex(byte[] bytes) {
          StringBuilder result = new StringBuilder();
          for (byte b : bytes) {
              result.append(String.format("%02x", b));
          }
          return result.toString();
      }
  }
  ```
</CodeGroup>

<Warning>
  **Critical:** You must verify the signature against the raw request body, **before** parsing it as JSON. Many frameworks automatically parse JSON, which can alter the body and break signature verification.
</Warning>

***

## Why Signature Verification Matters

<AccordionGroup>
  <Accordion title="Prevents Spoofed Requests" icon="user-secret">
    Without verification, anyone could send fake webhook payloads to your endpoint. Signature verification proves the payload came from Smartcar.
  </Accordion>

  <Accordion title="Protects Against Replay Attacks" icon="rotate">
    While signatures don't prevent replays alone, combining them with `eventId` deduplication creates a complete defense.
  </Accordion>

  <Accordion title="Ensures Data Integrity" icon="shield-halved">
    If the payload is tampered with in transit, the signature won't match, alerting you to the modification.
  </Accordion>

  <Accordion title="Compliance Requirements" icon="building-columns">
    Many security standards and regulations require verification of external data sources.
  </Accordion>
</AccordionGroup>

***

## Additional Security Measures

### Use HTTPS Only

Smartcar only delivers webhooks to HTTPS endpoints with valid SSL certificates.

<Check>
  **Required:** Your callback URL must use HTTPS with a valid, trusted SSL certificate. Self-signed certificates are not supported.
</Check>

### Restrict Access by IP (Optional)

While Smartcar doesn't publish a fixed IP range (addresses may change), you can add an extra layer of security by:

1. Logging all webhook source IPs
2. Alerting on unusual source addresses
3. Rate limiting by IP to prevent abuse

<Note>
  **Don't rely on IP filtering alone.** Signature verification is the primary security mechanism. IP-based restrictions should be supplementary.
</Note>

### Rotate Management Tokens Periodically

Your Application Management Token is used to verify webhook signatures. Rotate it periodically for security:

<Steps>
  <Step title="Generate new token">
    Create a new Application Management Token in the Dashboard
  </Step>

  <Step title="Update your code">
    Deploy code that accepts either the old or new token temporarily
  </Step>

  <Step title="Switch to new token">
    Once deployed, switch Dashboard to use the new token
  </Step>

  <Step title="Remove old token">
    After confirming all webhooks use the new token, remove old token support
  </Step>
</Steps>

### Monitor Failed Verifications

Track and alert on signature verification failures:

```python  theme={null}
@app.post("/webhooks/smartcar")
def webhook_handler():
    signature = request.headers.get('SC-Signature')
    raw_body = request.data.decode('utf-8')
    
    if not verify_signature(raw_body, signature, MANAGEMENT_TOKEN):
        # Log the failure
        logger.warning(
            "Invalid webhook signature",
            extra={
                "source_ip": request.remote_addr,
                "signature": signature,
                "payload_size": len(raw_body)
            }
        )
        
        # Alert if threshold exceeded
        if recent_failures_count() > 10:
            send_security_alert("High rate of invalid webhook signatures")
        
        return {"error": "Invalid signature"}, 401
```

***

## Using SDK Helpers

Smartcar's SDKs provide built-in methods for signature verification:

<CodeGroup>
  ```javascript Node.js SDK theme={null}
  const smartcar = require('smartcar');

  // Verify signature
  const isValid = smartcar.verifyPayload(
    managementToken,
    signature,
    rawBody
  );
  ```

  ```python Python SDK theme={null}
  import smartcar

  # Verify signature
  is_valid = smartcar.verify_payload(
      management_token,
      signature,
      raw_body
  )
  ```

  ```java Java SDK theme={null}
  import com.smartcar.sdk.Smartcar;

  // Verify signature
  boolean isValid = Smartcar.verifyPayload(
      managementToken,
      signature,
      rawBody
  );
  ```
</CodeGroup>

***

## Next Steps

<CardGroup cols={2}>
  <Card title="Payload Verification Guide" icon="book" href="/integrations/webhooks/payload-verification">
    Complete implementation details
  </Card>

  <Card title="Reliability" icon="shield" href="/integrations/webhooks/best-practices/reliability">
    Implement idempotency
  </Card>

  <Card title="Monitoring" icon="chart-line" href="/integrations/webhooks/best-practices/monitoring">
    Track verification failures
  </Card>

  <Card title="Architecture" icon="diagram-project" href="/integrations/webhooks/best-practices/architecture">
    Design secure webhook handlers
  </Card>
</CardGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://smartcar.com/docs/llms.txt