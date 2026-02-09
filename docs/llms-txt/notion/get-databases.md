# Source: https://developers.notion.com/reference/get-databases.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.notion.com/llms.txt
> Use this file to discover all available pages before exploring further.

# null

<Danger>
  **Deprecated as of version 2025-09-03**

  This endpoint is deprecated and is only available on API version "2021-08-16" and earlier. Use the [Search API](/reference/post-search) instead. This endpoint will only return explicitly shared databases, while search will also return child pages. This endpoint's results cannot be filtered, while search can be used to match on page title.
</Danger>

List all [Databases](/reference/database) shared with the authenticated integration. The response may contain fewer than `page_size` of results.

<Info>
  **Database access**

  Integrations can only access databases a user has shared with the integration.
</Info>

See [Pagination](/reference/pagination) for details about how to use a cursor to iterate through the list.

<Info>
  **Integration capabilities**

  This endpoint requires an integration to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).
</Info>

### Errors

Returns a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
