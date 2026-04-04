# Source: https://docs.ghost.org/content-api/pages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Pages

> Pages are static resources that are not included in channels or collections on the Ghost front-end. The API will only return pages that were created as resources and will not contain routes created with [dynamic routing](/themes/routing/).

```js  theme={"dark"}
GET /content/pages/
GET /content/pages/{id}/
GET /content/pages/slug/{slug}/
```

Pages are structured identically to posts. The response object will look the same, only the resource key will be `pages`.

By default, pages are ordered by title when fetching more than one.


Built with [Mintlify](https://mintlify.com).