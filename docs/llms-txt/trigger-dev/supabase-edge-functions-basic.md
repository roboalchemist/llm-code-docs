# Source: https://trigger.dev/docs/guides/frameworks/supabase-edge-functions-basic.md

# Triggering tasks from Supabase edge functions

> This guide will show you how to trigger a task from a Supabase edge function, and then view the run in our dashboard.

## Overview

Supabase edge functions allow you to trigger tasks either when an event is sent from a third party (e.g. when a new Stripe payment is processed, when a new user signs up to a service, etc), or when there are any changes or updates to your Supabase database.

This guide shows you how to set up and deploy a simple Supabase edge function example that triggers a task when an edge function URL is accessed.

## Prerequisites

* Ensure you have the [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started) installed
* Since Supabase CLI version 1.123.4, you must have [Docker Desktop installed](https://supabase.com/docs/guides/functions/deploy#deploy-your-edge-functions) to deploy Edge Functions
* Ensure TypeScript is installed
* [Create a Trigger.dev account](https://cloud.trigger.dev)
* Create a new Trigger.dev project

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/supabase-edge-functions">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## Initial setup

<Steps>
  <Step title="Optional step 1: create a new Supabase project">
    <Info> If you already have a Supabase project on your local machine you can skip this step.</Info>

    You can create a new project by running the following command in your terminal using the Supabase CLI:

    ```bash  theme={null}
    supabase init
    ```

    <Note>
      If you are using VS Code, ensure to answer 'y' when asked to generate VS Code settings for Deno,
      and install any recommended extensions.
    </Note>
  </Step>

  <Step title="Optional step 2: create a package.json file">
    If your project does not already have `package.json` file (e.g. if you are using Deno), create it manually in your project's root folder.

    <Info> If your project has a `package.json` file you can skip this step.</Info>

    This is required for the Trigger.dev SDK to work correctly.

    ```ts package.json theme={null}
    {
      "devDependencies": {
        "typescript": "^5.6.2"
      }
    }
    ```

    <Note> Update your Typescript version to the latest version available. </Note>
  </Step>

  <Step title="Run the CLI `init` command">
    The easiest way to get started is to use the CLI. It will add Trigger.dev to your existing project, create a `/trigger` folder and give you an example task.

    Run this command in the root of your project to get started:

    <CodeGroup>
      ```bash npm theme={null}
      npx trigger.dev@latest init
      ```

      ```bash pnpm theme={null}
      pnpm dlx trigger.dev@latest init
      ```

      ```bash yarn theme={null}
      yarn dlx trigger.dev@latest init
      ```
    </CodeGroup>

    It will do a few things:

    1. Log you into the CLI if you're not already logged in.
    2. Create a `trigger.config.ts` file in the root of your project.
    3. Ask where you'd like to create the `/trigger` directory.
    4. Create the `/trigger` directory with an example task, `/trigger/example.[ts/js]`.

    Install the "Hello World" example task when prompted. We'll use this task to test the setup.
  </Step>

  <Step title="Run the CLI `dev` command">
    The CLI `dev` command runs a server for your tasks. It watches for changes in your `/trigger` directory and communicates with the Trigger.dev platform to register your tasks, perform runs, and send data back and forth.

    It can also update your `@trigger.dev/*` packages to prevent version mismatches and failed deploys. You will always be prompted first.

    <CodeGroup>
      ```bash npm theme={null}
      npx trigger.dev@latest dev
      ```

      ```bash pnpm theme={null}
      pnpm dlx trigger.dev@latest dev
      ```

      ```bash yarn theme={null}
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

## Create a new Supabase edge function and deploy it

<Steps>
  <Step title="Create a new Supabase edge function">
    We'll call this example `edge-function-trigger`.

    In your project, run the following command in the terminal using the Supabase CLI:

    ```bash  theme={null}
    supabase functions new edge-function-trigger
    ```
  </Step>

  <Step title="Update the edge function code">
    Replace the placeholder code in your `edge-function-trigger/index.ts` file with the following:

    ```ts functions/edge-function-trigger/index.ts theme={null}
    // Setup type definitions for built-in Supabase Runtime APIs
    import "jsr:@supabase/functions-js/edge-runtime.d.ts";
    // Import the Trigger.dev SDK - replace "<your-sdk-version>" with the version of the SDK you are using, e.g. "3.0.0". You can find this in your package.json file.
    import { tasks } from "npm:@trigger.dev/sdk@3.0.0";
    // Import your task type from your /trigger folder
    import type { helloWorldTask } from "../../../src/trigger/example.ts";
    //     👆 **type-only** import

    Deno.serve(async () => {
      await tasks.trigger<typeof helloWorldTask>(
        // Your task id
        "hello-world",
        // Your task payload
        "Hello from a Supabase Edge Function!"
      );
      return new Response("OK");
    });
    ```

    <Note>You can only import the `type` from the task.</Note>

    <Note>
      Tasks in the `trigger` folder use Node, so they must stay in there or they will not run,
      especially if you are using a different runtime like Deno. Also do not add "`npm:`" to imports
      inside your task files, for the same reason.
    </Note>
  </Step>

  <Step title="Deploy your edge function using the Supabase CLI">
    You can now deploy your edge function with the following command in your terminal:

    ```bash  theme={null}
    supabase functions deploy edge-function-trigger --no-verify-jwt
    ```

    <Warning>
      `--no-verify-jwt` removes the JSON Web Tokens requirement from the authorization header. By
      default this should be on, but it is not strictly required for this hello world example.
    </Warning>

    <Note>
      To learn more about how to properly configure Supabase auth for Trigger.dev tasks, please refer to
      our [Supabase Authentication guide](/guides/frameworks/supabase-authentication). It demonstrates
      how to use JWT authentication for user-specific operations or your service role key for
      admin-level access.
    </Note>

    Follow the CLI instructions and once complete you should now see your new edge function deployment in your Supabase edge functions dashboard.

    There will be a link to the dashboard in your terminal output, or you can find it at this URL:

    `https://supabase.com/dashboard/project/<your-project-id>/functions`

    <Note>Replace `your-project-id` with your actual project ID.</Note>
  </Step>
</Steps>

## Set your Trigger.dev prod secret key in the Supabase dashboard

To trigger a task from your edge function, you need to set your Trigger.dev secret key in the Supabase dashboard.

To do this, first go to your Trigger.dev [project dashboard](https://cloud.trigger.dev) and copy the `prod` secret key from the API keys page.

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=0733b8d37ded28dfc8eb55cfbbf8d1de" alt="How to find your prod secret key" data-og-width="1624" width="1624" data-og-height="924" height="924" data-path="images/api-key-prod.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=b6322b1c7486febaa68d044cdcee166a 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=5a9c86949e65af4e51e105f3e3a6bcc9 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=0b8cd9edac7b0f133e8790c302a64269 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=5f86de1e7348b781d66bd13737b0dd37 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=5f2fc6b58d2ed8d6d6a1653bb840bd67 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-key-prod.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=aed3fb7368091c0ee12cac472e02fc07 2500w" />

Then, in [Supabase](https://supabase.com/dashboard/projects), select your project, navigate to 'Project settings' <Icon icon="circle-1" iconType="solid" size={20} color="A8FF53" />, click 'Edge functions' <Icon icon="circle-2" iconType="solid" size={20} color="A8FF53" /> in the configurations menu, and then click the 'Add new secret' <Icon icon="circle-3" iconType="solid" size={20} color="A8FF53" /> button.

Add `TRIGGER_SECRET_KEY` <Icon icon="circle-4" iconType="solid" size={20} color="A8FF53" /> with the pasted value of your Trigger.dev `prod` secret key.

<img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=70842bf838bc1ea9e1f195c9926bb746" alt="Add secret key in Supabase" data-og-width="1624" width="1624" data-og-height="924" height="924" data-path="images/supabase-keys-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=1b893de3a516863384e77179c709a631 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=ba9cab56f377dc72898cd388a3280901 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=37d7d313be698f7015fe490fc01cad30 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=73a7d40712c7a889bbe6af3803b86df7 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=0c62e86405a9e23947ed073be6c5fca4 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-keys-1.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=30c4316db62c7820dd5c513c922b2976 2500w" />

## Deploy your task and trigger it from your edge function

<Steps>
  <Step title="Deploy your 'Hello World' task">
    Next, deploy your `hello-world` task to [Trigger.dev cloud](https://cloud.trigger.dev).

    <CodeGroup>
      ```bash npm theme={null}
      npx trigger.dev@latest deploy
      ```

      ```bash pnpm theme={null}
      pnpm dlx trigger.dev@latest deploy
      ```

      ```bash yarn theme={null}
      yarn dlx trigger.dev@latest deploy
      ```
    </CodeGroup>
  </Step>

  <Step title="Trigger a prod run from your deployed edge function">
    To do this all you need to do is simply open the `edge-function-trigger` URL.

    `https://supabase.com/dashboard/project/<your-project-id>/functions`

    <Note>Replace `your-project-id` with your actual project ID.</Note>

    In your Supabase project, go to your Edge function dashboard, find `edge-function-trigger`, copy the URL, and paste it into a new window in your browser.

    Once loaded you should see ‘OK’ on the new screen.

        <img src="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-function-url.png?fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=39bf78f3b0d9fab4d92cc1cda60fbcec" alt="Edge function URL" data-og-width="1624" width="1624" data-og-height="924" height="924" data-path="images/supabase-function-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-function-url.png?w=280&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=ec78f91a1c5569170094e79228eb7e13 280w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-function-url.png?w=560&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=bb2c38ef3741c7f9efbf9aeeed2d9212 560w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-function-url.png?w=840&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=91eeaf194a648ab24e3d372722f0ba3d 840w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-function-url.png?w=1100&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=2ad7b3e2ffb9a70bb87dff0b0c41c94c 1100w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-function-url.png?w=1650&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=d25ca24ca979a211d53163b0a8daf9aa 1650w, https://mintcdn.com/trigger/0bD0UfsjaINxS6Tw/images/supabase-function-url.png?w=2500&fit=max&auto=format&n=0bD0UfsjaINxS6Tw&q=85&s=f29534a7737c8c81db3da9c382dc9e97 2500w" />

    The task will be triggered when your edge function URL is accessed.

    Check your [cloud.trigger.dev](http://cloud.trigger.dev) dashboard and you should see a succesful `hello-world` task.

    **Congratulations, you have run a simple Hello World task from a Supabase edge function!**
  </Step>
</Steps>

## Learn more about Supabase and Trigger.dev

### Full walkthrough guides from development to deployment

<CardGroup cols={1}>
  <Card title="Edge function hello world guide" icon="book" href="/guides/frameworks/supabase-edge-functions-basic">
    Learn how to trigger a task from a Supabase edge function when a URL is visited.
  </Card>

  <Card title="Database webhooks guide" icon="book" href="/guides/frameworks/supabase-edge-functions-database-webhooks">
    Learn how to trigger a task from a Supabase edge function when an event occurs in your database.
  </Card>

  <Card title="Supabase authentication guide" icon="book" href="/guides/frameworks/supabase-authentication">
    Learn how to authenticate Supabase tasks using JWTs for Row Level Security (RLS) or service role
    keys for admin access.
  </Card>
</CardGroup>

### Task examples with code you can copy and paste

<CardGroup cols={2}>
  <Card title="Supabase database operations" icon="bolt" href="/guides/examples/supabase-database-operations">
    Run basic CRUD operations on a table in a Supabase database using Trigger.dev.
  </Card>

  <Card title="Supabase Storage upload" icon="bolt" href="/guides/examples/supabase-storage-upload">
    Download a video from a URL and upload it to Supabase Storage using S3.
  </Card>
</CardGroup>
