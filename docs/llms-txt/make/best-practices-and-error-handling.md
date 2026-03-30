# Source: https://developers.make.com/api-documentation/authentication/oauth-flow/best-practices-and-error-handling.md

# Best practices and error handling

### Security best practices

* Validate the `state` parameter to prevent CSRF attacks
* Store secrets securely (confidential clients only)
* Implement proper error handling for expired or invalid tokens

### Common scopes

* `openid`: Required for OpenID Connect authentication
* Add other Make-specific scopes as needed for your application

### Error handling

Common error responses from the token endpoint:

<table><thead><tr><th width="252.61328125">Error </th><th>Description</th></tr></thead><tbody><tr><td><code>invalid_request</code></td><td>Missing or invalid parameters</td></tr><tr><td><code>invalid_client</code></td><td>Invalid client credentials</td></tr><tr><td><code>invalid_grant</code></td><td>Invalid or expired authorization code</td></tr><tr><td><code>unsupported_grant_type</code></td><td>Grant type not supported</td></tr></tbody></table>

Always check the response status and handle errors appropriately in your application.
