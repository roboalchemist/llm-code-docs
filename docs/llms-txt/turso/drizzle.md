# Source: https://docs.turso.tech/sdk/ts/orm/drizzle.md

# Drizzle + Turso

> Configure Drizzle to work with Turso

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/drizzle-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=fa7f430abb2a3b3df72c6ca45649b099" alt="Drizzle banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/drizzle-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/drizzle-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=26a0e032b82dd3f67c65acc2afbb8866 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/drizzle-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=c2668f6d2dc51b4d3b5b077c81e983a2 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/drizzle-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=3dd2356ee0d84cd04a535ecfe53e00f4 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/drizzle-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=2c5507db081b3fe193ba071007faa15c 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/drizzle-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=b6fb550ab1756ba75a875e8e84af3917 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/drizzle-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=95887a93a56c3151331382fb30fd71b0 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)

<Steps>
  <Step title="Install Drizzle and the libSQL SDK">
    <CodeGroup>
      ```bash npm theme={null}
      npm i drizzle-orm @libsql/client dotenv
      npm i -D drizzle-kit
      ```

      ```bash pnpm theme={null}
      pnpm add drizzle-orm @libsql/client dotenv
      pnpm add -D drizzle-kit
      ```

      ```bash yarn theme={null}
      yarn add drizzle-orm @libsql/client dotenv
      yarn add -D drizzle-kit
      ```
    </CodeGroup>

    Finish by updating `package.json` to include three new `scripts`:

    ```json  theme={null}
    {
      "scripts": {
        "db:generate": "drizzle-kit generate",
        "db:migrate": "drizzle-kit migrate",
        "db:studio": "drizzle-kit studio"
      }
    }
    ```
  </Step>

  <Step title="Retrieve database credentials">
    <Snippet file="retrieve-database-credentials.mdx" />
  </Step>

  <Step title="Create a Drizzle schema">
    ```ts db/schema.ts theme={null}
    import { sql } from "drizzle-orm";
    import { text, sqliteTable } from "drizzle-orm/sqlite-core";

    export const fooTable = sqliteTable("foo", {
      bar: text("bar").notNull().default("Hey!"),
    });
    ```
  </Step>

  <Step title="Configure Drizzle Kit">
    Create the file `drizzle.config.ts` in the root of your project with the following:

    ```ts drizzle.config.ts theme={null}
    require("dotenv").config();

    import type { Config } from "drizzle-kit";

    export default {
      schema: "./db/schema.ts",
      out: "./migrations",
      dialect: "turso",
      dbCredentials: {
        url: process.env.TURSO_DATABASE_URL!,
        authToken: process.env.TURSO_AUTH_TOKEN,
      },
    } satisfies Config;
    ```

    <Note>
      We're using `dotenv` above, but if you're using something like Next.js, Remix, Astro, or Vite, you can use their built-in environment variables manager to source these values.
    </Note>
  </Step>

  <Step title="Connect Drizzle with libSQL">
    <CodeGroup>
      ```ts Node.js / Serverless theme={null}
      import { drizzle } from "drizzle-orm/libsql";
      import { createClient } from "@libsql/client";

      const turso = createClient({
        url: process.env.TURSO_DATABASE_URL!,
        authToken: process.env.TURSO_AUTH_TOKEN,
      });

      export const db = drizzle(turso);
      ```

      ```ts Edge Runtimes theme={null}
      import { drizzle } from "drizzle-orm/libsql";
      import { createClient } from "@libsql/client/web";

      const turso = createClient({
        url: process.env.TURSO_DATABASE_URL!,
        authToken: process.env.TURSO_AUTH_TOKEN,
      });

      export const db = drizzle(turso);
      ```
    </CodeGroup>
  </Step>

  <Step title="Database migrations">
    Drizzle can generate and apply database migrations with `drizzle-kit`.

    Whenever you make changes to the schema, run `db:generate`:

    ```bash  theme={null}
    npm run db:generate
    ```

    Now apply these changes to the database with `db:migrate`:

    ```bash  theme={null}
    npm run db:migrate
    ```
  </Step>

  <Step title="Query">
    ```ts  theme={null}
    import { db } from "./db";
    import { fooTable } from "./schema";

    const result = await db.select().from(fooTable).all();
    ```
  </Step>

  <Step title="Connect Drizzle Studio">
    <CodeGroup>
      ```bash npm theme={null}
      npm run db:studio
      ```

      ```bash pnpm theme={null}
      pnpm run db:studio
      ```
    </CodeGroup>
  </Step>
</Steps>

## Vector Embeddings

You can extend Drizzle to support Turso's native vector — [learn more](/features/ai-and-embeddings).

<Steps>
  <Step title="Define custom vector type">
    Inside `db/schema.ts`, add the following:

    ```typescript  theme={null}
    import { sql } from "drizzle-orm";
    import { customType } from "drizzle-orm/sqlite-core";

    const float32Array = customType<{
      data: number[];
      config: { dimensions: number };
      configRequired: true;
      driverData: Buffer;
    }>({
      dataType(config) {
        return `F32_BLOB(${config.dimensions})`;
      },
      fromDriver(value: Buffer) {
        return Array.from(new Float32Array(value.buffer));
      },
      toDriver(value: number[]) {
        return sql`vector32(${JSON.stringify(value)})`;
      },
    });
    ```
  </Step>

  <Step title="Create a table with a vector column">
    Now where you define the schema, invoke `float32Array` to create a column that stores vectors:

    ```typescript  theme={null}
    import { sqliteTable, integer } from "drizzle-orm/sqlite-core";

    export const vectorTable = sqliteTable("vector_table", {
      id: integer("id").primaryKey(),
      vector: float32Array("vector", { dimensions: 3 }),
    });
    ```
  </Step>

  <Step title="Create a vector index">
    You will need to use raw SQL to create the index:

    ```typescript  theme={null}
    import { drizzle } from "drizzle-orm/libsql";
    import { createClient } from "@libsql/client";

    const client = createClient({
      url: process.env.TURSO_DATABASE_URL!,
      authToken: process.env.TURSO_AUTH_TOKEN,
    });

    const db = drizzle(client);

    await db.run(sql`
      CREATE INDEX IF NOT EXISTS vector_index
      ON vector_table(vector)
      USING vector_cosine(3)
    `);
    ```
  </Step>

  <Step title="Insert vector data">
    ```typescript  theme={null}
    await db
      .insert(vectorTable)
      .values([{ vector: sql`vector32(${JSON.stringify([1.1, 2.2, 3.3])})` }]);
    ```
  </Step>

  <Step title="Query vector data">
    Calculate vector distance:

    ```typescript  theme={null}
    const res = await db
      .select({
        distance: sql<number>`vector_distance_cos(${vectorTable.vector}, vector32(${JSON.stringify([2.2, 3.3, 4.4])}))`,
      })
      .from(vectorTable);

    console.log(res);
    ```

    Perform efficient nearest neighbor search:

    ```typescript  theme={null}
    const topK = await db
      .select({
        id: sql`id`,
        distance: sql`distance`,
      })
      .from(
        sql`vector_top_k('vector_index', vector32(${JSON.stringify([2.2, 3.3, 4.4])}), 5)`,
      )
      .leftJoin(vectorTable, sql`${vectorTable}.id = id`);

    console.log(topK);
    ```
  </Step>
</Steps>

Remember to create appropriate indexes for efficient vector operations and adjust vector dimensions as needed for your use case.
