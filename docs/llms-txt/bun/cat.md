# Source: https://bun.com/docs/guides/write-file/cat.md

# Write a file to stdout

Bun exposes `stdout` as a `BunFile` with the `Bun.stdout` property. This can be used as a destination for [`Bun.write()`](https://bun.com/docs/api/file-io#writing-files-bun-write).

This code writes a file to `stdout` similar to the `cat` command in Unix.

```ts cat.ts icon="https://mintcdn.com/bun-1dd33a4e/Hq64iapoQXHbYMEN/icons/typescript.svg?fit=max&auto=format&n=Hq64iapoQXHbYMEN&q=85&s=c6cceedec8f82d2cc803d7c6ec82b240" theme={"theme":{"light":"github-light","dark":"dracula"}}
const path = "/path/to/file.txt";
const file = Bun.file(path);
await Bun.write(Bun.stdout, file);
```

***

See [Docs > API > File I/O](https://bun.com/docs/api/file-io#writing-files-bun-write) for complete documentation of `Bun.write()`.
