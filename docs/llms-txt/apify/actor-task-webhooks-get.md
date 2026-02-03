# Source: https://docs.apify.com/api/v2/actor-task-webhooks-get.md

# Get list of webhooks


```
GET 
https://api.apify.com/v2/actor-tasks/:actorTaskId/webhooks
```


Gets the list of webhooks of a specific Actor task. The response is a JSON with the list of objects, where each object contains basic information about a single webhook.

The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 records.

By default, the records are sorted by the `createdAt` field in ascending order, to sort the records in descending order, use the `desc=1` parameter.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
