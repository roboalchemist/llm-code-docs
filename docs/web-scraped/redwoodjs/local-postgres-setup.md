# Source: https://docs.redwoodjs.com/docs/local-postgres-setup

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Local Postgres Setup]

[Version: 8.8]

On this page

<div>

# Local Postgres Setup

</div>

RedwoodJS uses a SQLite database by default. While SQLite makes local development easy, you\'re likely going to want to run the same database you use in production locally at some point. And since the odds of that database being Postgres are high, here\'s how to set up Postgres.

## Install Postgres[​](#install-postgres "Direct link to Install Postgres") 

### Mac[​](#mac "Direct link to Mac") 

If you\'re on a Mac, we recommend using Homebrew:

``` 
brew install postgresql@14
```

> **Install Postgres? I\'ve messed up my Postgres installation so many times, I wish I could just uninstall everything and start over!**
>
> We\'ve been there before. For those of you on a Mac, [this video](https://www.youtube.com/watch?v=1aybOgni7lI) is a great resource on how to wipe the various Postgres installs off your machine so you can get back to a blank slate. Obviously, warning! This resource will teach you how to wipe the various Postgres installs off your machine. Please only do it if you know you can!

### Windows and Other Platforms[​](#windows-and-other-platforms "Direct link to Windows and Other Platforms") 

If you\'re using another platform, see Prisma\'s [Data Guide](https://www.prisma.io/dataguide/postgresql/setting-up-a-local-postgresql-database?utm_source=redwoodjs_docs&utm_medium=docs) for detailed instructions on how to get up and running.

## Alternatives to local PostgreSQL Installation[​](#alternatives-to-local-postgresql-installation "Direct link to Alternatives to local PostgreSQL Installation") 

### Local Prisma Postgres[​](#local-prisma-postgres "Direct link to Local Prisma Postgres") 

For local development, you can use [local Prisma Postgres](https://www.prisma.io/docs/postgres/database/local-development?utm_source=redwoodjs_docs&utm_medium=docs) which runs a PostgreSQL-compatible database locally. This eliminates the need to install and manage PostgreSQL locally while maintaining full compatibility with production PostgreSQL databases.

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

For quick testing or prototyping, [Prisma Postgres](https://www.prisma.io/postgres?utm_source=redwoodjs_docs&utm_medium=docs) offers temporary production-ready databases that require no setup or accounts. Use [`npx create-db`](https://www.prisma.io/docs/postgres/introduction/npx-create-db?utm_source=redwoodjs_docs&utm_medium=docs) to create a database that\'s automatically deleted after 24 hours:

``` 
npx create-db@latest
```

This provides both Prisma ORM-optimized and standard PostgreSQL connection strings. You can also claim the database to make it permanent if needed.

## Creating a database[​](#creating-a-database "Direct link to Creating a database") 

If everything went well, then Postgres should be running and you should have a few commands at your disposal (namely, `psql`, `createdb`, and `dropdb`).

Check that Postgres is running with `brew services` (the `$(whoami)` bit in the code block below is just where your username should appear):

``` 
$ brew services
Name Status User Plist
postgresql started $(whoami) /Users/$(whoami)/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
```

If it\'s not started, start it with:

``` 
brew services start postgresql
```

Great. Now let\'s try running the PostgresQL interactive terminal, `psql`:

``` 
$ psql
```

You\'ll probably get an error like:

``` 
psql: error: FATAL: database $(whoami) does not exist
```

This is because `psql` tries to log you into a database of the same name as your user. But if you just installed Postgres, odds are that database doesn\'t exist.

Luckily it\'s super easy to create one using another of the commands you got, `createdb`:

``` 
$ createdb $(whoami)
```

Now try:

``` 
$ psql
psql (13.1)
Type "help" for help.

$(whoami)=#
```

If it worked, you should see a prompt like the one above---your username followed by `=#`. You\'re in the PostgreSQL interactive terminal! While we won\'t get into `psql`, here\'s a few the commands you should know:

-   `\q` --- quit (super important!)
-   `\l` --- list databases
-   `\?` --- get a list of commands

If you\'d rather not follow any of the advice here and create another Postgres user instead of a Postgres database, follow [this](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04#step-3-%E2%80%94-creating-a-new-role).

## Update the Prisma Schema[​](#update-the-prisma-schema "Direct link to Update the Prisma Schema") 

Tell Prisma to use a Postgres database instead of SQLite by updating the `provider` attribute in your `schema.prisma` file:

api/db/schema.prisma

``` 
datasource db 
```

> Note: If you run into a \"PrismaClientInitializationError\" then you may need to regenerate the prisma client using: `yarn rw prisma generate`

## Connect to Postgres[​](#connect-to-postgres "Direct link to Connect to Postgres") 

Add a `DATABASE_URL` to your `.env` file with the URL of the database you\'d like to use locally. The following example uses `redwoodblog_dev` for the database. It also has `postgres` setup as a superuser for ease of use.

``` 
DATABASE_URL="postgresql://postgres@localhost:5432/redwoodblog_dev?connection_limit=1"
```

Note the `connection_limit` parameter. This is [recommended by Prisma](https://www.prisma.io/docs/reference/tools-and-interfaces/prisma-client/deployment#recommended-connection-limit) when working with relational databases in a Serverless context. You should also append this parameter to your production `DATABASE_URL` when configuring your deployments.

### Local Test DB[​](#local-test-db "Direct link to Local Test DB") 

You should also set up a test database similarly by adding `TEST_DATABASE_URL` to your `.env` file.

``` 
TEST_DATABASE_URL="postgresql://postgres@localhost:5432/redwoodblog_test?connection_limit=1"
```

> Note: local postgres server will need manual start/stop \-- this is not handled automatically by RW CLI in a manner similar to sqlite

### Base URL and path[​](#base-url-and-path "Direct link to Base URL and path") 

Here is an example of the structure of the base URL and the path using placeholder values in uppercase letters:

``` 
postgresql://USER:PASSWORD@HOST:PORT/DATABASE
```

The following components make up the base URL of your database, they are always required:

Name

Placeholder

Description

Host

`HOST`

IP address/domain of your database server, e.g. `localhost`

Port

`PORT`

Port on which your database server is running, e.g. `5432`

User

`USER`

Name of your database user, e.g. `postgres`

Password

`PASSWORD`

password of your database user

Database

`DATABASE`

Name of the database you want to use, e.g. `redwoodblog_dev`

## Migrations[​](#migrations "Direct link to Migrations") 

Migrations are snapshots of your DB structure, which, when applied, manage the structure of both your local development DB and your production DB.

To create and apply a migration to the Postgres database specified in your `.env`, run the *migrate* command. (Did this return an error? If so, see \"Migrate from SQLite\...\" below.):

``` 
yarn redwood prisma migrate dev
```

### Migrate from SQLite to Postgres[​](#migrate-from-sqlite-to-postgres "Direct link to Migrate from SQLite to Postgres") 

If you\'ve already created migrations using SQLite, e.g. you have a migrations directory at `api/db/migrations`, follow this two-step process.

#### 1. Remove existing migrations[​](#1-remove-existing-migrations "Direct link to 1. Remove existing migrations") 

**For Linux and Mac OS** From your project root directory, run either command corresponding to your OS.

``` 
rm -rf api/db/migrations
```

**For Windows OS**

``` 
rmdir /s api\db\migrations
```

> Note: depending on your project configuration, your migrations may instead be located in `api/prisma/migrations`

#### 2. Create a new migration[​](#2-create-a-new-migration "Direct link to 2. Create a new migration") 

Run this command to create and apply a new migration to your local Postgres DB:

``` 
yarn redwood prisma migrate dev
```

## DB Management Tools[​](#db-management-tools "Direct link to DB Management Tools") 

Here are our recommendations in case you need a tool to manage your databases:

-   [TablePlus](https://tableplus.com/) (Mac, Windows)
-   [Beekeeper Studio](https://www.beekeeperstudio.io/) (Linux, Mac, Windows - Open Source)

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/local-postgres-setup.md)