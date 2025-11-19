# Source: https://docs.apify.com/api/v2/actor-run-abort-post.md

# Abort run


```
POST 
https://api.apify.com/v2/actor-runs/:runId/abort
```


Clientshttps://docs.apify.com/api/client/python/reference/class/RunClientAsync#aborthttps://docs.apify.com/api/client/js/reference/class/RunClient#abortAborts an Actor run and returns an object that contains all the details about the run.

Only runs that are starting or running are aborted. For runs with status `FINISHED`, `FAILED`, `ABORTING` and `TIMED-OUT` this call does nothing.

## Request

## Responses

* 200

**Response Headers**

