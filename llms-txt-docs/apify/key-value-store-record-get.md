# Source: https://docs.apify.com/api/v2/key-value-store-record-get.md

# Get record


```
GET 
https://api.apify.com/v2/key-value-stores/:storeId/records/:recordKey
```


Clientshttps://docs.apify.com/api/client/python/reference/class/KeyValueStoreClientAsync#get_recordhttps://docs.apify.com/api/client/js/reference/class/KeyValueStoreClient#getRecordGets a value stored in the key-value store under a specific key.

The response body has the same `Content-Encoding` header as it was set in .

If the request does not define the `Accept-Encoding` HTTP header with the right encoding, the record will be decompressed.

Most HTTP clients support decompression by default. After using the HTTP client with decompression support, the `Accept-Encoding` header is set by the client and body is decompressed automatically.

## Request

## Responses

* 200
* 302

**Response Headers**



**Response Headers**

* **Location**
