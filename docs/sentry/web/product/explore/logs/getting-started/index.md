---
---
title: Set Up
description: "Learn how to set up Sentry's Logs feature using our supported SDKs."
---

To set up Sentry Logs, use the links below for supported SDKs. After it's been set up, you'll be able to view and query logs and parameters sent from your applications within Sentry.

## Supported SDKs

### JavaScript

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

### Java

- 
- 
- 

### Mobile

- 
- 
- 
- 
- 

### PHP

- 
- 
- 

### Python

- 

### Ruby

- 
- 

### Go

- 

### Rust

- 

### .NET

- 
- 
- 
- 
- 

### Native

- 

### Gaming

- 
- 
- 

## Upcoming SDKs

We're actively working on adding Log functionality to additional SDKs. Check out these GitHub issues for the latest updates:

- 

If you don't see your platform listed above, please reach out to us on [GitHub](https://github.com/getsentry/sentry/discussions/86804) or [Discord](https://discord.gg/sentry), we'll get it prioritized!

## Log Drains

Log drains allow you to forward logs from platforms like Vercel, Cloudflare, Heroku, and Supabase directly to Sentry without modifying your application code. Learn more about [log and trace drains](/product/drains/).

### Supported Platform Integrations

- **[Vercel](/product/drains/integration/vercel/)**: Forward runtime, build, and static logs from Vercel deployments
- **[Cloudflare](/product/drains/integration/cloudflare/)**: Forward logs from Cloudflare Workers
- **[Heroku](/product/drains/integration/heroku/)**: Forward logs from Heroku apps using telemetry drains
- **[Supabase](/product/drains/integration/supabase/)**: Forward logs from your Supabase stack

We are actively working on adding support for more platforms, which we are tracking in [this GitHub issue](https://github.com/getsentry/sentry/issues/91726).

### OpenTelemetry (OTLP) Endpoint

You can also send logs to Sentry via [Sentry's OpenTelemetry (OTLP) Logs endpoint](/concepts/otlp/#opentelemetry-logs). This can be used with any OpenTelemetry SDK, or with the [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) to send logs to Sentry. This is useful if you're already using OpenTelemetry instrumentation or want to route logs through an OTLP collector.
