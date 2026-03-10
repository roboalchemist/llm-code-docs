# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/webhook-signature-generation.mdx

***

## stoplight-id: m9rvg4zgqpzgq

# Webhook Signature Generation

A webhook signature is a cryptographic hash used to verify the authenticity and integrity of webhook requests. It ensures that the request comes from a trusted source and has not been tampered with.

Cash App Afterpay uses webhooks to [notify merchants and partners about disputes](/cash-app-afterpay/guides/api-development/disputes/integrate-with-the-disputes-api).

Webhooks need a signature for security and verification purposes. Webhook signatures help:

* Prevent spoofing – They ensure only trusted sources can send webhooks
* Detect tampering – If the payload is altered, the signature will not match
* Add security – The signature works as an additional layer of protection alongside HTTPS.

## Pre-work

Before you can receive and act on webhooks, you need to do the following:

1. Set up a webhook endpoint and an associated URL. The endpoint must allow POST requests with content-type = application/json.
2. Contact Afterpay merchant support and give them the following information:
   * The URL you set up for webhook notification in step 1
   * Your unique partner ID

After we receive this information, we share an HMAC (Hash Message Authentication Code) value with you and enable our systems for notification.

<Note>
  Don't confuse the HMAC shared secret key with the HMAC value that is generated using the HMAC shared secret key.
</Note>

## Verify the webhook event payload

To verify a webhook event payload with the HMAC value, follow these steps:

1. **Retrieve the webhook event signature:**
   * Retrieve the event signature from the `X-Afterpay-Request-Signature` header provided in the webhook.
2. **Construct raw signature in canonical form:**
   * `url`: The destination URL for the webhook
   * `time`: The `X-Afterpay-Request-Date` header value, represented as a UNIX timestamp
   * `payload`: The raw JSON body of the webhook
   * Concatenate raw signature with format: `${url}\n${time}\n${payload}`
3. **Generate HMAC-SHA-256 value:**
   * Create HMAC value using the raw signature and the API secret corresponding to API key utilities to create the webhook
   * Use a constant-time cryptographic library to generate the signature to prevent timing attacks
4. **Compare the generated signature with the received signature:**
   * Compare the computed signature against the `X-Afterpay-Request-Signature` header value
   * If both signatures match, then the request is verified as legitimate
   * If they don't match, reject the request

### Code sample:

```js
const express = require('express');
const crypto = require('crypto');
const app = express();

app.use(express.json({ verify: (req, res, buf) => { req.rawBody = buf; } }));

// Secret provided by Afterpay team.
const SECRET = "WEBHOOK_URL_SECRET" 

function verifyWebhookSignature(req) {

// Step 1: Retrieve the webhook event signature
 const receivedSignature = req.headers['x-afterpay-request-signature'];

 // Step 2: Construct the message
 const url = req.headers['host'];
 const time = req.headers['x-afterpay-request-date'];
 const payload = req.rawBody;
 const message = `${url}\n${time}\n${payload}`

 // Step 3: Create HMAC SHA-256 value.
 const expectedSignature = crypto.createHmac('sha256', SECRET)
 .update(message)
 .digest('base64');

 // Step 4: Assert recieved signature with expected signature.
 const receivedBuffer = Buffer.from(receivedSignature, 'hex');
 const expectedBuffer = Buffer.from(expectedSignature, 'hex');
 return crypto.timingSafeEqual(receivedBuffer, expectedBuffer);
}

app.post('/afterpay', (req, res) => {
 console.log("Message received:", req.body);
 if (!verifyWebhookSignature(req)) {
     return res.status(403).send("Invalid signature");
 }

 console.log("✅ Webhook verified:", req.body);
 res.status(200).send("Webhook received");
});

app.listen(80, () => {
 console.log('Webhook server listening on port 80');
});
```

## Manual signature verification

You can verify the webhook signature manually using the command line. This can be helpful for debugging or verifying payloads without using a backend server.

```bash
PAYLOAD='{"webhook_event_id": "b4df2187-4090-4845-be15-a73546107cbe", "webhook_event_type": "created", "dispute_id": "dp_KvGaECApCMdsH8earUSa2V", "merchant_reference": "08CF65ZSFNHVM"}'
URL="${notification_uri}" # replace with your webhook endpoint URL
SECRET=<your_hmac_secret_key> # replace with the HMAC secret key shared by Afterpay
TIME=1741100821 # UNIX timestamp from X-Afterpay-Request-Date header

MESSAGE="$URL\n$TIME\n$PAYLOAD"
HMAC=$(printf "${MESSAGE}" | openssl dgst -hmac "${SECRET}" -sha256 -binary | base64)
```

The resulting `HMAC` value is the signature you should compare against the value in the `X-Afterpay-Request-Signature` header.

**Sample request:**

```http
POST ${notification_uri} HTTP/1.1
Host: ${notification_base_url}
X-Afterpay-Request-Date: 1664239810
X-Afterpay-Request-Signature: ${HMAC}
Content-Type: application/json

{
  "webhook_event_id": "b4df2187-4090-4845-be15-a73546107cbe",
  "webhook_event_type": "created",
  "dispute_id": "dp_KvGaECApCMdsH8earUSa2V",
  "merchant_reference": "08CF65ZSFNHVM"
}
```
