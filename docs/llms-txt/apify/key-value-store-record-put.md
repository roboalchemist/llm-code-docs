# Source: https://docs.apify.com/api/v2/key-value-store-record-put.md

# Store record


```
PUT 
https://api.apify.com/v2/key-value-stores/:storeId/records/:recordKey
```


Stores a value under a specific key to the key-value store.

The value is passed as the PUT payload and it is stored with a MIME content type defined by the `Content-Type` header and with encoding defined by the `Content-Encoding` header.

To save bandwidth, storage, and speed up your upload, send the request payload compressed with Gzip compression and add the `Content-Encoding: gzip` header. It is possible to set up another compression type with `Content-Encoding` request header.

Below is a list of supported `Content-Encoding` types.

* Gzip compression: `Content-Encoding: gzip`
* Deflate compression: `Content-Encoding: deflate`
* Brotli compression: `Content-Encoding: br`

## Request

## Responses

* 201
* 400

**Response Headers**

* **Location**

Bad request - invalid input parameters or request body.
