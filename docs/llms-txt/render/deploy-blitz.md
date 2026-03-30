# Source: https://render.com/docs/deploy-blitz.md

# Deploy Blitz on Render

[Blitz](https://blitzjs.com) is a batteries-included framework that's inspired by Ruby on Rails and built on Next.js. It features a "zero-API" data layer abstraction that eliminates the need for REST/GraphQL.

## One-click deploy

<deploy-to-render repo="https://github.com/render-examples/blitzjs">
</deploy-to-render>

## Modify an existing Blitz project for Render

If you've been developing a Blitz project locally and are ready to deploy it to Render, follow these steps:

1. [Switch your project to use PostgreSQL](https://blitzjs.com/docs/database-overview#switch-to-postgre-sql) if you're currently using SQLite (or another database).
2. Add the YAML below to a `render.yaml` file at the root of your repo.
3. Commit and push your changes to GitHub/GitLab/Bitbucket.
4. [Deploy your code to Render](https://dashboard.render.com/select-repo?type=iac). If you haven't already, connect your GitHub/GitLab/Bitbucket account to Render.
5. Render will deploy your code as a web service, create a PostgreSQL instance, and configure the connection between them. Additionally, future pushes to your repo will automatically deploy your Render web service.

```yaml
services:
  - type: web
    name: blitzapp
    runtime: node
    plan: starter
    buildCommand: yarn --frozen-lockfile --prod=false &&
      blitz prisma generate &&
      blitz build &&
      blitz prisma migrate deploy
    startCommand: blitz start
    envVars:
      - key: NODE_ENV
        value: production
      - key: DATABASE_URL
        fromDatabase:
          name: blitzapp-db
          property: connectionString
      - key: SESSION_SECRET_KEY
        generateValue: true

databases:
  - name: blitzapp-db
    plan: starter
```

You may also find it helpful to review the commit history of the [repo used for the one-click deploy above](https://github.com/render-examples/blitzjs) to better understand these steps.