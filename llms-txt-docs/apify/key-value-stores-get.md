# Source: https://docs.apify.com/api/v2/key-value-stores-get.md

# Get list of key-value stores


```
GET 
https://api.apify.com/v2/key-value-stores
```


Clientshttps://docs.apify.com/api/client/python/reference/class/KeyValueStoreCollectionClientAsync#listhttps://docs.apify.com/api/client/js/reference/class/KeyValueStoreCollectionClient#listGets the list of key-value stores owned by the user.

The response is a list of objects, where each objects contains a basic information about a single key-value store.

The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 array elements.

By default, the records are sorted by the `createdAt` field in ascending order, therefore you can use pagination to incrementally fetch all key-value stores while new ones are still being created. To sort the records in descending order, use the `desc=1` parameter.

## Request

## Responses

* 200

**Response Headers**

