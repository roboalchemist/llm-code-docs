# Source: https://docs.anchorbrowser.io/advanced/file-download.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# File Download

Anchor Browser supports two methods for downloading files during your browser sessions:

1. **Traditional Downloads**: Files are downloaded to the browser instance and then uploaded to S3 for retrieval

<Note>
  To download PDF files directly instead of viewing them in the browser, set `pdf_viewer` to `false` when creating your session.
</Note>

2. **P2P Downloads**: Files are captured directly in the browser using peer-to-peer technology, bypassing S3 storage

## Traditional File Downloads

The following examples demonstrate how to download a file using the traditional method and retrieve it from the browser session.

<Steps>
  <Step title="Create a browser session">
    Use the [create session](api-reference/browser-sessions/start-browser-session) API to create a new browser session.
    To enable automatic PDF downloads, include the following `browser` configuration:

    <CodeGroup>
      ```tsx node.js theme={null}
      browser: {
          pdf_viewer: {
              active: false
              }
          }
      ```

      ```python python theme={null}
      "browser": {
          "pdf_viewer": {
              "active": False
              }
          }
      ```
    </CodeGroup>
  </Step>

  <Step title="Browse and download a file">
    Use the following example to perform a file download

    <CodeGroup>
      ```tsx node.js theme={null}
      await page.goto("https://browser-tests-alpha.vercel.app/api/download-test");

      await Promise.all([page.waitForEvent("download"), page.locator("#download").click()]); // The download has completed
      ```

      ```python python theme={null}
      await page.goto("https://browser-tests-alpha.vercel.app/api/download-test")

      async with page.expect_download() as download_info:
          await page.locator("#download").click()

      download = await download_info.value
      ```
    </CodeGroup>
  </Step>

  <Step title="Fetch the file from the browser session">
    You can retrieve the downloaded file from the browser session using the [get session downloads](/api-reference/browser-sessions/list-session-downloads) API
  </Step>
</Steps>

## P2P Downloads

For enhanced performance and direct file capture without S3 storage, see our [P2P Download Guide](/advanced/p2p-downloads) which provides complete implementation examples and best practices.
