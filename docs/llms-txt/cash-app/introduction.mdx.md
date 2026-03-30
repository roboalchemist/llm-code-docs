# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/introduction.mdx

***

## stoplight-id: 2ddgxbn9ty2xw

# Cash App Afterpay API introduction

The Cash App Afterpay API is organized around [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer). The API uses predictable, resource-oriented URLs and uses HTTP status codes to indicate errors.

* All communication must use TLS 1.2 or higher.
* The API supports [idempotency](https://en.wikipedia.org/wiki/Idempotence), which guarantees that if a request is retried, the operation is performed only once. This is especially important for partial refunds.
  <Note>
    Afterpay recommends using UUIDs as `requestId` values. For most endpoints, requests with the same `requestId` will return the same response for up to 24 hours. Refund requests are an exception — they support idempotency for longer than 24 hours.
    If an idempotent request returns an HTTP 409, it means the original request is still being processed. Retry the request with the same requestId until a different response is returned.
  </Note>
* API call response times can vary, especially when requests rely on downstream banking networks. All idempotent resources can be safely retried if a timeout occurs.
* All dates are represented in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, and are stored and returned in UTC. You can provide dates in UTC (e.g. `2025-01-01T13:25:00Z`) or with a time zone offset (e.g. `2025-01-01T23:25:00+10:00` for AEST).

***

## Environments

* **Production**: `https://global-api.afterpay.com`
* **Sandbox:** `https://global-api-sandbox.afterpay.com`

<Note>
  Existing merchant using region-specific endpoints (e.g. `https://api.us.afterpay.com`), can continue using them for their current region.
</Note>

***

## Pagination

The List Payment endpoint supports pagination using the `includeNextLink` query parameter.

### Request parameters

| Name              | Type    | Description                                                                                                     |
| ----------------- | ------- | --------------------------------------------------------------------------------------------------------------- |
| `includeNextLink` | boolean | Return a modified pagination object which includes a url to return the next page. The default value is `false`. |

### Response

| Field          | Type    | Description                                                                                                                |
| -------------- | ------- | -------------------------------------------------------------------------------------------------------------------------- |
| `limit`        | integer | The number of results that this page was limited to.                                                                       |
| `totalResults` | integer | The total number of results matching the query. If greater than `limit`, one or more results were excluded from this page. |
| `nextPageUrl`  | string  | A URL to return the next page (empty if there are no more results).                                                        |
| `results`      | array   | A page of matching results (may be a subset of the total).                                                                 |

### Example request

```cURL
curl https://global-api-sandbox.afterpay.com/v2/payments?includeNextLink=true \
  -H 'Authorization: Basic <Base64EncodedCredentials>' \
  -H 'User-Agent: <MyUserAgent>' \
  -H 'Accept: application/json'
```

### Example response

```json
{
  "totalResults": 210,
  "limit": 20,
  "nextPageUrl":     "https://global-api-sandbox.afterpay.com/v2/payments?cursor=MjAyMTExMDlUMDUzNTI1LjI1Nlo%3D%3AMDAxLjVuNDhzbm1qNTh0ZzFkZmcwMzR2cGV2ZG1zY2ZiaTllZmVqMzRkMjl1c25mbDVnbg%3D%3D&includeNextLink=true", 
  "results": [
    ...
  ]
}
```
