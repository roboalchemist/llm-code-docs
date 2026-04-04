# Source: https://bun.com/docs/guides/websocket/simple.md

# Source: https://bun.com/docs/guides/http/simple.md

> ## Documentation Index
> Fetch the complete documentation index at: https://bun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Write a simple HTTP server

This starts an HTTP server listening on port `3000`. It responds to all requests with a `Response` with status `200` and body `"Welcome to Bun!"`.

See [`Bun.serve`](/runtime/http/server) for details.

```ts server.ts icon="https://mintcdn.com/bun-1dd33a4e/Hq64iapoQXHbYMEN/icons/typescript.svg?fit=max&auto=format&n=Hq64iapoQXHbYMEN&q=85&s=c6cceedec8f82d2cc803d7c6ec82b240" theme={"theme":{"light":"github-light","dark":"dracula"}}
const server = Bun.serve({
  port: 3000,
  fetch(request) {
    return new Response("Welcome to Bun!");
  },
});

console.log(`Listening on ${server.url}`);
```
