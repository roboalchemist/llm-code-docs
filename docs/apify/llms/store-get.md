# Source: https://docs.apify.com/api/v2/store-get.md

# Get list of Actors in store


```
GET 
https://api.apify.com/v2/store
```


Gets the list of public Actors in Apify Store. You can use `search` parameter to search Actors by string in title, name, description, username and readme. If you need detailed info about a specific Actor, use the  endpoint.

The endpoint supports pagination using the `limit` and `offset` parameters. It will not return more than 1,000 records.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
