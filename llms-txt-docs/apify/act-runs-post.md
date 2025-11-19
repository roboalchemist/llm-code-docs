# Source: https://docs.apify.com/api/v2/act-runs-post.md

# Run Actor


```
POST 
https://api.apify.com/v2/acts/:actorId/runs
```


Clientshttps://docs.apify.com/api/client/python/reference/class/ActorClientAsync#callhttps://docs.apify.com/api/client/js/reference/class/ActorClient#startRuns an Actor and immediately returns without waiting for the run to finish.

The POST payload including its `Content-Type` header is passed as `INPUT` to the Actor (usually `application/json`).

The Actor is started with the default options; you can override them using various URL query parameters.

The response is the Run object as returned by the  API endpoint.

If you want to wait for the run to finish and receive the actual output of the Actor as the response, please use one of the  API endpoints instead.

To fetch the Actor run results that are typically stored in the default dataset, you'll need to pass the ID received in the `defaultDatasetId` field received in the response JSON to the  API endpoint.

## Request

## Responses

* 201

**Response Headers**

* **Location**
