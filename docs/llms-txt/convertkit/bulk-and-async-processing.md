# Source: https://developers.kit.com/api-reference/bulk-and-async-processing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk & async processing

> Working with our bulk endpoints

We support bulk processing for some common use cases, e.g. create subscribers, requiring OAuth authentication.

These endpoints exist in the bulk namespace, i.e. `https://api.kit.com/v4/bulk/`.

In our bulk requests, we support synchronous processing for small batch sizes. The cut off size is clearly documented in each bulk request's documentation below.

For large batch sizes, we use an asynchronous callback design. If you include a `callback_url` in your request body, we’ll `POST` to that URL when our processing has completed. Our `POST` request body will be the same response shape as our documented our synchronous `200 OK` use case for each endpoint.

If you try to enqueue too many bulk requests at once, you'll receive an error response with a `413` status code, which your code should gracefully handle. Try again after a short period.

<Note>We can receive up to 300MB of request data per app, per creator account, before we respond with a `413` status. This is shared across all bulk requests (e.g. bulk creation of subscribers and tags).</Note>


Built with [Mintlify](https://mintlify.com).