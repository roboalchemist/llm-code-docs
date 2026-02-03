# Source: https://docs.anchorbrowser.io/advanced/file-upload.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# File Upload

Anchor Browser allows you to upload files during your browser sessions, enabling you to interact with web applications/forms that require files as input.

The following examples demonstrate how to upload a file, either from your local development environment or one downloaded during the browser session.

## Using a local file

### Playwright example

<CodeGroup>
  ```tsx node.js theme={null}
  await page.goto('https://browser-tests-alpha.vercel.app/api/upload-test')

  const input = await page.$("#fileUpload")

  await input.setInputFiles('/tmp/my-files/google.png'); // Reference the local file path
  ```

  ```python python theme={null}
  page.goto('https://browser-tests-alpha.vercel.app/api/upload-test')

  input = page.locator("#fileUpload")

  input.set_input_files('/tmp/my-files/google.png') # Reference the local file path
  ```
</CodeGroup>
