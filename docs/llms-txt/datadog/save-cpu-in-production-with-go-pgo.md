# Source: https://docs.datadoghq.com/profiler/guide/save-cpu-in-production-with-go-pgo.md

---
title: Go - Save up to 14% CPU in Production with Profile-Guided Optimization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Profiler > Continuous Profiler Guides > Go - Save up to 14%
  CPU in Production with Profile-Guided Optimization
source_url: https://docs.datadoghq.com/guide/save-cpu-in-production-with-go-pgo/index.html
---

# Go - Save up to 14% CPU in Production with Profile-Guided Optimization

## Overview{% #overview %}

Starting with [Go 1.21](https://tip.golang.org/doc/go1.21), the Go compiler supports profile-guided optimization (PGO).

PGO enables additional optimizations on code identified as hot by CPU profiles of production workloads. This is compatible with [Datadog Go Continuous Profiler](https://docs.datadoghq.com/profiler/enabling/go) and can be used for production builds.

## How PGO works{% #how-pgo-works %}

Here are some key points about how PGO works:

- Building a Go program with PGO enabled causes the compiler to look for a pprof CPU profile named `default.pgo` and use it to produce a more optimized binary.
- Typical programs should see a 2-14% decrease in CPU time after optimization. PGO remains under active development, and future versions of Go aim to achieve even greater CPU savings. Datadog is [actively supporting this initiative](https://github.com/golang/go/issues/65532).
- PGO produces the best results when using representative profiles. However, using non-representative or old profiles (from previous versions of the software) is not expected to result in slower binaries compared to not using PGO.
- Using a profile from a PGO optimized application is not expected to cause optimization/deoptimization cycles. This is referred to as iterative stability.

For more information, see the [Go PGO documentation](https://go.dev/doc/pgo).

## Enabling PGO{% #enabling-pgo %}

PGO is a standard Go compiler option that you can use by manually downloading profiles from Datadog. Datadog built a tool, `datadog-pgo` to help you enable PGO on all services, using the latest and most representative profiles.

To enable PGO using the `datadog-pgo` tool:

1. Create a dedicated API key and an application key scoped to at least `continuous_profiler_pgo_read` as described in [API and Application Keys](https://docs.datadoghq.com/account_management/api-app-keys).

1. Set `DD_API_KEY`, `DD_APP_KEY`, and `DD_SITE` with the environment secret mechanism of your CI provider.

1. Run `datadog-pgo` before your build step. For example, for a service `foo` that runs in `prod` and has its main package in `./cmd/foo`, you should add this step:

   ```
   go run github.com/DataDog/datadog-pgo@latest "service:foo env:prod" ./cmd/foo/default.pgo
   ```

The Go toolchain automatically picks up any `default.pgo` file in the main package, so you don't need to modify your `go build` step.

See the [datadog-pgo GitHub repository](https://github.com/DataDog/datadog-pgo?tab=readme-ov-file#getting-started) for more details.

## Checking if PGO is enabled{% #checking-if-pgo-is-enabled %}

To check where PGO is enabled, search for [Go profiles without pgo tag set to true](https://app.datadoghq.com/profiling/explorer?query=runtime%3Ago%20-pgo%3Atrue%20&viz=stream).

The `pgo` tag was implemented in dd-trace-go 1.61.0, so any profiles prior to this version will not have `pgo:false`.

## Further reading{% #further-reading %}

- [Datadog Continuous Profiler](https://docs.datadoghq.com/profiler)
- [Comparing Profiles](https://docs.datadoghq.com/profiler/compare_profiles/)
