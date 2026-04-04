# Source: https://developers.webflow.com/webflow-cloud/storing-data/sqlite.mdx

***

title: SQLite storage
slug: storing-data/sqlite
description: Deep dive on using SQLite for structured data in Webflow Cloud.
hidden: false
max-toc-depth: 3
subtitle: 'Reliable, relational storage for structured data'
------------------------------------------------------------

Webflow Cloud lets you store and manage structured data using SQLite, a lightweight, serverless database engine. This managed solution gives you familiar [SQL syntax](https://developers.cloudflare.com/d1/sql-api/sql-statements/), secure access at the edge, and seamless integration with modern frameworks, without the need to manage servers or credentials.

Webflow Cloud handles database provisioning, security, and scaling, so you can focus on building features, not infrastructure.

<Card
  title="Add storage to your app"
  icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/CMS.svg" alt="" className="hidden dark:block" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/CMS.svg" alt="" className="block dark:hidden" />
    </>
  }
  iconPosition="left"
  iconSize="12"
>
  Ready to add your first database to your app? Jump into the quickstart and start building with real data in minutes.

  <div>
    <a href="/webflow-cloud/add-sqlite">
      <button>
        Start building
      </button>
    </a>
  </div>
</Card>

***

## Key benefits

* **Familiar SQL syntax** - Use standard SQL for queries and data manipulation.
* **Automatic authentication** - No credential management, secure by default.
* **Flexible multi-database architecture** - Create thousands of small, isolated databases per account, ideal for multi-tenant SaaS or per-user data isolation.
* **ORM and driver compatibility** - Works with popular tools like Prisma and Drizzle for type-safe queries and schema management.
* **Data security** - All data is encrypted at rest and in transit.
* **Automatic daily backups** - Webflow Cloud manages backups for you.

***

## Add SQLite to your app

Create a SQLite database by declaring [bindings](/webflow-cloud/storing-data/overview#declaring-a-binding) in your `wrangler.json` file in the root of your project. Once declared and deployed, Webflow Cloud automatically connects your app to a managed SQLite instance.

<Steps>
  <Step title="Add a binding to your `wrangler.json` file">
    In your `wrangler.json` file, add a `d1_databases` array. Declare a binding for each database you want to use inside the array.

    **Note:** Webflow Cloud will assign a unique ID for each resource on deployment.

    ```json title="wrangler.json"
    {
    "d1_databases": [
        {
        "binding": "DB",
        "database_name": "MY_DATABASE",
        "database_id": "1234567890", // Replace after deployment
        "migrations_dir": "./migrations" // Specify the directory for your migrations
        }
    ]
    }
    ```
  </Step>

  <Step title="Generate types for your binding">
    Generate TypeScript types for your bindings to enable autocomplete and type safety in your code editor:

    <CodeBlocks>
      ```bash title="Astro"
      npx wrangler types
      ```

      ```bash title="Next.js"
      npx wrangler types
      npm run cf-typegen
      ```
    </CodeBlocks>

    This creates/updates a `worker-configuration.d.ts` file with your binding types. **Note:** in Next.js you'll also need to update the types for the `cloudflare-env.d.ts` file to avoid type errors.
  </Step>

  <Step title="Deploy your app">
    Deploy your app to Webflow Cloud. After deployment, you can view and manage your storage resources [in the Webflow Cloud dashboard.](/webflow-cloud/storing-data/overview#accessing-storage-in-webflow-cloud)
  </Step>
</Steps>

## Work with a SQLite database

### Access the binding

Webflow Cloud exposes your SQLite database to your app as an environment variable, known as a binding. This lets you interact with your database directly from your application code.

Always access the environment variable in your app’s runtime environment. This variable exposes methods from the [Cloudflare Workers Bindings API](https://developers.cloudflare.com/workers/runtime-apis/bindings/), allowing you to run SQL statements directly from your code.

For full details on available methods and advanced usage, see the [Cloudflare D1 Bindings API documentation](https://developers.cloudflare.com/d1/worker-api/).

<Tabs>
  <Tab title="Astro">
    In Astro, you can access the binding in your code using the `locals` object.

    ```typescript title="src/pages/api/users.ts" {7-9, 11-12}
    import type { APIRoute } from "astro";
    import type { D1Database } from "@cloudflare/workers-types";

    // 👀 GET request to create users table and insert users
    export const GET: APIRoute = async ({ request, locals }) => {

      // Access the runtime environment and get the database binding
      const env = (locals as any).runtime.env;
      const db = env.DB as D1Database;

      // Query users using the binding
      const { results } = await DB.prepare("SELECT * FROM users_table;").all();

      // Return the results
      return new Response(JSON.stringify(results), {
        headers: { "Content-Type": "application/json" },
        });
    };
    ```
  </Tab>

  <Tab title="Next.js">
    In Next.js, access the binding in your code using the `getCloudflareContext()` function.

    ```typescript title="src/app/api/users/route.ts" {9-11, 13-14}
    // Import getCloudflareContext and types for D1Database
    import { getCloudflareContext } from "@opennextjs/cloudflare";
    import type { D1Database } from "@cloudflare/workers-types";
    import { NextRequest, NextResponse } from "next/server";

    // 👀 GET request to create users table and insert users
    export async function GET(request: NextRequest) {

      // Access the runtime environment and get the database binding
      const { env } = getCloudflareContext();
      const DB = env.DB as D1Database;

      // Query users using the binding
      const { results } = await DB.prepare("SELECT * FROM users_table;").all();

      // Return the results
      return new Response(JSON.stringify(results), {
        headers: { "Content-Type": "application/json" },
        });
    }
    ```

    <Warning title="Accessing bindings in Next.js">
      Next.js requires you to access bindings through the [Workers runtime](/webflow-cloud/environment) using the `getCloudflareContext()` function. Import `getCloudflareContext` at the top of your file, then use it to access the binding.
    </Warning>

    * **Always** call `getCloudflareContext()` inside a function to ensure the binding is available in the correct context.
    * **For static routes or use outside of request handlers** (such as Incremental Static Regeneration or Static Site Generation), use `getCloudflareContext({ async: true })` and await the result. This ensures the environment bindings are correctly resolved in all environments.
  </Tab>
</Tabs>

### Manage schema and migrations

Webflow Cloud uses migrations to manage changes to your SQLite database schema over time. Migrations are versioned `.sql` files that describe how your database structure should evolve as your app changes.

When you declare your SQLite binding in `wrangler.json`, use the `migrations_dir` property to specify the directory containing your migration files. Webflow Cloud will automatically apply those migrations to your database when you deploy your app.

Additionally, Webflow Cloud supports popular ORM libraries like Drizzle ORM and Prisma-Edge for type-safe queries and schema management. See more on [using an ORM with Webflow Cloud.](/webflow-cloud/storing-data/sqlite#using-an-orm)

<Tip title="Testing migrations locally">
  You can use Cloudflare’s Wrangler CLI to test migrations locally before deploying to Webflow Cloud. See more on [local development with SQLite.](/webflow-cloud/storing-data/sqlite#local-development-with-sqlite)
</Tip>

#### Key concepts

* **Migration files:** Place `.sql` files in the migrations directory you defined in `wrangler.json`. Each file should contain SQL statements that create or modify tables, indexes, or other schema elements.
* **Automatic application:** When you deploy your app, Webflow Cloud automatically applies any new migration files to your database. This keeps your schema up to date with your codebase.
* **Additive changes only:** Migrations **must** be additive. You can’t “undo” a migration by editing or deleting a migration file in your directory. To change your schema, always add a new migration file with the required SQL.

**Example migration file:**

```sql title="migrations/001_init.sql"
CREATE TABLE IF NOT EXISTS users_table (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL
);
```

#### Best practices

* Use clear, sequential filenames (for example, `001_init.sql`, `002_add_email_index.sql`).
* Never edit or remove existing migration files after they’ve been deployed.
* Test migrations locally before deploying to production.

### ORM support for SQLite

Webflow Cloud’s SQLite databases support [edge-compatible](/webflow-cloud/environment) ORM libraries, letting you write type-safe queries and manage schema changes with familiar tools. [Drizzle ORM](https://orm.drizzle.team/docs/get-started/d1-new) and [Prisma-Edge](https://www.prisma.io/docs/orm/overview/databases/cloudflare-d1) are popular choices for seamless integration with Webflow Cloud.

When using an ORM, you’ll typically add a dedicated folder (such as `/migrations` or `/drizzle`) to your project to store migration files and schema definitions. Be sure to specify this directory in your `wrangler.json` using the `migrations_dir` property for your SQLite binding.

```json title="wrangler.json"

{
  "d1_databases": [
      {
          "binding": "DB",
          "database_name": "MY_DATABASE",
          "database_id": "1234567890",
          "migrations_dir": "drizzle"
      }
  ]
}
```

### Local development with SQLite

You can use Cloudflare’s Wrangler CLI to develop and test your SQLite database locally before deploying to Webflow Cloud.

When you run your project locally, Wrangler creates a SQLite database in your `.wrangler` directory. This local database lets you test SQL statements and migrations in a safe environment. Use Wrangler CLI commands, either directly in your terminal or as scripts in `package.json` to run your project and execute SQL statements or files on your local database.

You can use Cloudflare’s Wrangler CLI to:

* **Run your project locally**<br />

  {/* <!-- vale off --> */}

  <CodeBlocks>
    ```bash title="Astro"
    npx wrangler dev
    ```

    ```bash title="Next.js"
    npx opennextjs-cloudflare preview
    ```
  </CodeBlocks>

  {/* <!-- vale on --> */}

  This command starts your app locally, simulating the [Workers runtime](/webflow-cloud/environment) with your declared bindings, and creates a local SQLite database in your `.wrangler` directory.

* **Apply migrations to your local database:**
  ```bash
  wrangler d1 migrations apply <DATABASE_NAME> --local
  ```
  Updates your local SQLite schema with any new migration files in the `migrations` directory defined in your `wrangler.json` file. Replace `<DATABASE_NAME>` with the name of your binding.

* Execute SQL statements or files on your **local** database:

  ```bash
  wrangler d1 execute <DATABASE_NAME> --local --command "<SQL_STATEMENT>"
  wrangler d1 execute <DATABASE_NAME> --local --file ./migrations/001_init.sql
  ```

  Run ad-hoc queries or apply SQL files directly to your local database.

  <Note>
    These commands won't affect your remote database.
  </Note>

<Tip>
  Add these commands as scripts in your `package.json` for convenience. See the following example for Next.js:

  {/* <!-- vale off --> */}

  <CodeBlocks>
    ```json title="package.json - Astro"
    "scripts": {
      "preview": "astro build && wrangler dev",
      "db:apply:local": "wrangler d1 migrations apply DB --local",
    }
    ```

    ```json title="package.json - Next.js"
    "scripts": {
      "preview": "opennextjs-cloudflare build && opennextjs-cloudflare preview",
      "db:apply:local": "wrangler d1 migrations apply DB --local",
    }
    ```
  </CodeBlocks>

  {/* <!-- vale on --> */}
</Tip>

## Next steps

* [Learn about Webflow Cloud Key Value store](/webflow-cloud/storing-data/key-value-store)<br />
  Explore how to store and retrieve unstructured data using Webflow Cloud’s Key Value store.

* [Review Limits for Webflow Cloud SQLite](/webflow-cloud/limits)<br />
  Understand the limits for your databases and storage usage.

* [Set up a SQLite database with Drizzle ORM](/webflow-cloud/storing-data/sqlite#local-development-with-sqlite)<br />
  Follow the guide to set up a SQLite database with Drizzle ORM.

* [Learn more about Webflow Cloud](/webflow-cloud/intro)
  Explore the full capabilities of Webflow Cloud and how it can help you build your next project.

<div>
  # Notes

  D1 is designed for horizontal scale out across multiple, smaller (10 GB) databases, such as per-user, per-tenant or per-entity databases. D1 allows you to build applications with thousands of databases at no extra cost for isolating with multiple databases, as the pricing is based only on query and storage costs.

  Each D1 database can store up to 10 GB of data, and you can create up to thousands of separate D1 databases. This allows you to split a single monolithic database into multiple, smaller databases, thereby isolating application data by user, customer, or tenant.
  SQL queries over a smaller working data set can be more efficient and performant while improving data isolation.
</div>
