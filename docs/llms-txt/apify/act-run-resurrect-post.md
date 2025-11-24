# Source: https://docs.apify.com/api/v2/act-run-resurrect-post.md

# Resurrect run


```
POST 
https://api.apify.com/v2/acts/:actorId/runs/:runId/resurrect
```


**\[DEPRECATED]** API endpoints related to run of the Actor were moved under new namespace .Resurrects a finished Actor run and returns an object that contains all the details about the resurrected run.

Only finished runs, i.e. runs with status `FINISHED`, `FAILED`, `ABORTED` and `TIMED-OUT` can be resurrected. Run status will be updated to RUNNING and its container will be restarted with the same storages (the same behaviour as when the run gets migrated to the new server).

For more information, see the https://docs.apify.com/platform/actors/running/runs-and-builds#resurrection-of-finished-run.

## Request

## Responses

* 200

**Response Headers**

