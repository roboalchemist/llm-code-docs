# Source: https://docs.apify.com/api/v2/actor-task-runs-post.md

# Run task


```
POST 
https://api.apify.com/v2/actor-tasks/:actorTaskId/runs
```


Runs an Actor task and immediately returns without waiting for the run to finish.

Optionally, you can override the Actor input configuration by passing a JSON object as the POST payload and setting the `Content-Type: application/json` HTTP header.

Note that if the object in the POST payload does not define a particular input property, the Actor run uses the default value defined by the task (or Actor's input schema if not defined by the task).

The response is the Actor Run object as returned by the  endpoint.

If you want to wait for the run to finish and receive the actual output of the Actor run as the response, use one of the  API endpoints instead.

To fetch the Actor run results that are typically stored in the default dataset, you'll need to pass the ID received in the `defaultDatasetId` field received in the response JSON to the  API endpoint.

## Request

## Responses

* 201
* 400

**Response Headers**

* **Location**

Bad request - invalid input parameters or request body.
