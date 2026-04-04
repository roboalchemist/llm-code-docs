# Source: https://render.com/docs/postgresql-connection-pooling.md

# Render Postgres Connection Pooling

Render Postgres databases support a limited number of simultaneous direct connections. If your database is approaching this limit, you can set up *connection pooling* on Render using [PgBouncer](https://www.pgbouncer.org/).

Using this setup, your other services connect to your PgBouncer instance instead of connecting directly to your database. PgBouncer reuses its pool of active database connections to serve queries from any number of different services.

## Setup

You can deploy PgBouncer on Render either by [declaring its configuration](infrastructure-as-code) in a `render.yaml` blueprint file, or by manually configuring a private service from your dashboard. Both options are covered below.

### Deploying with a `render.yaml` blueprint

1. Create a file named `render.yaml` in the root of a Git repository. This file describes your PgBouncer instance, along with the database it serves:

   ```yaml
   databases:
     - name: mysite
       databaseName: mysite
       user: mysite

    services:
    - type: pserv
      name: pgbouncer
      runtime: docker
      plan: standard
      repo: https://github.com/render-oss/docker-pgbouncer
      envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: mysite
          property: connectionString
      - key: POOL_MODE
        value: transaction
      - key: SERVER_RESET_QUERY
        value: DISCARD ALL
      - key: MAX_CLIENT_CONN
        value: 500
      - key: DEFAULT_POOL_SIZE
        value: 50
   ```

2. Commit your changes and push them to GitHub/GitLab/Bitbucket.

3. In the Render Dashboard, go to the [Blueprints](https://dashboard.render.com/blueprints) page and click *New Blueprint Instance*. Select the repository with the blueprint file (give Render permission to access it if you haven't already) and click *Approve* on the next screen.

That's it! Render creates your database and PgBouncer instance.

You can navigate to your new `pgbouncer` service in the dashboard to find the URL that your applications should connect to. You can connect using the internal connection string from your database, replacing the database host with internal hostname of your PgBouncer instance `postgresql://USER:PASSWORD@PGBOUNCER_HOST:PORT/DATABASE`.

### Creating services from the dashboard

1. Create a new [Render Postgres database](postgresql). Note your database's *internal database URL* (you'll need it in a later step).

2. Create a new *Private Service* and point it to Render's PgBouncer Docker Image: `https://github.com/render-oss/docker-pgbouncer`

3. Set the private service's *Language* field to `Docker`.

4. Add the following environment variables to the private service:

   | Key                  | Value                                                            |
   | -------------------- | ---------------------------------------------------------------- |
   | `DATABASE_URL`       | The *internal database URL* for the database you created above |
   | `POOL_MODE `         | `transaction`                                                    |
   | `SERVER_RESET_QUERY` | `DISCARD ALL`                                                    |
   | `MAX_CLIENT_CONN`    | `500`                                                            |
   | `DEFAULT_POOL_SIZE`  | `50`                                                             |

That's it! Save your private service to deploy your PgBouncer instance on Render.