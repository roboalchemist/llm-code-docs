# Source: https://docs.turso.tech/features/embedded-replicas/with-railway.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Turso + Railway

> Deploy a JavaScript/Rust app using [Turso embedded replicas](/features/embedded-replicas) to [Railway](https://railway.app/).

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/railway-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=c04df842dadd8d42cd24364580fbf7bf" alt="Koyeb banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/platforms/railway-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/railway-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=7a2da6f3ae7830cf5920606ab60414c1 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/railway-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=969fe3af1ec1097016c5cfa8db2ce858 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/railway-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=d687210faf0308b804c2fffa589258cb 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/railway-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=e890cc6aa90a2997267ba26c8e51ea80 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/railway-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=ac9e200a13dbcc2b57f3578461d639e3 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/platforms/railway-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=7292a312d2b6f479acae09d766c06458 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* [Install the Railway CLI](https://docs.railway.app/guides/cli#installing-the-cli)

<Steps>
  <Step title="Retrieve database credentials">
    You will need an existing database to continue. If you don't have one, [create one](/quickstart).

    <Snippet file="retrieve-database-credentials.mdx" />

    <Info>You will want to store these as environment variables.</Info>
  </Step>

  <Step title="Get application code">
    Fork and clone the following embedded replica project from GitHub locally:

    <CardGroup cols={2}>
      <Card title="My Expenses Tracker - (Elysia + Bun)" icon="github" href="https://github.com/tursodatabase/embedded-replicas-with-js">
        See the full source code
      </Card>

      <Card title="Web Traffic API - (Rust)" icon="github" href="https://github.com/tursodatabase/embedded-replicas-with-rust">
        See the full source code
      </Card>
    </CardGroup>
  </Step>

  <Step title="Create a new Railway project">
    Run the following command to create a new Railway project. Provide the project's name when prompted.

    ```sh  theme={null}
    railway init
    ```
  </Step>

  <Step title="Add a service to the Railway project">
    [Create a new empty service](https://docs.railway.app/guides/services#creating-a-service) on your Railway project to act as your app's deployment target.
  </Step>

  <Step title="Link application to service">
    Run the following command to list and select the service to link to your application:

    ```sh  theme={null}
    railway service
    ```
  </Step>

  <Step title="Add database credentials">
    Open the service on your Railway dashboard and add your Turso database Credentials.

    ```sh  theme={null}
    TURSO_DATABASE_URL=libsql://[db-name]-[github-username].turso.io
    TURSO_AUTH_TOKEN=...
    LOCAL_DB=file:local-db-name.db
    ```
  </Step>

  <Step title="Deploy">
    Run the following command to deploy your application:

    ```sh  theme={null}
    railway up
    ```

    <Info>
      Make sure you [expose your application to the internet](https://docs.railway.app/guides/public-networking) to make it accessible from the public network.
    </Info>

    <Warning>
      If you are on a free plan, you'll need to connect your Railway account to GitHub to have access to code deployments.
    </Warning>
  </Step>
</Steps>
