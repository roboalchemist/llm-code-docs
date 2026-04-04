# Source: https://planetscale.com/docs/vitess/tutorials/using-planetscale-with-prisma.md

# Using PlanetScale with Prisma

> [Prisma](https://www.prisma.io/) ORM provides type-safe database access through an intuitive API, eliminating the need to write SQL queries manually.

Prisma and PlanetScale together offer a powerful workflow. Prisma handles the object-relational mapping with full type safety and intuitive data modeling, while PlanetScale provides horizontal scaling, branching workflows, and zero-downtime schema changes, making it an ideal stack for building modern, scalable applications.

This guide covers how to use Prisma and PlanetScale together, including how to:

* Create a database with PlanetScale
* Integrate it with Prisma
* Use additional features like sharding and the serverless driver

If you don't already have an application set up with Prisma, but want to test how it works with PlanetScale, we recommend grabbing a sample application from [Prisma's examples repository](https://github.com/prisma/prisma-examples/tree/latest/orm).

## Set up your PlanetScale database

First, set up your PlanetScale database.

<Steps>
  <Step>
    Sign in to your PlanetScale account
  </Step>

  <Step>
    Click "Create a database"
  </Step>

  <Step>
    Give your database a name
  </Step>

  <Step>
    Select your preferred region
  </Step>

  <Step>
    Choose cluster and storage size
  </Step>

  <Step>
    Click "Create database"
  </Step>
</Steps>

Your database will deploy with an initial production branch, `main`.

### Create a password

After the database is created, you'll be prompted to generate credentials for it. You can come back to this later if needed.

<Steps>
  <Step>
    Give your password a name or leave the default
  </Step>

  <Step>
    Select a [password role](/docs/vitess/security/password-roles). We recommend `Admin` for your default password.
  </Step>

  <Step>
    Click "Create password"
  </Step>

  <Step>
    Select "Prisma" for "Select your language or framework"
  </Step>

  <Step>
    Do not navigate away from this page. The next section covers where to paste these credentials in your Prisma app. If you close without copying, you can regenerate new credentials.
  </Step>
</Steps>

## Connect to PlanetScale in your application

Next, add your database credentials to your Prisma application. If you are migrating an existing database to PlanetScale, you can test the PlanetScale/Prisma integration locally or in staging first. Once you're ready to migrate the database from your existing provider, refer to our no downtime [migration guides](/docs/vitess/imports/database-imports).

To connect PlanetScale to your Prisma application:

<Steps>
  <Step>
    Follow the steps in the above section if you navigated away from the page previously
  </Step>

  <Step>
    Update your `prisma/schema.prisma` file with the following:

    ```js  theme={null}
    datasource db {
      provider     = "mysql"
      url          = env("DATABASE_URL")
      relationMode = "prisma"
    }
    ```
  </Step>

  <Step>
    Update the `DATABASE_URL` value in your `.env` file with the value provided to you when you created a new password in the PlanetScale dashboard. It should look like this:

    ```
    DATABASE_URL='mysql://<USERNAME>:<PASSWORD>@aws.connect.psdb.cloud/<DATABASE>?sslaccept=strict'
    ```
  </Step>
</Steps>

## Foreign key constraints

PlanetScale does not enable foreign key constraints by default. If you are not using foreign key constraints to enforce referential integrity at the database level, integrating with Prisma will still work, but it requires a couple additional steps (detailed below).

If you do plan to use foreign key constraints, enable them on your PlanetScale database settings page.

<Steps>
  <Step>
    In your database dashboard, go to "Settings"
  </Step>

  <Step>
    Enable "Foreign key constraints"
  </Step>

  <Step>
    Save your changes
  </Step>
</Steps>

### Using Prisma without foreign key constraints

If you are not using foreign key constraints, you can use Prisma's [`relationMode`](https://www.prisma.io/docs/orm/prisma-schema/data-model/relations/relation-mode) to emulate relations.

You need to update `datasource db` in your `schema.prisma` file to include `relationMode = "prisma"`:

```
datasource db {
  provider     = "mysql"
  url          = env("DATABASE_URL")
  relationMode = "prisma"
}
```

When emulating relations, you also need to manually create dedicated indexes on foreign keys to avoid performance issues. For example, if you have `Post` and `Comment` tables, where the `Comment` table references a `post`, you need to add an index to your `Post` model:

```js  theme={null}
model Post {
  id       Int       @id @default(autoincrement())
  title    String
  content  String
  likes    Int       @default(0)
  comments Comment[]
}

model Comment {
  id      Int    @id @default(autoincrement())
  comment String
  postId  Int
  post    Post   @relation(fields: [postId], references: [id], onDelete: Cascade)

  @@index([postId]) // manually created index
}
```

You can learn more about how to do this in Prisma in their [Emulating relations documentation](https://www.prisma.io/docs/orm/overview/databases/planetscale#option-1-emulate-relations-in-prisma-client).

## Push your Prisma schema to PlanetScale

Push your schema to your PlanetScale branch with:

```bash  theme={null}
npx prisma db push
```

The recommended workflow with using Prisma alongside PlanetScale is to use `prisma db push` instead of `prisma migrate`. You can read more about [`prisma db push` here](https://www.prisma.io/docs/orm/reference/prisma-cli-reference#db-push).

Your PlanetScale database schema now matches the Prisma schema you configured in `prisma/schema.prisma`. To confirm this, go to your PlanetScale dashboard, click "Branches", and select the branch you generated credentials for. You should see your schema.

## Using the PlanetScale serverless driver with Prisma

The [PlanetScale serverless driver](/docs/vitess/tutorials/planetscale-serverless-driver) allows you to execute queries over HTTP. You can use it with Prisma ORM via the @prisma/adapter-planetscale driver adapter. This adapter is available in Preview from Prisma ORM versions 5.4.2 and later.

<Steps>
  <Step>
    Enable the `driverAdapters` Preview feature in your Prisma schema:

    ```js  theme={null}
    generator client {
      provider        = "prisma-client-js"
      previewFeatures = ["driverAdapters"]
    }
    ```
  </Step>

  <Step>
    Generate Prisma Client:

    ```bash  theme={null}
    npx prisma generate
    ```
  </Step>

  <Step>
    If you're not already using a direct connection string, update your host to `aws.connect.psdb.cloud` or `gcp.connect.psdb.cloud`, depending on your chosen region.
  </Step>

  <Step>
    Install the Prisma `adapter-planetscale` and PlanetScale serverless driver packages:

    ```bash  theme={null}
    npm install @prisma/adapter-planetscale @planetscale/database undici
    ```
  </Step>

  <Step>
    Configure your Prisma Client with the adapter:

    ```js  theme={null}
    import { PrismaPlanetScale } from '@prisma/adapter-planetscale'
    import { PrismaClient } from '@prisma/client'
    import dotenv from 'dotenv'
    import { fetch as undiciFetch } from 'undici'

    dotenv.config()
    const connectionString = `${process.env.DATABASE_URL}`

    const adapter = new PrismaPlanetScale({ url: connectionString, fetch: undiciFetch })
    const prisma = new PrismaClient({ adapter })
    ```
  </Step>
</Steps>

For more information, see the [Prisma documentation](https://www.prisma.io/docs/orm/overview/databases/planetscale#how-to-use-the-planetscale-serverless-driver-with-prisma-orm-preview).

## Sharding with PlanetScale and Prisma

If you are using a [sharded database](/docs/vitess/sharding) with PlanetScale, Prisma supports defining shard keys in your Prisma schema. This is currently available as a [Preview](https://www.prisma.io/docs/orm/more/releases#preview) feature in Prisma as of [v6.10.0](https://github.com/prisma/prisma/releases/tag/6.10.0).

To use shard key attributes, specify the `shardKeys` Preview feature on your Prisma generator in `schema.prisma`:

```prisma  theme={null}
generator client {
  provider        = "prisma-client-js"
  previewFeatures = ["shardKeys"]
}
```

This allows you to use `@shardKey` and `@@shardKey` attributes.

* `@shardKey` — Used to define a single-column shard key
* `@@shardKey` — Used to define a multi-column shard key

For example, if you have a shard key on your `region` column in your `User` database, you can define that in your Prisma model with:

```js  theme={null}
model User {
  id     String @default(uuid())
  region String @shardKey
}
```

## Next steps

* Make safe schema changes with [branching and deploy requests](/docs/vitess/schema-changes/branching)
* Explore [PlanetScale Insights](/docs/vitess/monitoring/query-insights) for performance monitoring
* Learn how to [target your replicas](/docs/vitess/scaling/replicas)
* Explore our [migration guides](/docs/vitess/imports/database-imports)
* Enable [PlanetScale vectors](/docs/vitess/vectors)
* Implement [read replicas](/docs/vitess/scaling/replicas) for scale
* Join the [PlanetScale Discord](https://discord.gg/planetscale) community

## Additional resources

<Columns cols={2}>
  <Card title="Prisma Documentation" icon="file-lines" horizontal href="https://www.prisma.io/docs" />

  <Card title="Prisma + PlanetScale Best Practices" icon="file-lines" horizontal href="https://www.prisma.io/docs/orm/overview/databases/planetscale" />

  <Card title="PlanetScale Support" icon="envelope" horizontal href="https://docs/support.planetscale.com" />

  <Card title="Foreign key constraints support" icon="file-lines" horizontal href="/docs/vitess/foreign-key-constraints" />
</Columns>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt