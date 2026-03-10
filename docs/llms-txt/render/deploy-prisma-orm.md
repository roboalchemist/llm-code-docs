# Source: https://render.com/docs/deploy-prisma-orm.md

# Deploy a Node.js app with Prisma ORM and PostgreSQL


> This tutorial is featured by [Prisma](https://www.prisma.io/), a Render partner.

Deploy a Node.js application that uses Prisma ORM together with a Render PostgreSQL database.

## Deploy the example

In this tutorial, you'll learn how to:

1. Create a PostgreSQL database
1. Deploy a Node.js app that uses Prisma ORM
1. Connect the Node.js app to the PostgreSQL database
1. Specify a Pre-Deploy Command in Render to execute the database migrations defined by Prisma ORM
1. Seed the database with example data using the seeding functionality in Prisma ORM

## About Prisma ORM

Prisma ORM is an [open-source](https://github.com/prisma/prisma) next-generation ORM for Node.js & TypeScript.

Prisma ORM lets you define your data model declaratively in a schema file. Here's an example schema that defines two entities, `User` and `Post`:

```
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

model Post {
  id        Int     @id @default(autoincrement())
  title     String
  content   String?
  published Boolean @default(false)
  author    User?   @relation(fields: [authorId], references: [id])
  authorId  Int?
}

model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[]
}
```

Based on this schema file, Prisma ORM can:

- Autogenerate database migrations that create database tables for `User` and `Post`
- Help you track and run these database migrations
- Generate client code that lets you query your database using JavasScript or TypeScript. For example, you can use the following code snippet to fetch all users from the database, along with their posts:
  ```javascript
  const allUsers = await prisma.user.findMany({
    include: { posts: true },
  })
  ```

You can use Prisma ORM together with PostgreSQL, SQLite, MongoDB, and many other databases.

See the [Prisma ORM docs](https://www.prisma.io/docs/orm/overview/introduction/what-is-prisma) to learn more.