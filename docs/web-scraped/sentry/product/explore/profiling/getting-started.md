---
---
title: Set Up
description: "Get started with Profiling, which allows you to see code-level profiling information for your Sentry apps."
---

Continuous Profiling and UI Profiling are the latest iteration of Sentry’s profiling capabilities, but they are currently only supported in select SDKs as described below.

Other platforms are supported via the prior transaction-based Profiling product, but these will not benefit from new capabilities introduced by Continuous and UI Profiling (direct start/stop control over the profile lifecycle and removal of duration limits). For more information on the differences between transaction-based Profiling and Continuous/UI Profiling, read [this documentation](/product/explore/profiling/transaction-vs-continuous-profiling).

If you are currently using transaction-based Profiling and want to migrate to Continuous Profiling or UI Profiling on a supported SDK, read the [migration guide](/product/explore/profiling/continuous-ui-profiling-migration-guide).

All SDKs that currently support transaction-based Profiling will be migrated over time to support Continuous Profiling and UI Profiling.

## Supported SDKs

### Continuous Profiling

Continuous Profiling can be used both independently and as a complement to the tracing product.

- 
- 

### UI Profiling

UI Profiling can be used both independently and as a complement to the tracing product.

- 
- 
- 
- 

### Transaction-based Profiling

If Continuous Profiling or UI Profiling are not supported on your SDK, you can fall back to the older transaction-based Profiling implementation for the platforms below.

Transaction-based Profiling requires Sentry's tracing product being enabled beforehand. To enable tracing and performance monitoring features in the SDK, check out our [Insights guide](/product/insights/).

#### Mobile

- 
- 
- 

#### Standalone and server apps

- 
- 
- 
