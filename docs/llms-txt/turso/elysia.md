# Source: https://docs.turso.tech/sdk/ts/guides/elysia.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Elysia + Turso

> Set up Turso in your Elysia project in minutes.

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/elysia-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=feb0570b5243f4be9c133fe35f0f8f42" alt="Elysia banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/elysia-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/elysia-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=9d779ae17b95de5bffcdd6d6b00c52cd 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/elysia-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=5c4c42b19a88b721c82bcf3e92746d77 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/elysia-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=c8dac8cb47227600bab867c120f96c62 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/elysia-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=9e29f807ea44446d070721ff0feec017 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/elysia-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=099cee954cf61283c7a3fe348d8b3a40 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/elysia-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=278e08a186ab927fcf1f64c974b935fd 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have an Elysia app — [learn more](https://elysiajs.com/quick-start.html)

<Steps>
  <Step title="Install the libSQL SDK">
    <Snippet file="install-libsql-client-ts.mdx" />
  </Step>

  <Step title="Retrieve database credentials">
    <Snippet file="retrieve-database-credentials.mdx" />
  </Step>

  <Step title="Configure libSQL client">
    <Snippet file="configure-libsql-client-ts.mdx" />
  </Step>

  <Step title="Execute SQL">
    ```ts  theme={null}
    import { Elysia } from "elysia";
    import { turso } from "./lib/turso";

    const app = new Elysia().get("/items", async () => {
      const { rows } = await turso.execute("SELECT * FROM items");
      return rows;
    });
    ```
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="Expenses tracker app with Elysia & Turso" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-expenses-tracker-elysia">
    See the full source code
  </Card>
</CardGroup>
