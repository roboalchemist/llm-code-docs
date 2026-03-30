# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/webhooks/webhook-signature-generation.mdx

***

## stoplight-id: dcbkd61go680e

# Webhook Signature Generation

A webhook signature is a cryptographic hash used to verify the authenticity and integrity of webhook requests. It ensures that the request comes from a trusted source and has not been tampered with.

Cash App Pay uses webhooks for the following events:

| Event Type                      | Trigger                                                                                                                                                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| customer.created                | When a Cash App user approves a client's Cash App Pay request for the first time.                                                                                                                                           |
| customer.deleted                | When a customer account is deleted by Cash App.                                                                                                                                                                             |
| customer.updated                | When a customer updates their Cashtag.                                                                                                                                                                                      |
| customer\_request.state.updated | When a customer request's state is updated. This is typically caused by a customer approving or declining the request.                                                                                                      |
| dispute.created                 | When a dispute is created. This happens when a customer files a dispute for a payment collected by a merchant.                                                                                                              |
| dispute.state.updated           | When a disputed status changes due to action taken by Block or the partner.                                                                                                                                                 |
| grant.created                   | When a grant is created. This happens when a customer request is approved.                                                                                                                                                  |
| grant.status.updated            | When a grant's status is updated. The status change can occur under these conditions:<br />• An API client-initiated action to create a payment or revoke a grant<br />• A customer revoking an extended-use grant          |
| merchant.status.updated         | When a merchant's status is updated.                                                                                                                                                                                        |
| payment.status.updated          | When a payment status is updated. The status change can occur under these conditions:<br />• An API client-initiated action to void or capture the payment<br />• A payment auto-voiding after 7 days of not being captured |
| refund.status.updated           | When a refund status is updated. The status change can occur under these conditions:<br />• An API client-initiated action to void or capture the refund<br />• A refund auto-voiding after 7 days of not being captured    |

For all events, the webhook needs a signature for security and verification purposes. Webhook signatures help:

* Prevent spoofing – They ensure only trusted sources can send webhooks
* Detect tampering – If the payload is altered, the signature will not match
* Add security – The signature works as an additional layer of protection alongside HTTPS.

## Pre-work

Before you can receive and act on webhooks, you need to do the following:

1. Set up a webhook endpoint and an associated URL. The endpoint must allow POST requests with content-type = application/json.
2. Create a Webhook endpoint using the [Create Webhook API](/cash-app-pay-partner-api/api-reference/management-api/create-webhook-endpoint):
   ```
   curl --location 'https://sandbox.api.cash.app/management/v1/webhook-endpoints' \
   --header 'Accept: application/json' \
   --header 'Authorization: Client CASH_APP_CLIENT_ID API_KEY' \
   --header 'X-Region: PDX' \
   --header 'X-Signature: sandbox:skip-signature-check' \
   --header 'Content-Type: application/json' \
   --data '{
    "webhook_endpoint": {
         "event_configurations": [
       {
         "event_type": "grant.created",
         "api_version": "v1"
       },
       {
         "event_type": "grant.status.updated",
         "api_version": "v1"
       }
     ],
         "delivery_timeout": 10000,
         "api_key_id": "KEY_*",
         "url": "<webhook_url>",
         "reference_id": "reference_id"
    },
    "idempotency_key": "idempotency_key"
   }'
   ```
3. Ask your Cash App Pay Partner Engineering contact to allowlist the webhook URL.
4. Verify that your webhook is approved by querying the [Webhook Events API](/cash-app-pay-partner-api/api-reference/management-api/list-webhook-events):
   ```
   curl --location 'https://sandbox.api.cash.app/management/v1/webhook-endpoints' \
   --header 'Authorization: Client CASH_APP_CLIENT_ID API_KEY' \
   --header 'Accept: application/json' \
   --header 'X-Region: PDX' \
   --header 'X-Signature: sandbox:skip-signature-check'
   ```

## Verify the webhook event payload

To verify a webhook event payload with the HMAC value, follow these steps:

1. **Retrieve the webhook event signature:**
   * Retrieve the event signature from the `x-Signature` header provided in the webhook.
2. **Construct raw signature in canonical form:**
   * Get event method (e.g. POST)
   * Get the event handler path
   * Get the host
   * Construct headers with format: `{lowercase(name)}:{strip(value)}\n`
   * Hash event body
   * Concatenate raw signature with format:`${method}\n${path}\n${headers}\n${bodyDigest}`
3. **Generate HMAC-SHA-256 value:**
   * Create HMAC value using the raw signature and the API secret corresponding to API key utilities to create the webhook
   * Use a constant-time cryptographic library to generate the signature to prevent timing attacks
4. **Compare the generated signature with the received signature:**
   * Compare the computed signature against the `x-signature` header value
   * If both signatures match, then the request is verified as legitimate
   * If they don't match, reject the request

<Note Title="Note">
   The API secret is only available when a Webhook is created through  Cash App Pay APIs. If you lose the API secret, then update the Webhook with a new API key. 
</Note>

### Code sample:

```js
const express = require('express');
const crypto = require('crypto');
const app = express();

app.use(express.json({ verify: (req, res, buf) => { req.rawBody = buf; } }));

// Your API credentials
const CLIENT_ID = 'CAS-CI_*';
const API_KEY = 'KEY_*'; // API key used to create the webhook.
const API_SECRET = 'CASH_*'; // API secret generated when webhook was created.

function verifyWebhookSignature(req) {

 // Step 1: Retrieve signature from Webhook x-signature header.
 const signatureHeader = req.headers['x-signature'];
 if (!signatureHeader) return false;

 // Extract received signature (removing "V1 " prefix)
 const [version, receivedSignature] = signatureHeader.split(' ');
 if (version !== 'V1' || !receivedSignature) return false;

 // Step 2: Construct the raw signature in canonical form.
 const method = 'POST';
 const path = '/';
 const host = req.headers['host'];
 const headers = 'accept:*/*' + '\nauthorization:Client ' + CLIENT_ID + ' ' + API_KEY + '\ncontent-type:application/json; charset=utf-8' + '\nhost:' + host;
 const bodyDigest = crypto
  .createHash('sha256')
  .update(req.rawBody, 'utf8')
  .digest('hex');
 const rawSignature = `${method}\n${path}\n${headers}\n${bodyDigest}`;

 // Step 3: Create HMAC SHA-256 value.
 const expectedSignature = crypto
  .createHmac('sha256', API_SECRET)
  .update(rawSignature)
  .digest('hex');

 // Step 4: Assert recieved signature with expected signature.
 const receivedBuffer = Buffer.from(receivedSignature, 'hex');
 const expectedBuffer = Buffer.from(expectedSignature, 'hex');
 return crypto.timingSafeEqual(receivedBuffer, expectedBuffer);
}

// Webhook endpoint
app.post('*', (req, res) => {
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
