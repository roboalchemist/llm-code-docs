# Source: https://docs.turso.tech/sdk/ts/guides/quasar.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Quasar + Turso

> Set up Turso in your Quasar project in minutes

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/quasar-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=182fddd15a287e68b1780415464cec13" alt="Quasar banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/quasar-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/quasar-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=603696183288616b38c56d31534b9c31 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/quasar-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=4ec5e625b6aa4a81e85c688fe31ad953 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/quasar-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=89f836cae210c0ca240d118025141a84 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/quasar-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=76f69f80e2758438693195f418c8924c 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/quasar-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=eb8e7b24973ed40ede4df58d6131ddeb 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/quasar-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=d57a65d82eea0054be3a6f6b4177ea79 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Quasar app — [learn more](https://quasar.dev/start/quick-start#step-1-create-a-project)

<Steps>
  <Step title="Install the libSQL SDK">
    <Snippet file="install-libsql-client-ts.mdx" />
  </Step>

  <Step title="Configure database credentials">
    Get the database URL:

    ```bash  theme={null}
    turso db show --url <database-name>
    ```

    Get the database authentication token:

    ```bash  theme={null}
    turso db tokens create <database-name>
    ```

    Assign credentials to the environment variables inside `.env.local`.

    ```bash  theme={null}
    VITE_TURSO_DATABASE_URL="..."
    VITE_TURSO_AUTH_TOKEN="..."
    ```
  </Step>

  <Step title="Configure libSQL Client">
    ```js  theme={null}
    import { createClient } from "@libsql/client/web";

    const turso = createClient({
      url: import.meta.env.VITE_TURSO_DATABASE_URL,
      authToken: import.meta.env.VITE_TURSO_AUTH_TOKEN,
    });
    ```

    <Info>
      Avoid a [gotcha
      moment](https://github.com/quasarframework/quasar/discussions/16071) by
      modifying the app configuration using the settings below.
    </Info>

    ```javascript quasar.config.js theme={null}
    {
      build: {
        target: {
          browser: [
            'es2020', 'edge88', 'firefox78', 'chrome87', 'safari13.1'
          ],
          node: 'node16'
        },
        extendViteConf(config) {
          config.optimizeDeps = {
            esbuildOptions: {
              target: 'es2020',
            }
          }
        }
      }
    }
    ```
  </Step>

  <Step title="Fetch data from Turso.">
    ```js IndexPage.vue theme={null}
    import { ref } from "vue";

    const items = ref();

    const { rows } = await turso.execute("select * from my-table");

    items.value = rows;
    ```
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="Todo App" icon="github" href="https://github.com/tursodatabase/examples/tree/master/quasar-todo-list">
    See the full source code
  </Card>
</CardGroup>
