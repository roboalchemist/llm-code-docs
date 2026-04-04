# Source: https://docs.ghost.org/admin-api/posts/email-only-posts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Email only posts

To send a post as an email without publishing it on the site, the `email_only` property must be set to `true` when publishing or scheduling the post in combination with the `newsletter` parameter:

<RequestExample>
  ```json  theme={"dark"}
  // PUT admin/posts/5b7ada404f87d200b5b1f9c8/?newsletter=weekly-newsletter
  {
      "posts": [
          {
              "updated_at": "2022-06-05T20:52:37.000Z",
              "status": "published",
              "email_only": true
          }
      ]
  }
  ```
</RequestExample>

When an email-only post has been sent, the post will have a `status` of `sent`.


Built with [Mintlify](https://mintlify.com).