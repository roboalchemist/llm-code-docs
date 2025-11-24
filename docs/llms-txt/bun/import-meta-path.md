# Source: https://bun.com/docs/guides/util/import-meta-path.md

# Get the absolute path of the current file

Bun provides a handful of module-specific utilities on the [`import.meta`](https://bun.com/docs/api/import-meta) object. Use `import.meta.path` to retrieve the absolute path of the current file.

```ts /a/b/c.ts icon="https://mintcdn.com/bun-1dd33a4e/Hq64iapoQXHbYMEN/icons/typescript.svg?fit=max&auto=format&n=Hq64iapoQXHbYMEN&q=85&s=c6cceedec8f82d2cc803d7c6ec82b240" theme={"theme":{"light":"github-light","dark":"dracula"}}
import.meta.path; // => "/a/b/c.ts"
```

***

See [Docs > API > import.meta](https://bun.com/docs/api/import-meta) for complete documentation.
