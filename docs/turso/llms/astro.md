# Source: https://docs.turso.tech/sdk/ts/guides/astro.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Astro + Turso

> Set up Turso in your Astro project in minutes.

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/astro-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=5b0999657788a4cdccf007d44d34ca89" alt="Astro banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/astro-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/astro-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=acd93bb0a08016652c40033dc484eb53 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/astro-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=f955e74fb17f84acee3a9befa34a6c49 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/astro-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=ba1cf3cb6adb4f65bd1a8eb245402be3 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/astro-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=c35aedb626841dcf33320730c45a3b2a 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/astro-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=495d78b0edd0607175da507eda81e38d 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/astro-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=0d9e9b1989c1a48b3dfaf878629742f9 2500w" />

## Prerequisites

To get the most out of this guide, you'll need to:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have an Astro project — [learn more](https://docs.astro.build/en/install/auto/#1-run-the-setup-wizard)

<Steps>
  <Step title="Install the libSQL SDK">
    <Snippet file="install-libsql-client-ts.mdx" />
  </Step>

  <Step title="Configure database credentials">
    <Snippet file="retrieve-database-credentials.mdx" />
  </Step>

  <Step title="Configure libSQL client">
    ```ts src/turso.ts theme={null}
    import { createClient } from "@libsql/client/web";

    export const turso = createClient({
      url: import.meta.env.TURSO_DATABASE_URL!,
      authToken: import.meta.env.TURSO_AUTH_TOKEN,
    });
    ```

    <Note>
      Astro will soon introduce a new ENV API. [Take a
      look](https://docs.astro.build/en/reference/configuration-reference/#experimentalenv).
    </Note>
  </Step>

  <Step title="Execute SQL">
    ```ts  theme={null}
    ---
    import { turso } from './turso'

    const { rows } = await turso.execute('SELECT * FROM table_name')
    ---
    ```
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="Blog" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-tustro-blog">
    See the full source code
  </Card>
</CardGroup>
