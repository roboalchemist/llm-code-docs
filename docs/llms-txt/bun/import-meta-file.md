# Source: https://bun.com/docs/guides/util/import-meta-file.md

# Get the file name of the current file

Bun provides a handful of module-specific utilities on the [`import.meta`](https://bun.com/docs/api/import-meta) object. Use `import.meta.file` to retrieve the name of the current file.

```ts /a/b/c.ts icon="https://mintcdn.com/bun-1dd33a4e/Hq64iapoQXHbYMEN/icons/typescript.svg?fit=max&auto=format&n=Hq64iapoQXHbYMEN&q=85&s=c6cceedec8f82d2cc803d7c6ec82b240" theme={"theme":{"light":"github-light","dark":"dracula"}}
import.meta.file; // => "c.ts"
```

***

See [Docs > API > import.meta](https://bun.com/docs/api/import-meta) for complete documentation.
