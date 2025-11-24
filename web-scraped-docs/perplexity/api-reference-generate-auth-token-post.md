# Source: https://docs.perplexity.ai/api-reference/generate-auth-token-post

#### Authorizations
[​](https://docs.perplexity.ai/api-reference/generate-auth-token-post#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Body
application/json
[​](https://docs.perplexity.ai/api-reference/generate-auth-token-post#body-token-name)
token_name
string
Optional name for the authentication token to help identify its purpose.
Example:
`"Production API Key"`
#### Response
200 - application/json
Successfully generated authentication token.
[​](https://docs.perplexity.ai/api-reference/generate-auth-token-post#response-auth-token)
auth_token
string
required
The newly generated authentication token. Store this securely as it cannot be retrieved again.
Example:
`"pplx-1234567890abcdef"`
[​](https://docs.perplexity.ai/api-reference/generate-auth-token-post#response-created-at-epoch-seconds)
created_at_epoch_seconds
number
required
Unix timestamp (in seconds) of when the token was created.
Example:
`1735689600`
[​](https://docs.perplexity.ai/api-reference/generate-auth-token-post#response-token-name)
token_name
string
The name associated with this token, if provided.
Example:
`"Production API Key"`
