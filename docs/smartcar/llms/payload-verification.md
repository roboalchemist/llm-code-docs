# Source: https://smartcar.com/docs/integrations/webhooks/payload-verification.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Payload Verification

> Verify webhook payloads are authentic using signature verification

<Info>
  **This page covers verifying ongoing webhook payloads.** For initial endpoint verification when creating a webhook, see [Callback URI Verification](/integrations/webhooks/callback-verification).
</Info>

Always verify that webhook payloads actually came from Smartcar before processing them. Every webhook includes an `SC-Signature` header containing an HMAC-SHA256 signature of the payload.

## Why Verification Matters

Without signature verification:

* Anyone could send fake webhook payloads to your endpoint
* Malicious actors could inject false vehicle data
* You have no guarantee the payload came from Smartcar

Signature verification ensures:

* The payload was sent by Smartcar
* The payload wasn't tampered with in transit
* You can safely process the data

***

## How Signature Verification Works

1. Smartcar creates an HMAC-SHA256 hash of the raw request body using your **Application Management Token** as the secret key
2. The hash is sent in the `SC-Signature` header
3. You recreate the hash using the same secret and compare it to the received signature
4. If they match, the payload is authentic and unmodified

***

## Quick Implementation

Use our SDKs for automatic signature verification:

<Tip>
  Our [backend SDKs](/api-reference/api-sdks) have helper methods that return `true` if the payload is valid.
</Tip>

<CodeGroup>
  ```js Node.js theme={null}
  smartcar.verifyPayload(
      application_management_token,
      sc_signature_header, 
      raw_webhook_body
  );
  ```

  ```python Python theme={null}
  Smartcar.verify_payload(
      application_management_token,
      sc_signature_header, 
      raw_webhook_body
  )
  ```

  ```java Java theme={null}
  Smartcar.verifyPayload(
      application_management_token,
      sc_signature_header, 
      raw_webhook_body
  );
  ```

  ```ruby Ruby theme={null}
  Smartcar.verify_payload(
      application_management_token,
      sc_signature_header, 
      raw_webhook_body
  )
  ```
</CodeGroup>

***

## Manual Implementation

If you're not using an SDK, implement signature verification manually:

<CodeGroup>
  ```javascript Node.js theme={null}
  const crypto = require('crypto');

  function verifyWebhookSignature(payload, signature, managementToken) {
    // Create HMAC hash of the raw body
    const hmac = crypto
      .createHmac('sha256', managementToken)
      .update(payload)
      .digest('hex');
    
    // Securely compare (prevents timing attacks)
    return crypto.timingSafeEqual(
      Buffer.from(hmac),
      Buffer.from(signature)
    );
  }

  // Important: Use raw body parser
  app.post('/webhooks/smartcar', 
    express.raw({ type: 'application/json' }), 
    (req, res) => {
      // Get the signature from headers
      const signature = req.headers['sc-signature'];
      
      // Get the raw body
      const rawBody = req.body.toString();
      
      // Verify signature
      if (!verifyWebhookSignature(rawBody, signature, MANAGEMENT_TOKEN)) {
        return res.status(401).json({ error: 'Invalid signature' });
      }
      
      // Now safe to process
      const payload = JSON.parse(rawBody);
      processWebhook(payload);
      res.status(200).json({ status: 'received' });
    }
  );
  ```

  ```python Python theme={null}
  import hmac
  import hashlib

  def verify_webhook_signature(payload, signature, management_token):
      """Verify the SC-Signature header matches the payload"""
      # Create HMAC hash of the raw body
      expected = hmac.new(
          management_token.encode(),
          payload.encode(),
          hashlib.sha256
      ).hexdigest()
      
      # Securely compare (prevents timing attacks)
      return hmac.compare_digest(expected, signature)

  @app.post('/webhooks/smartcar')
  def webhook_handler():
      # Get the signature from headers
      signature = request.headers.get('SC-Signature')
      
      # Get the raw body (BEFORE parsing as JSON)
      raw_body = request.data.decode('utf-8')
      
      # Verify signature
      if not verify_webhook_signature(raw_body, signature, MANAGEMENT_TOKEN):
          return {"error": "Invalid signature"}, 401
      
      # Now safe to process
      payload = request.get_json()
      process_webhook(payload)
      return {"status": "received"}, 200
  ```

  ```java Java theme={null}
  import javax.crypto.Mac;
  import javax.crypto.spec.SecretKeySpec;
  import java.security.MessageDigest;

  public class WebhookVerification {
      
      public static boolean verifySignature(
          String payload, 
          String signature, 
          String managementToken
      ) throws Exception {
          // Create HMAC-SHA256
          Mac hmac = Mac.getInstance("HmacSHA256");
          SecretKeySpec secretKey = new SecretKeySpec(
              managementToken.getBytes(), 
              "HmacSHA256"
          );
          hmac.init(secretKey);
          
          // Generate hash
          byte[] hash = hmac.doFinal(payload.getBytes());
          String expected = bytesToHex(hash);
          
          // Securely compare
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

  @PostMapping("/webhooks/smartcar")
  public ResponseEntity<?> handleWebhook(
      @RequestBody String rawBody,
      @RequestHeader("SC-Signature") String signature
  ) {
      // Verify signature
      if (!WebhookVerification.verifySignature(rawBody, signature, MANAGEMENT_TOKEN)) {
          return ResponseEntity.status(401).body(Map.of("error", "Invalid signature"));
      }
      
      // Now safe to process
      processWebhook(rawBody);
      return ResponseEntity.ok(Map.of("status", "received"));
  }
  ```

  ```ruby Ruby theme={null}
  require 'openssl'

  def verify_webhook_signature(payload, signature, management_token)
    # Create HMAC hash of the raw body
    expected = OpenSSL::HMAC.hexdigest(
      'SHA256',
      management_token,
      payload
    )
    
    # Securely compare
    Rack::Utils.secure_compare(expected, signature)
  end

  post '/webhooks/smartcar' do
    # Get the signature from headers
    signature = request.env['HTTP_SC_SIGNATURE']
    
    # Get the raw body
    raw_body = request.body.read
    
    # Verify signature
    unless verify_webhook_signature(raw_body, signature, MANAGEMENT_TOKEN)
      halt 401, { error: 'Invalid signature' }.to_json
    end
    
    # Now safe to process
    payload = JSON.parse(raw_body)
    process_webhook(payload)
    
    status 200
    { status: 'received' }.to_json
  end
  ```
</CodeGroup>

<Warning>
  **Critical:** You must verify the signature against the **raw request body** before parsing it as JSON. Many frameworks automatically parse JSON, which can alter the body and break signature verification.
</Warning>

***

## Best Practices

<AccordionGroup>
  <Accordion title="Always verify signatures" icon="shield-check">
    Never skip signature verification, even in development. It's your only guarantee that payloads are authentic.
  </Accordion>

  <Accordion title="Use the raw body" icon="file-code">
    Verify against the raw request body before JSON parsing. Parsed JSON may have different whitespace/ordering that breaks verification.
  </Accordion>

  <Accordion title="Reject invalid signatures" icon="ban">
    Return `401 Unauthorized` for invalid signatures. Don't process the payload or return `200`.
  </Accordion>

  <Accordion title="Keep tokens secure" icon="lock">
    Store your Application Management Token securely (environment variables, secrets manager). Never commit it to source control.
  </Accordion>
</AccordionGroup>

***

## Next Steps

<CardGroup cols={2}>
  <Card title="Best Practices" icon="star" href="/integrations/webhooks/best-practices/security">
    Complete security best practices guide
  </Card>

  <Card title="Event Reference" icon="book" href="/api-reference/webhooks/events/overview">
    Understand webhook event structures
  </Card>

  <Card title="Receiving Webhooks" icon="code" href="/integrations/webhooks/receiving-webhooks">
    Build your webhook endpoint
  </Card>

  <Card title="Delivery Behavior" icon="truck-fast" href="/api-reference/webhooks/delivery-behavior">
    Learn about retries and timeouts
  </Card>
</CardGroup>
