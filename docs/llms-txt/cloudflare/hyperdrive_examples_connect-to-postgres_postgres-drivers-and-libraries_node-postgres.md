# Source: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/node-postgres/index.md

---

title: node-postgres (pg) · Cloudflare Hyperdrive docs
description: node-postgres (pg) is a widely-used PostgreSQL driver for Node.js
  applications. This example demonstrates how to use node-postgres with
  Cloudflare Hyperdrive in a Workers application.
lastUpdated: 2026-01-27T21:11:25.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/node-postgres/
  md: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/node-postgres/index.md
---

[node-postgres](https://node-postgres.com/) (pg) is a widely-used PostgreSQL driver for Node.js applications. This example demonstrates how to use node-postgres with Cloudflare Hyperdrive in a Workers application.

Recommended driver

[Node-postgres](https://node-postgres.com/) (`pg`) is the recommended driver for connecting to your Postgres database from JavaScript or TypeScript Workers. It has the best compatibility with Hyperdrive's caching and is commonly available with popular ORM libraries. [Postgres.js](https://github.com/porsager/postgres) is also supported.

Install the `node-postgres` driver:

* npm

  ```sh
  npm i pg@>8.16.3
  ```

* yarn

  ```sh
  yarn add pg@>8.16.3
  ```

* pnpm

  ```sh
  pnpm add pg@>8.16.3
  ```

Note

The minimum version of `node-postgres` required for Hyperdrive is `8.16.3`.

If using TypeScript, install the types package:

* npm

  ```sh
  npm i -D @types/pg
  ```

* yarn

  ```sh
  yarn add -D @types/pg
  ```

* pnpm

  ```sh
  pnpm add -D @types/pg
  ```

Add the required Node.js compatibility flags and Hyperdrive binding to your `wrangler.jsonc` file:

* wrangler.jsonc

  ```jsonc
  {
    // required for database drivers to function
    "compatibility_flags": [
      "nodejs_compat"
    ],
    "compatibility_date": "2026-02-14",
    "hyperdrive": [
      {
        "binding": "HYPERDRIVE",
        "id": "<your-hyperdrive-id-here>"
      }
    ]
  }
  ```

* wrangler.toml

  ```toml
  compatibility_flags = [ "nodejs_compat" ]
  compatibility_date = "2026-02-14"


  [[hyperdrive]]
  binding = "HYPERDRIVE"
  id = "<your-hyperdrive-id-here>"
  ```

Create a new `Client` instance and pass the Hyperdrive `connectionString`:

```ts
// filepath: src/index.ts
import { Client } from "pg";


export default {
  async fetch(
    request: Request,
    env: Env,
    ctx: ExecutionContext,
  ): Promise<Response> {
    // Create a new client instance for each request. Hyperdrive maintains the
    // underlying database connection pool, so creating a new client is fast.
    const client = new Client({
      connectionString: env.HYPERDRIVE.connectionString,
    });


    try {
      // Connect to the database
      await client.connect();


      // Perform a simple query
      const result = await client.query("SELECT * FROM pg_tables");


      return Response.json({
        success: true,
        result: result.rows,
      });
    } catch (error: any) {
      console.error("Database error:", error.message);


      return new Response("Internal error occurred", { status: 500 });
    }
  },
};
```
