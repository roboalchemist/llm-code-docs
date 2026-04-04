# Source: https://docs.turso.tech/sdk/ts/guides/hono.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Hono + Turso

> Set up Turso in your Hono project in minutes.

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/hono-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=1c88c1bf0425b350d511be756e47f83f" alt="Hono banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/hono-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/hono-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=234cb8da3dfdea684ed7917070fa098a 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/hono-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=305fa4551cad881c77cd62778aa08dd1 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/hono-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=771fafafa997bdeacd3ef111d78e7871 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/hono-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=e9ffe56a8ba2cda4e00d97d59ddb6cdd 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/hono-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=5e96d297a5e2a61b343e4f6b83e2b273 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/hono-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=abbd75b72849fc77ab6f29082958ccff 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Hono app — [learn more](https://hono.dev/top#quick-start)

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
    import { Hono } from "hono";
    import { turso } from "./lib/turso";

    const app = new Hono();

    app.get("/items", async (c) => {
      const { rows } = await turso.execute("SELECT * FROM items");

      return c.json({ rows });
    });
    ```
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="Expenses tracker app with Hono & Turso" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-expenses-tracker-hono">
    See the full source code
  </Card>
</CardGroup>
