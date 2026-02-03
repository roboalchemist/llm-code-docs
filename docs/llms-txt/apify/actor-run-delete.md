# Source: https://docs.apify.com/api/v2/actor-run-delete.md

# Delete run


```
DELETE 
https://api.apify.com/v2/actor-runs/:runId
```


Delete the run. Only finished runs can be deleted. Only the person or organization that initiated the run can delete it.

## Request

## Responses

* 204
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
