# Source: https://bun.com/docs/guides/util/entrypoint.md

# Check if the current file is the entrypoint

Bun provides a handful of module-specific utilities on the [`import.meta`](https://bun.com/docs/api/import-meta) object. Use `import.meta.main` to check if the current file is the entrypoint of the current process.

```ts index.ts icon="https://mintcdn.com/bun-1dd33a4e/Hq64iapoQXHbYMEN/icons/typescript.svg?fit=max&auto=format&n=Hq64iapoQXHbYMEN&q=85&s=c6cceedec8f82d2cc803d7c6ec82b240" theme={"theme":{"light":"github-light","dark":"dracula"}}
if (import.meta.main) {
  // this file is directly executed with `bun run`
} else {
  // this file is being imported by another file
}
```

***

See [Docs > API > import.meta](https://bun.com/docs/api/import-meta) for complete documentation.
