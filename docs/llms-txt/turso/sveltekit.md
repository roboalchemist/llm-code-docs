# Source: https://docs.turso.tech/sdk/ts/guides/sveltekit.md

# SvelteKit + Turso

> Set up Turso in your SvelteKit project in minutes

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/svelte-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=c5f43db5d48bf2eb2657f687d1f60fa2" alt="SvelteKit banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/svelte-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/svelte-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=4732f954767bc40a9a61401d1aaf71a3 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/svelte-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=1b44ab6d36b6d7bd05914e7cb0c5e408 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/svelte-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=5b209f1aa1ccbdbfac645dc03f9bf41a 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/svelte-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=5bc36b6595ae2e6cda96680e98a7bffc 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/svelte-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=b003cd9bdeb13d8f583e782fb07be7d2 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/svelte-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=6739569534ee1a20e6ea67e6391ee8ab 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a SvelteKit app — [learn more](https://kit.svelte.dev/docs/creating-a-project)

<Steps>
  <Step title="Install the libSQL SDK">
    <Snippet file="install-libsql-client-ts.mdx" />
  </Step>

  <Step title="Configure database credentials">
    <Snippet file="retrieve-database-credentials.mdx" />
  </Step>

  <Step title="Configure libSQL Client.">
    <CodeGroup>
      ```ts Node.js / Serverless theme={null}
      import { TURSO_DATABASE_URL, TURSO_AUTH_TOKEN } from "$env/static/private";
      import { createClient } from "@libsql/client";

      export const turso = createClient({
        url: TURSO_DATABASE_URL,
        authToken: TURSO_AUTH_TOKEN,
      });
      ```

      ```ts Edge Runtimes theme={null}
      import { TURSO_DATABASE_URL, TURSO_AUTH_TOKEN } from "$env/static/private";
      import { createClient } from "@libsql/client/web";

      export const turso = createClient({
        url: TURSO_DATABASE_URL,
        authToken: TURSO_AUTH_TOKEN,
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Execute SQL">
    <CodeGroup>
      ```ts src/routes/+page.server.ts theme={null}
      import { turso } from "$lib/turso.server";

      export async function load() {
        const { rows } = await turso.execute("SELECT * FROM table_name");

        return { rows };
      }
      ```

      ```svelte src/routes/+page.svelte theme={null}
      <script lang="ts">
        export let data
      </script>

      <ul>
        {#each data.rows as row}
          <li>{row.id}</li>
        {/each}
      </ul>
      ```
    </CodeGroup>
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="Blog" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-at-the-polls">
    See the full source code
  </Card>
</CardGroup>
