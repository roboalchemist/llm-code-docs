# Source: https://checklyhq.com/docs/detect/synthetic-monitoring/browser-checks/mac-structure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Mac structure

Monitoring as Code works by connecting Playwrighttest files with Checkly constructs to handle the end-to-endconfiguration of your Browser Check.

## Browser Check Construct

The Browser Check construct is used to configure your monitoring settings, such as frequency, locations, and tags. Learn more about the [Browser Check Construct](/constructs/browser-check)

```ts browser-check.ts theme={null}
import { BrowserCheck, Frequency } from 'checkly/constructs'
import * as path from 'path'

new BrowserCheck('browser-check-1', {
  name: 'Browser check #1',
  frequency: Frequency.EVERY_10M,
  locations: ['us-east-1', 'eu-west-1'],
  code: {
    entrypoint: path.join(__dirname, 'login.spec.js')
  }
})
```

## Test Script Structure

Checkly uses Playwright to power Browser Checks. [Playwright](https://playwright.dev/docs/intro) is a robust, open-source framework for browser automation and end-to-end web application testing. It enables you to write atomic, reliable tests and easily control interactions within a web page. Browser checks execute automated test scripts in real browsers.

```typescript login.spec.ts theme={null}
// Use environment-specific URLs and credentials
const baseURL = process.env.BASE_URL || 'https://app.example.com'
const testUser = process.env.TEST_USER_EMAIL
const testPassword = process.env.TEST_USER_PASSWORD

test('Environment-aware test', async ({ page }) => {
  await page.goto(`${baseURL}/login`)
  await page.fill('[name="email"]', testUser)
  await page.fill('[name="password"]', testPassword)
  // ... rest of test
})
```

## Environment variables

[Check, group and global variables](/platform/variables) are accessible in your code using the standard Node.js `process.env.MY_VAR` notation. For example, the code snippet below show how you can log into GitHub.

<CodeGroup dropdown>
  ```ts variables.spec.ts theme={null}
  import { test } from '@playwright/test'

  test('GitHub login', async ({ page }) => {
    await page.goto('https://github.com/login')
    await page.getByLabel('Username or email address').type(process.env.GITHUB_USER)
    await page.getByLabel('Password').type(process.env.GITHUB_PWD)
    await page.getByRole('button', { name: 'Sign in' }).click()
  })
  ```

  ```js variables.spec.js theme={null}
  const { test } = require('@playwright/test')

  test('GitHub login', async ({ page }) => {
    await page.goto('https://github.com/login')
    await page.getByLabel('Username or email address').type(process.env.GITHUB_USER)
    await page.getByLabel('Password').type(process.env.GITHUB_PWD)
    await page.getByRole('button', { name: 'Sign in' }).click()
  })
  ```
</CodeGroup>

### Built-in runtime variables

Our [check runtimes](/platform/runtimes/overview/) also expose a set of environment variables (e.g. `process.env.CHECK_NAME`)
to figure out what check, check type etc. you are running.

| Variable          | Description                                 | Availability                                                |
| ----------------- | ------------------------------------------- | ----------------------------------------------------------- |
| `ACCOUNT_ID`      | The ID of the account the check belongs to. |                                                             |
| `CHECK_ID`        | The UUID of the check being executed.       | Only available after saving the check.                      |
| `CHECK_NAME`      | The name of the check being executed.       |                                                             |
| `CHECK_RESULT_ID` | The UUID where the result will be saved.    | Only available on scheduled runs.                           |
| `CHECK_RUN_ID`    | The UUID of the check run execution.        | Only available on scheduled runs.                           |
| `CHECK_TYPE`      | The type of the check, e.g. `BROWSER`.      |                                                             |
| `PUBLIC_IP_V4`    | The IPv4 of the check run execution.        |                                                             |
| `PUBLIC_IP_V6`    | The IPv6 of the check run execution.        |                                                             |
| `REGION`          | The current region, e.g. `us-west-1`.       |                                                             |
| `RUNTIME_VERSION` | The version of the runtime, e.g, `2023.09`. | Only in Browser, Multistep, and API setup/teardown scripts. |


Built with [Mintlify](https://mintlify.com).