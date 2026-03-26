# Source: https://momentic.ai/docs/quickstart/cli.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# CLI

> This quickstart guide will walk you building your first test locally and integrating into CI/CD

<Info>
  **Prerequisite**: Please install [Node.js](https://nodejs.org/en) (version
  20.19.0 or higher) before proceeding.
</Info>

Before you begin, you must already have a `package.json` file. If you don’t,
make sure to run `npm init` or `yarn init` to create the file beforehand.

## Get your API key

To get started, log in to
[Momentic Cloud](https://app.momentic.ai/settings/api-keys) and generate an API
key.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/create-api-key.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=54eb9f3c01e00a3ae7d71996760dcd39" width="3616" height="2434" data-path="images/create-api-key.png" />
</Frame>

You can export the API key in your shell configuration file (usually `.bashrc`
or `.zshrc`) like so:

```bash  theme={null}
export MOMENTIC_API_KEY=your-api-key
```

## Install the Momentic CLI

Install the CLI, [momentic](https://www.npmjs.com/package/momentic), by running
the following command in your terminal:

<CodeGroup>
  ```bash npm theme={null}
  npm install momentic --save-dev
  ```

  ```bash yarn theme={null}
  yarn add momentic --dev --ignore-workspace-root-check
  ```

  ```bash pnpm theme={null}
  pnpm add momentic --save-dev --ignore-workspace-root-check
  ```
</CodeGroup>

## Install browsers

Momentic relies on [headless browsers](/browsers) that must be installed. To
install all available browsers:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-browsers --all
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-browsers --all
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-browsers --all
  ```
</CodeGroup>

## Initialize a new project

To create a new Momentic project, run the following command in your terminal:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic init
  ```

  ```bash yarn theme={null}
  yarn dlx momentic init
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic init
  ```
</CodeGroup>

## Start the Momentic Local App

Start the Local App by running the following command in your terminal:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic app
  ```

  ```bash yarn theme={null}
  yarn dlx momentic app
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic app
  ```
</CodeGroup>

It will open a new browser window with the Momentic Local App, where you can
manage your tests, view results, and more.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/local-app.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=3c12ef7971084f830999cd89fc2d7ce5" width="3620" height="2518" data-path="images/local-app.png" />
</Frame>

## Create a test

Click on the **Create test** button in the top-right corner.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/local-create-test.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=d2fc426d18020a34d1ccf91b7e5ce429" width="4016" height="2376" data-path="images/local-create-test.png" />
</Frame>

Enter these details:

* **Name**: `example-test`
* **Base URL**: `https://practicetestautomation.com/practice-test-login/` (a
  demo site for testing)

This will open the Momentic Editor, where you can add instructions in natural
language. Click **Run from start** to execute the test live.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/example-test-editor.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=a586e8d81276469c7d97121e17b3571f" width="3614" height="2430" data-path="images/example-test-editor.png" />
</Frame>

This will create a new file in your project directory called
`example-test.test.yaml`. Changes are saved automatically, so you don't need to
worry about losing your work.

## Run the test

You can run the test you just created by running the following command in your
terminal:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run example-test
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run example-test
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run example-test
  ```
</CodeGroup>

## Next steps

Congratulations! You have successfully built and ran your first test with
Momentic. Here are suggested next steps:

<Card title="Set up GitHub Actions" icon="github" horizontal href="/ci/github-actions">
  Integrate Momentic tests into your GitHub Actions workflows
</Card>

<Card title="Variables" icon="square-root-variable" horizontal href="/variables">
  Learn how to use variables to make your tests more dynamic and reusable
</Card>


Built with [Mintlify](https://mintlify.com).