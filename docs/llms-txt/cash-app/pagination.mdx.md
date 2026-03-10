# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/pagination.mdx

***

## stoplight-id: 9c5cede440051

# Pagination

## What is pagination

When data sets get large, it becomes inefficient to return them in a single response. To make it faster for both the server and API clients, we divide the data into small chunks. The API client asks for a chunk of data, and the server returns it along with a token called a *cursor*. The API client then sends the cursor back to the server to request the next chunk of data. This process repeats until the API client has iterated through all the data and is called *pagination*.

## How does pagination work in the API?

All "list" endpoints in Cash App Pay use pagination, and support two pagination-related fields on the request:

* **`cursor`**, which is a string used by the server to fetch the next page of data. Use the `cursor` from the response to populate this field.
* **`limit`**, which is an integer from 1 to 100 that sets the maximum number of resources that can be returned in the response.

A `cursor` is provided at the top-level of each paginated response **if there is another page of data to load**. Once no cursor is present on the response, you've iterated through all the data.

### Example: Listing all payments

In this example, we'll attempt to list all the payments taken by our API client. First, we'll build a `cURL` request to call [list payments](/cash-app-pay-partner-api/api-reference/network-api/list-payments):

```json http
{
  "method": "get",
  "url": "https://sandbox.api.cash.app/network/v1/payments",
  "headers": {
    "Accept": "application/json",
    "Authorization": "Client CLIENT_ID API_KEY_ID",
    "X-Region": "SEA",
    "X-Signature": "sandbox:skip-signature-check"
  },
  "query": {
    "limit": 1
  }
}
```

The API will respond with some JSON that looks like this:

```json
{
  "payments": [
    {
      "id": "PWC_4nn21zy6t0v2yhqg5bvhk7xkq",
      "amount": 1500,
      "refunded_amount": 100,
      "net_amount": 1400,
      "currency": "USD",
      "customer_id": "AUTH_24g7nq7m1je9b6fnzbtvwzqej",
      "merchant_id": "MERCHANT_4vxs5egfk7hmta3qx2h6rp91x",
      "grant_id": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50",
      "status": "AUTHORIZED",
      "created_at": "2022-01-01T12:00:00Z",
      "updated_at": "2022-01-05T12:00:00Z",
      "refund_ids": [
        "PWCR_da1v3j4p3z15y47adpzzq0whj"
      ],
      "reference_id": "external-id"
    }
  ],
  "cursor": "be167132a9f2b565"
}
```

Since we set the `limit` parameter to `1`, only one resource is returned. To grab the next resource, we would make a similar request, but with the addition of the cursor as a query parameter:

```json http
{
  "method": "get",
  "url": "https://sandbox.api.cash.app/network/v1/payments",
  "headers": {
    "Accept": "application/json",
    "Authorization": "Client CLIENT_ID API_KEY_ID",
    "X-Region": "SEA",
    "X-Signature": "sandbox:skip-signature-check"
  },
  "query": {
    "limit": 1,
    "cursor": "be167132a9f2b565"
  }
}
```

In the response, notice that there is no longer a `cursor` field:

```json
{
  "payments": [
    {
      "id": "PWC_50n21zyac0v2yhq23vvhk7xkwpc",
      "amount": 100,
      "net_amount": 100,
      "currency": "USD",
      "customer_id": "AUTH_24g7nq7m1je9b6fnzbtvwzqej",
      "merchant_id": "MERCHANT_4vxs5egfk7hmta3qx2h6rp91x",
      "grant_id": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50",
      "status": "CAPTURED",
      "created_at": "2022-01-01T12:00:00Z",
      "updated_at": "2022-01-05T12:00:00Z",
      "reference_id": "external-id"
    }
  ]
}
```

This means that there is no more data to page through; we've now iterated through the entire data set.
