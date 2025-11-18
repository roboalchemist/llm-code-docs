# Source: https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions.md

# Source: https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions.md

# Source: https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions.md

# pageExtensions
@doc-version: 16.0.3


You can extend the default Page extensions (`.tsx`, `.ts`, `.jsx`, `.js`) used by Next.js. Inside `next.config.js`, add the `pageExtensions` config:

```js filename="next.config.js"
module.exports = {
  pageExtensions: ['mdx', 'md', 'jsx', 'js', 'tsx', 'ts'],
}
```

Changing these values affects *all* Next.js pages, including the following:

* [`proxy.js`](/docs/pages/api-reference/file-conventions/proxy.md)
* [`instrumentation.js`](/docs/pages/guides/instrumentation.md)
* `pages/_document.js`
* `pages/_app.js`
* `pages/api/`

For example, if you reconfigure `.ts` page extensions to `.page.ts`, you would need to rename pages like `proxy.page.ts`, `instrumentation.page.ts`, `_app.page.ts`.

## Including non-page files in the `pages` directory

You can colocate test files or other files used by components in the `pages` directory. Inside `next.config.js`, add the `pageExtensions` config:

```js filename="next.config.js"
module.exports = {
  pageExtensions: ['page.tsx', 'page.ts', 'page.jsx', 'page.js'],
}
```

Then, rename your pages to have a file extension that includes `.page` (e.g. rename `MyPage.tsx` to `MyPage.page.tsx`). Ensure you rename *all* Next.js pages, including the files mentioned above.