# Source: https://docs.apify.com/api/v2/schedules-post.md

# Create schedule


```
POST 
https://api.apify.com/v2/schedules
```


Creates a new schedule with settings provided by the schedule object passed as JSON in the payload. The response is the created schedule object.

The request needs to specify the `Content-Type: application/json` HTTP header!

When providing your API authentication token, we recommend using the request's `Authorization` header, rather than the URL. ().

## Request

## Responses

* 201
* 400

**Response Headers**

* **Location**

Bad request - invalid input parameters or request body.
