# Source: https://docs.apify.com/api/v2/key-value-stores-post.md

# Create key-value store


```
POST 
https://api.apify.com/v2/key-value-stores
```


Clientshttps://docs.apify.com/api/client/python/reference/class/KeyValueStoreCollectionClientAsync#get_or_createhttps://docs.apify.com/api/client/js/reference/class/KeyValueStoreCollectionClient#getOrCreateCreates a key-value store and returns its object. The response is the same object as returned by the  endpoint.

Keep in mind that data stored under unnamed store follows https://docs.apify.com/platform/storage#data-retention.

It creates a store with the given name if the parameter name is used. If there is another store with the same name, the endpoint does not create a new one and returns the existing object instead.

## Request

## Responses

* 201

**Response Headers**

* **Location**
