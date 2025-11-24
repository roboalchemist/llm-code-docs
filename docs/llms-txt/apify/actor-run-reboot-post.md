# Source: https://docs.apify.com/api/v2/actor-run-reboot-post.md

# Reboot run


```
POST 
https://api.apify.com/v2/actor-runs/:runId/reboot
```


Clientshttps://docs.apify.com/api/client/python/reference/class/RunClientAsync#reboothttps://docs.apify.com/api/client/js/reference/class/RunClient#rebootReboots an Actor run and returns an object that contains all the details about the rebooted run.

Only runs that are running, i.e. runs with status `RUNNING` can be rebooted.

The run's container will be restarted, so any data not persisted in the key-value store, dataset, or request queue will be lost.

## Request

## Responses

* 200

**Response Headers**

