# Source: https://bun.com/docs/guides/binary/blob-to-typedarray.md

# Convert a Blob to a Uint8Array

The [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) class provides a number of methods for consuming its contents in different formats. This snippets reads the contents to an `ArrayBuffer`, then creates a `Uint8Array` from the buffer.

```ts  theme={"theme":{"light":"github-light","dark":"dracula"}}
const blob = new Blob(["hello world"]);
const arr = new Uint8Array(await blob.arrayBuffer());
```

***

See [Docs > API > Binary Data](https://bun.com/docs/api/binary-data#conversion) for complete documentation on manipulating binary data with Bun.
