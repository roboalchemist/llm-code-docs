# Source: https://docs.port.io/api-reference/create-an-access-token.md

# Create an access token

```
POST 
/v1/auth/access_token
```

This route allows you to create an access token for your Port account. You can use this token to authenticate your requests to the Port API.<br /><br />To obtain your client ID and client secret, go to your [Port application](https://app.getport.io), click on the `...` button in the top right corner, then click `Credentials`.

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 200
* 401
* 404
* 413
* 422

Authorized successfully

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
