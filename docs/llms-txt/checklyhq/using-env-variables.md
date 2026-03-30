# Source: https://checklyhq.com/docs/detect/testing/using-env-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using env variables

Use environment variables to test different environments:

```ts Homepage.test.ts theme={null}
// In your test file
test('Homepage loads', async ({ page }) => {
  const baseUrl = process.env.ENVIRONMENT_URL || 'https://example.com'
  await page.goto(baseUrl)
  // ... rest of your test
})
```

Run with environment variables:

```bash Terminal theme={null}
npx checkly test --env ENVIRONMENT_URL="https://staging.example.com"
```


Built with [Mintlify](https://mintlify.com).