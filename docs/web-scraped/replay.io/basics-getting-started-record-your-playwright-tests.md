# Source: https://docs.replay.io/basics/getting-started/record-your-playwright-tests

Title: Replay - Browser DevTools from the future.

URL Source: https://docs.replay.io/basics/getting-started/record-your-playwright-tests

Markdown Content:
1

Create a new Test Suite team
----------------------------

Start by visiting our [new test suite form](https://app.replay.io/team/new/tests). It will create an API key and guide you through each step.

![Image 1: New playwright team](https://docs.replay.io/_next/image?url=%2Fimages%2Fnew-team-tests.png&w=1920&q=75)

2

Install the Replay Playwright plugin
------------------------------------

Terminal

```
npm install --save-dev @replayio/playwright
```

3

Install the Replay browser
--------------------------

Terminal

```
npx replayio install
```

4

Save your API key
-----------------

To use your API key, you can either use [dotenv package](https://www.npmjs.com/package/dotenv) and save it to a `.env` file or add the API key to your environment directly.

.env

```
REPLAY_API_KEY=<your_api_key>
```

5

Update playwright.config.js
---------------------------

playwright.config.ts

```
1import { PlaywrightTestConfig, devices } from "@playwright/test";
 2import {
 3  devices as replayDevices,
 4  replayReporter
 5} from "@replayio/playwright";
 6import "dotenv/config";
 7
 8const config: PlaywrightTestConfig = {
 9  reporter: [
10    replayReporter({
11      apiKey: process.env.REPLAY_API_KEY,
12      upload: true,
13    }),
14    ["line"],
15  ],
16  projects: [
17    {
18      name: "replay-chromium",
19      use: { ...replayDevices["Replay Chromium"] },
20    },
21  ],
22};
23export default config;
```

6

Record your test
----------------

With everything set up, you can now run `playwright test` to record and upload your first Playwright replays.

Terminal

```
npx playwright test --project replay-chromium
```

Terminal

```
➜ npx playwright test
Running 1 test using 1 worker
[1/1] things-app.spec.ts:14:7 › Todos › should allow me to add todo items
[replay.io]: 🕑 Completing some outstanding work ...
[replay.io]:
[replay.io]: 🚀 Successfully uploaded 1 recordings:
[replay.io]:
[replay.io]:    ✅ should allow me to add todo items
  1 passed (2.1s)
```

> [Check out this replay](https://replay.help/playwright-flake-debug) for a detailed walkthrough on debugging a flaky Playwright test.

Record your test suite in CI
----------------------------

Now that you're ready to inspect your local tests, the next step is to record your tests in CI. Learn how to set up Replay with your Playwright tests on [GitHub Actions](https://docs.replay.io/reference/test-runners/playwright/github-actions) and [other CI providers](https://docs.replay.io/reference/test-runners/playwright/other-ci-providers).

Read more

Learn how to record your tests, manage your test suite and debug flaky tests using Replay DevTools
