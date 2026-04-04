# Source: https://developers.cloudflare.com/sandbox/llms.txt

# Sandbox SDK

Build secure, isolated code execution environments

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/sandbox/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Sandbox SDK llms-full.txt](https://developers.cloudflare.com/sandbox/llms-full.txt) for the complete Sandbox SDK documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Sandbox SDK (Beta)](https://developers.cloudflare.com/sandbox/index.md)

## Getting started

- [Getting started](https://developers.cloudflare.com/sandbox/get-started/index.md)

## Tutorials

- [Tutorials](https://developers.cloudflare.com/sandbox/tutorials/index.md)
- [Build an AI code executor](https://developers.cloudflare.com/sandbox/tutorials/ai-code-executor/index.md): Use Claude to generate Python code from natural language and execute it securely in sandboxes.
- [Analyze data with AI](https://developers.cloudflare.com/sandbox/tutorials/analyze-data-with-ai/index.md): Upload CSV files, generate analysis code with Claude, and return visualizations.
- [Automated testing pipeline](https://developers.cloudflare.com/sandbox/tutorials/automated-testing-pipeline/index.md): Build a testing pipeline that clones Git repositories, installs dependencies, runs tests, and reports results.
- [Run Claude Code on a Sandbox](https://developers.cloudflare.com/sandbox/tutorials/claude-code/index.md): Use Claude Code to implement a task in your GitHub repository.
- [Build a code review bot](https://developers.cloudflare.com/sandbox/tutorials/code-review-bot/index.md): Clone repositories, analyze code with Claude, and post review comments to GitHub PRs.
- [Data persistence with R2](https://developers.cloudflare.com/sandbox/tutorials/persistent-storage/index.md): Mount R2 buckets as local filesystem paths to persist data across sandbox lifecycles.
- [Code interpreter with Workers AI](https://developers.cloudflare.com/sandbox/tutorials/workers-ai-code-interpreter/index.md): Build a code interpreter using Workers AI GPT-OSS model with the official workers-ai-provider package.

## API Reference

- [API Reference](https://developers.cloudflare.com/sandbox/api/index.md)
- [Backups](https://developers.cloudflare.com/sandbox/api/backups/index.md)
- [Commands](https://developers.cloudflare.com/sandbox/api/commands/index.md)
- [File Watching](https://developers.cloudflare.com/sandbox/api/file-watching/index.md)
- [Files](https://developers.cloudflare.com/sandbox/api/files/index.md)
- [Code Interpreter](https://developers.cloudflare.com/sandbox/api/interpreter/index.md)
- [Lifecycle](https://developers.cloudflare.com/sandbox/api/lifecycle/index.md)
- [Ports](https://developers.cloudflare.com/sandbox/api/ports/index.md)
- [Sessions](https://developers.cloudflare.com/sandbox/api/sessions/index.md)
- [Storage](https://developers.cloudflare.com/sandbox/api/storage/index.md)
- [Terminal](https://developers.cloudflare.com/sandbox/api/terminal/index.md): Connect browser-based terminal UIs to sandbox shells via WebSocket.

## How-to guides

- [How-to guides](https://developers.cloudflare.com/sandbox/guides/index.md)
- [Run background processes](https://developers.cloudflare.com/sandbox/guides/background-processes/index.md): Start and manage long-running services and applications.
- [Backup and restore](https://developers.cloudflare.com/sandbox/guides/backup-restore/index.md): Create point-in-time backups and restore sandbox directories.
- [Browser terminals](https://developers.cloudflare.com/sandbox/guides/browser-terminals/index.md): Connect browser-based terminals to sandbox shells using xterm.js or raw WebSockets.
- [Use code interpreter](https://developers.cloudflare.com/sandbox/guides/code-execution/index.md): Execute Python and JavaScript code with rich outputs.
- [Run Docker-in-Docker](https://developers.cloudflare.com/sandbox/guides/docker-in-docker/index.md): Run Docker commands inside a sandbox container.
- [Execute commands](https://developers.cloudflare.com/sandbox/guides/execute-commands/index.md): Run commands with streaming output, error handling, and shell access.
- [Expose services](https://developers.cloudflare.com/sandbox/guides/expose-services/index.md): Create preview URLs and expose ports for web services.
- [Watch filesystem changes](https://developers.cloudflare.com/sandbox/guides/file-watching/index.md): Monitor files and directories in real-time to build responsive development tools and automation workflows.
- [Work with Git](https://developers.cloudflare.com/sandbox/guides/git-workflows/index.md): Clone repositories, manage branches, and automate Git operations.
- [Manage files](https://developers.cloudflare.com/sandbox/guides/manage-files/index.md): Read, write, organize, and synchronize files in the sandbox.
- [Mount buckets](https://developers.cloudflare.com/sandbox/guides/mount-buckets/index.md): Mount S3-compatible object storage as local filesystems for persistent data storage.
- [Handle outbound traffic](https://developers.cloudflare.com/sandbox/guides/outbound-traffic/index.md): Intercept and handle outbound HTTP from sandboxes using Workers.
- [Deploy to Production](https://developers.cloudflare.com/sandbox/guides/production-deployment/index.md): Set up custom domains for preview URLs in production.
- [Proxy requests to external APIs](https://developers.cloudflare.com/sandbox/guides/proxy-requests/index.md): Keep credentials secure by routing sandbox requests through a Worker proxy that injects authentication at request time.
- [Stream output](https://developers.cloudflare.com/sandbox/guides/streaming-output/index.md): Handle real-time output from commands and processes.
- [WebSocket Connections](https://developers.cloudflare.com/sandbox/guides/websocket-connections/index.md): Connect to WebSocket servers running in sandboxes.

## Concepts

- [Concepts](https://developers.cloudflare.com/sandbox/concepts/index.md)
- [Architecture](https://developers.cloudflare.com/sandbox/concepts/architecture/index.md)
- [Container runtime](https://developers.cloudflare.com/sandbox/concepts/containers/index.md)
- [Preview URLs](https://developers.cloudflare.com/sandbox/concepts/preview-urls/index.md)
- [Sandbox lifecycle](https://developers.cloudflare.com/sandbox/concepts/sandboxes/index.md)
- [Security model](https://developers.cloudflare.com/sandbox/concepts/security/index.md)
- [Session management](https://developers.cloudflare.com/sandbox/concepts/sessions/index.md)
- [Terminal connections](https://developers.cloudflare.com/sandbox/concepts/terminal/index.md)

## Configuration

- [Configuration](https://developers.cloudflare.com/sandbox/configuration/index.md)
- [Dockerfile reference](https://developers.cloudflare.com/sandbox/configuration/dockerfile/index.md)
- [Environment variables](https://developers.cloudflare.com/sandbox/configuration/environment-variables/index.md)
- [Sandbox options](https://developers.cloudflare.com/sandbox/configuration/sandbox-options/index.md)
- [Transport modes](https://developers.cloudflare.com/sandbox/configuration/transport/index.md)
- [Wrangler configuration](https://developers.cloudflare.com/sandbox/configuration/wrangler/index.md)

## Platform

- [Platform](https://developers.cloudflare.com/sandbox/platform/index.md)
- [Beta Information](https://developers.cloudflare.com/sandbox/platform/beta-info/index.md)
- [Limits](https://developers.cloudflare.com/sandbox/platform/limits/index.md)
- [Pricing](https://developers.cloudflare.com/sandbox/platform/pricing/index.md)