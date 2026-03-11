# Source: https://manifest.build/docs/contributing.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://manifest.build/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Contributing

> Get the development environment up and running

## Tech stack

| Layer    | Technology                          |
| -------- | ----------------------------------- |
| Frontend | SolidJS                             |
| Backend  | NestJS                              |
| Database | sql.js (local) / PostgreSQL (cloud) |
| Auth     | Better Auth                         |
| Build    | Turborepo                           |

## Prerequisites

* Node.js 22.x
* npm 10.x

## Dev setup

<Tabs>
  <Tab title="Cloud">
    <Steps>
      <Step title="Clone and install">
        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
        git clone https://github.com/mnfst/manifest.git
        cd manifest
        npm install
        ```
      </Step>

      <Step title="Start PostgreSQL">
        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
        docker run -d --name postgres_db \
          -e POSTGRES_USER=myuser \
          -e POSTGRES_PASSWORD=mypassword \
          -e POSTGRES_DB=mydatabase \
          -p 5432:5432 postgres:16
        ```
      </Step>

      <Step title="Configure environment">
        Copy `.env.example` to `.env` and fill in:

        * `BETTER_AUTH_SECRET` — any random string
        * `DATABASE_URL` — `postgres://myuser:mypassword@localhost:5432/mydatabase`
        * `SEED_DATA=true`
      </Step>

      <Step title="Start the backend">
        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
        cd packages/backend
        NODE_OPTIONS='-r dotenv/config' npx nest start --watch
        ```
      </Step>

      <Step title="Start the frontend">
        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
        cd packages/frontend
        npx vite
        ```
      </Step>

      <Step title="Login">
        Use `admin@manifest.build` / `manifest`.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Local">
    <Steps>
      <Step title="Clone and install">
        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
        git clone https://github.com/mnfst/manifest.git
        cd manifest
        npm install
        ```
      </Step>

      <Step title="Build">
        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
        npm run build
        ```
      </Step>

      <Step title="Run">
        ```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
        MANIFEST_MODE=local node packages/backend/dist/main.js
        ```
      </Step>

      <Step title="Open the dashboard">
        Open [http://127.0.0.1:3001](http://127.0.0.1:3001). No login needed.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Running tests

```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Jest unit tests
npm test --workspace=packages/backend

# Jest e2e tests
npm run test:e2e --workspace=packages/backend

# Vitest frontend tests
npm test --workspace=packages/frontend
```

## Database migrations

Cloud mode only. Local mode uses `synchronize: true` — no migrations needed.

```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
cd packages/backend
npm run migration:generate -- src/database/migrations/DescriptiveName
npm run migration:run
```

## Changesets

Every PR needs a changeset. Backend/frontend changes need a `manifest` changeset.

```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Add a changeset
npx changeset

# For docs/CI-only changes
npx changeset add --empty
```

## Links

* [GitHub Issues](https://github.com/mnfst/manifest/issues)
* [Discord](https://discord.gg/FepAked3W7)
* [Code of Conduct](https://github.com/mnfst/manifest/blob/main/CODE_OF_CONDUCT.md)

Built with [Mintlify](https://mintlify.com).
