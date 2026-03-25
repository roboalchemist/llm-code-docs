# Source: https://docs.ghost.org/admin-api/posts/publishing-a-post.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Publishing a Post

Publish a draft post by updating its status to `published`:

<RequestExample>
  ```json  theme={"dark"}
  // PUT admin/posts/5b7ada404f87d200b5b1f9c8/
  {
      "posts": [
          {
              "updated_at": "2022-06-05T20:52:37.000Z",
              "status": "published"
          }
      ]
  }
  ```
</RequestExample>


Built with [Mintlify](https://mintlify.com).