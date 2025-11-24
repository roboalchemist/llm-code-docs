# Source: https://docs.apify.com/api/v2/schedules-post.md

# Create schedule


```
POST 
https://api.apify.com/v2/schedules
```


Clientshttps://docs.apify.com/api/client/python/reference/class/ScheduleCollectionClientAsync#createhttps://docs.apify.com/api/client/js/reference/class/ScheduleCollectionClient#createCreates a new schedule with settings provided by the schedule object passed as JSON in the payload. The response is the created schedule object.

The request needs to specify the `Content-Type: application/json` HTTP header!

When providing your API authentication token, we recommend using the request's `Authorization` header, rather than the URL. ().

## Request

## Responses

* 201

**Response Headers**

* **Location**
