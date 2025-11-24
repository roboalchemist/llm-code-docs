# Source: https://www.daytona.io/docs/en/preview-and-authentication.md

The Daytona SDK provides a method to generate preview links for Sandboxes. A preview link's schema consists of the port and Sandbox ID (e.g.
`https://3000-sandboxid.proxy.daytona.works`).

Any process listening for HTTP traffic on ports 3000–9999 can be previewed.

## Fetching a Preview Link

To fetch the preview link and the authorization token for a specific port, you can simply use the SDK method:

```python

preview_info = sandbox.get_preview_link(3000)

print(f"Preview link url: {preview_info.url}")
print(f"Preview link token: {preview_info.token}")

```

```typescript

const previewInfo = await sandbox.getPreviewUrl(3000);

console.log(`Preview link url: ${previewInfo.url}`);
console.log(`Preview link token: ${previewInfo.token}`);

```


:::tip
If you want to serve the previews under your own domain instead of using Daytona's URLs, check out the [Custom Domain/Authentication](https://www.daytona.io/docs/en/custom-domain-authentication.md) section.
:::

See: [get_preview_link (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxget_preview_link), [getPreviewLink (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/sandbox.md#getpreviewlink)

## Authentication

If the Sandbox has its `public` property set to `true`, these links will be publicly accessible, otherwise the preview link will be available only to the Sandbox Organization users.

For programmatic access, use the authorization token to access the preview URL:

```bash
curl -H "x-daytona-preview-token: vg5c0ylmcimr8b_v1ne0u6mdnvit6gc0" \
https://3000-sandbox-123456.proxy.daytona.work
```

## Warning Page

When opening the preview link in a browser, a warning page will be shown for the first time.
This warning serves as a security measure to inform users about the potential risks of visiting the preview URL.

The warning page will only be shown when loading the preview link in a browser.

To avoid this warning you can do one of the following:

- Send the `X-Daytona-Skip-Preview-Warning: true` header
- Upgrade to [Tier 3](https://www.daytona.io/docs/en/limits.md)
- Deploy your own [custom preview proxy](https://www.daytona.io/docs/en/custom-domain-authentication.md)