# Source: https://docs.apify.com/api/v2/webhook-dispatches-get.md

# Get list of webhook dispatches


```
GET 
https://api.apify.com/v2/webhook-dispatches
```


Gets the list of webhook dispatches that the user have.

The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 records. By default, the records are sorted by the `createdAt` field in ascending order. To sort the records in descending order, use the `desc=1` parameter.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
