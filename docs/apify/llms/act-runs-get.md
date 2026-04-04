# Source: https://docs.apify.com/api/v2/act-runs-get.md

# Get list of runs


```
GET 
https://api.apify.com/v2/acts/:actorId/runs
```


Gets the list of runs of a specific Actor. The response is a list of objects, where each object contains basic information about a single Actor run.

The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 array elements.

By default, the records are sorted by the `startedAt` field in ascending order, therefore you can use pagination to incrementally fetch all records while new ones are still being created. To sort the records in descending order, use `desc=1` parameter. You can also filter runs by status ([available statuses](https://docs.apify.com/platform/actors/running/runs-and-builds#lifecycle)).

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
