# Source: https://docs.apify.com/api/v2/acts-get.md

# Get list of Actors


```
GET 
https://api.apify.com/v2/acts
```


Gets the list of all Actors that the user created or used. The response is a list of objects, where each object contains a basic information about a single Actor.

To only get Actors created by the user, add the `my=1` query parameter.

The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 records.

By default, the records are sorted by the `createdAt` field in ascending order, therefore you can use pagination to incrementally fetch all Actors while new ones are still being created. To sort the records in descending order, use the `desc=1` parameter.

You can also sort by your last run by using the `sortBy=stats.lastRunStartedAt` query parameter. In this case, descending order means the most recently run Actor appears first.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
