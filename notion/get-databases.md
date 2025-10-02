# Source: https://developers.notion.com/reference/get-databases

> ##
>
> Search pages for more details
>
> This endpoint is deprecated and is only available on API version "2021-08-16" and earlier. Use the [Search API](/reference/post-search) instead. This endpoint will only return explicitly shared databases, while search will also return child pages. This endpoint's results cannot be filtered, while search can be used to match on page title.
List all [Databases](/reference/database) shared with the authenticated integration. The response may contain fewer than `page_size` of results.
> ##
>
> Database access
>
> Integrations can only access databases a user has shared with the integration.
See [Pagination](/reference/pagination) for details about how to use a cursor to iterate through the list.
> ##
>
> Integration capabilities
>
> This endpoint requires an integration to have read content capabilities. Attempting to call this API without read content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).
### Errors
Returns a 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).