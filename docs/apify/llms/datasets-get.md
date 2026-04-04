# Source: https://docs.apify.com/api/v2/datasets-get.md

# Get list of datasets


```
GET 
https://api.apify.com/v2/datasets
```


Lists all of a user's datasets.

The response is a JSON array of objects, where each object contains basic information about one dataset.

By default, the objects are sorted by the `createdAt` field in ascending order, therefore you can use pagination to incrementally fetch all datasets while new ones are still being created. To sort them in descending order, use `desc=1` parameter. The endpoint supports pagination using `limit` and `offset` parameters and it will not return more than 1000 array elements.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
