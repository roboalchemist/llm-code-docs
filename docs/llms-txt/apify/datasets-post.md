# Source: https://docs.apify.com/api/v2/datasets-post.md

# Create dataset


```
POST 
https://api.apify.com/v2/datasets
```


Clientshttps://docs.apify.com/api/client/python/reference/class/DatasetCollectionClientAsync#get_or_createhttps://docs.apify.com/api/client/js/reference/class/DatasetCollectionClient#getOrCreateCreates a dataset and returns its object. Keep in mind that data stored under unnamed dataset follows https://docs.apify.com/platform/storage#data-retention. It creates a dataset with the given name if the parameter name is used. If a dataset with the given name already exists then returns its object.

## Request

## Responses

* 201

**Response Headers**

* **Location**
