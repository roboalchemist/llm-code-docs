# Source: https://docs.perplexity.ai/api-reference/async-chat-completions-get

#### Authorizations
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-get#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Query Parameters
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-get#parameter-limit)
limit
integer
default:20
Maximum number of requests to return.
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-get#parameter-next-token)
next_token
string
Token for fetching the next page of results. Ensure this token is URL-encoded when passed as a query parameter.
#### Response
200 - application/json
Successfully retrieved list of async chat completion requests.
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-get#response-requests)
requests
AsyncApiChatCompletionsResponseSummary · object[]
required
Show child attributes
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-get#response-next-token)
next_token
string | null
Token for fetching the next page of results.
