# Source: https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/index.md

---

title: Non-JavaScript modules · Cloudflare Workers docs
description: Additional module types that can be imported in your Worker
lastUpdated: 2026-01-20T15:51:22.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/
  md: https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/index.md
---

In addition to TypeScript and JavaScript, the following module types are automatically configured to be importable in your Worker code.

| Module extension | Imported type |
| - | - |
| `.txt` | `string` |
| `.html` | `string` |
| `.sql` | `string` |
| `.bin` | `ArrayBuffer` |
| `.wasm`, `.wasm?module` | `WebAssembly.Module` |

For example, with the following import, `text` will be a string containing the contents of `example.txt`:

```js
import text from "./example.txt";
```

This is also the basis for importing Wasm, as in the following example:

```ts
import wasm from "./example.wasm";


// Instantiate Wasm modules in the module scope
const instance = await WebAssembly.instantiate(wasm);


export default {
  fetch() {
    const result = instance.exports.exported_func();


    return new Response(result);
  },
};
```

Note

Cloudflare Workers does not support `WebAssembly.instantiateStreaming()`.
