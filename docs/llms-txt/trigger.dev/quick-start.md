# Source: https://trigger.dev/docs/quick-start.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quick start

> How to get started in 3 minutes using the CLI and SDK.

<Steps titleSize="h3">
  <Step title="Create a Trigger.dev account">
    Sign up at [Trigger.dev Cloud](https://cloud.trigger.dev) (or [self-host](/open-source-self-hosting)). The onboarding flow will guide you through creating your first organization and project.
  </Step>

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

        <img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/test-dashboard.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=92c810690f961d0033dd94d758c6bbfb" alt="Test page" width="2254" height="1367" data-path="images/test-dashboard.png" />
  </Step>

  <Step title="View your run">
    Congratulations, you should see the run page which will live reload showing you the current state of the run.

        <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/run-page.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=4b0bb5f9b181499cf324cdb8d5d673a8" alt="Run page" width="2978" height="2110" data-path="images/run-page.png" />

    If you go back to your terminal you'll see that the dev command also shows the task status and links to the run log.

        <img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/terminal-completed-run.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=a9284c5228343b72d798c6e36f5acb24" alt="Terminal showing completed run" width="955" height="197" data-path="images/terminal-completed-run.png" />
  </Step>
</Steps>

## Next steps

<CardGroup cols={2}>
  <Card title="Building with AI" icon="brain" href="/building-with-ai">
    Learn how to build Trigger.dev projects using AI coding assistants
  </Card>

  <Card title="How to trigger your tasks" icon="bolt" href="/triggering">
    Learn how to trigger tasks from your code.
  </Card>

  <Card title="Writing tasks" icon="wand-magic-sparkles" href="/tasks/overview">
    Tasks are the core of Trigger.dev. Learn what they are and how to write them.
  </Card>

  <Card title="Guides and example projects" icon="books" href="/guides/introduction">
    Guides and examples for triggering tasks from your code.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).