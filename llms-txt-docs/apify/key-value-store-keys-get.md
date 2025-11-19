# Source: https://docs.apify.com/api/v2/key-value-store-keys-get.md

# Get list of keys


```
GET 
https://api.apify.com/v2/key-value-stores/:storeId/keys
```


Clientshttps://docs.apify.com/api/client/python/reference/class/KeyValueStoreClientAsync#list_keyshttps://docs.apify.com/api/client/js/reference/class/KeyValueStoreClient#listKeysReturns a list of objects describing keys of a given key-value store, as well as some information about the values (e.g. size).

This endpoint is paginated using `exclusiveStartKey` and `limit` parameters

* see https://docs.apify.com/api/v2.md#using-key for more details.

## Request

## Responses

* 200

**Response Headers**

