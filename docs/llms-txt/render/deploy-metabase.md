# Source: https://render.com/docs/deploy-metabase.md

# Deploy Metabase

[Metabase](https://github.com/metabase/metabase) is an easy, open-source way to derive insights from data:

- Let anyone on your team [ask questions](https://metabase.com/docs/latest/users-guide/04-asking-questions.html) without knowing SQL.
- Rich beautiful [dashboards](https://metabase.com/docs/latest/users-guide/06-sharing-answers.html) with auto refresh and fullscreen.
- SQL Mode for analysts and data pros.
- Create canonical [segments and metrics](https://metabase.com/docs/latest/administration-guide/07-segments-and-metrics.html) for your team to use.
- Subscribe to reports with [Slack or email](https://www.metabase.com/docs/latest/users-guide/dashboard-subscriptions.html).
- [Humanize data](https://metabase.com/docs/latest/administration-guide/03-metadata-editing.html) for your team by renaming, annotating and hiding fields.

[image: Metabase Product Screenshot]

You can deploy Metabase on Render in under 5 minutes. It is backed by Render's [fully-managed PostgreSQL](postgresql) and can be used to gain insights from any supported database including PostgreSQL, MySQL, Google Analytics, and MongoDB.

## One-Click Deploy

Click *Deploy to Render* below and follow the prompts to deploy Metabase on Render.

<deploy-to-render repo="https://github.com/render-examples/metabase">
</deploy-to-render>

## Manual Deploy

1. [Create](https://dashboard.render.com/new/database) a new PostgreSQL database on Render and copy the internal DB URL to use below.

> <strong>This is the database where Metabase stores its own data</strong>. You will configure a connection to your application database in Metabase after installation.

2. Fork [render-examples/metabase](https://github.com/render-examples/metabase) on GitHub.
3. Create a new *Web Service* on Render, and give Render permission to access your new repo.
4. Select `Docker` for the runtime, and add the following environment variable under the _Advanced_ section:

   | Key                    | Value                                                             |
   | ---------------------- | ----------------------------------------------------------------- |
   | `MB_DB_CONNECTION_URI` | The *internal database URL* for the database you created above. |

   You can optionally encrypt your Metabase database connection details by adding the `MB_ENCRYPTION_SECRET_KEY` environment variable as described in the [Metabase operations guide](https://www.metabase.com/docs/latest/databases/encrypting-details-at-rest).

5. We recommend selecting a Web Service instance type with *at least 1GB of RAM* for Metabase. If you have more than a small amount of test data, we recommend at least 2GB of RAM.

That's it! Metabase will be live on your Render URL as soon as the Docker build finishes.

Next, create a Metabase admin account and connect to your database using the [Metabase Setup Guide](https://metabase.com/docs/latest/setting-up-metabase.html). Soon everyone in your team will be uncovering data insights with your shiny Metabase instance on Render! 🙌

## Upgrading Metabase

When you first install Metabase, Render will use the latest stable version in the Dockerfile:

```dockerfile
FROM metabase/metabase:latest
```

To upgrade, simply trigger a manual deploy for Metabase in your Render Dashboard.

You can also use a specific version of Metabase in your Dockerfile:

```dockerfile
FROM metabase/metabase:v0.35.1
```

Commit and push your changes and Render will automatically upgrade and deploy your Metabase instance.