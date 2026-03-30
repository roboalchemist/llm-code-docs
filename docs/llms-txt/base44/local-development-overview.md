# Source: https://docs.base44.com/developers/backend/overview/local-dev/local-development-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Local development

> Develop and test your backend project locally with base44 dev

Local development lets you run your backend project on your own machine so you can test changes instantly, inspect data without affecting production, and catch issues before deploying.

See [Setup](/developers/backend/overview/local-dev/get-started) for prerequisites and step-by-step instructions.

## What runs locally

The dev server handles these features entirely on your machine:

* **[Functions](#functions):** Backend functions run locally with automatic reload on file changes.
* **[Entities](#entities):** Entity data is stored in a local in-memory database. Schema changes are picked up automatically.
* **[Media](#media):** File uploads are saved locally.

<Note>
  Function
  [automations](/developers/backend/resources/backend-functions/automations)
  don't run locally.
</Note>

## What's forwarded

Some features aren't handled locally yet. When the dev server receives a request it can't serve, it forwards it to your deployed app so the call still works. The server logs a warning each time this happens.

Forwarded features include:

* **Authentication:** OAuth and login routes are redirected to Base44 so session cookies work correctly.
* **User entity:** Reads from the `User` entity always go to production.
* **Core integrations:** Endpoints like `SendEmail` or AI generation are forwarded. File uploads are the exception and run locally.
* **Custom integrations:** API calls configured through OpenAPI specifications.

This means your app continues to work end-to-end during development. Features that run locally use local data, and everything else uses production.

## Functions

Backend functions run locally on your machine. You can call them from your frontend just like deployed functions.

* Each function runs as a separate [Deno](https://docs.deno.com/runtime/) process, which must be [installed separately](https://docs.deno.com/runtime/getting_started/installation/).
* Functions reload automatically when you edit the source code.
* Function output is printed directly to your terminal. You don't need to use [`base44 logs`](/developers/references/cli/commands/logs) during local development.

<Note>
  The first request to a function may be slower because the dev server starts
  the process on demand. Subsequent requests reuse the running process.
</Note>

## Entities

Entity operations go to a local in-memory database instead of the remote database. This lets you create, read, update, and delete records without affecting your production data.

* All data is stored in memory and is cleared when you stop the dev server.
* Schema changes are picked up automatically. Changing an entity schema clears all in-memory data for that entity.
* Realtime subscriptions work locally. If your frontend uses `entities.subscribe()`, it receives events for local entity changes.
* The `User` entity is a special case. Reads are always forwarded to the production backend because user records are managed by Base44's authentication system.

## Media

File uploads are handled locally so you can test media features without uploading to production storage. Files are saved to a temporary directory and cleaned up when the dev server stops. The maximum file size is 50 MB.

## See also

* [Setup](/developers/backend/overview/local-dev/get-started): Prerequisites and step-by-step instructions
* [Backend functions](/developers/backend/resources/backend-functions/overview): Write serverless functions that run on Base44's infrastructure
* [Entities](/developers/backend/resources/entities/overview): Define data models for your app
* [Project structure](/developers/backend/overview/project-structure): How project files are organized


Built with [Mintlify](https://mintlify.com).