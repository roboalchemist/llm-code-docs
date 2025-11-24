# Source: https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags.md

# Source: https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags.md

# generateEtags
@doc-version: 16.0.4


Next.js will generate [etags](https://en.wikipedia.org/wiki/HTTP_ETag) for every page by default. You may want to disable etag generation for HTML pages depending on your cache strategy.

Open `next.config.js` and disable the `generateEtags` option:

```js filename="next.config.js"
module.exports = {
  generateEtags: false,
}
```