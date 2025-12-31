# Source: https://docs.apify.com/api/v2/act-build-abort-post.md

# Abort build


```
POST 
https://api.apify.com/v2/acts/:actorId/builds/:buildId/abort
```


deprecated

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

**\[DEPRECATED]** API endpoints related to build of the Actor were moved under new namespace . Aborts an Actor build and returns an object that contains all the details about the build.

Only builds that are starting or running are aborted. For builds with status `FINISHED`, `FAILED`, `ABORTING` and `TIMED-OUT` this call does nothing.

## Request

## Responses

* 200

**Response Headers**

