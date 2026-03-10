# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/signing-requests.mdx

***

## stoplight-id: 72bbb6a77c769

# Signing Requests

> To sign `multipart/form-data` requests, see the section [Signing Multipart Requests.](#signing-multipart-requests)

All requests to the Network and Management APIs must be *signed* and have a valid signature passed in the `X-Signature` header. To generate the signature:

1. Construct the following string: `{method}\n{path}\n{headers}\n{bodyDigest}`, where:

   * `{method}` is the HTTP method, in uppercase.

   * `{path}` is the remainder of the URL following the host, including the query string (if present).

   * `{headers}` is the concatenation of the following headers (if present) in the form `{lowercase(name)}:{strip(value)}\n`:

     * `Accept`
     * `Authorization`
     * `Content-Type`
     * `Host`

   * `{bodyDigest}` is the lowercased, hexadecimal representation of the SHA256 digest of the bytes of the request body (hashing an empty string if there is no body).

2. Create an HMAC-SHA256 cryptographic hash where the text to hash is the string you created in step 1, and the secret is the secret value associated with the API key being used to make the request.

3. Set the `X-Signature` header to `V1 {signature}` where:

   * `{signature}` is the signature obtained in step 2 in hexadecimal, lowercased.

   > Instead of computing a real signature in Sandbox, you can use a [magic header value](/cash-app-pay-partner-api/guides/technical-guides/sandbox/developer-sandbox): `X-Signature: sandbox:skip-signature-check`

4. Set an `Authorization` header of `Client {CLIENT_ID} {KEY_ID}` where:

   * `{CLIENT_ID}` is the client ID value obtained from Cash App
   * `{KEY_ID}` is the Cash App identifier for the API key used to generate the signature in step 2

```javascript
// Example request
// curl --request GET \
//      --url 'https://sandbox.api.cash.app/network/v1/payments?limit=50' \
//      --header 'accept:application/json' \
//      --header 'Authorization:Client {CLIENT_ID} {CLIENT_KEY}' \
//      --header 'content-type:application/json' \
//      --header 'host:sandbox.api.cash.app' \
//      --header 'X-Region: PDX' \
//      --header 'X-Signature: {X-Signature}'

//Loading the crypto module in node.js
let crypto = require('crypto');

// API Credentials
let client_id = '';
let api_key = '';
let api_secret = '';
let path = '/network/v1/payments?limit=50';
let host = 'sandbox.api.cash.app';

// STEP 1: construct the following string: {method}\n{path}\n{headers}\n{bodyDigest}
let method = 'GET';
let headers = 'accept:application/json' + '\nauthorization:Client ' + client_id + ' ' + api_key + '\ncontent-type:application/json' + '\nhost:' + host;
let body_digest = crypto.createHash('sha256').update('').digest('hex');
let raw_signature = method + '\n' + path + '\n' + headers + '\n' + body_digest

// STEP 2: create an HMAC-SHA256 crypto hash with API secret.
let hashed_signature = crypto.createHmac('sha256', api_secret).update(raw_signature).digest('hex');

// STEP 3: X-Signature header should be set to the following schema "V1 {signature}
let final_signature = 'V1 ' + hashed_signature;

//Printing the output on the console
console.log("X-Signature: " + final_signature);
```

> **Webhook signatures:** Webhook deliveries also contain an `X-Signature` header that is computed using the same process. This allows webhooks delivered by Cash App to be validated by computing the signature from the request payload and verifying that it matches the `X-Signature` header

# Signing Multipart Requests

To sign requests using the `multipart/form-data` content type, use this modified signing algorithm:

1. Construct the following string: `{method}\n{path}\n{headers}\n{bodyDigest}`, where:
   * `{method}` is the HTTP method, in uppercase.

   * `{path}` is the remainder of the URL following the host, including the query string (if present).

   * `{headers}` is the concatenation of the following headers (if present) in the form `{lowercase(name)}:{strip(value)}\n`:

     * `Accept`
     * `Authorization`
     * `Content-Type` (this should be `multipart/form-data` with no other parameters)
     * `Host`

   * `{bodyDigest}` is the lowercased, hexadecimal representation of the SHA256 digest of the bytes of the `request` object specified in the request body.

2. Create an HMAC-SHA256 cryptographic hash where the text to hash is the string you created in step 1, and the secret is the secret value associated with the API key being used to make the request.

3. Append a `text/plain` object named `signature` to the request body, containing the value `V1 {signature}` where `{signature}` is the value obtained in step 2 in hexademical and lowercased.

   > This signature will take precedence over any `X-Signature` header present in the request.

   > Instead of computing a real signature in Sandbox, you can use a [magic value](/cash-app-pay-partner-api/guides/technical-guides/sandbox/developer-sandbox#magic-values): `sandbox:skip-signature-check`
