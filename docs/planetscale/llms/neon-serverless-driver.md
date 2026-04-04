# Source: https://planetscale.com/docs/postgres/connecting/neon-serverless-driver.md

# Using the Neon serverless driver

PlanetScale supports connections via the [Neon serverless driver](https://neon.com/docs/serverless/serverless-driver).
This is a good option for connecting to your PlanetScale database in serverless environments like [Vercel Functions](https://vercel.com/docs/functions) or [AWS Lambda](https://aws.amazon.com/pm/lambda/).
You can find detailed documentation on [Neon's website](https://neon.com/docs/serverless/serverless-driver) or on the [GitHub repository](https://github.com/neondatabase/serverless).

## HTTP vs WebSocket modes

The Neon serverless driver supports two connection modes:

* **HTTP mode** — Uses the `neon` function to execute queries over HTTP. Faster for single queries and non-interactive transactions. No connection state is maintained between requests.
* **WebSocket mode** — Uses the `Pool` object to establish a WebSocket connection. Required for session support, interactive transactions, or `node-postgres` compatibility.

PlanetScale supports both modes. Choose based on your use case:

| Use case                                        | Recommended mode |
| ----------------------------------------------- | ---------------- |
| Single queries                                  | HTTP             |
| Non-interactive transactions (batch of queries) | HTTP             |
| Interactive transactions                        | WebSocket        |
| Session-based features                          | WebSocket        |
| `node-postgres` compatibility                   | WebSocket        |

## Setting up credentials

Both modes use the same credentials setup.

<Steps>
  <Step>
    Install the driver via npm:

    ```bash  theme={null}
    npm install @neondatabase/serverless
    ```
  </Step>

  <Step>
    You'll need to create a [Postgres role](/docs/postgres/connecting/roles) to use with the driver.
    Once you have these credentials, place them in environment variables:

    ```bash  theme={null}
    DATABASE_HOST=XXXX.pg.psdb.cloud
    DATABASE_PORT=5432
    DATABASE_NAME=XXXX
    DATABASE_USERNAME=XXXX
    DATABASE_PASSWORD=pscale_pw_XXXX
    ```

    These can all be added to a unified Postgres connection URL for use by the driver:

    ```bash  theme={null}
    DATABASE_URL="postgresql://$DATABASE_USERNAME:$DATABASE_PASSWORD@$DATABASE_HOST:$DATABASE_PORT/$DATABASE_NAME"
    ```
  </Step>
</Steps>

## Using HTTP mode

HTTP mode is the simplest way to execute queries. You must configure the `fetchEndpoint` to use PlanetScale's SQL endpoint.

```ts  theme={null}
import { neon, neonConfig } from "@neondatabase/serverless";

// This MUST be set for PlanetScale Postgres connections
neonConfig.fetchEndpoint = (host) => `https://${host}/sql`;

const sql = neon(process.env.DATABASE_URL!);

const posts = await sql`SELECT * FROM posts WHERE id = ${postId}`;
```

The `neon` function returns a tagged template literal that automatically handles parameterized queries, protecting against SQL injection. See [Neon's HTTP mode documentation](https://neon.com/docs/serverless/serverless-driver#use-the-driver-over-http) for additional configuration options.

### Non-interactive transactions

HTTP mode supports non-interactive transactions where you send a batch of queries to be executed together. Use the `transaction` function:

```ts  theme={null}
import { neon, neonConfig } from "@neondatabase/serverless";

// This MUST be set for PlanetScale Postgres connections
neonConfig.fetchEndpoint = (host) => `https://${host}/sql`;

const sql = neon(process.env.DATABASE_URL!);

const [posts, tags] = await sql.transaction([
  sql`SELECT * FROM posts ORDER BY posted_at DESC LIMIT ${limit}`,
  sql`SELECT * FROM tags`,
]);
```

## Using WebSocket mode

WebSocket mode provides a full `Pool` interface compatible with the `pg` library. See [Neon's WebSocket documentation](https://neon.com/docs/serverless/serverless-driver#use-the-driver-over-websockets) for the full API reference. This mode requires additional configuration for PlanetScale connections.

<Steps>
  <Step>
    When connecting, you must set the following configuration options:

    ```ts  theme={null}
    neonConfig.pipelineConnect = false;
    neonConfig.wsProxy = (host, port) => `${host}/v2?address=${host}:${port}`;
    ```
  </Step>

  <Step>
    Here's a complete example:

    ```ts  theme={null}
    import ws from "ws";
    import { Pool, neonConfig } from "@neondatabase/serverless";

    neonConfig.webSocketConstructor = ws;
    // These MUST be set for PlanetScale Postgres connections
    neonConfig.pipelineConnect = false;
    neonConfig.wsProxy = (host, port) => `${host}/v2?address=${host}:${port}`;

    const pool = new Pool({ connectionString: process.env.DATABASE_URL });

    const posts = await pool.query("SELECT * FROM posts WHERE id = $1", [postId]);

    pool.end();
    ```
  </Step>
</Steps>

<Note>
  In browser or edge environments that have a native `WebSocket` global, you don't need to import `ws` or set `neonConfig.webSocketConstructor`.
</Note>

## Security

PlanetScale requires `SCRAM-SHA-256` for all authentication to Postgres servers.
We maintain this strict requirement for security purposes.

For WebSocket connections, you must set `neonConfig.pipelineConnect = false;`.
This adds a bit of additional latency, but is necessary to connect using `SCRAM-SHA-256`.
When this is `"password"` (the default value) it requires using cleartext password authentication, reducing connection security.

HTTP mode connections handle authentication automatically and don't require this configuration.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt