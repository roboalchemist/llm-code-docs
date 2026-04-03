# Source: https://developers.cloudflare.com/d1/llms.txt

# D1

Create managed, serverless databases with SQL semantics

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/d1/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [D1 llms-full.txt](https://developers.cloudflare.com/d1/llms-full.txt) for the complete D1 documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare D1](https://developers.cloudflare.com/d1/index.md)

## Getting started

- [Getting started](https://developers.cloudflare.com/d1/get-started/index.md)

## Workers Binding API

- [Workers Binding API](https://developers.cloudflare.com/d1/worker-api/index.md)
- [D1 Database](https://developers.cloudflare.com/d1/worker-api/d1-database/index.md)
- [Prepared statement methods](https://developers.cloudflare.com/d1/worker-api/prepared-statements/index.md)
- [Return objects](https://developers.cloudflare.com/d1/worker-api/return-object/index.md)

## Wrangler commands

- [Wrangler commands](https://developers.cloudflare.com/d1/wrangler-commands/index.md)

## REST API

- [REST API](https://developers.cloudflare.com/d1/d1-api/index.md)

## Examples

- [Examples](https://developers.cloudflare.com/d1/examples/index.md)
- [Query D1 from Hono](https://developers.cloudflare.com/d1/examples/d1-and-hono/index.md): Query D1 from the Hono web framework
- [Query D1 from Remix](https://developers.cloudflare.com/d1/examples/d1-and-remix/index.md): Query your D1 database from a Remix application.
- [Query D1 from SvelteKit](https://developers.cloudflare.com/d1/examples/d1-and-sveltekit/index.md): Query a D1 database from a SvelteKit application.
- [Export and save D1 database](https://developers.cloudflare.com/d1/examples/export-d1-into-r2/index.md)
- [Query D1 from Python Workers](https://developers.cloudflare.com/d1/examples/query-d1-from-python-workers/index.md): Learn how to query D1 from a Python Worker

## Tutorials

- [Tutorials](https://developers.cloudflare.com/d1/tutorials/index.md)
- [Build a Comments API](https://developers.cloudflare.com/d1/tutorials/build-a-comments-api/index.md): Use D1 to add comments to a static blog site. Create a D1 database and build a JSON API with Hono that allows the creation and retrieval of comments.
- [Build a Staff Directory Application](https://developers.cloudflare.com/d1/tutorials/build-a-staff-directory-app/index.md): Build a staff directory using D1. Users access employee info; admins add new employees within the app.
- [Build an API to access D1 using a proxy Worker](https://developers.cloudflare.com/d1/tutorials/build-an-api-to-access-d1/index.md): This tutorial shows how to create an API that allows you to securely run queries against a D1 database. The API can be used to customize access controls and/or limit what tables can be queried.
- [Query D1 using Prisma ORM](https://developers.cloudflare.com/d1/tutorials/d1-and-prisma-orm/index.md): This tutorial shows you how to set up and deploy a Cloudflare Worker that is accessing a D1 database from scratch.
- [Bulk import to D1 using REST API](https://developers.cloudflare.com/d1/tutorials/import-to-d1-with-rest-api/index.md): This tutorial uses the REST API to import a database into D1.
- [Using D1 Read Replication for your e-commerce website](https://developers.cloudflare.com/d1/tutorials/using-read-replication-for-e-com/index.md): D1 Read Replication is a feature that allows you to replicate your D1 database to multiple regions. This is useful for your e-commerce website, as it reduces read latencies and improves read throughput.

## Demos and architectures

- [Demos and architectures](https://developers.cloudflare.com/d1/demos/index.md)

## best-practices

- [Import and export data](https://developers.cloudflare.com/d1/best-practices/import-export-data/index.md)
- [Local development](https://developers.cloudflare.com/d1/best-practices/local-development/index.md)
- [Query a database](https://developers.cloudflare.com/d1/best-practices/query-d1/index.md)
- [Global read replication](https://developers.cloudflare.com/d1/best-practices/read-replication/index.md)
- [Remote development](https://developers.cloudflare.com/d1/best-practices/remote-development/index.md)
- [Retry queries](https://developers.cloudflare.com/d1/best-practices/retry-queries/index.md)
- [Use D1 from Pages](https://developers.cloudflare.com/d1/best-practices/use-d1-from-pages/index.md)
- [Use indexes](https://developers.cloudflare.com/d1/best-practices/use-indexes/index.md)

## configuration

- [Data location](https://developers.cloudflare.com/d1/configuration/data-location/index.md)
- [Environments](https://developers.cloudflare.com/d1/configuration/environments/index.md)

## observability

- [Audit Logs](https://developers.cloudflare.com/d1/observability/audit-logs/index.md)
- [Billing](https://developers.cloudflare.com/d1/observability/billing/index.md)
- [Debug D1](https://developers.cloudflare.com/d1/observability/debug-d1/index.md)
- [Metrics and analytics](https://developers.cloudflare.com/d1/observability/metrics-analytics/index.md)

## platform

- [Alpha database migration guide](https://developers.cloudflare.com/d1/platform/alpha-migration/index.md)
- [Limits](https://developers.cloudflare.com/d1/platform/limits/index.md)
- [Pricing](https://developers.cloudflare.com/d1/platform/pricing/index.md)
- [Release notes](https://developers.cloudflare.com/d1/platform/release-notes/index.md)
- [Choose a data or storage product](https://developers.cloudflare.com/d1/platform/storage-options/index.md)

## reference

- [Backups (Legacy)](https://developers.cloudflare.com/d1/reference/backups/index.md)
- [Community projects](https://developers.cloudflare.com/d1/reference/community-projects/index.md)
- [Data security](https://developers.cloudflare.com/d1/reference/data-security/index.md)
- [FAQs](https://developers.cloudflare.com/d1/reference/faq/index.md)
- [Generated columns](https://developers.cloudflare.com/d1/reference/generated-columns/index.md)
- [Glossary](https://developers.cloudflare.com/d1/reference/glossary/index.md)
- [Migrations](https://developers.cloudflare.com/d1/reference/migrations/index.md)
- [Time Travel and backups](https://developers.cloudflare.com/d1/reference/time-travel/index.md)

## sql-api

- [Define foreign keys](https://developers.cloudflare.com/d1/sql-api/foreign-keys/index.md)
- [Query JSON](https://developers.cloudflare.com/d1/sql-api/query-json/index.md)
- [SQL statements](https://developers.cloudflare.com/d1/sql-api/sql-statements/index.md)