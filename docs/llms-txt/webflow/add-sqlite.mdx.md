# Source: https://developers.webflow.com/webflow-cloud/add-sqlite.mdx

***

title: Add a SQLite database to your app
slug: add-sqlite
description: Add a SQLite database to your app
hidden: false
subtitle: Add persistent storage to your Webflow Cloud app using SQLite and Drizzle ORM
---------------------------------------------------------------------------------------

This tutorial guides you through connecting a [SQLite database](/webflow-cloud/storing-data/sqlite)
to your Webflow Cloud app, defining your schema, and building API routes to store
and retrieve user data.

**What you’ll learn:**

* How to add a SQLite database to your Webflow Cloud project
* How to define and manage your schema with Drizzle ORM
* How to run and apply database migrations
* How to create API routes to add and fetch data

## Prerequisites

Before you begin, make sure you have:

* A Webflow Cloud project linked to a GitHub repository
* A Webflow Cloud environment set up
* Node.js 20+ and npm 10+
* Basic familiarity with JavaScript/TypeScript

<Note title="New to Webflow Cloud?">
  If you haven’t already, follow the [Quick Start guide](/webflow-cloud/getting-started) to set up your project and environment.
</Note>

## Add a SQLite database

Set up a SQLite database so your Webflow Cloud app can store data. This step connects your project to a reliable, easy-to-use SQLite database.

<Steps>
  <Step title="Open your project in your IDE.">
    Navigate to your project in your IDE, and open the `wrangler.json` file.
  </Step>

  <Step title="Add a SQLite database binding to the `d1_databases` array in `wrangler.json`.">
    Add the `d1_databases` array to the `wrangler.json` file, and declare a new database binding.

    ```json
    "d1_databases": [
      {
        "binding": "DB", // A valid JavaScript variable name
        "database_name": "db",
        "database_id": "1234", // Webflow Cloud will generate this for you once you deploy your app
        "migrations_dir": "drizzle" // We'll create this directory later
      }
    ]
    ```

    This tells Webflow Cloud to create a SQLite database for your project and to apply any migrations found in the `drizzle` directory.

    | Property         | Description                                                                                                      |
    | ---------------- | ---------------------------------------------------------------------------------------------------------------- |
    | `binding`        | The variable name you’ll use to access the database in your code. This must be a valid JavaScript variable name. |
    | `database_name`  | The name for your database.                                                                                      |
    | `database_id`    | A unique identifier for your database (Webflow Cloud will generate this for you once you deploy your app).       |
    | `migrations_dir` | The directory where your migration files are stored.                                                             |
  </Step>

  <Step title="Generate TypeScript types for your binding.">
    <Tabs>
      <Tab title="Astro">
        ```bash title="Terminal"
        wrangler types
        ```
      </Tab>

      <Tab title="Next.js">
        ```bash
        npm run cf-typegen
        ```
      </Tab>
    </Tabs>

    This command updates your project’s type definitions so you can safely access the database in your code.
  </Step>
</Steps>

## Add Drizzle ORM

[Drizzle ORM](https://orm.drizzle.team/docs/overview) is a tool that helps you work with your database using JavaScript or TypeScript code, instead of writing raw SQL. It makes it easier to define your database structure, run migrations, and interact with your data safely and reliably.

<Steps>
  <Step title="Install Drizzle ORM and Drizzle Kit.">
    Install the required packages for working with Drizzle ORM and managing migrations:

    ```bash
    npm i drizzle-orm
    npm i -D drizzle-kit tsx better-sqlite3
    ```

    * `drizzle-orm`: The ORM for interacting with your database.
    * `drizzle-kit`: CLI for migrations and schema generation.
    * `tsx` and `better-sqlite3`: Required for local development and SQLite support.
  </Step>

  <Step title="Create the Drizzle config file.">
    In the root of your project, create a file named `drizzle.config.ts`. Configure the schema path and output path:

    <CodeBlocks>
      ```typescript title="drizzle.config.ts"
      import { defineConfig } from "drizzle-kit";

      export default defineConfig({
          schema: "./src/db/schema/index.ts",
          out: "./drizzle",
          dialect: "sqlite",
      });
      ```
    </CodeBlocks>
  </Step>

  <Step title="Add local migration scripts to your package.json.">
    Add the following scripts to your `package.json` to manage **local** migrations:

    ```json
    "scripts": {
        // ... existing scripts ...
        "db:generate": "drizzle-kit generate",
        "db:apply:local": "wrangler d1 migrations apply DB --local",
    }
    ```

    * `db:apply:local`: Applies migrations to your local database.
    * `db:generate`: Generates migration files from your schema.
  </Step>
</Steps>

## Create a schema

A database schema defines the data your app can store. Here, you’ll set up your first table to keep things organized as your project grows.

<Steps>
  <Step title="Create the schema directory.">
    To keep your schema organized, create a `db/schema` folder inside your `src` directory to hold all your schema files.

    ```bash
    cd src
    mkdir -p db/schema
    ```
  </Step>

  <Step title="Define your first table.">
    Create an `index.ts` file in `src/db/schema` Import the necessary Drizzle ORM methods use them to define a `usersTable`:

    <CodeBlocks>
      ```typescript title="src/db/schema/index.ts"
      // Import the necessary Drizzle ORM functions
      import { sqliteTable, text, int } from "drizzle-orm/sqlite-core";

      // Define the users table with the following fields:
      // - id: The primary key of the table
      // - name: The name of the user
      // - age: The age of the user
      // - email: The email of the user

      export const usersTable = sqliteTable("users_table", {
          id: int().primaryKey({ autoIncrement: true }),
          name: text().notNull(),
          age: int().notNull(),
          email: text().notNull().unique(),
      });
      ```
    </CodeBlocks>

    This code defines a `usersTable` with multiple fields.

    By defining your schema in code, you ensure your database structure is always documented and version-controlled. To learn more about defining schemas with Drizzle ORM, see the [Drizzle ORM documentation](https://orm.drizzle.team/docs/sql-schema-declaration).
  </Step>

  <Step title="Initialize the database">
    Whenever you change your schema, you need to generate a migration. A migration is a set of instructions for updating the database structure. Migrations let you evolve your database structure safely over time, without losing data or breaking your app.

    Since you just created a new table, you need to generate a migration file to update the database. In your terminal, run the following commands to generate a new migration file in the `drizzle` directory from your schema defined in `src/db/schema/index.ts`, and apply it to the local database:

    ```bash
    npm run db:generate
    npm run db:apply:local
    ```
  </Step>
</Steps>

## Connect to the database

Now you’ll connect your app to the database. This makes it easy to add, find, and update information as your users interact with your app.

<Steps>
  <Step title="Create a helper function to get the database instance.">
    To avoid repeating connection logic, create a reusable helper that returns a Drizzle ORM instance. This ensures you always use the correct schema and [environment](/webflow-cloud/environment), and improves performance by reusing connections.

    In `src/db`, create a `getDb.ts` file and add the following code:

    <Tabs>
      <Tab title="Astro">
        ```typescript title="src/db/getDb.ts"
        import { drizzle } from "drizzle-orm/d1";
        import * as schema from "./schema";

        // For dynamic routes
        export const getDb = (locals: App.Locals) => {
        const { env } = locals.runtime;
        return drizzle(env.DB, { schema });
        };

        // For static routes
        export const getDbAsync = async (locals: App.Locals) => {
        const { env } = locals.runtime;
        return drizzle(env.DB, { schema });
        };
        ```
      </Tab>

      <Tab title="Next.js">
        ```typescript title="src/db/getDb.ts"
        import { getCloudflareContext } from "@opennextjs/cloudflare";
        import { drizzle } from "drizzle-orm/d1";
        import { cache } from "react";
        import * as schema from "./schema";

        // For dynamic routes
        export const getDb = cache(() => {
        const { env } = getCloudflareContext();
        return drizzle(env.DB, { schema });
        });

        // For static routes
        export const getDbAsync = cache(async () => {
        const { env } = await getCloudflareContext({ async: true });
        return drizzle(env.DB, { schema });
        });
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Create a route to add users to the users table.">
    To allow your app to add new users, create an API route that accepts user details and inserts them into the `usersTable`. This pattern is common for building RESTful APIs and helps keep your data layer organized.

    <Tabs>
      <Tab title="Astro">
        In `src/pages/api`, create a `users.ts` file with the following code:

        ```typescript title="src/pages/api/users.ts"
        import { APIRoute } from "astro";
        import { getDb } from "../../db/getDb";
        import { usersTable } from "../../db/schema";

        // Define the expected shape of the request body
        type UserInput = {
        name: string;
        age: number;
        email: string;
        };

        // Define CORS headers
        const corsHeaders = {
        "Access-Control-Allow-Origin": "*", // Or specify your domain instead of *
        "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
        };

        // Handle OPTIONS requests for CORS preflight
        export const OPTIONS: APIRoute = async ({ request }) => {
            return new Response(null, {
                headers: corsHeaders,
            });
        };

        // Handle POST requests to add a new user
        export const POST: APIRoute = async ({ request, locals }) => {
        const db = getDb(locals); // Get the database instance
        const { name, age, email }: UserInput = await request.json();
        try {
            // Insert the new user into the usersTable
            const newUser = await db
            .insert(usersTable)
            .values({ name, age, email })
            .returning();
            // Return the created user
            return Response.json(newUser[0], { status: 201 });
        } catch (error) {
            // Handle errors (e.g., duplicate email)
            return Response.json({ error: "Failed to create user" }, { status: 500 });
        }
        };
        ```
      </Tab>

      <Tab title="Next.js">
        In `src/app/api/users`, create a `route.ts` file:

        ```typescript title="src/app/api/users/route.ts"
        import { NextRequest, NextResponse } from "next/server";
        import { getDb } from "@/db/getDb";
        import { usersTable } from "@/db/schema";

        type UserInput = {
        name: string;
        age: number;
        email: string;
        };

        export async function POST(request: NextRequest) {
        const db = getDb();
        const { name, age, email }: UserInput = await request.json();
        try {
            const newUser = await db
            .insert(usersTable)
            .values({ name, age, email })
            .returning();
            return NextResponse.json(newUser[0], { status: 201 });
        } catch (error) {
            return NextResponse.json({ error: "Failed to create user" }, { status: 500 });
        }
        }
        ```
      </Tab>
    </Tabs>

    **What’s happening?**

    * The route receives a POST request with user data.
    * It inserts the data into the `usersTable`.
    * On success, it returns the new user; on error, it returns a failure message.
  </Step>

  <Step title="Create a route to get users from the users table.">
    To retrieve data, create a GET route that returns all users from the database.

    <Tabs>
      <Tab title="Astro">
        In the same `users.ts` file, add:

        ```typescript title="src/pages/api/users.ts"
        export const GET: APIRoute = async ({ locals }) => {
          const db = getDb(locals);
          try {
            const users = await db.select().from(usersTable);
            return Response.json(users, { status: 200 });
          } catch (error) {
            return Response.json({ error: "Failed to fetch users" }, { status: 500 });
          }
        };
        ```
      </Tab>

      <Tab title="Next.js">
        In the same `route.ts` file, add:

        ```typescript title="src/app/api/users/route.ts"
        export async function GET(request: NextRequest) {
          const db = getDb();
          try {
            const users = await db.select().from(usersTable);
            return NextResponse.json(users, { status: 200 });
          } catch (error) {
            return NextResponse.json(
              { error: "Failed to fetch users" },
              { status: 500 }
            );
          }
        }
        ```
      </Tab>
    </Tabs>

    **What’s happening?**

    * The route receives a GET request.
    * It queries all users from the database.
    * Returns the list of users or an error message.
  </Step>

  <Step title="Test your routes.">
    Test your API routes to make sure you can add and retrieve users from your database.

    1. Start your app by running the following command in your terminal:

       ```bash
       npm run dev
       ```

    2. Add a user by sending a POST request (replace `<YOUR_PORT>` with your actual port number, for example, `4321`):

       ```bash
       curl -X POST http://localhost:<YOUR_PORT>/{YOUR_APP_MOUNT_PATH}/api/users \
         -H "Content-Type: application/json" \
         -d '{"name": "Arthur Dent", "age": 33, "email": "arthur.dent@bbc.co.uk"}'
       ```

       A successful response returns the new user as JSON, for example:

       ```json
       {
         "id": 1,
         "name": "Arthur Dent",
         "age": 33,
         "email": "arthur.dent@bbc.co.uk"
       }
       ```

       Try adding more users with different data to populate your database.

    3. Retrieve all users by sending a GET request:
       ```bash
       curl http://localhost:<YOUR_PORT>/{YOUR_APP_MOUNT_PATH}/api/users
       ```
       You should see a list of users in the response.
  </Step>
</Steps>

## Deploy and view your app

When you deploy to Webflow Cloud, your database migrations are applied automatically and your remote database is updated. From here, you can connect to your database through your app’s endpoints, and any data you add will persist. You can also view and manage your data directly in the Webflow Cloud UI.

<Steps>
  <Step title="Deploy your app.">
    Use the Webflow CLI to trigger a new deployment of your app. Additionaly, you can commit and push your changes to your GitHub repository to trigger a new deployment as well.

    <CodeBlocks>
      ```bash title="Webflow CLI"
      webflow cloud deploy
      ```

      ```bash title="GitHub"
      git add .
      git commit -m "Add users table"
      git push
      ```
    </CodeBlocks>
  </Step>

  <Step title="View your app and database in Webflow Cloud">
    1. Open your project’s environment in Webflow Cloud.
    2. After your deployment completes, click the "Storage" tab in your environment.
       <Frame>
         <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/2ab4fecbc3e9a35cb90853ab6f598b60f62f65d5cb095ab660f60fc9b2c74ff1/products/webflow-cloud/pages/concepts/storing-data/assets/storage-sql-lite.png" />
       </Frame>
    3. Select the `DB` binding to view your database.
    4. You should see the `users_table`. For now, it will be empty, since all the previous changes were local. In the "Storage" tab, you can add and update users through the UI.

       <Frame>
         <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/29730530f2a03935c0930c5f7c7a4a8c5ac70f3d892e15408572a49717914399/products/webflow-cloud/pages/concepts/assets/database-viewer.png" alt="Database viewer in Webflow Cloud" />
       </Frame>

    <Tip title="Try calling your API routes">
      You can also try calling your API routes to add and retrieve users from your deployed app.

      ```bash
      curl -X POST https://<your-app-url>/<your-app-mount-path>/api/users \
      -H "Content-Type: application/json" \
      -d '{"name": "Arthur Dent", "age": 33, "email": "arthur.dent@bbc.co.uk"}'
      ```
    </Tip>
  </Step>
</Steps>

You’ve now added persistent storage to your Webflow Cloud app using SQLite and Drizzle ORM. You learned how to:

* Connect a SQLite database to your project
* Define and manage your schema in code
* Run and apply migrations
* Build API routes to add and retrieve data

## Next steps

Ready to build more? Check out related guides and resources to keep growing your app’s capabilities.

* Learn more about [SQLite in Webflow Cloud](/webflow-cloud/storing-data/sqlite)
* Learn about other [storage options in Webflow Cloud](/webflow-cloud/storing-data/overview)
* See examples for [adding authentication to your app](/webflow-cloud/examples)
