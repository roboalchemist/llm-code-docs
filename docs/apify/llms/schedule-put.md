# Source: https://docs.apify.com/api/v2/schedule-put.md

# Update schedule


```
PUT 
https://api.apify.com/v2/schedules/:scheduleId
```


Updates a schedule using values specified by a schedule object passed as JSON in the POST payload. If the object does not define a specific property, its value will not be updated.

The response is the full schedule object as returned by the  endpoint.

**The request needs to specify the `Content-Type: application/json` HTTP header!**

When providing your API authentication token, we recommend using the request's `Authorization` header, rather than the URL. ().

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
