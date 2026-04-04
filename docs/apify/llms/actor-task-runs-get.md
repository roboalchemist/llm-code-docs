# Source: https://docs.apify.com/api/v2/actor-task-runs-get.md

# Get list of task runs


```
GET 
https://api.apify.com/v2/actor-tasks/:actorTaskId/runs
```


Get a list of runs of a specific task. The response is a list of objects, where each object contains essential information about a single task run.

The endpoint supports pagination using the `limit` and `offset` parameters, and it does not return more than a 1000 array elements.

By default, the records are sorted by the `startedAt` field in ascending order; therefore you can use pagination to incrementally fetch all records while new ones are still being created. To sort the records in descending order, use the `desc=1` parameter. You can also filter runs by status ([available statuses](https://docs.apify.com/platform/actors/running/runs-and-builds#lifecycle)).

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
