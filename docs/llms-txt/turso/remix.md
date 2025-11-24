# Source: https://docs.turso.tech/sdk/ts/guides/remix.md

# Remix + Turso

> Set up Turso in your Remix project in minutes

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/remix-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=84822de5a6eb5531447a66d6afe6662a" alt="Remix banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/remix-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/remix-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=cb9d6a03ec600ad6299cf08724510d04 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/remix-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=500769f952ad411d97629e2c0a8f7097 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/remix-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=0ef00c6077224f81ed5bcb9909c07e7b 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/remix-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=590ba1f30c3be2dae0a94fe04eec59b2 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/remix-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=ee9954f6081c95ff47c408a60efc2d85 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/remix-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=6be355e382ad6a283961015d0e8d51e6 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Remix app — [learn more](https://remix.run/docs/en/main/start/quickstart#quick-start)

<Steps>
  <Step title="Install the libSQL SDK">
    <Snippet file="install-libsql-client-ts.mdx" />
  </Step>

  <Step title="Configure database credentials">
    <Snippet file="retrieve-database-credentials.mdx" />
  </Step>

  <Step title="Configure libSQL Client.">
    <Snippet file="configure-libsql-client-ts.mdx" />
  </Step>

  <Step title="Execute SQL">
    ```ts app/routes/_index.ts theme={null}
    import type { LoaderFunction } from "@remix-run/node";

    import { turso } from "~/lib/turso";

    export const loader: LoaderFunction = async () => {
      const { rows } = await turso.execute("SELECT * from TABLE_NAME");

      return {
        items: rows,
      };
    };
    ```
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="E-commerce Store" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-the-mug-store">
    See the full source code
  </Card>

  <Card title="CRM App" icon="github" href="https://github.com/tursodatabase/examples/tree/master/app-turso-crm">
    See the full source code
  </Card>
</CardGroup>
