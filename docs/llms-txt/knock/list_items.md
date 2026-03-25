# Source: https://docs.knock.app/api-reference/users/feeds/list_items.md

### List feed items

Returns a paginated list of feed items for a user in reverse chronological order, including metadata about the feed. If the user has not yet been identified within Knock, an empty feed will be returned.

You can customize the response using [response filters](/integrations/in-app/knock#customizing-api-response-content) to exclude or only include specific properties on your resources.

**Notes:**
* When making this call from a client-side environment, use your publishable key along with a user token.
* This endpoint’s rate limit is always scoped per-user and per-environment. This is true even for requests made without a signed user token.
* Any [attachments](/integrations/email/attachments) present in trigger data are automatically excluded from both the `data` and `activities` fields of `UserInAppFeedResponse`.


**Endpoint:** `GET /v1/users/{user_id}/feeds/{id}`

**Rate limit tier:** 2

