# Source: https://docs.replay.io/basics/getting-started/record-your-cypress-tests

Title: Replay - Browser DevTools from the future.

URL Source: https://docs.replay.io/basics/getting-started/record-your-cypress-tests

Markdown Content:
1

Create a new Test Suite team
----------------------------

Start by visiting our [new test suite form](https://app.replay.io/team/new/tests). It will create an API key and guide you through each step.

![Image 1: Create a cypress team](https://docs.replay.io/_next/image?url=%2Fimages%2Fcypress-team.png&w=1920&q=75)

2

Install the Replay Cypress plugin
---------------------------------

Terminal

```
npm install --save-dev @replayio/cypress
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

Add the plugin to your project
------------------------------

Installing Replay Cypress is as simple as adding the plugin to your [cypress.config.js](https://docs.cypress.io/guides/references/configuration) and [support](https://docs.cypress.io/guides/core-concepts/writing-and-organizing-tests#Support-file) files. Once installed, the plugin will let you record your tests with the [Replay Chrome browser](https://docs.replay.io/reference/replay-runtimes/replay-chrome) and add the Cypress timeline to Replay DevTools.

cypress/support/e2e.js

```
require('@replayio/cypress/support')
```

cypress.config.js

```
1const { defineConfig } = require('cypress')
 2const { plugin: replayPlugin, wrapOn } = require('@replayio/cypress')
 3require('dotenv').config()
 4
 5module.exports = defineConfig({
 6  e2e: {
 7    setupNodeEvents(cyOn, config) {
 8      const on = wrapOn(cyOn)
 9      replayPlugin(on, config, {
10        upload: true, // automatically upload your replays do DevTools
11        apiKey: process.env.REPLAY_API_KEY,
12      })
13      return config
14    },
15  },
16})
```

6

Record your test suite in CI
----------------------------

Now that you're ready to inspect your local tests, the next step is to record your tests in CI. Learn how to set up Replay with your Cypress tests on [GitHub Actions](https://docs.replay.io/reference/test-runners/cypress-io/github-actions) and [other CI providers](https://docs.replay.io/reference/test-runners/cypress-io/other-ci-providers).

Read more

Learn how to record your tests, manage your test suite and debug flaky tests using Replay DevTools
