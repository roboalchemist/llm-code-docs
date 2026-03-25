# Source: https://docs.redwoodjs.com/docs/connection-pooling

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Connection Pooling]

[Version: 8.8]

On this page

<div>

# Connection Pooling

</div>

> ⚠ **Work in Progress** ⚠️
>
> There\'s more to document here. In the meantime, you can check our [community forum](https://community.redwoodjs.com/search?q=connection%20pooling) for answers.
>
> Want to contribute? Redwood welcomes contributions and loves helping people become contributors. You can edit this doc [here](https://github.com/redwoodjs/redwoodjs.com/blob/main/docs/connectionPooling.md). If you have any questions, just ask for help! We\'re active on the [forums](https://community.redwoodjs.com/c/contributing/9) and on [discord](https://discord.com/channels/679514959968993311/747258086569541703).

Production Redwood apps should enable connection pooling in order to properly scale with your Serverless functions.

## Prisma Postgres[​](#prisma-postgres "Direct link to Prisma Postgres") 

[Prisma Postgres](https://www.prisma.io/docs/postgres/introduction/overview?utm_source=redwoodjs_docs&utm_medium=docs) is a managed PostgreSQL database service that includes:

-   **Built-in connection pooling**: No need to configure external pooling services
-   **Global caching**: Query-level caching with TTL and Stale-While-Revalidate strategies
-   **Serverless optimization**: Designed specifically for serverless and edge applications
-   **Easy setup**: Get started in minutes with minimal configuration

Prisma Postgres supports schema migrations and queries via Prisma ORM, and automatically handles connection pooling and caching.

To get started with Prisma Postgres, visit the [Prisma Postgres documentation](https://www.prisma.io/docs/postgres/introduction/overview?utm_source=redwoodjs_docs&utm_medium=docs).

### Local Prisma Postgres[​](#local-prisma-postgres "Direct link to Local Prisma Postgres") 

For local development, you can use [local Prisma Postgres](https://www.prisma.io/docs/postgres/database/local-development?utm_source=redwoodjs_docs&utm_medium=docs) which runs a PostgreSQL-compatible database locally. This eliminates the need to install and manage PostgreSQL locally while maintaining full compatibility with production PostgreSQL databases.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

To use Local Prisma Postgres, you do not need to create an account or install PostgreSQL locally.

First, update your Prisma schema to use PostgreSQL as the provider:

api/db/schema.prisma

``` 
datasource db 
```

Start the local Prisma Postgres server:

``` 
npx prisma dev
```

The server will start and display connection options. Press `t` to get the TCP connection URL for standard PostgreSQL connections, or press `h` if you\'re planning to use Prisma Postgres in production (which requires the [Prisma Client extension](https://www.prisma.io/docs/postgres/introduction/overview#using-the-client-extension-for-prisma-accelerate-required)).

If you\'re using any other provider for PostgreSQL, use the TCP connection URL in your `.env` file:

``` 
DATABASE_URL="postgresql://localhost:54322/main"
```

Keep the server running while performing migrations and using the database for local development.

### Temporary Prisma Postgres database[​](#temporary-prisma-postgres-database "Direct link to Temporary Prisma Postgres database") 

For quick testing or prototyping, [Prisma Postgres](https://www.prisma.io/postgres) offers temporary production-ready databases that also requires no setup or accounts. Use [`npx create-db`](https://www.prisma.io/docs/postgres/introduction/npx-create-db?utm_source=redwoodjs_docs&utm_medium=docs) to create a database that\'s automatically deleted after 24 hours:

``` 
npx create-db@latest
```

This provides both Prisma ORM-optimized and standard PostgreSQL connection strings. You can also claim the database to make it permanent if needed.

## Prisma & PgBouncer[​](#prisma--pgbouncer "Direct link to Prisma & PgBouncer") 

PgBouncer holds a connection pool to the database and proxies incoming client connections by sitting between Prisma Client and the database. This reduces the number of processes a database has to handle at any given time. PgBouncer passes on a limited number of connections to the database and queues additional connections for delivery when space becomes available.

To use Prisma Client with PgBouncer from a serverless function, add the `?pgbouncer=true` flag to the PostgreSQL connection URL:

``` 
postgresql://USER:PASSWORD@HOST:PORT/DATABASE?pgbouncer=true
```

Typically, your PgBouncer port will be 6543 which is different from the Postgres default of 5432.

> Note that since Prisma Migrate uses database transactions to check out the current state of the database and the migrations table, if you attempt to run Prisma Migrate commands in any environment that uses PgBouncer for connection pooling, you might see an error.
>
> To work around this issue, you must connect directly to the database rather than going through PgBouncer when migrating.

For more information on Prisma and PgBouncer, please refer to Prisma\'s Guide on [Configuring Prisma Client with PgBouncer](https://www.prisma.io/docs/guides/performance-and-optimization/connection-management/configure-pg-bouncer).

## Supabase[​](#supabase "Direct link to Supabase") 

For Postgres running on [Supabase](https://supabase.io) see: [PgBouncer is now available in Supabase](https://supabase.io/blog/2021/04/02/supabase-pgbouncer#using-connection-pooling-in-supabase).

All new Supabase projects include connection pooling using [PgBouncer](https://www.pgbouncer.org/).

We recommend that you connect to your Supabase Postgres instance using SSL which you can do by setting `sslmode` to `require` on the connection string:

``` 
// not pooled typically uses port 5432
postgresql://postgres:mydb.supabase.co:5432/postgres?sslmode=require
// pooled typically uses port 6543
postgresql://postgres:mydb.supabase.co:6543/postgres?sslmode=require&pgbouncer=true
```

## Heroku[​](#heroku "Direct link to Heroku") 

For Postgres, see [Postgres Connection Pooling](https://devcenter.heroku.com/articles/postgres-connection-pooling).

Heroku does not officially support MySQL.

## Digital Ocean[​](#digital-ocean "Direct link to Digital Ocean") 

For Postgres, see [How to Manage Connection Pools](https://www.digitalocean.com/docs/databases/postgresql/how-to/manage-connection-pools)

To run migrations through a connection pool, you\'re required to append connection parameters to your `DATABASE_URL`. Prisma needs to know to use pgbouncer (which is part of Digital Ocean\'s connection pool). If omitted, you may receive the following error:

``` 
Error: Migration engine error:
db error: ERROR: prepared statement "s0" already exists
```

To resolve this, use the following structure in your `DATABASE_URL`:

``` 
<YOUR_CONNECTION_POOL_URL>:25061/defaultdb?connection_limit=3&sslmode=require&pgbouncer=true&connect_timeout=10&pool_timeout=30
```

Here\'s a couple more things to be aware of:

-   When using a Digital Ocean connection pool, you\'ll have multiple ports available. Typically the direct connection (without connection pooling) is on port `25060` and the connection through pgbouncer is served through port `25061`. Make sure you connect to your connection pool on port `25061`
-   Adjust the `connection_limit`. Clusters provide 25 connections per 1 GB of RAM. Three connections per cluster are reserved for maintenance, and all remaining connections can be allocated to connection pools
-   Both `pgbouncer=true` and `pool_timeout=30` are required to deploy successfully through your connection pool

Connection Pooling for MySQL is not yet supported.

## AWS[​](#aws "Direct link to AWS") 

Use [Amazon RDS Proxy](https://aws.amazon.com/rds/proxy) for MySQL or PostgreSQL.

From the [AWS Docs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html#rds-proxy.limitations):

> Your RDS Proxy must be in the same VPC as the database. The proxy can\'t be publicly accessible.

Because of this limitation, with out-of-the-box configuration, you can only use RDS Proxy if you\'re deploying your Lambda Functions to the same AWS account. Alternatively, you can use RDS directly, but you might require larger instances to handle your production traffic and the number of concurrent connections.

## Why Connection Pooling?[​](#why-connection-pooling "Direct link to Why Connection Pooling?") 

Relational databases have a maximum number of concurrent client connections.

-   Postgres allows 100 by default
-   MySQL allows 151 by default

In a traditional server environment, you would need a large amount of traffic (and therefore web servers) to exhaust these connections, since each web server instance typically leverages a single connection.

In a Serverless environment, each function connects directly to the database, which can exhaust limits quickly. To prevent connection errors, you should add a connection pooling service in front of your database. Think of it as a load balancer.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/connection-pooling.md)