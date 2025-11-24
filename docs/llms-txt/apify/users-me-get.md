# Source: https://docs.apify.com/api/v2/users-me-get.md

# Get private user data


```
GET 
https://api.apify.com/v2/users/me
```


Returns information about the current user account, including both public and private information.

The user account is identified by the provided authentication token.

The fields `plan`, `email` and `profile` are omitted when this endpoint is accessed from Actor run.

## Responses

* 200

**Response Headers**

