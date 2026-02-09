# Source: https://docs.apify.com/api/v2/key-value-store-record-get.md

# Get record


```
GET 
https://api.apify.com/v2/key-value-stores/:storeId/records/:recordKey
```


Gets a value stored in the key-value store under a specific key.

The response body has the same `Content-Encoding` header as it was set in .

If the request does not define the `Accept-Encoding` HTTP header with the right encoding, the record will be decompressed.

Most HTTP clients support decompression by default. After using the HTTP client with decompression support, the `Accept-Encoding` header is set by the client and body is decompressed automatically.

Please note that for security reasons, Apify API can perform small modifications to HTML documents before they are served via this endpoint. To fetch the raw HTML content without any modifications, use the `attachment` query parameter.

## Request

## Responses

* 200
* 302
* 400

**Response Headers**



**Response Headers**

* **Location**

Bad request - invalid input parameters or request body.
