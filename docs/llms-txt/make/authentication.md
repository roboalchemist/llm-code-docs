# Source: https://developers.make.com/api-documentation/authentication.md

# Authentication

The Make API requires authentication of the API requests with your API tokens or your OAuth 2.0 connection. If your requests are not authenticated, the Make API will return an authentication error.

## Authentication token

To authenticate your API request, send your API token in the following HTTP `header` parameter:

```http
Authorization: Token 12345678-12ef-abcd-1234-1234567890ab
```

The authentication token always contains information about the access to the API resources. The authentication token access is defined with API scopes. If you want to learn about Make API scopes, continue to the [Make API scopes overview](https://developers.make.com/api-documentation/authentication/api-scopes-overview).

To learn how to create and manage your API token, go to the [creating](https://developers.make.com/api-documentation/authentication/create-authentication-token) and [management](https://developers.make.com/api-documentation/authentication/authentication-managing) sections.

## OAuth 2.0 connection

As an alternative to using an authentication token, you can request an OAuth 2.0 connection to access resources on the Make platform. OAuth 2.0 access is defined with API scopes. To learn more about this connection type and to request access, continue to the [requesting-an-oauth-2.0-client](https://developers.make.com/api-documentation/authentication/requesting-an-oauth-2.0-client "mention") section.
