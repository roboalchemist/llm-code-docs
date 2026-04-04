# Source: https://docs.turso.tech/sdk/ts/guides/nuxt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Nuxt + Turso

> Set up Turso in your Nuxt project in minutes

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nuxt-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=9c0353730a9944cd5e99e71cb2666025" alt="Nuxt banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/nuxt-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nuxt-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=d23020628a50e20de2adb3640c9f8d59 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nuxt-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=1332aca63b6ecb15314160bb66f6233c 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nuxt-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=da752fd34f3d2d9c198168372325f2dd 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nuxt-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=cc7f2c6c63e6fdc34eb212fd521aff88 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nuxt-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=1a8a4af2319bfe8b67d182a6537b5fd2 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nuxt-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=4c090687b14172f59a0e3159aaf323b3 2500w" />

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Nuxt app — [learn more](https://nuxt.com/docs/getting-started/installation#new-project)

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

    Assign credentials to the environment variables inside `.env`.

    ```bash  theme={null}
    NUXT_TURSO_DATABASE_URL=
    NUXT_TURSO_AUTH_TOKEN=
    ```
  </Step>

  <Step title="Configure variables inside Nuxt's runtime config.">
    ```ts nuxt.config.ts theme={null}
    export default defineNuxtConfig({
      runtimeConfig: {
        turso: {
          databaseUrl: "",
          authToken: "",
        },
      },
    });
    ```

    <Note>
      Make sure that names of the keys in the `runtimeConfig` object match the names
      of your environment variables. Read more about this
      [here](https://nuxt.com/docs/guide/going-further/runtime-config).
    </Note>
  </Step>

  <Step title="Configure libSQL Client.">
    ```ts server/utils/turso.ts theme={null}
    import { createClient } from "@libsql/client";
    // You can optionally pass in the event to useRuntimeConfig
    // import { H3Event } from "h3";

    export function useTurso(/* event: H3Event */) {
      const { turso } = useRuntimeConfig(/* event */);

      return createClient({
        url: turso.databaseUrl,
        authToken: turso.authToken,
      });
    }
    ```
  </Step>

  <Step title="Execute SQL">
    ```ts server/api/items.get.ts theme={null}
    export default defineEventHandler(async (event) => {
      const client = useTurso(/* event */);
      const { rows } = await client.execute("select * from table_name");

      return {
        data: {
          items: rows,
        },
      };
    });
    ```
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="Website + App" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-top-web-frameworks">
    See the full source code
  </Card>
</CardGroup>
