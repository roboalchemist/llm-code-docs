# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/making-requests.mdx

***

## stoplight-id: 939448543783a

# Making Requests

The Cash App Pay API follows standard, RESTful JSON API conventions. All communication must be over `HTTPS` using TLS 1.2 or above.

We don't provide any server-side SDKs, so you'll need to write your own code to communicate with the API.

## Sample request

The following cURL request demonstrates how to form a valid request to the Cash App Pay API, including all required headers:

```json http
{
  "method": "post",
  "url": "https://sandbox.api.cash.app/network/v1/brands",
  "headers": {
    "Accept": "application/json",
    "Authorization": "Client TEST_CLIENT_ID TEST_API_KEY_ID",
    "Content-Type": "application/json",
    "X-Region": "SEA",
    "X-Signature": "sandbox:skip-signature-check"
  },
  "body": {
    "brand": {
        "name": "My Brand"
    },
    "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19"
  }
}
```

## Required headers

All requests to the Cash App Pay API require these headers:

* `Authorization`: This [standard header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) is used to authenticate your API client with the Cash App Pay API
* `Accept`: This [standard header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) ensures that the API client and Cash App Pay API are communicating using the same MIME type in the response payload

**For requests with payloads:**

* `Content-Type`: This [standard header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) ensures that the API client and Cash App Pay API are communicating using the same MIME type in the request payload

**For the Network API only:**

* `X-Region`: This custom header helps the Cash App Pay API optimize latencies and data storage by routing requests closest to where you and your customers are

<Note>
   All other headers are ignored by the Cash App Pay API. We don't use the 

  `Accept`

   header because the only response content type is 

  `application/json`

  . 
</Note>

### Accept

All endpoints provided by the Cash App Pay API return `application/json` content. All requests sent to the API should specify this type in the `Accept` header.

**Example**

```
Accept: application/json
```

### Authorization

All endpoints require an `Authorization` header. However, what is sent in the header varies based on the API being called:

* The **Network API** and **Management API** require a client ID and API key, formatted as `Client <Client ID> <API Key ID>`.
  * The client ID is considered public information. The API key is secret and must be well-secured. API keys will automatically expire 30 days after they are created.
* The **Customer Request API** requires a client ID, formatted as `Client <Client ID>`.
  * Since the Customer Request API can be called from customers' browsers or point of sale devices, it only requires the client ID.

<Error>Never share API keys with browsers or point of sale devices.</Error>
**Example- Network API**

```
Authorization: Client <Client ID> <API Key ID>
```

**Example- Customer Request API**

```
Authorization: Client <Client ID>
```

### Content-Type

There are two content types supported by the Cash App Pay API:

* `application/json`: This is used by the vast majority of endpoints. It specifies that the request contains a JSON payload (if a payload is provided). API clients should default to setting this content type on each request.
* `multipart/form-data`: File upload endpoints use this content type to break the request into 2 parts: a JSON payload with file metadata and a binary payload which contains the actual file. This is currently only used by the [create dispute evidence file](/cash-app-pay-partner-api/api-reference/network-api/create-dispute-evidence-file) endpoint.

**Example- Standard endpoints**

```
Content-Type: application/json
```

**Example- File upload endpoints**

```
Content-Type: multipart/form-data
```

### X-Region

To improve latencies for API clients and customers, Cash App Pay can run in multiple regions simultaneously. The `X-Region` header tells the Cash App Pay API which region the API client/consumers are closest to. It's required on all calls to the Network and Management APIs.

<Note Title="Note">
   Idempotency is scoped to a single region. If you make a request with the same idempotency key to two separate regions, you may create duplicate data. 
</Note>

**Example**

```text
X-Region: PDX
```

### X-Signature

To prevent payload tampering and keep plaintext secrets out of API requests, all requests to the Cash App API must be signed, with the signature passed in the `X-Signature` header.

When Cash App receives the request, a signature is calculated for the request and verified against the signature the API client provided. If they match, the request will complete successfully. If not, it fails.

`X-Signature` is required on all calls to the Network API and Management API.

<Note>
   When making requests in the sandbox, the magic signature value of 

  `sandbox:skip-signature-check`

   is always accepted in place of a valid signature. 
</Note>

Learn how to [sign requests](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/signing-requests) to start making API requests.
