# Source: https://docs.perplexity.ai/api-reference/async-chat-completions-post

#### Authorizations
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-post#authorization-authorization)
Authorization
string
header
required
Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.
#### Body
application/json
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-post#body-request)
request
object
required
Show child attributes
#### Response
200 - application/json
Successfully created async chat completion job.
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-post#response-id)
id
string
required
Unique identifier for the asynchronous job.
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-post#response-model)
model
string
required
The model used for the request.
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-post#response-created-at)
created_at
integer
required
Unix timestamp of when the job was created.
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-post#response-status)
status
enum<string>
required
The status of an asynchronous processing job.
Available options:
`CREATED`,
`IN_PROGRESS`,
`COMPLETED`,
`FAILED`
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-post#response-started-at)
started_at
integer | null
Unix timestamp of when processing started.
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-post#response-completed-at)
completed_at
integer | null
Unix timestamp of when processing completed.
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-post#response-response)
response
object
The actual chat completion response, available when status is COMPLETED.
Show child attributes
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-post#response-failed-at)
failed_at
integer | null
Unix timestamp of when processing failed.
[​](https://docs.perplexity.ai/api-reference/async-chat-completions-post#response-error-message)
error_message
string | null
Error message if the job failed.
