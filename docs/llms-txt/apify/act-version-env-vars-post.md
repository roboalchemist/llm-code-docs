# Source: https://docs.apify.com/api/v2/act-version-env-vars-post.md

# Create environment variable


```
POST 
https://api.apify.com/v2/acts/:actorId/versions/:versionNumber/env-vars
```


Creates an environment variable of an Actor using values specified in a  passed as JSON in the POST payload.

The request must specify `name` and `value` parameters (as strings) in the JSON payload and a `Content-Type: application/json` HTTP header.


```
{
    "name": "ENV_VAR_NAME",
    "value": "my-env-var"
}
```


The response is the  as returned by the  endpoint.

## Request

## Responses

* 201
* 400

**Response Headers**

* **Location**

Bad request - invalid input parameters or request body.
