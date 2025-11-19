# Source: https://docs.apify.com/api/v2/actor-build-abort-post.md

# Abort build


```
POST 
https://api.apify.com/v2/actor-builds/:buildId/abort
```


Clientshttps://docs.apify.com/api/client/python/reference/class/BuildClientAsync#aborthttps://docs.apify.com/api/client/js/reference/class/BuildClient#abortAborts an Actor build and returns an object that contains all the details about the build.

Only builds that are starting or running are aborted. For builds with status `FINISHED`, `FAILED`, `ABORTING` and `TIMED-OUT` this call does nothing.

## Request

## Responses

* 200

**Response Headers**

