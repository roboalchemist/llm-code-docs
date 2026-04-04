# Source: https://docs.apify.com/api/v2/actor-runs-get.md

# Get user runs list


```
GET 
https://api.apify.com/v2/actor-runs
```


Gets a list of all runs for a user. The response is a list of objects, where each object contains basic information about a single Actor run.

The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 array elements.

By default, the records are sorted by the `startedAt` field in ascending order. Therefore, you can use pagination to incrementally fetch all records while new ones are still being created. To sort the records in descending order, use `desc=1` parameter. You can also filter runs by `startedAt`` and `status\`\` fields ([available statuses](https://docs.apify.com/platform/actors/running/runs-and-builds#lifecycle)).

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
