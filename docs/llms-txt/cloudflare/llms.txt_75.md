# Source: https://developers.cloudflare.com/queues/llms.txt

# Queues

Reliably send and receive messages without the egress fees

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/queues/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Queues llms-full.txt](https://developers.cloudflare.com/queues/llms-full.txt) for the complete Queues documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Queues](https://developers.cloudflare.com/queues/index.md)

## Getting started

- [Getting started](https://developers.cloudflare.com/queues/get-started/index.md)

## Event subscriptions

- [Event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/index.md): Subscribe to events from Cloudflare services to build custom workflows, integrations, and logic with Workers.
- [Events & schemas](https://developers.cloudflare.com/queues/event-subscriptions/events-schemas/index.md)
- [Manage event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/index.md): Learn how to create, view, and delete event subscriptions for your queues.

## Examples

- [Examples](https://developers.cloudflare.com/queues/examples/index.md)
- [List and acknowledge messages from the dashboard](https://developers.cloudflare.com/queues/examples/list-messages-from-dash/index.md): Use the dashboard to fetch and acknowledge the messages currently in a queue.
- [Publish to a Queue via HTTP](https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/index.md): Publish to a Queue directly via HTTP and Workers.
- [Publish to a Queue via Workers](https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-workers/index.md): Publish to a Queue directly from your Worker.
- [Use Queues to store data in R2](https://developers.cloudflare.com/queues/examples/send-errors-to-r2/index.md): Example of how to use Queues to batch data and store it in an R2 bucket.
- [Send messages from the dashboard](https://developers.cloudflare.com/queues/examples/send-messages-from-dash/index.md): Use the dashboard to send messages to a queue.
- [Serverless ETL pipelines](https://developers.cloudflare.com/queues/examples/serverless-etl/index.md)
- [Use Queues from Durable Objects](https://developers.cloudflare.com/queues/examples/use-queues-with-durable-objects/index.md): Publish to a queue from within a Durable Object.

## Tutorials

- [Tutorials](https://developers.cloudflare.com/queues/tutorials/index.md)
- [Handle rate limits of external APIs](https://developers.cloudflare.com/queues/tutorials/handle-rate-limits/index.md): Example of how to use Queues to handle rate limits of external APIs.
- [Build a web crawler with Queues and Browser Rendering](https://developers.cloudflare.com/queues/tutorials/web-crawler-with-browser-rendering/index.md): Example of how to use Queues and Browser Rendering to power a web crawler.

## Demos and architectures

- [Demos and architectures](https://developers.cloudflare.com/queues/demos/index.md)

## Glossary

- [Glossary](https://developers.cloudflare.com/queues/glossary/index.md)

## Queues REST API

- [Queues REST API](https://developers.cloudflare.com/queues/queues-api/index.md)

## configuration

- [Batching, Retries and Delays](https://developers.cloudflare.com/queues/configuration/batching-retries/index.md)
- [Configure Queues](https://developers.cloudflare.com/queues/configuration/configure-queues/index.md)
- [Consumer concurrency](https://developers.cloudflare.com/queues/configuration/consumer-concurrency/index.md)
- [Dead Letter Queues](https://developers.cloudflare.com/queues/configuration/dead-letter-queues/index.md)
- [R2 Event Notifications](https://developers.cloudflare.com/queues/configuration/event-notifications/index.md)
- [JavaScript APIs](https://developers.cloudflare.com/queues/configuration/javascript-apis/index.md)
- [Local Development](https://developers.cloudflare.com/queues/configuration/local-development/index.md)
- [Pause and Purge](https://developers.cloudflare.com/queues/configuration/pause-purge/index.md)
- [Pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/index.md)

## observability

- [Metrics](https://developers.cloudflare.com/queues/observability/metrics/index.md)

## platform

- [Audit Logs](https://developers.cloudflare.com/queues/platform/audit-logs/index.md)
- [Changelog](https://developers.cloudflare.com/queues/platform/changelog/index.md)
- [Limits](https://developers.cloudflare.com/queues/platform/limits/index.md)
- [Pricing](https://developers.cloudflare.com/queues/platform/pricing/index.md)
- [Choose a data or storage product](https://developers.cloudflare.com/queues/platform/storage-options/index.md)

## reference

- [Delivery guarantees](https://developers.cloudflare.com/queues/reference/delivery-guarantees/index.md)
- [Error codes](https://developers.cloudflare.com/queues/reference/error-codes/index.md)
- [How Queues Works](https://developers.cloudflare.com/queues/reference/how-queues-works/index.md)
- [Wrangler commands](https://developers.cloudflare.com/queues/reference/wrangler-commands/index.md)