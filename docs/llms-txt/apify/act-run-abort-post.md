# Source: https://docs.apify.com/api/v2/act-run-abort-post.md

# Abort run


```
POST 
https://api.apify.com/v2/acts/:actorId/runs/:runId/abort
```


deprecated

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

**\[DEPRECATED]** API endpoints related to run of the Actor were moved under new namespace . Aborts an Actor run and returns an object that contains all the details about the run.

Only runs that are starting or running are aborted. For runs with status `FINISHED`, `FAILED`, `ABORTING` and `TIMED-OUT` this call does nothing.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
