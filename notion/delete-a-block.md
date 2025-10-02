# Source: https://developers.notion.com/reference/delete-a-block

Sets a [Block object](/reference/block), including page blocks, to `archived: true` using the ID specified. Note: in the Notion UI application, this moves the block to the "Trash" where it can still be accessed and restored.
To restore the block with the API, use the [Update a block](/reference/update-a-block) or [Update page](/reference/patch-page) respectively.
> ##
>
> Integration capabilities
>
> This endpoint requires an integration to have update content capabilities. Attempting to call this API without update content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).
### Errors
Returns a 404 HTTP response if the block doesn't exist, or if the integration doesn't have access to the block.
Returns a 400 or 429 HTTP response if the request exceeds the [request limits](/reference/request-limits).
*Note: Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.*