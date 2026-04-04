# Source: https://docs.apify.com/api/v2/datasets-post.md

# Create dataset


```
POST 
https://api.apify.com/v2/datasets
```


Creates a dataset and returns its object. Keep in mind that data stored under unnamed dataset follows [data retention period](https://docs.apify.com/platform/storage#data-retention). It creates a dataset with the given name if the parameter name is used. If a dataset with the given name already exists then returns its object.

## Request

## Responses

* 201
* 400

**Response Headers**

* **Location**

Bad request - invalid input parameters or request body.
