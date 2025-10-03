# Source: https://developers.notion.com/reference/create-a-comment

Returns a [comment object](https://developers.notion.com/reference/comment-object) for the created comment.
There are three locations where a new comment can be added with the public API:
  1. A page
  2. A block
  3. An existing discussion thread


The request body will differ slightly depending on which type of comment is being added with this endpoint.
To add a new comment to a page or block, a `parent` object with a `page_id` or `block_id` must be provided in the body params. 
To add a new comment to an existing discussion thread, a `discussion_id` string must be provided in the body params. (Inline comments to start a new discussion thread cannot be created via the public API.)
**_Either_ the `parent.page_id` , `parent.block_id` _or_ `discussion_id` parameter must be provided — ONLY one can be specified**.
To see additional examples of creating a [page](https://developers.notion.com/docs/working-with-comments#adding-a-comment-to-a-page) or [discussion](https://developers.notion.com/docs/working-with-comments#responding-to-a-discussion-thread) comment and to learn more about comments in Notion, see the [Working with comments](https://developers.notion.com/docs/working-with-comments) guide.
### [](https://developers.notion.com/reference/create-a-comment#errors)
Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
> ## 📘
> Reminder: Turn on integration comment capabilities
> Integration capabilities for reading and inserting comments are off by default.
> This endpoint requires an integration to have insert comment capabilities. Attempting to call this endpoint without insert comment capabilities will return an HTTP response with a 403 status code. 
> For more information on integration capabilities, see the [capabilities guide](https://developers.notion.com/reference/capabilities). To update your integration settings, visit the [integration dashboard](https://www.notion.so/my-integrations).
