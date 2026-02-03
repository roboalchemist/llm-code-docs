# Source: https://rspack.dev/guide/tech/json.md

# JSON

Rspack has built-in support for [JSON](https://en.wikipedia.org/wiki/JSON), and you can import JSON files directly.

## Default import

```json title="example.json"
{
  "foo": "bar"
}
```

```ts title="index.js"
import json from './example.json';
console.log(json.foo); // "bar"
```

## Named import

In non-`.mjs` non-strict ESM files, you can directly import properties from JSON.

```json title="example.json"
{
  "foo": "bar"
}
```

```ts title="index.js"
import { foo } from './example.json';
console.log(foo); // "bar"
```

## Import attributes

[Added in v1.0.0-beta.1](https://github.com/web-infra-dev/rspack/releases/tag/v1.0.0-beta.1)
Rspack supports [import attributes](https://github.com/tc39/proposal-import-attributes), and you can use import attributes to import JSON:

```ts title="index.js"
import json from './example.json' with { type: 'json' };
import('./example.json', { with: { type: 'json' } });
```
