# Source: https://docs.perplexity.ai/api-reference/revoke-auth-token-post

#### Authorizations
[​](https://docs.perplexity.ai/api-reference/revoke-auth-token-post#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Body
application/json
[​](https://docs.perplexity.ai/api-reference/revoke-auth-token-post#body-auth-token)
auth_token
string
required
The authentication token to revoke.
Example:
`"pplx-1234567890abcdef"`
#### Response
200
Successfully revoked authentication token.
