# Source: https://docs.nhost.io/products/functions/

Title: Overview

URL Source: https://docs.nhost.io/products/functions/

Markdown Content:
functions serverless lambda API endpoints backend webhooks event triggers TypeScript JavaScript routing deployment environment variables

Nhost Functions are server-side JavaScript or TypeScript functions that are deployed as HTTP endpoints. They are a great option for handling Event Triggers, integrating with external services like Stripe or Slack, and building custom API logic.

How Functions Work
------------------

[Section titled “How Functions Work”](https://docs.nhost.io/products/functions/#how-functions-work)

Each `.js` or `.ts` file you place in the `./functions` directory of your project becomes an HTTP endpoint. A function exports a default handler that receives an Express `Request` and `Response`:

`import type { Request, Response } from 'express'export default (req: Request, res: Response) => {  res.status(200).send('Hello World!')}`

Endpoints are generated based on the file path relative to `./functions`:

| File | HTTP Endpoint |
| --- | --- |
| `functions/index.js` | `https://[subdomain].functions.[region].nhost.run/v1/` |
| `functions/users/index.ts` | `https://[subdomain].functions.[region].nhost.run/v1/users` |
| `functions/users/active.ts` | `https://[subdomain].functions.[region].nhost.run/v1/users/active` |
| `functions/my-company.js` | `https://[subdomain].functions.[region].nhost.run/v1/my-company` |

All HTTP methods (GET, POST, PUT, DELETE, etc.) are routed to the same handler. Use `req.method` to differentiate.

### Directory Conventions

[Section titled “Directory Conventions”](https://docs.nhost.io/products/functions/#directory-conventions)

*   Files and folders prefixed with an **underscore** (`_`) are ignored and not exposed as endpoints. Use this for shared utilities.
*   `index` files map to the parent directory path.

Request and Response
--------------------

[Section titled “Request and Response”](https://docs.nhost.io/products/functions/#request-and-response)

Functions receive standard Express `Request` and `Response` objects with a few additions:

| Property | Description |
| --- | --- |
| `req.method` | HTTP method (GET, POST, etc.) |
| `req.headers` | Request headers |
| `req.query` | Parsed query string parameters |
| `req.body` | Parsed request body (JSON, form data) |
| `req.rawBody` | Raw request body as a Buffer |
| `req.invocationId` | Unique identifier for this function invocation |

The `invocationId` is useful for correlating [logs](https://docs.nhost.io/products/functions/logging) across a single invocation.

Environment Variables
---------------------

[Section titled “Environment Variables”](https://docs.nhost.io/products/functions/#environment-variables)

The following environment variables are automatically injected into your functions at runtime:

| Variable | Description |
| --- | --- |
| `NHOST_ADMIN_SECRET` | Admin secret for your project |
| `NHOST_WEBHOOK_SECRET` | Webhook secret for your project |
| `NHOST_JWT_SECRET` | JWT secret configuration (JSON string) |
| `NHOST_SUBDOMAIN` | Project subdomain |
| `NHOST_REGION` | Project region |
| `NHOST_HASURA_URL` | Internal Hasura URL |
| `NHOST_AUTH_URL` | Internal Auth URL |
| `NHOST_GRAPHQL_URL` | Internal GraphQL URL |
| `NHOST_STORAGE_URL` | Internal Storage URL |
| `NHOST_FUNCTIONS_URL` | Internal Functions URL |

Any [custom environment variables](https://docs.nhost.io/platform/cloud/environment-variables) you define are also available.

Functions are deployed automatically when you push to the connected GitHub repository. Nhost computes checksums for your functions and their dependencies, so unchanged functions are skipped during deployment.

Nhost detects your package manager based on the lockfile present in the functions folder or a parent folder. See [Runtimes and Dependencies](https://docs.nhost.io/products/functions/runtimes) for details.

Functions are billed per GB-sec or GB-hour. 1 GB-hour is 3600 GB-seconds.

1 GB-sec is 1 function with 1 GB of RAM running for 1 second. If 1 function with 1 GB of RAM runs for 3600 seconds, that equals 1 GB-hour.
