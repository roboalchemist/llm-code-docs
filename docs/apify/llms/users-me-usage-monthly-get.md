# Source: https://docs.apify.com/api/v2/users-me-usage-monthly-get.md

# Get monthly usage


```
GET 
https://api.apify.com/v2/users/me/usage/monthly
```


Returns a complete summary of your usage for the current usage cycle, an overall sum, as well as a daily breakdown of usage. It is the same information you will see on your account's [Billing page](https://console.apify.com/billing#/usage). The information includes your use of storage, data transfer, and request queue usage.

Using the `date` parameter will show your usage in the usage cycle that includes that date.

## Request

## Responses

* 200
* 400

**Response Headers**



Bad request - invalid input parameters or request body.
