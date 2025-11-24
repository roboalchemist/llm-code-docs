# Source: https://docs.apify.com/api/v2/schedules-get.md

# Get list of schedules


```
GET 
https://api.apify.com/v2/schedules
```


Clientshttps://docs.apify.com/api/client/python/reference/class/ScheduleCollectionClientAsync#listhttps://docs.apify.com/api/client/js/reference/class/ScheduleCollectionClient#listGets the list of schedules that the user created.

The endpoint supports pagination using the `limit` and `offset` parameters. It will not return more than 1000 records.

By default, the records are sorted by the `createdAt` field in ascending order. To sort the records in descending order, use the `desc=1` parameter.

## Request

## Responses

* 200

**Response Headers**

