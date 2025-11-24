# Source: https://developers.notion.com/reference/delete-a-block

Sets a [Block object](https://developers.notion.com/reference/block), including page blocks, to `archived: true` using the ID specified. Note: in the Notion UI application, this moves the block to the "Trash" where it can still be accessed and restored. 
To restore the block with the API, use the [Update a block](https://developers.notion.com/reference/update-a-block) or [Update page](https://developers.notion.com/reference/patch-page) respectively. 
> ## 📘
> Integration capabilities
> This endpoint requires an integration to have update content capabilities. Attempting to call this API without update content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](https://developers.notion.com/reference/capabilities).
### [](https://developers.notion.com/reference/delete-a-block#errors)
Returns a 404 HTTP response if the block doesn't exist, or if the integration doesn't have access to the block.
Returns a 400 or 429 HTTP response if the request exceeds the [request limits](https://developers.notion.com/reference/request-limits).
_Note: Each Public API endpoint can return several possible error codes. See the[Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information._
