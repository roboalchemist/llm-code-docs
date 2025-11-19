# Source: https://bun.com/docs/guides/http/proxy.md

# Proxy HTTP requests using fetch()

In Bun, `fetch` supports sending requests through an HTTP or HTTPS proxy. This is useful on corporate networks or when you need to ensure a request is sent through a specific IP address.

```ts proxy.ts icon="https://mintcdn.com/bun-1dd33a4e/Hq64iapoQXHbYMEN/icons/typescript.svg?fit=max&auto=format&n=Hq64iapoQXHbYMEN&q=85&s=c6cceedec8f82d2cc803d7c6ec82b240" theme={"theme":{"light":"github-light","dark":"dracula"}}
await fetch("https://example.com", {
  // The URL of the proxy server
  proxy: "https://usertitle:password@proxy.example.com:8080",
});
```

***

The `proxy` option is a URL string that specifies the proxy server. It can include the username and password if the proxy requires authentication. It can be `http://` or `https://`.

***

You can also set the `$HTTP_PROXY` or `$HTTPS_PROXY` environment variable to the proxy URL. This is useful when you want to use the same proxy for all requests.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
HTTPS_PROXY=https://usertitle:password@proxy.example.com:8080 bun run index.ts
```
