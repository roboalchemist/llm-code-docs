# Source: https://docs.apify.com/api/v2/actor-tasks-get.md

# Get list of tasks


```
GET 
https://api.apify.com/v2/actor-tasks
```


Clientshttps://docs.apify.com/api/client/python/reference/class/TaskCollectionClientAsync#listhttps://docs.apify.com/api/client/js/reference/class/TaskCollectionClient#listGets the complete list of tasks that a user has created or used.

The response is a list of objects in which each object contains essential information about a single task.

The endpoint supports pagination using the `limit` and `offset` parameters, and it does not return more than a 1000 records.

By default, the records are sorted by the `createdAt` field in ascending order; therefore you can use pagination to incrementally fetch all tasks while new ones are still being created. To sort the records in descending order, use the `desc=1` parameter.

## Request

## Responses

* 200

**Response Headers**

