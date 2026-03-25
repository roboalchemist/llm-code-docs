# Source: https://docs.ghost.org/themes/helpers/data/authors.md

# Source: https://docs.ghost.org/content-api/authors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Authors

> Authors are a subset of [users](/staff/) who have published posts associated with them.

```js  theme={"dark"}
GET /content/authors/
GET /content/authors/{id}/
GET /content/authors/slug/{slug}/
```

Authors that are not associated with a post are not returned. You can supply `include=count.posts` to retrieve the number of posts associated with an author.

<ResponseExample>
  ```json  theme={"dark"}
  {
      "authors": [
          {
              "slug": "cameron",
              "id": "5ddc9b9510d8970038255d02",
              "name": "Cameron Almeida",
              "profile_image": "https://docs.ghost.io/content/images/2019/03/1c2f492a-a5d0-4d2d-b350-cdcdebc7e413.jpg",
              "cover_image": null,
              "bio": "Editor at large.",
              "website": "https://example.com",
              "location": "Cape Town",
              "facebook": "example",
              "twitter": "@example",
              "meta_title": null,
              "meta_description": null,
              "url": "https://docs.ghost.io/author/cameron/"
          }
      ]
  }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).