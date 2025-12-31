# Source: https://docs.redwoodjs.com/docs/how-to/test-in-github-actions

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Testing Redwood in GitHub actions]

[Version: 8.8]

On this page

<div>

# Testing Redwood in GitHub actions

</div>

A good testing strategy is important for any project. Redwood offers a few different types of tests that you can write to make your app more robust---to ship with confidence. In this guide we\'ll focus on how to run your Redwood tests in GitHub Actions, so you can test your app on every push or pull request.

We\'ll set up a tiny project with a few tests and a Postgres database that\'ll be created and used in every test run on GitHub. If you need to set up tests for an existing project, or if you want to write better tests, check out the (amazing) [Testing](/docs/testing) docs.

## Background[​](#background "Direct link to Background") 

Let\'s start by introducing some concepts and products that we\'ll use in this guide. Then we\'ll get to the code.

### Continuous Integration[​](#continuous-integration "Direct link to Continuous Integration") 

Continuous Integration (CI) is the practice of automatically running your tests on every push or pull request. This is a great way to catch bugs before they\'re merged into your main branch.

### Continuous Deployment[​](#continuous-deployment "Direct link to Continuous Deployment") 

Continuous Deployment (CD) is the practice of automatically deploying your app (and database in this case) to a server after every successful test run. This is a great way to make sure your app or database is always up to date.

### GitHub Actions and GitHub Secrets[​](#github-actions-and-github-secrets "Direct link to GitHub Actions and GitHub Secrets") 

GitHub Actions is a service that allows you to run a series of commands on a virtual machine. You can use it to run tests, deploy your app, or do anything else you may think of. It\'s free for public repositories and has a free tier for private ones. For more information, check out [GitHub Actions\' docs](https://docs.GitHub.com/en/actions).

GitHub Secrets is a way to store sensitive information like API keys or passwords needed by GitHub Actions. They are encrypted and only exposed to the GitHub Actions service. You can use them to pass sensitive information to your tests or deploy script. For more information, check out [GitHub Secrets\' docs](https://docs.GitHub.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository).

## How to run tests in GitHub Actions[​](#how-to-run-tests-in-github-actions "Direct link to How to run tests in GitHub Actions") 

All right, let\'s get to the code. In this how to, we\'ll focus on how to run your tests in GitHub Actions, but not how to write your tests (see the [Testing](/docs/testing) doc for that).

If you already have a project, you can skip to [4. Set up GitHub Actions](#4-set-up-GitHub-actions).

### 1. Create a Redwood app[​](#1-create-a-redwood-app "Direct link to 1. Create a Redwood app") 

Start by creating a Redwood app and `cd`ing into it:

``` 
yarn create redwood-app rw-testing-gh-actions
cd rw-testing-gh-actions
```

Then make sure everything is working:

``` 
yarn rw test
```

If it is, you should see something like this:

``` 
...

PASS api api/src/directives/requireAuth/requireAuth.test.ts
PASS api api/src/directives/skipAuth/skipAuth.test.ts

Test Suites: 2 passed, 2 total
Tests: 3 passed, 3 total
Snapshots: 0 total
Time: 1.669 s
Ran all test suites.

Watch Usage: Press w to show more.
```

### 2. Modify the Prisma schema[​](#2-modify-the-prisma-schema "Direct link to 2. Modify the Prisma schema") 

For the purpose of this how to, we\'ll use the `UserExample` model that comes with the Redwood app. We\'ll also change the database to Postgres since that\'s what we\'ll be using in our GitHub Actions.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]Make sure you have a Postgres instance ready to use

Here\'s a handy guide for how to [set it up locally](/docs/local-postgres-setup). We\'ll need the connection string so our Redwood app knows where to store the data

On to the changes. Modify your `schema.prisma` file to look like this:

api/db/prisma.schema

``` 
datasource db 

generator client 

model UserExample 
```

Then add your connection strings to your `.env` file:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

Make sure you don\'t commit this file to your repo since it contains sensitive information.

``` 
DATABASE_URL=postgres://postgres:postgres@localhost:54322/postgres
TEST_DATABASE_URL=postgres://postgres:postgres@localhost:54322/postgres
```

You need one connection string for your development database and one for your test database. Read more about it in the testing doc\'s [The Test Database](/docs/testing#the-test-database) section.

Next, navigate to the `scripts/seed.ts` file. Uncomment the contents of the array that contains the \"fake\" users. We\'ll also use the `createMany` method for inserting records in the database so we can skip the duplicates (see the [Prisma docs](https://www.prisma.io/docs/reference/api-reference/prisma-client-reference#createmany) for more info). When you\'re all done, it should look like this:

scripts/seed.ts

``` 
    ...

    const data: Prisma.UserExampleCreateArgs['data'][] = [
      // To try this example data with the UserExample model in schema.prisma,
      // uncomment the lines below and run 'yarn rw prisma migrate dev'
      //
      ,
      ,
      ,
      ,
    ]
    console.log(
      "\nUsing the default './scripts/seed.' template\nEdit the file to add seed data\n"
    )

    // Note: if using PostgreSQL, using `createMany` to insert multiple records is much faster
    // @see: https://www.prisma.io/docs/reference/api-reference/prisma-client-reference#createmany
    Promise.all(
      //
      // Change to match your data model and seeding needs
      //
      data.map(async (data: Prisma.UserExampleCreateArgs['data']) => )
        console.log(record)
      })
    )

    ...
```

Finally, migrate your database:

``` 
yarn rw prisma migrate dev --name init
```

### 3. Generate the UserExample scaffold[​](#3-generate-the-userexample-scaffold "Direct link to 3. Generate the UserExample scaffold") 

We need some real tests to work with. Scaffolding out the `UserExample` model gives us everything we need to create \"users\" in our app, including some of the services tests which interact with our test database:

``` 
yarn rw g scaffold UserExample
```

Make sure everything is still working:

``` 
yarn rw test
```

You should see something like this:

``` 
PASS web web/src/lib/formatters.test.tsx
PASS api api/src/services/userExamples/userExamples.test.ts

Test Suites: 2 passed, 2 total
Tests: 21 passed, 21 total
Snapshots: 0 total
Time: 3.587 s
Ran all test suites related to changed files in 2 projects.
```

### 4. Set up GitHub Actions[​](#4-set-up-github-actions "Direct link to 4. Set up GitHub Actions") 

Create a new file in the `.github/workflows` directory (create those directories if they don\'t exist) called `ci.yml` and add the following:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

This action only runs when the `main` branch is updated, but you can configure it to run on any other branch.

.github/workflows/ci.yml

``` 
name: Redwood CI

on:
  push:
    branches: ['main']
  pull_request:
    branches: ['main']

env:
  DATABASE_URL: postgres://postgres:postgres@localhost:5432/postgres
  TEST_DATABASE_URL: postgres://postgres:postgres@localhost:5432/postgres

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [20.x]
        # See supported Node.js release schedule at https://nodejs.org/en/about/releases/

    services:
      # Label used to access the service container
      postgres:
        # Docker Hub image
        image: postgres
        # Provide the password for postgres
        env:
          POSTGRES_PASSWORD: postgres
        # Set health checks to wait until postgres has started
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          # Maps tcp port 5432 on service container to the host
          - 5432:5432

    steps:
      - uses: actions/checkout@v4
      - name: Use Node.js $}
        uses: actions/setup-node@v4
        with:
          node-version: $}
      - run: corepack enable
      # install all the dependencies
      - run: yarn install
      # build the redwood app
      - run: yarn rw build
      # run the api tests
      - run: yarn rw test api --no-watch
      # run the web tests
      - run: yarn rw test web --no-watch
```

Now push your changes to the `main` branch on GitHub; the \"Redwood CI\" action we just made will run like this:

![ci-results-1](https://user-images.GitHubusercontent.com/14810250/202825732-c7d77929-58ff-4ad5-9072-48e4403471c9.png)

1.  Set up the job (\"build\")
2.  Initialize the containers and create the postgres instance
3.  Checkout the code
4.  Set up Node.js
5.  Install the Redwood app\'s dependencies
6.  Build the Redwood app
7.  Run the api tests
8.  Run the web tests
9.  Clean up the environment

At this point, if all is well, you may start feeling the joy of automated tests! You push a commit, the Action runs, your tests pass, and you get a green checkmark. To savor this moment, consider updating one of your unit tests, making it fail. Push again. Watch it fail. Fix it. Push again. Watch it pass. Repeat and enjoy.

### 5. Set up CI on pull requests only[​](#5-set-up-ci-on-pull-requests-only "Direct link to 5. Set up CI on pull requests only") 

We want tests to run on every pull request so we can make sure that our code is working as expected. Update the `ci.yml` file by removing the `push` event. The first lines should look like this:

.github/workflows/ci.yml

``` 
name: Redwood CI for Pull Requests

on:
  pull_request:
    branches: ['main']
```

Now, if you open or push to a pull request, this action will run and you\'ll see something like this:

![ci-pr-1](https://user-images.GitHubusercontent.com/14810250/202825767-c7f23b24-e311-4a70-bf50-fbad40a6abee.png)

Once the action is done running, you can see the results in the \"Conversation\" tab:

![ci-pr-2](https://user-images.GitHubusercontent.com/14810250/202825772-93c8fe50-6b91-4048-882b-21497d47e211.png)

### 6. Deploy the database changes to an actual database[​](#6-deploy-the-database-changes-to-an-actual-database "Direct link to 6. Deploy the database changes to an actual database") 

Now for the CD---we want to use another action to deploy the database changes to an actual database, so we can automatically deploy the latest and greatest to a real environment. In this action we\'ll run the tests one more time against the local database, then deploy the database migrations to the external database.

Create a new file in the `.github/workflows` directory called `cd.yml` and add the following:

.github/workflows/cd.yml

``` 
name: Redwood CD for database deployment

on:
  push:
    branches: ['main']

env:
  DATABASE_URL: postgres://postgres:postgres@localhost:5432/postgres
  TEST_DATABASE_URL: postgres://postgres:postgres@localhost:5432/postgres

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [20.x]
        # See supported Node.js release schedule at https://nodejs.org/en/about/releases/

    services:
      # Label used to access the service container
      postgres:
        # Docker Hub image
        image: postgres
        # Provide the password for postgres
        env:
          POSTGRES_PASSWORD: postgres
        # Set health checks to wait until postgres has started
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          # Maps tcp port 5432 on service container to the host
          - 5432:5432

    steps:
      - uses: actions/checkout@v4
      - name: Use Node.js $}
        uses: actions/setup-node@v4
        with:
          node-version: $}
      - run: corepack enable
      # install all the dependencies
      - run: yarn install
      # build the redwood app
      - run: yarn rw build
      # run the api tests
      - run: yarn rw test api --no-watch
      # run the web tests
      - run: yarn rw test web --no-watch
      # run migrations on the actual database
      - run: yarn rw prisma migrate deploy
      # run seed script in the actual db
      - run: yarn rw prisma db seed
```

The main changes are:

-   We only run the action on push events to the `main` branch
-   We run the migrations and seed scripts after the tests

### 7. Set up GitHub Secrets[​](#7-set-up-github-secrets "Direct link to 7. Set up GitHub Secrets") 

Because you\'re using an actual Postgres instance in your action, you need to set up the secrets for the database connection so that the username and password stay secret.

Go to the \"Settings\" tab in your GitHub repo and click \"Secrets\", then \"Actions\", then \"New repository secret\". In the name field, type `DATABASE_URL`. In the value field, put the actual secret---something like this:

``` 
postgres://[USER_NAME]:[PASSWORD]@[HOST]:[PORT]/postgres
```

When you\'re done, click \"Add secret\". This creates a new secret that you can use in your GitHub Actions. In this case, it species the connection string for the database we\'ll deploy changes to.

You can use the secret in your GitHub Actions by using the `$}` syntax:

``` 
env:
  DATABASE_URL: $}
```

Now you can merge the PR and the database changes will be tested, then deployed to the actual database.

What\'s next? It is up to you---refine and streamline!

As you consider automating your project workflows, keep the following wise philosophical observation in mind\...

> Civilization advances by extending the number of important operations we can perform without thinking.
>
> ---Alfred North Whitehead

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/test-in-github-actions.md)