# Source: https://developers.cloudflare.com/containers/llms.txt

# Containers

Enhance your Workers with serverless containers

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/containers/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Containers llms-full.txt](https://developers.cloudflare.com/containers/llms-full.txt) for the complete Containers documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Containers (Beta)](https://developers.cloudflare.com/containers/index.md)

## Getting started

- [Getting started](https://developers.cloudflare.com/containers/get-started/index.md)

## Examples

- [Examples](https://developers.cloudflare.com/containers/examples/index.md)
- [Static Frontend, Container Backend](https://developers.cloudflare.com/containers/examples/container-backend/index.md): A simple frontend app with a containerized backend
- [Cron Container](https://developers.cloudflare.com/containers/examples/cron/index.md): Running a container on a schedule using Cron Triggers
- [Using Durable Objects Directly](https://developers.cloudflare.com/containers/examples/durable-object-interface/index.md): Various examples calling Containers directly from Durable Objects
- [Env Vars and Secrets](https://developers.cloudflare.com/containers/examples/env-vars-and-secrets/index.md): Pass in environment variables and secrets to your container
- [Mount R2 buckets with FUSE](https://developers.cloudflare.com/containers/examples/r2-fuse-mount/index.md): Mount R2 buckets as filesystems using FUSE in Containers
- [Stateless Instances](https://developers.cloudflare.com/containers/examples/stateless/index.md): Run multiple instances across Cloudflare's network
- [Status Hooks](https://developers.cloudflare.com/containers/examples/status-hooks/index.md): Execute Workers code in reaction to Container status changes
- [Websocket to Container](https://developers.cloudflare.com/containers/examples/websocket/index.md): Forwarding a Websocket request to a Container

## Platform Reference

- [Platform Reference](https://developers.cloudflare.com/containers/platform-details/architecture/index.md)
- [Lifecycle of a Container](https://developers.cloudflare.com/containers/platform-details/architecture/index.md)
- [Durable Object Interface](https://developers.cloudflare.com/containers/platform-details/durable-object-methods/index.md)
- [Environment Variables](https://developers.cloudflare.com/containers/platform-details/environment-variables/index.md)
- [Image Management](https://developers.cloudflare.com/containers/platform-details/image-management/index.md): Learn how to use Cloudflare Registry, Docker Hub, and Amazon ECR images with Containers.
- [Limits and Instance Types](https://developers.cloudflare.com/containers/platform-details/limits/index.md)
- [Handle outbound traffic](https://developers.cloudflare.com/containers/platform-details/outbound-traffic/index.md): Intercept and handle outbound HTTP from containers using Workers.
- [Rollouts](https://developers.cloudflare.com/containers/platform-details/rollouts/index.md)
- [Scaling and Routing](https://developers.cloudflare.com/containers/platform-details/scaling-and-routing/index.md)

## Container Package

- [Container Package](https://developers.cloudflare.com/containers/container-package/index.md)

## Local Development

- [Local Development](https://developers.cloudflare.com/containers/local-dev/index.md): Learn how to run Container-enabled Workers locally with `wrangler dev` and `vite dev`.

## Wrangler Configuration

- [Wrangler Configuration](https://developers.cloudflare.com/containers/wrangler-configuration/index.md)

## Wrangler Commands

- [Wrangler Commands](https://developers.cloudflare.com/containers/wrangler-commands/index.md)

## Beta Info & Roadmap

- [Beta Info & Roadmap](https://developers.cloudflare.com/containers/beta-info/index.md)

## Frequently Asked Questions

- [Frequently Asked Questions](https://developers.cloudflare.com/containers/faq/index.md)

## SSH

- [SSH](https://developers.cloudflare.com/containers/ssh/index.md): Connect to running container instances with SSH.

## Pricing

- [Pricing](https://developers.cloudflare.com/containers/pricing/index.md)