# Source: https://docs.apify.com/api/v2/key-value-store-keys-get.md

# Get list of keys


```
GET 
https://api.apify.com/v2/key-value-stores/:storeId/keys
```


Returns a list of objects describing keys of a given key-value store, as well as some information about the values (e.g. size).

This endpoint is paginated using `exclusiveStartKey` and `limit` parameters

* see [Pagination](https://docs.apify.com/api/v2.md#using-key) for more details.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
