# Source: https://docs.apify.com/api/v2/actor-builds-get.md

# Get user builds list


```
GET 
https://api.apify.com/v2/actor-builds
```


Gets a list of all builds for a user. The response is a JSON array of objects, where each object contains basic information about a single build.

The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 records.

By default, the records are sorted by the `startedAt` field in ascending order. Therefore, you can use pagination to incrementally fetch all builds while new ones are still being started. To sort the records in descending order, use the `desc=1` parameter.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
