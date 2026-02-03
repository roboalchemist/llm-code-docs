# Source: https://trigger.dev/docs/deploy-environment-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Environment Variables

> Any environment variables used in your tasks need to be added so the deployed code will run successfully.

An environment variable in Node.js is accessed in your code using `process.env.MY_ENV_VAR`.

We deploy your tasks and scale them up and down when they are triggered. So any environment variables you use in your tasks need to accessible to us so your code will run successfully.

## In the dashboard

### Setting environment variables

<Steps>
  <Step title="Go to the Environment Variables page">
    In the sidebar select the "Environment Variables" page, then press the "New environment variable"
    button. <img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=af652254781808a35c2bcefd4b61b59f" alt="Environment variables page" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/environment-variables-page.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=fd6487833d9c659f8a514c7cc86cf84d 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=1758721fd84f5040b88997db401f7391 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=4416f51b1528ae14285a03b560f22389 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=12b90b89f7662aadaea07df17d9d3898 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=28e6921620cda10d335a095dbfa85806 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-page.jpg?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=4f6c67a030b20699bde25c22d68e57af 2500w" />
  </Step>

  <Step title="Add your environment variables">
    You can add values for your local dev environment, staging and prod. <img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-panel.jpg?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=79b5fd91e809cb0c6c9298410922df96" alt="Environment variables
    page" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/environment-variables-panel.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-panel.jpg?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=4c3f6181dea5542157cdbdebafb44989 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-panel.jpg?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=b0c302ef3d814a0c781b684e64d090f9 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-panel.jpg?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=a110ee9bb119eaaf7404097904a1f442 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-panel.jpg?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=6e774fb137908fbaaf28318d1bfa419d 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-panel.jpg?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=aa5d4bef7b66551887043c4420807bc4 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-panel.jpg?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=ed23a501677d11631bb832eb6f95ceae 2500w" />
  </Step>
</Steps>

<Note>
  Specifying Dev values is optional. They will be overriden by values in your .env file when running
  locally.
</Note>

### Editing environment variables

You can edit an environment variable's values. You cannot edit the key name, you must delete and create a new one.

<Steps>
  <Step title="Press the action button on a variable">
        <img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=05dd8ce39784065107f6eba1625866d0" alt="Environment variables page" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/environment-variables-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=fbed005dc7dcd0058a422838de4c0b9b 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=7e7f70a3116af7bba9837b4f87a85637 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=00ef502fa21ec6d5b0ad1268844fca1f 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=ead290a05e430dc69fa2cfdb2fa4217d 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=d769af16568cd23cbe1a7d6d5ed7c46e 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=ce9fba7375a89774d6eb6fd3800ba2b9 2500w" />
  </Step>

  <Step title="Press edit">
        <img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-edit-popover.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=e865f9406555034430788bbf98fbc785" alt="Environment variables page" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/environment-variables-edit-popover.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-edit-popover.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=f163d64590aa81c0cb6d74c3c7f94a2a 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-edit-popover.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=0a7d79db13a818c545764a658c81aba8 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-edit-popover.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=dbe05ce74ce05ae3100b8520f24a48e1 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-edit-popover.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=c0660d9ee4369bd8bdf4e7c5b9849258 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-edit-popover.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=b030c985d2733fc8b6ae7bdcb6577688 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-edit-popover.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=a56b25cb17ed5da98f82f0ede3e1b14f 2500w" />
  </Step>
</Steps>

### Deleting environment variables

<Warn>
  Environment variables are fetched and injected before a runs begins. So if you delete one you can
  cause runs to fail that are expecting variables to be set.
</Warn>

<Steps>
  <Step title="Press the action button on a variable">
        <img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=05dd8ce39784065107f6eba1625866d0" alt="Environment variables page" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/environment-variables-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=fbed005dc7dcd0058a422838de4c0b9b 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=7e7f70a3116af7bba9837b4f87a85637 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=00ef502fa21ec6d5b0ad1268844fca1f 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=ead290a05e430dc69fa2cfdb2fa4217d 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=d769af16568cd23cbe1a7d6d5ed7c46e 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-actions.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=ce9fba7375a89774d6eb6fd3800ba2b9 2500w" />
  </Step>

  <Step title="Press delete">
    This will immediately delete the variable. <img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-delete-popover.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=642350946bd75c3c508065a198aaa005" alt="Environment variables
    page" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/environment-variables-delete-popover.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-delete-popover.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=9f4d42ee9719adbb6c6850c63839e6a2 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-delete-popover.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=8ec32e6dffaa55bc7baabeec69610136 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-delete-popover.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=42771e6c5b67013d13dbb23a84f37754 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-delete-popover.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=59a6c0bf701def1f80311e61916d481d 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-delete-popover.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=2b0182cb34138fc9beda364b95de7f68 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/environment-variables-delete-popover.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=5564d5157938fad70bbb0bed5cbd7ad7 2500w" />
  </Step>
</Steps>

## In your code

You can use our SDK to get and manipulate environment variables. You can also easily sync environment variables from another service into Trigger.dev.

### Directly manipulating environment variables

We have a complete set of SDK functions (and REST API) you can use to directly manipulate environment variables.

| Function                                           | Description                                                 |
| -------------------------------------------------- | ----------------------------------------------------------- |
| [envvars.list()](/management/envvars/list)         | List all environment variables                              |
| [envvars.upload()](/management/envvars/import)     | Upload multiple env vars. You can override existing values. |
| [envvars.create()](/management/envvars/create)     | Create a new environment variable                           |
| [envvars.retrieve()](/management/envvars/retrieve) | Retrieve an environment variable                            |
| [envvars.update()](/management/envvars/update)     | Update a single environment variable                        |
| [envvars.del()](/management/envvars/delete)        | Delete a single environment variable                        |

#### Initial load from .env file

To initially load environment variables from a `.env` file into your Trigger.dev cloud environment, you can use `envvars.upload()`. This is useful for one-time bulk imports when setting up a new project or environment.

```ts  theme={"theme":"css-variables"}
import { envvars } from "@trigger.dev/sdk";
import { readFileSync } from "fs";
import { parse } from "dotenv";

// Read and parse your .env file
const envContent = readFileSync(".env.production", "utf-8");
const parsed = parse(envContent);

// Upload to Trigger.dev (replace with your project ref and environment slug)
await envvars.upload("proj_your_project_ref", "prod", {
  variables: parsed,
  override: false, // Set to true to override existing variables
});
```

When called inside a task, you can omit the project ref and environment slug as they'll be automatically inferred from the task context:

```ts  theme={"theme":"css-variables"}
import { envvars, task } from "@trigger.dev/sdk";
import { readFileSync } from "fs";
import { parse } from "dotenv";

export const setupEnvVars = task({
  id: "setup-env-vars",
  run: async () => {
    const envContent = readFileSync(".env.production", "utf-8");
    const parsed = parse(envContent);

    // projectRef and environment slug are automatically inferred from ctx
    await envvars.upload({
      variables: parsed,
      override: false,
    });
  },
});
```

<Note>
  This is different from `syncEnvVars` which automatically syncs variables during every deploy. Use `envvars.upload()` for one-time initial loads, and `syncEnvVars` for ongoing synchronization.
</Note>

#### Getting the current environment

When using `envvars.retrieve()` inside a task, you can access the current environment information from the task context (`ctx`). The `envvars.retrieve()` function doesn't return the environment, but you can get it from `ctx.environment`:

```ts  theme={"theme":"css-variables"}
import { envvars, task } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload, { ctx }) => {
    // Get the current environment information
    const currentEnv = ctx.environment.slug; // e.g., "dev", "prod", "staging"
    const envType = ctx.environment.type; // e.g., "DEVELOPMENT", "PRODUCTION", "STAGING", "PREVIEW"

    // Retrieve an environment variable
    // When called inside a task, projectRef and slug are automatically inferred
    const apiKey = await envvars.retrieve("API_KEY");

    console.log(`Retrieved API_KEY from environment: ${currentEnv} (${envType})`);
    console.log(`Value: ${apiKey.value}`);
  },
});
```

The context object provides:

* `ctx.environment.slug` - The environment slug (e.g., "dev", "prod")
* `ctx.environment.type` - The environment type ("DEVELOPMENT", "PRODUCTION", "STAGING", or "PREVIEW")
* `ctx.environment.id` - The environment ID
* `ctx.project.ref` - The project reference

For more information about the context object, see the [Context documentation](/context).

### Sync env vars from another service

You could use the SDK functions above but it's much easier to use our `syncEnvVars` build extension in your `trigger.config` file.

<Note>
  To use the `syncEnvVars` build extension, you should first install the `@trigger.dev/build`
  package into your devDependencies.
</Note>

In this example we're using env vars from [Infisical](https://infisical.com).

```ts trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { syncEnvVars } from "@trigger.dev/build/extensions/core";
import { InfisicalSDK } from "@infisical/sdk";

export default defineConfig({
  build: {
    extensions: [
      syncEnvVars(async (ctx) => {
        const client = new InfisicalSDK();

        await client.auth().universalAuth.login({
          clientId: process.env.INFISICAL_CLIENT_ID!,
          clientSecret: process.env.INFISICAL_CLIENT_SECRET!,
        });

        const { secrets } = await client.secrets().listSecrets({
          environment: ctx.environment,
          projectId: process.env.INFISICAL_PROJECT_ID!,
        });

        return secrets.map((secret) => ({
          name: secret.secretKey,
          value: secret.secretValue,
        }));
      }),
    ],
  },
});
```

#### Syncing environment variables from Vercel

To sync environment variables from your Vercel projects to Trigger.dev, you can use our build extension. Check out our [syncing environment variables from Vercel guide](/guides/examples/vercel-sync-env-vars).

#### Deploy

When you run the [CLI deploy command](/cli-deploy) directly or using [GitHub Actions](/github-actions) it will sync the environment variables from [Infisical](https://infisical.com) to Trigger.dev. This means they'll appear on the Environment Variables page so you can confirm that it's worked.

This means that you need to redeploy your Trigger.dev tasks if you change the environment variables in [Infisical](https://infisical.com).

<Note>
  The `process.env.INFISICAL_CLIENT_ID`, `process.env.INFISICAL_CLIENT_SECRET` and
  `process.env.INFISICAL_PROJECT_ID` will need to be supplied to the `deploy` CLI command. You can
  do this via the `--env-file .env` flag or by setting them as environment variables in your
  terminal.
</Note>

#### Dev

`syncEnvVars` does not have any effect when running the `dev` command locally. If you want to inject environment variables from another service into your local environment you can do so via a `.env` file or just supplying them as environment variables in your terminal. Most services will have a CLI tool that allows you to run a command with environment variables set:

```sh  theme={"theme":"css-variables"}
infisical run -- npx trigger.dev@latest dev
```

Any environment variables set in the CLI command will be available to your local Trigger.dev tasks.

### The syncEnvVars callback return type

You can return env vars as an object with string keys and values, or an array of names + values.

```ts  theme={"theme":"css-variables"}
return {
  MY_ENV_VAR: "my value",
  MY_OTHER_ENV_VAR: "my other value",
};
```

or

```ts  theme={"theme":"css-variables"}
return [
  {
    name: "MY_ENV_VAR",
    value: "my value",
  },
  {
    name: "MY_OTHER_ENV_VAR",
    value: "my other value",
  },
];
```

This should mean that for most secret services you won't need to convert the data into a different format.

### Using Google credential JSON files

Securely pass a Google credential JSON file to your Trigger.dev task using environment variables.

<Steps>
  <Step title="Convert the Google credential file to base64">
    In your terminal, run the following command and copy the resulting base64 string:

    ```
    base64 -i path/to/your/service-account-file.json
    ```
  </Step>

  <Step title="Set up the environment variable in Trigger.dev">
    Follow [these steps](/deploy-environment-variables) to set a new environment variable using the base64 string as the value.

    ```
    GOOGLE_CREDENTIALS_BASE64="<your base64 string>"
    ```
  </Step>

  <Step title="Use the environment variable in your code">
    Add the following code to your Trigger.dev task:

    ```ts  theme={"theme":"css-variables"}
    import { google } from "googleapis";

    const credentials = JSON.parse(
      Buffer.from(process.env.GOOGLE_CREDENTIALS_BASE64, "base64").toString("utf8")
    );

    const auth = new google.auth.GoogleAuth({
      credentials,
      scopes: ["https://www.googleapis.com/auth/cloud-platform"],
    });

    const client = await auth.getClient();
    ```
  </Step>

  <Step title="Use the client in your code">
    You can now use the `client` object to make authenticated requests to Google APIs
  </Step>
</Steps>

## Using `.env.production` or dotenvx with Trigger.dev

Trigger.dev does not automatically load `.env.production` files or dotenvx files during deploys.\
To use these files in your Trigger.dev environment:

### Option 1 — Manually add your environment variables

1. Open your `.env.production` (or `.env`) file
2. Copy the full contents
3. Go to your Trigger.dev project → **Environment Variables**
4. Click **Add variables**
5. Paste the contents directly into the editor

Trigger.dev will automatically parse and create each key/value pair.

This is the simplest way to bring dotenvx or `.env.production` variables into your Trigger.dev environment.

### Option 2 — Sync variables automatically using `syncEnvVars`

If you'd prefer an automated flow, you can use the `syncEnvVars` build extension to programmatically load and return your variables:

```ts  theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { syncEnvVars } from "@trigger.dev/build/extensions/core";
import dotenvx from "@dotenvx/dotenvx";
import { readFileSync } from "fs";

export default defineConfig({
  project: "<project id>",
  build: {
    extensions: [
      syncEnvVars(async () => {
        const envContent = readFileSync(".env.production", "utf-8");
        const parsed = dotenvx.parse(envContent);
        return parsed ?? {};
      }),
    ],
  },
});
```

This will read your .env.production file using dotenvx and sync the variables to Trigger.dev during every deploy.

**Summary**

* Trigger.dev does not automatically detect .env.production or dotenvx files
* You can paste them manually into the dashboard
* Or sync them automatically using a build extension
