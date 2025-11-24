# Source: https://developers.notion.com/reference/update-a-block

Updates the content for the specified `block_id` based on the block type. Supported fields based on the block object type (see [Block object](https://developers.notion.com/reference/block#block-type-object) for available fields and the expected input for each field). 
**Note** : The update replaces the _entire_ value for a given field. If a field is omitted (ex: omitting `checked` when updating a `to_do` block), the value will not be changed. 
> ## 📘
> Updating `child_page` blocks
> To update `child_page` type blocks, use the [Update page](https://developers.notion.com/reference/patch-page) endpoint. Updating the page's `title` updates the text displayed in the associated `child_page` block.
> ## 📘
> Updating `child_database` blocks
> To update `child_database` type blocks, use the [Update database](https://developers.notion.com/reference/update-a-database) endpoint. Updating the page's `title` updates the text displayed in the associated `child_database` block.
> ## 📘
> Updating `children`
> A block's children _CANNOT_ be directly updated with this endpoint. Instead use [Append block children](https://developers.notion.com/reference/patch-block-children) to add children.
> ## 📘
> Updating `heading` blocks
> To update the toggle of a `heading` block, you can include the optional `is_toggleable` property in the request. Toggle can be added and removed from a `heading` block. However, you cannot remove toggle from a `heading` block if it has children. All children _MUST_ be removed before revoking toggle from a `heading` block.
### [](https://developers.notion.com/reference/update-a-block#success)
Returns a 200 HTTP response containing the updated [block object](https://developers.notion.com/reference/block) on success.
> ## 📘
> Integration capabilities
> This endpoint requires an integration to have update content capabilities. Attempting to call this API without update content capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](https://developers.notion.com/reference/capabilities).
### [](https://developers.notion.com/reference/update-a-block#errors)
Returns a 404 HTTP response if the block doesn't exist, has been archived, or if the integration doesn't have access to the page.
Returns a 400 if the `type` for the block is incorrect or the input is incorrect for a given field.
Returns a 400 or a 429 HTTP response if the request exceeds the [request limits](https://developers.notion.com/reference/request-limits).
_Note: Each Public API endpoint can return several possible error codes. See the[Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information._
