# Source: https://docs.apify.com/api/v2/act-version-env-vars-get.md

# Get list of environment variables


```
GET 
https://api.apify.com/v2/acts/:actorId/versions/:versionNumber/env-vars
```


Gets the list of environment variables for a specific version of an Actor. The response is a JSON object with the list of , where each contains basic information about a single environment variable.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
