# Source: https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader.md

# Source: https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader.md

# Source: https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader.md

# Source: https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader.md

# Source: https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader.md

# Source: https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader.md

# poweredByHeader
@doc-version: 16.0.4


By default Next.js will add the `x-powered-by` header. To opt-out of it, open `next.config.js` and disable the `poweredByHeader` config:

```js filename="next.config.js"
module.exports = {
  poweredByHeader: false,
}
```