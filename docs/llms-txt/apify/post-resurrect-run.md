# Source: https://docs.apify.com/api/v2/post-resurrect-run.md

# Resurrect run


```
POST 
https://api.apify.com/v2/actor-runs/:runId/resurrect
```


Clientshttps://docs.apify.com/api/client/python/reference/class/RunClientAsync#resurrecthttps://docs.apify.com/api/client/js/reference/class/RunClient#resurrectResurrects a finished Actor run and returns an object that contains all the details about the resurrected run. Only finished runs, i.e. runs with status `FINISHED`, `FAILED`, `ABORTED` and `TIMED-OUT` can be resurrected. Run status will be updated to RUNNING and its container will be restarted with the same storages (the same behaviour as when the run gets migrated to the new server).

For more information, see the https://docs.apify.com/platform/actors/running/runs-and-builds#resurrection-of-finished-run.

## Request

## Responses

* 200

**Response Headers**

