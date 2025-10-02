# Source: https://developers.notion.com/reference/list-comments

See [Pagination](/reference/intro#pagination) for details about how to use a cursor to iterate through the list.
### Errors
Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.
> ##
>
> Reminder: Turn on integration comment capabilities
>
> Integration capabilities for reading and inserting comments are off by default.
>
> This endpoint requires an integration to have read comment capabilities. Attempting to call this endpoint without read comment capabilities will return an HTTP response with a 403 status code.
>
> For more information on integration capabilities, see the [capabilities guide](/reference/capabilities). To update your integration settings, visit the [integration dashboard](https://www.notion.so/my-integrations).