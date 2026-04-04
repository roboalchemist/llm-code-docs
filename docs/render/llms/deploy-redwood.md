# Source: https://render.com/docs/deploy-redwood.md

# Deploy RedwoodJS on Render

[RedwoodJS](https://redwoodjs.com/) is a full-stack framework for building and deploying JAMstack web applications. It consists of a React frontend and a Node backend that exposes a GraphQL API. Redwood uses [Prisma](https://www.prisma.io/) to communicate with a database such as SQLite or PostgreSQL.

Check out our demo Redwood app running on Render [here](https://redwoodjs-web.onrender.com/).

## Getting started

1. Create a new Redwood project by running `yarn create redwood-app my-redwood-app` in your terminal or by forking our [Redwood demo](https://redwoodjs-web.onrender.com/) from [https://github.com/render-examples/redwoodjs](https://github.com/render-examples/redwoodjs).

2. Read the [Redwood Tutorial](https://learn.redwoodjs.com/docs/tutorial/welcome-to-redwood/) and [Docs](https://redwoodjs.com/docs/introduction) to learn how to create your custom Redwood application.

## Preparing for deployment

Run the following command to configure your project for deployment to Render:

`yarn rw setup deploy render`

This command will:

- Create a starter Blueprint Spec for [infrastructure as code](infrastructure-as-code).

- Define a health check endpoint at `api/src/functions/healthz.js`.

By default, this command will configure your project to use a Postgres database that is fully managed by Render. See [Database Selection](#database-selection) for more information.

Redwood typically uses an `.nvmrc` file to control the Node version. With Render, the Node version is controlled with the `NODE_VERSION` environment variable in the generated `render.yaml` file.

See [Specifying a Node Version](node-version) if you need to customize the version of Node.js used for your app.

## Deployment

Once your Redwood project is ready for deployment to Render:

1. Create a [Render account](https://dashboard.render.com/register).

2. Create your services from a Blueprint spec [https://dashboard.render.com/select-repo?type=iac](https://dashboard.render.com/select-repo?type=iac) by linking your GitHub/GitLab/Bitbucket account and selecting the repository for your Redwood project.

3. Review and apply the changes.

4. After deployment:

   - Navigate to the API service and obtain your `onrender.com` service URL.

   - Navigate to the `web` static site and click on *Redirects/Rewrites*.

   - Create a Rewrite rule pointing to the API service URL.

   - Click *Save Changes*.

[image: Redwood Rewrite]

5. In your `render.yaml` file, replace the rewrite rule destination with the `onrender.com` service URL. This ensures that the rewrite rule will not change on subsequent deployments.

## Database Selection

By default, the setup command configures your project to use PostgreSQL, which is recommended for production workloads. Render also supports deployments that use SQLite or any of the [databases supported by Primsa](https://www.prisma.io/docs/reference/database-reference/supported-databases).

Use the `-d` flag to override the default value (`postgres`):

- `yarn rw setup deploy render -d sqlite`
- `yarn rw setup deploy render -d none`

Before running the command, check that the data source provider in `api/db/schema.prisma` is correct. Otherwise:

1. Correct the data source provider.
2. Delete the migrations folder at `api/db/migrations/`.
3. Run the following command: `yarn redwood prisma migrate dev` to run migrations for the new provider.

### PostgreSQL (most reliable)

Render's fully-managed PostgreSQL offering includes *encryption at rest, automated backups, and expandable SSD storage.*

[Learn more.](postgresql)

### SQLite (lowest cost)

SQLite allows you to run a small and fast SQL database engine that writes directly to disk on your API server. The advantage of SQLite is fast and easy local development, which translates to a low-cost cloud deployment.

See [Appropriate Uses for SQLite](https://www.sqlite.org/whentouse.html) for more information.

> Adding a disk to a service prevents <a href="https://render.com/docs/deploys#zero-downtime-deploys">zero-downtime deploys</a>.

### Externally Hosted

To use an externally hosted database, add your connection URL as an environment variable named `DATABASE_URL`.