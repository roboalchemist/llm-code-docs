# Source: https://docs.skypack.dev/skypack-cdn/code/deno.md

# Deno

## Hello, Deno!

Deno is a TypeScript runtime based heavily on ESM. It ships without a package manager, and instead relies on import URLs like Skypack for loading dependencies.&#x20;

Skypack is the best that you can import npm packages from in Deno.

```
deno
> const pkg = await import('https://cdn.skypack.dev/foo');
```

### A Note on Node.js Compatability

Skypack automatically converts legacy npm packages to modern ESM and polyfills some common Node.js built-in modules that they might depend on.

However, some modules (like the "fs" file system API) cannot be polyfilled and thus can't run on Deno (or anywhere outside of Node.js). Any packages on npm that rely on these dependencies won't run on Deno.

* fs
* crypto
* http
* https

### Automatic TypeScript Declarations

Skypack supports Deno's `X-TypeScript-Types` header to return TypeScript type declarations with loaded package. This gives you an extra level of safety with built-in Deno type warnings when your code breaks from the provided type declarations.

To enable TypeScript declarations, add the `?dts` query param to your lookup URL

```javascript
import React from 'https://cdn.skypack.dev/react?dts';
```
