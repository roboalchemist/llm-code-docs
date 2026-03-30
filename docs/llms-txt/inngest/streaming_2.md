# Source: https://www.inngest.com/docs-markdown/reference/typescript/v4/serve/streaming

# Streaming

In select environments, the SDK allows streaming responses back to Inngest, hugely increasing maximum timeouts on many serverless platforms up to 15 minutes.

While we add wider support for streaming to other platforms, we currently support the following:

- [Cloudflare Workers](/docs-markdown/learn/serving-inngest-functions#framework-cloudflare-workers)
- [Express](/docs-markdown/learn/serving-inngest-functions#framework-express)
- [Next.js on Vercel Fluid Compute or Edge Functions](/docs-markdown/learn/serving-inngest-functions#framework-next-js)
- [Remix on Vercel Edge Functions](/docs-markdown/learn/serving-inngest-functions#framework-remix)

## Enabling streaming

Select your platform above and follow the relevant "Streaming" section to enable streaming for your application.

Every Inngest serve handler provides a `streaming` option, for example:

```ts
serve({
  client: inngest,
  functions: [...fns],
  streaming: true,
});
```

This can be one of the following values:

- `false` - Streaming will never be used. This is the default.
- `true` - Streaming will be used. If the serve handler does not support streaming, an error will be thrown.

> **Callout:** In v3, streaming accepted "allow" and "force" string values. In v4, these were simplified to true | false. See the migration guide for details.