# Source: https://docs.apify.com/api/v2/actor-build-delete.md

# Delete build


```
DELETE 
https://api.apify.com/v2/actor-builds/:buildId
```


Delete the build. The build that is the current default build for the Actor cannot be deleted.

Only users with build permissions for the Actor can delete builds.

## Request

## Responses

* 204
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
