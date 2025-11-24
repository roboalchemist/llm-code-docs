# Source: https://bun.com/docs/guides/util/gzip.md

# Compress and decompress data with gzip

Use `Bun.gzipSync()` to compress a `Uint8Array` with gzip.

```ts  theme={"theme":{"light":"github-light","dark":"dracula"}}
const data = Buffer.from("Hello, world!");
const compressed = Bun.gzipSync(data);
// => Uint8Array

const decompressed = Bun.gunzipSync(compressed);
// => Uint8Array
```

***

See [Docs > API > Utils](https://bun.com/docs/api/utils) for more useful utilities.
