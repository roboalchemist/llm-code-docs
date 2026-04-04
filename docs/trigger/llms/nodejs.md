# Source: https://trigger.dev/docs/guides/frameworks/nodejs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Node.js setup guide

> This guide will show you how to setup Trigger.dev in your existing Node.js project, test an example task, and view the run.

export const framework_0 = "Node.js"

## Prerequisites

* Setup a project in {framework_0}
* Ensure TypeScript is installed
* [Create a Trigger.dev account](https://cloud.trigger.dev)
* Create a new Trigger.dev project

## Initial setup

<Steps>
  <Step title="Run the CLI `init` command">
    The easiest way to get started is to use the CLI. It will add Trigger.dev to your existing project, create a `/trigger` folder and give you an example task.

    Run this command in the root of your project to get started:

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest init
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest init
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest init
      ```
    </CodeGroup>

    It will do a few things:

    <Tip title="MCP Server">
      Our [Trigger.dev MCP server](/mcp-introduction) gives your AI assistant direct access to Trigger.dev tools; search docs, trigger tasks, deploy projects, and monitor runs. We recommend installing it for the best developer experience.
    </Tip>

    1. Ask if you want to install the [Trigger.dev MCP server](/mcp-introduction) for your AI assistant.
    2. Log you into the CLI if you're not already logged in.
    3. Ask you to select your project.
    4. Install the required SDK packages.
    5. Ask where you'd like to create the `/trigger` directory and create it with an example task.
    6. Create a `trigger.config.ts` file in the root of your project.

    Install the "Hello World" example task when prompted. We'll use this task to test the setup.
  </Step>

  <Step title="Run the CLI `dev` command">
    The CLI `dev` command runs a server for your tasks. It watches for changes in your `/trigger` directory and communicates with the Trigger.dev platform to register your tasks, perform runs, and send data back and forth.

    It can also update your `@trigger.dev/*` packages to prevent version mismatches and failed deploys. You will always be prompted first.

    <CodeGroup>
      ```bash npm theme={"theme":"css-variables"}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={"theme":"css-variables"}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={"theme":"css-variables"}
      yarn dlx trigger.dev@latest dev
      ```
    </CodeGroup>
  </Step>

  <Step title="Perform a test run using the dashboard">
    The CLI `dev` command spits out various useful URLs. Right now we want to visit the Test page.

    You should see our Example task in the list <Icon icon="circle-1" iconType="solid" size={20} color="F43F47" />, select it. Most tasks have a "payload" which you enter in the JSON editor <Icon icon="circle-2" iconType="solid" size={20} color="F43F47" />, but our example task doesn't need any input.

    You can configure options on the run <Icon icon="circle-3" iconType="solid" size={20} color="F43F47" />, view recent payloads <Icon icon="circle-4" iconType="solid" size={20} color="F43F47" />, and create run templates <Icon icon="circle-5" iconType="solid" size={20} color="F43F47" />.

    Press the "Run test" button <Icon icon="circle-6" iconType="solid" size={20} color="F43F47" />.

        <img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/test-dashboard.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=92c810690f961d0033dd94d758c6bbfb" alt="Test page" data-og-width="2254" width="2254" data-og-height="1367" height="1367" data-path="images/test-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/test-dashboard.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=970cc3e2d58a06fbf197fce5d6d0664b 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/test-dashboard.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=10d36ffd64e1f455f45a20d5e39f7bca 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/test-dashboard.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=62b4ec2301d11e645d3ebe45b2e3adc2 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/test-dashboard.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=2db30f2ebfe494c81f5965a014e4fc6e 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/test-dashboard.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=67b24a2d00bde47226c4db88c4f7ac51 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/test-dashboard.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=e44fddf5357449c582b92cd3d434e43d 2500w" />
  </Step>

  <Step title="View your run">
    Congratulations, you should see the run page which will live reload showing you the current state of the run.

        <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-page.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=4b0bb5f9b181499cf324cdb8d5d673a8" alt="Run page" data-og-width="2978" width="2978" data-og-height="2110" height="2110" data-path="images/run-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-page.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=d7f419295b621c779c6a9a10b9152958 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-page.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=c66995702aace3888813ee1a66d33f97 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-page.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=c6c36408dc85f156d15a333ddb849d26 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-page.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=2c1d7275465749eeae32196698f4a1b5 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-page.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=6965f3e2263296fb6529384021ce362a 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-page.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=7d890c5d199be7feaddc9162435bcc17 2500w" />

    If you go back to your terminal you'll see that the dev command also shows the task status and links to the run log.

        <img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/terminal-completed-run.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=a9284c5228343b72d798c6e36f5acb24" alt="Terminal showing completed run" data-og-width="955" width="955" data-og-height="197" height="197" data-path="images/terminal-completed-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/terminal-completed-run.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=62826752155594bd580ae51582870cce 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/terminal-completed-run.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=5270d0e823346fe8517fcc356cc5d20c 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/terminal-completed-run.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=8ae13acb781c5d08e2351af3c2cbb70a 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/terminal-completed-run.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=da9e9f485055786210b6d7ce3812b9cf 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/terminal-completed-run.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=dd59fd38559b7b7ca865a015d029e0de 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/terminal-completed-run.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=4de391f21eb74db6e3f7c174d86b4b71 2500w" />
  </Step>
</Steps>

## Useful next steps

<CardGroup cols={2}>
  <Card title="Tasks overview" icon="diagram-subtask" href="/tasks/overview">
    Learn what tasks are and their options
  </Card>

  <Card title="Writing tasks" icon="pen-nib" href="/writing-tasks-introduction">
    Learn how to write your own tasks
  </Card>

  <Card title="Deploy using the CLI" icon="terminal" href="/cli-deploy">
    Learn how to deploy your task manually using the CLI
  </Card>

  <Card title="Deploy using GitHub actions" icon="github" href="/github-actions">
    Learn how to deploy your task using GitHub actions
  </Card>
</CardGroup>
